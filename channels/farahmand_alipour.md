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
<img src="https://cdn4.telesco.pe/file/Ml60COLT4KvrJfA0juPT56ekKDYD0K1jxhtZUhtfJqFK-UCY76e2lOuDm24viKkLcQOnXM4TNYzXqWKwc_Q3nO9I_RiwHBrDvG2iHiWimnW6gOuLorekljARWFI97qk2adis84d5jc3yhHXZnS2lKqcWX_v6cH8EinJ-DDHOZO-NdxPLccz71HhY57IcZOwo7BWF50VrzgMjvVzbDsN3z3PVlHXI4N88BVFaBwfEntu4VOrhyspxVEnxVbGAWaoO_MO2DdkGYs68OSemCifrCIhSc_ZOZcSr4ZwnBlKfBgIEjskr7UMRFkWOnx3JQivtQjvSi6iTIuk3xHlMVNScUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=jZQPllj9zplsVJ6WXyXPgbxYIpBMfzupXgeycxHR4RSxdb9Kh6p0oCKDwp_9MLv4IQwvAqEYcb2v62am63iM9vQSgvv-xkVoi4Ba3vIsM6dOyNB-Kz5ItLfzGtspQaRB7KA4yNJQT2aifvn7OYdmdBba8pac5Ib6ItbdtOT_yZikQ1adr-x67toVlZf2Fxl4Pzo_VrJm8ilHujvk7u3XSbwAlnhednqtMYmnKZt7K5YqVWVLlbpHzHt2kNXoYIzsXsWFc8BGk3tGnU1SFhTh8ptKR7jufqJn5DWFukepEMnR_YyP3D_rOGYMhy5FwMhG0AZ_SboXOCt_tqmngUTRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=jZQPllj9zplsVJ6WXyXPgbxYIpBMfzupXgeycxHR4RSxdb9Kh6p0oCKDwp_9MLv4IQwvAqEYcb2v62am63iM9vQSgvv-xkVoi4Ba3vIsM6dOyNB-Kz5ItLfzGtspQaRB7KA4yNJQT2aifvn7OYdmdBba8pac5Ib6ItbdtOT_yZikQ1adr-x67toVlZf2Fxl4Pzo_VrJm8ilHujvk7u3XSbwAlnhednqtMYmnKZt7K5YqVWVLlbpHzHt2kNXoYIzsXsWFc8BGk3tGnU1SFhTh8ptKR7jufqJn5DWFukepEMnR_YyP3D_rOGYMhy5FwMhG0AZ_SboXOCt_tqmngUTRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsuMVwbycOVcKxuIsl8NhNoah4C8Lf-fvDjm9Qx_apRKyHEmvAOY39Pg_XtQb1s0Satath6r65ylCGxZ0Epe7_A3YyqakeYvcaNRozmd-hDudHiUXQRKs1VL0pCMueM9rAIHksMWSYN7-rYaqPGiaRYgXmVuLk8iRkye2Zv-ySE90tEjfd82Nc_I_suh4lAZd8Y0O4CvgtAWQsRiYXGALnytfvYIkHBZObGkDGHWta2AkziBjcfS4twnE6A-rCgYSZiCWLNL5r70ggzVB2fJ8frEXWYv9IBkZL1kJsacTZCGSp4ReGAROkc3slwLZO96LRaYHpJpCi7kGWhGmtir6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk6fphPF7k3GAXKniH27qXUdVZijx136CtDbuOAq0OBZEl9OeXV1Pszr9daS0G2CH7aZMkw5Cn2ftqgqBFI4q-_pniyjcykRvEc8RCyseJZt_rivU95z_joaDJA0kSXzjWWE9MuOV2ynElWJp4Nw8b_BGD5hicnT5klD_szuGWAqr7L56R5zdYGVTgfaADOXjoigXBmPO5uG6VRKYmg7RH6f8epGoGniHMmvlhFXEywxgpwsyrqOk05qGkmW_rwSb1hgG3VWuh5Eai26eQP9fdm5OHFXZDucPZf6pPOeVTO9aTzm4LdEq0YgJGlz7G47N41UbH4QlR1inWtAc3eCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6brwnxT1KHRZ1oIIDlge8EKLDpyqE-k5ojbhuIWve_P1e2hOaIzxcKxiYFp5t_FKUWpDK93JPKxmsD2f9k6VpK0Q7ylFw4QKPoUsrx-RBwlbZBCg6iQgc3XcKEm8V3dgdsKMgySEi-Vgl8_Gz5C3LGc4A6HOSH8Uir-6h76-9Ds_MNPGVJfsmqXiQUQ5oU1dH6VVKyHmgEuX0F475bYz31iR3JP6LKP2_6sp5s1CgrKDRB9XR2UOxtOPswelfiiWpcM5ZEy8OSMjEXVagRH0O2IvzOrA63mfo2StM3Rg5GiLMqgPOXybErSYq0CYEWR5g6WEXZRhoC95X2JTmjGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=tSDsIf-dHZ02EpPi434NKBAuIb8E_UzqBzv4j4XoBQtidXyZlcrqIH4EBdazaiHtcQJp4N5q7DZIIasRnN9LDUCel4YtQtqu4k_vzaPuFzNm0ECXAiOyLjmwAmA58j_Goydg3-hrZx5CFE5erQ2JxxhEmsQHJOm_FNSWhTLfbqLsOlghobYZrNtAVfttoUfxnjlSShJ_cQprC0ZVfEK71QLLB325WhyETBELi7P7XB6DMz4unTeaDKBV9QSatuF5gJHhp-NW9145mHVQDpVC1GOBid4eODxx3iNqClXP2fF9bc1suyhLi3qNvKSicf1hQ6cJk9FevnHwSHqL9whHLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=tSDsIf-dHZ02EpPi434NKBAuIb8E_UzqBzv4j4XoBQtidXyZlcrqIH4EBdazaiHtcQJp4N5q7DZIIasRnN9LDUCel4YtQtqu4k_vzaPuFzNm0ECXAiOyLjmwAmA58j_Goydg3-hrZx5CFE5erQ2JxxhEmsQHJOm_FNSWhTLfbqLsOlghobYZrNtAVfttoUfxnjlSShJ_cQprC0ZVfEK71QLLB325WhyETBELi7P7XB6DMz4unTeaDKBV9QSatuF5gJHhp-NW9145mHVQDpVC1GOBid4eODxx3iNqClXP2fF9bc1suyhLi3qNvKSicf1hQ6cJk9FevnHwSHqL9whHLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=faK0g3iaw0E_ReVuwOV9-C8sc4doK2rjDn4ONdNtRLNGU7HUaTEPHL1uYmExONf_o5427JUP61M8xvehREMnUSAdkrSrruMUZCRh4XX_Ow7pbJ_ZaJGwc3sK8Uzq2IDvmt071fN05QBth_abCpfg7joTtftaJGUNtXJbWRUtRIwo2jVDlWyRnF0vuTFp_f2v_mAQ51lR-UkdMQSqzVRwCRzUDOSC8aafp7GrMQ2dwidw12LDn9BLltiSNKrHCdLXgtxp9k6t8TTZTIGVdpixBs1g_ljIfHzt7_s_rXqRDcZtdirClJxs-3mYPbhRy5fOq5Ujx3xO_vRBC_v81Wz8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=faK0g3iaw0E_ReVuwOV9-C8sc4doK2rjDn4ONdNtRLNGU7HUaTEPHL1uYmExONf_o5427JUP61M8xvehREMnUSAdkrSrruMUZCRh4XX_Ow7pbJ_ZaJGwc3sK8Uzq2IDvmt071fN05QBth_abCpfg7joTtftaJGUNtXJbWRUtRIwo2jVDlWyRnF0vuTFp_f2v_mAQ51lR-UkdMQSqzVRwCRzUDOSC8aafp7GrMQ2dwidw12LDn9BLltiSNKrHCdLXgtxp9k6t8TTZTIGVdpixBs1g_ljIfHzt7_s_rXqRDcZtdirClJxs-3mYPbhRy5fOq5Ujx3xO_vRBC_v81Wz8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=MoiD2CRM0WVO0UVc5Tkqu5FBcyaTp_hpnbeIWa67QBnV0uFIs-x9_qFZX_WcM-s35rFP03irndjJf5bw1tqyJ3rPUUKPCTnrDv4XyctorrgOt0oVTFh9DgrcaMnup5fGgsi3sDbt9hHiFlTpulIaBOQ1tJXFO5cfElstiqXy3kTigXlbP54AzjWIU26RgJW6jaqJkP2k1RgW1daO6qrN0HWXFlPVFTc-NYaLwQpp8S_hT17yZDarlPb-iDTND-xnJ_7zA-dC_7pFpVYYIrQdOGhXUayRW-M8wuU1UsK-l9UskUwzfW3onV2hvxdENs6NsxWQDlz5GDR9U0jhglUnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=MoiD2CRM0WVO0UVc5Tkqu5FBcyaTp_hpnbeIWa67QBnV0uFIs-x9_qFZX_WcM-s35rFP03irndjJf5bw1tqyJ3rPUUKPCTnrDv4XyctorrgOt0oVTFh9DgrcaMnup5fGgsi3sDbt9hHiFlTpulIaBOQ1tJXFO5cfElstiqXy3kTigXlbP54AzjWIU26RgJW6jaqJkP2k1RgW1daO6qrN0HWXFlPVFTc-NYaLwQpp8S_hT17yZDarlPb-iDTND-xnJ_7zA-dC_7pFpVYYIrQdOGhXUayRW-M8wuU1UsK-l9UskUwzfW3onV2hvxdENs6NsxWQDlz5GDR9U0jhglUnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=UBEe_M442AWd78rQupRV5d5Y48940vUk3xo4ZQNBqCppfPg-c5P-EG0Cd_4llzsTJZp55V3cuxt4wMlFhrWWXdR8r4sNB0Gwx7bOAVxB3O7G-orxFmKCQ7fj7JWVWtmjeeN1oZfejWS-aOagZM6kmpHSEXE-gKeHv3F7u6mpMSfnxxR5JKdk8PzFOanfM8aHQrKjTz_0bI-eTfxzY7Tgw6iasr0SRiz2GZ7Vjjs3dCXoqLdsV2Siqt_WcF7sbVBlFe4H1tzS9bj3cqLrS4uEtm6q3ymLphFIGRXKYIZg3k2RGT-3mF9mUnfhp8yUzikBkwPnbVN2kVX-JLjlrZ586g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=UBEe_M442AWd78rQupRV5d5Y48940vUk3xo4ZQNBqCppfPg-c5P-EG0Cd_4llzsTJZp55V3cuxt4wMlFhrWWXdR8r4sNB0Gwx7bOAVxB3O7G-orxFmKCQ7fj7JWVWtmjeeN1oZfejWS-aOagZM6kmpHSEXE-gKeHv3F7u6mpMSfnxxR5JKdk8PzFOanfM8aHQrKjTz_0bI-eTfxzY7Tgw6iasr0SRiz2GZ7Vjjs3dCXoqLdsV2Siqt_WcF7sbVBlFe4H1tzS9bj3cqLrS4uEtm6q3ymLphFIGRXKYIZg3k2RGT-3mF9mUnfhp8yUzikBkwPnbVN2kVX-JLjlrZ586g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=XW-vUvubv7FXfETlo7Mn0YYjRhwIMHFVwsS53ZgYk1LmuQuBUtYb93Zk0Trzi20azMyn3KP8vZgD_etrPi44h-STvIjN7KJlXiZVdn9qigZQQTk2dqiRuBNP-nDprdWKsyw3hPidMqVCgkn7I4jFaV0wmFbLMbKIxWjjYSO_Bo0N_IP4p5pa_8LxpS1jI4qilfsVTLb-DB0NWKAvFY7oW-jCqVDprg21bEcG92ovQuwCIROc7mAzWkzPBZPQGlyXw-dha5r5qDL6mhNbZvRWmmoSNLMgA0z4ah0UIqOEJmKWk_OSD2z9DJrWToJuwetjM_Fs0RFCAeaguIcVvmkXRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=XW-vUvubv7FXfETlo7Mn0YYjRhwIMHFVwsS53ZgYk1LmuQuBUtYb93Zk0Trzi20azMyn3KP8vZgD_etrPi44h-STvIjN7KJlXiZVdn9qigZQQTk2dqiRuBNP-nDprdWKsyw3hPidMqVCgkn7I4jFaV0wmFbLMbKIxWjjYSO_Bo0N_IP4p5pa_8LxpS1jI4qilfsVTLb-DB0NWKAvFY7oW-jCqVDprg21bEcG92ovQuwCIROc7mAzWkzPBZPQGlyXw-dha5r5qDL6mhNbZvRWmmoSNLMgA0z4ah0UIqOEJmKWk_OSD2z9DJrWToJuwetjM_Fs0RFCAeaguIcVvmkXRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=plG_REiBtIuDzTpZNbTndy00ewsuzLbbjrEzHk7UFRsXmIGz3dAe_CIKFKFPydAz2_qClQ-FAPAbAvVkTwrc41vb6zNvfDK55d_N3gV_lZXxQ_Z_M7rHYPRLRZSzTmZ2FGDiw41dzE84mkX7bgPfQ0V9eyhsbGLyNCjaVLxHb4WnrOFtTq3IFwAYhZjTtJ24gY21AnUTunyxSZn7KbUMmri8z60SPKVESOFykXdL5KH4sQCfKGU6u_qYN4jl1BdFVckhyGq9j4pMx5YvAqUYWHL4ZUmbNK7v_jiS98kzvvqq3SQAQK_yvT1SHv1TwZgkr1mvPHGGxGOVN2hEvjxJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=plG_REiBtIuDzTpZNbTndy00ewsuzLbbjrEzHk7UFRsXmIGz3dAe_CIKFKFPydAz2_qClQ-FAPAbAvVkTwrc41vb6zNvfDK55d_N3gV_lZXxQ_Z_M7rHYPRLRZSzTmZ2FGDiw41dzE84mkX7bgPfQ0V9eyhsbGLyNCjaVLxHb4WnrOFtTq3IFwAYhZjTtJ24gY21AnUTunyxSZn7KbUMmri8z60SPKVESOFykXdL5KH4sQCfKGU6u_qYN4jl1BdFVckhyGq9j4pMx5YvAqUYWHL4ZUmbNK7v_jiS98kzvvqq3SQAQK_yvT1SHv1TwZgkr1mvPHGGxGOVN2hEvjxJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=A8cE7frJgpnq4-rwg2xzp8YiWXSVuLpSqYUNXzpSnqTRxDOqG_LlFli2wJYCA-QGjmexGfhoNEhgWstOKuCX4jQr0hqMDleq3bNfINFXtyYH6jaCqSJ7m7j4KMvWpfUlG6ZSFuUlC1o8HxamQQHjTEey641z8SOz-uCTZ0qlr0iWjUM9Bb34VNed3g-RsfkAzCfrw4hR2HussNiYeL5jlwIQMI_83fUdKE948UYSB0sccoTs-UVrMrsOSGffavT7_lv_qSg6uFcDtb53w9hLDzJuDfpRKzrtGxKvrPzIdtIKzpHk_BqJKq1fQeQJqX4Iv5Wo0NUSe48puQOTSUi5HotGXme6XrKB3wEUqxHKWEagxhdhUDSXVkCbaDi63lZoSl6ss-ErVU8ALou3EnsShodoAR-yDeB8Ke7HNbWqGuW27WwFSyCAZUll4_k7c0KpMiQeMvx3ULGaXfc5iaVVF_HWS4YJ4-0byVTzs-IcNTjqDeeIceFbgA4z23cpJXpoIseOLjophSUjP7A4NQMzcWP5qblYtGKyxVrTvyBkuGCVT619UVLqDcKf5j5sSlXc5HUgVbonx1GG-d6dqSVD1Iv3exCb3Q0OiJdxFWcJ8LMvdkhIBy66B2k3NjjaMiybywEx-hLc3-FLxGebW8TH5xI4sRYwjuTenf9aq37lIAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=A8cE7frJgpnq4-rwg2xzp8YiWXSVuLpSqYUNXzpSnqTRxDOqG_LlFli2wJYCA-QGjmexGfhoNEhgWstOKuCX4jQr0hqMDleq3bNfINFXtyYH6jaCqSJ7m7j4KMvWpfUlG6ZSFuUlC1o8HxamQQHjTEey641z8SOz-uCTZ0qlr0iWjUM9Bb34VNed3g-RsfkAzCfrw4hR2HussNiYeL5jlwIQMI_83fUdKE948UYSB0sccoTs-UVrMrsOSGffavT7_lv_qSg6uFcDtb53w9hLDzJuDfpRKzrtGxKvrPzIdtIKzpHk_BqJKq1fQeQJqX4Iv5Wo0NUSe48puQOTSUi5HotGXme6XrKB3wEUqxHKWEagxhdhUDSXVkCbaDi63lZoSl6ss-ErVU8ALou3EnsShodoAR-yDeB8Ke7HNbWqGuW27WwFSyCAZUll4_k7c0KpMiQeMvx3ULGaXfc5iaVVF_HWS4YJ4-0byVTzs-IcNTjqDeeIceFbgA4z23cpJXpoIseOLjophSUjP7A4NQMzcWP5qblYtGKyxVrTvyBkuGCVT619UVLqDcKf5j5sSlXc5HUgVbonx1GG-d6dqSVD1Iv3exCb3Q0OiJdxFWcJ8LMvdkhIBy66B2k3NjjaMiybywEx-hLc3-FLxGebW8TH5xI4sRYwjuTenf9aq37lIAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=albaARGDr9MhOa8NNUjwho7k4J2ZV7tytk_uR3-VaaWPDu9DdGH4OGBgunKIgBsIXSaRPqMvedubnZXkq-3cinew6MwiljyH27_ZNmWdAfE8noe2aBgqS-uW0cEJtM6GTRn6wUGtGsfWxn1vDyBSOFp0py0uOlvYFG7hsfXfFJ_qYUN5yzzUu4rIlSehWwg64LFRoaU3NOdo-65qYW4630yY8M_xcZ-5lyb19DDMIYcvoQaZ-Z0U86F4btL265UW4R4vP7Hx7C0GLQmhyCFBiFoIXVlAKEEgxeM7aRNiqAuSheMavoYmnRlFWudAVVi6LIdpG8r44iaHLvDpcE_N_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=albaARGDr9MhOa8NNUjwho7k4J2ZV7tytk_uR3-VaaWPDu9DdGH4OGBgunKIgBsIXSaRPqMvedubnZXkq-3cinew6MwiljyH27_ZNmWdAfE8noe2aBgqS-uW0cEJtM6GTRn6wUGtGsfWxn1vDyBSOFp0py0uOlvYFG7hsfXfFJ_qYUN5yzzUu4rIlSehWwg64LFRoaU3NOdo-65qYW4630yY8M_xcZ-5lyb19DDMIYcvoQaZ-Z0U86F4btL265UW4R4vP7Hx7C0GLQmhyCFBiFoIXVlAKEEgxeM7aRNiqAuSheMavoYmnRlFWudAVVi6LIdpG8r44iaHLvDpcE_N_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=qYYeS0li3D4DojKiuJ8sOGrGnSbd7anGB2F-Jwoza7nWQMYo2-sCFnsR6EaEf3GGhPeSsrSBRUn8UqU1-v0fHL6DJ7x39Yopobskf6EottBKhFDLIPenNctvixD8ZkkJtnZctX3jqwQJLM4ec4jb5dCyCdG-nRrjQoosf-ui74ErJtIr7HzN-kXNtdFMfpUdlYeH2GBCEXbPMKP_XYsNul2-V9PjPVg2gqv2ljNCH1Tf31jaU-0cMIyzHAIMt9uxk-GrqpaYf8CbSyyhlFZVrRsaqcXAc0B8FwQgZn9Z9YNtH-F2O6n4dpFZISfiAHthpHhlWob1E3HQ7Ha60v4dzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=qYYeS0li3D4DojKiuJ8sOGrGnSbd7anGB2F-Jwoza7nWQMYo2-sCFnsR6EaEf3GGhPeSsrSBRUn8UqU1-v0fHL6DJ7x39Yopobskf6EottBKhFDLIPenNctvixD8ZkkJtnZctX3jqwQJLM4ec4jb5dCyCdG-nRrjQoosf-ui74ErJtIr7HzN-kXNtdFMfpUdlYeH2GBCEXbPMKP_XYsNul2-V9PjPVg2gqv2ljNCH1Tf31jaU-0cMIyzHAIMt9uxk-GrqpaYf8CbSyyhlFZVrRsaqcXAc0B8FwQgZn9Z9YNtH-F2O6n4dpFZISfiAHthpHhlWob1E3HQ7Ha60v4dzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFns3kcnArCS_Zju2LovQv7wyGtIuHNtTCaeWmFUh0QMIJyaeHhnJamIiV0e7Ag2mf2E7yTg-XQ0a8KC6WIND4POEBZt_KKL6_2TF5Mg2HnsPBlm08t_7Qz4iUgS7VLbUAE9HSWNuFpMsippTpgD2kOgqnRAz2EyGWZ3E96m5hxQL4eOzphOdtz1AjBA4qe2K7Q3w25vJbqZ6yApggNUQi7GAIhQ0V8tlCgRxKp5Jqm79UYiqd78EUx8K0tcvKGqAHtfUsMZlQbDsBhKn-3Gf7ykteTPjug90B4qUv7Qj9D0p7CQh-zibtnkFXrr8XzAxT-1UqMfuMGNJ4B42PPH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7C7uqboG1ssL34sdQTfHnxjBqPTIn7NPWZ4-bxNe7jMifFhVf2O2vFha0ApumkOwFXTp4kcqKHDLUWK8ExekQ8F6gusj5UWglnORuTGa1vbvzlzBvh26zYtJ8n8aUWN6RmjISb-5oXOW6pERZqisuizhm9X_07XgPMrtldyeNhW4Mbf2SKOD0U6GhroAs-33ATOQfrwvB1RQ7T7ni8SGgQL-bbl02pbgd2Ounq9e4m4annv_8JqGDeDl1J1JNsl3NWI1taC0IQshANiMx287d9WXdQrgPPT-YezJBluKaV4wajG0Q46WeXQRE4WURQC3qqT15XhUKkjZYWpXv60BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xhk8p4oi206N1d7bYariTpTM_R9rIjuUJDlFGhiRXY0MEbQFYt0p6TylrK2XT29niFqAPtO2sm28hPgBHIhkUcFBuvTVG9HMe1exH7eMotdCI6GSJGNHmsof8UH4lIUhGtCWPmknX5N7uRo6swErMWkW6HJads_hB9hXvDJKK_ihBhx0c1-BXvB2OSWFZAyTuJCMJsxZ9Omi7kVrUxdyWmSBxhlIoa8FE1DDkUjjDwJLeh9w9rvXGHZRRetkt0QyYnO10vF0G-Tzy5t5UPr-UxZdnWpBpIBaNZugAJiLF1FNF5SM9p8fNqdnDLvWoJFNe3TnDtRAp7ssa9Vj8YLhlQWkcaUIlXHrBQstgYFkYYvUVlIiWUQj0SQoZyxO2QuAsHCR-4F2oJ_6xFwM2efMs0mthOlwHzdZZNGpAYYgr_bymUMbVu7TSs5cOFHM47_R5cUo9SvlG7VpouK7vqK4COoLOOrkXRlG2coQTTmgHbLlT3hK0t7EdTHeYUzgcL4vtp8LXkGRovJH4WDRbrsQXI2dEBiwPdAYON0_YF4p9_nOtT3T2kSSyNb458RMQoivg80SOStdheqmI8rVrQsf6p2morZxR-G6N7ri8ulpg4omfFvDT7zgPz9flpaZWsPkQIFlUwjMRfDaM83EFXEXcjwsDbdF2mS8z3auiGRn5yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xhk8p4oi206N1d7bYariTpTM_R9rIjuUJDlFGhiRXY0MEbQFYt0p6TylrK2XT29niFqAPtO2sm28hPgBHIhkUcFBuvTVG9HMe1exH7eMotdCI6GSJGNHmsof8UH4lIUhGtCWPmknX5N7uRo6swErMWkW6HJads_hB9hXvDJKK_ihBhx0c1-BXvB2OSWFZAyTuJCMJsxZ9Omi7kVrUxdyWmSBxhlIoa8FE1DDkUjjDwJLeh9w9rvXGHZRRetkt0QyYnO10vF0G-Tzy5t5UPr-UxZdnWpBpIBaNZugAJiLF1FNF5SM9p8fNqdnDLvWoJFNe3TnDtRAp7ssa9Vj8YLhlQWkcaUIlXHrBQstgYFkYYvUVlIiWUQj0SQoZyxO2QuAsHCR-4F2oJ_6xFwM2efMs0mthOlwHzdZZNGpAYYgr_bymUMbVu7TSs5cOFHM47_R5cUo9SvlG7VpouK7vqK4COoLOOrkXRlG2coQTTmgHbLlT3hK0t7EdTHeYUzgcL4vtp8LXkGRovJH4WDRbrsQXI2dEBiwPdAYON0_YF4p9_nOtT3T2kSSyNb458RMQoivg80SOStdheqmI8rVrQsf6p2morZxR-G6N7ri8ulpg4omfFvDT7zgPz9flpaZWsPkQIFlUwjMRfDaM83EFXEXcjwsDbdF2mS8z3auiGRn5yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoiWDHY3Kvkg_-VGHLYMlGV0-CsfE0va6UdyMwWmUwkv6w6tJu-Es4bTxYu_vRuTv1teAXX-oXCrX166ZrJLF64F009ZrWtFBWkXFaz3DasXbd7dOJjHY2EDPPdZWJHDuKLwcxbBT5GIuPo8Jwao5vjUslKu9IzkVYO3CkAWPPnFRw970uGiNCYk0-4nu71zU6VBVQetAu7tBEOb3-lcDmEtByzEEbXRp-KLjwlf1YnJ2wH0CVqwmw8cTpwt-11RLhGwisyX9ETH6ROvZ25WIAONJ8Bdf7HCqM6RCoI9-zNqXUZLuUJK14m-C1k9aVu4ViOVYPj8JYRR8psTV3JIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGmGxa7FjrjVeab4HG_IlwDlz94ieXGwTd133Ktk0lQdKq_TvjPo8Bqwsagh2vh5tibb9FAFYe4csdqwn3ySDP5CknXs3QN2BfHBI7tEkP-WtwNinvCv7ZI3WAA0VpLXjtXYhQU04vzpcHqiI07YXGU134TmCmpp6FjFBWuUyk6e0cvrty88CeTz8d2-dDa_h_vypCBTCMkABwtV8RP9QRUfcD3m9ilUZ7taaO9J6o1s9SkFLa-Zab2tUcJQjywe-HJQwpah2ceTqQfo9Bx7WeGR3BDGg9iqmhpc0h7XIf0HrhItO2PswQLQtQXt73Aqp7--SO68KC-YcFL53ghO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noYlJNH1vux9sZFDIc4WbJUKpPg6Ri8bjgtN-eZuKY6N1QmN72w5ztrQiDf207cbCaGoBP6dq7ROzjrZ36HgatKIjOC0OuLo8y66T0bUWXAgDrY0hIiIB59xyhSf-9kMftCLOQOqu4OGtrJ3XsGATfAIkdoSo7ntS1C6BS-kRZqfiVBzUZNohGUQR-KAnqbt8S1TIf8ETiIELMgkZrzmv3-WWnA_z2ZoDTo6UXqNx-uomtCSGqTn_r1ti_afbO_2XzcD4iYmVDqMS2fUlvxPTd6qhKkzmj3lCh8rnSxTr9CU8e5jCjhi2aF3JDWkgBuX8crs-ai_tBhixdCCkJ7SNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGghipYoc-EM0m6wNcW2xzuQZroogLlFjf3jnPkGiGa0a-rxAe-Zj3t4Rv4kFLQCCDPiphGq9EQpktpcZChGr3oOLSkrUs-rYatknx_cqdq_s6PzEfcx9JQwW3P5WAgTq08gqIMXjFVwLQhjS-iwFmkfGhrDV9Xrtuz57Z15LV0S37IlOTLK9UPGdbmdAwgkb5PURXkb77KObkptaNlDZ3PAauaIxP0mnEXbJ2wLE3CtIgX9HrDJ3PBdLtfgx4d0tOgjcJuV3Wq6_8Pl7oT-z4iyjL4RoDPF2XfeSdQTmFbF-pgLniUlYLejeBUpZZY5x0UI70sCHjo7nyfTV6eiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ZoP6vd6QqfvC0Li__gTb6WwAlIY5kRsCWcA0aiOQO5MiFmb60WcL76aHkyMzAv70FNV80CrE7RHGwaV_AaQHPktX7_dc5OGxx4VVZEfvH3of9IBm7SUqzvBenJJNo5fNbEKFKSwDpA1f3c5GTCf0gtWeAlMyKFvk2kShC2BDciVdMX8ba7YT1qthCzM4ncy7ckBHwbq_-utKM2Vwj0tV11xtoqO6mx_6IRlpoG_a0ELKwIt6qQoRzxYVuN09SMG4ZzQJ-xOHF-WawUdK6UniiM2EnTlV-4mfuEaIpu286nqw9v0Li07QereNNvpv42krZbS-gKlKqTNYnDAEyZ2uk2xDJgY1ErG3sc-F9L8X39h1dnYC1rpA5r3h0G-M5pWIEm1M9YPHLpDjOTPSKr71CcCZ5xcnIIaZoOa3F7yORDEED41h-ZpMREEo5qxZDdK6lXJPtkBGK9QJkkuEI8sJF-EtL0-uHe3mIjsAO1LYKq28SuDfhppPHjU-sgyG2iDH3lM97T25CZ_aHKnoZ0FxBxDzvTjqeG3rOhhOGFjbbaFccO71w08lJanAQS7e6kU3Z2fy6hbAe-HU0ixjJnwOrDDF-2nNtCpmqmy3KASOMeShWtPH-MrQ7lmZi3k0DOQlZWPwWs0rkyuNHJ8nheYrQ5Yh3M7pg14S0whl7KyJBvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ZoP6vd6QqfvC0Li__gTb6WwAlIY5kRsCWcA0aiOQO5MiFmb60WcL76aHkyMzAv70FNV80CrE7RHGwaV_AaQHPktX7_dc5OGxx4VVZEfvH3of9IBm7SUqzvBenJJNo5fNbEKFKSwDpA1f3c5GTCf0gtWeAlMyKFvk2kShC2BDciVdMX8ba7YT1qthCzM4ncy7ckBHwbq_-utKM2Vwj0tV11xtoqO6mx_6IRlpoG_a0ELKwIt6qQoRzxYVuN09SMG4ZzQJ-xOHF-WawUdK6UniiM2EnTlV-4mfuEaIpu286nqw9v0Li07QereNNvpv42krZbS-gKlKqTNYnDAEyZ2uk2xDJgY1ErG3sc-F9L8X39h1dnYC1rpA5r3h0G-M5pWIEm1M9YPHLpDjOTPSKr71CcCZ5xcnIIaZoOa3F7yORDEED41h-ZpMREEo5qxZDdK6lXJPtkBGK9QJkkuEI8sJF-EtL0-uHe3mIjsAO1LYKq28SuDfhppPHjU-sgyG2iDH3lM97T25CZ_aHKnoZ0FxBxDzvTjqeG3rOhhOGFjbbaFccO71w08lJanAQS7e6kU3Z2fy6hbAe-HU0ixjJnwOrDDF-2nNtCpmqmy3KASOMeShWtPH-MrQ7lmZi3k0DOQlZWPwWs0rkyuNHJ8nheYrQ5Yh3M7pg14S0whl7KyJBvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TZ2WJLzQPkdXuDIDWeQrMEgDc7WmVMQOfUrGV34shvptLlI054KOCSkgGVAADXqX6SA69nm_pECuz8-zjZ2uzd99OskyPjq37Q94zZUkquQhSUrJNHnUcvZn-SqBN1Dndmf8qMWtCD1ptur9a0adZhcKXHLovWbwkI_mx88dcegPLgRHp5bXiNZNSosH6c4WNfcBM-3SSJ6V-0bojbx6l655G2LtsyfzuXq3E5akgvExbsw-jzmHdsUJre8fakzyuOqbE5inFL_Z2Ynql67LvKuGRBYFXWf0sWCfTOc3MPErwVhBub_cQhA6VZZUpCXxQdJz9pkd967Hq0bHLINvnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TZ2WJLzQPkdXuDIDWeQrMEgDc7WmVMQOfUrGV34shvptLlI054KOCSkgGVAADXqX6SA69nm_pECuz8-zjZ2uzd99OskyPjq37Q94zZUkquQhSUrJNHnUcvZn-SqBN1Dndmf8qMWtCD1ptur9a0adZhcKXHLovWbwkI_mx88dcegPLgRHp5bXiNZNSosH6c4WNfcBM-3SSJ6V-0bojbx6l655G2LtsyfzuXq3E5akgvExbsw-jzmHdsUJre8fakzyuOqbE5inFL_Z2Ynql67LvKuGRBYFXWf0sWCfTOc3MPErwVhBub_cQhA6VZZUpCXxQdJz9pkd967Hq0bHLINvnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2eBKJzOr8-jrR-rrKmnAyASpMbXEH0PkneLrXAXxRLj2wCy17iE2vAJ5lg_WsRuqAyqKxEvzivIcjDnnENNYrQy6nGLGQ_4OHL-2YGi_ZZ-YlKgQno5GlpxEy2-7_8735g8U1vSAxff_Z1JhLQuX7CKMQC194ZisZxDCn7ND-KVy1I8Ap_gsgqjbozWHJ6ELBSsEooUt9FhdiZAlOgnI69wF0YGa6yRdOeXF69rPHZBZoUajJek9zdI-P9o-U2gAJd9JoGxgLFOkxI2D-5WJxx09zS7t7cpyX44UZaZoLQ2MsTslDrlyg-4Js5NyWgtcZ3rVtJyAMNB7oG3uBp80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXuMqDVFP-5vnYorMs4kh20c0ErTwXtOBKeyKc-CqjqhvWuCCPCYB5-BypkYnWjFH4mGo3G2emJcOu10aO7az8SL9v1ynvaovnENNRvgr9N1vcJ2IKI-faE68q7TCxsAm36YVNqs5VmPZ3PEAkWs-lS3NPobzlSgPCNeRCgQ7NX8Zo--NyktleQMWwysdCgZ6P3_LllY0oDRrgitZ-CMprRvC4xve2X9nNabG4VFgy8a9ZRo6F6YeBwcGu6wf3rLGVPJP8xSgscb4wY53p7mNgcdvI122Z_qzSBEQOZYsH-IO3C9UlMumx-uBwXqHDoOaBot23cDeKG3DclX5234bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv60MqiFaifWL-RXK9Y-GTAkm4I1rfuWVrY5q1Qt2RoJh27531wTe8PQ8ry5N-RrkmGhKn1viXtIGUh7pbykptb5BSm7OV4YH_O4rRATW8NffliX_M-t_JvaHfhAT-JkAO-peaz33RG-HydfOK9JOy_vD0NT3zR0pIAa7rpJLf0Z52P7rZSFQdvLtDPd1oUq_q-9yyGLTCX7XG1hxOdaSIK1p_HE2qayA8scbPL33fjrqvopL7aChTTdTgs6oEhqe89QJcz5BUX6CkVP4IX3ifIggKRK1pJEZdcAfKRKjoku5T97I9_40ezddgkfsjXl0691wBYdhwiCHfY0L90Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZ20tcAXvbYTC01OMWiElxqqGB9SbfKsiKAt7kDqKWY6zkan9mjVebtq9KnjLGrPTPPly0LdUyd0uWyD4QyOyfqAQFE1kTOei4SbVFOTY2wVbVP68O9kSZ6ei8sGmeCCWvDOu4w4XxcPz7p38Fmtu_Hu6BVeBX5G0ej5zFs1gCAPqITdw7H3jBXg_9cKDSFhgDeyj6-AHKZ3WnfwwCq9_-66q62ojcS2BF2F6vEnvzeoVVvDyv6WmfROJ0jQ6MZ_xTyP2U9BnJU_6txJfgzjdAoK6QoT8ddbTeBSXLs6TlIZ9lUYxj-Lo7ZvpYeI5dDfKbl6VUsk8n2P16EhGN9j1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKv0Ctr_Ap1sRxNq2WbSz9Jc-5jDv0AWE7DOxIldQi3NY1Mx1rd7XRc-ylB6rP-MIL5JBKKEWmnksIVwjL4v-RjFt-YESHrZKM_IMZenWWoCWxmzc9yLshewUT92HhReGY8PrkWRs-fcXQR4TPimIbgbsSKqRNM1CHqdHYoGHZg77ZGKnT0U0M_0dvZEBgb7MEYQgCAqc5slHsWh5154V2tsfifNcvtIxr4hiGMbiewYG-oJ0yQk9E1QHVs1NdQFfs3yidjIKPKyouXS0vLRH10Rjiruk9HPFao0hMNRAJisq6mREC18CooYJkbML2rWg-jaQzMKQVslm-dV30OLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj5TtTYJfXKO9dCyZPQmkm3wjzr1sRfJ7V9gQ9KMYK35UpH86r_W3jsz-fMK6nenENUo_UumQi7fM2jFKQCuq7hCRRzeEBv346kAbxWJbJ53ySsuWBD5-XpMvwXh_Rkj0NuAlp-U1gR1s4RCPYdBUyVbVrJ9YyW_Z1d50fwhnpfUoQmRo8I1mHk-O4yLfMXPwIFWzykFRqBlwg4MOxK7jon_kGeoxpdnUivzoYk7bhUURomFtv1gktYL5_gyCrR3eY5I0B9LfxuzjKY6Car5oARiJTrYJ0NQoGVcJ9oYM6AmShAonMiDXcFqUvDjqwy0PRbRaOzHV_Bkexy9pOavSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTg5UNlHaHwtMCVFIOd9OsccTSrG4aWtAR7n1_nwlZB8sslW-0ZqbnZ4CiKSNkFeg_6bIEyhZ3SAHPh-5JAbKPu670LB-fvDidl5yWAc2ukBryzdIcSmez6f7oHrspIQxkkXrMNj9CLQAaypDSX6E32ob6gFhzwJahuYr9sRpTZdhYVmruRRX_7Cd2oKrtxVa3gOpbf-30GWS0qHU6mK-96IwTzUA_aczUCcuKTvVBZB_FJiY6l17eTukGLTMdYW4QxoqX-Q6X12T3EWqqn8QBEiySbp2y-aYfD7edVk3uWgmtOGiUfbIwuEpeQ67EZBGzkLZNR_A-EY6XC5EhM_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=jfM5y8L2DSAB8fqEryyUzaOkwmjW58tgxxr7dXL-kLR4XUwTOaiBFN0I8Ob9yrmFbW3Um-rrDNio0aA3S971k0D8wxOeJ8B7-V76rzbqkn4Rn7iuWuuTqt3IuzDvNIjP4dm-ZdTOOvwnawiBmTvcDoCTcLrtyIuTzjzN5mDYezcIfCQuZk2hw6kf-cEjPwQi82DjBfO8fzogyU1A6RzVs5hMBDjWsTIq1WG0yEnaUhqy6NE9c67IEUuhL54wI5oDwcfsYpgS5RmPm0c-WaUBRAzdPnGSjxDZTKRgDJ_RdydM1vV_MWRJamEi1LU0tgL5htCUD0NR6xuOhVgET66yqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=jfM5y8L2DSAB8fqEryyUzaOkwmjW58tgxxr7dXL-kLR4XUwTOaiBFN0I8Ob9yrmFbW3Um-rrDNio0aA3S971k0D8wxOeJ8B7-V76rzbqkn4Rn7iuWuuTqt3IuzDvNIjP4dm-ZdTOOvwnawiBmTvcDoCTcLrtyIuTzjzN5mDYezcIfCQuZk2hw6kf-cEjPwQi82DjBfO8fzogyU1A6RzVs5hMBDjWsTIq1WG0yEnaUhqy6NE9c67IEUuhL54wI5oDwcfsYpgS5RmPm0c-WaUBRAzdPnGSjxDZTKRgDJ_RdydM1vV_MWRJamEi1LU0tgL5htCUD0NR6xuOhVgET66yqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FesRZKYsu9r6d5ZI0mAFmCmGfDapqV-e7exWxs_ykEOoWntqIz2Mr5sRxdW-BWAPeLZsb-VCk2g6ha4Lyr-oztD2iZEt0gQ0enM0JE9sqNHunlMG9dUgU2hXoBGm0nTEdgAqdIAa9LyejCk_uz7cY3YMjKzJGQ9ixch4LtZCNJaUHfm9ASnGEgG58lliSZHuxWIswGj1ZdA8im35DfL3jasY-9JvkGZnwDzB1Am9o6R5EL53G9hPlVItxnygAOORxlbqf7XWxcPzixJS3bxOF_lVrX1qAnxlY9oua4pOenGwleY2mGtAeYoZUSYJk40sIxBa3a_0Fvg8pukkb6uGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=q5njMJGXHAzparEXz3N1z5Wou0rqH1dGhlHKImM4qle0gvA4n7V_hmPMtToZrdlda5iDJtfFfAGUottVrVsjusX8QOm-SxaM1cFcZFFPBwOLS0wu6OBkfXJIc75RZZBpCFwUjLXmZLWrgPUlUhVGJj7VE0Bi1uZGbQP4taZHdCakMHep7kwTvJUz0uh8n5BloiE2jq17oVcVtxRAB9ajn8Xa12F5dzNcZj6DIuTheC9ShFDQNHrzn9Uqr337RDHuBhNEXYO_vj0GssQHqMzix0PB08F6QIuuvQtqmCaMn4FTE9jq8ehoJQAHR6Z-vrngdllNY_GpvsVVzT-v5-ydbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=q5njMJGXHAzparEXz3N1z5Wou0rqH1dGhlHKImM4qle0gvA4n7V_hmPMtToZrdlda5iDJtfFfAGUottVrVsjusX8QOm-SxaM1cFcZFFPBwOLS0wu6OBkfXJIc75RZZBpCFwUjLXmZLWrgPUlUhVGJj7VE0Bi1uZGbQP4taZHdCakMHep7kwTvJUz0uh8n5BloiE2jq17oVcVtxRAB9ajn8Xa12F5dzNcZj6DIuTheC9ShFDQNHrzn9Uqr337RDHuBhNEXYO_vj0GssQHqMzix0PB08F6QIuuvQtqmCaMn4FTE9jq8ehoJQAHR6Z-vrngdllNY_GpvsVVzT-v5-ydbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnKpk7qSj5NJs2fdFDA7HbxNwXsF3bObJk7xt3JZTUsCfDX92xfCqb3nSHcIasqOZc7h05hJ5KQe-5FLFLRMYfGkzTxCBxuCLyyN855f5LEvhJXs_-LRoFiLbDjmlB6rD4h-_gs304EZ2rOP4B2DYppXgYoPZAlycFQHD3lF2Sk_vV7l7fYnnn2_H9dKNZRl4iaRw4cz8owAzkWuHy1CpzVz8CBOQlzu8ib9hHIYCs0ML3JLs_O3Q7gfl_ycfo9pw-b3dGTuc6_zLF1MK9axq3ZS-QXxlV1tJ8TEcNkd0qXR5k2I8qM-IGxobGqNOqgryM_u9j-eXc0Xdp3pYf9guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCUdlTMQzgfwjj1E8bQzHinQqe0XbgF7vW_IOYOd52-IMhXnuwKiSzcGSU5Qz4umasK2jUNorA9-7fvelpAyUzbjd4mtMx_ld1I8SDtcpfSpmb2evH6S6MdLqDHRf9czQ-zc1GBN6KgUmouHJPrKHK8ZQ22DDhBGBj414B3aFJ1nNe3IIQy_nqUMrIdvJBz3upY7NVDDqd8El0TpMKUs9Hh18Inz0BLZ7RKvfs2hagNDIYGc2qth8aaLmIYB519VWdWahrQAi0m0AduGrzmRfvEMdYJSZIsVMqoUgZo1qxRaYMuK1KLO9rt_7Iy5xvvqUSepJmYXjivSi8M5OOELWnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCUdlTMQzgfwjj1E8bQzHinQqe0XbgF7vW_IOYOd52-IMhXnuwKiSzcGSU5Qz4umasK2jUNorA9-7fvelpAyUzbjd4mtMx_ld1I8SDtcpfSpmb2evH6S6MdLqDHRf9czQ-zc1GBN6KgUmouHJPrKHK8ZQ22DDhBGBj414B3aFJ1nNe3IIQy_nqUMrIdvJBz3upY7NVDDqd8El0TpMKUs9Hh18Inz0BLZ7RKvfs2hagNDIYGc2qth8aaLmIYB519VWdWahrQAi0m0AduGrzmRfvEMdYJSZIsVMqoUgZo1qxRaYMuK1KLO9rt_7Iy5xvvqUSepJmYXjivSi8M5OOELWnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=BayWudgdJU0cwfoa15sBNGKgfVwHJMRugluL3MrqEeNTTbgJ6wfZpB0FoSciN_3grW_7MoKw42wfsLQTLq3OIk0UtD5uRA31k5-NETBYgWTO7ZvSsrTbtQPd6RjScfPyJX1LvRQZ46y3EVVdWRHyfRrUhGKNnkmQsL7W_Rgib_k4S68XHRCUN7zuJ6lZXimjqJZSNfYuWa91-f5SmzW60yHZCo5SIvKkD1PqmVUcRaQXF6NHpD19EmpuaM1HImikp8QKJ3G460Hz43pK6_P376YZ_l4xohyF5G544aD98vEeDXNUU4uRE0vqdA6pRRHDxv98_tFeov-Zq1vU-eopYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=BayWudgdJU0cwfoa15sBNGKgfVwHJMRugluL3MrqEeNTTbgJ6wfZpB0FoSciN_3grW_7MoKw42wfsLQTLq3OIk0UtD5uRA31k5-NETBYgWTO7ZvSsrTbtQPd6RjScfPyJX1LvRQZ46y3EVVdWRHyfRrUhGKNnkmQsL7W_Rgib_k4S68XHRCUN7zuJ6lZXimjqJZSNfYuWa91-f5SmzW60yHZCo5SIvKkD1PqmVUcRaQXF6NHpD19EmpuaM1HImikp8QKJ3G460Hz43pK6_P376YZ_l4xohyF5G544aD98vEeDXNUU4uRE0vqdA6pRRHDxv98_tFeov-Zq1vU-eopYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTr17LJkeTVwA0gioJnUDixYpIq4tBuTmkrC0XlKEvrncXyk5amh23FuZt1w1Fr3JE-yuxu9gGg0lTWzwhCOxjF4ByQ-3cU5PlmMGLi_Pc9cAdDLi7EuecPc3TaEwGIZZVYMnI7SV3dVCYY0nM3hpZ2f97Tff0mHMeNZ2Yw2ztjFyWd0bUcurtdFpym5ac3unx8gPsUKLOgVvETtnXcpdDJhaoG6Fu8Ie81357muP726OO2ZLLFpTvx410qdnFDtGEOeCFsGo2VVT-bt6soD8LPEzZZlthtscYebiYN63kNHMBiXFrHGwO1NDxF2jWF1Ujh91GWhwFTIkrITVef_0lI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTr17LJkeTVwA0gioJnUDixYpIq4tBuTmkrC0XlKEvrncXyk5amh23FuZt1w1Fr3JE-yuxu9gGg0lTWzwhCOxjF4ByQ-3cU5PlmMGLi_Pc9cAdDLi7EuecPc3TaEwGIZZVYMnI7SV3dVCYY0nM3hpZ2f97Tff0mHMeNZ2Yw2ztjFyWd0bUcurtdFpym5ac3unx8gPsUKLOgVvETtnXcpdDJhaoG6Fu8Ie81357muP726OO2ZLLFpTvx410qdnFDtGEOeCFsGo2VVT-bt6soD8LPEzZZlthtscYebiYN63kNHMBiXFrHGwO1NDxF2jWF1Ujh91GWhwFTIkrITVef_0lI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8-ImhScoEXrFnl_lWNAU6Q9qR80s-wciP5UB8gwu3apADMXQv76bd5l-uVliS0QNaCnaMwO0lQU-0BP3EyO1aCh7mtweLpgC_2Y08dtnavyyC6vospmIX-M1MwBMFuq5E0SzCBlvvd2STBXwJiZSnxhnFlncmi6o2_aeE3sqJv55Yf_uPXhxGEfdn6DmCFgdK0umDcxGAorWR60UuBuOh-bca2IDFwflTPN5Dig8MjTNpnTlyg5q1VtlBMy0aM8IlBPKXdHAvZE0-iI5pKobJSQp3X6wu4es0IL5KNaL-i0-z8EvCT6NaIRXRtoVDXHSVJ3juxDX3liL64UdfqSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3re0b5U2Qph_ZAdf2gtOxCkOEPDh1UdCKZZ90LLHOVtZstFPKR38Hgv9xlCivow1j50oICcmLI7yP2ORaxPdvr9fQl5M8JskLgYYt2gQheWUhEnj6lFlexVwQU6Oh9bhE9KQJOD0dnjGBmy7ne5OWCEwebv7uWKhpiKpCUKhRWIdbKh5NXe7eL_6UEJUisiobRlnS52CbCfEGPMmeMV1oUKVMC01KlyyrJ-X0VMsMAAYcUhxa_lT1q-sW56vQAGVEE9hpsKieWub1aaf0JPI_B5nAN-853WUOJQsv6k9JHVJieXzgRYrOc6gSZqXt3SDx3H-EpTDCS0VZcq--nP1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMzy6AFPdWX1CTwnDrjrlppXaD5cazqIO52P60e6qQpbufLyZsmfIrhlwyU1XF3p25B8S3ABG41rkLD3pssOUtNGW2yzbVEHBlME_neUMmTLQN9Fr1Wypc_P8761IDIlub-kAsTiJbFS3WEaPaWeAcMXb1nlZKPKfs6Svnck-feyV7QlUq5Us6ZHl8BraEJcELnEafHqCX7ecQ89Q5wzphD1ZtmnC3IBMfoPVrBfoQniJeH9rllLoVFeGRN4AvYKlf-n2JO4BcimtLN-rZEZwEtqnjAebFAxYtwkjguh7x66Tfuu0fGlxagp72rtfrGdVvxh54j-W4OaOqNJzxjGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeCmInGSYPUXNJaaBdPJcxPUa0UAmGNvI0nRhqUDhz_Ghqmy8o5WxaCaKAXVmxNr6i-XkOMjsh-CzXY_G7KfCmyzhlJ63txFIoCfqgUxaTJUc7rdYAGiE1jzz2Dy5B_S5TZmgs92EYE5y7dHgbq3urwCmciUmw8S2JV4QRw7Jv_k4PqZUrfnztyZZX7mbgj7qMnn4JIDuJfFmZn91VB3J-NLodGDqg2Uq-7kGBCniAMwjgNqq2hO7hhsgi-4fMvHWzX2AcBb74JhdJdxtzSzLcIYFZEI34kEDz4Kf4XlXfT_wyjd1uhfB3Xzm-f95ecrm4IY6iRohz7xWK7PRJzPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clZ7YGIIN3mOkXkqiL6HUlfhi5oYp9Cf9rIPCsUCHcPWG_g6EkieCyQ-wR1_yd23hPIQxhjjOv8L3LPXdgFjdhZMsg6S41Ku_WUpFcj02ex_FJat3-KM8yF2WeHFMFkRinI29uXmYfZbv2g8GEvOQfvJOsAKpU6P5QDPcN_WFitFBjJTui2ELUxW9WyFkJ6aJbw0dazMppn5tSwV6YZcXADyKMNNJY8a8HAHNrF_bXiQmRdOu0uCzDHbA-wT7qrMiueQD59PaPcg3yuLnntZArugAwcng-r9nuxBynVS1DBz-T5ht4LUWNcoucwX-aCs7hmux7FEtCaPxCR0ta_ECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjGifZYZTjSLQsbZRauER4sgAm_6Cb-ofSvqS_hafeQCMeqb5Nv4YubAvwm_OpEwoYC2F1IAG7BdPLUeDJVQDlGtQyjzj4gCzXhSnkV0SUJzfeKdIn12KtzmWQ0qthlJgnWWjDC8_kMQPY-bcwFAjzlYXCdMBGYmvA9UrJvHjQ5QGKvAS2ykviq1kxQOr8_gJ6kbT_-emQMZ5ZAAY2NETHdC8Y63obIhG82DizbGsz5zmT0Efoi9cDSYo9oIIYIh2nwmrM5QZR0vuBJ5zJGo3HJ5sI0QJon8cKSZE3Y_wcmnLw389rzvAfzvLbJLayH2HoJiJJSR6eBjz43Rf_l_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvczJwciNDjLyOyG7dqHqFcgbpIh0t6e71QNqD3p56e6QjgmNmwBAT3IsYdxaqwQi4K6PvA72YClLKBXCisBT4PLDIcHOfUMJhY-8OL-9cNHkwvisBvUekGvS-bQlm1j47TCENR2xcYo4v67oznlN20lCBhWcIYqywqo-BSP2tLudWflHwrWqHyhRdH6TTq-B6DrjycklP9rSJFq717Tm_etIuDyn8H5Zq4q7UsM7zbum3V9xQm8OmjfQUCB2Xf211NoL3I7JWebVGfJLBDmW1tFxj62gCbgEtpSFp05aslugDFjDBiRxfz9dTzYFRaEfmKkVBpbdtp8co61Fawbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT4b4DkCgmDXc8az7T7pf8pY7ZUZz1cFDGl1OaUqEfnG_v2Tf4nF5or-h2PzA8R_avV-R7zb6FkIrU7QBTsTaweLo6lDRr2aFlV3hRWnuqLd1B9obzGeMQln49d5uc2Zk2_cH2CL2z7_wpW1J1xS6_6d_kqCgDLElf3_XVLpTqmMYDoFi13lIrlqTou4fauioTVTN_zLgU12_Dic-VkuIkWDYVS4Bup2HYn8cnNl2-uWhBxbRuAy_n4SyJSeqD7tFQAJ_wEieQabvnLQwVlg43439jeYER0aePT8ooGWYeElO7P-f0DE68rFsbUOWjlkDDbB-aFX8BtUzYaVimjXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7krBkm_Tp4kIfLsx8uPXOomVHd1nd5mJWTzIH-tXipWDkoMo9-j0MDCl4l_JzIVOSHmydP2B7RXKHSVe8P0Q4rveZ-Wh1sOzmWdG72UzM3WnoDlPA0KBHWmZb1URDRo7pGwgNdKjo6oSKM5kD2jCxwEGTwfpG3RRgSc48NcQOikX2u3KWDDeyrB2H8w17PgblAlmySi1_goNKhoMoVsVf-D3HCKzpNsEU7O3g8HGy1qHad36wvK6fZPkcGWj8QapcPg7ipDQyvD_hjxSHsX4C-OjLu3P11YHBExOhL9uDza3texCZ9vceUM5gIAlUEFPqny-z83Y-QHPkde7X1rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlEvGKmdOv2ePRf7_tDKbigJjFdE95Qdp686Nl5tVOuQaps96UB_HT1fT0M7F4C2KSAeH8t7nZu1Neay-jGmRrHq866-cslT91iju1Ks3_uGUela4HV9MlY9867BYs6u5QjhwMt_ZjbShZ26jbeL6NANf6SdeV7BTNUjDOCsYIJelk5ccNR0RDzNE7jQ7UIsQFVjUe4xK8x4yqsoBEbEnHeST1P3cjLb8e6eIoCpOILHTX4A5r2est-39LS3tPru0csv3u5-KKAptIlTNK132Kc25mYyNKTGynCgA3J0H8qA44t6UPYhrMcI8hL5mdtKIN-Jzf_KFhcoLJYSawBa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
