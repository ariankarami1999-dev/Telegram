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
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 569K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 19:40:15</div>
<hr>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtXtGya4m1eMWt0GAKhKJYQIqtTjJCdnjmuF9PAXDaXqQ_HIenKJz0RhQXBkaamdZlVIAVyI5vCHf54pZBKt9dXjq0DX27FcsSiVjJvnPFp0mHgxTnkM9jq-fx8EXAZizSYefPoar278oBxd_k-xPyJiz3yNH_MrRvYkiBSgIHYUDEGAethYv-ChfiyWc7V2ohBFy1xMYWg9J4K-pqumKZSOI4g8jham-OLXOZ5nL6y5CUDbwf68EHL09lQXs8YfXfaAXQIJqPULtoevafEP2ISScOvNoNJxIbuIyO2pKFlu_-BnaVbk1GLn2Gdse3tx5n90eVD2yL3O6_AzTZUkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tikfnqILYDG7_iRclgxXy_MEk2HHsyxpH-XVNPnO_l2Ui074tG0sq_o3yc5X3WCFLE0vitIW1s4uXxrnhnwm3JNJMzVNMglxKfg55MOfU7VV2rUXBS9PfXodY-hvXgXCk9RxjDvIajwTiecHHZfnJhZGSao_BklEbR4oYWgGQyteilWuqxuxhwCAnvw2nJl3jTOjJDKNBcigUS4DwfjOZiKKjFew1n4Vqu51C1fbPkCo0iRG8bOfk0301I6TjCm8BgANvK-DrA-Zik8JHkAt6iBTUtohGOIogWYlLTUfjoZuhDIsBPNvOqZyWB-2iBiNovi0TIe9FpWQHiXXc_hqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcY61zCUdEp_9q9CrvIjhIsvEpNq30XUNdII92UOTnJG7iXmOQG2Pf4935clwtbvkxGyx0utwTUwpf6I5xTUFxJQZVtzZOZ2o8-tlzluogdgET1pCn6QH8orw1KRR3QfW4Yhf3L5NMoz3vPNW-Nvpe-730voD-xDtKp2F-0CEAHEoKjnDIHvrgPINDPbH8vWKQ9cJllmawoEdfSurDgv0DOYgUDwXWrV8p9A0KXmW79k0TLKvtfpa1ptJCSq0WsBMLJLl6hUW0tq_qRbZywCBijTFoWg_O6qaTjXoTkFo7PnwMEr7pp3JXS4NqGT_cn4bu9iUDk5pePhwZKLlS16Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfxpm_m-gN3F4BXnqx4gyR1r92cZqKIeH154NwPBJcCquIUfBbKAdwd5VWeWnjep_sTQjbWxxcBKtLNKm3o1yz7iSmQ-n9cCxa1p6mU7d0ug_6IBrCahw4QgVkgGG7wAPdnIr8kFMzPSekrluXWzzNufLQ4_kwFQCP3LUapM7PtyBxebaoEaY7jElmcQPkWIkbkJ09PhhDxZRxi5yji_OAhS01CYcKkILmUSUxGW92XMGjDeonZxX84TTh06uC7XzYFBXjQ152owmqsNZRwSCD6geDNpc2JLYqeCQAyxJZPcZrKIH1hHMd3Ks-Ub6Qz-gN5UEW6Hm0NKd8GVxAs45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhpMX2EmACN7MZ_wcp72EkPM2Hlz6lWjg3VS7xYGxnn4W_qXiDU23jHXMBN60VExTOIeBvpcURe6IbeAgSazTLeNrq2gEM-IrQ-PUFBwRnIo47aLdp70D5vukHahRitOHGzECOqZQDbVfqAlUmvpx9z485a_qQ6ZegTfOpFeKMMroXjLsFOmRaSHck8JGClSxYdBL_K3PNU27pTBvdhzGZKBaOqPRTH1pyI5l93xQovqIJfB05ogSeL5gQyH5YddVakpigLs_0tM-UtiTATbOC1co7t3d9pM9ZEe256vZneoerAuADg67TM89I0pRB4ODJIeryruUSyFVIZOtfb2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6P8D88h1e_ywTuh4UbXQl0IfKxaOV3ICgNj9HZMNa6vUrtLgEvcWrA-4XKjikI95cSbIOI3UxhEo130W9H7sCxIHj1sS0nkabkVPi-XLWDYx4gwxLt6I0H_phj0YYP1w9mdgYgdy00oUeMbBg4Th1Gf6LvyQGciFGdEm1YIuFf1UcdBulm1GcMHEzv1X08i6epvFD8i7oOfIQnr0Edjony9FrCacSx0F9vMeEyKqupitevpO3xQMk_2JIjfhoFucUpiSJiqCveP4xFM5YM4TBuG5hahgVx2OGBl2SVcNRM859sg3d-0iKhXGSFWIaAL0PRMBuU65LZKgIoihoyMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=eAwhfAIvS0kOZhJSW4A7Kz8ndrhv0jDTY4OeK1NuZvSKlNMd85_3I4i9Ir8M8kSnJJvxL-AOE3Qcy7HcLp4ft5aG8WgzIRz6cTfAwTrbon4hLp83nIGQGz4waFzAg0OePy9qp9Y2fdydPcGIiRZel3rfIM_11Fu3b0LeSVeDq3mtO5CJLxI60bhLHj8GqZHWVcfb_vGAL-zziDLTsJ6z_mDC8ARr2A19omwKlysoDVtwndrhYjX7YS2EFVBSftB_zRR6ps2t0fGGNFUYt0_K3NVAEtgK-Kh9aEnb2iAtKT_t3GzJthem1UG-_yjH9NzzJ4EQMa5GTx53cxYWkkA31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=eAwhfAIvS0kOZhJSW4A7Kz8ndrhv0jDTY4OeK1NuZvSKlNMd85_3I4i9Ir8M8kSnJJvxL-AOE3Qcy7HcLp4ft5aG8WgzIRz6cTfAwTrbon4hLp83nIGQGz4waFzAg0OePy9qp9Y2fdydPcGIiRZel3rfIM_11Fu3b0LeSVeDq3mtO5CJLxI60bhLHj8GqZHWVcfb_vGAL-zziDLTsJ6z_mDC8ARr2A19omwKlysoDVtwndrhYjX7YS2EFVBSftB_zRR6ps2t0fGGNFUYt0_K3NVAEtgK-Kh9aEnb2iAtKT_t3GzJthem1UG-_yjH9NzzJ4EQMa5GTx53cxYWkkA31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLgHvIcjW3v5cxBrPfeOEQbc1MubyAHwBEH0h3-eEbdBkbBiLjMnZK9uh3aLTB4EneklySr7DQRXll9lo9m30Fjb2Dkqo_3nVwu-oZ-ArAlzZKWHJzZ8qAmwlCty9UmE3Gpi5wkUow-Pbm8uOqE4Sq_pYBd4Q3Yjvo-Cli_68CjOQ166rgz6Dm4gpyR8nXta_iZz94upXci4A4pewMxg30_lX3N11P4fzpVOKWkolZjNz4kzipL3pdcU5y8QjMiSvaLOf-A2oqEFgr9Fm2Bb2Ane2ws9WkSbX6kYdxQZzkMzRB6kebP0zpEuxAAgvzZTEZZtr7WeIbLtGoshrwAz-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvD1o_L6-OC_3pt6tiNxH32dSMxcW83AjIz9HFTn1qeu1bxq6B3qDxy_4pa2WQ2-GlaYtrWhCMF47Xn_7ZklF4OAIXIt8rCA1Xb7DcGlIoHobzrGTpP546ufW9Q2TUoKz9hMogq23I4UxwrXX7PNBBkzd9dWqf-XZDr43e1lLbmre45fAD3JEfkxA-Gx5wsHUDjXKgQvM12ZsZ8B9sKnaTKhQYnGgSrbCeMaamuW43an8l3yfTtGUDynDidX0Y5-s0ELsVnIAYEe1bC5asW7tbciavaq1-OeZBrOIqVQk5XB37UEgSCQcBaPRaGGGCfu-RxQOR2jfQQk7yXN8mZzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxErwStoKTi15Z9NPKM96b8ln3BuOsTtnyIQiK1MEuMGVPcpaLT4lAE0gM0AewfVhdda7-wUCpesGI_z_T1havWwoUbiSXh4ZJD_5a3fCmvD_VOycP5HPyxhRsgHTJlQbHF_nWt8yzw71HcgJIe9yZpb5x54X2b-f4uh8EQLuU_NCTtodVjBihjfB6cbcShOUsaP-_WlxKMJfPuyHTSXYmarozgh7I98vOl6qcTLxf_WdBu88cemokmdmEXsPR9pMZn-fWVMZJPTv0ssAJ8R3y_JF22T0DWJeGs8aPMaDYTJgIaE96KfwIMpsgykJvc3fDhT5b0fSAgtUr0hpeNE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N92zQns_P9Ro-c8n1xGcyRTq7k6Eb6uxJ7jb9vdhnSaT8RrlgCAiFS36u0K3y1fkysM-evd5pj3MOGamQBZsP76g0AHdv3KP9laorkQ-HZZLLad-97O05RLl3dlZ0RseN72nEMHi0iCOxG9HE2TQte93FYYR2fSkllK96CYyaXXoQ2K3fBgd31ayntmwZs31fAEB3ojQA5g3tfUquFnW0M1YW3UJ1-ks8gFNUBvUTPUlS6H9GGVc8VHkjP5A6QvYE_uxI7Unpt167u5rqje3p8ylPDK6xwRlWa7-rVOU_qJSbdPY0RFLVNgsAn2ot_iJVVAc1PHzaNBYB4EPG4hTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd1G_fIKc3AuegYTEV5r8-mWnNaXj7LF459qAWhs4Gf28UVTpjwMM3FjFNeN51CjTv_INvYJ1dDy2qmi1D8C_QCrxZziPdBSJarxhLwMdMzAJMom42rxKWRnzDM63RUauuZhpq5ENc7oonyKNsURU0tv_z49fp11sPqEC-KWZx0xsa02xnp7uYAthHJ9C4FXYB2OoKL_UbCPkEpA0uReqZbqAgiw8rveDRN65WS3z60B0mTPRFzCA_Rm8GEuzKh3a1MDrisu_zrWtx5sgHn4Kb2eXG3cNM7bS_XiGVMegNSzFbMQe_GxiIkEsdIaxUtbngvTUL_kXL-xW1SSSPW0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZdyhRScUn2A513_RPvtabk8iZmhrNZJJwOjrfu5r4qhJ3eZhZh7bP9tNYQF5sDBstCiDcN_1aN4Ho3CddsOi1vo_3ZNCuE1c55YWzlb1XRLbLHJMPxZ7e2amdLkNwgTpI5TUqxrPAiRWIis2P9q4AZv_q7N4XTkFArZstx6h8yodhnyj6pjbnkAoFy0NzhOOtbaKXviuFS10E5hRWUenwwaZi3iupICNavDcxaDx7mSxiVIRZXcKuIMqHevRcqk0mOZbKW8YyUw7nYlOxVuRBw13OxtamgbxxVRRc0CohqihkB867IUnm6yRm0lCVGkFxOxaHgqa8R_MeJOo_ldZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-I5MCyBozQRxvYuknNE-ct5ewx027CXlmiyiNvclzLco43GyAa2LvJZKPeAygOG4Y4OaeaJfmxcwUFoBADEHTVjlIijp5DqWLj5dLr7JzSJMfYk8Cuu6hVQyZiYTXmAJdRSQY-u1c2_YwS5aWB6HZqxWmLSMZaRUPhC-UJT_svUePUf8Jb-QUG1wIqVHXueVfLvsEOZbti8oMEvfBFvqXau9iB4WF3DiP2xMgi3PZ6Fw3i0n6uUwfioqkUkH-kgx7N9zV-F-pLDPt5rwt8wWkUYD7Y5tqq4SURu0TmE_sRhuPPgsbIVDrEhIpiuT7vMKfL6vqhRWdRDRE2mw3OZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب تیم‌ملی آرژانتین
🔥
👀
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U54Dih8fr03Yj8tRyiczh56x1n9Uw4jfhCch4JjFZrnAR8lBD4FWEMUqyvAkHHcWxJybbGA5ncBXfLkubF6gn9jSuOdmtFvX3j3JVTufQKkduo-GDSFoLILBcuYaCQMpbZPhwBBZRvPC74g2UzF46_MqXjkTsIQj7vcytl5L2jr6nLeR9_lrN8KLdDPC2N_4FJtWsnRu3EavuM7kx7H-798Fd_0KHlQlYf7DdTo0Ke6-ShMXfYpbgNGqNNt6odB25GyZWXVdEVXss3mAVeyJTPEb8Sfn_NcyHhJWY9Cy0QH8q9GL1QO7YsF7vtIPYPrUe7StMDVXSxY9fqHS7hxteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
توصیف عادل فردوسی‌پور از کامبک آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
گل‌دوم آرژانتینی‌ها از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
پست جالب باشگاه اینتر برای لائوتارو
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63EL4ssOxM9XwjFfl3wP4V76LNz9EaQV901tuyVeQWEBW-Vj2UCxsCBXfWVeSkJQWrzs8chFurhRQi9bvykMGRRB54M7HFLGKn2q03xipP7bQOqc1FYaSzuzCppAl2U3MQq2Y820VDGTlTEoTGPH14lsHun_VeXfP_iqUjtE9XuKOnMbxQ5q10TScUSJYi3bIYRlR1uGsPWKzKrT11D0QYIj3mFopPCgH4r1BBu0FAMWikfkN8RQsOwldmZFXY_7_xNvUhWwjqliZh1u8vjqCwtK5c5OO4fRmP59XsC1WaETcI8M_xSNsiOGuMkT3bZSFj0iY3x0QGDp-0_77MENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4QbAhNQTNzD4BYDpcS9K9BF7hOwVdOoMDsZ7iUJRAg-G7mUjdQRVR96X8DQD-yFAwc_Ntqt2nqWqjIfeDwJa7U8iJmakal8Eb3C5JqXj5O-fZWgTeXQPGlEhFeLm4ghqwoyFUqaySfKZdM_Pzlj9eciJupOLCIUC8qUahUof55tNlrFu1yvcpN22TKb9GklF6jAS7BukPg6wPHD56Cl3bv3m3xiknnSozwvtCqIcKBwaYjvDM7GlF8RoBLxWC6lRc4qg0tV--Qg3b-_Pti3DuAyz7dtckVziKmXOP73CktxzPW0RaLIxEjU0LN7QFB4AFOETyywzQPpeQd0wnUczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYaIKm8E5-Gj4vgEw1bX46IZTA5GoHpd24Vi2f4fjC0X_qxHA4yTKFrVh3VXE0mfcOnnDJTGhZgtf_j8fPSmuUuf9PTm69SWhBEsTNH28Obb1j2i-gcsuvtd61kjx1OE3l6SMg1mBU_WrXxxstRxP5bmxq4ITa_Ctiw8_zfqk1RjP1nwY-5Iz_9E-N4KUTG0orVTw04wrQcywoQ-TD6U32JpDObbv-2beOda4M8Uh0U56Cqd9f8XJ7mFS_cT0gTR6mXxLlxY4wRI7WQ21Xto8NIII8fN1VB-f4G28AUnvESNua0alXV0kIfs1LCZtLfX2bT27VXNcUUKSuxGMK4gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUt3LGRUuEUK_jsg-33v8CRFUTUA68HGFLLFBZOT4q0Qh5pej5iTS6co8p4LzAWjXDv6A8MwwJ1XIHZ9wOLGMN_hB2Y1dbhVKu_8olt_bmUoxla5Gj0ZIXNYCLCMP7bplKgX5ztHHXYd9QdQHATdtphWpUMNgDE23TtNynAk7SfuTSDPydzie7LBuX7LUh6JGcGepO0o0Fn0bGk6jcBGwisdrnS30DiOyAwp2gFzPjCDyQzcfsSSDciErQQd14mP53PwUr1teYqunA30HJcXi6CH8Hui9CnB9hwZbv9gkm8C0sU1lKnu0EJt7Rm2q6a71izwk43DtSUetwXyHETtEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
📊
مقایسه قدی سه‌بازیکن مدافع انگلیس در دقایق پایانی بازی‌دیشب با لائوتارو مارتینز که نشون میده قد دراز همیشه ملاک موفقیت در نبرد هوایی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoIZj75agkj7Ap5qJp2Og7DShaYMODqTUsDfHbaYIJnQEqhbjGpaR-4kIwA-lMGOtTKiblvOkNw8opPKp0Y2cZjCL7GSL1I4jfyTn0qW9HfH2FdsLsfF-FPihPHD2l5bDTzAoOA5dtQ6ADNpi-ACT0r3Od3du2Rv5OHS4ClO66xCzBcT8o3fvY1a-9LonDPFnQ2aRDMoLmCOcMvUc1iafFzLr1ugDEEApkEWMcgK-dvVZMlKAmRiGkUmiTIijn0rPR6e0NOs7v_12OIn--xXv4gmjyxFXrdgDzpPaNlPOO3xlz5fLmFWWP8iiAmUMtofbnqfsPYx24VZSRePIvFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uG4M42J0R5rE1GTnW935sHW1OGlutr27R96V4G0z8v8MYdxWwUDv_POdnqIhaDIGrVsg568fMr1yhipoOkWrpdMrsIxotJg8stfqP4cqcRhMyrak_uDzXEJNxa5zX7XGGTKJvO2SXg5Hbhv6GODMFll4djt5hBWhwbjihC9e7Fya79Hpdsjn8n0c8TZs6xE5t06Qoan3ljtntP0qTaZU_AByn79uMMVQXn1iMKYv__WnM9-2MVU5O6R1VbS8fyhZ1h8fuzHLYOWmJDzuA2Djjcyg37OEEgb3nXzNQA2-TSv3jb4001SxkH9rZxhhIehsBAceLrIvnk13YJ3kpsFBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTUkSiKxfLI58-m3FjL5XdoB-gbPnztuSprG9OxoVoA2w9_PdDa1v_GZqd4uZCv8NBjwBLgcWKwKGDzfJOl_PR1sL85_CRjNcchyz0Mbe6E_5sLbptrHx7kVE-Soa-nOAmMPBM1Sp3ogpLPcF6U3kf0_EM0CgB8q8lB-gC3M08ZWHF0Q5AdRdYSizbn6yedFMCAf35g4cjFMkBrg38j_GMINrGLtAYvaRlz-IwMf-r6w6eu1rFt52oVejH83cLOccaebEwJQQRb5CxS85SmmmL1NMs_I7TDSvGpAsF-1lMqCWbY9skcrGzgBcgINyjXLjrG6H9LCwDRu7vCdhTnlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHXczvbUgH3i35Qy8PN9dpgoHEfFrontLjefBYxKfM2bsRDifpI0rUZRv6WA_3QzqqZkzS7h-pBCKG4c2secwuebmUgxF9Erx9c7W_QH1Cyvzxp5zYuJZArq--X-9is-wDd8TlY-VKRGwUPZpQnXeE_Yuvy8XS7Ckg3-I748Ye3Gd47SXP5lcmvMr9vdysaR1lO6LGIlpPh5e3L-S83JTwEAPyQEV1wSSMkkPWAvKqQJG95IxM_D09gudTbZ9e9RKSqdsHs5gbiBSCIbZRBplhmN3MDNYMhRdUGECbDKWX15Imo3GAa1EfCkQDpfe9JEtJSvMNXW3IaVL2HKuNBwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLnaHyH3lp2vGALezLt3p-5TtKIGP4mlSNc8k1vI5VyvSdKz8t00J0ByNOuD6WI1PZjMzPJqAp5w-uQXwJsekLQTSm6NkWwHPJcCXy1BCKg9DgsIU8DFD1Gz-lSM-8WH-S4Xylf87I_qt6F7OR0dAEx6pB-CB50grjfjlT-zdc8KOv5YAHTCiAy1B0uxm7siYFpvhXE0gGTa2TB45NPWwckbLXyG-NSyr-nBWA_QnpQC3Z6c6A40N_2IoM2RAGcNkfef58Y5StBerlvhxzmCxsMMWq1cLQ5MY0HmWUfOSG-9QZb_bKYWrQb4qzVhoqdj71G9vu3aqScaHFa9fRlSRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🙂
اگه یه روزی بعد دیدن این عکسا میگفتیم مسی قراره با همین بچهاا فینال جام‌جهانی بازی کنه بهمون میگفتن کسخل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه‌های فیروز کریمی به قلعه‌نویی: تا الان سه تا تیم تو جام‌جهانی نباختن که دوتاشون فینالیست شدن و یکیش ایران بود. این برای ما افتخار بزرگیه و باید جشن بگیریم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
😍
بغض و اشک‌های جولیانو سیمئونه‌ وقتی دیشب راجب لیونل‌مسی صحبت می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
لیونل اسکالونی در تمجید از مسی: "اون دیگه چیکار باید می‌کرد تا ثابت کنه بهترین فوتبالیست تاریخه؟ واقعاً دیگه هیچ شک و تردیدی وجود نداره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
بطری تقلب پیکفورد که دیشب دست بازیکنای آرژانتین افتاد و حسابی سوژه خنده شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100458">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
۲۰ سال و ۶ جام‌جهانی و افتخارآفرینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100458" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100457">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
پشمام از مردم آرژانتین بعد گل لائوتارو
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100457" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100456">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کون پاره لب خندون مثل اسپید کسخل
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100456" target="_blank">📅 09:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbdUNMG8A44NjycQ1217wv3Fd8bEoSknZdxABs2xBRRvuswtEM7w9mst2Ggfy2b4fldvLLvf1H-Rum-H3OE_EsumYb1ruiA0oaSy2CZ4gXUCOMJDpEAnCcFd9Rh6woXQOav_bjoX3abAQ9xwn8St5mWrd1RnlY-b4AwwhycNbNvULk-xyHKXnYD-zscVFhhLRaSTqZw6p9HP-uSK84NQI6WhVZjr5MsWlwpVNxoNbfMGaezNdfZD2RgxfxeyrZyAvt30EEjMD9UuHfnwiLG53p-JgvPf_dBunXDZSWd58xaedFFimXekVgUUQWBmEQXs3JdqUQz-KkUSSJsWrXrrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جود بِلینگهام: "برای من، بازی کردن در برابر لئو مسی فوق‌العاده است. عملکردی که او در جام جهانی ارائه می‌دهد، شگفت‌انگیز است. برای او در فینال آرزوی موفقیت دارم."
🤝
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100455" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی خودمونیم بدل هالند خیلی خوشکله
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100454" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpDjc5fcHl9LAoS6DVtaVU1K2uL4KBw0G8mnu2Ihl4PGtxGDDaEPp0gvPrHQxRu3P339OGV9EEqhdSxO3xIwHSN0XJZf8QwwSqoebfs_N0hAVMoFbZCD4D-JQLjG7HME8ZmFuWZKVstBdJieK9Do4evlZ46v6rebwrDLZashSRX4jY_tsORkKzd7nQw-GQ5T3hxb6L-IepDqn6te1A4r-UjeK5pwX2qlbxer_09YP8-R7hnTKGqvdt5meiwh1wNwJh67i7Glu670jODDnFmnCIi_9M7LPN-9YrE2gLdwBqrgOfe8Ji6vCb7x32TInI2Me-ChHwKJsILlJoA-vBvqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
| تعداد دریبل موفق بازیکنان آرژانتین (به جز مسی) + بازیکنان انگلیس در طول کل مسابقه: ۱۰ دریبل موفق
🥂
مسی ۳۹ ساله: ۱۰ دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100453" target="_blank">📅 06:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pea_U9C02Rc3k2ssk5GF7jwkcKV84cHyW9jGZPLeFPzLr0u5iwVinrd5l9pflTR-VEuRwqKo4xL0PMQfCbBC-vBVfpDLYUSgN-FnsNTbXOie7ilpfdU7ZgNsFJsT1ocVtrWz3CNN5stt2l8pIXpWzqOpT5gu8GcXEGSZfcbhqxkqKCWuFL_5_RrQZ_GdZRKLSAPbff7IU4IwYYLmx8HduEg59hEZFV5gwaH-rMmxvx6t3DjB4hcf9UuJI1lTw5-oIkNlo9HQP5tjbmbTTNeEVjBUN7e--sKwcfjy2oyEfoX3tDibiZt4HmSWwKsaOB058tYDvpV8Od4Kfs35e1XG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
لیونل مسی :
🔺
من خیلی از بازیکنان اسپانیا رو می‌شناسم. خیلی از اونا در بارسلونا بازی می‌کنند، تیمی که من عاشق آن هستم و هنوز هم اخبارشو دنبال می‌کنم. این مسابقه بین ما و اونا بسیار نزدیک خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100452" target="_blank">📅 05:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=slYoz8lgjZXRP7zf9AJqgNKcBviBTG1I4inFQKV3nt6aqb39O0xB-5uSdwz7k0OfxG-PUkEiVLmmeRjQqtaNAkR3bVNCb6138gee9W9ll8YzgHSC3ggrnZI8NXzaex2E_GMScrA5jKVAmJaWVnT1XWC3S5MufSiDQw5JtWwBtGYQT_DtbJiUQ-coJEIg9n2LVJTHrgRkU7tYuYHnPV4xOr1nhGKzigIdnj9Yi29gvGsxVBpe80IrfYIiIWm5vIjJdI-G35NX85rKpgeVvEgvm6y4OAezlUuHBgWtuj-G168JvyVOqSUXEyEyon469Jt0AsZzErrVd2TXZaFrJ5uJjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=slYoz8lgjZXRP7zf9AJqgNKcBviBTG1I4inFQKV3nt6aqb39O0xB-5uSdwz7k0OfxG-PUkEiVLmmeRjQqtaNAkR3bVNCb6138gee9W9ll8YzgHSC3ggrnZI8NXzaex2E_GMScrA5jKVAmJaWVnT1XWC3S5MufSiDQw5JtWwBtGYQT_DtbJiUQ-coJEIg9n2LVJTHrgRkU7tYuYHnPV4xOr1nhGKzigIdnj9Yi29gvGsxVBpe80IrfYIiIWm5vIjJdI-G35NX85rKpgeVvEgvm6y4OAezlUuHBgWtuj-G168JvyVOqSUXEyEyon469Jt0AsZzErrVd2TXZaFrJ5uJjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی 2026: اسپانیا-آرژانتین.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRWIAhdtXb5doLEKOxJVIPYApFt1ibm-9lcZlVrTj-zgPkeIZGK9Th84t_ZrQmkshLI7HduBLy_DezuOazG1w9DnBt51cUAnp_9o7kgcKCuLK28pM3XuwHPOTzYyD8SwHo2zaPRtZPEc456D9Ri_pIIf_oMYkopgdPSDkKhKm7TdE8WpM2kPYPLfTa7OrdSBoGbry3dXIpVEn5F7_S1ZmmnY1s0qCOxLBcobksUOGEA7IHKVa9CVWBvrHresAbh8GZqnmd5mwLGSI86hmzIB6YHbzF8R_ISSj7O42iYD1s6KFO6wp98Tw3FYxkyjXccPcw9NggRpUw0rfeSqcAKV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOyqaV4_xdcDhvVpi_bjOLiE8EImuRcNxNVK4eryQ_DQd9A_HDVqzF5XT15USSidr1z7QVOZgunDiueLa23vWScWNyvRMbIFAhZ6VxYYVutuQXujhFBPJv_qunrGSKGJm4Wkq2McE5zfyPjmw-KcIR1oIhyWEHtOtYK8LuXUJPXQ9swDwZHtM2KIblq7RwNsWIqcO5it9B8fr-7NQfOvP-PMvtLOOg6XcXhR9JtewSW80Lji_P6ereqvjgJxuvKMcEnzJ8crjAYVKcMUuGT6qriRCAPqq5xi1A9PgFDsFypGyGCvQeS-8pvTIXtNG0suy8Ixg-aJXctBlcZP_2Qyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=lUakfvGurSAyhwMMz27EI9A2Ly5bTWv_Ftf94T-evLx7RDBL3DZAOBftHejJ4EtdbWr4I5A0bcFSWx-hfBdDgFanp3_vWxeir9eZpH6a7yZY3yQxeRqwZzNSz4C0paKweEccW8Sxo2vetpqVgjLQrVbP9AlpkPiceK5YOgLtuLpF2m51OPjde0VdOO9Oh9MNLT1ZaE7fB0vyPnGKuaPalUcYTGqO-LhJ9G5tdJnj3CHRnIuKcIJaa2O_JNm0rztAsBOICvHZH4bZ97exdQnNNYXYtwzY7tS6c_6QJJeAuO6fzLRWxknQS0wazTQakPlVd3mnLEpT_Xe2sLfPljAhdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=lUakfvGurSAyhwMMz27EI9A2Ly5bTWv_Ftf94T-evLx7RDBL3DZAOBftHejJ4EtdbWr4I5A0bcFSWx-hfBdDgFanp3_vWxeir9eZpH6a7yZY3yQxeRqwZzNSz4C0paKweEccW8Sxo2vetpqVgjLQrVbP9AlpkPiceK5YOgLtuLpF2m51OPjde0VdOO9Oh9MNLT1ZaE7fB0vyPnGKuaPalUcYTGqO-LhJ9G5tdJnj3CHRnIuKcIJaa2O_JNm0rztAsBOICvHZH4bZ97exdQnNNYXYtwzY7tS6c_6QJJeAuO6fzLRWxknQS0wazTQakPlVd3mnLEpT_Xe2sLfPljAhdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری اکت توخل و اسکالونی بعد از گل دوم آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=iZX6Xd60xs2ZlUOEKvYQNZuhRScLxoPgNpiRPf-KE6BVVsGTntCFSm1fH9fFh2kyuhE1p3M78dOxwgZWU7y8XwXnhGYlLTF07FCOi9-NeWyGZqoe_yvVcU15y0RQD5NnJAL2MZYbKTTmu8rsklFHZjaDLsKtypVPitdfwITktZ09ijdDjInTgHwKaVqyI4tSs9SqppdwlFPM8dgHUpZiRILPluPBw_89VolQFKyTLHT1nhRwSTzMP4ZyaDAUyVHw1Ee_VFF9VGlVRFkoAj1Aly2TJqdG3I5t8c7Dja4siPAqLx32_2XefFXqzbWQlRvFXrLxBRDAbYg6_tbrvkmduA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=iZX6Xd60xs2ZlUOEKvYQNZuhRScLxoPgNpiRPf-KE6BVVsGTntCFSm1fH9fFh2kyuhE1p3M78dOxwgZWU7y8XwXnhGYlLTF07FCOi9-NeWyGZqoe_yvVcU15y0RQD5NnJAL2MZYbKTTmu8rsklFHZjaDLsKtypVPitdfwITktZ09ijdDjInTgHwKaVqyI4tSs9SqppdwlFPM8dgHUpZiRILPluPBw_89VolQFKyTLHT1nhRwSTzMP4ZyaDAUyVHw1Ee_VFF9VGlVRFkoAj1Aly2TJqdG3I5t8c7Dja4siPAqLx32_2XefFXqzbWQlRvFXrLxBRDAbYg6_tbrvkmduA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل کل مسی و بلینگهام
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai46WfaZmDXBz9zLPMA5MIvsluR1evRUuFxz0gCeb4gG7Ok_HMSJAkJv4_XXwS-i-Giz-vcpBkDsYchTCODDuzOkjoJFdtTfEwOgvh7lPZ4rEOFarqvh3Alto_5hzcT4SnC_33I7spyUJ7TajOQQqhhr4XilNiQLZt8JgQc0NJ95Nk1NnjI3UBqfzJgJBzMdOTywMRYQKac_4P751lcyGk790BIKonJDNPBg28O5sqMBhSuo5BXfzMQ8KCG7Nr-GYWQnV-1-u2M_I_-IGotD3-e7V_CIlsZ7UXQbY2tCQacd8oN21Mf4yc3i7EUozTUA1-lXvTIus0awnKWudIKIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Qf5kwig-oDZjyURNwvFdW3BntZNXcAUfpuvsz1yEKEJWDK55c46go74xL9sQ8SduDK8OIC9MOmzCgjUgTrXT8NNcJtBEePbBrZbRq3yzX60szzDp7WRHRg1howjG7zwkqVk2gxa6WaAyEjB1lo0BcTx82OT-6WRQc_ZcmOdcvBQtvdYON7Ldw8j2q8QcC-Vs4cDgjvNie624C9GLXMXrHDQ5jt5v3DkSzSf0ZULD7ZDan7jdpcqRwlsa0UZZH8FVx9C7qWG7XIGLLIcE1VeRwQyrDniaIv7uMFAxCDvvuqVgeax42ZqEMwKKS5soVXKTqBoFCBSFnTiIeWUZLlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی:
این جام جهانی دیوانه کننده است و رسیدن دوباره به فینال باورنکردنی است. من به آرژانتینی ها در قطر گفتم: خوش بگذرانید، این تیم هرگز ناامید نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100444" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BccT7cByP5YVMAkBQyc0FftnUPCJTPPTZwhzulWNPoPtOZqyW43NxDNY21Sz7qC3MkJ9armubqVEVkCbNcVNXCD1KuRIUw-r1dsXD3E-1qDy-toUzHSBcA7T-ZQ1_9Yuvi9CteQzb97AhVDl-1D1tHzdrEkwxQT1jWUgRHEQ7mdjhk-gBJsa_i2V_7CPOCXzQBt_l5Lx6mHtfFQRrMtdGaGEF6J3BTxd8rOERgAswh9GqE1WTmceAMZKh727XBcxA_IGF8fV6jO5VBHNfSH_9xjl23IHLH2SGy3euuQOE1uvvSLpviWMj0UwGSHFW1ZVrl3UyiVNRDP5J7-z2oel5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGy8FETTO8Xnq7iBLFafRftgnZX-RQBOHQ7fRLzQVGTJJMaatmGKVa9ASa8xyeyYslUlhxojUbTh-SzoV9xx0ku-k4O9Tfj_vPdtpLIg360cMhnqcLy2FD4BP92LePe86z1tsXu9NyKOcy3cBCx8flHy52orxOXpJmlutsq4j4aRSRC27klAvQ_HwTpmUyIwrjS4YhvBpTxBNE5RsBs6Vtedn82dwHyo19vjWZ7cXxGek78TkjfRjpIp7qf0TN9tF-c3Z33711uJcssAmkvQxlqwuEPlIImJovJh-2DLa7rNV48qCboxJrJhXMsUeaeGJIafM0KvDj9GL6an9c3D7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6YAadoxxepiTqmhF65z1apwuHc5SqlZHfgapzWS0Z8YV_gL6nufrbvgcgeHFZOFOY3vmneaO-mnaa_AFXP-Hh0LfgK6HLSdZ3Of29va8XYNDuuVE9GAb5OpuEtaGQGjjH7KiG4OQ1nGHfALURWrlEUG7AGMHQzvwJI8rNQa0mn1inTisKRRDAsxp9ztL1HV3L-WtuiAdnwRrl5wRe87ylaxfv7CePtoUYtPLPhQrQwCLA7_dWPNQye3P7i9gGxio-094jNfPtvJbiKKMXcvxwrZ9E1yn7-kCJCBl0DSZ899opNgY2Jlp1dr_HgMJkNfZCKdLCyD0K626xNxTL4Vjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🐐
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100441" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pojbg284sst1uFsvBDz9xMnQ_sCm6aFyQIKwAYlZbRJFrxANasT6Cd92YQNLA1p0rZIvulMdxgGcCmLXVo8nGylmiZSM5Jpnv2CWvWlWfmEoVzAhb-X26egp2i3mX9VxtA3xtLkP9t7rdBsSBFVNP3kAdMa-UOU_3A7jr_JeZcEcI43a12sw6gwfxmPd892lqThlqbfwrLWUrgfLXIIAN_hYufpIWx3Zse3SH4AMo_AaYQdL1uEWfaGn2u21iHgTN-CRdzQsJ63pHKgtvThkAP1HBRoJI7NZpvEJd-_9w1iwAlDhrBFex4Mo_1bPl1Mi1IF8EePXO4mpqq8D_RAI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100440" target="_blank">📅 02:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135c24c050.mp4?token=bhtpaUf1z8dUHpdKFCz8nZes_fq87iTXa_Mmwf10jQoB4GlBiWuXwzEd3pkjdAEmo94Y_VzqZhKUMJ4K_oZNJTbSymG1voXsQrN7aiCVWmLR6E5qZ0leG-kJElTTsaAfBdHGMRh-hLqkOukqK6Z4Bq_FcABIFEymwg7JQRbJi-VjNhULc92Yc907gKV-bp9jeLK8iF_DdwOWySIZJke1Bdcp5glN4kgsqZ90xP1sSJhfA0MZGwI5gjfRIDkTXyJpgIU9BoioFTn3gqxISisG-FbQh8qvay9AbkbVGtJ4rAj-YACransyi-WlJrUY1zOOxvd_5hmM25jbfUXWKnQ_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135c24c050.mp4?token=bhtpaUf1z8dUHpdKFCz8nZes_fq87iTXa_Mmwf10jQoB4GlBiWuXwzEd3pkjdAEmo94Y_VzqZhKUMJ4K_oZNJTbSymG1voXsQrN7aiCVWmLR6E5qZ0leG-kJElTTsaAfBdHGMRh-hLqkOukqK6Z4Bq_FcABIFEymwg7JQRbJi-VjNhULc92Yc907gKV-bp9jeLK8iF_DdwOWySIZJke1Bdcp5glN4kgsqZ90xP1sSJhfA0MZGwI5gjfRIDkTXyJpgIU9BoioFTn3gqxISisG-FbQh8qvay9AbkbVGtJ4rAj-YACransyi-WlJrUY1zOOxvd_5hmM25jbfUXWKnQ_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
شادی آرژانتینی‌ها با رهبری لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100439" target="_blank">📅 02:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A30STVEMlxxyOIRxP3d9sAvzAAE42Ml_tizfpY33dfcTGcXIT4dhZ6ZqxSgRXa-H92VLiDbKnGv24jlZsctzoR4TPuGX09Z86jLNjGH8U3CQrJY17U7ioDmAWpIkbt0w_YvQVaIrh9MnJWzS5vPO_Fcu1Kfhqke4eQHlbVYqXdHJYwl3Ht3gLIKnPcPmA4583__bxdgihMvv2ZJ85CVWcJG_PRDSvX7xpeliZQkvZ57ClxiC32QJIQofFm3gaeEc4IpEsjkScjFZ5hD9b9AEXgeSB5vZn58QtqS3Bn-OrqHU7a8-RWaUzQy5mErEDr848UYmreCRjx-EmKSdx--Ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی و کافو تنها بازیکنانی هستند که در سه فینال جام جهانی شرکت کرده اند.
کافو: 1994، 1998 و 2002
مسی: 2014 ، 2022 و 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100438" target="_blank">📅 02:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=gUG6eADuuva3yBGrLeZQH7QppVmyaUvGyCrqakGvpPEveXy2Q_SlUNwhhGE9qQ4dSVpDwcw8fxeUE4nthD76std94gee2kYgAoETMevXjDpQx7Yyj42kd202bWVP8yVGmtuWvFQDMJlnt7OfvZdfGuQ0TGcdh53uiKmZcIs7kXMo2zRQUMDd2ubBQFtNvQohM1lzA-IrERQt5uLzAeyR8P_sY0V5AgAc_JySRzY8tKWVMlnbggccfn5WvCTaHQg7d8VeGy3gpaUcGW7FJGhfk9jXbGWHmQHzbmYx0iA781DQlnvy8Byvan9aX2Rpq6NYS2gCyUkjC9rLd9WFJ0krlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=gUG6eADuuva3yBGrLeZQH7QppVmyaUvGyCrqakGvpPEveXy2Q_SlUNwhhGE9qQ4dSVpDwcw8fxeUE4nthD76std94gee2kYgAoETMevXjDpQx7Yyj42kd202bWVP8yVGmtuWvFQDMJlnt7OfvZdfGuQ0TGcdh53uiKmZcIs7kXMo2zRQUMDd2ubBQFtNvQohM1lzA-IrERQt5uLzAeyR8P_sY0V5AgAc_JySRzY8tKWVMlnbggccfn5WvCTaHQg7d8VeGy3gpaUcGW7FJGhfk9jXbGWHmQHzbmYx0iA781DQlnvy8Byvan9aX2Rpq6NYS2gCyUkjC9rLd9WFJ0krlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حرکت زشت و عجیب بلینگهام بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100437" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100436">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎙
اسکالونی:
ما برای پیروزی به فینال می رویم و برای قهرمانی در جام جهانی تلاش خواهیم کرد.
هیچ کلمه ای برای توصیف بازیکنانم پیدا نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100436" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100435">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=vzEXMSqscfqbXrZ5Y2AMJbn9qOIqzBTm-7wfjVowChEaoJOKszLWbZkFME00b75XA8xvzr1TkjTHxEsNslNIAaFmENWWNVouLUoeuG2clwV31-iyupoTZotptcnyu_995Zd_8CFsHVNbDy4kgnp5FI5P9lpobS_wDohVlSN-zD1ArlNirRIGKWHB3eYT9r7h5cXjglJ6bE9BMcbuHx9dZ_3pT64E3H5iDrFra3XlHprUaTrnxFYrhd_mOM-mraIoRNP8842M7AF-YkeOGAdNYrBYpwUStxo2ZQGQyDsNLHNZ0vxkJNSWYAiJln-vRc3nHUWsx4A2RM3RVU_-XcqNPKe5-SHOCIpplLARjLKFxeCMNbUIPjRptAF8nAu96aysXXix0iUER1g0VDPRAZN63M7sfZc6DmZVEl58sOEtzwx6REUhT0CZCWk6fkt-l7CsJLlyfaD45sQHl9ssV1hqalB3kHfXBKw482mkuV-Whukz4-2F2DtPibC7sxPEJLcI8m2bS4IhSh25HpGFwqoI4LGImm-s4N6iPqjgPAIWJjJEHfLENE6zt5BtbM4d-NS9qzXkh0UqvktkPjmSPiVOr9f0Jf0uZpWvplgZmhOcnwGLyynGnkK99DRGUBWw5fSuED5uBr-5ApcBk3G81X_THderGJ7C1nJ5HI6Opy73gGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=vzEXMSqscfqbXrZ5Y2AMJbn9qOIqzBTm-7wfjVowChEaoJOKszLWbZkFME00b75XA8xvzr1TkjTHxEsNslNIAaFmENWWNVouLUoeuG2clwV31-iyupoTZotptcnyu_995Zd_8CFsHVNbDy4kgnp5FI5P9lpobS_wDohVlSN-zD1ArlNirRIGKWHB3eYT9r7h5cXjglJ6bE9BMcbuHx9dZ_3pT64E3H5iDrFra3XlHprUaTrnxFYrhd_mOM-mraIoRNP8842M7AF-YkeOGAdNYrBYpwUStxo2ZQGQyDsNLHNZ0vxkJNSWYAiJln-vRc3nHUWsx4A2RM3RVU_-XcqNPKe5-SHOCIpplLARjLKFxeCMNbUIPjRptAF8nAu96aysXXix0iUER1g0VDPRAZN63M7sfZc6DmZVEl58sOEtzwx6REUhT0CZCWk6fkt-l7CsJLlyfaD45sQHl9ssV1hqalB3kHfXBKw482mkuV-Whukz4-2F2DtPibC7sxPEJLcI8m2bS4IhSh25HpGFwqoI4LGImm-s4N6iPqjgPAIWJjJEHfLENE6zt5BtbM4d-NS9qzXkh0UqvktkPjmSPiVOr9f0Jf0uZpWvplgZmhOcnwGLyynGnkK99DRGUBWw5fSuED5uBr-5ApcBk3G81X_THderGJ7C1nJ5HI6Opy73gGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇦🇷
🤯
کسخل شدن گزارشگر آرژانتینی پس از گل لائوتارو مارتینز به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100435" target="_blank">📅 01:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100434">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIJgYci4LTzDpAiEWcY4vUO9kkSWv-Zne2X3pagmDvwn-s18U3MmK2JcjdEIUfqocUa4xYkm3KokcwRaaNOgv0Hfi8wt7XzgTx-YFCUZsIJuup79_fk7MLKToT9WP-NtOrvcFRjyw_IKeE5U449dqaJUBl8Re_PXsIZVjS-rRFBST1dSmZLpVTbf5lNpHYlHEJ1AwX27w23taxR1czb2Lha9q3owwHUspIC7Mn_eqGeF4Wg87mLw8XeGL5zc2EvF7W4iHz1dcGJJqwTquNEel7vAFhH-P3-XYjKclLOlJxcK-HvKo2zb9Kdf8cSzMlOcDyD-YjwTzpMITweD30kOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ‌هالند بعد برد آرژانتین
😂
😂
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100434" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100433">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDRmt1PdPtFqQtv7583_reWV4dBw2XEkiPyU9HSSn53hgTlATgBKD9RHNArzzq98I020krvcp9dxwkWMye_n66U8P67BdGWFAtTb63BfeEq3yOB_GLE1DKe6XLpgadCXyTsI88_ql5gXX88jptMfgH2OUSq-HcnQKrWSvwqsHtMFdfTHyCcf-zPSrQXgj2WWR-bjh4l88X7fslQiSJjRTNmMinaDHinEu8NVK8rbHSsnEqnjOtzuDQIyo6TgmDwJo_k-R2NBh1bJCtmoQ9pdh1PygcKb5p-zeArc9yAFb1vKOf267mazH49Kra8p_1R918_ciLomlkpJaDerKgR-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
خایه‌مالی سنگین گوردون برای بارساییا
:
سال‌هاست که شاهد تأثیرگذاری لئو مسی برای بارسلونا هستم و امروز متوجه شدم که او حتی از آنچه فکر می‌کردم هم بهتر است. از حذف ناامید هستم، اما می‌دانم که حداقل جام جهانی را کسی خواهد برد که دیوانه‌وار بارسلونا را دوست دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100433" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=ZMK9SfBQr58-2m4RXn8cuwm3kgxsJA4dQauBHEVMbpHOzqLSz6kYIrtnacMbIlfuttx-n7YdtmF3pYAcEDu5TfHk-4ST3TwpoT0rxXlghvFYzxJYBYxGKCMRUnxnt4mDaI54npYJ7jL3bKnqFEFj2_MnSwyN5NjOxbE4B9imdn8jBVTHWJCoTT4Y9ukN5MG5B0g_ON1XTGE-KuvUr2E8B-9JtzVr48hOOuyvZ7d75CubVmtDkkkqKVRm5g59XKxXrtTRccEnPCnidO8OQvhFlvGncyU90_ZT6Wy7TxYzRYut7amByka5j5V95ZJSvdHuMqpurSR984R9cXwYxXqL958CXdAaX5m9zwYu0RiFN-eqDAzAX6rYQaKs8j0R9xL8qdAnvTskErgSlced3vA8HxbzXk0EylKFtluWSiMR8FthR6qIQNcTGSZgAlnmu4_QHORBCcz6ZKuPVn3gF5kM_pHVTN_iir7DeOpUGlys1qDWC753QJVlRs9RIyHFp5BsA20Hhx0iT-R85_ODATNW5BIeIamsDJAJmqw_r4NYoU8JtrJYY6ZCOSP2XBY3eY-GrWNGmuR15P3Py3nxmmhf3xkCThcfhs2Sd5-PXeo09n1Q9bXeMZeFnOgIQc7zEPnQNHCB0L-SykfPCzOLVXQrZI_95m5QzO5eLyQeDLbpn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=ZMK9SfBQr58-2m4RXn8cuwm3kgxsJA4dQauBHEVMbpHOzqLSz6kYIrtnacMbIlfuttx-n7YdtmF3pYAcEDu5TfHk-4ST3TwpoT0rxXlghvFYzxJYBYxGKCMRUnxnt4mDaI54npYJ7jL3bKnqFEFj2_MnSwyN5NjOxbE4B9imdn8jBVTHWJCoTT4Y9ukN5MG5B0g_ON1XTGE-KuvUr2E8B-9JtzVr48hOOuyvZ7d75CubVmtDkkkqKVRm5g59XKxXrtTRccEnPCnidO8OQvhFlvGncyU90_ZT6Wy7TxYzRYut7amByka5j5V95ZJSvdHuMqpurSR984R9cXwYxXqL958CXdAaX5m9zwYu0RiFN-eqDAzAX6rYQaKs8j0R9xL8qdAnvTskErgSlced3vA8HxbzXk0EylKFtluWSiMR8FthR6qIQNcTGSZgAlnmu4_QHORBCcz6ZKuPVn3gF5kM_pHVTN_iir7DeOpUGlys1qDWC753QJVlRs9RIyHFp5BsA20Hhx0iT-R85_ODATNW5BIeIamsDJAJmqw_r4NYoU8JtrJYY6ZCOSP2XBY3eY-GrWNGmuR15P3Py3nxmmhf3xkCThcfhs2Sd5-PXeo09n1Q9bXeMZeFnOgIQc7zEPnQNHCB0L-SykfPCzOLVXQrZI_95m5QzO5eLyQeDLbpn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جو فوق‌العاده رختکن آرژانتین
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100432" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100430">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw21Bb80OAcZ11EihyOcgh3RXJVeOYxRnrIAmtp9_YUCYoiTAUXcWb519RnUpxJEx9wS5fF1xFoZ-hvf8malPR5ywrwvJjbYog0ov31lLE5PdcK7cTIf9E_0nncNEQY7wp3kMh2WELAbJsQb0fwJe-yWx4s_zRTfKouxfOh0JZ0bWOQDlOm4MkKEVA6i1bHXOzbzvzXLuUJ8gXyNyyrgnHvPC0nMOkmPHHmLb8xA9KKT-DhY_wgIVWtRUPcWLd0H-1LsJfqOohaTvjhByb09-ABOYW0tCkdyQdQhMpMDuKo52wTv7vLxmdpFfj8e34Tu7NTSNWMYbSvWN8iLnrPhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
هری کین: مسی یکی از بهترین بازیکنان جهان است. ما سعی کردیم تا حد ممکن جلوی او را بگیریم، اما وقتی توپ به او می‌رسد، حس می‌کنید که انگار دوباره به زندگی برمی‌گردد.
😮‍💨
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100430" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100429">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9-ylyh8CAhj2Qdr-KWVRrdhinTCCFrquFzA5VNkUmEsC8BWl_l_3cyzP8pBszNxdkR-T0FID_HHYVRBc1kwLvJqN8GP-NUP9BlCHCAYxkJ0P748h1T7LKOBYcDhQoLeSJOscBxgric737U1gnm6R6cikfb_wgnFL5v0X2U72rWtImZMFyehU8EZBaeXQxXM9v53paB-H1oBbYyMZ7KgvOLcAVrG9WzJPB7ZLRC0JqV7FXsHyTkUahjWKWMQHrdAA5aFxMTK9muipQVsPyNhKILcMRIeIqhPXiErW15Q9lUlYstXc4bo7uz-yT65EkUiyXQZ1CBhw7y5fJuHIbqLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇦🇷
طبق آمار اپتا، احتمال پیروزی آرژانتین قبل از گل انزو فرناندز، 1.3 درصد بود.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100429" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100428">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaPEK0Uby4goexb8dtfEr6cfR-RU-NpNNQorGGNO3P4FQN93aE5Ttg--DUcFkEJjtBWOuKruVMHJl2ASFP2vS2X7bMxK5ckc3NKd7BbeU4RL8wJZdS6YdPrNs0SCaM4b82gfAWrNBqgTi4GMd2Z862gAr4ADjy-0gL-V7kU3gY32ezfbNdOOQkWZLWVE2lkIbUj0wtBciR3qT3BiFM4uYGa9xe8Yk6apO6eX03kym7nmjjdRXrzdM3_jfabE1QIqQQuc8Xf6XZGEpfRWJ4sOM_C9wQCAnSrM3O08-_ODiG9-IxYF6AazXaNDpDcuSiheL4KgvxXkpA8ducCmExkSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
🤯
کاربری ۵ سال پیش پیش‌بینی کرده فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا سه بر دو به سود آلبی‌سلسته تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100428" target="_blank">📅 01:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100427">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_GYAK_rX3Ou_BQiEI578hZNHufniuwTHovynhB2hvhabUI_pWlqLDJ7YUTSTxPXikymzKkZY2WdCEOFkIN-7T5Z1zz6Sdh58Jqrj7gp50C4nTYLsUqmSRLsRR13njqSF68hEgyFk7gmjMEJpjQ7n860lkMe3I2iJwuh_cBI-f3EhjHsJozF75HJ2RWSNp8i6kTsIOWzK9qTj-hvxAVQpoi7GcXZBBjd7CdO8lruTPkinVYoeayHay53Sarp1z32j79F0adplFFQVJcMn5dgnNLxlbbl709CnjdqellcxGHBOdz7TN6bIaYrunonTgX380oMpsuVy9PD7StSobKUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
MOTM
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100427" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100426">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS7-0o7J7u7lUKW-tGThx5E26mTGwLxQiXqpL7bT8OUlnt169Azsm6BBl79NU3OeYSGrejb1YXklnjkfuJBwz73uHMaU2X1RKT3t4wFzAs3JvlWLAu0MK9nf3q5UASgV90xYrbMX2b0SL0g7Kuhcb7v-J47rN6DrIaFKYsfN3O5a2sZ8XAfWq3jDOks9BaOmKolHupoieddDlEl_EMYT2ib1Vb23kkd7INBlCIlEzXhPEUfpCfkUpMeC66DkiFsv8A5IDl2dqzvVe84PzBetQhIh8YOg9MclIh8owPk8g1jWc_EqReYS9rbwaVUULhX7qCSOz9wKMct8IbXqPVn3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری کین:
قلبم خیلی شکسته. تیم بعد از اینکه جلو افتاد، خیلی عقب‌نشینی کرد. نباید اینکارو میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100426" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100425">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARchS8x-Fumtd1wszkVN8AnzbgAt88Xop15utIECfNTqDC0ocsAHhoRPWzXO53h57Tr_P_BvCM_pKyar5_qkUSQycZoejm-TZCpac3Alr-CLBSzW2Gb1jgTxIuMroTILsuwpbbITZKLTunw7UyY-rIE2NkUekI6lBPHzw4i4QmoLkVzKXnexX8K6VcNqsh-RrZBg0OYXOyGZZtn0bKUnz6LfVMRCCnpYuSnrcp7vkQ-r4_CUj2j8nlUzaWyKe4dHclPVJl0S5j2tOXrYEBK8w1dJWl4wXQSH3zNRQShkRuRzVgdTBaA6tsf-r5qeSaeFknJBI5uFkRX24Jz0sYjaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: قبل از بازی به صراحت گفتم که لیونل‌مسی یک قاتل بی‌نظیر در زمین است و از او باید بترسیم. او در این سن توانایی خود را به نحو احسن ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100425" target="_blank">📅 01:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100424">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVk2_BGI46iZ_M-liDoiNqFrBsQpkLdSTDV-sq3HK47Uid2ZYeK_20lhSRHbl6vtEo-iZ1uU_pPDebwcOXjqrZUCKFqnTQ3_htsLtrIBjgQxXLBDaFsj_mQsFu1blf6KycvenqVGtp5BbU6fGlKewdkGzJZpV2qaMeX4PZI5WarsjGSoPNG0BPnBewm8RI6qaqwZT16Q6cYwmI6xv-cuZUik-uizu8hKa_KJ7GVyhsKmuTWiouMieWf4dlWcc7lf6MA5eahuDUSZgn0iAluMRmH7P9aQEG_IVdGuKK9T9cOMq0A9zj0AOp-bfSOkBwgYKN59vWqvfbnadPKjdY_KTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
اسطوره، مسی، تا به امروز، بیشترین تعداد دریبل موفق را در جام جهانی داشته است: 24 دریبل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100424" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100423">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMgTgAJa8F-J0L0eY_wi_aFFF6zshyGt3gfmVu4UNTMMCxTa_-rEJmSrwLDSveIZyt0VwIPAOgwR9Eg2yJKoycl4VQG_2E0KlKHFhkoYTKyJQ9PUbYqb9VLS00z5Dbf9FQJAw4Ly6hgTsqbGGVJDCX8AF5K30sLsN8LcXA9GTPOzEN43aSLoxAKD4BqvuMqdC8cqgmjAvfm4Vgk9UZ1ABpSMNMVBB-nA7uYC-ewUehM1M14529bUHBOYX5ipRbDlX0jvv8isUnMzudwUUQRg8ggXWgaMcJjJXMEMfU5a03lwHO3JMDAG6pJqP8XyWAoxgr1QwzheiKsWGC5CzD-oJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: شدیدا ناراحتم. نمیدونم چی بگم. بازی ضعیفی بعد گل اول ارائه دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100423" target="_blank">📅 01:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100422">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX0Sk46wtmqF7FLfOQPuSTo1oYaRMw7gp-YutOhNG3m0WdpuKHyVy96-RWedu8VJlLr6I2ttOt9a6BHBYUQqKQOchciDXNaGMU-Ea6CCScKdNJ6QTNP5uA6JmLRDgbPetTxkNeIT0OY7JSZAmEQOmdwn9Ep5VKXKV-MKOvgJTBOqxLPjaNxejkLFaLPSJoWzJR4e7btO5Xkq2DguyjN2HSKEaFJSfT_Zwfrl52XGFJLhl-7s6KVBSWADZtYYr_C7b_HSuW-hXCM3SqVvm5WfwTrhAhIToxRY3pJA2EWnOrWdmKUCSxQ2jun8ocZwKzWKOtsEc1JcdnfFlHETyPUhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100422" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100421">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX0t_FiGyAAMK2NzR9OSt-GzzaUre7vHeHnXXWxd3RWbTqgu0wXdSyhG6ttr1kfeLmTIXOrD0KQihYTTk6m0Yvr3obJS4XhjXu2NTIMjJ43-Tyaxx6yT32LSJT5w--TeYB3yeXX1RjGSLYMLITOcRqgfdv8ffRWLxQZcsSebB6QOKUBNwFOPexMKspZWr5B-3GguQhFH9oUx_q0aLpMtp_8qGRkOWuloL37pB5yJWDLJrziYbw3JtamEQHGsHAyoMNeh2p9hY2NdtFMa5hhTtf972bp-uSH8EWdkJJ837lX5lvjpqbp5OMHn_dpi6x83yritjlrYuIhzTZPHxNjZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
⚽️
پست جالب DAZN: ‏بعضی داستان‌ها تغییر نمی‌کنند، فقط قهرمان داستان عوض می‌شود.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100421" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100420">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx80ra0zDIpNhUsfbZWeoz-OKsYSzmgYW0AkT4fLHO75APTL8lNwYwVqPAIbfcjju6eGCmDHaIGAbrpqOWWKfojcFKwQwBuXaH0XVFIUuRl2BLoYPMag83OpcmujAuNP7oes2CpvHEfixq3gs4hpG__RUDIub5dkCQM7Tj7N1Rrue0RFLvGs6IfFupXq2o_nWI40MDwtZQ4n1eeo8w78MWMoK_McC0An0IKP7xGSoHCCXooPzrTsCG09mVGeeZpYAhogdWkY41k-X43DFPwSnirY1ijUrN_UbqT0kzl8Z-QlhWQWwhWo4IdP1G3blrYGpsuQberVDb2w0i4p6Xmhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
کلاس‌آموزشی احترام به اسطوره توسط آرژانتینی‌ها؛ کاری که پرتغالی‌های بی‌لیاقت برای CR7 انجام ندادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100420" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100419">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d365933365.mp4?token=JlQIF2vJBjrrJadpuPi_WjtgM-Sbp3Ig7cqrRLRlLqBhTs8xb8cDc68a07bM6F8v13voIanpsgiR6HMOtaD4ZCZHOx6w_4diJ270MxbeI7Yc8bNPS2Mt30R8eVCYNlRwToq0R_5Vg56t-ahjeuYBG_AF0mvqQH0OquHIu5iy3zxjxq1XWNRZmb2E_OlK7JqI17aVUEArqXci7c_A_MapW7cSZbBfWziUX5bEKYuJWhENiXV8tRqdffClm2DFQnMfAjw3zDWcvYbWDt8fDrnGTpWZ6yQIdIxJ_6j1zAmOznDjA4kcT4KzvUXXFjPN4ZZSajcQ8PdFojWhwaXuWJdEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d365933365.mp4?token=JlQIF2vJBjrrJadpuPi_WjtgM-Sbp3Ig7cqrRLRlLqBhTs8xb8cDc68a07bM6F8v13voIanpsgiR6HMOtaD4ZCZHOx6w_4diJ270MxbeI7Yc8bNPS2Mt30R8eVCYNlRwToq0R_5Vg56t-ahjeuYBG_AF0mvqQH0OquHIu5iy3zxjxq1XWNRZmb2E_OlK7JqI17aVUEArqXci7c_A_MapW7cSZbBfWziUX5bEKYuJWhENiXV8tRqdffClm2DFQnMfAjw3zDWcvYbWDt8fDrnGTpWZ6yQIdIxJ_6j1zAmOznDjA4kcT4KzvUXXFjPN4ZZSajcQ8PdFojWhwaXuWJdEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم این چه سمیه
😂
😂
😂
😳
😳
😳</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100419" target="_blank">📅 01:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100418">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGUbho4NXkbVRNG4NRlzJnFRDgp0jSsEP0FUe1IbtaocgeSUorw6drMDF6Gx-HDH0uc0IlCToaBNVq0z8RF4Lwm4wFT4RENGVWPTmS98MLLbWbsj64pz1RiNX2EAAvcBai0dfMlF6jPu6yzVDgS9wxtESn_M7MlQfstxfA4mVQyzyvh4QAWP64oiweGciL1UcL01Y-Dez-ZpFgu78a9x35s2R5mKxNuIyfWaV7gBNkkXL1cDTuQ6jkDFvZcoQ7kHroj8PjtJaPm2USC_xwpGrVMkfutVA_ijXqNhYCsy1r911PZ5TbRDD0lfcZT1NyaBopsAWYjUt80lFaai-5GU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
لیساندرو مارتینز بعد از بازی
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100418" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100417">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUHKmripf1LqFzYlwplIzof104ytvm1dCDzVH4T6eWDEZ11Q_3o2hWBI8GYWHk8X54dCbWnmJJ2JLBpvmswxFsNkKdbR4l-eUlnxB_-BasxoBPB6gpdDSWOYL_Uuw4hFD5WC_b_xHaECRztwhulZUQGe1lIKtSyHjsit5tnFT2enJWigyg7_e6u-72MiB90ArTrEgeo0yzD_iM8JMX_u9miUBOl5BU950YsaJzqgsYgbDtqKohh-uy5vfdmy6DEVhXlb0KidPLtV3gNWu579W7_1B2O1bavLzpkDAz8vcAcV0953ptmaKb-fpEhw4Eg2_cUvAf40NKBrfGJ19tIa7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو جام جهانی و 2 فینال
کسی بهش نمیپردازه ولی ایشون واقعا مفهوم آندرریتد رو برامون معنا کرده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100417" target="_blank">📅 01:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100416">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRDqX6M40Msfi_Xj6PLULANvZnsRjbVU_EI5Jv4J4bL9IhDlGZkVAoSANsONYDmdwZD8nEM98jYS3U6jPFZVEWqVzgq2onIurAAIFQ5QGRJrzwpXZwLr9oPt2ur-ey9_wr7eAD_0rcpvxxkaiqhUK8e_NyIzQD6Uv854jzZg9PitoOJmulDoktVvfibbt9WtrQ6gSNHMxanlrM6PBJdEMpIZZfqqKO8BpiRUn8ajVVc1b2miMFtQ2AqK_S7pj_NXHz1QNs-fG2f_1NbWtSCInGGXJCispD-YFrDuFSE7Xe8VUR7cllfoyi51teK-APpdVEWb_0nMQoXi-9BLQUiwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
لیونل با کسب 87.1 درصد آرا، در صدر رقابت برای توپ طلایی جام‌جهانی قرار دارد، طبق گزارش پولی مارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100416" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100415">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g758OrS1EqoUbMVGBeKlkDIojzauBj8KgOs7mKZuhFOtzihZlMYC6WPdBDbKapF79EDs60s-HljeHko3QkfDF4CaUYGq6SUPyt7-gaS3sNyu1pwYzf7OW3uqcgPpFe1h1cf-s5gwD9fnFiwhtq6hdJWQhfaA95bYNtX9VFbrUCPpvMTm34rQ5QVh_OOtdvqu24zJyO38PHx8e8cBR79Ytzd2S0GAm43mM4QBIRnwEKwCJxMHCgaiDWzzy_Z5HY1h5xMFm1JdMD8j99gsGenoh9gu3w5W388Wnfs39xT2rEge-90GfF7PZrA9hAxrvmUo_oD7k_Lih3Cw8TJVdZgSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک توخل بعد از اینکه انگلیس گل اولو زد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100415" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100414">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAUqxPtstTNdIDRXCy0GhF8o4Q2Ls7RtsAl9ZhOejLL43PX0smb8Qn065WMifXtXCsEqmmOe29R60sQlFgpb9Vuk6tWD9N-BqjDSpsyD_bBWcPskD3eqdNHNZjsvkWnuKOnOZGo6C9tLwhqIAjSbhKTif9G1SotYIB1balcsDCRCpghKgrILZ5n8iPnBIC0gTqy-ltaajC5qhsxPlxBGLMEV_tfH_qlt4N0AOihZZ0wGKmx67j2cqp7-qxjR8Du_nqRkoazP5d1zR1ZOnXRpc-2GvAwOI4KKXMwE6irK7D0g0HOVM-SjAWWssjhGaSDCSD44n0vaDsKJf6rV0CcSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
ویلیام سالیبا مدافع تیم‌ملی فرانسه بدلیل مصدومیت از ناحیه کمر ۴ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100414" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100413">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100413" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXbjZicWiSrwo74lvrPOSu0HOaTOA4Or4Bt8vEW0-e3UatGdbXCfaGW5Vc6pOrQH7asc7uOBWstethroil8X1OAakDXeop0Rf_cBT-NCDFZbsx8mwgL0lRVr3DujsjaOhewOL-aQt9LjLyM5846ak7Wc4nY-6RlzXgRr3GLT6YywgIJm8Jzs8WQY1nJ3u077h2QrtLb3DlbSwtdhmrovZ8UXGuhRGhGNoGFkChavSLhm3t4XKF9myta4L84CmtzMMG9rZRDjFZr7jjkpldGroxwBvAk_9FTXJNfFNG5unGjU0YsOXzs6yEeyFVJ-G5mkmIu5tWCGUTAE7zFc3cTH8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100412" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
از الان بگم دوستان رئالی - بایرنی - منچستری - آرسنالی - پاریسی - بازم رئالی - وغیرررره
بازی فینال هیچ ربطی به شما نداره بهتره نبینین و‌خوابتونو حروم نکنین
مرسی از توجه تون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100411" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ4cWA1p7hBldGEdeJ5w2JGhe0xqVLukGjZ2ya2tKZvpJ36hHVJKL8A69-TpLQ79CX07vmLvgL--ZuFPsTHBHRHM3veAiWMVXuHN4UNyvTsoh4Ro1jqdBmbY9FeRxDLVd5_L1mh5o3JAN72TPh6h1mKINWmqe5fEb-fP0-eor_lT2BVIRVJTshxVTjBnyQybvgYDq-7K3C1nPClMrCXTBU98VlKYBE1bDNHNgnv3LTugxoEgQvI-F6Edh0z1sgPdxj-idMX_DzAwtWYZG_2bGywJR0CIqWz8s8SqLzjH6k0XOULxuZrf-9sOFHwC6sbWEwxqtr6RpY0nx7kbIVEe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روباه مکار گریه کن پدرسگگگگگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100410" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
