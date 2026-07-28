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
<img src="https://cdn4.telesco.pe/file/TFVI06otTWwqb3qYvcO7VHKFGXtD7EtWSsg1kLAwT_t7qJ2E7Y0yY1KHmMutoPd2xfgPm-JO2NOwWYZ29S05au9Atroaq4cKUa67gPkewEOSGQXdbBWMzFiJO4x8vpCOBNlCgnjE6_nzAxkP9nDCHgHcMMKJz4r7DoN15e5QI5-hUlWjJa7TaIAAmKkgrN5BosaoF-G3N6ZxmQb5aPr4j34FyR1R7KnT-6RjH--XWyi-yRx9vWIMq34MZ8gfejtnwehzeBYt7JQyqjVuTkJ-9Xn6L9_g4h73ZZiu3aYSgGuy_du34h3XEnj5zCXJdUJWog8Wn74gjAGkW7hQMv0kew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 00:35:05</div>
<hr>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCWzFqW31WYtZzeExhwI8Fgwf1yFqFBn5W2Td4dhYx9cCgMA-Q1pDtYe9Bn6Cw4aS0nhUk4qFTwiXWRXL2q7Styck9idhKGt9ZiSkGK-RrDnUtsx4d0SLNcjGdoHfnc7JTQIbcLUIG0RcXWZhz-cS9k3okPAGTGXEM963ozhglN-q3T7lL4BxWlTzWIwsiO5xOgPFtAn3i8CG_EaJkPQrA4OE57MMP2T7NChVp5tyGTfSxEgkl5Fy0Kmm_usI_5ZFU6Qnk6UtB9WsrAQgM2nCnfRos_7gkemNiCVD84ZiruiXb0EEJXmpsHT5VuRExyLwP-HzPb4J1EWY1Qb5J1BnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:  برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند ترکیه و پیوندهای اقتصادی با چین هستند.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/19389" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j71-jLBqXp70we0SsSkPPeV4KsAQ2_ALB2FgWuqIRIjH7qRc2dx50QxyIO4L5exDmQqHwACpBDWXzW5h0PltQTSaJFMI1xYePBokzw7cUv88DjZDi0PvHika1AsMzHmeDJWBFEWpc-C5ZhsnOJlIFsmyqaiEIyr9TF2wJHQl0I_xPlsJDQo1RMxbVethMPyuvWjm9FLMww5WUSdD7-kmFkUZXDHlOoOd47ZEb4D4myQQehL-b_qukARDYYxgiFFM8RgVZ1B8SH8kZV2mgAW_mNnDA_grXVDRuKGEcfBhXDjDkXBAwjhOOzs5shtoXjltfxYXFSop9v0K8dR9XQnjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که وزیرخارجه اوکراین هیچ عذرخواهی نکرده و یا وعده ای برای جبران خسارت نداده است.  تاکید کرده که هدف ما زدن روسهاست و هر کسی با روسها باشد خب هدف قرار می گیرد و جنگ روسها ضد ما غیرقانونی است و ...</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/19388" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  من با وزیر امور خارجه ایران برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.  من بار دیگر تاکید کردم که تمام اقدامات اوکراین…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/19387" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  تهدیدهای ایران بی‌دلیل و بی‌اساس است. رژیم تهران یک همدست مستقیم در تهاجم روسیه به اوکراین است که با سلاح‌هایی که از سال ۲۰۲۲ جان اوکراینی‌ها را گرفته‌اند، جنگ جنایتکارانه مسکو را دامن می‌زند.  ایران هیچ جایگاهی برای ادعای قربانی…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/19386" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/19385" target="_blank">📅 22:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">غریب‌آبادی، معاون حقوقی وزارت خارجه:   هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/19384" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/19383" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQath9pZMJaiu4jHxUyo_LgYFFxR42iGtvL4XgKvQ0qUmugg3RT3pcnery4GI0IK9Jsc9AafYbd-BpJn1VL559StYy2a_GN7WxRwdCIRUtHHNjX7QNWn9i19nCtZtrrALWA2UNvErNqjtPUQgOL7bxqcab5z6QjzELnm6OWhGg3NLAcREhX7wENVvuG_NM2Qd6qzifrUd9rYot7TEHBG-iTqNbC7oFyQaHN5B-Eyfs40RIDYT8AJJJ8T_dMIpJMdah02w3oaFqxYwYHJtWTevueTwaRiZcIZkjyhFxjMlsL1dUybLS0RWBoqzOyh3HBqxWYiCLOtLiiyrXBKKXlTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/19382" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=MP87fFYkd1m9BDxyr82q6tHyRD6sbbH_Jt2uTFPxsxM8euPRRTt7DazeiaOUAeY7KxTk2qz41Pf9RykIsftyncPl-wtZNA3IQP6WCKUCJWU-_w_xqFb5WzdPVKyzViMPSIi6rsiMgD7U8-T_gKK1DNiIJdc5-cT61HsW_Al-mZxmB6nSCe640rgbx4hT4MQcoXkL_QjBlw_Uqsb4fhDGNksRtJChfnQ9cZIaHp8waKWeS64jisz9r1Q5qPE19kxVxsQGx89b5M6r9y7tKzLgMt3SDL-7bxOwjNSe6vYRryHLod8oUbrqUjIrGhkhUSHCqmBrk_mpJ2vi_6iup6Rzlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=MP87fFYkd1m9BDxyr82q6tHyRD6sbbH_Jt2uTFPxsxM8euPRRTt7DazeiaOUAeY7KxTk2qz41Pf9RykIsftyncPl-wtZNA3IQP6WCKUCJWU-_w_xqFb5WzdPVKyzViMPSIi6rsiMgD7U8-T_gKK1DNiIJdc5-cT61HsW_Al-mZxmB6nSCe640rgbx4hT4MQcoXkL_QjBlw_Uqsb4fhDGNksRtJChfnQ9cZIaHp8waKWeS64jisz9r1Q5qPE19kxVxsQGx89b5M6r9y7tKzLgMt3SDL-7bxOwjNSe6vYRryHLod8oUbrqUjIrGhkhUSHCqmBrk_mpJ2vi_6iup6Rzlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندسی گراهام:
به نظر من، من می‌دانم او کجا قرار دارد، و فکر می‌کنم او آن بالاست و به نظر من، او ما را زیر نظر دارد. من تقریباً از این موضوع مطمئنم.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/19381" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=MXCBmJhIjuYeMwRdaqSDmOSX_FDKvr-ZAZddsxP_9XNjzKWO26X7fwQwH5SOVN2tAsOFCVysTEwk6xfiRi0XTJNqpEt9eEboLF4p09EtrEV7B9DfaPVb9dZw3w_LXcnUFxlYxyEb16Uec6Yez-If6umoKmqJf2FIEw6kNtzmvFbuXVxiSli1DgrYOBFLR7Unk_rB8afL0XLCGjB-y0rQDMWDCiDF4Z6Bv0HV4YD7MjUhrSp39ZN2oJ_crcqokffpAlr6wGc2wZ-CibdLNPvwXc_zLuss7M9jqd9bG4VPCywzmC3i8IJwB7eXlGjtD9pdr5GKX877JENmrIJrOJPVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=MXCBmJhIjuYeMwRdaqSDmOSX_FDKvr-ZAZddsxP_9XNjzKWO26X7fwQwH5SOVN2tAsOFCVysTEwk6xfiRi0XTJNqpEt9eEboLF4p09EtrEV7B9DfaPVb9dZw3w_LXcnUFxlYxyEb16Uec6Yez-If6umoKmqJf2FIEw6kNtzmvFbuXVxiSli1DgrYOBFLR7Unk_rB8afL0XLCGjB-y0rQDMWDCiDF4Z6Bv0HV4YD7MjUhrSp39ZN2oJ_crcqokffpAlr6wGc2wZ-CibdLNPvwXc_zLuss7M9jqd9bG4VPCywzmC3i8IJwB7eXlGjtD9pdr5GKX877JENmrIJrOJPVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مصاحبه این 3 چه نکات تازه ای در بردارد.</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/19380" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvNYEuH8UBVrCsYBAfK085w6jZlY5GgZHSEwxRTl76AF0g4CRL-9bMhGff2XYlY1plN9NDt3CWT3RvfXZ7rQyCK7_ToPvpK4mxappBsgO_X45OqbmBLZP2AFMsZTAhA3qPqUYNJkGsMmH9oDMMyF4MZQVdVmlAXj_PiESNW6I863IS4HTMH2rbYU0X1xEnyoX0Lhr5W7rgn-Cx29KM4yY_1KNNfxSG5W94-e4P02z_jhPUaAExZBus0Qe_Wq8fTXJJQEIpLoxSzcNDX8g8KD1-6lBOtXasX-MOBLqycKG8xEiKTAZ7cjI1B3DDvrmfQMoxb3LWfhXl52M7i4Qb-l1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/19379" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">روسیه:  «حمله اوکراین به یک کشتی ایرانی، به عنوان حمله به ایران تلقی می‌شود.»</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19378" target="_blank">📅 21:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19377" target="_blank">📅 21:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19376" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/19375" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">غریب‌آبادی:
آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد
مجری صداوسیما:
ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید
غریب آبادی:
کسی مانع نیروهای مسلح ما نیست، برویم بزنیم
نباید پاسخ‌های خودمان را ضعیف تلقی کنیم.</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/19374" target="_blank">📅 20:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حمله یمنی ها به یک کشتی دیگر سعودی</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/19373" target="_blank">📅 20:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کاخ سفید:  رئیس‌جمهور ترامپ جلسات خود را در دفتر بیضی شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو به پایان رساند.  هر دو جلسه مثبت و سازنده بودند!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/19372" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19371" target="_blank">📅 20:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19370" target="_blank">📅 20:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19369" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها  افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.  این ریزش فعلاً بیشتر به بازتنظیم…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19368" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkprTpJEtsPvy7OuRg4GaJzwbxJMz08UIPCs33JT7u-hwSk3ns09JDGm-WYJ3AZE2Ni7dGtZaP1gGvOFxEXV6PSZq1veuvO7uF6aI5mfVIsMqz_qLWcV_Yu7ivvX2YGW3Mh13Y9GVCTQB0q182aFp8SIdoj9kW2Eutet9Ez_p8HblyENrKxayIJzPJgeK9r1uTLx6giqH7lMxEfYDw7jbCPXHCMaXV_8e_cYAhDNF5hNIyWhxdxwswYvwM2Yp51AEislSi5r9JEcrJXfI9oVYwKOclPB-8fyT-os7zukhFKiIvA92h1gZewPzPOguqv5MWYh0U0J_UksrFKji71WqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها
افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.
این ریزش فعلاً بیشتر به بازتنظیم انتظارات بازار شباهت دارد و تداوم آن به توان شرکت‌ها در اثبات سودآوری واقعی سرمایه‌گذاری‌های هوش مصنوعی بستگی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19367" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ادعای رسانه های روسی:
یک مقام ایرانی به ما گفت تهران قطعاً به صورت نظامی به حمله اوکراین به یک کشتی ایرانی در دریای کاسپین پاسخ خواهد داد.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19366" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.  سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19365" target="_blank">📅 14:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شما ببینید چقدر سرعت تحولات ژئوپولیتیکی بالا و تاثیرگذاری آن روی پارامترهای اقتصادی از جمله احساسات مصرف کننده و تولیدکننده بالاست که امروز موسسه ING در
تحلیل گزارش مثبت دیروز IFO آلمان
چنین نوشته:
Normally, three consecutive increases in the Ifo index points would be a reason to party, celebrating increasing optimism in German businesses and higher hopes for an economic rebound in the second half of the year. However, in this highly volatile geopolitical environment, even leading indicators have become rather outdated.
Today’s Ifo index reading probably reflects more the initial relief after the US-Iran Memorandum of Understanding than the recent surge in energy prices.
ترجمه:
به‌ طور معمول، سه افزایش متوالی در شاخص ایفو دلیلی برای جشن گرفتن است؛ چراکه نشانه‌ای از افزایش خوش‌بینی در کسب‌وکارهای آلمانی و امید به بهبود اقتصادی در نیمه دوم سال است. با این حال، در محیط ژئوپلیتیکی بسیار ناپایدار کنونی، حتی شاخص‌های پیشرو نیز تا حدودی از اعتبار افتاده‌اند.
ارقام امروز شاخص ایفو احتمالاً بیش‌تر بازتاب‌دهنده آرامش اولیه پس از تفاهم‌نامه آمریکا و ایران است تا افزایش اخیر قیمت‌های انرژی.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19364" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">311.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 14</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19363" target="_blank">📅 14:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19362" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر دفاع اسرائیل:
در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19361" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 14</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 14
سه شنبه 28 جولای 2026</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwt8k4nA6hgMgixf11hyDyTA3xfBnjPSoWkvGQ82CQlYsKAlbJ6GL0_5mR-gAM9gtNzl-KoA-o18K45n0e_oyGxDK1ftjhuHGEry5GrqbFfNJkjWhW8BP5VbBIMJ-DH7_ZqcImdNwEAbn8hhC2LoM-CY_nDlEYoe3xDvo2Ca4RpGhOYiEQJzbsHsA1vEWKF1chZV8j4xvtn7XN2wO5FAytEaNPddUlRmrnILIhuMayGpFSizzQatT5BoZx8zRBimeEnsaHeGaAX0IMtAEqOD4o561tDwHJoMLCeAkSIO1StI2nC_zyzVtV5oNQhgsAunbHZaDghagW75f2iWMOgoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب تأسیسات گاز پارس جنوبی عمق بحران ناترازی انرژی در ایران را چند برابر کرده است!
خروج ناگهانی ۲۳۰ میلیون متر مکعب از ظرفیت تولید روزانه گاز، شوک شدیدی به رگ‌های حیاتی اقتصاد و رفاه عمومی وارد آورده است. این رخداد، ناترازی مزمن گاز را از یک چالش مدیریتی و ساختاری به یک بحران ملی و اضطراری تبدیل کرده و پیامدهای این ویرانی به سرعت در دو جبهه حیاتی خود را نشان خواهدداد: سفره و آسایش مردم در بخش گاز شهری، و شریان‌های اقتصادی در بخش صنایع سنگین مانند فولاد.
سقوط مصرف در بخش گاز شهری
گاز شهری خط قرمز دولت‌ها برای حفظ رضایت عمومی است. با این حال، کسر بخش بزرگی از تولید، پایداری شبکه توزیع را در شهرهای بزرگ و مناطق سردسیر به لرزه درآورده است. افت فشار شدید در شبکه‌های خانگی، قطع پراکنده گاز در نقاط انتهایی شبکه و لزوم جیره‌بندی پنهان انرژی، نخستین پیامدهای ملموس این بحران هستند.
دولت برای جلوگیری از خاموشی مطلق خانه‌ها، مجبور به کاهش ارسال گاز به نیروگاه‌ها خواهدشد. این تغییر مسیر، نیروگاه‌ها را به سمت سوزاندن مازوت و گازوئیل سوق می‌دهد. نتیجه این زنجیره، تشدید آلودگی هوا در کلان‌شهرها و به خطر افتادن سلامت عمومی است. به عبارتی، شهروندان هزینه این تخریب را یا با سرمای خانه‌ها یا با استنشاق هوای آلوده و یا هر دو پرداخت می‌کنند.
فلج شدن صنعت فولاد و زنجیره‌های تولید
بخش عمده‌ای از بار سنگین این کسری به دوش بخش مولد اقتصاد، به‌ویژه صنعت فولاد، افتاده است. تولید فولاد در ایران به شدت وابسته به فرآیند احیای مستقیم و مصرف گاز طبیعی به عنوان ماده اولیه و سوخت است. قطع یا محدودیت شدید گاز صنایع به معنای توقف کوره‌ها و کاهش چشمگیر حجم تولید است.
کاهش درآمد و صادرات
افت تولید فولاد، ارزآوری کشور را کاهش داده و ارز غیرنفتی را محدود می‌کند.
کاهش سود کارخانه‌ه:
توقف خطوط تولید، هزینه‌های ثابت را بالا برده و سودآوری شرکت‌های بورسی را کاهش می‌دهد.
بحران در صنایع وابسته
کمبود فولاد خام، صنایع خودروسازی، ساختمان‌سازی و لوازم خانگی را نیز با جهش قیمت مواجه می‌کند.
سرایت بحران به سیمان و پتروشیمی
علاوه بر فولاد، صنایع سیمان و پتروشیمی نیز در صف نخست آسیب قرار دارند. پتروشیمی‌ها که گاز را به عنوان خوراک مصرف می‌کنند، با توقف تولید و فسخ قراردادهای صادراتی روبرو شده‌اند. کارخانه‌های سیمان نیز با قطع گاز به سمت مازوت‌سوزی رفته‌ و خواهندرفت که هزینه‌های حمل‌ونقل و تولید آن‌ها را به شدت افزایش داده و قیمت نهایی ساخت‌وساز را بالا می‌برد.
نتیجه‌گیری
تخریب‌های ناشی از جنگ، ساختار آسیب‌پذیر انرژی ایران را با چالشی بی‌سابقه روبرو کرده است. جبران ۱۰۰ میلیون متر مکعب از این ظرفیت در ماه‌های آینده، تنها یک مُسکن موقت است. تا زمانی که زیرساخت‌ها به طور کامل بازسازی نشوند و سرمایه‌گذاری کلان در بهینه‌سازی مصرف رخ ندهد، ناترازی گاز مانند سایه‌ای سنگین بر سر رفاه خانگی و رشد صنعتی کشور باقی خواهد ماند.</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7_KF_-ilChKG59zYAfeHSb_zBqnLomCWY3KpTwdTmZ_KLehJsnnTwFxIkVERH81YxGeJCKndVPeCL7-xmGPL7FmfaLbIqaUN9sI22xSnlUyyfMiqb1xtg21qs45aKwYee_e5JGYiJ_khsvI4kfgL0AMRKpa-O583P8s-yUDJHGDBwYh_SOyzh7y16srJDMzL9rtlCWXyDSFnWZLhiHIiISdupLmhXsIeosh7_5QWmqImxa0LXFZ8W68Wg2BpABXzvLcRA34r6d81o-GTR36iKcRKx9ZQRT0TxnMqjfytHDzuwhb-O4re5DMMc8z16PxOHMsR_CqgGfncyHlpqAOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff7yQXQzQPtblS8-eCgVqtQ6X_C64Q-q4w5LbVKBVbnENrCKRQk5MIEHy5K6W5Cb4LqDRHNkpWPdX3zdpKrLmdX4V04KbcxR3re6OdgR2kPH3uKZySQDpaqzc7vkJiwvSqmkFfGpe6bIScXSA_oOIv5PMgm4FGObhAQa07OpNUUcBuIS1snUoSIbCOacX63bDq3aPKYC4yaorqkxgJ0x6x80yUHohoyRqg2GvrWXy2YzMG1xqq3ryJyPoWnGn8wk6fHjoCZRAdIS8fmqs7QpRi5O927KQJ8_EaGDSX5JyMqHtjD_2j1w9Pn-nRBLVaQICrhOIVpSNXFAQ9zCNCCPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=ZMOAyBFkUFKc2kbQXWoMCFTU4GVmBR5alYjH4_SlWQa05cBkhKqESvnTgXLC_M_xxKwMzNnIEErBahbGWlc2AzKpLZhdQ20zW3KQACoYdBIXv9th4gZrRdhxAiOm7i2GB5hqhdBgUnY_Ul18m7LtXGbxFw0ZEWRZNwo85B9lxXCS3C7UvKy1P3GpldqesfmHWO_4JJ6UjgW_Td56YEO_0JrYjT5b7zgUDx1l40SCEfLOkJ48rnSOuWfen4R2GvzfJr1V7wVqZ5SD7kZpLwwkgoR_dHJhv7oTBKBlytC4TM6UT6dYPUQHqiUIwiRg8Kqq7wGIifoi82ANHqF95MLtQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=ZMOAyBFkUFKc2kbQXWoMCFTU4GVmBR5alYjH4_SlWQa05cBkhKqESvnTgXLC_M_xxKwMzNnIEErBahbGWlc2AzKpLZhdQ20zW3KQACoYdBIXv9th4gZrRdhxAiOm7i2GB5hqhdBgUnY_Ul18m7LtXGbxFw0ZEWRZNwo85B9lxXCS3C7UvKy1P3GpldqesfmHWO_4JJ6UjgW_Td56YEO_0JrYjT5b7zgUDx1l40SCEfLOkJ48rnSOuWfen4R2GvzfJr1V7wVqZ5SD7kZpLwwkgoR_dHJhv7oTBKBlytC4TM6UT6dYPUQHqiUIwiRg8Kqq7wGIifoi82ANHqF95MLtQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq0j6ZUm0S46-zT9SJLPy6X0077HB_1LULr9Rvh-NvuWozw9bhkps7Q0izvH6DbSOXqMIOj5O1FvFcJrHvGUhlkh1Zeyi3TfqV6U1Tca9HCBxd08BbQ3me0ILaNCIVO2UpqvUW-oev_pmaOMumNoVkKtUxe7qA1aDOJPJWEJWrUwsAFJ1AC0tcZLFJJ2MatZwK7OuAnMVXqiyq9z2uRe3gOCGVBo9vA0nU2GAelTpQt9L2B0JPoGgSnN6OZhlRIRQfA5Lw5eR1o7R5QMxtJoEZlV92AiXEHgnNWnY1-uih3rmznhRtq2ROcs4qKMxl5NYkLKybyeIYiADG4PG1GYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgAaSEt5A1LT8WrnjjkeQ3teM1b89K4bOGX7mZchkjM9boOvZA0R15VbxtcBYTwQB4_oCxhATIho3FYQtDy8U_9HD_i0vQHZ2H1OmZjEDryIKqHHCmCJBG8N96k6F8uwGlArH3MnwnotEtcKZJMuq5OZdTzq5qq93JTBN4q4WvG6ypkpsxK2gBM6zM7o2_lBBIy6AehN_h5pHmpFyFbAOBf8Iy5sr9DBmYScR7p1qaUSLzvwwl5cwVjMBvA5mR9uqsGtRjwL4ccNLIwmyrxeMfqXmNa_kV6vgXJBzpVeUyHEOOV5Z5o1USnlEJAsbz9c3MXa7g-Ks5FnJTbHlwqNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laLXZx7LFHi88AG1QpNHrRz5RGkhd5Y3NAfiuzjYe2UOLf6f2ckyGMU-ELG-J1EzXHrdyI_YqBrNzRkWDpNRWG9KZc18_hujo5XXpVeb7fgOMSwuSGGqOpHAHTdjCAI-9sX7syGWdlFTxgIYpziCA1yjHC1wnEUOPHU8q9p6bPQREa7_rWoEKQZUEAE1fDFQzrIpxssZeaJDkjSt6w3zUwOFt5wuDuamT7RZcKPwun6fPj-NBlaLlO-KYB5DX1Rgc_i-Ads_6bpj8PH63YsTkvevTDAGyI77wLeSl3p1FR-L5um_sMjIuhWI6TwkWLDpStp0OK1YWxfsNwXnsrJ6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_prAXxaUFvp_vfwaQDxkDY2JkmWJ3Vvx1fL5xgePx6vrJC27S_WUWuD98zmPCL2qMuh2jpKNgJRD7U62KkHXIo8BMHaif__kOfjAm-esvNfu4Les_yIJbDizTN5Tr3ac1-dGw6h5bvYsKUwmgYUjWKS8ddzguadoRwAK5nFQ5vh59q54ciI_B2QOVe0he_mvwtRAsUzfDdE0ifhBZafFb0MiuUp2BDYHNQibmIkTISMLw9Fh-OPfzWuv4tLd2FNSmc97ZMxf-gY8H8AZIpSyy4AFDH1VppXoVoAzQKQnx2PZiXRaX7rI3FhS8AJWFT8nWtngXu7_6P82YrGafzZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=NW1sbAQCEM6QS-b_-Aaqgk1NzBU94ttucEzNzVAsvFeyS0UoJ4zZKsJuGU0Yc7w2vdWIK5IU5zXOC3u67r1zW6aHCCOqRipUK-W-biNlTbTdNL0zlLOk6v8KPRfjyC2zZz6UhpjvjVCSUE4axuEy7qh1Bhf533GcMmpmd0QQ03zFiV8cknDqw_zLu1IzrUW2MO_OPXDAaUVY_TOevyjTwLYF-A394rpGW6R3uStf_iaF2F22i2sZs3BJACUdBxPjlbBNQV7SiWhH3XheeaEo8GykVzQWi0disTnxFTD5mYC2QFCL5bBTDbusFZZKV3YpDfJOFuhRhCM5MpUgd7xYTrXvt2Uv0Fe0HqRlrM5jg_Cwo5LsXHgCv9MPEMInFiqXotRCu71E4IRI2pbGLd7ZqIU_LgfH9H3_cpjgf0qctgWb4oYQxNfwlpxrefzIsJOrhYjYzIhMSbk14TfvzqCRPAbMlbDbOmx0e1khfHc_f_ZVvOFEvZJ_NiRBdamiC7n2KHAaFgJ4nnhtwCUHYIHnax1TnUYDgS5Q64fS3T1B6U6NgJ4wc6VJcgJ3h6Ld5AlOKEUEz2ZUA5eWe1ZnlTb0tXmBxR_sV4chPb_UdYM0b0gNczVfE7Ra-Pbv0ZUVUimue2iyMHdhMkESZP_pqCwtiyLSv1_erxOdAJE4FACjvKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=NW1sbAQCEM6QS-b_-Aaqgk1NzBU94ttucEzNzVAsvFeyS0UoJ4zZKsJuGU0Yc7w2vdWIK5IU5zXOC3u67r1zW6aHCCOqRipUK-W-biNlTbTdNL0zlLOk6v8KPRfjyC2zZz6UhpjvjVCSUE4axuEy7qh1Bhf533GcMmpmd0QQ03zFiV8cknDqw_zLu1IzrUW2MO_OPXDAaUVY_TOevyjTwLYF-A394rpGW6R3uStf_iaF2F22i2sZs3BJACUdBxPjlbBNQV7SiWhH3XheeaEo8GykVzQWi0disTnxFTD5mYC2QFCL5bBTDbusFZZKV3YpDfJOFuhRhCM5MpUgd7xYTrXvt2Uv0Fe0HqRlrM5jg_Cwo5LsXHgCv9MPEMInFiqXotRCu71E4IRI2pbGLd7ZqIU_LgfH9H3_cpjgf0qctgWb4oYQxNfwlpxrefzIsJOrhYjYzIhMSbk14TfvzqCRPAbMlbDbOmx0e1khfHc_f_ZVvOFEvZJ_NiRBdamiC7n2KHAaFgJ4nnhtwCUHYIHnax1TnUYDgS5Q64fS3T1B6U6NgJ4wc6VJcgJ3h6Ld5AlOKEUEz2ZUA5eWe1ZnlTb0tXmBxR_sV4chPb_UdYM0b0gNczVfE7Ra-Pbv0ZUVUimue2iyMHdhMkESZP_pqCwtiyLSv1_erxOdAJE4FACjvKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMCIAOIwjSlEwIcSTR9cUwX3yrraj1nx4kCpFFDDNouv9x-UAKUEUJMoUay8rH861zuipV-VAPBFJaaR6nEB3-Vri06iYNS45yRNafvjrilY3A40UckyjHcZ-wRM6LpcIWtYE9bnb8rKKPehSAcCsmSZXSMR2olvMmMPmj9ljYgCoxqRvXC8fm4hD1xa6e4L3fi9HyqLCrRCGxVYKZ67fKm4PfhFRcu3c6XAAqP5pGR9z_XwtrwSC2Nz3JClzz1gNHh3SNyTYsaKRIAfPJfVUFsQMvavJWnJM5b3wDGv_Q99CpyLxOwTn-Qh7mGj-kAvd05qoYygigdM_t8u1EVuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q40rjXnpjGp9Fp-nlI__MiLslNyT-NWVdzfqzmAumQI-jk--uW18uaibKEgUidLAskJfMrhG4I3fXlZw-XYqbUNe5U6hyWBIK3d7s2x7xVxOmabA2ZRCH3BhEVVGQMhMvRWqGyivp1Aj_ljF6MlV8Focwcj9nL0KBwgRPGl-kcPg8V1iEdIcKLjgH_5WOLP672MqnQ-GGCMePSsw8MojUTrsOmlcNruEvxn0ajEmIlrBkyEnPXCu3ELxC5MmwlPp9h8QbvqDc5Kl47Td6bo7lByC-Nct7E751uTyD_TBI3yDpX8ap1UEppBCRsnmtF2oqFmfQOvMhF95RY8wHZ09-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtbvtrZB7Ccfng4cqt6m7RyL85m-yMrMvL6-sVcEByf1SbcB6E6w4KjHfQjyHvXgncRo3wQlhmMZinD7kC8Kh35ik3kI79CXQo1SHWnGlS6px6vzOubqqrKsd5mJE_2i6_mAUP65dm9hWcxNftGGldSXGVMVFiaKe8w5dss-BJB3tHSkTr9_n9m8PcTt2hpn0RQsNjkK0bbKW0BQfQL-cZoBDAHoO3K1q0eW0ddMgGR8wResuZzR39eCRogT2g-zbiAxf5gyupp6tB0bdP4qUnwz8YCSFIvjb-TXRF0KQBdUMe3OfMuu_0uYKlsX-ADouzKZzIPY-idrDUDRBtYe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlYB62vF33cpfKUSnnZyurPMqmw6RrbtguTODBSPgnfKONMDEiq2btmQShI4lfXMOAozKIe2wTC20njmTK6ntfnqvkJTVtXS8sj7JkVJ1VfRAPPg0M0X7NdzAR4-QVUjddgD0ADadzDNCLH_AAkhOIbLMkZSYXPoN98me8PuORUThFtrz53uYUd4N7inaWHEeKTFx7wiTdTiUrVOMorJQBnHVgWt2OMcDgackpP5yI-Eu7R8zPbiELOUeN1-dUq7o68EgKRXoVbdIw3BiDFc4kAL_ft1zQ9y4v5AnFn819w-D9crBfkYy9i0d_PRYVbzy8jVujAsiAWgdCTQPPn_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 13</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 13
دوشنبه 27 جولای 2026</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnhgz25oMlxgJnqa4uDU434CyxPSFzFChz7o3IUqXPwvYgnSkZbWWiNKgu7LUs7ZU_uiSj1zhpCg6wMki878IKKLdkteFm0b1u3LI-nuEFz_ZWJ5rLLvYjZ6NEaDYuG2NRMn_lLpstJCxtoGJJz5Amej6vRMBumc7ciEw0QNa-waZnnHyPRWfzmYwA1PuZdrjv_Oq1IjP9LrZrfH1gsyv_JqY1cALbeOOXkek-YhLzDcOK1cN7B7oRP77Pp_-nFKBaJCJ5qjElWkQPv_nMuPxnRrA3VisIM_85_bZmBYfzqXcmlQDK22RznJCKh-51koVIWJE3WOAQbMOSBmyY0Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0pUtFcQ5PCRRdRtLdObw5x9SXqFY2S8LlTkNo1Wb5ecTXj13LlIZvdzzKBZR_db48NkOvH4dKXtIGnhrWnh3pxzofTUoPDGeAI4tmXgsOPmPelYHNZYBshvxRay3CEAuPeCQl6lTtmOCoVlMWMMKocQsfsYnuU6oU1fwogT_4hNFO9mJS2WIMcE0OUms0vZLxqv_XZC8JP-KbsX_XsmrNlQ_dylR3rGSWCek6J2xGLdW6plcLxqd5qCD3NEkR8FhndAvIx0ab1YbtiEcNtBExj3Kru6xvevdPS-AOjGMGMcsdqcA3jwLIMDuPvpLAy4O0UnMwnyPuxpZWGgp6vnNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VkxHr-D4gpUqC0GbgMjCN1n5B5o5qPFIetJIOsMnPKoIDnaf0rMUcsdQ3I0nIJopsE2rl9PKpu1RZX8cawyh0hTI4mHMwtjAnXabRYcFkD3Lc7yz2KBpKgJ1RUx7Owv9i2qVNRXyzaT9c-QRcFRE5iXfuz61_tRHoBzed7rszDuVzFa80yWGzZ3NmnASdYBhMgei9idO-QtvUTBY3eahc54EVGXPOCvOWYKuUD_scvyqdfMhR8M9UJvCIhjlVLhBrybGJYYUT0as3ytAC07RVqKXBMbmn4z3_2j6Bf9XP8wEo8LSFvrsBxqttM2cMu1dIAGkPAtI7JTV3wglqAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها و اخلال در مسیر جایگزین صادرات نفت عربستان
با ادامه تنش‌ها در تنگه هرمز و دریای سرخ، عربستان سعودی برای صادرات نفت خود بیش از گذشته به مسیر دریای سرخ و کانال سوئز وابسته شده است. ریاض از زمان آغاز جنگ با ایران، با استفاده از خط لوله شرق–غرب، بخش عمده نفت خود را به پایانه‌های دریای سرخ منتقل کرده و صادرات از این مسیر را از حدود
۷۰۰ هزار بشکه
به
۴.۹ میلیون بشکه در روز
افزایش داده است؛ رقمی معادل نزدیک به
۵ درصد عرضه جهانی نفت
. از این مقدار، حدود
۳.۵ میلیون بشکه در روز
از تنگه باب‌المندب، عمدتاً به مقصد آسیا، عبور می‌کند.
اما حملات اخیر حوثی‌ها به کشتی‌های سعودی، این مسیر جایگزین را نیز با خطر مواجه کرده است. در نتیجه، بخشی از نفت عربستان ناچار است از
کانال سوئز
یا حتی با دور زدن
دماغه امید نیک
در جنوب آفریقا به بازارهای آسیایی برسد؛ مسیری که
۲۰ تا ۳۰ روز
به زمان حمل‌ونقل می‌افزاید و هزینه‌های حمل و بیمه را به‌طور قابل توجهی افزایش می‌دهد.
در سه هفته نخست ژوئیه، حجم عبور نفت از کانال سوئز به بالاترین سطح خود در
دو سال و نیم گذشته
رسید و انتقال نفت از طریق خط لوله
سومد
مصر نیز نسبت به ماه قبل
۵۰ درصد
افزایش یافت. با این حال، محدودیت عمق کانال سوئز باعث می‌شود نفتکش‌های غول‌پیکر نتوانند با بار کامل از آن عبور کنند و ناچار به تخلیه بخشی از محموله و انتقال آن از طریق خط لوله سومد یا استفاده از نفتکش‌های کوچک‌تر شوند.
در همین حال، ایران پیش‌تر هشدار داده بود که در صورت تشدید اقدامات آمریکا، ممکن است
باب‌المندب و دریای سرخ
را نیز هدف قرار دهد. به همین دلیل، تحلیلگران هشدار می‌دهند که با محدودتر شدن مسیرهای صادرات نفت، توان بازار جهانی برای مقابله با هرگونه شوک جدید عرضه کاهش یافته است. در شرایطی که قیمت نفت برنت به حدود
۹۷ دلار
رسیده و برای مدتی از
۱۰۰ دلار
نیز عبور کرده بود،
گلدمن ساکس
احتمال افزایش قیمت تا
۱۲۰ دلار
را مطرح کرده است.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr1eso56k74rx6Rz9K5qTOO8CQyUBbPN0NZuwDsAieV7Srg7GgiT50DbXU-zfAkN-ed3qAivVskY6As_wTmHSZGXl4CWwB1LOK-LNgPmhl5T-wdDubpPxuAVgR499Qj0kiSktR62jEc3JKqvS5oZqMP6oZiD9bOS61EVbQQm6i4M-b-RIkCFCO1WAHEGIsiQ_pqTfXT3Mzs0mQzN68nInoj9-p4jIszfcCnP4DC4TGlmBbMSfAFenGQJhK8rQvF4H0pD9INt3jeopemLX2yrDErNxEvKCPyTqTqJnFNPPR7nFa6NI1LNYrGsUv0GcRiJKQ8Df0bpjTPfnZ37vYeymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXOWd3tOvQXJPW9w52LVsusGZOpssPCatnxW2r7N-E5kqcK_dLoHrKfUXi1VCiJq4bYsvHLCWpqdDrk59S9ae_1RNek7cKNhgbQgZSLksh6DhgpKvADcoSevrQooRHQLrMXjEuWsxLZJWnPSTrmelL8tmNO7gBKjjPqkAChZC8x-sd6hr3hmojPi9vpk2oWSC4CO3aTf1oLY1KpeoCwODPQUQbGrQ-1-tCXeBuGVxlN9WvxML37qnhqnBr8oC4PujXQgDz8gMQuulKVJ-0HkCj4K2ZiOOVOo-w-kWrjBS7H0XR2BMCL4fB-M81tiTC5XvYtEABF7hrmm7VI7HYmDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmiys6j_6rKtNbJeC7R2ePeKHNEsR-_0ACpByHonaXI4IvJfnhwnnJb-W-WaOLU2EM4-CtWLMNvXR-jkyPaKCFZUgFIVMZdMvdDf0_uNednU8wE_aiyXL5OzblcVJ13kySty6DA_9YAwTNKjQVej0mxWRDjWh9PIQb-jVQz1AIB6yMj3TSXriygKdjc41WU0GgPCtd0G-Vuq2XmnESO_kG_Qt4GsJtf5sS4W9uHn7EBYpxy80Pa84dmCVHdfuVtJyZLOVopt412wHtYdp_1D2E1ZzICuxVd5OHpKGMstI1keLBBkTXzKslTRGH5HF-GgUd2YtCLSAzC0lsYygt7S6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR87FhiDcFMln0smcylR9YsC2tb_G_ju-O1F6ozE5awM1ZAgFileFzTcOTv0_8MQx3DZt__btLluC22dS4hUCB3FBjtIXTcgkfKvFlowY2Z6Q_iaeCpawxfWwLcCSejxkKAHTdo74d0oW5_ojn4lJ3EAxBRuwS-Y-sb4vV0kp7nw1uHafFG-opNq-DOVTNZT6u6TZKWSmVrinb1j-6HqA-jaNCgNWd3rJH73R6677uK1an2NL04vokqqp725L6EmKQssly11WhpYe-lcEKM8BN-_PmAd_24L8mX_GAfdRGR7xRR3-gbQY28jZfY26wzjkVrFrV-CWwRTf7Q9c-owkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-uNLXbogsSj1T46ggJXIFFn_BNzFaOf75TB755o39RAE9-LNoRxrXz-FlRj_AIgnfSkdZJdOl6mPrJG9CsPyH1DUHgtQd83Irc5Yz_BSF9_hi7G3yOm8TXKK7zLUzr9nbJcZNF-TpdIuv5DuAyG3lF-ExjpIoqdDW85eDEHaqvC6piMheBkwzuCp6F-8UDxw5RaHfvY5XEqTMVsX_g61sij3GrdcZflQ1YRjOW4w1PBErRirp8kncpjsb1nb9G0QVsTxDwm69z0MBeAHhgRlf9aB_LeMwbTIL3-KPRr6sdlrAbGft9eq3woOXEUkdzY_8jWwYoaWkQ-aso0bSlaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsQ2r6miQvDzXPn8fRXg98ulzReWVCQdJKOM9Iowx41Yh_WLCa3M1pXuy7NlGCaKmdCUICCaMgox0n1RclkeW2PPIorsV97uOiiv2A62twHa3WMJJO7ejtbi7ag-7-MD1_fkYPoUtiS60B04-Hjx2hr_nMVYlC4czgQJGDj53WQmlLLOe6khSD_XnT21xJ7XQb_AxzRjpbs_5bhv9sV7zQW2DNX9PVWshBZj5fQZLpjDJ4yPZuSCZSavCk_Vv5c0a2T1j2xB3jAbp0yBpSn0mrWpAQw_LYphxlIQDn6hRUD89FgPO99zUJEF28BomgKDACbWuS-XhU56GRCdggogdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKupfoQZJdS_r12cyPPfXKCIbR3giy-kBe1ADICmqW_99eC7cZScnBx4ZR5gIUn6joCpXyt7eeHLxdOulELz1c6kvY_BcC1My16hRaR_huSbTY5Ys2zOJ2EXM3g_CzaZN8lKrHRUe84suIJBtbyZATOJJmOVGeuHp3Ji1QT5I-KchOZH4zS4FpQ8hllCUFLzSItwl5_Xb_3_tDqilqfsyY5Kt-7XjUSUoilyqEcKNoIQTu85rzvVzPZHqu_WOfGWP8X6eY1rTJf9xCCwMjVMYv_s294-ALw6zpkZ6nIte_tir29ii_k26Loj9RC3eB9TvAxy65q6fyhwqbvfMcUrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vku1ywgAwj0vNIag90MjjBD1iuKVRNZup02nrN4NPSrlAWbY0SS-MxntewdWCkiOAPDZf-dhFlDbMU0libpo5v0Ar00dd4xIKpk5UWXgDcwx4V01n_kwFCSUu0STi2Qmo0ML3Ro4Fmw4v-hbVoONZt8aaOvKteK9KBzmi3_7WriYsxVHc6qV4HNpYKSCaluNVO3OV5bFy3Vk0QocA8qmr9FV0glOh2yVGmOffl1sFklvUkytmhX9y_yAvz0hswIZMuft6Rf969_Z4Jye9VzC3y9sD_RjWv7guBJjRxIkPHeFmKTv9IzVodttigXX6bDY86FS-9dbqmRw68BKmTrhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_6Q2rmMNtzfVfQF0q4Tuwqm8fhRyWJ7JVafVVOXfP3Lz8iLZrZXfFPk6EE_gsYPgGlc6YUKGafkdZ_qZrHS2mVYYSGwuePj1JJsZnL0gUkK6dQm6UcfwtdKjrVcx4VmEOvsToDsxSRRlFBBj69W9d1jJq68C4FD-f4eiu0QYA8iauYi6MF96BLqRnRCHwEY9DtEMYfDLLqnXciDOqnMlfAZBREF54SKtmFwrqOB6RSgOhVkFP7NZddzCFdZmRgTaQ3RdU1SOoFuiRLa9sWecmgrhJ5SUhjU9DQZ9YPYLlC1vVg3Kr4IKnWhAqTWJ-NMZCDta6KdxacUQkONlMv9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onWauxOI7YLcrIyMzYSUHHtRH4Tec-RaMkHAybJ69jLtw0srwPLeTSUI35uJEAVI4L8eBpp2sxxWVmlGYC8hTajHkCW2Ib-a_S3lXNlvYcjExe-x5huEewNXKDsor8VOnlURzH8LLQ8KcoyIpw3-PDAVAopdVgnZ7BIjxISriNw279044daXT0XQabR9bfKcjCOPG4MW7M2eacLNJLh9G4vYY9tGLzbQ9Lvw3VePZbrR1UM6hWssRu_FMscvQ2noOtMstIzjMytJqeQ2zPm5GgkcpZ_xAFAN0lPzdXN5LL09fb0QS4OStxm12o9hfyF409vSExjXJxpv1C6RrL_YDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
