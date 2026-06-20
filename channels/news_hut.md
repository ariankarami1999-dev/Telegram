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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 00:17:24</div>
<hr>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDvExEj6VyEL5MQn1yCKVV6x1fr744oWSmzzRmKISzQWR25outQK05LGQKSsmt06C8LtvzJQVNY321hlCZvss6NicRHTlF7H9TiS2znZ_v_MFWuT7J9oZZn2YNhqyRgLaFkHiZzJaDLi25tJLC82uwiC-jUqOaIwBHtqRnQ8oAo5JsLIkUXWJNW9nCKrh5sA2EUMjTlYTt8wNqQEW8mdmUJ5YoRmXGSBi27PwBhnzpg5cEPijD8QacO1zQIGq8OhLZP8BBi-fgUMlVuZLcQcGb6sVc3FEkARxqx4M-6ZTEIx7QiBahuWvWdcJ5RqQImmOilyQsmEBK1qC-Bzm5Z9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2UAvyY0mxAROgLu6cO3upEUYkjNQyQXjQQYnFxICr1txAzDhz4FTBIV8DcxzYGzjDluXNK4-fu9fN3C4bIaxmYoU0P8vmwNKqPx4zt9ngpcbDi9wUATIHI0HjRRo7XyFkJO7RAVXiCpZ1s5QQBJaNIruAe5f-1u7DWA4u02IQx-FuefoIG3RW4Pn8wrVv2Cz_9ru7WdFZH4KRBe7TDI65QjrWlOelqIenHEDF-SY4gAu-kOG5PfQi-lywdIXTPRJEt72ddWDckFmbepsr6oJOwi9gEJAcb6sc1_kBsHK606n8xH1sI17RN0BH8fLqdJk_fR8Auv0eIDlx-qTKaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB7ELjcqDxXK1CnVtX-OkMBsxpzt40Gasgj2J-d0DNQtVGeQEPUrpTK661JDz5-Y-hjthsWd_QfeDJvd5Srw6foSWbfQE_lup1s_6JUbggOf3oKfxAnPhn2rASisDkho74nXnhyPMPY9NXekBrQmHSEmfqNvAJPdf1Jw-ZJASo48HJLV_BnTjr3l3CYdlHhtUjEF-2ciWMdRFzWzHKpDzitTycN8TUR9DmyIG6Z1UDFP6X4dW0Z2e_9YLO7Chqbt9k3CxgWGxe5sevtz-N9czNJbRI3lvGMON74Cw060HJ0dxVW2gthkKkfmSjWUX03rMAdl3Tg3nI2rXyEQOL1juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUGVl9CLfy37So5sqBBMYbxXLuD9sCzFw6LinaXl-7w3ouprur9EyLxezhCtXSUdbfg2oUjplZ_X0oHAvAtz1UzvIPu9WAmjRLpr3If-1vgdT3-E_4zWN36eSe3jfMstchkkL8s9XV7U0cjWFdnAAM1UhsnFRJ6zPfF6Shy97y5dznAhdujuoQ8Lu3WgE5-8sFyI-JwjQ4CirCk1_OhiMJbEHRmYUIaZ0DDT-qs2V-W7zMeZ8HPlQF0FM8xPoRQnyHYw7q6qwa3qMmYFe_drpJ4nP7UnMvqFvfzHsXY_jRqLs7N2JS1gEdv6msV0803FjUb91Q_PZx-eJJCM9k9lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDsTo0FJ0Yci8VQyCiPWwwfyNyX6VRWeYL4zYDoLo7pwhLcPxOCcvnSKBGKktdlGr8_ta_2UG7GCgKU6zMJqxuc51TzPmFMQE7_pTtvSW2ulKX4YJwWGBwATFdGnIh4cQpKDuMNmfgpUrRHkLIdfPFSVXcUIDOIHXjZGPVFTN7btfq4oM8dAXPL9EUVyT1UyYcgYzjojHfHMjTBCjQEcxvlDuQ7Br9e2kW8BQLIQ97-aqbsaHnrjDrJvplKMpe7lBoOdjXprhjbFBFMBRvRMpsJTPwjJ2Slm4HUXzyzH1pqs-dzsMDDQ3mS0G6L5CNg9Xg2beG27tx0ERSdLCq0o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=MHuwGwesvod8eYRhdPvRDLXpHYIqINtztpuyq5oJn6Z1pfDFp1G_KZpKB6TXMRbyLgZgZHBarRdH2NcCkv3otWzS4-xJ8rkjesrFZxXS25O62zYH_s9KMXRjnIJrmsc0RAS65MQWUltTloX2zTIt_pBydZutqSRwU_eyLcAKVXZ5KXCl5iJVJ6ZumFBuNS21dBikchVamGhQMFQG3VSCdhWL5id8GVuwvhYXYAvwYhOhRIPhTOulaphyO-VDoA0m--BD7qm9R-i-zJ6s2qfew6qF65mNNeWBe4BmcF5oIy_PwtDkNfYTqdrAHokzH9ZL0qk_h_VNj0Kn_-j3a4tyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=MHuwGwesvod8eYRhdPvRDLXpHYIqINtztpuyq5oJn6Z1pfDFp1G_KZpKB6TXMRbyLgZgZHBarRdH2NcCkv3otWzS4-xJ8rkjesrFZxXS25O62zYH_s9KMXRjnIJrmsc0RAS65MQWUltTloX2zTIt_pBydZutqSRwU_eyLcAKVXZ5KXCl5iJVJ6ZumFBuNS21dBikchVamGhQMFQG3VSCdhWL5id8GVuwvhYXYAvwYhOhRIPhTOulaphyO-VDoA0m--BD7qm9R-i-zJ6s2qfew6qF65mNNeWBe4BmcF5oIy_PwtDkNfYTqdrAHokzH9ZL0qk_h_VNj0Kn_-j3a4tyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQTaIZOPaPW-Cc23mEpBBo25n8haZzNjwiAuxHUE1-2XQ7w6CwNPWNBqvLb7_20TI3dusAT0v7h8P-qxn9kBEsnWppJH_5YROKXGtDWVt8G3esArOtkfJAOh3jWmZf9nMMc8craPOhql0vNF7qnM0mcuxbzFimJtGNs_d0pV7c0Cnr8g3xlMPdVxn1uSwS03OA3_lDHeyUy4H-KXMQ-hufsjlM3JkIwNsBruaNDE84TVZqyPFeseUncqAGolX6iQMJU5VXi-cW6A79AiURO3Zcg7u2Ouw7xXo1r7q7zEl_8tQ3IB60V8QQYQ7mr-5Nz2TnbMR7ZSMUAZTCBpNZCucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7zVc0gmxAdwrdyyzN_PsSHXboTA46w-iQM1jLKSdF872SXn1NehdQV9K93oB0nLC3AeBwhunrRzC3l6dY1PhRHm_PkzznwGG4eJG6iFtJnthIVdfCiNoI_2_kfA9doUARU7cbnQ37QbNJW8UTZeLmeCXUmK-JeTnlXRL44ZpsA0gtzEBZsgpC7xIZB1ccUbr5yGCHckuVTpUVUfxhnYFXHRkgroh_U2DhZBVTFYdzJsXp3QaeLnzCL9kyMx2ZTbEtrJGM9IdvHwwwyi9uF3xm-Ng1kNrgT5JJQosIJAIbyYFu1L5AxJBYyRkvAYWZR_hvgQvv4hmARaF414n_iaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXkopTs0BPYS6hFohEBSehhkZGiQQEJ_jej0tHtHqWyZENT7E7DtjAZvopgJKwux4rCiHq8DaPn3PUtB5EUY47z8FURiLsNfZQQCZX7DnXHtjOl4Z3UDGndYeS4d6T-fnEJ0pndAsalVMtRtzArKy3sidtXFuRBpXmLE2M8aCZgOXnK1yeM7ufFQXDAi1grHX9wb0Sk_bGKSvrkMPOPMLz8xpcCADkniuaKJYBP4-VQUB897FF-CoLne-1jfaoD740IGrzF53Jwb98bWilPL4LVzv5wGlwn3IfECImosgMiCUL6TMzurs6vuU6e_QUPAZDImnnLQZP6vjQdx-1_b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c_sI4bhpD3XlcUC4C3Fm1ONNWynX_9FsHirWI9tlJysgPmAacUXFG0lQnhquIt66zeHGL-GeQ0IglieoMfwg2vSwAMIzPXlwXsDFUOvKFjlj41dAYUeIsWu5x7k01YX4uWNUlzYUem2ELCeJwQCE2sQIrGN3lPUed1dyqMiCpqOX4wnvtnFWoAqLouf4D0Sj60yU24vv4lPkDBPLg-f1jiNRP9RtQ_BdCOQnAUC_C7YKF4ntKSKRLhDvXKPtpoe0_ybSs9vE-ud935cazBLcHcFEABnKpVm28fTmb41fjSefm3HOGUzRFEVWNbv5kkgagXGp0yYQ_wKyLlL5NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxG9VWO936M6EJkyyOj0PDXrkuzrVPIMspNJuuvVmWHWuEnEv7e946qQ2Jsq_h3E8NYMk_UmQVu85KnoAFzbKhPeaXLPxW0_lh3_tEHwhfbZDgL-uQrJqY57QX3HPi5FjZA9jaQJCSR66eIrgNg4wPe1SPU1RIYgBWW5dnw16swGyr_1aDLrjU-q-_50nDvEOid7JCcqJezXXVxy3onPy0v0Is-6HBB8SJoqpYmqIdLENdpkTfnCfgqc9Fe19XH4LXOQeBf7GuLejRn3JRMf0yT0puLtd68PGatvV18uJgxav304mHIuvuhxmYOyqo2TB1cas8_2GUgcEreWzmyFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF4eyQKcanYCuwhqtTHZsY7z1EWeK4W8vQtmRz6pURO44YtqkpC5AuFhKNhf9lBJCTh-QXWsoKdYYUXeG43dGONl3YS5snW3v6JA203OzYLWtv6N2kGU1fsIW5k_NCAwA3RgwumDhMzbKc86aRQAaZCnNOUfZJQUAqfPgVGWnXPtGo4tNCZAorHxfvNDhBIAJydkQqZsxF9UMrFUTqr8q6_pfyaZvQSvEpUbejZ4skTOK40oDswiZKZa_lv8J85l3RuW3mK6oO63Hq1M6Beo1HVR7LmIsStlmdG5dpOwD5yx9NXk6uhIycYvHJ67z9qBs0O89D4XS27BDpJSarxuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=sxPQ1XPkxU1pzy2Bt2b8KAKx1lBgurM6Ol7wsG8U7YZPpOr0XUxtwRUbQvp_ZX9GZ2kgSRrhFHZRdbAITfsz5yPLJZjkYlv_-mXCS10p76ny0wxWVq70nHY0Z14-Aqec4OI-j8VOeyFnlUj6lbI1K3gzyWRTPIr8p2_4lWbGW6-AZMQbOa_cSC3yJ-OFTOAGy3zVQmkIbA_OCbQqT0bnOtL01hDPxoPSQzIDu__DodshwzcVvqR9sqbkujl5KsIttwEhzy5wsJ2-myPe_A9muLyDUFgBIYLrhCQ5w5vf8pB6MJKvt1hp1PZLI0XImGnlv-cf1lBdoHS4saewsZhBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=sxPQ1XPkxU1pzy2Bt2b8KAKx1lBgurM6Ol7wsG8U7YZPpOr0XUxtwRUbQvp_ZX9GZ2kgSRrhFHZRdbAITfsz5yPLJZjkYlv_-mXCS10p76ny0wxWVq70nHY0Z14-Aqec4OI-j8VOeyFnlUj6lbI1K3gzyWRTPIr8p2_4lWbGW6-AZMQbOa_cSC3yJ-OFTOAGy3zVQmkIbA_OCbQqT0bnOtL01hDPxoPSQzIDu__DodshwzcVvqR9sqbkujl5KsIttwEhzy5wsJ2-myPe_A9muLyDUFgBIYLrhCQ5w5vf8pB6MJKvt1hp1PZLI0XImGnlv-cf1lBdoHS4saewsZhBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=dIvsFWQz5YuPWR3hFeeUPX22iIUEy_mfbWClFyLodHjX5_f0RnnSu-aALZC196vCyRNg_zFelEPBEjlOdDt9o7nfE_BvlcqIX4rliFqvySkRywrPy53XNFuF0JHVbKcfPeQisBLHIWIxS4TGnXDoel6yPc-m62kfnhote7Z6ca7_hcLqm0_DiO1OfwCILsRpAac8rXS7KZHF3eAFAd1eCwa6E2Lf4OiNz8vysouH2n0Ij6w0JCYkvjH8km_mAVPIOr18MVTICybv4znBwOZqGrycnD3H5Gx78edyXxtHHz9aAPlIopV2J98Rj6bolm85gB12Eo8SkZzIMngk-rIq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=dIvsFWQz5YuPWR3hFeeUPX22iIUEy_mfbWClFyLodHjX5_f0RnnSu-aALZC196vCyRNg_zFelEPBEjlOdDt9o7nfE_BvlcqIX4rliFqvySkRywrPy53XNFuF0JHVbKcfPeQisBLHIWIxS4TGnXDoel6yPc-m62kfnhote7Z6ca7_hcLqm0_DiO1OfwCILsRpAac8rXS7KZHF3eAFAd1eCwa6E2Lf4OiNz8vysouH2n0Ij6w0JCYkvjH8km_mAVPIOr18MVTICybv4znBwOZqGrycnD3H5Gx78edyXxtHHz9aAPlIopV2J98Rj6bolm85gB12Eo8SkZzIMngk-rIq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=Yyi5t3hGIATrCZdAjqfaXTELzHfqmEHEYxOuMHfDO32AeJigfPzoEhXA18gHEj_1gTZlBe0MPKp7QjCQQWt-XgYVarkSairMneRRgE5djH7wpfleGqkeQhMcA78OP4V21A7dPw0SZ_TGK0FzAdzypx7e2GExoeFKUI7uUDlUq9ohsn3ZuPD2I9PJgoFKPEgwtQF2e7tehQPENkICXjXGW-2qwMvRmXfhKtIBHT_8mZX7EkEh7k80SUxOZMQZuZnNlq8h8qoKv-LTUQKGbsWCyT7FSO6LXjpFS_nt1wjg6MtwjqfmzkstMG7Ok71GLmFL0v3OzJY6CJuFmUtLkbrcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=Yyi5t3hGIATrCZdAjqfaXTELzHfqmEHEYxOuMHfDO32AeJigfPzoEhXA18gHEj_1gTZlBe0MPKp7QjCQQWt-XgYVarkSairMneRRgE5djH7wpfleGqkeQhMcA78OP4V21A7dPw0SZ_TGK0FzAdzypx7e2GExoeFKUI7uUDlUq9ohsn3ZuPD2I9PJgoFKPEgwtQF2e7tehQPENkICXjXGW-2qwMvRmXfhKtIBHT_8mZX7EkEh7k80SUxOZMQZuZnNlq8h8qoKv-LTUQKGbsWCyT7FSO6LXjpFS_nt1wjg6MtwjqfmzkstMG7Ok71GLmFL0v3OzJY6CJuFmUtLkbrcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=s7poTNPd03mwWjKt--MJCPBzDI8EKynnSt4jBtU7D3pTHS6_kIAgyI9XmkAjaRf2yCr-GpmziCCtP6APT6Oep_YhIHHke8IgoOp3Lbe2lES7t9EzRYdFaHYR6PWjEDz6Ma6FULTOvpL1fdT3FOc_G56hPdXn_pmAvYcP2KKJcqmAF59jJ47y1opxr8LUJDXYdCDO0wS0wXKkXUhKPpK9f0UH6qs2TxdbiZx2mJ7AaBKgs4qWeRD4ahO2yQkTbFTSTpOfLQWTTLH8llcpjIyMJQ9mRLdpFcY2YE_B0Lsszu-06WZCPPA1YdHWgx0cxa6HlbmpNaDzP7ZGvS5bEaq9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=s7poTNPd03mwWjKt--MJCPBzDI8EKynnSt4jBtU7D3pTHS6_kIAgyI9XmkAjaRf2yCr-GpmziCCtP6APT6Oep_YhIHHke8IgoOp3Lbe2lES7t9EzRYdFaHYR6PWjEDz6Ma6FULTOvpL1fdT3FOc_G56hPdXn_pmAvYcP2KKJcqmAF59jJ47y1opxr8LUJDXYdCDO0wS0wXKkXUhKPpK9f0UH6qs2TxdbiZx2mJ7AaBKgs4qWeRD4ahO2yQkTbFTSTpOfLQWTTLH8llcpjIyMJQ9mRLdpFcY2YE_B0Lsszu-06WZCPPA1YdHWgx0cxa6HlbmpNaDzP7ZGvS5bEaq9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=iVQtsbpY2BINWhEFR8T4gB0O40OG60vvK5EnwNfxbKlW1RmxG918toWUChPSQ0qR8ALhW5ThAjx9MYHo6DBugU_xSdQk3I_ZyEMWGbpBdU7pAjr3VJ2W5H2W5sqvaaqn4sD9g8d7NbUZ5Nj1mE_F0CVrNya7_MpJqy9f1C-EC8-3Us5FoxRcWWJv1tZ-zfmImrucSJ9RoFe-1BAS9hZWF73ebgemAnvfwphTANVLqQaCxnuU93NG_WVGUUGG8p48P0qHyKfWbT83SIWqvsOnFJ84HTqDD1EA8lqyr_egAWAGxKZ9kkwv9SsleB8YJGIm9oXYT6sB9r1kGu2t-bjgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=iVQtsbpY2BINWhEFR8T4gB0O40OG60vvK5EnwNfxbKlW1RmxG918toWUChPSQ0qR8ALhW5ThAjx9MYHo6DBugU_xSdQk3I_ZyEMWGbpBdU7pAjr3VJ2W5H2W5sqvaaqn4sD9g8d7NbUZ5Nj1mE_F0CVrNya7_MpJqy9f1C-EC8-3Us5FoxRcWWJv1tZ-zfmImrucSJ9RoFe-1BAS9hZWF73ebgemAnvfwphTANVLqQaCxnuU93NG_WVGUUGG8p48P0qHyKfWbT83SIWqvsOnFJ84HTqDD1EA8lqyr_egAWAGxKZ9kkwv9SsleB8YJGIm9oXYT6sB9r1kGu2t-bjgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=drVkvdhOHDUifuWdvsqgP1cKuEvnl4I8zM_tBs43Yeqn4UCXJjE15bMXWpk1N1aSyhjGY5ecFfXP53wKrpjDZGg7WRyuGoXGw6KxLpsOfRMuK41fvefTrvwXDV329_dV6Lb9ejVvtZDzm2WVaU1rqhHKjOru5_tSJ_UWXth_m371V3M2tfmma7MwhhlIxq0ZKfvxIaupkm0ySQNFtlbM28qLLlnPWnOIte1mmHo5BcVeKJE4GApdHBvURS4bFDfeh4ZeFiuA_AcMXemFYBye7hCePByMakXdn6yFgzQRTZ_w5jDiJgNkIKQbSEumWgBUEHzxalNFtO1j86etCZQFbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=drVkvdhOHDUifuWdvsqgP1cKuEvnl4I8zM_tBs43Yeqn4UCXJjE15bMXWpk1N1aSyhjGY5ecFfXP53wKrpjDZGg7WRyuGoXGw6KxLpsOfRMuK41fvefTrvwXDV329_dV6Lb9ejVvtZDzm2WVaU1rqhHKjOru5_tSJ_UWXth_m371V3M2tfmma7MwhhlIxq0ZKfvxIaupkm0ySQNFtlbM28qLLlnPWnOIte1mmHo5BcVeKJE4GApdHBvURS4bFDfeh4ZeFiuA_AcMXemFYBye7hCePByMakXdn6yFgzQRTZ_w5jDiJgNkIKQbSEumWgBUEHzxalNFtO1j86etCZQFbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPWm2_KGG_uB-_Qd-_3SJdbDDjikUweWTcyrnPkLNFD2HIe2IuF4Tfl-1bL2_KoNRR38qCMpEik264BRxatsSn5XK73KNA4dS6VWkWoYt-fajWqaPDD2gX5ImPZzLQvXLdPqqvAZLN4M8CBz29gaWAf4rTOkC1vyygrjLqvCwcTc9sxx0hlTCCcf403MDUydwFQVdlqpih0tqVf8Kuxqo78xN6sbE05Wvq4QigWtS25PJ-uz1lnCHlt49bYkHqiIpTspqZ6v0uIJ-5aOJIv9oJJklaR5xljtfnVvNTkYuSKho5z9NGf3dFisVQJGCCjPZTNcIqWVY3oev6ux2kbFNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=npHC_2TshjoPQbRVRaaXjM5w_QGIVwLG2wmIIjTP6SsTiQgl7w_hD2Xyr71UN5u0GnX22jodbOAkGsrIw7p-eL-cQBQsZSguqPYbvPmr9nLrjtqo4wXeGJhV-EsSc3lIytJ6dGf_-u2_1kIANvdtIUsuA3oJxYuLaj8noxtQ_W5gEL5iYGzjIeaBDD4udPpXLUyyL5AHuAx7mIj4-1rXMOS1i4AKIkHi8T4qJgFNQis58xzbGf8oVHVuouHp2OsBM798csoreIT0n2PmKlApNNvUPdIMM89CazEArWyMJbsDRteZAd3TgLC0EN_l0AapJEsk51_VFVFL09aAjmCddw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=npHC_2TshjoPQbRVRaaXjM5w_QGIVwLG2wmIIjTP6SsTiQgl7w_hD2Xyr71UN5u0GnX22jodbOAkGsrIw7p-eL-cQBQsZSguqPYbvPmr9nLrjtqo4wXeGJhV-EsSc3lIytJ6dGf_-u2_1kIANvdtIUsuA3oJxYuLaj8noxtQ_W5gEL5iYGzjIeaBDD4udPpXLUyyL5AHuAx7mIj4-1rXMOS1i4AKIkHi8T4qJgFNQis58xzbGf8oVHVuouHp2OsBM798csoreIT0n2PmKlApNNvUPdIMM89CazEArWyMJbsDRteZAd3TgLC0EN_l0AapJEsk51_VFVFL09aAjmCddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=npr5FdwTBEJBYxJixTnd6ynPPXIO-Uy1R9ornJGAH4Z5Sl-IVTutGe1nSYJ2UpBCq3KLkFsbygGJWj890kI76FLdlycYdfBx6Sc8rM2lY66XijN0K_mjubxCv_9wlvxGg7wptedF5lBuWfI2kixesrbd92CdU1cdYtENzEdOoZcs73Evwz-rXM9TWP7W1KsS9oFT7VdWgoK1o1OrEwaF1cy-ZYmmkOsGJKyLFhoSiIL2_GvoOvNs6yrl1DM3zpAklVnfY2Gw9FalIHvmXNCHPIu0SR-Hcjg2cukMQiPOiKKsM6P3M5gn_pyn708iMRI0cJY2BDPViExFMJ3LVZsytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=npr5FdwTBEJBYxJixTnd6ynPPXIO-Uy1R9ornJGAH4Z5Sl-IVTutGe1nSYJ2UpBCq3KLkFsbygGJWj890kI76FLdlycYdfBx6Sc8rM2lY66XijN0K_mjubxCv_9wlvxGg7wptedF5lBuWfI2kixesrbd92CdU1cdYtENzEdOoZcs73Evwz-rXM9TWP7W1KsS9oFT7VdWgoK1o1OrEwaF1cy-ZYmmkOsGJKyLFhoSiIL2_GvoOvNs6yrl1DM3zpAklVnfY2Gw9FalIHvmXNCHPIu0SR-Hcjg2cukMQiPOiKKsM6P3M5gn_pyn708iMRI0cJY2BDPViExFMJ3LVZsytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=m8WZMtpIoC2iNmm-MES6Sk7mUnP1KE0Fl5nwBCQnlOg-718W_oUknGTQ0skrayQ71mjRj9CmuGfCrYLEPS1W-MpIJjlkWDHRj_EhWTCBkXD2e7drRbOECnVQEgUQRvr2zdx0Db_Sf4-XqxS58L3vHW_z72fDmDgfwJ3CdQWcMvWa8S9p5vYM3lOaDHuD2iacsV5aWauyV6CH-jOxNr4ueK1bwKpJEWiiBCiGw13yYFEKmx5Ss3FATPKscNMjhEcrM-fdcwf3WxVghUJ3GBW9H-x7VmvZdCkyEH3Jf9LZavBC6GZcbdxsA3LHUXZL_qQJ6H-bXbeMOKw2_qqK-3WM5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=m8WZMtpIoC2iNmm-MES6Sk7mUnP1KE0Fl5nwBCQnlOg-718W_oUknGTQ0skrayQ71mjRj9CmuGfCrYLEPS1W-MpIJjlkWDHRj_EhWTCBkXD2e7drRbOECnVQEgUQRvr2zdx0Db_Sf4-XqxS58L3vHW_z72fDmDgfwJ3CdQWcMvWa8S9p5vYM3lOaDHuD2iacsV5aWauyV6CH-jOxNr4ueK1bwKpJEWiiBCiGw13yYFEKmx5Ss3FATPKscNMjhEcrM-fdcwf3WxVghUJ3GBW9H-x7VmvZdCkyEH3Jf9LZavBC6GZcbdxsA3LHUXZL_qQJ6H-bXbeMOKw2_qqK-3WM5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=knvFLTnmaaiHFo4ju8yxkOIsC6xosxQXmTPM9JEYML8MVlhPBizCQ5Ujl0AJ644-MouSV7EOT4F0PZOWjTocXT1F6zkq8IIN0IVt9pvpsgbsrX9hqRmRVeJoBpZB2Xm7iGpRmZX7XYmVfFvT4vp1SQk6vbNyvJtj6nV2oziJ41jCOBbbIglgdow2ecdcHgklccukaswFLkA6V0HChdwwyveDgaPFiFvURIZPtjwzgO7VQPcpZVzrtqPUHZr1IJQlNBoHKCkUQ0GRtH_odJANiG8IipEfPnZ8hDHk8qcfUXYDMOh3sEhBdPUF5SgfKV-s3fLtqjeishtvCKOECEdCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=knvFLTnmaaiHFo4ju8yxkOIsC6xosxQXmTPM9JEYML8MVlhPBizCQ5Ujl0AJ644-MouSV7EOT4F0PZOWjTocXT1F6zkq8IIN0IVt9pvpsgbsrX9hqRmRVeJoBpZB2Xm7iGpRmZX7XYmVfFvT4vp1SQk6vbNyvJtj6nV2oziJ41jCOBbbIglgdow2ecdcHgklccukaswFLkA6V0HChdwwyveDgaPFiFvURIZPtjwzgO7VQPcpZVzrtqPUHZr1IJQlNBoHKCkUQ0GRtH_odJANiG8IipEfPnZ8hDHk8qcfUXYDMOh3sEhBdPUF5SgfKV-s3fLtqjeishtvCKOECEdCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=TSM9B1P4N1-zzdVw-VrkoYa4266I1is4aPgC1qBfk-FcyHoPCKqbQRZr8PmmNaWI0dUjts24-hUWrVMTdUw1VH03KrZ1Pu11kkGz4eDJasbJn4WtUR8O59k17ME5MoLY17tEtOLR3qLMDxZs4Kfqp0-24QoTXdCTZzOJTxUiX68WVCVYAtOtoAFzLlmY3Vw5WqIslm-soUX6UCNA688cXCiKKRZb8vFlatjzkQu1JeolJZDsGAMwYIyGDZwP0SWLPgu1_WuLGhh69M4dWNjK3P6_RlznNeG6j3bPyCEmo1_7CoJSYQoJ18qnhe3Zy0wGYQF7lg0KaqENs4RT_hJGwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=TSM9B1P4N1-zzdVw-VrkoYa4266I1is4aPgC1qBfk-FcyHoPCKqbQRZr8PmmNaWI0dUjts24-hUWrVMTdUw1VH03KrZ1Pu11kkGz4eDJasbJn4WtUR8O59k17ME5MoLY17tEtOLR3qLMDxZs4Kfqp0-24QoTXdCTZzOJTxUiX68WVCVYAtOtoAFzLlmY3Vw5WqIslm-soUX6UCNA688cXCiKKRZb8vFlatjzkQu1JeolJZDsGAMwYIyGDZwP0SWLPgu1_WuLGhh69M4dWNjK3P6_RlznNeG6j3bPyCEmo1_7CoJSYQoJ18qnhe3Zy0wGYQF7lg0KaqENs4RT_hJGwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=vRRLeE4xoMkJdo5UPrGGgELZOLdWSFac3fZp6xHmcxnvj2e2k5rvpYez6gj_3R2dATiT17EFzjKX6vXjXKwEWEyzm2IyvXehF740yEXJdQXrIwtcw13v6AHDTtsO4WNIqZokyQZwdWPAkNi0Cec0L6gt3gEOpbjdKinP07-KbCW6Jn3DncaC2pXi70wLjYkLtSRE437puBD8jPOAu_x_e-wzg0-HdiOFEoVltGTcnQtHlnMdP7A6w0R2E1elD6OO2cOnwo97pvnwf46_hQW04ELuZoIt2QgWr8_FwQIogBNyCRq9y1mtzTPuEV8gkpf-51oNmXKD_iELwSWlEkaqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=vRRLeE4xoMkJdo5UPrGGgELZOLdWSFac3fZp6xHmcxnvj2e2k5rvpYez6gj_3R2dATiT17EFzjKX6vXjXKwEWEyzm2IyvXehF740yEXJdQXrIwtcw13v6AHDTtsO4WNIqZokyQZwdWPAkNi0Cec0L6gt3gEOpbjdKinP07-KbCW6Jn3DncaC2pXi70wLjYkLtSRE437puBD8jPOAu_x_e-wzg0-HdiOFEoVltGTcnQtHlnMdP7A6w0R2E1elD6OO2cOnwo97pvnwf46_hQW04ELuZoIt2QgWr8_FwQIogBNyCRq9y1mtzTPuEV8gkpf-51oNmXKD_iELwSWlEkaqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=mW9KfR84MLt4_7CwMGWcyGC1H5rU4xk8zhsCc3LcnBT3Syjra-nm3HiVWmO5fN8__aQ3Z6BiqZ7u6EG9tnbTmFyUt9Z-dYQ_BLOiXOlHmYEmT8-cowLoXaFharXPOrcXD-31UD-jNYWGn1BVCHOspd3f8AkiBA2VGmBrXG7Ad9WNiSu9jv4ykYA6H06F2ynhBRz53Son54-UwXUInslTAaTre48w2UnCxjhoTzPqyjQXQi9dHVUm0MMWZKqbaDYEORSLltYTbZErHB4GjZE0VU0U49hZrpaRX6RTK5Ggxhp1MHfEdWP7JNPsLXkDiDGOmnZf8ZlfiH0D2O-UahcPRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=mW9KfR84MLt4_7CwMGWcyGC1H5rU4xk8zhsCc3LcnBT3Syjra-nm3HiVWmO5fN8__aQ3Z6BiqZ7u6EG9tnbTmFyUt9Z-dYQ_BLOiXOlHmYEmT8-cowLoXaFharXPOrcXD-31UD-jNYWGn1BVCHOspd3f8AkiBA2VGmBrXG7Ad9WNiSu9jv4ykYA6H06F2ynhBRz53Son54-UwXUInslTAaTre48w2UnCxjhoTzPqyjQXQi9dHVUm0MMWZKqbaDYEORSLltYTbZErHB4GjZE0VU0U49hZrpaRX6RTK5Ggxhp1MHfEdWP7JNPsLXkDiDGOmnZf8ZlfiH0D2O-UahcPRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=HVT4uRjUHf51h4ObJxqLRke9VeFIiCcGpeUmMT0zQNwsaLjdX3a5dNlDKI1_ducWSkIYeuT_jXN2_FiE5hx9RIR-0gkdP_vk9yp1oGUVbm2ju4RJNrZsiQ1VCHPNDufCEV--0VcWI51QIvQ4Bly3OuonTDrcYDd-SbYfQkDXQB_bI0CIsq7At_n48Hf3bJCaPLICuRX0LF5sxHnbkleZL4h7lGargl913eOgn_d7W0kCFISunDhQvMka8qpvktjoouCSNK61q0n-h_3Lzw-BVvO7CacALSaV9SCyxb-w-jZ5MwQbTjrAq0tINiH7NanztYTA5GVouhrCoD9KOxabXKO_NnTmaLRWc9EU6k1TlbuUarkCz81kxZa-n5uDea1VmxFiSnOcv2LIM4MMV6XgjOu9gjCB46VwLiJlomzQK9MoHYCW8NWQ5nL-zC2uKQ_Hr0vESVmT12d5zXC9Ok7XUvxi545k_OocUMs1lItcjSx7MEiOIh2XoACszx-8WYRheRB6mO4pz2yv4iUXdWZBSG6XXrXEuUC13Vc8EraKSwcDcwoWPI4PFLKc5uHmypvy-cxY9kzq2erCOQbGpIjepQj4FBU6q4PNTBxhAz2KKuPCvsyCfcDmcBfhO5yk1GkOzNaBt4i1v6RuDWZgZlcUE7tfRbFI8S8N5g-Hm5lKnjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=HVT4uRjUHf51h4ObJxqLRke9VeFIiCcGpeUmMT0zQNwsaLjdX3a5dNlDKI1_ducWSkIYeuT_jXN2_FiE5hx9RIR-0gkdP_vk9yp1oGUVbm2ju4RJNrZsiQ1VCHPNDufCEV--0VcWI51QIvQ4Bly3OuonTDrcYDd-SbYfQkDXQB_bI0CIsq7At_n48Hf3bJCaPLICuRX0LF5sxHnbkleZL4h7lGargl913eOgn_d7W0kCFISunDhQvMka8qpvktjoouCSNK61q0n-h_3Lzw-BVvO7CacALSaV9SCyxb-w-jZ5MwQbTjrAq0tINiH7NanztYTA5GVouhrCoD9KOxabXKO_NnTmaLRWc9EU6k1TlbuUarkCz81kxZa-n5uDea1VmxFiSnOcv2LIM4MMV6XgjOu9gjCB46VwLiJlomzQK9MoHYCW8NWQ5nL-zC2uKQ_Hr0vESVmT12d5zXC9Ok7XUvxi545k_OocUMs1lItcjSx7MEiOIh2XoACszx-8WYRheRB6mO4pz2yv4iUXdWZBSG6XXrXEuUC13Vc8EraKSwcDcwoWPI4PFLKc5uHmypvy-cxY9kzq2erCOQbGpIjepQj4FBU6q4PNTBxhAz2KKuPCvsyCfcDmcBfhO5yk1GkOzNaBt4i1v6RuDWZgZlcUE7tfRbFI8S8N5g-Hm5lKnjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=IPISgp-dsxr5TFiCF8wGRrm-i52xRmBH0UWEB7koK1oUh2Fa1nBvzlFq9CzPSDgZm7hNV-9ZrsjJst3ojJl-7a9gOe0OZaQpD8LQyEzHbWXkP_WVCP_m9-wKq3rNe_PbDSA7KPUZkcLXZvQYo7gtsXkMVViXWeiiBx3tzNS6ZP4p846hEC12znHpLNx8dMJPg11DBCwzSwKd78Q9il6s4214il-ZGzgutP9Flvsp-XosmnqYt6OzmjaE_WpodkzYreltEl4pTZ8lmdL4BvklKcDw0Aqyubs3hLU_1Ez4Cl61izYQoGmgYjvreA9voSBBvuxdG_iQyGtE3QOQoGTWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=IPISgp-dsxr5TFiCF8wGRrm-i52xRmBH0UWEB7koK1oUh2Fa1nBvzlFq9CzPSDgZm7hNV-9ZrsjJst3ojJl-7a9gOe0OZaQpD8LQyEzHbWXkP_WVCP_m9-wKq3rNe_PbDSA7KPUZkcLXZvQYo7gtsXkMVViXWeiiBx3tzNS6ZP4p846hEC12znHpLNx8dMJPg11DBCwzSwKd78Q9il6s4214il-ZGzgutP9Flvsp-XosmnqYt6OzmjaE_WpodkzYreltEl4pTZ8lmdL4BvklKcDw0Aqyubs3hLU_1Ez4Cl61izYQoGmgYjvreA9voSBBvuxdG_iQyGtE3QOQoGTWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=tXqqj01o7XvpQRLWrJ7GnTVO_Xq6JXBF5xTTGE1MCvVOfx_d3yhP_rYyLyOwCZMDobZJpvIqUvRbu5QxXIf1FqVQiJGk9e9B7Pg2RJDB4X0c3IZC0DFp-vmn-KyA4IfbNIouINsAhuVDKa_bw0KSz3MmL0L1IR4jEYmHe5eSf41NvHECsX0pw9-UI-Dpp7n5er7dW1cqLuiwjV9A09M24nTCmM6J_ucETGgMrRl1rYGqRhnmauHrY55nR1wimxDzE1wSPnS7bcJMQa3teL8xEi322cqnlw7bIMqQ-qhvB-Ew4rbA7HC_0crCqSVRNjwxQj10k83yH0iDbxfLqV_4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=tXqqj01o7XvpQRLWrJ7GnTVO_Xq6JXBF5xTTGE1MCvVOfx_d3yhP_rYyLyOwCZMDobZJpvIqUvRbu5QxXIf1FqVQiJGk9e9B7Pg2RJDB4X0c3IZC0DFp-vmn-KyA4IfbNIouINsAhuVDKa_bw0KSz3MmL0L1IR4jEYmHe5eSf41NvHECsX0pw9-UI-Dpp7n5er7dW1cqLuiwjV9A09M24nTCmM6J_ucETGgMrRl1rYGqRhnmauHrY55nR1wimxDzE1wSPnS7bcJMQa3teL8xEi322cqnlw7bIMqQ-qhvB-Ew4rbA7HC_0crCqSVRNjwxQj10k83yH0iDbxfLqV_4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=OtBQuX3q7CBRfv0FlObLS3VaAfCNZpUQh_tP-5mqoVS__L5ZGU7LI2t9kcCNLe9HLkhqF3L-iKVHrSrvvrY-YyuAeOz8HRKjnUWCtnQFxEvuLUrhCxzxmFHuoupM75rapCbzzGVwecIG2s_WOOcsv7pKAKbe3WTGGKJ7KsXk3vrAtPriJCUlMHgOVW7Mwwx7yTFyZyY8Yrs_48SQhRW_S0DjASFjd8xBim2LksosoogLN2BPCuL_R1sT5573bmGG3Tequ4qb5ilINl7JBggBbvyyvxHebiB0DZV8SArWF2Q6yn65e92HsTyZnbRvcBXBDeDSYBKB3UWVz3Qibap_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=OtBQuX3q7CBRfv0FlObLS3VaAfCNZpUQh_tP-5mqoVS__L5ZGU7LI2t9kcCNLe9HLkhqF3L-iKVHrSrvvrY-YyuAeOz8HRKjnUWCtnQFxEvuLUrhCxzxmFHuoupM75rapCbzzGVwecIG2s_WOOcsv7pKAKbe3WTGGKJ7KsXk3vrAtPriJCUlMHgOVW7Mwwx7yTFyZyY8Yrs_48SQhRW_S0DjASFjd8xBim2LksosoogLN2BPCuL_R1sT5573bmGG3Tequ4qb5ilINl7JBggBbvyyvxHebiB0DZV8SArWF2Q6yn65e92HsTyZnbRvcBXBDeDSYBKB3UWVz3Qibap_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=DH1KNXh7XK42bKXZHHCdA7a4RQ0KlWVGgnZT0jOLw5phXai69lXYSUA_iliq2zgfVhtkmsKZFve2qJ1Rh2r5aKdVp5tknmQ3jWgeo9gq55XALksCJfFleO1H3sT3Ob0caL5BbJMPLEK3bKqksd99eIvvlbDaVXGv5pBGO5ceg4m695WjKNcFuu0GgNoP6ffmNQUtAE8wgNGZCBT0M6-yHVBlC2ZafaPxTY3c3MDtsvko7BUaGOAjZt7d4_qmHbbKEp2Zhj77M4Jaos3dfZw9h24iG0RGo06SRAU_z7q4OX7L5Yi8AGtAeLyT1WUQBb1ArmRnODrPBeryJW5Pn9Z0GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=DH1KNXh7XK42bKXZHHCdA7a4RQ0KlWVGgnZT0jOLw5phXai69lXYSUA_iliq2zgfVhtkmsKZFve2qJ1Rh2r5aKdVp5tknmQ3jWgeo9gq55XALksCJfFleO1H3sT3Ob0caL5BbJMPLEK3bKqksd99eIvvlbDaVXGv5pBGO5ceg4m695WjKNcFuu0GgNoP6ffmNQUtAE8wgNGZCBT0M6-yHVBlC2ZafaPxTY3c3MDtsvko7BUaGOAjZt7d4_qmHbbKEp2Zhj77M4Jaos3dfZw9h24iG0RGo06SRAU_z7q4OX7L5Yi8AGtAeLyT1WUQBb1ArmRnODrPBeryJW5Pn9Z0GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=r60j0VR47xsHqS2_Grm62zLFMOX34bY5b9JqR8tBGmJYTls9bZZxhwo96pOxhGIwZYhOKMLQGUSHyKoKbM-GYUewg80is3OQ3T6oATqBN4HHJ1rM3i4dB8GGwgUEwQ2YTOmozLPXyJ5a_SYvAr64iMJ59MzlgpblrVocehzEi7PYKSXrJME3CT-GY6nM9sc4OBuwbgIeOVoqcJ4N5hdrYYuoVabjDw7wKrDNfLbRPMmmce1Dj2gjeyelZr19-T8MITtet4bXy5sm3szqOTE-Bn4DPtB3B_k0osnMKb3NZ6mS9F9Ex-Q3J7AwrLkTnGiMwh5aOhmuHEDkZ47JNmBr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=r60j0VR47xsHqS2_Grm62zLFMOX34bY5b9JqR8tBGmJYTls9bZZxhwo96pOxhGIwZYhOKMLQGUSHyKoKbM-GYUewg80is3OQ3T6oATqBN4HHJ1rM3i4dB8GGwgUEwQ2YTOmozLPXyJ5a_SYvAr64iMJ59MzlgpblrVocehzEi7PYKSXrJME3CT-GY6nM9sc4OBuwbgIeOVoqcJ4N5hdrYYuoVabjDw7wKrDNfLbRPMmmce1Dj2gjeyelZr19-T8MITtet4bXy5sm3szqOTE-Bn4DPtB3B_k0osnMKb3NZ6mS9F9Ex-Q3J7AwrLkTnGiMwh5aOhmuHEDkZ47JNmBr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz1lP4c4SXn-oyYy94XHJKKnZBRAyXSP8gzfszEZ3XwFyJZizFnAFPc4fXtv3_tvkB2Iqf-6TuG37I61zjPKWvtAM6H5nUBhE8D9nk3Quq94EsWuvXOT444B3-yiFMc6R2heFwRW6pPCT_GP98Eum8ryF2sBdLsi1ALhXSTYO_CpecrIDpZEuf5Wvi5svXwD1OHn5cQVqXzHLK8_cDqD2UkqTeyX7x3F4_OQ6W4ZjhgZgtMUZMofCH-PmnoAMEXDQj0DIoSUmHnT7UynyeRKYZFlOA6hlIH1qnnFLmCZT4ugxxaNVZmTl7IVAf1AcLIE6SzWwQ-Nd5tDXEjwwpwN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djC03eYdpY6slpYwXYqcZAhUUgsUk-apAgvbHLpP2y0zSWmjEkpTdHCtzoATV6dJA3Yx2APMz1J9-PU_vs91RcB2fMusTKVHmLVgAkU7ATs1IfXArVs3PCrtQ_hTHQYrxAhUnZfx_1lSzGWKkEQaarUoKgCzPK3H-wNg7IXiz4oXMUHVZyFxsp4NZRcmjUOgCgMQyGUBmA1IqxMupqe-_q8Rmla6niIQiKUf6EVe6n9GexbD5VIXSgCR1NGOLqh3nyOURyJKe8PE2sxH_8T9syJmRQWg3cj0se9HlRwfidB0Esx1CI8GsIp9an6EWZX8Eay0QRHphOXUyCIwpTlTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7cyzP_oNL0s-6Xmb8KFxJ1hBBwiSsDMUtxTwIShg6pwMlVY-FggBAtYRqliDF_XEzFrFw_2TJYWAXLCHv5o3huI5rDgMgnGg8Z4AKKXG4rHEvL17z2ivOxKxj7ef3SyIlR7eXj1aR7geBmMmRwY-Kv7_eju5kL23AlB9pPammA8TjI3tuYCnsNOhKF2uPOV2yAQirh9i5KmSh38mNm-gkQSdXg3eyfqYQxFchfmY7Yt6xu4RDG0VY_UyWGzCfT9hSPmIN_DiUlWPAe9EoNQ66PVNrFc4Oy5K_ah1jH9GyhLhJFKl3DyFtMabn1uJCWWUsysBD06NPbPSqjJS4Sksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=HdtHGpOhBIFj4tKi17ilWkBHJIQC0SbOa4F_eZ_yhcMhKIL71gNHSwSB8XleSpUprDPM7EsUtXkd4zgmhG6qZgRuc6kCZV8TuLP5i2RYbT9Ov5cqkqXCdm_thzQFJcmxXBccbKEZIJm26a-fcJqeCjEbRCEbEeXzu3PmkYDgXdcIDQT8k8wss4zjo7PRgEhratm0wDS5bZ3D5dX79CssnFQn3ynCQg4-GnPdDC-Jr7hD15-DMzNJbI18PX_GGbWKz1qe6ToxC3XC9qfl_R93o2G9bYRnswcP0VnZMVnnLBB5xq-GXPwl6OXxJ-yd9qvdiaM3V1V8h6fcxKrKZAq38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=HdtHGpOhBIFj4tKi17ilWkBHJIQC0SbOa4F_eZ_yhcMhKIL71gNHSwSB8XleSpUprDPM7EsUtXkd4zgmhG6qZgRuc6kCZV8TuLP5i2RYbT9Ov5cqkqXCdm_thzQFJcmxXBccbKEZIJm26a-fcJqeCjEbRCEbEeXzu3PmkYDgXdcIDQT8k8wss4zjo7PRgEhratm0wDS5bZ3D5dX79CssnFQn3ynCQg4-GnPdDC-Jr7hD15-DMzNJbI18PX_GGbWKz1qe6ToxC3XC9qfl_R93o2G9bYRnswcP0VnZMVnnLBB5xq-GXPwl6OXxJ-yd9qvdiaM3V1V8h6fcxKrKZAq38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=haUAWqkdDp78fnlGbvrASnbqqlaR5wlwziviV2r71I9n1fXuTgHe_AguFTrodj9EohWQxbi0J1x5tWMAMFv3e1ugMs0mvA6s2T10sHecsF1jqgzxbrgwZhUEytlZkcruMz27kz_LUcAijr7lQTSYIWNToUfWvQ0gKlTNsWpFsSolJeDDxlPIbyLGEOcHZqCZ6YqbyS6peHEr-_jud7s-k1Yt9D-hMtYasPsdu9QKfc8D9z7-rZaDlr9cdTRvt58G-kG-NqXzcRnz2J1PcW2TlmDia7s8_swWIv8Bh54Y_VEZdMevby9tVAjx8ffRIHbQZc9jflWU_k5kFJjoO_mKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=haUAWqkdDp78fnlGbvrASnbqqlaR5wlwziviV2r71I9n1fXuTgHe_AguFTrodj9EohWQxbi0J1x5tWMAMFv3e1ugMs0mvA6s2T10sHecsF1jqgzxbrgwZhUEytlZkcruMz27kz_LUcAijr7lQTSYIWNToUfWvQ0gKlTNsWpFsSolJeDDxlPIbyLGEOcHZqCZ6YqbyS6peHEr-_jud7s-k1Yt9D-hMtYasPsdu9QKfc8D9z7-rZaDlr9cdTRvt58G-kG-NqXzcRnz2J1PcW2TlmDia7s8_swWIv8Bh54Y_VEZdMevby9tVAjx8ffRIHbQZc9jflWU_k5kFJjoO_mKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swh1h1gsdwhEigZWsvy4qWYRmzNjfNF-zKSSqhLeU8g_jVDX-0OjxcQLloZPHHCNPvc-hQOzn4BjGoaGtv5XRUbBvMv4tRjPcBQYleAJ9Lcgtv9qsOeD9Z5kvxu-hsPoWFAfc5Q17Ea7Zi1Yrug8rodE5IvfKV35_kGobve24pws-H43In_8-EYOhR355UMvGG6OqSDcHX9h_WBQQ4PT3IlFIYHV2EPcwnkkfoPOLRIHn-qFpKY5ktCEvPQ9_eCCYzmu83d7F5iy1pqlsshhT5E86HvP6hsKASsBRF6MOIqYmCgPKIJgqBfBwV5K7JxyaFg41HNpdzbbtosiOINOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=HNLx4VmNSomkoLudj6DO_LLinItcjLaRta9wga27-gjMg8eQ6pMGIQWBLdIHGcX_LDCsyUQINn1Pa8g3KIMLntORinLnHE1RP1Zm_bJzHEOIJfayj71cqSdDiIBK6NprbNRJHY3pIgARm6EDru-wh8Z6aKZdthcuEiHbx072B--aD8jk6lNRd7i6kGaP40d4iBUao5T3FLlt7tyeqBJyNfsiR9BBvO1e6tLWKiBQC3hxhrPJm1Xu1VtG2bxIKufL9kxK-EzzBcpfXKc5PIG-jZG8tQKDLJ-wSCBJeeTGWqLWGwVmTgQJOOewYetkMCmYutN-KqJgEJ9JoVH0E5UFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=HNLx4VmNSomkoLudj6DO_LLinItcjLaRta9wga27-gjMg8eQ6pMGIQWBLdIHGcX_LDCsyUQINn1Pa8g3KIMLntORinLnHE1RP1Zm_bJzHEOIJfayj71cqSdDiIBK6NprbNRJHY3pIgARm6EDru-wh8Z6aKZdthcuEiHbx072B--aD8jk6lNRd7i6kGaP40d4iBUao5T3FLlt7tyeqBJyNfsiR9BBvO1e6tLWKiBQC3hxhrPJm1Xu1VtG2bxIKufL9kxK-EzzBcpfXKc5PIG-jZG8tQKDLJ-wSCBJeeTGWqLWGwVmTgQJOOewYetkMCmYutN-KqJgEJ9JoVH0E5UFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfk3WTnkiO_SAWZ3cwIcd3NAXjiGK-Dj7r88e-QkbAYFz_S6oL3OzxHSath91q0kJF3uXbNMd0zRQ2kwJScSNjtnXql3zHXoKNpDkb3xhLMa5d3qIqa0y_o-FLlVeGhrN6UrQEagoPhtZw9Szij_s9LGkXWlK4D5YLYLo7U14VtnlRQxGkh4Ow_oDEXUkmS5-ZPmLbYHvxxTCcKvqUjZCQk52O-n03BzL2T_11mjXyHmZVmzVvfa2HENCef0gDZejWQO2IkArGeXuHX38RxPVx_53LASo6cEGywMvlAYq7y-qopQEeR6eKPTinbJ-myTCNol04496I5eZDTPnqViow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=VYkVgejVco6z1ebQH_Cbqs3sMWMGlvVXVKGb7TZz9V6-U1sQDyGpj_FoXaoV_DuFf0q9edKbZHYeaD0s6XfAmkrWgK6EIdEudVr56S6ixJcznSLTqtT53-KGXTXDitByTNHz3jmuJdGgeq6QM9RhKg5kfvLJVpd1cE0eHaT5URxY3WF2rT6c_oc_GnoyDfAr2vRoMCAcxci1D2bcbuFlMIHQne_z2GoEn9IgKDYfyQ-nAjs7xQRO9ZBbRQSrZZ98gBzdK-HpFqbRII_ZBAyYAl-zszS44C6wu3WHTtnMr3htrimVyYLOws-zoUhUS3GLzHHkdvluvLBtccX8mwU8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=VYkVgejVco6z1ebQH_Cbqs3sMWMGlvVXVKGb7TZz9V6-U1sQDyGpj_FoXaoV_DuFf0q9edKbZHYeaD0s6XfAmkrWgK6EIdEudVr56S6ixJcznSLTqtT53-KGXTXDitByTNHz3jmuJdGgeq6QM9RhKg5kfvLJVpd1cE0eHaT5URxY3WF2rT6c_oc_GnoyDfAr2vRoMCAcxci1D2bcbuFlMIHQne_z2GoEn9IgKDYfyQ-nAjs7xQRO9ZBbRQSrZZ98gBzdK-HpFqbRII_ZBAyYAl-zszS44C6wu3WHTtnMr3htrimVyYLOws-zoUhUS3GLzHHkdvluvLBtccX8mwU8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=Ap6gvmgpQWXyXFP_FCYMHA_1Ak1qq08xt7t9mrDVwkCUl_2l3yx_0DB82oAzyeX99Ou7k8gDZVJ15Rd6qL4MBrZOW4iKAtIcJvEU3BaATOKwp6pRMe5BCWKvk0tmpxq6USI1BynfJ42_sNQUsuANKMJRY49_1LlSCGHI3oIZM5LslC82oih--0HSdd3DaiGl1DAqlsLSqQCufJwaIuyq35udtkkGv3xURyGW_-DdCVIZ0RNYQjdG6eit3BauwQOHGjGsAdPw8UrvXIQ6mOmJ8_rMAFDgx_DyKgzCDlXjC-pmwbCYmhur9GQH-OiIR0F14Xytmb8iadBBDuJUOA6GDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=Ap6gvmgpQWXyXFP_FCYMHA_1Ak1qq08xt7t9mrDVwkCUl_2l3yx_0DB82oAzyeX99Ou7k8gDZVJ15Rd6qL4MBrZOW4iKAtIcJvEU3BaATOKwp6pRMe5BCWKvk0tmpxq6USI1BynfJ42_sNQUsuANKMJRY49_1LlSCGHI3oIZM5LslC82oih--0HSdd3DaiGl1DAqlsLSqQCufJwaIuyq35udtkkGv3xURyGW_-DdCVIZ0RNYQjdG6eit3BauwQOHGjGsAdPw8UrvXIQ6mOmJ8_rMAFDgx_DyKgzCDlXjC-pmwbCYmhur9GQH-OiIR0F14Xytmb8iadBBDuJUOA6GDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=e2ZHtWa0PkGJgUeOexFD2SfO33MS0d29Y6KKEK483ah5Amb4DyYFMcmFH2jZMr4tiqnXaeGLY0g5TjegrnjU0YpLiy6sb8CvcnyRn9PDDCJLl7M-LZs9-ETR6Rb9zUuvJZU7LqXAmaTdKbdLqHc4k3MMXd97DI1KqwgZhRwV3c-mZfEXqO2kuabh2O0_SG2pOPT2xqnZGMEzXxLsYWbqGor_pSXV6pj5y2uFQOfNNOS-UQEsO7b8mQ119dLhBOax2ZXQGIGZMgWnl4O2l6HaXfFfsQeHGEj9qWBDi5Ow0NUpOfk0ZE3umfpGnNvz86YswSiJZzPD0yANundD2Raj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=e2ZHtWa0PkGJgUeOexFD2SfO33MS0d29Y6KKEK483ah5Amb4DyYFMcmFH2jZMr4tiqnXaeGLY0g5TjegrnjU0YpLiy6sb8CvcnyRn9PDDCJLl7M-LZs9-ETR6Rb9zUuvJZU7LqXAmaTdKbdLqHc4k3MMXd97DI1KqwgZhRwV3c-mZfEXqO2kuabh2O0_SG2pOPT2xqnZGMEzXxLsYWbqGor_pSXV6pj5y2uFQOfNNOS-UQEsO7b8mQ119dLhBOax2ZXQGIGZMgWnl4O2l6HaXfFfsQeHGEj9qWBDi5Ow0NUpOfk0ZE3umfpGnNvz86YswSiJZzPD0yANundD2Raj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=f02-cGqlGLUeRFe5QO3OzI7-OFolCTwX1UCni7tz79QQIwctKhGOJASgPoVlaAbfnU4KktMmkCqiu5nLBaURJyWYyD30IoyaPDA3tXQk3C5tSCnOnkhdJJqwxHYPFofStYG5mIfmTLVFg17AZTVXMIrffwasM5VXQOSTNVAGxSvgPDiHtZRriEzJEymDErTimbbQ9KIrBW-F6f55WlrJi8C73_56Y6E9ypq5Zhs4r-dDHZos9IBYlMLzm9cTsdg_6tZ5ZUyozfrjXNyNmH8NGOcFApNIkRYt3XR43ugXnLA7zQ-GH2eJxdSfDoppBOqJ232ywMXLdCSoPYoiokdQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=f02-cGqlGLUeRFe5QO3OzI7-OFolCTwX1UCni7tz79QQIwctKhGOJASgPoVlaAbfnU4KktMmkCqiu5nLBaURJyWYyD30IoyaPDA3tXQk3C5tSCnOnkhdJJqwxHYPFofStYG5mIfmTLVFg17AZTVXMIrffwasM5VXQOSTNVAGxSvgPDiHtZRriEzJEymDErTimbbQ9KIrBW-F6f55WlrJi8C73_56Y6E9ypq5Zhs4r-dDHZos9IBYlMLzm9cTsdg_6tZ5ZUyozfrjXNyNmH8NGOcFApNIkRYt3XR43ugXnLA7zQ-GH2eJxdSfDoppBOqJ232ywMXLdCSoPYoiokdQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioI981fZ74inRCZvmJSfVfrpgVcVUS_iJYsUxGlf0Pn-PKshDvhBUuDqc5PC-WSwedIua5GpFeVI7lXTrqb6K3CalVHPzgCGt2k3v6I1hgTRFzvvPWE5ZaA3Z5gSK57PhqHaWgpx_pP0NHbw-acn4ymbGnn-8XO28_gkqzdDC8wat_gFWarNO0kQCUljYtJCsku3ves1kWVy9wgT3hgu0TgdQNHs2-RYXwQWm4p8xrzc60CQoZDxJs2vrHCIlxPVbOUd3WBhExXiE2VAi1v6jsMdLtJe3N_GKb5_csBeyIJpd_UYvklX6o-zzYpmIKVVqXgL4eqcwIP2ZpQa-oLIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmMNCAnHcBcDkm1U345nC-xA95Q91qYrks1r17dXIrBNKdtYMQQ2rqMbwhOJlZ4kvLA1gTNjLmp2B5OnkjFRLPoYCJBAts7C2fD9OfM8RC_IkMpgPS2rfEIwpN_ruQXuADiyZNHO-zmWIhaqP1vPoRnSJtqnvUs_WeCDl3HWiiwcpGDHmj3Johh2k3cyfID8Q_fkV3jaMnO-Oz0Xuu2TwRY9etgewxeHImtlbQxVUKwXrIVj8fckeMy6qJdaqO9PxOf2STWXX1sw3bhj5rzYACn4HCMu3durgtiIkjbfNqUzkj-UdPCnhFXNTx6BjtnN2qlDUd0qlMKdytS4T8i1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpmAssFX8leSS8-Wmr0Iv21siYUxonmCYR0YXL7D_sHSVqIcjLop-L2kXy9sp9q8q2DC1Rib42G9HAlrxhKGWkZcJ4EMHR7i3wQKqtdzZhdKDkgzuZJBr2PR871vIC9Yqs8i8jE3fOz7r0jnxRGlrC6R1A2QpYC5UQ8kK_0f-jFerCj8IjLMsJWqmVs-auvG9_KNax0Cu4MwF_Qy8wsKlE27Z4fr4-D8BM18OGTwR5BjRi6SIbBql4IPAwkxup5n5CJ55F7N5K3HqZWzn4TY6iDAWZ0QIov7eSFq37GXVLn_EebrX5xw0pvJwc0qj3orvilWfbUtvUt8NMdfTdByag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnnVIrvXdlg29o9__Ymw2SttAmRGB3iLHL8ZRSEYz9BjBU4w1WNGqca0I2H1OBD5Be0lDM1F-reT0yGzT3RekE_k_bvSwRZGHTRuqEAb1EyNw6Z0BIQaQbErx_VfKCa3DIVHWAri8CAA6jghr0a4-JNIXTzO5_uyyAjEzfnv6bjFrXVDUJb0fNZnQaOChwvbd6XR0ieMbeFec1NR5QVRRyGb4VBk0ILPdjXzrUs8EtErtDvgChO_K_5rPO2O8HUJsQ4WmcX3DTP7G2Xjn8xRxPmM3mPktoIvWwi0BZ4TXCDwYO9NWJfRYnx45iPE4Hm264ep1ceABN5qDgzeKidswQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd3MvI-26WaCt5n3bmic5VnSbY-qwFktGraAwG4XjdesQYsTtJz6lcOePePvgkpCSTgZnxKicOFSLDSyEG8QOeyPRwch6ky9sDeGyRcbczc6iS9bVkLrb0CKXMgkEnBjQZpTG4SUpDqvbbUmWzOrbLfpGy3JMBGzqlQPiBtW2ZcG-X5mQpL_B_KaHVslmeyEtNC7KiI885TYkuJlpZ34-krqJ9weKJ_2srtJicz8VU2mQeqXpgZz4GBCVN208czvH2RHDbUqVsFzIfHit1bQ5ILNXYqSYUdkwC4yoDRl-B8Z8r3XLWXBeX4U9oNZ4eTqehC4nMlROiAkw-jlkfNJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=o0kB4ftPw1_bOaNNd8hLv210e3MVD4P5FdAZ11fawP7IywFI-w_K1X0PNp1EGF_dHfV7psB9EhWV_nWNy3zhjah59rrIJm-Vq_80YQeV4SIvA5jnO_4XnXmrfdK3IWT7M2GOfIDCdx6N6SCPRX75q_SjYis4htInw9bzrKEcUA9N2MpwIar3dgYlmmrP5GbqPcGS-WMfFvhrlras8s9c6RRJpZdY7erQl2JPmZ_ysA-PzPsZRHYBHUbFBlbqKR6FnVIORm08g4xVXoL74WsmseIres5QS23k_mKQSBLDUBML1P2zWRdj-B7dSJvq-pmCsJE3yq8wSvkxKyraIxKhWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=o0kB4ftPw1_bOaNNd8hLv210e3MVD4P5FdAZ11fawP7IywFI-w_K1X0PNp1EGF_dHfV7psB9EhWV_nWNy3zhjah59rrIJm-Vq_80YQeV4SIvA5jnO_4XnXmrfdK3IWT7M2GOfIDCdx6N6SCPRX75q_SjYis4htInw9bzrKEcUA9N2MpwIar3dgYlmmrP5GbqPcGS-WMfFvhrlras8s9c6RRJpZdY7erQl2JPmZ_ysA-PzPsZRHYBHUbFBlbqKR6FnVIORm08g4xVXoL74WsmseIres5QS23k_mKQSBLDUBML1P2zWRdj-B7dSJvq-pmCsJE3yq8wSvkxKyraIxKhWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=juWI8Oo78XnVcweB4APfQQBBM3Eq_ypEwhr2_ufUn8sJgQrdPREL_HF6n63lGRQyvfNO4nTbsdo3xZKEZURFIzpNAwL_yJByVvEcDN5Iaslcvz8xR5KHBX4GP9_S5yHSAjAdc4Zakq2qbgJZdOr3zcKQC8nC_T8XOOYsu4YuNVjU3jm1iaxccNPSIc0VowZPql0gBz6yHTqrjuEnMLmR-cA1Q0Z2mmfg6jZvb4aMfQ9hMgu7phE1a5P12-H-oeL14lesAtFQXm1_2J2TIXko_J0386hQE5smhR069CTgwTqZQDrpC-fFkerUkJOhN3Sii_u200Atpu1-OzPcASCrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=juWI8Oo78XnVcweB4APfQQBBM3Eq_ypEwhr2_ufUn8sJgQrdPREL_HF6n63lGRQyvfNO4nTbsdo3xZKEZURFIzpNAwL_yJByVvEcDN5Iaslcvz8xR5KHBX4GP9_S5yHSAjAdc4Zakq2qbgJZdOr3zcKQC8nC_T8XOOYsu4YuNVjU3jm1iaxccNPSIc0VowZPql0gBz6yHTqrjuEnMLmR-cA1Q0Z2mmfg6jZvb4aMfQ9hMgu7phE1a5P12-H-oeL14lesAtFQXm1_2J2TIXko_J0386hQE5smhR069CTgwTqZQDrpC-fFkerUkJOhN3Sii_u200Atpu1-OzPcASCrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHL7SHrQ__H1LXdajL3DPUqP4uY_bkiWZEGCOO7FJeRxdrnVwMV6TuwwIFz9t1E7IimRcwtd_wYCBZAqsLZ3bqLmBTGuLF7XP8_fM-X2hmWx-SS4_ue49iOtziq4RTLe5WTcnmo5Vo6a66kYXxsNpCNuJiyM_LEUE1OSKYzFS_ii1AH7GtTgpF8kPsIR5R5-CeIzaY-WfZajGExVPigpQ8NAETlYDLBttLv0EmObJDIryMW55RuMehoJd9Ts3OWtxaky7447OUiE8v5w7XgPvsbhwbqWVKqkYVNVjhet3Od_XEk01jxI7EusQBnQBVVb_ou9mTWZdC36ruTa99q8tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZXFhMwHYiydAKhVfpzi5WoUpKA4cJ5XYDye-hcTXOhrPg2Zl5qlPPQ6bG-Lwxz3X2O6lxJlu4m9CPjnKBGRyD2rgiEcahfp4XRAZ1Ki9pGUvBwcihLwelirKnKNmJvvBmJ23hun9IEOJdq9qE8QlqWa_KSnFkGP88f8TbxjQUEJio8cbjlMWawDklDqkuaugg1tkLswu-ysnP6Gn0bL68yfnbR-Cuhdmg7GRkGbADo7wuLkEgeNQUA1CV_ADYu5fnxDD2SerGShYDjf3EcQMkQNH2CjxfLYh-2-nVy60f6k4_Z3AGjfBLLL4qaL3UQlie30DzGar-Tq8yBzU_-esQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=FC6SYx__Nl649xR4pYSw9SNhbVwQ7fjwDEvD-doHVyQdnn0pX-xwxXllWtglqWtWY8u8XYtl8BlabU5ya5taReTCevIIBtkJO1WzMHXBQWZbWDzhViauXMJIORxb8a3lVolJ2wFA91B0_tyILsPmuKTMDWYgCpUnqJ6RbehE65LQ1f9hag1dtcLJ3yYrLbZ0X5LeODlxzv8gFCRZ6vHUxiTBxAWzB019HKpyuM3BNtPohbIeqlP3zMvDwZigg0umg_T2W7NWTVr7x9Ht3KOCwIZNt8WdGfvJr62meEddUxlTMtRHNUxuDJcYecKGKhCXpxsJlpfWkbtIRFzNATxs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=FC6SYx__Nl649xR4pYSw9SNhbVwQ7fjwDEvD-doHVyQdnn0pX-xwxXllWtglqWtWY8u8XYtl8BlabU5ya5taReTCevIIBtkJO1WzMHXBQWZbWDzhViauXMJIORxb8a3lVolJ2wFA91B0_tyILsPmuKTMDWYgCpUnqJ6RbehE65LQ1f9hag1dtcLJ3yYrLbZ0X5LeODlxzv8gFCRZ6vHUxiTBxAWzB019HKpyuM3BNtPohbIeqlP3zMvDwZigg0umg_T2W7NWTVr7x9Ht3KOCwIZNt8WdGfvJr62meEddUxlTMtRHNUxuDJcYecKGKhCXpxsJlpfWkbtIRFzNATxs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=EtCoE-3hxrIuOKyG85T3yVlVUshc6XK8TCDineUC8tWNMelDFylHxO4OoMnpLWS35UhIvNJh6tseMonjYrjwWDAxwna6QLq6ui2jKBDRg1p1c_xMReT4pFGTvl3lTIKqY8ptLGJ0B7-_yjkroG0W6cCVQGTEBEnhYk8S2b_nN3C8re_BgUCTxeFiYfNzifmEdHGJcp3n_D6LBOzj-FqJihm8Cxs7JLLnhqiXkvii60H9o2MA35XzGLNEaWMio8-8vWCgmUwX5M73fofoh-JZ7hWU0UQooQBn2gx5NJ7o_NXxuCWSCNCoWrk5zMliziUfyvRRFietunr8MqKDnOaUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=EtCoE-3hxrIuOKyG85T3yVlVUshc6XK8TCDineUC8tWNMelDFylHxO4OoMnpLWS35UhIvNJh6tseMonjYrjwWDAxwna6QLq6ui2jKBDRg1p1c_xMReT4pFGTvl3lTIKqY8ptLGJ0B7-_yjkroG0W6cCVQGTEBEnhYk8S2b_nN3C8re_BgUCTxeFiYfNzifmEdHGJcp3n_D6LBOzj-FqJihm8Cxs7JLLnhqiXkvii60H9o2MA35XzGLNEaWMio8-8vWCgmUwX5M73fofoh-JZ7hWU0UQooQBn2gx5NJ7o_NXxuCWSCNCoWrk5zMliziUfyvRRFietunr8MqKDnOaUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=vRKh64WwL7M4kkCBjKGuvq9x4iVC0uy5oO0cWAfSt6lpZX36HR_U2JwVl84Wo30Ro5n5itxiaeB-okr-uvVcVHAh_frHwBTodo_wpsHUqtlyDq5tMLtUhIapaIxFzkWjLE1LVsxGHeSYtLw425IZV9cIPHQcL7Y-oxNsQCVdx0pB2SvzQzwbRT2jrOd6uvyXkjk1YM7OJ6wPwlhjow1WraSRyodoq-7D0_xEgE0fQ40AAyknXjU4LgAyg3a_T6CjWt9DR_bpVLYHS8fNn5ErGkIoMZM6DEGMmhk-rEmznOrchOUHgyP4vNiQHvvKa4eogiTBh_3HnC3aq3uBPF-p-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=vRKh64WwL7M4kkCBjKGuvq9x4iVC0uy5oO0cWAfSt6lpZX36HR_U2JwVl84Wo30Ro5n5itxiaeB-okr-uvVcVHAh_frHwBTodo_wpsHUqtlyDq5tMLtUhIapaIxFzkWjLE1LVsxGHeSYtLw425IZV9cIPHQcL7Y-oxNsQCVdx0pB2SvzQzwbRT2jrOd6uvyXkjk1YM7OJ6wPwlhjow1WraSRyodoq-7D0_xEgE0fQ40AAyknXjU4LgAyg3a_T6CjWt9DR_bpVLYHS8fNn5ErGkIoMZM6DEGMmhk-rEmznOrchOUHgyP4vNiQHvvKa4eogiTBh_3HnC3aq3uBPF-p-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=gplP_4pAmoDs5lj-F7qWaeW3N5Nz2unpeWMDxWU27PCzorgqs7phwU7lXa5k1JVh21norMJnxQDKAFrdy119wc8lURVUgBaJi6wLRyVeIT-zgkYN_8RoPbgNOQA7XDqfeICdO9YGvMFIqRTZLp8fxHx5k5feq5Ca8l6oQ3Hq6zjx93I8fod-O2vE7lEJi-e2aTGQ30iUs7QbNCtXJ7TILSbkUAmT3ge9D7Ef_f0Eyn9tswV8vHEDCRSiWHXuWjmW26e9Z2JPEf0YbXWPJUhWYRUREe5XgbbGl3XtKe13SdYgFD_xyxxQYDbkImSqytGJNcxMJi2TM4G1AmVX8w0BdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=gplP_4pAmoDs5lj-F7qWaeW3N5Nz2unpeWMDxWU27PCzorgqs7phwU7lXa5k1JVh21norMJnxQDKAFrdy119wc8lURVUgBaJi6wLRyVeIT-zgkYN_8RoPbgNOQA7XDqfeICdO9YGvMFIqRTZLp8fxHx5k5feq5Ca8l6oQ3Hq6zjx93I8fod-O2vE7lEJi-e2aTGQ30iUs7QbNCtXJ7TILSbkUAmT3ge9D7Ef_f0Eyn9tswV8vHEDCRSiWHXuWjmW26e9Z2JPEf0YbXWPJUhWYRUREe5XgbbGl3XtKe13SdYgFD_xyxxQYDbkImSqytGJNcxMJi2TM4G1AmVX8w0BdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=ev4lSOmh9og60KfIgRk5fWWd9f-AoGae1nIySvewfxxUb2TkWKMviwPifzkCW_dRyK88wZDnaMTdHJVbrerwpAwTVXYzFwP4JcjaAPk0nxVn_AOGtiwFPrFFkBSnlRCRKsm4BGYwmeFtff_Xoo_od1Kj1WjQjzLPblbE7m8QbLh6hcwEtGybx7UW5Ld42F7mOOh3jjv_YsUQ76Syf4hOfvAY8iK1pg7jC7v0MPmsdh7oVCsl5nbeeEdIm5fcpUq5JYsJkfr0Yc5BWzl8I0qZtE6MkUXKkJ0pnKW1TLHmVFGwd0DdldDMWJRgl_9jaWcI4CMNkVk1yWrESgUu2KFJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=ev4lSOmh9og60KfIgRk5fWWd9f-AoGae1nIySvewfxxUb2TkWKMviwPifzkCW_dRyK88wZDnaMTdHJVbrerwpAwTVXYzFwP4JcjaAPk0nxVn_AOGtiwFPrFFkBSnlRCRKsm4BGYwmeFtff_Xoo_od1Kj1WjQjzLPblbE7m8QbLh6hcwEtGybx7UW5Ld42F7mOOh3jjv_YsUQ76Syf4hOfvAY8iK1pg7jC7v0MPmsdh7oVCsl5nbeeEdIm5fcpUq5JYsJkfr0Yc5BWzl8I0qZtE6MkUXKkJ0pnKW1TLHmVFGwd0DdldDMWJRgl_9jaWcI4CMNkVk1yWrESgUu2KFJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=WuR5TW7bY1-2xPPtTcJrxhrJ_1CPeNvP0woQCLWR3PSaomAAfizRtPFOUX8-SAkqbdu-b1t5cM99Y7dtvv6728Sc6P5MLuXFpemm1sP_vSWTny6qFRBaj3ObOJMgVVvZioojUKXdzoNpwvPKojC3W-ztYofbQblTPgY8YsCPFjbmJ_mXEPG0EwDUMy2OsYDyuCyA7wrUZIo-2uaQgJrccLuizjOBxjsYQb3_VNeFTtVXNuX5SZOm2R082ryN5rmUurqwDhbdFm6N_nsgVi90WSq3O8CbzfNAZoKhiPTF2rXDSXbKHb_BXIGezzUKnnjadZ5uqfrfvMQN1Sq5QK4-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=WuR5TW7bY1-2xPPtTcJrxhrJ_1CPeNvP0woQCLWR3PSaomAAfizRtPFOUX8-SAkqbdu-b1t5cM99Y7dtvv6728Sc6P5MLuXFpemm1sP_vSWTny6qFRBaj3ObOJMgVVvZioojUKXdzoNpwvPKojC3W-ztYofbQblTPgY8YsCPFjbmJ_mXEPG0EwDUMy2OsYDyuCyA7wrUZIo-2uaQgJrccLuizjOBxjsYQb3_VNeFTtVXNuX5SZOm2R082ryN5rmUurqwDhbdFm6N_nsgVi90WSq3O8CbzfNAZoKhiPTF2rXDSXbKHb_BXIGezzUKnnjadZ5uqfrfvMQN1Sq5QK4-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
