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
<img src="https://cdn4.telesco.pe/file/f3VMPlIyDI8GrdF3Rvwk9HGa5EhoFl6HI6QF07wJIC3kj3Af7oHmQDFma6-5L6wXA_a_8FlRSzoARvgz7SVcKJXMFWwQUUUEbvh5cSyLfZW8QVJeRxKMcMEVd0oBxbmOu7zIir0GzofuXfmZdm46B3QHWmOiJV7ZyXOMTp9VYOAmJg6MkH4eqFcm0Q3XqliHbM_FGx0y2OlnlIKSYAV2-L1K3viuWesKc8rB5jKXjz-e4RfbslVlznrjhoeV3doxXJwH-BjX4EbKZH7oPtrbQdS4M-LtDgLar8ysQnvEOZfcoT0rLsrkzrEwRjBGeit8vld_rweloPr488nO6DQbiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-436612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae2b25b77.mp4?token=N8NdF7zyB5XKxIeMaj7JFW5ZzAIv6SEGgvdmuh439qg0I3ni3WzY2cGkVUHymum5hXVWd_BTMAQpZXDow-ix0Uo14uaefhfdAZbkJBL6-O14e8g-TnYfjmKGpik2W1qk6gP1_Rf2eK46EQxrXr48l1qF2W0Dxfz87cPVCtsNCq0k5QUn8adHU65Yw7DR8hSgiLV3S5cDgxc-_rwbgbUo05_SrsJfCkz93c8D0vZAEZcLnHEKXECDYg2KTYIC5_mj4T47uaSJ0rGMUusyvGwxgLajqftugxCybsmvZINxRI03J2-P6Ms4lO5auIJ5fxU1nK73W_sefbFCIF9594-C8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae2b25b77.mp4?token=N8NdF7zyB5XKxIeMaj7JFW5ZzAIv6SEGgvdmuh439qg0I3ni3WzY2cGkVUHymum5hXVWd_BTMAQpZXDow-ix0Uo14uaefhfdAZbkJBL6-O14e8g-TnYfjmKGpik2W1qk6gP1_Rf2eK46EQxrXr48l1qF2W0Dxfz87cPVCtsNCq0k5QUn8adHU65Yw7DR8hSgiLV3S5cDgxc-_rwbgbUo05_SrsJfCkz93c8D0vZAEZcLnHEKXECDYg2KTYIC5_mj4T47uaSJ0rGMUusyvGwxgLajqftugxCybsmvZINxRI03J2-P6Ms4lO5auIJ5fxU1nK73W_sefbFCIF9594-C8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به یک بولدوزر رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 299 · <a href="https://t.me/farsna/436612" target="_blank">📅 14:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
آرون مکلین، تحلیلگر آمریکایی: ترامپ در یک چرخهٔ باطل قرار گرفته است
🔹
ترامپ اساساً پشت‌سرهم تهدید کرده که اگر ایران تنگه هرمز را باز نکند و از دیدگاه او در مذاکرات منطقی رفتار نکند، اتفاقات وحشتناکی رخ خواهد داد اما اکنون چند هفته از آن روند می‌گذرد و به…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/farsna/436611" target="_blank">📅 14:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKtreC3R3IsWI96RusdUhFjCgXWUxyN6AxF5vEsFWFzBCCTtd6aBy0n5mWJNH5KZF_au34Tvk8JwGmAP8gXgIAfinBwGJKlbpJ1BwukphXRN986wFnmPkvrkkecu7f1LNLH2_YZzLb9BJwYydnIOiKsDhbzA_savojHYtXFSXnxeSHTliGLiEqYzSDgLwH2lWs5MD07Q0EjzTSU6GSqlVYDJNTQyuLNNPJdAujMUVLaRrdVTHJeEzIqP5bbi3pFrX-W3XzhwM1Md7ZEnur51NI4SDg2Qb3HeJ6THKMrQmC34ej3VTs8960x3sCWfO5DmprSooi8PuwuR1drtLwLvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TedO2IRSXdAKysk4l7oBmZ0mMbWddjglLXgTGaNgz4SQQriuLMtt6nmaeyl-V2wE5VkGiGv9wj9VXMvtoYd0ORs82TNQ9XX7t82uFBbzFhZRXQDHol7o4KQyWuFU57Xvg-ti_l_UoD_bROnBAzWRmRwJ3SpebTqxX9SxWCP40uOgSKB9YMFWZ_bMDjj-VyId972pl_tGwSp2cFwW7PsZLl6A1hYX49MXgYLReQfhTRtSacr-pTHQLllMSWmYrGbaFEb4q68C7cNX8L6gSNepHd3TMoM9zAcyOjIdeEQ7uiFWPHk-cgV2Vpm4MRjSTEIw6-EhWgqmfXjfWhc4L344Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_P6Qd3YKf-7vnoCgxJtaW-zsl3pUoGwjJQ8oDui6kUVA9GnSaRJtzY5-01tpx7RyG_8l7dU2DJngDqnc7sApJmU6c0uwUPOxG-CMQAEVq9ygrKJInQsYrkPfSgCGp5081gZB6NIXRGf1Fn_7eYcAJPcqZSIfB5UnPjOZ23EQiuBgPrO_93XI8f_6Fm9ZkUWRp9TvsZr1atMTnFUIw5JMD6cCPXQNXGtz7n0sIe6fzjdJH21k4JipVOzvqbKqZDTyP3zIOuLsm3zphZ-7V8wbQN2N7Bszs0KA_4Zxm8qRG6IjnnbspzlCU1dCRv98b0VP1YjdpdXIFX3DTSBgEdk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XE-bYXYvORDMBZjJYN2mytWibp4ED-Gws2A53-4ouKb7tz9AG1C9NrC3wwRSYnjiqk_5_-0t0fZXzJietJcf9dQHwPLTUk4lZ36D0ABh7u1MFJ7znlY6_nATHatFCYDbm976C4RAGzTSe9NEALXHMRT2zjz-YJYz32pFv0ZJVHbZ2Y3-zxLFBF-MsG1i1CrXMERcvhePpmvAKr9lW_RJLmONaIfDrsT5OWYKSPXfCx8BqsKE5gzNElIlYT2iD78_wJfESRYjMKSSehpV-IwRufYlYM2LBe7o1tj1f7AdMaJpufhSdkdgLbwhTYXp9W0xvKL-4q7Cx3AM-RHWahiS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpJlgAnVYYzXGTH5WuOhGPd8r1KX03YqMmxZ5nYaxzj9_tZG1hLlqHTP17nBHH4hp2j8jdzLV_Gi1MiF2tNSFQgtfCZ3jGljIVYtGXAUrA4soEDCLQxg8hQCdI4t7LsZwBmCieceZJDHDj3uz73poIUpXhi52EKyZVG6jgk_0ZFFla7UFEvAvu0ew1vYeGgNYb0rQSOEH0ysSMooNXqvKGPD2NJIauEwLCi4x5dswsYSyXPm3AoeI13ZaTTa7Nm6U1UjIemniPLFDLV9rYkw-YUn-coFu6jmMMph4T-KHpQ9hdOf1uA5TiiRUoxFSQIedchZQuajdexEKBzHJ4CywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcZ0uI1GEpetboQP1lw_xSMoadSMW2u7xROPC5Y84lq0b2_ZYgoOrXcLsgJxE4qr4Es1uDCHvvaCTshgJpBLCZeFxrAbLB4FVQsfefP0q9lWZMvpMHmWsz6Zjtzv_w2YC2BDMyGNzyrvibWi2LjLZZghi5OnWsimYI_UJVJNlIg9oT8Z4xtub3YTech4o20csRjP_648HYJmk1OnquEmbCTXU0aPTEbm64PS9jQ3P8Js1PQzdV6UG-wETuWHoKdw-MUFTHzYJn0e1tHfr3LWV3FwUpWCxbxgE7pm9gK_ApUk6TqO7IIQ4Yq51HSKy1vO57wEZhFJ7f69SH3yVXVL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QasULYP2Nv6I5H2bz2Kfff3oDt-o0SyAzb1PiQoQKcXzOm0UAuakoDOuBmVYH-njedVYIfX68uWyRFX_gl4f-vD5ry6SFJ8oCrMXEZzL5S25xnJtuQyyZo_fQTdLgh0z2BFkLJgsZVnVEnhxes2ukNxmj8RQbjco1v9m8FELxIEUpSHHATcFoW_zYYnZra_CqxbrYL-c2YH-Lzs3AntoB557BoGSSmTyIEaB7GWPmlWz5Ae4sbe1Z91L3WdVGY1HZqN6WEIgY1VfUri7plQ6w-lujEWDW71j6DuAV0pBdMf4Ko-HxBPXLlHJRROVLXPxLhEaHVB7QJrPqujwoohOcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم
گردهمایی
روز ملی بومگردی‌های ایران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/farsna/436604" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی ارتش: دشمنان دوباره حماقت کنند، جبهه‌های جدیدی باز می‌کنیم
🔹
ایران محاصره‌پذیر و قابل شکست نیست. اگر دشمن حماقت کند و مجدداً در دام صهیونیست‌ها گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
🔹
با توجه به اشراف نیرو‌های مسلح به تنگۀ هرمز و غیرقابل بازگشت‌بودن وضعیت تنگه به گذشته، تنها راه دشمن احترام به ملت ایران و رعایت حقوق حَقۀ ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farsna/436603" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-RDKZ8WFy49aFHksox9rtX-Bw6_z7LmY7U5bFNcz-7MduVajLwsdxyuXNCyt90fJw42wYglb2dJM1aK0vQEZCPp2cIKE_JNGMbygRe5-q8EsYWX-iyrlpn8FwL2UZpXQ-k7VIs3K1V37TsAcRGXNUmtQ_7asEIpVRJaU9ppW0O4rIeH-zmpDfQcpuD27UgwlQlq5k4FwpqrfEBIjlPkvOP0HSNwr5-lXyvHPqXgItj0vAm0y8qlMlEQ73PIhjqMKWowZBZs6jfLDyuzKnbltkgqex_Dj7otKKM72alxteOSVcpCSVOY3odJnJTr-geLIPfQgl-EZ3C5-1iOYlcOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اقتدار امروز ایران ریشه در روحیهٔ مقاومت مردم دارد
🔹
پیام رئیس‌جمهور در آیین گرامیداشت شهدای صنعت پتروشیمی: در روزهای دشوار جنگ تحمیلی رمضان، تلاشگران صنعت نفت و پتروشیمی در خط مقدم جهاد اقتصادی از استقلال و اقتدار ایران اسلامی دفاع کردند.
🔹
دشمنان پس از ناکامی در اهداف شوم خود، زیرساخت‌های اقتصادی کشور را هدف قرار دادند؛ اما فرزندان غیور ایران اجازه ندادند چرخهٔ اقتصاد ملی متوقف شود.
🔹
شهدای این صنعت ثابت کردند جهاد، تنها در میدان نبرد معنا نمی‌یابد؛ بلکه ایستادگی در سنگر تولید نیز جلوه‌ای روشن از جهاد مقدس است.
🔹
اقتدار امروز ایران اسلامی ریشه در فرهنگ ایثار، خودباوری و روحیهٔ مقاومت مردمی دارد.
🔹
عبور موفق کشور از شرایط موجود، متکی‌بر انسجام ملی و اعتماد به توان متخصصان و کارگران متعهد ایرانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/436602" target="_blank">📅 13:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=NYemzB3bOSmV15_PfGmKrfLZHMbrBJxe7pdAtLGBDec4g_Nggnmumgpkc3bsj2OC0b4DI0O6wtIdRLQ6EkvCA_vV5J-a_H4ZBlKD3MFEq-sq_n1KkSNpG94OBeTQBY_TLO5gf9jcggaBj9ByegB_AkTgjFLVXPs1N0QLIKr8e6SYgF-CguRUX9rF77Mewms4U_fUB5y68WEag8eCNRvlPvnLTl9WUNV_-GungAhJ0aVJ_XFk6HN3XINxoRSXEGYcRV1-VhgUp2Dt_I33AgFD0-aHIDSCaSjjc9r85HvaRTLv2oUgg7DB6uOrKEYfOBNJ52ANneK9GRPvV6UwmkI3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=NYemzB3bOSmV15_PfGmKrfLZHMbrBJxe7pdAtLGBDec4g_Nggnmumgpkc3bsj2OC0b4DI0O6wtIdRLQ6EkvCA_vV5J-a_H4ZBlKD3MFEq-sq_n1KkSNpG94OBeTQBY_TLO5gf9jcggaBj9ByegB_AkTgjFLVXPs1N0QLIKr8e6SYgF-CguRUX9rF77Mewms4U_fUB5y68WEag8eCNRvlPvnLTl9WUNV_-GungAhJ0aVJ_XFk6HN3XINxoRSXEGYcRV1-VhgUp2Dt_I33AgFD0-aHIDSCaSjjc9r85HvaRTLv2oUgg7DB6uOrKEYfOBNJ52ANneK9GRPvV6UwmkI3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فوریت طرح رایگان‌شدن مترو و بی‌آرتی تهران برای برخی اقشار تصویب شد
🔹
در جلسهٔ امروز شورای شهر تهران طرح رایگان‌شدن مترو و اتوبوس تندرو برای اقشار ویژه بررسی شد که در نهایت یک فوریت این طرح به تصویب رسید.
🔹
براساس این تصمیم، جزئیات اجرایی، نحوهٔ تأمین منابع…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/farsna/436601" target="_blank">📅 13:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKPSz9oGZKbHPEADalwIfubQJ9witUyMxvMKtEZCmxOccHJ6a8gbMpVKGDhQ6otOBSZ48iUMHxnOEYBET8vRqHpuEVKs3Tpb1fMhrGqb5RZB2sCIG4jlxxDbX5cInMqkvUqqV4Z2GF1Bm4wtRpcYGLDyv8tqlU2epPRNbK5KGop2_n2cmTxIDlGBo5zS9KgO6QFTc-qw0i-LRK71G6RGnqiKN-V3q0wocj0hjPZpPCiI357hfK6NDJd_L9SIWlQjRXWcIN7ezMYopf-HVZJH0uJzH_0nxcd6rII1M3tXe9L6lYpFjPwFzhGUMTPvRx5CM6oZa63K_B899yuXpIcMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ آغاز معاملات در بورس زده شد
🔹
۲۸ درصد نمادهای بورسی در محدودۀ مثبت در حال معامله هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/436600" target="_blank">📅 13:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc065a9.mp4?token=vFQHF7P9QxFnRqziB1OLcvL76fCdLMvw_4Yfr2UTxqQyAp3IHk9s-2bM9wYRntBq7z6V-duihW7Zob9XsjrfwKG9Pgslolgpy-A4edUrJHb1A2MN3XE8OZcMyjjx8TMCGtU3uehg0Sq7cl9PvI2rK6eE2c2LKk0emPrwyMUwD6mxVDEcS8vsV9_pjbYKQlfVRA9Ql3lhIQWm87VBRQ-1h9DkxKi8UI1bF2nz8JAu5ICBZsHMSixIVOM-vyTdoeP_MTO0YCy1l3u72lVNRUtBqZosLFROnfnTAXzMUl-GRARBvx-JjzsDvgg0oe3aat4wEAer6IY8SPbLmh0ndhKJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc065a9.mp4?token=vFQHF7P9QxFnRqziB1OLcvL76fCdLMvw_4Yfr2UTxqQyAp3IHk9s-2bM9wYRntBq7z6V-duihW7Zob9XsjrfwKG9Pgslolgpy-A4edUrJHb1A2MN3XE8OZcMyjjx8TMCGtU3uehg0Sq7cl9PvI2rK6eE2c2LKk0emPrwyMUwD6mxVDEcS8vsV9_pjbYKQlfVRA9Ql3lhIQWm87VBRQ-1h9DkxKi8UI1bF2nz8JAu5ICBZsHMSixIVOM-vyTdoeP_MTO0YCy1l3u72lVNRUtBqZosLFROnfnTAXzMUl-GRARBvx-JjzsDvgg0oe3aat4wEAer6IY8SPbLmh0ndhKJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی رهبر شهید مسابقۀ تلویزیونی را می‌بیند و اشکالش را به داور می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/436599" target="_blank">📅 13:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwmab3bx-qLeC-gSXxvUkwNB9fS87AqvtyynR18xCIq9shCizasY3__2QVx41Qi9eVr7Ika-JxfsbYohLLNdf7RH9wJjJWAJXnkdigi6aa0tjFsTl9qV8bay3uLbXB8pBsExqH9k0GjUElPSfFtcgWcPM6jvGissaueqir0LrPyCMTSwby0N6bcNGjDp1QAG9YiYggjI3-qMC4F0dTFGDaMvOF3owUXWuz-3xwspTYCQt3ppP2UqcpsugEcY5FE4kw0sG4GON9-2zrKcUlY3NPl93BmBRGH2YxiR8AM-6VfnKE3xEtDuuFdh7AwZFhStl4jYNIsAb0ahvr5DqiAS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زارعی: خودم را سرباز رهبر انقلاب در عرصه فرهنگ و هنر می‌دانم
🔹
کوروش زارعی در گفت‌وگو با فارس: من همیشه معتقد بودم که هنرمند باید فرزند زمان خودش باشد و نسبت به مسائل پیرامون واکنش نشان دهد.
🔹
پیش از آنکه رهبر معظم انقلاب موضوع بعثت هنرمندان را مطرح کنند، کار بر روی پروژه‌های هنری در حوزه موسیقی و تئاتر را آغاز کردم.
🔹
من همیشه خودم را فرزند حضرت آقا و سرباز ایشان در عرصه فرهنگ و هنر می‌دانستم؛ از همان روزی که ایشان به عنوان رهبری جدید منصوب شدند، اعلام کردم که در رکاب پدر عزیز و بزرگوارشان و در رکاب خودشان و سرباز ایشان در عرصه فرهنگ و هنر هستیم.
@farsnart
_
Link</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/436598" target="_blank">📅 12:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ed86f8ba.mp4?token=n1ArWsrab_O78BZOGRNXE6Ta5a9ZDlmaTlfFTt0fDJ7jI0-HqbwfBE-V3mGqpX8kcmBChKCXOCuXGe-HXc8lWFgqS4yRtxICCYQzNlnPXFqjvF6-yy2T09QKx8Ti0hZsN7e0FGZN-XSVn5fm6WcyPEGuEef0XFBoTBpR9unzoOXtspxoXvI112OZADRLcWNdl4PF-EgMzKvV-ookX7SwU-bZFSR5myPgA-fZ17bX0dVXXuzQY3osdm75zliE7M5kjROFjS5ZQTWep2MG-9LPIzBDXLOAEMCMCzoal7IRJJ-e87wKpdDlvh07qXzmxQLIakvIJCsFUuLskow62KFRQCiL8BVU0ypCZ8xC8h3MHYRnEPAwOPcm0ixGDjc65W_Lr_tyOOZUlkjktJnTPxIOI9zSfdvcFxMfqcEOlkg-tEkMq_CN9wuxYGDmyzIg1auq-Py-OHE0Q0l0pxmd6vkvqOkZffgbRgTkBQBcCIKe3nQ966aYO0Vzr__1b85gh47UDmDTA87CXtDRR-z4ij0t4qLOOIo_ehU3_EMi1ahzZehYKQY0iWf9hwanjqCUzbJxjGMRpPjUcWnhMZ8layc7edzphdmT99j196dyqBdQwyjaIruxk0wE1rZKWTvVGRmYiDuAQR9o3qn4_WbEfuSEAWmdWaZ_m0xHpwoR4hVhLZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ed86f8ba.mp4?token=n1ArWsrab_O78BZOGRNXE6Ta5a9ZDlmaTlfFTt0fDJ7jI0-HqbwfBE-V3mGqpX8kcmBChKCXOCuXGe-HXc8lWFgqS4yRtxICCYQzNlnPXFqjvF6-yy2T09QKx8Ti0hZsN7e0FGZN-XSVn5fm6WcyPEGuEef0XFBoTBpR9unzoOXtspxoXvI112OZADRLcWNdl4PF-EgMzKvV-ookX7SwU-bZFSR5myPgA-fZ17bX0dVXXuzQY3osdm75zliE7M5kjROFjS5ZQTWep2MG-9LPIzBDXLOAEMCMCzoal7IRJJ-e87wKpdDlvh07qXzmxQLIakvIJCsFUuLskow62KFRQCiL8BVU0ypCZ8xC8h3MHYRnEPAwOPcm0ixGDjc65W_Lr_tyOOZUlkjktJnTPxIOI9zSfdvcFxMfqcEOlkg-tEkMq_CN9wuxYGDmyzIg1auq-Py-OHE0Q0l0pxmd6vkvqOkZffgbRgTkBQBcCIKe3nQ966aYO0Vzr__1b85gh47UDmDTA87CXtDRR-z4ij0t4qLOOIo_ehU3_EMi1ahzZehYKQY0iWf9hwanjqCUzbJxjGMRpPjUcWnhMZ8layc7edzphdmT99j196dyqBdQwyjaIruxk0wE1rZKWTvVGRmYiDuAQR9o3qn4_WbEfuSEAWmdWaZ_m0xHpwoR4hVhLZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: ترامپ در حال نابودکردن خانواده‌های آمریکایی است
🔹
کریس مورفی با حضور در پمپ‌بنزین‌های آمریکا از عملکرد ترامپ در به‌راه‌انداختن جنگ ایران انتقاد کرد و گفت: این هزینه‌ها در حال نابودکردن خانواده‌های آمریکایی است. قیمت بنزین به ۵ تا ۶ دلار در هر گالن رسیده و این اعداد همچنان در حال بالارفتن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/436597" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl1_v4kobjWJAwyqazWB2KU22Z79N3-lP5NXTWMa9K6QWGK-QTt01EnZ4rbwayi1bGRzutCCXh8bp7dK0gnTdZGlyNHdBjKEA3ZOstExbDp-13eo3pX_vDhqHwpc0dZUllQ-zFLCLh6cLPPaTjdR1Jgrsq7SoGx7_g5r194dRL2Zn9G6VXmOhKMVkD5DNbP2IlO9tP1g3aEq_R7qoCjhCRXYi_EHI_9AvGOJPK9HrXmmpMY8epXj5vGt9RqgsuU5AsguzGGMKxuimAYovzQ94dbf4xO1awEBcaIwKWGF4oleaFK7akxNAeKtJD2N20vtEfgbr4BkbChrDckD9xnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت رزمندهٔ بروجنی در مأموریت خنثی‌سازی بمب‌های عمل‌نکرده
🔹
شهید حمید خانی پاسدار بازنشستهٔ بروجن، در مأموریت خنثی‌سازی بمب‌های عمل‌نکردهٔ دشمن صهیونیستی-آمریکایی در تهران به درجهٔ رفیع شهادت نائل شد.
🔹
مراسم وداع با پیکر مطهر شهید امروز از ساعت ۲۰ تا ۲۰:۳۰ در شهر نقنه و پس از آن ساعت ۲۱ شب مراسم شب وداع در روضةالشهدای بروجن برپا خواهد شد.
🔹
مراسم تشییع و خاکسپاری این شهید عزیز نیز فردا ساعت ۱۶:۳۰ از حسینیهٔ ثارالله سپاه بروجن به‌سمت روضةالشهدا برگزار می‌شود.
🔹
همچنین مراسم ترحیم شهید خانی فردا شب هم‌زمان با آیین بزرگداشت سالگرد شهادت آیت‌الله سیدابراهیم رئیسی در بروجن برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/436596" target="_blank">📅 12:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بازگشایی مرز ایران-آذربایجان برای واردات خودرو
🔹
براساس جدیدترین تصمیم هیئت وزیران، گمرک منطقهٔ آزاد اردبیل-بیله‌سوار در شمال‌غرب کشور به جمع گمرکات مجاز ترخیص خودرو اضافه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/436595" target="_blank">📅 12:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463189fa48.mp4?token=DKKiGsRwuju5iaSQySMzehe8Yo6KhPM6cNOJskc6eeRDcE2vADOZpxW_56pJtGf0OEg2m5f5k-0WbkjtxPKABpPyBySYBJv8bNeF8ccjtRQEzPZwukPIGrXVqqcEVnXHkFNBVUeQQQvI6O8WR4q-_Ydv69gRLOg_Aq7Gv1lfEh6TyMyNPHveUtc7Ce6GjsZ-_YC58rBkXNLrnOJlfFRGGU2rU_EOFD1JYxE0hBf3uOBl256hfdqXdimvEDVZ9OSz478QlbpiLPdSx7uBzDbTGTQx1k71gE3zzQSBqGP3_7KbwtEyP7E-whT8S8dAvhGG4ykxNTA2IfSFx3v20yLqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463189fa48.mp4?token=DKKiGsRwuju5iaSQySMzehe8Yo6KhPM6cNOJskc6eeRDcE2vADOZpxW_56pJtGf0OEg2m5f5k-0WbkjtxPKABpPyBySYBJv8bNeF8ccjtRQEzPZwukPIGrXVqqcEVnXHkFNBVUeQQQvI6O8WR4q-_Ydv69gRLOg_Aq7Gv1lfEh6TyMyNPHveUtc7Ce6GjsZ-_YC58rBkXNLrnOJlfFRGGU2rU_EOFD1JYxE0hBf3uOBl256hfdqXdimvEDVZ9OSz478QlbpiLPdSx7uBzDbTGTQx1k71gE3zzQSBqGP3_7KbwtEyP7E-whT8S8dAvhGG4ykxNTA2IfSFx3v20yLqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۴ هسته تروریست‌های تکفیری در جنوب‌شرق ایران
🔹
وزارت اطلاعات: سربازان گمنام امام زمان(عج) در سیستان‌وبلوچستان موفق شدند ۱۹ تروریست عضو ۴ هسته تروریست‌های تکفیری را که تحت هدایت مستقیم دشمن آمریکایی-صهیونی بودند را پیش از انجام هرگونه اقدام شناسایی و بازداشت کنند.
🔹
از محل اختفای مزدوران یک دوشکا، ۲ آرپی‌جی ۷ به‌همراه ۷ موشک مربوطه، یک سلاح آمریکایی‌ ام۴، ۵ کلاشینکوف، ۶ کلت کمری، ۲ دوربین نظامی و حجم زیادی مهمات کشف شد.
🔹
بیشتر مزدوران بازداشت‌شده از اتباع بیگانه بودند که پس از جذب و عضویت در گروهک‌های تروریستی تکفیری و گذراندن آموزش‌های نظامی، وارد کشور شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436594" target="_blank">📅 12:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSATHZMEiMAfdnWqYn1ABg9Mk_pAsqa_K18Mf8nV7syJgzfwW8YVM75aZBdVls83Nd4aiqgUE4m5ClAtjz9IhRW3TGuR35mYuxxOpW9cFqMYGtzn4bbUQ5y5MYJBlmAYIUf47-Y3cLdG4si1BSd-tZKlR3Et0jwKUdenKEXndUXBjpeZK6o4JnppIuCFYJyJ2hbnq1n85Rl5Q0Vx8unp22qeKfiVpUfdvwmcjp0CmSvwt5s-RibYfJiN4Tm6QoW8m_m73gkAh7Ch7qH6Ab41X_VyStktqlNMO6Oha4-49-L33uwmV4ty3-JMS5x8w3rjqPSQRvMYG0yXgvv-3oHCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قیمت تخم‌مرغ کاهشی شد
🔹
رئیس سازمان جهاد کشاورزی آذربایجان‌غربی: واردات تخم‌مرغ شروع شده و امروز ۳۰۰۰ کارتن از ترکیه وارد کشور شد.
🔹
در روزهای گذشته قیمت تخم‌مرغ به شانه‌ای ۶۰۰ هزار رسیده بود و الان در محدودۀ ۵۰۰ هزار تومان و حتی پایین‌تر است.
🔹
هرچه به…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/436593" target="_blank">📅 12:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436592">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiO_k9tuyWWpcadfICnCAF2emKWWMxXq1Cyiyt9nw8XUDGiffMklDtEFQ_uQ9g6apUl1SRl7_x7-1YIWGHnzMuPJVf-lSIRcQCAmXj6XE6Ud53SZUZDuccbSveFlRgSV_i98b5GIsZdtCyVV8uJGwzJh2tuawX6Y21n2qRISnZgHRwxDWlGAGk-gT40gbZEMIzHIG1ldq09e8I-XfXdNV0FqqdBWtSnMXiaUhBWCk71abT04Nil2ioM8BnU5ojrbZGsW4jccQ24jtxi2gf-jGRkYzMn94XG9DgDqGZaG43kTufOTOMN5GyJ1LgodMGoLL1tk2gfeiQD9GdKNoeiVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از ۱۰۰ روایت ناگفته از دولت شهید رئیسی
🔹
آیین رونمایی از کتاب «خسته نیستم» به‌قلم مهدی مجاهد که روایتگر ۳ سال دوران ریاست‌جمهوری شهید سیدابراهیم رئیسی است، فردا ساعت ۱۶ در باغ کتاب تهران برگزار می‌شود.
🔹
این کتاب شامل ۱۰۰ روایت مستند از تصمیم‌گیری‌ها، سفرها و لحظات کمتر دیده‌شدهٔ دولت سیزدهم است و بخش‌هایی از زندگی شخصی و سبک مدیریتی شهید رئیسی را به‌تصویر می‌کشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/436592" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436591">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ مترو و اتوبوس در تهران همچنان رایگان می‌ماند
🔹
صادقی، عضو شورای‌شهر تهران: تا زمان طی‌شدن مراحل بررسی و تصویب نهایی، روند رایگان‌بودن استفاده از مترو و اتوبوس همانند گذشته ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/436591" target="_blank">📅 11:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436590">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBz6ak5uYsRxT5E8nxoRZOqxdBtkriI1fdFWQTjIuV8EzVUrMJEAVjOmMikAW_cPlhaZzNemThj7L3T-_Hv9t6AvzWAHKWLXu6Hjt_hjt8Cz6iLkCCFM5CievP4lMdEc47otyGXJHsH4flWvJS0p3WoYNnKgQwC8lZnSkTB1uGmkz5OgYcZgn6Q33f7MVy9te09s2jXJwMeuOk0wW0ivhQ7vLhvp0AiSnNoGCadgTUPpv4tJJhcR9oROHfM9Kw19Yx5tiLhG7aAzifT7POllWAvMYlgmq3ITBqe0TkZpNAW1EEj4Hhtw7kN2RYH_R_juYRg2PSAVEZURig8zCWWW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه جنگ برای آمریکا از ۸۵ میلیارد هم عبور کرد
🔹
دونالد ترامپ بر خلاف ادعاهای انتخاباتی خود، نه تنها وضع مردم آمریکا را بهتر نکرده بلکه با به راه انداختن جنگ ایران، بیش از ۸۵ میلیارد دلار از محل مالیات این مردم را نیز صرف یک «جنگ انتخابی» کرده است.
🔹
سایت «Iran War Cost Tracker» پس از ۸۰ روز، هزینه جنگ ایران و حضور گسترده تجهیزات و نیروهای آمریکایی در منطقه را  بالغ بر ۸۵ میلیارد و ۳۹۶ میلیون دلار برآورد کرده است.
🔸
این در حالی است که پیش‌تر جوئل هرست، یکی از مسئولان مالی پنتاگون در ۲۲ اردیبهشت، هزینه این جنگ را حدود ۲۹ میلیارد دلار تخمین زده بود. به اذعان سی‌ان‌ان، وزارت جنگ آمریکا از بیم انتقادات، رقم دقیق این هزینه‌ها را اعلام نمی‌کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/436590" target="_blank">📅 11:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436589">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK-X9SqeuDuf0Zg-IT0Wj9c9S6rw0iHJs2BasiOYUPBB0PNoE12ut-l5dXbTQkdAXCdKm6XMoPKoGrU2Bc3uBakyNVVkdJklhqdKtbQp3mgic1DXqaRuHdWcwCxD4-nvdgjuiTeZqc_dBhVG8qy3PKtuCtcyDhb5uc_J-9h2x7j9Rnf91ARJ8ERWdR49f1OVYjRXAqdsmEoXUPhfcRkVBfO4xNlZY7_TbwTOeQlve-8skGAaavZHxhN8o6_H2Hs7MJ5GQtfpjWByPO2umgIMraJxaQKACJf7NGRXmh8iYpm3AJGRzSAt5W-7aZW1IafL1ZJc6MHi7VY7_idAKgiOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی: انتخابات هیئت‌رئیسۀ مجلس هفتۀ آینده برگزار می‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: به‌هیچ وجه انتخابات به تعویق نخواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/436589" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3OfHerqUlNZZASkHCNpH8zKwj3np5_MFDMUT8aMVftgUWHj-Mn2cSJFYkhCBgotwBcwnaE-mg5saiNeqHfl4QZ89dtb_rijgOh9cElSt7JbNNOzSfJ1cs3trcnArin0hICMFuBlP5Xn-YWdkrivOk8TkkZwNxUI_ybNG7Xt1TvMyvzB54kR-i5ZIgR4ieW1CvD6zcFs48eR7kcDcfiav8Vm05eeaa9TvhkvmbgQ2grQHozxG5d0n431K9GE8wGHEkK8HfIfM_ckukrAh837wBMotLHQScQhaKUm7Xj6p1MG7sH3TpcqVzoivzKfsq1lpIVOSDBEz6u2PfXPUQdPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقدم‌فر: مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد
🔹
مشاور فرمانده کل سپاه: تحولات دو سال گذشته، به‌ویژه جنایات رژیم صهیونیستی و آمریکا در غزه و همچنین فساد اخلاقی و ساختاری رهبران غربی همچون ترامپ و ماجرای جزیره اپستین، ماهیت پست حقیقی و ناکارآمدی مدل‌های حکمرانی سکولار را برملا کرد و نشان داد که این الگوها شایستگی سرمشق بودن را ندارند.
🔹
در مقابل، الگوی حکمرانی دینی بر دو پایۀ «سلامت شخصیتی کارگزار» و «مدل خدامحور» استوار است به‌گونه‌ای که مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد.
🔹
شهید رئیسی با وجود عمر کوتاه دولت خود، توانست با کارنامۀ اجرایی موفق و سلامت اخلاقی، این الگو را تثبیت کند؛ به‌طوری که امروز مدیریت ایشان به‌عنوان شاخص و مدلی عینی از حاکمیت اسلامی شناخته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/436588" target="_blank">📅 11:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سکوت مؤسسات بین‌المللی دریانوردی دربارۀ انفجارهای تنگۀ باب‌المندب
🔹
منابع خبری از وقوع انفجارهای مهیب شب گذشته در تنگۀ استراتژیک باب‌المندب خبر می‌دهند که به مدت دو ساعت تردد تمامی شناورها در دو سوی این آب‌راه حیاتی را به‌طور کامل متوقف کرد.
🔹
به گفتۀ این منابع، منشأ این انفجارها هنوز به‌طور دقیق مشخص نیست و این ابهام، نگرانی‌های جدی را در محافل دریانوردی و امنیتی ایجاد کرده. آنچه بر پیچیدگی ماجرا افزوده، سکوت معنادار و تأمل‌برانگیز مؤسسات بیمۀ بین‌المللی و نهادهای مسئول اطلاع‌رسانی امنیت دریانوردی است.
🔹
کارشناسان ارشد حوزۀ دریانوردی این سکوت گسترده را بی‌سابقه و خلاف تعهدات حرفه‌ای این نهادها ارزیابی می‌کنند. به باور آنان، سکوتی که زیر سوال رفتن تعهد مؤسسات در حفظ امنیت دریانوردی و مخدوش شدن اعتبار جهانی آنان را در پی داشته، ناشی از دو عامل اصلی است:
🔹
۱. فشار مستقیم دولت آمریکا به این مؤسسات به منظور جلوگیری از بازتاب خبری منفی که می‌تواند منجر به جهش قیمت نفت در بازارهای جهانی شود.
🔹
۲. ناتوانی ارتش آمریکا در تأمین و برقراری امنیت در این آبراه حساس.
🔹
این تحولات در حالی رخ می‌دهد که تنگۀ باب‌المندب به‌عنوان یکی از گلوگاه‌های حیاتی انتقال انرژی، همواره زیر ذره‌بین امنیت بین‌المللی بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/436587" target="_blank">📅 10:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67eeb2d82d.mp4?token=I4m7lqOvc0H7L3zRTp-aDkrybY3Wq1iDHJ_EI70nau3-K0HsUK1JJaLEVzAaDBW2JqZpZpaEhH3ARtiZp5qFzqGVDXrerOMD1SEGSyT7p9kzjVpwBTLHMH-wxFU8NBlBxpXp6qx7d4C-_A7KsNbLZCVXWhFJoxXQEztVAFjp9P_mgi08TYdef5cEr0VPYDQTtS0Nq_RqPMxgBAeMCWHephoRbPSHwADinqEXf4pMt2taGxJ7o9ab45EmysCXvWGTOaQRh94RKMaecq36C_AwHOd6M34ApGrMkBnKk4bW7nTA-dnZQHsyNDTl3e5Wipz3iVkFNit2K8H6MUT0W2AC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67eeb2d82d.mp4?token=I4m7lqOvc0H7L3zRTp-aDkrybY3Wq1iDHJ_EI70nau3-K0HsUK1JJaLEVzAaDBW2JqZpZpaEhH3ARtiZp5qFzqGVDXrerOMD1SEGSyT7p9kzjVpwBTLHMH-wxFU8NBlBxpXp6qx7d4C-_A7KsNbLZCVXWhFJoxXQEztVAFjp9P_mgi08TYdef5cEr0VPYDQTtS0Nq_RqPMxgBAeMCWHephoRbPSHwADinqEXf4pMt2taGxJ7o9ab45EmysCXvWGTOaQRh94RKMaecq36C_AwHOd6M34ApGrMkBnKk4bW7nTA-dnZQHsyNDTl3e5Wipz3iVkFNit2K8H6MUT0W2AC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدمت ارگ کریمخان‌زند برای آمریکا زیادی سنگین است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/436586" target="_blank">📅 10:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دستگیری ۲ عنصر نفوذی در تهران در پوشش خبرنگار
🔹
فرماندهی انتظامی تهران: ماموران پلیس اطلاعات فاتب موفق به شناسایی و دستگیری ۲ عنصر نفوذی شدند که در غرب و شمال تهران فعالیت می‌کردند و خود را در پوشش خبرنگار معرفی می‌کردند.
🔹
این افراد با سوءاستفاده از پوشش رسانه‌ای، اقدام به جمع‌آوری و ارسال اطلاعات طبقه‌بندی‌شده مرتبط با مراکز حیاتی و حساس نظامی و اطلاعاتی کشور به شبکه‌های معاند نظام می‌کردند.
🔹
تحقیقات اولیه نشان می‌دهد کانال ارتباطی امن این شبکه با اتاق عملیات خارج از کشور، از طریق اینترنت ماهواره‌ای و با بهره‌گیری از تجهیزات استارلینک برقرار بوده است. دستگاه گیرنده استارلینک این شبکه نیز در جریان عملیات کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436585" target="_blank">📅 10:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtL9rPLPl_FozwPh1b7AUEZ4-DJuhA9fPgEDuUJl65w1DF4W3kSLmQwkm3cuVtoT2ETPmpI5cTM0Jwrr541lJadTfzTwYt3QNivDmcKTcb6a6MNoSS0VmRUS8zKjQgrHYDpOi4Sk-wF71yJA4V2d8PmqjUhx2wK4C7Y9mGFClCqrLqKQCksyhSdwldKg9avrBME9wQh5NKbZxaI3y3D8vzwsnhEB8OtkIu2oyAnBWne9vZh5ziT8BuQO0UJuqfoS__tD8hlE7F5pvL2y3ssSDZDLrDg5KPbhs5RIKSHeeMzeU-aG51kWOykCaAkU7exNzhQu3AsNYK1Nx2sp5-IHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تولیت آستان قدس رضوی: قوه‌‌قضائیه باید با قاطعیت وارد میدان شود و علاوه بر برخورد، نام محتکران و اخلالگران را علنی اعلام کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436584" target="_blank">📅 09:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436583">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcca367ade.mp4?token=Z6zwInjcoKeDc9IOzDtCL3YY1-hqacnw22if14XbPGYQJQ208MPk0M5x37YlVOocsP9umbfu18ICXdAuHPOgAbLi1phm8tqhQax9kFn2PipDq3Vh2TS9uIW0YrvqdhYk-qVVGv_qcAsNY1IpkT3hmJIm-zPEqONipz8P9sH3xPDoV2dBuQIevqgZ7z7aVqvr8LdbsvOLW58BemRBJo-ZAdKLiUyTGQpnvz3Kw_HCJQ0fn2Lx__Gg3J-0BsE0VjftUX3cywBPCQGljuLb4KtPIOstYAgEnQpvBbIgsfWl_0k7wS8T8vqBD9jJMASpjoICTVSKnYy5DNgIVmceNzTyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcca367ade.mp4?token=Z6zwInjcoKeDc9IOzDtCL3YY1-hqacnw22if14XbPGYQJQ208MPk0M5x37YlVOocsP9umbfu18ICXdAuHPOgAbLi1phm8tqhQax9kFn2PipDq3Vh2TS9uIW0YrvqdhYk-qVVGv_qcAsNY1IpkT3hmJIm-zPEqONipz8P9sH3xPDoV2dBuQIevqgZ7z7aVqvr8LdbsvOLW58BemRBJo-ZAdKLiUyTGQpnvz3Kw_HCJQ0fn2Lx__Gg3J-0BsE0VjftUX3cywBPCQGljuLb4KtPIOstYAgEnQpvBbIgsfWl_0k7wS8T8vqBD9jJMASpjoICTVSKnYy5DNgIVmceNzTyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مهدی رسولی از «بزن که خوب میزنی
»
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436583" target="_blank">📅 09:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436576">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr2BnBRE69bT4njNLjXNY-RUWv9URBBgi7QWFVmIlBuMx6i4e4HjhbP9PpsbxcEjcc7XJbe3LD5rpDf8OtAuEDR4fcKoJRt6wHSRaf4davIQrTzgLupIVrYwvKz8VOmSpWkZsm5D6TXbIfcRgpSneG_nmmPl2K5KsOzWpSetFxuzxcm9CUZKTKBMZqfPanZf87E11v1CDPzTKEOFNPUM5xI-Tx_5dP5w3x-LVfQW-22bgWoQ4i_8-FczrS2OA81mQc-y3B9VkGyJ8NDViH2SDVkflQ7XR1EbExRNd7pDhH86Dv-BLEwKdz2iAAL-lXkSujrhKuv53fJfs4mM6ivI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-3DadDNHmDUVT5VXoQhQNI6xgoa8tWwj_SNGF45sdWH0gYJxpTURm3bX702qJXG_uaPDCRqSawvO0Wy5_dK-8Oeekcd_thHfl0DDXJaBP3vwbT5pTri9Uix-ECXadCNZnEZI4jN06Bt_kZibzOx2Goww6eWSfAUmACVOvNjwvrAbvyvu1y864FpIrZnK1KXLtUehX5t_DfVaneRcrDlys0JUpqjqFpleh5SzcJtbl8hQyDgUDTeRdu2mFlXmj-gl9MOXM2T4BK6Gy-rh0porHBlouv0-SE7hQDYLVLRXP-YakFEFs4n0daBN4ZBMaPItAkzU0XxFU7lgw9ePGtNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCvdE65_dRTL4NN-d6MnqyAXDMRbWPcujV_YB1uXBdq8b6-Va66Glp16h0iarBx0EoNitu1Tx8d7KLiCbZlDdBU6bvHlFP5suscd2VWvAc1DzT0kmeux6HbLMag1ebb1AN1u57RWqU-TFa2D3oAr6wkQnXvP2kmAUtHV9Ag18kDVxJjf3_7hYPM_fhnmVdPXOE8I3SYnwejnr1dyaM7Vuu0E-LEpGyzGYRY_dWoQ8JtiGymr5sP_ProAl35O7ZizzfPxghvaktcSMRbHTpgLrt8M1q5xqG2mZuDIY6z315jsdqpNmYECeVNWXuwdj-Cx1vFHFZkTYWzvSubLG07mpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6dyDserFdO4WbTLp32ZFAhUcWNGOFwoK37HLqbVwy_TZ-fWIyvFo6iZIQkSnVS5EHyvoUkI1xAra-lO7IEiIzClVMPLknknZfTuWpvtPB9jruP7v_lgzVHppgLI1EvKLDwEhK7iVu6qXho9uYAYhARtBxa-h3pi17pzK6hnmyxQEUMy2_4w__VNXgk3Jz4po0wP4OQBiVsOxPzNeuTs5byW0u9yvAy4RUtjGWRFbM4fG4wKihER6FHMm9_SZIDddtgqh_fU4XIaqcPVC3_sPx1koe9wOJbhxeT7H7TD9t5-AfBrs_4rCSpUJLfGFSOlJh99_mD5VPGtFGe-Z7Wkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSS7WqcSnEE_LJHLO2S_JFvm44dmjuABZde3Z_XKJ-5TZ6XuL1WuXaiSZUsCFFbKug68Tva0I9HX0OoX4yBFY4cWsfgVBG5i39wFmsgZc90EE_o_DUsISTPx_UkNAPms8aJanEl-H4Wz5EKLMWUSbfuATLZhmPEzNfm1Uft1X5NhmPFSu34dGqnc5-hywrQK8mu6Kv4zpkK5c4Fjtt2lft2IQDRPOJq55FHFwsFa4hqlnfgIth2vOhgGqU7HOBq7boD0MvxZ96S0iJe9MLphpDanw62csuh_MHN8rGe-Cmq4_tll8zgBlPGBuOQWFJPl-0YQUJMI7hsh9txydl7prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4e0aJcNj0OAd7iCBheX7gbIMgPSaJS7gWYD1kx1Ymp-JWdu1mxnSi6hINfYRRsXnU2y9WsPrp2-44czZSabYjJ5U6QbBoYoHJjSLWVoY1EWi-P3PgVhwgWurQH52UUe61NgrJ40tLu3SVnJzAYgOKADpdl3Zjiu_VuZR2eqcss-799N4E2Cix6-0GeblG7sZ3CF7zBfl2Goi_xidDWyrd6WOepU0q6cr3-Xxxscm1sahuKe3Tn-SDYOYMdUDfYTbEnP-ohiZzREKFtrBYvtS3yrzrDGqsfr6QTfkHBKAdD-5mqsV7ovRputQYh3UTtan1QBJKzUS1-Pg9TDGav8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j48DnKrx5A1ro4OZMXAvCfj8_4wVBcjZQjVsiQbAN_4_2GRuESHNxmYdYcurgJ6NC98l670UXLjy6E6PmsTKvhl2kNT073HxGR66cF5ouFed5XrAu-Jo8IDvYUq_45puxNNrjiMw9f_mMwnCDMBTFns3I-s7lxq402FgYBpf8zNRxkzwbNUazoryTQ-tn928cCwhPV6L2VUOH1j186LPp6WIIHe3hz2TtNrlbn6F0Za7fumg92bBziSxR7NPHXAF5IU30iNEGtH8rPaXSq1yZETwIwAIWSq1Rfy--_AB5fOnCo-VDC_eClTpwVl3wdd31xMh06tK9fMvAp_ACNQqEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارۀ هلهلۀ فرشته‌ها در قم
🔹
هم‌زمان با سالروز پیوند آسمانی حضرت زهرا (س) و حضرت علی (ع) هجدهمین جشنوارۀ هلهلۀ فرشته‌ها با حضور اقشار مختلف مردم در جوار امام‌زاده موسی مبرقع برگزار شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436576" target="_blank">📅 09:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436575">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfaRwRpxI8z_FGiVHkexiPnkVkbmvCxvmfUVJg0fRo-j_xkhQ8cn7vk_28U8Qs9xozSQJB59C1h2VVslWlhLdG7Dc0b7WsHKChF4WHvxFU4LPRV6jFBYfi_P31DgXvU4_pr9nI-64kJbm3e_-badqAJKhfA4QDbT9iTeziwbDYpSgrz8sWlyi1LEdQ7dcoHLk9HxGfgkWCQl0Rv4T0SUyy7-MIy-B30CFGXyS__oxtrY8KGqrAFji4Wb1LCFmT3SXMp7ASDl4VSJ4UzZnxk3vPYyFafPXuSPi0_u3n1_4UdF-I5EG7Fz4ZNbcWdv6Z6jon1Z2H7gpBDqlEYj_D8C1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۴۲ نماد بورسی فردا بسته خواهند ماند
🔹
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔹
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436575" target="_blank">📅 09:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436574">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab78b3b3d.mp4?token=QiMfCC888WAkZh8g6fs9HapnSwrtZAyFAibmPZ12Xzb8LU60hyVvj9Wj8399kC25s5G5it1YQbEuKYkW4wY3MnAChwW6haUiso3XdGoQE1G6rw_OouPeLrAK0hbYx1d5-eu56HFsgk1DdIZRm1_yP-ahxp4yDegQnwZwZhl6zO5LeYvc4GAHY0mKadfwkt8SY-ZBHnkUFO9cHGNV0p2NXdm_I79Of2z1FjAitVyygVt8qnTXjAvyA5F2HOxkatJUJ8gk8-PvikwHakGbrS_1Qw7mVPGNw8g8KO6uq43-O8ucZgHcuLpI1uijjlGnBMud0z2YOa_LbgrvHXaS785zXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab78b3b3d.mp4?token=QiMfCC888WAkZh8g6fs9HapnSwrtZAyFAibmPZ12Xzb8LU60hyVvj9Wj8399kC25s5G5it1YQbEuKYkW4wY3MnAChwW6haUiso3XdGoQE1G6rw_OouPeLrAK0hbYx1d5-eu56HFsgk1DdIZRm1_yP-ahxp4yDegQnwZwZhl6zO5LeYvc4GAHY0mKadfwkt8SY-ZBHnkUFO9cHGNV0p2NXdm_I79Of2z1FjAitVyygVt8qnTXjAvyA5F2HOxkatJUJ8gk8-PvikwHakGbrS_1Qw7mVPGNw8g8KO6uq43-O8ucZgHcuLpI1uijjlGnBMud0z2YOa_LbgrvHXaS785zXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این لباس‌ها برای چه کسانی است؟
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436574" target="_blank">📅 08:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3IyF1oWZKufC2FQFwNZyEiPCTs1859QCgzjSkbDlBRfYlW1XGOCSABTc3DE9Epux-SeLX3fc47e3LMxa7to1I_PDt7YOrwDh7ePZDqZGq6YCjhK06nmrL0EDpETA1eDhIigACAIyimFQKAUo2Hf5j7q_s1j3ljKepE2ZLmgRrzrXCUTwP76SCLV5QlUMZKIj2jd3GiqfsepSgq0Rjda7D07JCQvJjs4gBw5FOegog9DMYOjzQcNK_ZRYhLGhkYzDjDCk-7EB_QhC9pscc-_sMfcqnh287NbVKNSk0NPxOq0P2QJVUCLHy9R9LLvMbQypg9wAqRs3YYJFkHzQ0ZB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDLphgTUMAYEb3STVYXzd18YHjRB-svAxM_XKN2_sjTNP3ymOT0rHJjVTE8CRvTx_VRskW8zOEM5qpLKECTxZox508MmTwjZiwIZ5-XCyxyw_2QPyClU4eo_o0hOo_zh59YlMeWU6CLIHjCGkDOxpuVM4N7DGiUdeVYA4qWWxzwL7lStTDU3JJBq4TbVVa4b8HDYJJ7GFNt531ht3Cef0W1RAasc6mR8eYnCAEJXhpM_cdPmHLamMYGhfEmmd48CeY7YpXMSLLgYRAeoWkYTOHr7X_VC5qh43c3aLbckaZm9oPg05aTRVi3aYA9JT4LO8SWPRG2J3ftEdAT2AdznbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slMZDUJIEagcJwuFWwzqHyUkoeIKNDYW2r41DY8cqg89-EG1Z9ynQXxtCogtgwcM5XX0bOoVzOqSCNtkez10zCabaTK8vrlanffJp0cQk0zhW27NuMIZWG5un_CtovfyLp8RjFgDVj_6UxGWbbvXWd5viKVCQ7d-swy25FJKN0-M4cYh4zOWDox5P8i2xjI6QiolGCf3W-IfWkBuBsHsoWcJAVGZ_yCPx3sNxCgGUgES9_4_RvMq3d9Q2EJYBnyiB5gu60uNQBO4SrzHYaJ3TWnoz5HPq2ivEwA7CEOdrGjv5vWHRKdLkx3LGg1UFRzsdTNJuCt1elOkNQ1PMN9n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzi7PE9DwwYKIKUkchjWC_C3xQOxE8DtHPoSzoLGyW44Dlhl-FEwPXov2qBavq5RrMVXTdA4ehQdl7mTlc8WVQOofcK75XFHTAH6qlU3Q6nl6safQwV56sUTujqvi0u19_o5hdUC47atN2Xa3X9xstxC9lEqCwT1ivbjJReJ3ZkSLBOrS9G-aBbmt6ioRf3IMo0Mj_YQyZSc7RXGzKpWfOfN_HQdXEPkR5ZuYjqLCUoQP3gBg2D1WTfLRK4lSuvhwJXVbWiHEhajkyLVsba7eeRlOYl9OeEbtCprWLj6W3c3nqdZ5hvtYazdvWK5hVqTUlgZbWGby9ZNtw7z0hObIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CK6g4QGGw3W2pMMeLajAFcFeHnL3kLEI3tXRJQ0XLreVtlIY4i-Dr1Ss1gkAvNcvRsuknc-lMxb4ebB0PciojCFsr0cdUe1m99n1xOeNNInytSouaHnHb6bbPl39hhSUCSU6qeagyfLDZL3gnzDTQFzTRLj9Jz_tXKZrEHb6uAn_YjfnlprI590Z6TpucFILudUF4b_wS-0H_zhQzyIGEkPqlucmQuOFy_3r7QMPyHaZKh2iWbX9rV97F0ycl-vUyxGhKq8SklCV6JX-zXj_UaUWQ7_-kLi5WkxgSf8Ci1uzSgtabDEVLpzdUJzeDydmkiHxci-df2UrB2hWFouHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-nyR2eZSYa8swMeej1hEppXJV4KMp9QTmr2k9KkGRmGjKNuwdwF7Pz3sVa-sL0Pz8SWF7vAEZ-Crb9O3-I3WWkk1MizbiKE3zLGWFtSB8hJdJzgtGwPvaHGlDMxNHHYVVyyn0pSzCxZblm6uyAe1s0evgTjQ0lBOwZQAhyutiHzHe-KCsEVcvIDzknEawrhNe5pQr0MHHNoTc2rMtMapzxDvp2-4YSf937Jqhv5OGpv1NcnVimkbfeB701y0zoFW-tfmz-TFDa817ygFWxjEKzW7_2VOTFxl4l-FpGpPol7muwiV32HDA4oUsxzV5tbfNwsY46P7xVf7XeAMd2c5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGgO3x8tZdaXjO1DLOL_LyC-ZQa6BSfOYxGei_T6kGaY5HErZ4sSqCBZUX3dRJOkVO8UFixMT1AybKe92FVXk6CWgT1ftwanZgxgjx7XDaAAzjjNlkqR_X49NsuUkpSQOS4OQmfatY8OTfzOb1at4o7KPCJo0HHYM-5WTR_IX1DHb17-QcrcSQc_SN0Hmm4dJ8CNKcG6a54rA4vZmcc28wjvxtjWxKRVNpEp3ifjKj7VGGp4RZNZZ2aHv9BpfkGXcvYvNW0L8k5tEEf0s_RXhTlgDHOiz3irAtwMcIhulJQ5H3Xm-SYM-qWlYhAMZiL9TLpMIglrXlaU1HQ3itMLLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زوج‌های جان‌فدا
🔹
همزمان با سالگرد ازدواج حضرت علی(ع) و حضرت فاطمه(س) مراسم جشن ازدواج ۵۰۰ زوج‌ جان‌فدا عصر دوشنبه در میادین اصلی شهر تهران برپا شد.
🔹
از این تعداد، آیین ازدواج ۱۱۰ زوج در میدان امام حسین (ع) برگزار شد.
عکس:
صادق نیک‌گستر
@farsimages</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436567" target="_blank">📅 08:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42603926e.mp4?token=YZFmmNMbgkFi1EkZan8YI6mpQkstW1x-qTqbrAb5lIfXEW1FuOjalqPSb05QSSloANrjVqZvZdlE1Ffk2O-hyqq1Vukiymh2jxzGCd5h7-gp6CC-JkNQHgmBAasx8Lpf_OZ6xFQuhFJXCVKL5uy4MGQwtCtBfAM5MJ7rbdV021KoX80QBuDV-Jww9jEZFYZ1BJ141qw1mItcyBNLguGoXLv_BYx1p0LW1aNwuK8I8wTOFLFTqPvXzz_6jpwAqUBytLMPwMh-zQo54eAjaX3ItfEMGnXdEIRUHmYD4ICodSqXEsQULBzgigsqLHAYqr1JkRZitagbssuoat1jRIZhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42603926e.mp4?token=YZFmmNMbgkFi1EkZan8YI6mpQkstW1x-qTqbrAb5lIfXEW1FuOjalqPSb05QSSloANrjVqZvZdlE1Ffk2O-hyqq1Vukiymh2jxzGCd5h7-gp6CC-JkNQHgmBAasx8Lpf_OZ6xFQuhFJXCVKL5uy4MGQwtCtBfAM5MJ7rbdV021KoX80QBuDV-Jww9jEZFYZ1BJ141qw1mItcyBNLguGoXLv_BYx1p0LW1aNwuK8I8wTOFLFTqPvXzz_6jpwAqUBytLMPwMh-zQo54eAjaX3ItfEMGnXdEIRUHmYD4ICodSqXEsQULBzgigsqLHAYqr1JkRZitagbssuoat1jRIZhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واحدهای صنعتی راکد که با پیگیری‌های رئیس‌جمهور شهید احیا شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/436566" target="_blank">📅 08:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYgWuPoB1HIKV_L8gsh1as_EAxTbEdimaBqGjtKiefBsv5kBi_CBV_exh2bF_yjx91_MrLelt1UqDjQwHMS8W0gsYn76FceTLdTrNNcid_hixbv7hd_WIJcc7D4j_1nEQ_RaNLDLCxDG2QYrhMbbLqMTZjVZEWblA8RHkguKmGf_M6ie-5SL1D5KjULuO0fto2nd_aMPHJYwkz4LGnD5IRgAZoAYgYCFdgbcJAoO6jnYS5Lpso7NGGcBhL2PJTH8TFlthz1focP1VPChrlJW5LiddkqN1775ce3b1_uU_DxVPH5mcwLjmQ1s5JeAgQ2slNOpxT63z8Xox3FQ43iopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عشایر کشوردوست
🔹
بیعت اقوام و عشایر ایران زمین با فرماندهٔ معظم کل قوا در سالروز بیعت تاریخی اقوام و عشایر کشور با بنیانگذار نظام مقدس جمهوری اسلامی ایران.
🔸
سه‌شنبه ۲۹ اردیبهشت، ساعت ۱۸
🔸
تهران، خیابان جمهوری، خیابان کشور دوست
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/436565" target="_blank">📅 08:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6406a66fd.mp4?token=XVhJk65FzZhHpne60fRaAgftPtvEUMn492tWs8urTVvW1yX90AbJueTG3rQJKyWpgqPsqbDnlITlACNNzpKFC3iN6DisFJlShSw6pFl9Xt9McbYuPDSN3J8l-pZxyAJBqqwWwyk5XEo5nTrfBel8Svy642T3GAQuOwf853feT4sVuW9YRSsW3g-W1U_gvVH95BnR0b5a04fsN48FG-uwav9YNKblJ2FpCuOXjunXHkDuZXBlHgwlNKfYkEYgpahuoxqZWKv1POnEtFqYYvVrM8fqCxvzQhXFGkJfy21Up6Sf3GBY_my3m5Kaixce2_WAE3uFhuXVl2TjeA5W5iUyCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6406a66fd.mp4?token=XVhJk65FzZhHpne60fRaAgftPtvEUMn492tWs8urTVvW1yX90AbJueTG3rQJKyWpgqPsqbDnlITlACNNzpKFC3iN6DisFJlShSw6pFl9Xt9McbYuPDSN3J8l-pZxyAJBqqwWwyk5XEo5nTrfBel8Svy642T3GAQuOwf853feT4sVuW9YRSsW3g-W1U_gvVH95BnR0b5a04fsN48FG-uwav9YNKblJ2FpCuOXjunXHkDuZXBlHgwlNKfYkEYgpahuoxqZWKv1POnEtFqYYvVrM8fqCxvzQhXFGkJfy21Up6Sf3GBY_my3m5Kaixce2_WAE3uFhuXVl2TjeA5W5iUyCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلجی: رهبر شهید انقلاب با بیش از ۱۰۰ ویژگی، شهید رئیسی را توصیف کردند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/436564" target="_blank">📅 08:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPG45huRMzrYtnJ0T2RHyPH4XtgyF5xc6nHnA76HQfNwD2WoA-OliEQIR23BKHc1tpPAx5RNsj2D_vbk7e1t8hVQr7ZuvxuoTQaMiSs77PtZhyFreN5r5m9eFCYB1WZXXixTt2u0wkCU-kch5VC0chrvBTKGtguSywtCp5edXiCalWTfvWDQ5P9ZWEtrjVBKxdVWH6OHPxcpXCDXut2ZJ_J_LZ5nwLBOpKx9xJmTihY_OOX6C_FK9GTAZzHYuVmrV23iFDXrg11UbsNWrGfw-xnDXbpalmFnqu-8lmGWGNoF6XzC3TpdkVrZbSguFgK9kkKMmBV9z1X0RWIspq894A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنبد طلایی آمریکا؛ ۷۸۰۰ ماهواره برای رهگیری تنها ۱۰ موشک
🔹
مطالعه‌ای از دفتر بودجۀ کنگرۀ آمریکا نشان می‌دهد، آمریکا برای رهگیری یک حملۀ محدود شامل ۱۰ موشک به‌طور همزمان، به استقرار سامانه‌ای متشکل از ۷۸۰۰ ماهواره با هزینه‌ای بالغ بر ۷۴۳ میلیارد دلار در طول ۲۰ سال نیاز خواهد داشت.
🔹
این ماهواره‌ها بخشی از لایه فضایی سامانۀ پدافند هوایی پیشنهادی «گنبد طلایی» را تشکیل می‌دهند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436563" target="_blank">📅 08:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIfFahm1x0joMUcQY_Difv7Sj7G_ra6s9kFxaRpGACnqJa2BBlsOPwFmf0iI_j9RlCs_tMLKW4K6qIIM4wiOCzBhEH1SZi6NO-KfOdgTIiHOHwzgbX6-O4uj7kMwwSSa8stUdtOvnj4j1Qby0FkyyKhcfpKgh0BVk-UbFkP1iwlTxlEUyBGUolPYIjj6NobcnN_La5SGFIFSfRbU6uNgHJN4Mdmy29J_5NowPWFEB1vMJCN8UXxZqcMZweePfSkPPUOiuJxO0KTPoX_kI0hC3q2TE9iDTwF9gBl2NcE60xEgWmOMO9uQ_XAdi636QwOny2a2Fc6XBU3EOzfFVmjbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل‌ قبول هوا در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت هم‌اکنون با عدد ۸۰ در شرایط «قابل‌ قبول» قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/436562" target="_blank">📅 08:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K48NFQn96hMyF4Xhw_o3r049VOsStWX6NqQRfm3dmx3maAAGs_SzTkr-w6DjFcZQo1DuZGbB_nPEAhwD9_appdMMg3JNEJB8kXYFcwuLus2Jcyt2Po6pAxPkmdrRZvxjpYTtgaSJ2gKBxWgYHYnOl8x8mdQRy_Qkmn53dcCPHRsGlDJVtHyCPb4fUwrnXxw2I3yA4kOOYgX6uxhJ8n6M4227GnDIoJV4VA5s9vBtFHSuvOcfXKgdfVhEUmk1ecdqymZiFDmoE5jBtUhCrJyOABlDWf5w6f2jZGXOVD5H_Y1sSk3_NN5_i_ipk_UNm0dR_yi2mUEKDlnQb7TWUR64Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت پدافندی ایران، ترامپ را وادار به عقب‌نشینی کرد
🔹
روزنامۀ آمریکایی نیویورک‌تایمز گزارش کرد، پنتاگون هشدار داده که ایران با بازسازی پدافند هوایی خود به توانایی «ردگیری عملیات هوایی» آمریکا دست یافته و ترامپ را واداشت موج تازۀ حملات علیه تهران را متوقف کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/436561" target="_blank">📅 07:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77cdee184.mp4?token=uNEerdjlzEq0BIChCXXVBhRyaQx0Dfn9myMggm-I3n5p6Jz-VjggdmfykjFE9t02GHpZKn1kM-OM1ypNdVJ3UqgeZjkOl_HiOt7oYjipgYe1pdmgtlQD2cjmuQsrTJkME9UbFRshDNaMawteuRSi49kOfN4DicWLsXb77BBFGa6eAaeP06KHn523vtGrnhMm9KD52H_A2ceaIGYs8oVnK66GoFfpxTahBMKoaz1VYugMJOFkkk11cl73hz-rTngbzBgiiNIDtkkrzzCpqAGnWl8Rr9jMkVokvHYK3C_Q3QX8TjPm8-aNCxZR4IIBg7hy-Gc3j3C98EzMXNQY9kJ5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77cdee184.mp4?token=uNEerdjlzEq0BIChCXXVBhRyaQx0Dfn9myMggm-I3n5p6Jz-VjggdmfykjFE9t02GHpZKn1kM-OM1ypNdVJ3UqgeZjkOl_HiOt7oYjipgYe1pdmgtlQD2cjmuQsrTJkME9UbFRshDNaMawteuRSi49kOfN4DicWLsXb77BBFGa6eAaeP06KHn523vtGrnhMm9KD52H_A2ceaIGYs8oVnK66GoFfpxTahBMKoaz1VYugMJOFkkk11cl73hz-rTngbzBgiiNIDtkkrzzCpqAGnWl8Rr9jMkVokvHYK3C_Q3QX8TjPm8-aNCxZR4IIBg7hy-Gc3j3C98EzMXNQY9kJ5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گله قوچ اوریال در پارک ملی سالوک خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436560" target="_blank">📅 07:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXUCnLi5gQvO_ypAoMjjUTrWcSE4gEzu796rhHQHNQ7uZbf52vZPEgcE3uukIjD_2t-BGHyolcvELgx3BbD2REbPdKr0t_i-BwjpRo4kLXmpLWwk0p-6HopkgyU-oV8LgUoDlTB30-WMjfS_Z4whavzhxyM3TwGEOG1Ukngxxzs6MjUqPOnyzI0dUX2JRFgVkHlAH6NqES7ckMDqEszuAgv8bU4xDmjw0iXvxDpxRgRE8hDANNZ9j-PvnWvDsUoqGX15pUNlL4KfGZhV8JTlDm84f8gAB8s-y_dKxkYmrUPc08SZNEu3SExj077c7vAXkegQLdTQWpUE_eoogEy4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFi_CntixHK93HSDPVfF26kpNyqFUjhrUbsRnnCTe252uR82Jy-o7R-ckVcXcCzAdo3GwhkYjpgg_opTPxaqjXmKKnXqA8XKL4HwgYPwqJHtFecCGdXeLMEKm-oFtnr9V29a4piusnDQv9NEwOFLM5RaEqp5Y1fIMYFTCURfKGqg51lyzjtlD6RO96RqY6l6ATF4W6XfMRLGvjmevuXFjFbaleI7LrekMHWqZ8EZo5k-jchE5frTbkcZJq9pL_hQj3Az-aQQ7YZIE7gIvElGS7GmOWkRaO0zQ-QdgsmLX7Va41DZX_vc3zN2BNuf42QyGfm3Uav17n1S_SzeCVmjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6dcieadCtvKUVGagtMOZp24areI9sKOypXOQJORKkYLiX-fEPA-uxBk0cmttSJh0-sVmtaf9LSm7g3n1Ul0rdrXsVIkSALQ2e6JFH_KRIcu2rKufsWey58D37O0vXA62xAnsfnYh-cxKrZY6DYqBWabA7uRtQYwBvmA-CWcl7qL0VS7RDM-BQFUpR-PLxTnPJm66fJePEWWCIqQop5X8czRROXF4HzYx4bJzV8wH9NKSmMRQep3nO180WnMTFGB6xhAdhcoMBR542PJukDSaNXJKz1PgcMF0mRCN6NJZCPlPShaF5kYTgShwSS4Unk2C6axqeSIJPGksvYQ3rQ6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cH6lS5rkw5dWlHhc6BSPHRL2sU20gnxLwIHl95lOXpHYrVb-rt9tcolR0VdfY4Am8zIOFdaaGAtqv8owNwevVIAk9YQKPhuiC93dFCxfCAO8z0RUz3KmgVBK9ilhcTPgK-nERU4QdBQ2FfGe9XBtpE1yzHXDlbqIon6Qptvz7RWynYTw3jx-1OhgdOnIbTaDxu1MizcrtD0ZLCSk0Z4reHLDd0XgpA73B4Ud2WMOX5sOzhV3Uon2jnI6crYRaj1ZSDtxebiLrzhLPxpQDAIaCtlrIz7zkukXzHK8jHHocPlJwSEK17YR7fw-QCwSjqMHmF2o6kR7NavUUcPWljEoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EeuGU2wneBRy42-aYWZYsUG7E-gR-xco3eCJE5pY0ajODDeNxRfrDn__FQaSlP5PnLugPLPgG_q0u5VPbNCLTW0NO0diquDTzeAHXUCBhrmDO2mkun97O2ZfEKoswGU-1g8mi3sFOCyGz6WcuG55NHEPT50SfJBNk03GOhEncnuF7lSpXXOycGqA1rKA7eTeykgwGlcnr334QXD6NZFHiulg23ihOTuVeMlOYY-_bWQFALBKTl8asdrMuMqQbzAsoyu_9-YGTjsncqMbfkBiBFcMdenMryIHaT2GxqLqIZni0VRfw-Rmm7tlHPefORCVs-FqVpYq7UBRHg9yBf64Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUM9EbA3QITjjDtLwqJf-m-iVY03N5ZxjcdMSHLE6BbBhGal53DD2Eg94YrMYjSztk8DfB1Zeb-SodQTdXdYN_FYmd57A8Qr75S_G4BJKFaMw5cLrS3fW7qp5e7hrg8Mmx69ijCoCSKe4KAcb-tenVfkpjQGg8L0vpgy-XY_XwsdOhIkwHcL9kAPHy0C1LKxKj_y2jkvcMSj0VjSfWXBM87nQ5Lg7Qb2PrATPN2Z4TB3qBrMmeq22aWyji0mWZ4JLEBZyMU361XCPvTphsQO5FisAqXI4EuTSfhDsMn48ncmscdgccV9MTuDQ4M2RVhp-Z5jtQ41BEXAvri_ACry3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC7n4-AbPxAI3EQmR8CZ_0My7alpb742Ge3QSBLWmK8ihz1u-WZek6kVfJiEgqNr_Fq3QFiurGcskbHhmOe40nu_D7FAP00DynUzHFJXTa3KauRr25k-9VsUrGJLhBw8pgnxaVuTRVsriBzcNYU-OpTe2JjJjazVluZ-QTvpZNZtd5JL3m_xfi1N8YNeP5-3-ItagC7zLl66od14lZLSVGOiqOA265A6i872V3XI9Rw8WTJv5nnD8A85N5rWFB0lCyFh_tafydel0ASv3n3kkpt5oIal78Cdvay8k2ZIRq-YgGSTc-fte3zkW35FpgzoOQAw3cdmoPjtnuVUgmpTHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بیعت بختیاری‌ها با رهبر انقلاب در رواق کشوردوست
🔹
دوهزار نفر از عشایر غیور بختیاری‌ برای بیعت با رهبر انقلاب، برنو به دست در رواق کشوردوست تجمع کردند و شعار «دایه دایه وقت جنگ» سر دادند.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436553" target="_blank">📅 07:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRRVZg82BFvQ4LESHNKKu38_6puH9XblVJunWAb3xv_b5wMTFE_cvnScTBPRJqIoXBzXCX5uAXtcYrYi7CypIS9TqERZ0bvIhJYPa6pyw9WPli_fAVMUzyMVSxB04StCgndoloq5RmsWJkavCrnzDz6puq3uSmDEI7dyDPMwIVhFUeUP4vJOhLXtsHr7nsfHjbDMFC3bRjgh403L6POw4VwwhVGdF06OmKA84NT6a3WIQOJTti9gLaYPf_X5_VGajPoJohZiPZqAgthly8MNG5Yoh3ajbnKcbR48WCeX9iItShxaC09BTJ-z4bUOegdCbWXcLtkjF83qNRi2IK2hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط ثبت‌نام کلاس اولی‌ها در مدارس
🔹
وزیر آموزش‌وپرورش اعلام کرد، «هیچ دانش‌آموزی بدون سنجش سلامت وارد کلاس اول نمی‌شود» و این تنها شرط برای ورود به پایۀ اول دبستان است.
🔹
در سال تحصیلی جدید، نوآموزان متولد دوم مهر ۱۳۹۸ تا اول مهر ۱۳۹۹ می‌توانند در پایۀ اول دبستان ثبت‌نام کنند و
هیچ الزامی به ارائۀ گواهی پیش‌دبستان برای نام‌نویسی وجود ندارد.
🔹
نوبت‌گیری سنجش نوآموزان نیز تا پایان اردیبهشت از طریق
سامانۀ «سیرت۲»
انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436552" target="_blank">📅 07:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV-htBxLnJNn5VRQwFJXxBLG6bm5nPXskT4wXbD_lvgp3yYVti6ZHyJYezAfpjQeCcDzmyydXXEHtYvQsklzgW7njPSc394Lrn7RjCFoTnfnn1_SIGu4wb31sjcJw6Y9GcDiv6ak4faLDYG4NLWnu-7wOFa8Q-QYKY3DLCxNlF1g3goat3thcxYpAfBU2esRC9MgYBRwTMVBM8Br57Uf-v5D6SwfYxwCn6VtE3rbaScpbvjq9oYSSR1z154AArjg_OBfv7zHJFbYHFulgrJZNMzszY1mlfonyujnq2EnYUSKWvOKYjoFmXQP3sYTIMuuCkuQ1XI9ZHvShzCNUrdaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhXnQqST7dbJ4a83u6lLAcOLE_TafwNKS1580JDzbbrbQ85goG3lpRnWYJ2sqgQb9WRbiV05CF56p9y344w9oPM50T99vGjuG3r9OrAYha8MQM68cMUmI7F7jJB6HmlkIPRXmdugHwqarCaxyrMknopZGYLmfpmFtIu7mdpsUr8sMk3-SD_W7GUhZGIoldTqt_aYeXI_oK_69xFwMKj-LSY9yflhKIRBgszOGZv0-7R4XkP6jWZiAroT051DZcv3gtHeS8HpBKV7VGh4xseDIR2c8Qapqifrc4i1evddRtN_amo2lXNB0MDUGdk5NB68d4lydwcRjGjDU8oV4ZF76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pECgPSQn7pKZChvYUgzW7TQ124MWsX5EoiBTJBKJPvCbJSeUTRQ30sy4-SiQmUumYFzPzPGkOyVLwVxxwMqcy0wJiCYbGEHZi-QtGsRgPHLXDpzurGC5udTSrLWPEI6NW5tr6DuZDd69zsuKhogTlBUniQJec2ixvLuY6PRAwzN8SQ_rWUdokz9-PZl75gF5X-EC44XQxiRga6KGjrJsLBrUUpjceNS7PlM8-zk8qoojEjuU1BMagmJh-YuQenil1RR5kS8w2IeH637ANH9JyCd_R03c1pTxKzYOghGcJShluYCU4Elaor7jnDMHQli0qdxpt-h2CLdbPrmzarhXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksn3bzGVwf6anGrU9btUzibLL1LjvcKZEJX07_tbiO7niyoBxkFRd98soy4_cN70xfTym-rBekbFXY89pvHLKnyqjq6KUfBK5-Pqgsm_8UugXkNW0uUO4RwNmc5wtkcI69QQhw-wNaBmE0HYzIDXq0bgX7KjO_7hJQxPwa_CUGtxIcy8eRjROmB_19f2azsPL58oxC-kFOzO9OO6Fk2gkZPxxcv7vjMnLM-9gKgT7Ug5s7QROsZTZE8J1sM1VYl47qyTNTxNJo0BiPkVytUYcKGzNRmiylHU13COPeQ22lJkZxu83Y1BY55xvN9o6KTmNO3CnrHRlB8YavB9CgNS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMYMSKGsBlTG51M3JCnTdRBmmoP5LGaZeL-xhnqoPsf_eC48ZiXXOsj5pqkk3Du7qOVtWhgwzmvxoVTUh02PVpvLu7BDS0wkZ-sSDgTr-gpipdiCa9FNCeNe8U_rgBaVEtKTTkuFLi-a1HVyo1vxXix1MXCKohveEZvDs5CwCkOOUKNHheSaMUzs-4OrLsVRTS_t9zmMHVJPf5qSwslAIsjicIwHWpMSXxubPfjnNejfpCrVPH_zH7tHMcqonyXEuUFJl8CWU6AKFIRYKIbkxCP0WnyhIJr1JjxxOObL8B0GeqDuUirJ0SK_oSTdxV0ml_hwcGNCmrA55yVZXSk67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXi7A0u0ORuNtJXz4rQaZsrh8C5YtlFj0VI_fJSSHWlsf38-kpou2yqQzCVT8WVQzVtGZogT2w3nTuBsClDVgZte-T0RnfIJyMOKFMBlTxDxfRdc__zILSTTOFxyWbubTcJxtEbxemSGVcjA7Kbn7cgI2G_zBoIRHUiwtJNYuP2BwWtfSjOXDUiju677DSkoDdvfZbclf0TOsmy1jglq4KpymL5GNWYqw5puMcuJXX8o10AwzkR0q0BiCvPNNTN9Abxa0vP0FjDdC7HnLWd_gqmtcyMZff38t2dvbZdr-lYveXki8SRGUYMPioUMpHxJGELjksoEu7w0E832LPLuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olQ26UGpN1tCfFd1UXcj1vHUL14qddpGfvCegBibRTSBTZVl_z470sf7WNvr-AZGxKeXUK3w-F-6ULDimfNoZXpR0Nldyr6peZmWXCiN7VFlLATCurYowjTWwBiGhB1_wOyX3r7Icc8Q_iRFMkGQLoGpuIWY25Z6xBfgyh5e9_4Hl_OW9GflvEM69qxuM-kYg63M0Ylq6npekYPpXcnTFD41WJMhCdAuD16UMzpQK3f3iJ1h7QdR712d5Yx5vMyfFoKDCayRYoFM_ZcjBF3ny-bxZrJIgf_3MN2BBqEig01NKaNLJtHrASZm75rXWMs-4SN7LykeQlUIqKVzJF1Y5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عروس‌ودامادهای جان‌فدای سمنانی هم مراسم عقدشان را در میدانِ خیابان گرفتند
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436545" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy3vCaQkISy6GiBoXb1H2pqjEp_zwR6_F_0U9f_6M-T00gUjnYBwjuVxW2dY4QrDaiHI6ayX13ouC7i1n_QnaM-ItjFG_mpgNPjfe583HOxDxPJ1uT-GR5ASRY62ypYqewd4t2dqkGzKOs0uoviAhK40HCy3A2GBD5Bj-s2rsePgPFBoxM6liw3brbT2iBVU9arEpDzQgV3NO4kQgwkVeNKpYJ1x3bXrZLRaU0UrTLh4oJlBT-7mDeWRKTSFzR8xH7aJPtZeUJTnB00lyHCnR1vxPVWGRYA6qBHZgXBNAMMRXxaGhd_5NqQrTDQSqm-NuKT0OxY1IN0DclBZaLDmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر دست اسرائیل را از دریای سرخ کوتاه کرد
🔹
طرح اسرائیل برای تسلط بر دریای سرخ با کریدور زمینی مصر نقش بر آب شد. مصر با همکاری اریتره، مسیر لجستیکی از مدیترانه به شرق آفریقا ایجاد کرد و نفوذ تل‌آویو در منطقه را شکست.
🔹
این پروژه که بنادر اسکندریه و سوئز را از طریق خاک سودان به بنادر اریتره متصل می‌سازد، عملاً حلقۀ محاصرۀ اقتصادی و لجستیکی اسرائیل در شرق آفریقا را تکمیل کرده و طرح‌های تل‌آویو برای تسلط بر کریدورهای تجاری دریای سرخ را برای همیشه خنثی می‌کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436544" target="_blank">📅 05:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWhzVomEePCNSvqc5tbV2ZId3lgyGbwTAPa64uniwUu0iPhG1V9aOt1h53-BwQM5X4f_fWQSUZE2bpghfY44noXroah-oMc3rza-la04Fkux9GlKrcIOAFn48CBP8ukTJKXb8vZh3DcE2ATEkCj19EdXN-6bMN3ztzbUysliqh6HcKgMnIZmDydF2gBJkoxb9qUpvTrUS3gpOL0BtUs2kIW4sa8Gil9o-DhDHdQPWObTDHuTt72eKvd5cQDdiEnoDh10llwmRVqZ-_XcwfLj8EoqlEH7-hqjPekDfTB6RslNfPBWWVzOswjJsIhr99mayFa68tPd8L7uC4xk5W4tPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالتیکو: آمریکا برای اقدام نظامی علیه کوبا آماده می‌شود
🔹
منابع مطلع می‌گویند که آمریکا در حال آماده‌سازی اقدام نظامی علیه کوبا، بعد از ناموفق بودن سیاست تحریم‌ها است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/436543" target="_blank">📅 05:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از نحوۀ ازدواج‌‌شان
🔹
این خاطره پس از پیروزی انقلاب و در دوران ریاست‌جمهوری ایشان، در گنجینۀ تاریخ‌شفاهی مرکز اسناد انقلاب‌اسلامی به ثبت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436542" target="_blank">📅 04:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676233c80a.mp4?token=HorGVAY3TgadeudnMsST4KSQTthHjlmO0VcBe8XQunx9iBucRPmubBCa_2WpRUT0znk3L87uEVGfCipQIv_W-4zyR01QWCaH_HTnc5Zkkt_oDrj9RUEWj80cLP9LhqQLg7VIxb9Oj0fsjaotVSK8OWpvmPKBnE-ry-pNkYaPl1bh4eASfVvpAHqQGEMWuefyLqpM7ZKmrfsRTltO39il6D3G7L2yv1-h9tKuwVppjhyxiMoQj31FKOZJg7AYa9NUQyHlyG_r7iOorytC9jL-9qDrsWUVKQ5TuhGMXJYIeTehBHccyDnCiU0BDwnszk33cqENf-IHq1bg1lz3YLnhAgegQePuNbF9HG8FFuXXOLXbta1w6QSQJRrem_CbTldvaJN2pE4Mftvpde6n7lKJTVHoYWaSAgxsDWQ1kY_xSxcJZoKGH86J2FBrBNAnlcYWvm-C1EdUlMM2gH7WOLBtMVKNF8dbIbl8AC9mNj2XKe3Le0mIHgpYlE4oXLM2QFMaDxUCIwTZ6CM7g1c9C2NDhIIdok0OEeWBXn-KZEze78qBStJB8XwXP-hjzwlzgVXsKBL5NkSeYLPHMNjSbaEtFQBsbY9OIYvhNRIjR0HqQhXpdnC-GZH9j8rH35uY3NA1xX_y8Af2GwPaO7UjFNj4-gapAvIad8_4_CNGRMVGgMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676233c80a.mp4?token=HorGVAY3TgadeudnMsST4KSQTthHjlmO0VcBe8XQunx9iBucRPmubBCa_2WpRUT0znk3L87uEVGfCipQIv_W-4zyR01QWCaH_HTnc5Zkkt_oDrj9RUEWj80cLP9LhqQLg7VIxb9Oj0fsjaotVSK8OWpvmPKBnE-ry-pNkYaPl1bh4eASfVvpAHqQGEMWuefyLqpM7ZKmrfsRTltO39il6D3G7L2yv1-h9tKuwVppjhyxiMoQj31FKOZJg7AYa9NUQyHlyG_r7iOorytC9jL-9qDrsWUVKQ5TuhGMXJYIeTehBHccyDnCiU0BDwnszk33cqENf-IHq1bg1lz3YLnhAgegQePuNbF9HG8FFuXXOLXbta1w6QSQJRrem_CbTldvaJN2pE4Mftvpde6n7lKJTVHoYWaSAgxsDWQ1kY_xSxcJZoKGH86J2FBrBNAnlcYWvm-C1EdUlMM2gH7WOLBtMVKNF8dbIbl8AC9mNj2XKe3Le0mIHgpYlE4oXLM2QFMaDxUCIwTZ6CM7g1c9C2NDhIIdok0OEeWBXn-KZEze78qBStJB8XwXP-hjzwlzgVXsKBL5NkSeYLPHMNjSbaEtFQBsbY9OIYvhNRIjR0HqQhXpdnC-GZH9j8rH35uY3NA1xX_y8Af2GwPaO7UjFNj4-gapAvIad8_4_CNGRMVGgMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هفتادونهم مردم توکهور و هشت‌بندی استان هرمزگان در دفاع از ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436541" target="_blank">📅 04:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkXjBclBsNUIggpgNrsW4K1xqOBbiyd-iWTocgDSW_o0AcjXZzwVlwzgsu6a0tRshKzOSa2lrDFjSpqa3gwiNSo3H151KFXxIcHTxY7VqqHBmh6D87NWuPGKItEjZugqNDYdIcfNTyaXMwkhA7ltgLJVgGxIdwdB2PfGW9X0ybgt3-Z4Yklqal2x73UvP-F2BVpUSD24alteu9EU631blgI_LknVd19xYc6fDrxzsFeur-POBUfTPTd-1X8wLyf5hR99WjYVY9VqPvl3SGwBG0a-J8i5MjD27YosQ7RZPSGB5vn9Wfc9HSmhK-_jNM1WdgLqBS6doA7aSibkTJLicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2viyfBO9zKq_LvBttuShkNsDiEtAxGBbTNWHRHFXB1OiTsmQ0lmKKpl7S1a-pDwTMetPg4OflYPrxyDSbaFrZtBMa6bI4O6r9RHJaAVLfI6Ga8MLqQg4kYoHKq6ZM_ZTAW86lkbGPMjQkTkkEHp0YcEbpiCPEJj7fiQEf0kzDn8bIPpfVsfIjCpjnE929kIgZJHP0KQWkJTPOB7BnmCxVB0jr3EBnOTghZ38ZIU-TD9g32HNMJQaFuvojOo5cxKAKcDr1YQJ5hPkHabRkxMnw3lTwnuMtEf0ShM0qmPIsCx8yOCxfmNgoj6S3wAm5c0IIXXGSdgpFaDjcUb6VchNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTMgSOEdqOu_4icdscE78EU9DDTyJ--wClJBw00BrY6zQr3OKz_YtL2ktQ7djlxEmpQXQSxddgv8_PuBDYZwWO4Q9nAjmciFHpWLuEM9MPoPBrE7bh8iynGaAir5wlsuGG9A2RZlcG77hbFnl2CcIvS3xALSQdoV48h8Nb5idRVRhX1E78k0xCurc7J1NsOWtOfBr7NXZUA5qOCHdIUxn_EFTM08GXFaGyFtO2vjJXQ2hNyb5TA4A_P1rvL86eAHRUfO_93NrC1eIHtETGCkSmecCMDC_Eq2x85gLDWedTwdh6weoRMGbm9CbHvBNlFmb7wC02JxEvFkG8WUTeT0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Izl1eVSDwi1UOZXjrktyo_Z2fweRpVQ7AJgfjoCOoJ5uLuqQ2-Y8FFXCfs3mf2cXA-Pas_VZ04TH6hIN_dT8Xw3byuz1WpcE1XQ-m-0YqstsnXJbPFrZl--5DZ_r5QQlDVPmRwfeBMK7CctxJ14VUDrDXJ9-bFT4u4HvVdIbkWR_xLhkmINuN04mxkGWePvbaWHtv3znEvhfb_A1bbq9FjpWiH_P9Gz7-hmzj0fu474U_F5wm9a_lXAETwrMNDPZg2zt_yINoBP3e0NXMWkACkKWL0u-jNt3E57d9vQlFgbMJwlvNjCmHwAhF3vho5HLtaCM3C1w_eQFSC5m-Mkq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmUMMPwVb6YQJxnGJmSsLLNtjzWnb4Hva5d5ZP4b6v2350O6hfdCM-Ny-ExkkuW4mE2J0lwd_KUQRZs6T49K1PV9WsruLYjsnYmmuL-PWPUj1Nu92ipi24he5q0VXE9ctEBeFw38WLoNs0KUl8LIpP_NURPFuvt6vFlhxVEnuDouIlp0kG0m0clZ27l6JzII72fQik4FuZdgLwyRCdMua6YM2YLAur5D8-0XZmmyvIoXiqtDV7s8w6fjPNV2YDjHUGb4ibJnmMRgP3ka3Dboe-gNG7YwMwcNPh5nNHqzyb6Nlq76RtfxA6AF7EexsXTBtu0iWqz_ufZ8Apg4r6s_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJZpzTsz2sq3hFzFMwT7fE90a4GQRhJf-iD9sLii7_i_pteGBHNviUkrFVXGIdmPo-kwk7pk455wcl91ZqvBHWMgHeuxtDBRNRVDyX4K4auYVTxpIrDNHLQIFKOtg1D6-YBY1nvqyR13BSoTcY57609rjjm-UUy7j4rZovkS8ICjhV4oz3z1ayIMGDmC4et9IxeSkTsnMYyydnMDMnLH-dJnRyW_gncZIPjliA72lFWPoiUjzNjNTMkwg4yfhVjDNk9AVC6mfRx0l_OCinmnMaf0Rd3f85QG0RblJE-_OS0PF_VILdnq0c0pXKxj1DwvuUaw6PuV6_oGYIC9BTEVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikmj2MgPomfP9T055IUicS3VLG1v6s8Gl9_EyvlLbc6N941w7XjkyKww_cYP6t5IHVbkKC9VWBaiGFed7h6XsQQNkdCufREGsNGh9rwfW0zDPBlZSFlmwCcQtfDi6pn4c-UbHjuw2BzWFxBsSN4nEARqwR0XjCTrb90NpFkZ1yPFlxwRb7XanG7VcQoj68ywbYR5WKAwx_VJvXUaxKPHMpbQaKnK2rVa-Mb58qF0VtT1EpbnKUc8jluVvkQ0msvYiJa1vOXrudoFyQyDQXBAbctLL8RZT8hqeuURbxw22y8E1ogBPSL_wbvMyofqc1vM3bgyPUkx2WxpB9s8EFGMug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آغاز زندگی زوج‌های ارومیه‌ای در آغوش ایران
عکاس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/436534" target="_blank">📅 03:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g182Kglx2ER4tvI-9d-oL7a2W5jt5bE_nruHiswdkMLOCVzmUU9MXDKVw4euQxZPhDkw7FEOwlTqUQhRmpz5OQl8zQFebYKFqSm3jRAdTeIqHO63heZBZY9606kMZqsvM29xP3wfNI7i-UtZtIK8aPlD5ri-Ks_jjNvV5dSqD_rGYiQztLq8N7Jp5Q8d2yuMxNOlsYbcAnT2lKB8_NW86Uta18froZmXMjshHExTelkpHYhrNaszguEQALN8gQuv9Lq-sPh7k6UZIoOnALaTwexxXGhxehb_zB4kRUsfry6Jud4juzkWgUR6CB_a-NB6EDzUeO9wzMqiKn_eCx95mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز دادگاه تاریخی ایلان ماسک علیه مالک چت‌جی‌پی‌تی
🔹
به گفته رویترز، دادگاه رسیدگی به شکایت ایلان ماسک از سم آلتمن، مدیر شرکت اوپن‌ای‌آی رسماً آغاز شده و توجهات گسترده‌ای را به خود جلب کرده است.
🔹
در این پرونده، ماسک گفته که اوپن‌ای‌آی (شرکت مادر چت‌جی‌پی‌تی)…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/436533" target="_blank">📅 03:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KamxeNMqfTGOfgPIN8sv79tbnfMhhVPxjaUug8wjJVrjqTLCYrCC0_qy5XZXf4k1t-pHgszz-kY5bsrKQKti--ugUNVfkFe8eRXrZIl9m74L8qc4XoDnJMgqqnXwfQAQvHSKg4hEg7w-71_DzU3M7NacvFAz5C2BFg0WJRIkBcIB4_3krxFP6h06YJRia-_hQT8jo3NbxxmZhFWwuoX_rFTjVoZJNDZYyhlDa1QZtnh_VdAYCsghv0XV8HjI7jeXCTgksHEbDZPy19b968p04-XuFQ5uBBEXTlXi8hS4ed8B7AIsKAMMa7VpAktjwUOvHPHqWEu9nYPDb8-2qT7GhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: ترامپ هیچ گزینۀ نظامی مؤثری برای پایان دادن به بحران جنگ با ایران ندارد
🔹
برای ترامپ عاقلانه خواهد بود که توصیه‌های جنگ‌طلبان را نادیده بگیرد و به‌دنبال توافق با ایران باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/436532" target="_blank">📅 03:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPN6pf3O8erOcrjHOp7f1vaft3qc_orTG5Wun4cQuJrjB5vHoOU83xo-8xti0fmH_fDIX3o3xPhBlLRphJHSE76ldN-qVcuCfEucZJ4p7UPOhkQQUZ-rJ4tKV5yvoDAye6wWrHAVj9I30Z6mCmjzArYRWkmPkJjCKBJzTS64MFuwCKU4ZPSOPjBZxproynIPuqIweG1dWzkVU326gQZzyLMER9vcRRiTnSRFac3Fnrfz3wwQGWd2LpDXQ7SlVzJT0fnipDSo1_LZ1cxdkQrRPM6UijSJ2CLHUMeDPyVzq0t7SUKxvZ6CSy2Ju-7EAJhkGW2HDJQ8Fjm_62N93hkn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IK0GoA7nV8vBQY_WBHd_CsYvSHVaZJ5N5OYAAbVDInl73STO7yQfOi_tBK87BPcOEroEvz0ATu21Bz84Ch4HsnEiw645cCXKL2Jtc6r9oS0_t0FbH5q2JiZ0kiPKOfpYe_OuszQGOpn2YVXmg2NglJ-N0gdM16eJ4zi6UW3Z_X_9T8uAmHUVuVAPiD-s752bUaECYVFaIS0OfXnU8_UWF09pxnZ_vMoII4puHSnBMDmqjLJ4zejhEqvfxT8bKAZGGh55TGLfBODbhlRH708D0uRxq0XCGvMASGfjN4LPvB0M92D7y9-4VO06JO-YYIRH9pHjcDe7rWbJCeTJiI7qCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlGyEMkSpYX6j7PDR35YxExeHv86-Wd5G_mbNsGWLRWQqBpd26RnV8k_WXQH0DmWjsFAugUgsyjXtDQrdmqgKqMdOVfLI5HsZFm5PQ8L9lpShB-BLeqUxZqcNnr34pzwE9tDhcNJSI_rWbZfXWh6nBVW-XXxlVhl9j76tyqdv5TiLCYbAy6SvAHymOY9Es6gNh1e3YxuzzZe8yCa_uh3FW8Dvqa9sWn_XFwe5YU0L1UQ4OEA8e2NJo72DMv644-dGoQsb2Gp9gjsWb1N7FB0mIWJbe6d4zt33lxZexvBl4CfCeGw9BFPbGfk1Pl8BiRZWRMNNOjUG6Wmu2YgGPxFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0vt8JBQ55xaYPdP6F54sABRNiww509m6d8hmWSG-o75FsFl73FkS9ooH8anHb0pc-_r1U4uiUf_e0LokHw4K1xM7T39srw5sqvy-OGR0yCZQzTC1Fm1QsJx5H7o34EpBjo_6CBQDLY9-EgRFFzqUx7p_-qevsoaYowTCKScv0JHZ61mPGjJc2_ol_dxu2UnnNHVcfOuu407wEOHJ7CBxcONQDPzwXnGZb6Bj8yGb2GzDvkfceKXquZxcmD-8N03AzsHxc4EKWq3v1getZejA7VGfJnz_9neHEs33tTnXT5EEs_Au259p46Am8FfZBI14YFL8koKpmCiXR8h5BiiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDLCF-4ljy-QoJsW8Med7dGTCIEnTU9F44vw0G82tQLpWFrEIYxjDaEBYz8pFSoV_MAIfU0D0rPIuTpQQsSQgVsad-F6wFqeS2NjtizEWvSInEHbE0F77wFpuneupPmJKuHBKodHWKIYLXwnP4i4S_tmh0mZJ_OpnX1NxUflYlRD3IwubIMhtbhKWm5VHcwRZ9fgo8uHv6X1dWX7HwyTdXQhX8oS57hHLDgYHQcZmnBrW0tK9zwaB_Bii5CQ4dUqqXl492myfj3ry75TnFgFQ56Ggi4_Z9sbp2pngtiTSejcScixZBVvw39T_c4520o8_srpgK_LeOu4rZIG28nppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBVyYQpwsxovwM1w7i5xjcIwldm_bPCvqhW-ZboRRZ9QB41q4-RdjFcYhxZXOZ2A4dkMdjAMX28CzT4MrJ2LNTcE8dsRl6v-JDNQZ49LlDe-dEHnwcaF2f-U1qVynIwssfViWsKwbA-w3YjQRTM9UgQcjbCHrbnEggPBN3H932ovPfUWfpVrrZwEIWP5Bl8FkGQ4SCexk4G5ajJZu7O8qBOeCnViUb3NaI6WplTvaGptQgQaFwKSjFoTGPiyrchihLJXGjUAkOWTp5vP-N81rftvSgasGYa0zLoLYCWFjYourMF-4aIQj25nqttErGvinuGMVVpgC84DssC33tJXaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیوند ۵۰ زوج جان‌فدای کرجی در هفتادونهمین شب دفاع ملی
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/436526" target="_blank">📅 02:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8OBbvTHmOZALM1hiosgF6ZTP6JfuJljTD4FJGowA9deCU5hFowI_x6OkZEf1OsCsaZZtl0ExjfcuSoVm-k9Eul1ZxKSoegKCehZ8CML8w-tt0TVsr4Evv64rPocHqRcPVgodXkzd9sHjphH18qXY1mTPODjlKxw21mupJH8cpzsNUZinqrelN7PxoH9lTsTBGRY-tQKz2YJNiT53usnqLPXkC2KtAvypjG6RyvvFGM1yh075yDAuVAg3bhdw2kjKy-3HZOZX4RnH1DhaJLs_mswbDwwhHD2F4iweaNnxn9h2W7SwX5fAZmplDw0Dd0AVedsteQizZf65bhdjMxjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به یک توافق هسته‌ای با ایران رضایت داد
🔹
رئیس جمهور آمریکا گفت: اگر بتوانیم به توافقی برسیم که مانع از دستیابی ایران به سلاح هسته‌ای شود، از آن راضی خواهیم بود.
🔹
ترامپ در این‌باره افزود: ما در گذشته به دستیابی به توافق نزدیک شده بودیم و سپس این اتفاق نیافتاد، اما این‌بار متفاوت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436525" target="_blank">📅 02:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/forG8qhqK0RPO6zCdTDUzNyfyooLkLpjSK2I_3bPKBuyngP07t3eXXTGoNeLTTnGCwgaSsaul5qZ6h0I5_BrFLXSKK23Wuw4Dj-bMQdbf5wqTYcDW87305T7ibcagkbJrA14k1D4QY2MxhT17-WRXDIREwCxtVHdXTY8ZsiqOEkJcnnpfCvd3MXihVZuC-0qeaGZhkkPU5RkhBZoEhq7Hz5ZzQRC3eWXFEuA8AIk91eZnlOQvmYasH8arsBVP20BzVBCBsPv-WxxMbSg0WHuuO9rV_GQJHloI3WyT89Ny82QL3A21O6nP_NcDGtEb44_bl_2EBz0Um8ha5H2PfO-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس انرژی: ذخایر نفت جهان در حال اتمام است
🔹
رئیس آژانس بین‌المللی انرژی اعلام کرد که در سایۀ بسته‌ماندن تنگۀهرمز، ذخایر تجاری نفت در جهان بسیارسریع درحال کاهش است و تنها برای چند هفتۀ دیگر کفایت می‌کند.
🔹
فاتح بیرول گفت، قبل از اینکه آمریکا و اسرائیل حملات خود را علیه ایران آغاز کنند، مازاد بزرگی در بازار نفت وجود داشت و ذخایر تجاری بسیار بالا بود. اما جنگ به سرعت شرایط را تغییر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/436524" target="_blank">📅 02:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a8949187.mp4?token=c-mGnvBAMP16I9WBsgEiFhUuvZLwQbTokxL7GhEIglzB0-Gy_6h7Y6j8iGdyxulELXRpGrCKQQ_W4vMrrP3Fved3LaMcsa_HWEWunQnrKPEsJJ0EZKYyvw39cYc9TqFif11mkh0CQMQDOgWKGNT-Dn9d8gkMaXRxfWpSY4TPHMBJHZbyeRBrGVB3gbPU1SnhD4Hu25AEY1VEJjL7ZZTwZz7zAtVpZu0QNSk9ijZQIth9m_wF8ZgjSMoiHP2KwLjqSg3qeXoUxku-_gslaF0E9QhCV3VEIVVlR-04f3zmmJfgHG7n--3I9HAQM0ojwRZJsjLTxipnvYXXGil7mTANPWkxxfnJEOYu6e_ekGs36ns4f4j6dGVR7B5rUA_4RqUte5R1GYFsJfMrGM5u2Bt4Zb8MS0_ApzSeWVeTNV9DJEMUVHRs_HYIKQK8FyZI5MnkYYVHCH9rFQ24xo_8NT9DrC8vFe8RiVdcZAnyqfS0T1JMq4IITauRALKdLLqjQ58fF9-d1BC35PgVd55E5m3LPQ3sPKG160Bdv4cfd3T4aiJFr9TIYviUbWEr7bX-lBT83ot8dAhl6siqAwMFtwXVGnVuydpHpp-y6yUfbo_6msXMklMDNolk6ThvvbspUYzponKtYw1DxqqyKV1Jgi0RbY83PDB-x5KsrzHrHMnQIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a8949187.mp4?token=c-mGnvBAMP16I9WBsgEiFhUuvZLwQbTokxL7GhEIglzB0-Gy_6h7Y6j8iGdyxulELXRpGrCKQQ_W4vMrrP3Fved3LaMcsa_HWEWunQnrKPEsJJ0EZKYyvw39cYc9TqFif11mkh0CQMQDOgWKGNT-Dn9d8gkMaXRxfWpSY4TPHMBJHZbyeRBrGVB3gbPU1SnhD4Hu25AEY1VEJjL7ZZTwZz7zAtVpZu0QNSk9ijZQIth9m_wF8ZgjSMoiHP2KwLjqSg3qeXoUxku-_gslaF0E9QhCV3VEIVVlR-04f3zmmJfgHG7n--3I9HAQM0ojwRZJsjLTxipnvYXXGil7mTANPWkxxfnJEOYu6e_ekGs36ns4f4j6dGVR7B5rUA_4RqUte5R1GYFsJfMrGM5u2Bt4Zb8MS0_ApzSeWVeTNV9DJEMUVHRs_HYIKQK8FyZI5MnkYYVHCH9rFQ24xo_8NT9DrC8vFe8RiVdcZAnyqfS0T1JMq4IITauRALKdLLqjQ58fF9-d1BC35PgVd55E5m3LPQ3sPKG160Bdv4cfd3T4aiJFr9TIYviUbWEr7bX-lBT83ot8dAhl6siqAwMFtwXVGnVuydpHpp-y6yUfbo_6msXMklMDNolk6ThvvbspUYzponKtYw1DxqqyKV1Jgi0RbY83PDB-x5KsrzHrHMnQIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن ازدواج زوج‌های جان‌فدای نطنزی در میدانِ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/436523" target="_blank">📅 01:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=Xa4K4lzmOrL0w-Xpp4cysLsql9i9NZBu4tsMf6ozNYbaNAA0OL1yiBMZ5qw08AlkI6LTXCwVIZGmgsfECdWihAvhFrDi0WVI60kqNiXHz6IHQVikqWn_FglIuK_Xwa-y4yHT6AIvmhi09O9umUEvjNGOnYPuf26vX9FJBmYlRyevReqBGD6eYeOKFO4DXwfkEvoqsGd5rF8U1zvcs53qJUrr5tM4M2-LgfbqRFbizFNeYMOKUiVRxsKQAya8Sf7QM1oqYZtXdgEzc-23aQY8Ql0hiqJT7fbhiA8EKoj3M-E6zll2-XKKeD9lGfK5Rf26iX7O2ripfBSoNLQoHztKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=Xa4K4lzmOrL0w-Xpp4cysLsql9i9NZBu4tsMf6ozNYbaNAA0OL1yiBMZ5qw08AlkI6LTXCwVIZGmgsfECdWihAvhFrDi0WVI60kqNiXHz6IHQVikqWn_FglIuK_Xwa-y4yHT6AIvmhi09O9umUEvjNGOnYPuf26vX9FJBmYlRyevReqBGD6eYeOKFO4DXwfkEvoqsGd5rF8U1zvcs53qJUrr5tM4M2-LgfbqRFbizFNeYMOKUiVRxsKQAya8Sf7QM1oqYZtXdgEzc-23aQY8Ql0hiqJT7fbhiA8EKoj3M-E6zll2-XKKeD9lGfK5Rf26iX7O2ripfBSoNLQoHztKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
@Sportfars</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/436522" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
مردم کاشمر، ایستاده پای ایران
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/436521" target="_blank">📅 01:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceQf9_V2tHmSt3VZwZa_UxZxFUbJzWBpnsE3KJjULn8QlULJmWxJMGZNu9qtjNokerWZms3Y2MnG0ft9LL0wJlt_QeK3xlo9S4daFdowW8lZ9tzRNinJ65N6ohi7_JvDazyDGm32DkWI5ev7m5pcrD5s8cSeHQSy4I-EccqZaRFcZYw1Y5WFAbvRvNnCkwWZPnEoZi4m6g1i5w93XGVkYZUDI25rCthj81HpKxJJfefQMlBD-RG-2RaJMgUoeO7n4P3TCjCBModNFqe3wgpLEZnTJkNysvr3pbe90Fv6vxrtid6G3W10pqfQj2rEQrXQO2QYL2DaS66Bt2LRqr5rDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vq3jWKbA8R4zUMqTumOdXQl7iBgWZqsQjHXFopR91fE7-X9sS8c9nFj9LlqvdqaCWQcJNP5gVa9oqnwJlVajIKSxstpp64fxv_knYWffMwtGyP8g2DxfwCgneRNAdgjCgzOBhvGx5_AmvOfB2Qbd_zvgndJeHM4Km2F56a2FxLJGTqEptcHPgQ3cs8vAktlGtOVgUg3bEN6BpEYovFum9dU-AlIvce2vqhNA71hEP3SGVRZf8sz-tRVWm35Z_cT6GCfKVLLXX-kUPpTVI4Q2qFQ3aK3Rbd0P7N3NDk370iRw8lwY0xQ-vmqnEBymNi_bUkKOC-O0SswPrhydNqlV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crGpxaLlzSMLH805HUgTXVpSEWEXpsmWP-F31TJtU2jGDv64yIFjNCW5-1kxFuZ1jWJf-Hm9Xu5QfrSsDbBJq39db47KRJg_lOKQSNqj5L4U9PiL11UiF0aYO1ylbK6PA9yGM6dgDqozIZ91734vjsxA_-CwAitrO91U1kS0BTcnJ8qXllb5vpduEuOgUAKTmBQD81M21AMHDCr2unHb1l92ovauwXIfW7RCRIyFc98vnojV21ehK8ACuJxOS3nDmiuHXp2wt6rJH2VLsXJv6t322S89Hn-w5wik9hmCojsWOyxbFO46DgJDc8FJSDSxcHCsdWfWLjT8nAqZYj46JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9ZXqLyR-edjxRWfJCtg9KuU5NpDwAeVdRNPBpFoJRKxrzT9DBuUL4sVkCG8mLI4L1kPL8cAzeMO4SM0uZz-ZHGY0QumIuRQRJJ_p0neknucmTzNrggFgTMbZvVD6IY6YNbv1b_jEmD4m-DOAem_vV3ZLjCJDloXLPSPjddXnTAFlKOq5QovXmV6VKsRdpkLdFnFSu8fkKGNdPwOsDYpGByQQ4ZUNDCxp_mWkfXLHzicJC8skfwVlNFK183p3eK0Zo5R4_ELMD26aOQMCdYR0BPygWlhTT-DaYsRqrwx1AaEm9H-hYPCGBKHKheTHlU_DVIeVRngyFspJCicSukcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwgn0-xSVS3SVYuvigHQdTKI7BqRooLIrLQcndQ1BHZiPRqv_OmSmMB0W30AVTgP3ymIXv04Ib3dHBp8eRtTwXEQ_wa-6Q06vQpIUiImJj2bY_-HXqj1fWwsK_u3IzCXfdOvwMU3FEfE9KQTRVJW_n38A3DNFPo6BYyngyZTZABly7Mpnp66a3won7YpMghmHg17WseP94LcjeAjO3pRGsFrDMl7MOu7zHvuoKYKt2X0Z1GGqzl24MnsDqv5CQ6QoplpGaTc5cyZ3mirSyrk_uAQHccTrFkVSVf37lwa6gSM2JuxHOpGcCysa6XMC6XDUeP_3pbtu1SNYPAhKczYLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436516" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNnga1DirecvxXdNYauhxmmPNwOWwHgpdsjalECdKq0UClNPxk0_Hay4h1zP0rZP8TCcihPDD6O9aiGuMEgMIeJK8OUXnknOlU-M6PiQs0ZS2IZ88nBScJWyG3z7jnRIACYJrKlWpmgdHxtA4Yy1mxjwuIcO8LgvBxVmxSRJsNFmaAp8DyeFpv8uN4Ht3kT2ee41DPLtfZNtNFNLTE6_LGIM8okl-XhfsugE62nKP9OlPF6RRV0ayTDxE9euJXMw6K5Du9MP2RbYrWZgSYgOlppwCKFr7r5nZ_40OBA6zrPSbftSM2kZaKv3G5ncKSeXoSvgHhqKoXZMxdwPPFTrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW5bZbL5B1eLu--T8EL0dzZNQEXC6HKOqBW6xYcb7YXcgPQV5tGWD00ejJ3iYZl-FG7gBknuo2Q_15ms2eKZ1nvlpkzjkrp9SoI2ETFpp11yS2S103lyJUeH7mdGzedEP080jMfaWwSJIyDzjCIpKX_75BNbbAjHHH4EL3KYHs6ZIHLGcczWEPTTgPUQAXuhbFjpaBgacs7agKibyAlybHFllijOqZ4LQwuIMeZxVNiOSzd1WwLobKjJyf27jrTrmopSxiw7asRwIFd6oVJq0zsrr9KHBVZTiwaQti0J-PPcdGzm7ly_gMfrjaE_uIoW6v90Ji0hYmKknVVaplZ-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDf8-3s7BQ_gSeGnF2aAfvZPHpjORHW3qYODzZtwQCeDU6V5UCWUUKzA2H97PSOISoxNRSEzXSXxdDWduQO8QSGdk7fjw1UVbEUXBUCZCxm8EVwIZ3wP2zBX3Z-BK0J2JJ5dvzYIQLn6KiZc8o2OAR9sTUYMEYnZyoZIxgiVoMSg8QxZN5pW-6QmNhrT3hhT4hIpUPLEtMLgcg7L_T6Iew9s4aMQrOELdzREKYxN30SxXxE8FYp36n2oW3ktYFQFqL9a8qC_XaceQwTqs3d5Gae8v_f6WKZyBtqKQ_OsJoajRMWpxSzTt4YhAmZoX8f-HVShs4wHhBuKorMWAfUIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJKuKTrtMHYgUusDsvuJ-DtKACQ2N6QbsSfO-tOKfmAKP2nlzWVzfcwE7ubzMuNIP9czERwPJijRQ9XdnitwpjPKqo4_iB3hi8ASrSQ-k-pI1dWXKLzPbpG2uOTqmMPGhbyOW75KsFzRJfzXxDKrPE-wSiOrtHmKBuuqc7wA6hY3l4mUVAk40vgPLJWKFNKQQxe-mh_lfjNxzxoP_2Y0ooNzEZtDNvJLEGkviQFhxmT4Wzw8wmVWLkYaEn_RZw-cMgBOjXqCFSbyj8nWgSvId9rsb1kYUbXhd0DzsrFqtDLCSzYb76agfu2xYnyq_wMJnEYIBGeRUPOThqEWEKI6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTh4tlO1Gg3DOsaK3Hf4dTZDhA7nfOarPLidQDrrNQWOmHl_NT_zbxgW2veOw40l2UWH6hUzM-sknWEjP5xcjH3GJ92uLrdxoHZxD3_9fHY0R4W3xLG3cf6RnWaLJxiwJARgW7wsgX64O60res1WbGuineKEBH-FHDNPScKE551AeygYlIJhbgbs9iNwcU-o-YGi2zKE3Eh-75XP7gMAUnyao7eN2MsnQUVlHvpZXfK-SOa63xjZPk9yAQOIs9YiaKdOrX201JbaHY4wiPoSoi3jdtBojsNYD1S_6YcoyHaxFq5IY90Nity-XHpPc6t-Y3Mvw3uw2uiEABep1hnCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSpxwDU8d3qV1p0GHxk7FY-Xs2L3pcr0FaPiWr4Y_E7EOXfOulMTuKtQYsLkRh0MrVoHJydTW70Kkp5m6-u2UhFi6CRgJAOM8jWsAvAKQdC8u6JaAjWVQuW28voB7gQ-tVa49jbwcGOJAAU7Qv1csHPkEik5B_b99o8eleh70wGbDNC-Spz5SdOb7Iik145cwEPuA-hT809iQWio-W-nOtgrJBhuYs6fAdgjRKHKJDECa2EVN5RYv37H0-daTD3VNWzKWblXCDDf00690ogeEcHUhNBxirQTA3hQZ5g2G8ZcSu7COdMmLv_Q4giBwps4oV5s-ADEM4Zy5a2HBmNL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmxTVCAbjYE1fV-6zCZLAQPMK4Q4EG7MIEVmVK1hQpUl_a4ZbgctKGI2oc_NrTJ6H7WqI50ofX_ND9PQHFGXxzvQZFWeF97uVxhD0e_rAZ-w6tsvIjnvUAvIMx-FwR4hdho0cWnIbIcvBW5oRlKNVrY13iX6-B56GHGSnI-eWKRK0WeENC5_nPGBMFAHqAibe-3t_Ak01wRrIdWfu-qGqrSRjK6b6Tu225jcGxBkefUlf8a7l4VEY8sd-Hu8UHZPjqqvra8Gkls-kNBsADSQgMCbKHOT_csfv6QxZf19mYFm7yD5LFuXtExzmxqqfFgf_LHgNbPcaaYHm8GqBAyL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEHZHsjoiPNmi_Y34TOe2piV_mtU1U7vd63_mpHlsmL2hXyX_ipoz02FDMcmYgiv1noPDHsxNDPrVbgYkWx8nCOPjJqu6tj0QWTmq3RbFMvynLfM16BVg6O07HaUIS-55zeBjHWi9UEXK6i05GgYwqVSX79QknOgiWfsbmvwDdeJv0I8KtNUHJ3AWK-Sr8rhzMeDMgYyJY2wOZp-BV-PDOjtIAWrTwXpcaXWd2JCB6x9mSr_Ko4Pq6EuD_YyPn0LM_HaCwEaDDgKe0G0BuBUf31-sRIX9Hr1d7SG2s8sYu672561QRwzpP8sGfOZ0QhOdYZVdu0Obg1y2fwJHjlqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlcMIg2eIf7bHovXNLXoQXsw0WI6E_mjGUGRojJ7EgIBJnbtss1X-QgiKdMweH2lnaoZimZ7Dw41tHeGQc-eSX_qSjau0RfvuXretcSwZB5s4I6Lq_UovFaTbayOXMT0R1Y2AL_g71TAqOMxYUO15-sSuMXB03eFHfJt_wXYZxQaRbO9Fc8Lj8ri2ofDKbbLVc0HPj02vQCU_3yfz0JPJ3-3JLEPvKnaD720AfUwW-AtUC4cKVAjKFlSGWiPDYlJVmp6brN2aJ--fwnFaB0q-4S6Tv2O8L0E2IVjOnesT_dm7louek1yD9uQp5VVKbpHtKSfDqvJZvnIRDnW3QdUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z28k4nVd8nc8i1CMReupEBUxj7gIAxP2vg0tEcPv0qDkl00TFdOk5Bvj1ytTEEzCitl_rgJSA21x9EksmsaEhInHIz4zhP0Jq24tl4rkwX-B-BCU1BeibTyWhazW2S77oTxvmEK8lcgePggvamaPDfUzA9wiDAHZf3gcrmv1gLPh5zwLMXocxugOPTyihf1UT2bXyqcjaN-Iq3ZYdxCJEgsZJinyOrepTaKdKY_kLAi7FYXaXG_RWnI0rN-KPJfnB7aaFUcyhjc0BycArP77Y9r9J7dex-HPzTkB8MHq5WVP7uC8bWa7BeqObz2vCD8e5K55WH_bJn3vT9UezEE7wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/436506" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17fa4bf1.mp4?token=kTYSnICDB2rTsEZ6iGVbKM3o-NVOTuhGeyGtjqsqXa2yNB-8CVDP4L6hWx9swTmXwmkWr_u_xnBQFjoEfrdzApy-prnCgNGFB2y1WyJL2vlS4S02BS_k3Cokm_QhuPyC3YGlo8g-MmPIXYqrmuvvuzTZR1nIOvYKcmKwOXRrjjsKAHNVaLNjBsCoYfH9XRm7RkG7o08vh_NgTfroXdLZA1_P6d8N2f84BHMHWFpNYocOWZ84OhrtmiKLJ1Kmjd3LFUF8K8XLI2E9uL0NCjRzn0OHqWfr-UCxytLHPVHEoYbBC-Z2JXlAjrul03TnqnZeBxaN2U0p9SDdDQX26cVyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17fa4bf1.mp4?token=kTYSnICDB2rTsEZ6iGVbKM3o-NVOTuhGeyGtjqsqXa2yNB-8CVDP4L6hWx9swTmXwmkWr_u_xnBQFjoEfrdzApy-prnCgNGFB2y1WyJL2vlS4S02BS_k3Cokm_QhuPyC3YGlo8g-MmPIXYqrmuvvuzTZR1nIOvYKcmKwOXRrjjsKAHNVaLNjBsCoYfH9XRm7RkG7o08vh_NgTfroXdLZA1_P6d8N2f84BHMHWFpNYocOWZ84OhrtmiKLJ1Kmjd3LFUF8K8XLI2E9uL0NCjRzn0OHqWfr-UCxytLHPVHEoYbBC-Z2JXlAjrul03TnqnZeBxaN2U0p9SDdDQX26cVyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم. @Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436505" target="_blank">📅 01:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8a7plaX0Mx_fERz8tDRkocZpNfbjjB3PCSh2cwINN6i0-JDYMiDasVg-HWbXNVPT2nHCX3EMRf6nrFyuy1gBi0CHN26Mhzo239X-MHBeCaVJJkqE07p_wjfi4w2OzveWFtkf6kDpjQDBVPPeM_e8sU_oHZWZZ0ogj4sGSyiZsWv95YWBYlG68yENRE55iycQQtCVreTfNQ6_xb0AuXdKo2HWMg-e_2JqHmVy4FibbgVk4llz_4mlXQlrxzOCgH2OVwkLiKgEL5qLRWszghEXWKL4dJRxGhV8zHMYUpiTehL9dxls4W_qSliuKQeNJQbT5ZzgdOpFDltj5n_QAlgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم بازداشت وزیر صهیونیست توسط دادگاه لاهه
🔹
دادگاه کیفری بین‌المللی شامگاه دوشنبه حکم بازداشت «بتزلل اسموتریچ» وزیر دارایی رژیم صهیونیستی را به دلیل جنایات علیه بشریت، جنایات جنگی و جنایت نژادپرستی صادر کرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/436494" target="_blank">📅 01:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نظرسنجی نیویورک‌تایمز: جنگ با ایران ارزش هزینه‌هایش را نداشت
🔹
در نظرسنجی جدید نیویورک‌تایمز، اکثریت قاطع شهروندان آمریکایی تأکید کرده‌اند که جنگ با ایران به هزینه‌هایش نمی‌ارزید. این نظرسنجی همچنین نشان‌دهنده شکل‌گیری دیدگاهی بشدت بدبینانه میان آمریکایی‌ها نسبت به آینده اقتصادی کشورشان است.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/436493" target="_blank">📅 00:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qAo2DepbTJvTI1GNbiQrHM9ZUQcZ4Y8LY1F3953PG3n52Q2jEbi1JqXshjekEfEJBFFNO3Rr9iUEO01TAvo6FY4b6R7rE45lXMocgCHp_-tj0cQ9kpjAYhrQDlScQV7dH7DqmUuoY5gONCaUsD_ZtZgetMq6o4wqe0emaI6g7Qzc7j1XO-E_MmJWsC5B1ra6_j0nYXFaVgfcG59mSr_jJvkldB6tGW_g8fWfDXmLNjK9g5uCIYPLBjz2VPDmemWYNm6EgD9FHjR0lT4McusiEwk2Oz5bjhdd3zNDvEeaPskPd83kSJNB_1taBEQIm0jlpOrYjuMVxiFXsYMs99kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش بقائی به اتهام‌زنی صدراعظم آلمان علیه ایران دربارۀ انفجار در نزدیکی نیروگاه‌ هسته‌ای امارات
🔹
سخنگوی وزارت خارجه در شبکۀ اجتماعی ایکس خطاب به صدراعظم آلمان نوشت: ریاکاری وقتی آشکار می‌شود که حملۀ آشکار آمریکا و رژیم‌صهیونیستی به تأسیسات هسته‌ای ایران که تحت نظارت آژانس بین‌المللی انرژی اتمی است نه‌تنها محکوم نمی‌شود، بلکه عملاً توجیه هم می‌شود؛ اما دربارۀ حادثه‌ای که عملیات پرچم دروغین دشمنان صلح و وفاق منطقه بوده و حتی امارات نیز رسماً ایران را مسئول آن معرفی نکرده، ناگهان زبان «حقوق بین‌الملل» و «امنیت منطقه» به کار می‌افتد.
🔹
اگر حمله به تأسیسات هسته‌ای تهدیدی برای مردم منطقه است، این اصل باید برای همۀ کشورها یکسان باشد، نه فقط زمانی‌که مصالح سیاسی غرب اقتضا کند.
🔹
در ادبیات آلمانی، چنین «داوری گزینشی» یادآور «قاضی آدام» در نمایشنامۀ «کوزه شکسته» است؛ او همان قاضی‌ای است که خلاف‌کاری‌هایش باید قضاوت شود، اما با ظاهرسازی ادای مدافع عدالت درمی‌آورد!
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/436492" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZxTYvYhgeVhiCDtdkqbCXfZPWsy2PCq_kNlEDNN6X1Sai1y7xOpDng0welU8fDfei8tzQMGP4WXgb96u8GXTcRp0ff4bim6At1nndxIu-mZEpX0_6g0lbhX-0SbPKWVzHX2z5CunxSlgcXNw37wt-0SjFXAL-joBDegAVQKI1J_8JL_0cUkWsklhBeBI-IJ0Q3XYBRf6BZY1IxT1sDvnsFrnf4L2rjmtXwrs82Tx0ZSKcOOybKVM9eaTcJYOXYXbUFTwUzSgS4n6o7rQYVeqOYCNz7e9Rk3B7d9p9h5gOCxPxZW3DNGFSsoHgNx-jna14UGCSdo7A8YYYAuKGeCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جای خالی این جدول را پر کنید
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436491" target="_blank">📅 00:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فرمانده قرارگاه مرکزی خاتم‌الانبیاء: دست هر متجاوزی را قطع می‌کنیم
🔹
به آمریکا و هم‌پیمانان آن اعلام می‌کنیم دوباره مرتکب اشتباه راهبردی و خطای محاسباتی نشوند.
🔹
​آن‌ها باید بدانند ایران اسلامی و نیروهای مسلح آن نسبت به گذشته آماده‌تر و قوی‌تر، دست بر ماشه هستند و هرگونه تعرض و تجاوز مجددی از سوی دشمنان سرزمین و ملت سربلند را سریع، قاطع، پرقدرت و گسترده پاسخ خواهند داد.
🔹
​دشمنان آمریکایی-صهیونیستی بارها ملت شجاع ایران و نیروهای مسلح مقتدر آن را آزموده‌اند.
🔹
​ما با عزم و ارادهٔ الهی ثابت کرده‌ایم که اقتدار و توانایی خود را در میدان عمل به دشمنان نشان می‌دهیم.
🔹
چنانچه خطای دیگری از سوی دشمنانمان سر بزند با قدرت و توانایی به مراتب بالاتر از جنگ تحمیلی رمضان با آن برخورد خواهیم نمود و با تمام توان از حقوق ملت ایران دفاع می‌کنیم و دست هر متجاوزی را قطع می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/436490" target="_blank">📅 00:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436489">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jha-wZJewL39XHx6cL6Q9MqNgJ5OONNdwhtJOCOv7Qhsn7Y0vAfBm__nD2Bsch313deOFuNxZVkpCJCzCHoL_l_CqMQ-CD4-fJR71EUAi1x9rWY1ERu_nYgjZmXuD7sUEUC5KXM1gtGaVksuszAabu6YSkoKeDaKC56AGGU7pTPF-rFCdRke5y1tOkKWWBh3D8WkITtuzidkXZ3rPPtTN4bQOzmqj-zi84RapetW5SDJ3UYaqlP4V0r4XfvURErK1gJlUKtnZa4U1RES0WNfEQKuQ701H2DK8wlNzf0AUHxdbU23xihA7M8aWje5i2ba46Ynw26abLgIghNJsVRT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۳۰ میلیونی ازدواج برای دانشجویان
🔹
مدیرعامل صندوق قرض‌الحسنۀ جهاددانشگاهی از ارائۀ تسهیلات ازدواج ۳۰ میلیون تومانی به دانشجویان خبر داد.
🔹
چنانچه زوجین هردو دانشجو باشند می‌توانند به‌صورت جداگانه آن‌را دریافت کنند، که مجموع مبلغ تسهیلات به ۶۰ میلیون تومان برای زوجین می‌رسد.
🔹
ثبت‌نام این طرح، از ۲۸ اردیبهشت آغاز و تا عید غدیر ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/436489" target="_blank">📅 00:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436488">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjjPu0xc74wKSZ0_oaPcbmw5KVsNI5jz7Kr0oEsy9tPXV7-FBlu_P-Idauxw2JgAoGNALRRqWrHjRJwXqZGC8xHbci6NU7BNKdKCFdeFv1IqRhu1kLC0rarkVGGKlpYqobdxje7stmivB3at8r6Mk2Dhac3mq6_y-TDAxuwT6Da2oTyqx3xmmU591N235vRGb7-JwO_9UuXaKv21QpBAm8Ghtf9ZluadtOavMC7Wv4RIEONneHcQpogB0-ufnw7CXap3ysQ1bg0vU-WDf-HZPb-XicJD8MPZHzUzIlp1ktRJDssaI5btxO2MgIm8HETzCmmOhZmegGb15pWV3TmfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش محسن رضایی به عقب‌نشینی ترامپ
🔹
‏ضرب‌الاجل حملۀ نظامی تعیین می‌کند و خودش هم آن را لغو می‌کند! با این امید واهی که ملت و مسئولان ایران را تسلیم کند!
🔹
مشت آهنین نیروهای‌مسلح قدرتمند و ملت بزرگ ایران آن‌ها را وادار به عقب‌نشینی و تسلیم خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/436488" target="_blank">📅 00:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436487">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7dakqG7IkXbTz4rP2bYvcA5KgT5t2vNxIHD5tAMitR8VjkPwh4xW6HRw4HFZfjpmvVtR9mSMcI2TyadSa6eSU30_CA6dyvCurHthGlsmroO9JRkgj5WXqOssEoGdzZigf5IjIfnqj-ZamP8-BNlhdoRi3pTf2ijYc48iM7VKECNDPOBBqalfLN6-unkT1adRWvZOtiZePddX7qhQi9tVJlbBIvWeUJkqXaXpCcRC72gg_sxv83ZB6MiG9jYB9lnoFpAuOt5-6EP1ZOu3WX4c2jf7zKkMjjTHEdODrIEQ1vgFxaE0nL6i3wG2171wz4YaYhGcR675J_97NA31j2KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشورت با ترس!
🔹
نقل است که یکی از ژنرال‌های برجستهٔ روم باستان، پیش از آغاز نبردی سرنوشت‌ساز، در چادر فرماندهی خود مشغول بررسی نقشه‌های جنگی بود.
🔹
یکی از افسران جوان و وفادار او، درحالی‌که آثار نگرانی در چهره‌اش هویدا بود، نزد او آمد و از خطراتِ احتمالی سخن گفت.
🔹
افسر جوان در نهایت گفت: «ژنرال من می‌ترسم که...»
🔹
ژنرال صحبت او را قطع کرد و با نگاهی نافذ گفت: «هرگز با ترس‌هایتان مشورت نکنید!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/436487" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
۷۹ شب ایستادگی برای وطن در دامغان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/436486" target="_blank">📅 23:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e40f06d8f.mp4?token=fdGoANOrpWV8dVx1Bk8BbUU9713H-7eEBsm5moQFoIlv2eKp9MsZo1gNBgkP6A-chj0cYKU9nfK8zw6ys_2aluRlDxxynasyAUZssqL8ghodn96bm7K7WPHAD9wAaphHMkgx6iRGAkddkS6ckuzE9kMoRo1MVKh83U6bVy6jC8pJE4-1-fG3qtY_-68OK0jYaL28YnVkWBEgG_I5XWNc_w0xWyV1nIyKiSauhmU0AlUyYgQD_GyIEjhw2Wo-F6Tt7oT79MMJi-GosQkHxx8JCzclYG4HAxsaNsPQWSMzZNyXoz5yiir8CpnSTTuvoYxkuWTA26BldiohrCXb5EvnpZ_ZBeObkCr5ojWsh0krtkrYP9O9O4B9AZojb6rNw1kCie2ojoUNr56stj-_QQeMtYvKMs1XMJAAaTzoQwVaThxpR7wEWFjnpW5l-zDbfw8nSYuuDwBksH12p1PX-cua4fANYD9Zjp7kfend615ul_oiOmzSiTTanu0uypTYn8_YyUENMqeTXQyFjrhA9Ja6mICw0PPQT2AcTw6DRBlazPEQEe5pxSuICPvdkMsbI1IZZ7SJgVTkSE_YbDXfQCc9nDXVUXN_SOko1MzFtFlA75AHQzpqvVEexhEw1-Zh12FLdvvT7mD2s47p4paHo2ltMfMbT_haBE5bUFpvl6nKI7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e40f06d8f.mp4?token=fdGoANOrpWV8dVx1Bk8BbUU9713H-7eEBsm5moQFoIlv2eKp9MsZo1gNBgkP6A-chj0cYKU9nfK8zw6ys_2aluRlDxxynasyAUZssqL8ghodn96bm7K7WPHAD9wAaphHMkgx6iRGAkddkS6ckuzE9kMoRo1MVKh83U6bVy6jC8pJE4-1-fG3qtY_-68OK0jYaL28YnVkWBEgG_I5XWNc_w0xWyV1nIyKiSauhmU0AlUyYgQD_GyIEjhw2Wo-F6Tt7oT79MMJi-GosQkHxx8JCzclYG4HAxsaNsPQWSMzZNyXoz5yiir8CpnSTTuvoYxkuWTA26BldiohrCXb5EvnpZ_ZBeObkCr5ojWsh0krtkrYP9O9O4B9AZojb6rNw1kCie2ojoUNr56stj-_QQeMtYvKMs1XMJAAaTzoQwVaThxpR7wEWFjnpW5l-zDbfw8nSYuuDwBksH12p1PX-cua4fANYD9Zjp7kfend615ul_oiOmzSiTTanu0uypTYn8_YyUENMqeTXQyFjrhA9Ja6mICw0PPQT2AcTw6DRBlazPEQEe5pxSuICPvdkMsbI1IZZ7SJgVTkSE_YbDXfQCc9nDXVUXN_SOko1MzFtFlA75AHQzpqvVEexhEw1-Zh12FLdvvT7mD2s47p4paHo2ltMfMbT_haBE5bUFpvl6nKI7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواسته نهایی آمریکایی‌ها از ایران چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/436485" target="_blank">📅 23:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac42e5865.mp4?token=Krzk6USlqP5spmrWlucwoiiqJAW5eeiOkIzMwl7E56F6Mj0ObLba1QmlTlm84XIjfFzC2O2obe9wA4mHNX9xE2AtaD6jSuCYUYuoxPkKBEK64Zg4HWuhEnzKugKDXhgElfjRXSjPEhdtqRpsMu93YneBT9oSC-0udh2ZXoNTHZGgkiuiCqpIPIsaKNnREs2s-3dvhltI_Bw80qkyXusAKkDPCf1pZnCpfoWQoNuC0LfBShXwbxIcC2NutCZf7XbAVdDzbazrjYcyD5QAQipgvYYodcV-jq_fIWz-SeveMdxcKwiMfU6ZFjJxXLW2NgdscVwb67la7EYK54NTLpwkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac42e5865.mp4?token=Krzk6USlqP5spmrWlucwoiiqJAW5eeiOkIzMwl7E56F6Mj0ObLba1QmlTlm84XIjfFzC2O2obe9wA4mHNX9xE2AtaD6jSuCYUYuoxPkKBEK64Zg4HWuhEnzKugKDXhgElfjRXSjPEhdtqRpsMu93YneBT9oSC-0udh2ZXoNTHZGgkiuiCqpIPIsaKNnREs2s-3dvhltI_Bw80qkyXusAKkDPCf1pZnCpfoWQoNuC0LfBShXwbxIcC2NutCZf7XbAVdDzbazrjYcyD5QAQipgvYYodcV-jq_fIWz-SeveMdxcKwiMfU6ZFjJxXLW2NgdscVwb67la7EYK54NTLpwkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در یک مرکز اسلامی در آمریکا
🔹
رسانه‌ها از حضور یک فرد مسلح و تیراندازی در مرکز اسلامی سن دیگو خبر می‌دهند.
🔹
هنوز آماری از تعداد مظنون‌ها و تلفات منتشر نشده، اما رسانه‌ها از زخمی شدن چند نفر و مرگ دو تن از جمله یک نیروی پلیس خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/436484" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3a055d3ef.mp4?token=BmOxkAfe0HkS9uLOlNfBScJLLJGGtGhwHZF_yNRzpbgfRfxwe61lPea5nQ3MRyVibT_FWVxgF5Z4Sx3z_G78ETksnCHr50Ex4uNomGWq9A6CyWSoOVMBsEM36R2vqVTtEDgAYVNpMI4y90-jHYjjTgw6dxijy9IoYt3oX3Hm-4b1oo7GlD6JgvvmVIBnIdKp7VuP352wQsQGF_sAytghn-tCr7NsmRzVgfb-A1e0wQgWQmrJ6TXSrkZzsLJbLB41cvNklDdhhr2qcnnuY01qCEwKnzl4_7uzv3Qfeq6J3l8qj8HEJwo18UWvpXIAS375YBpepBhyptsxLgfryDNHFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3a055d3ef.mp4?token=BmOxkAfe0HkS9uLOlNfBScJLLJGGtGhwHZF_yNRzpbgfRfxwe61lPea5nQ3MRyVibT_FWVxgF5Z4Sx3z_G78ETksnCHr50Ex4uNomGWq9A6CyWSoOVMBsEM36R2vqVTtEDgAYVNpMI4y90-jHYjjTgw6dxijy9IoYt3oX3Hm-4b1oo7GlD6JgvvmVIBnIdKp7VuP352wQsQGF_sAytghn-tCr7NsmRzVgfb-A1e0wQgWQmrJ6TXSrkZzsLJbLB41cvNklDdhhr2qcnnuY01qCEwKnzl4_7uzv3Qfeq6J3l8qj8HEJwo18UWvpXIAS375YBpepBhyptsxLgfryDNHFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاش یک بار از نزدیک می‌دیدمش!
🔹
کرمانی‌ها از یک حسرت برای خود سخن می‌گویند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/436483" target="_blank">📅 23:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37df6fe12a.mp4?token=ZODvEHy-6ENERezR7QeGLHs3vcyJVW6tpmAMqFv95ew9cy3aRkzniSSvqHGLAa5JTIMWZsf3au6eTC-w1W0ElqIpQdpV6XfX9gHGmD2y--3yxHgwWJ1MzYwkuV5lGoDeRiNz5klqKwPLGtU6KDWSjkuAfz13OX40G4gHFbLXIrzTbhISIWpwo_e4wPAK4XH1dOAaRsRT5E_GDyq3dGw3WwNPZRTGfSkhQrHqQishejAQkoAFEQGwLgvYw5gmlBZ4-vrDjIXUg0UueLISfWinMH3wD8pPcL1VvMYZTk86MvAblKhV1Y1gkvdjBZKyZxQYPeRcV_UUoKTp1kyV3BNanlpJzoCHJyoWjFoACNPFsgYZtv6YUlL6DaLXhlerX-7eIJGdUJ3JGcvIUHdxj5o5xkRR98C9zj6Va5pMUn4N-t7vlsUaa2sLha2wL-lU1_0ICErwGbJpsjqm4S1-UqzwwLzVI5fwCn1jiM9a238kCKNgUyPwXeXQNTzIxCRUK79Y4M49Z0SJ2bWYpdVVszqiAD7n3vNVg92u0DRg3LsSxxyZ4AoGuMnrpFnf9dEi_8hmuk8Uw79sGh0M8fZUn_sHxo7-9Cl1Drj9rShXm44QDtCLd0hrr866ZScWLtM39-z5p5TtDV5o7DecZWEwYUD1YjBhZ1JMhIR3jVig38VLb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37df6fe12a.mp4?token=ZODvEHy-6ENERezR7QeGLHs3vcyJVW6tpmAMqFv95ew9cy3aRkzniSSvqHGLAa5JTIMWZsf3au6eTC-w1W0ElqIpQdpV6XfX9gHGmD2y--3yxHgwWJ1MzYwkuV5lGoDeRiNz5klqKwPLGtU6KDWSjkuAfz13OX40G4gHFbLXIrzTbhISIWpwo_e4wPAK4XH1dOAaRsRT5E_GDyq3dGw3WwNPZRTGfSkhQrHqQishejAQkoAFEQGwLgvYw5gmlBZ4-vrDjIXUg0UueLISfWinMH3wD8pPcL1VvMYZTk86MvAblKhV1Y1gkvdjBZKyZxQYPeRcV_UUoKTp1kyV3BNanlpJzoCHJyoWjFoACNPFsgYZtv6YUlL6DaLXhlerX-7eIJGdUJ3JGcvIUHdxj5o5xkRR98C9zj6Va5pMUn4N-t7vlsUaa2sLha2wL-lU1_0ICErwGbJpsjqm4S1-UqzwwLzVI5fwCn1jiM9a238kCKNgUyPwXeXQNTzIxCRUK79Y4M49Z0SJ2bWYpdVVszqiAD7n3vNVg92u0DRg3LsSxxyZ4AoGuMnrpFnf9dEi_8hmuk8Uw79sGh0M8fZUn_sHxo7-9Cl1Drj9rShXm44QDtCLd0hrr866ZScWLtM39-z5p5TtDV5o7DecZWEwYUD1YjBhZ1JMhIR3jVig38VLb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن‌ ازدواج ۵ زوج مشهدی در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/436482" target="_blank">📅 23:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436481">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b0db00c1.mp4?token=Acx8ygmhB-vpHyiZjE6SNV4byHH-DPR1kHhAEb3ltGMN_vSRvhMjyPnR2faC9Pud0CqJTzxCayQPl5T13U3J7G3IlxDChdj79EdUhE2MA4bKRao3TSBDntQQtEZMvbo_AVwXOs6r4HZnn8Y11C5N8-SZD-cCvGLY2z1bdq7oRg4nbfzjs2RlswWSbdM7nFUa_YSOB9fyj-_kDh2O0GBLUcuClU4bcS1XikTuklD_SmNQ3ZQrnsF5JQF4WW-negia7-O5XZ-uSAcL2Gw3jGCtCyI1EhdalixvJWRVf2SDy9fs8Sttll0R-7jIpolmXmrLiBwjR6DWwYBBbNmfUwCUTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b0db00c1.mp4?token=Acx8ygmhB-vpHyiZjE6SNV4byHH-DPR1kHhAEb3ltGMN_vSRvhMjyPnR2faC9Pud0CqJTzxCayQPl5T13U3J7G3IlxDChdj79EdUhE2MA4bKRao3TSBDntQQtEZMvbo_AVwXOs6r4HZnn8Y11C5N8-SZD-cCvGLY2z1bdq7oRg4nbfzjs2RlswWSbdM7nFUa_YSOB9fyj-_kDh2O0GBLUcuClU4bcS1XikTuklD_SmNQ3ZQrnsF5JQF4WW-negia7-O5XZ-uSAcL2Gw3jGCtCyI1EhdalixvJWRVf2SDy9fs8Sttll0R-7jIpolmXmrLiBwjR6DWwYBBbNmfUwCUTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان عالی‌رتبه معتقدند که باید در مقابل محاصره نظامی آمریکا، پاسخ نظامی بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/436481" target="_blank">📅 23:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436480">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
حمله پهپادی به تروریست‌ها در شمال عراق
🔹
رسانه‌های عراقی گزارش دادند مقر گروهک‌های ضدایرانی در استان سلیمانیه عراق با چندین فروند پهپاد مورد حمله قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/436480" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436479">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb4adda89.mp4?token=qryLRBBeM1ZFA-fZR1HEeCcDqLy6L3-Y7GnxQP9SedXJ4bjEwGfGxUwHJStfGJHKPykVkwlwkX88nw5qxui9GoMnKO9i00JLSAQE6KS2AHwc7HZ7jvyuhWoytsADSml-_3tE8g-C0KehhSYEQIZZMbsWk7tNq5dys6CZ1bHehm6eTvH4xcVfSGWnjBQ-3j8_WAF_AuS1bN_MhQFsCjKagpmhIQICPni8ZC6d3RqjLOIsbrJfaJB9hcmEFQnhchLkDEBeSKin0jn5PMFFkln1sGco5iY07HtRSCNlooT_t9YsWJ1Y8SvKV9ddZbGxehDUh6G2IVJVo70GRDJMtiLuJzFHqZ_b3zaPH8QDqPu1OCN41FxW7--IiqBCocMboX2G7O9q3CJ4vCxyyO8KdYrDVuwYspQI7SD31yjEQ0h6mzF9XZSW6I4GuvP_P5kDLeL18E8jMzUUfYowfxlVwzRslBUt_mU6mwGQZQHhGYALf6zzkHbH_qKBukkgsCRJ3dvUTChVbWC91bWEupHevAnywqEOH48zJLMisF41rJtIITW89LTbsbLbYlanLsftq97F_YLFMFOjVYER8wYhBd10sUSrx8_Xl-rqVMSKDwPh2Y6zlVOE7woaQ27_k-u3HyJOhtUW2EqhizHqIw845FgE6aI8dGke_P9nDz3Z71nCwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb4adda89.mp4?token=qryLRBBeM1ZFA-fZR1HEeCcDqLy6L3-Y7GnxQP9SedXJ4bjEwGfGxUwHJStfGJHKPykVkwlwkX88nw5qxui9GoMnKO9i00JLSAQE6KS2AHwc7HZ7jvyuhWoytsADSml-_3tE8g-C0KehhSYEQIZZMbsWk7tNq5dys6CZ1bHehm6eTvH4xcVfSGWnjBQ-3j8_WAF_AuS1bN_MhQFsCjKagpmhIQICPni8ZC6d3RqjLOIsbrJfaJB9hcmEFQnhchLkDEBeSKin0jn5PMFFkln1sGco5iY07HtRSCNlooT_t9YsWJ1Y8SvKV9ddZbGxehDUh6G2IVJVo70GRDJMtiLuJzFHqZ_b3zaPH8QDqPu1OCN41FxW7--IiqBCocMboX2G7O9q3CJ4vCxyyO8KdYrDVuwYspQI7SD31yjEQ0h6mzF9XZSW6I4GuvP_P5kDLeL18E8jMzUUfYowfxlVwzRslBUt_mU6mwGQZQHhGYALf6zzkHbH_qKBukkgsCRJ3dvUTChVbWC91bWEupHevAnywqEOH48zJLMisF41rJtIITW89LTbsbLbYlanLsftq97F_YLFMFOjVYER8wYhBd10sUSrx8_Xl-rqVMSKDwPh2Y6zlVOE7woaQ27_k-u3HyJOhtUW2EqhizHqIw845FgE6aI8dGke_P9nDz3Z71nCwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور شیرازی‌ها در شب هفتادونهم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/436479" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPfnjAQcSHXF13k-3XdAe0oKQ_ZatqhmXrM3qqAe1MiTJ74-vQQo2h-rDBZjTnwosPtH3gLzJRK2u-qOwsoWpy7t1KuRq1s0YtvI63XToAYO3Cg985o_JGYrfiS6Rc040ItGYdnL4fCLlR9kLjTOGlUIiUhMp8eedPsy0UTjXzRVTqzFoZEVf4hr86ei2rPvPRmNaw1ILWKBNZgOZwccbRwaFOUukAc55c5x23uJd_L-XvZ9GcDRERwn9GCl18ZR2oY3x2TmP4XbZvvz-SobXg9E2v7AWM3HJRa6kuI-TZMe4jncPUMiK3JgwjM_w1olsbZd-xn07JexZuw8dcBk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hloIZKz-4EqgL4NnV4pyAwmNwVWFOgn8hZeI39bcPH7fw8W5otUAD8RmGrOYmu5ThVOiFATYU4rsVbdqoV0NUpjbxVPxakQzpXEDcbuUv7QWHrcD1PQtklR13K-XXkjGQOdTqy15iUDxf8p0XidytbmjwZF_QK3AwJUuKeLryveWBPiuYLtNCDQdHn3UX7aamXwtJElgDDxdlOxVzo1AmsHO35bUU9zfKqMMh6vraDz2hMELCzkNlPYZR_nKA44L3UQSVBW4oacyxvFCXDwjGcmabO9TEJmHGTiQOCPpQwFAumyL0zs9Kiqhy-DzF1RGBedpTvSDmQFeT8f_QvkhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhDbEhI4u3gNKB1ltXc_tktd4BZcE1UA2BGBTcqrX_5vlFCQHXW9FPV4E3JIEyydbGPJCIbCGMOo3yRMkw3p9cZXRE8qzigJ9clgfBzoAeqjzwAblckVjoZ6vakZaaW9HBr9YGIhThG30PtKZaKOTKHgM6xfV3MzPcArgG3kx-kXZWGxTFcR9Iw4qEJqHAAt-i_uxNTZ91PhPTot_wP-DfDs9KyZAG6nneVVZiGUV5Krb9UQ1v0uKY91XOh1uQWeRlg8Mm1qJyHlVEJj-OMt5VOdTMlJ5CFdKsdTi51Y0FTJ9-DMhfyERpza4w7Bt9FEwJK5JujVYE_tC6lRFXdI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p06EeBQO1-DHq8OREw4viBZ_PZL9BPAZKTqt1Tnp1Z9xJ2wgk5TceyV-00kD3YqvAFmVi4mx79rds05OJi-UMl-PWinFX-H3fM1Glr5ELpvpRKRf4ykbJSPGIjmYHkJIv_Yvfrn0Dco8lOTLBsqeBasGoEsfzSSzMksRZt_wh1fbf5qGzJ53KBZrKKFYUS16QC9Z_zQvtLCjlRm9E1zOuOcGvLIG6sfDwY_CN5CT4pGmNDKf_YWmA4hJZaRTUxLo5kcPg5wu9HLwG1sF4_tniJIKEJn7soerOeDhjCxUlLSPwje2HzPO4BCpwwzmjz5-JsjX-o0LXfLTDrEFgV1SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAed2Ned5PPttg6Puqkjnwwxz2AcDtDBr27psI6XzfIcFKpzNu1jM_XgF0uteKmRszT63IgG9Xt4w1uGamxyvqo1uHuj_mCVPfAcr1fQq_g2_AsASeTDXwRUIB7ogxynY4BZXrp5BM4VQT9mIP8r6RGnEDaJcKUm0hiVrNldfL6GROjgRKsJBrPiQiays3OjHBm-olrYeye-zj4_vd72-GAKr5QiZENyMW_BfmMQ39mxwlNYbkLfJS2yd4xVj-ct6DclVjlBFaolt-dWh_Wo-Ju2rX3QpJR0k4HzLWPsBPL6TZsEkTEDDPjep3_4qesTz_hY4MMu6VRhFG8BA-Gbzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHv5sM36inekRjkQmEQsGQXeXoomCmopN54_NFt5d14GHVQ7YkwNtpkhIWlh0QbBGFEH68kXBnzEkhxaknCphtg7kuNh6CyDaSadJ1c4XKvZuyfi9g2pL89boVNn7ZNnPXnIIm594auCT8uf5kJ1_fa2Kl3b2BLUMAR2-A_S7XwLvFJy4bDEcbD7HDTX2TuYunqjWem8amBpv6AnR1A3HFfqG62RUBBgP4KngjcQpONdM0_WOJWf6ooYE4jl2x7Sv1HoTXq-oFv8vyAPPJXqKkZFfwP1wDCA2Ir9Q-DWZU5_iaevtHTZkw154fyOItkXUSCJPDaQ-fLKtpSHD8RplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCMSGIonoM9O23TDuGzjkARIILPNbay4_FvW1-XSYdu6MVbAxfPdOOoETCJWHPts2JlPFpyCZiyGAWk9L-kAGT89VEu3B7VyJ22ud_WrhJOFDe9Td8el_bnflmEIWACmRiAszxCQB7m52SE-QjMLAARGj6Q6hHqLsD-u_5_IBj6c3-35LRuNssrEpthWTC77AkHX8Yinp_DJFMoNrqEkkQxdJvqs810vTCetkgWZnK0BKybHMTqxs0ORUZruwsbgTGuThIGjpJ6JXeVZPlj-Z8tkRcdFYn-hICOfTfrKxgCg8S3gfY5c7G3Z9-K7d82conhEneuraWoZ1I0LmYWxmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کاروان ازدواج دانشجویی در خیابان‌های همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/436472" target="_blank">📅 23:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRcpOs5p4QxaF43JLiAXSImPQeaejVhyvQ52w1yi_4v5IGydUmhf3W4OMcu2ay7-Gc-lQhM24YusOruCWLVVUzUGCLfSiszgVN0U50TdW3sdk-STCDU9ZIzdKXXeXawmTNtj8ndv87FzqoAmEGisxxMH6DDiH9wlfqqsKIgNUUFC4M6H11pgeuMBiPXo-FTezGjeKAUJLWM8tavn244G-yDmsuiA0ujpy5cgfd5Pk0z2U7YdAn0BX8NDr4OmJMS0qBsVqX-_uIaM2xTY-cIeU_HYoQ3te_Id8tgOgjfYLhctv1dci_vEG0z1_buyu-NkpjD2QxgiE-etOiKzhPhzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PA5J3ljdPJrX98YZQu1Ekfc-HnGjLMNxK5b7qOihFS2fAHVmUC_ttbX3o1XFtTIR7uXu9DvNXENYTm-SBrjUJElbNJxRKZSMIuMZ9RNx1UVnDzSuuynnJpApBtchJSGJSVoX-6WeMXga0s0snM3-L5Zm57seUyWr-cP7dIZk3pA3Z_ABHL__s1zWvVn2n2ucrL5du6gFG5cv8xabtjJf7tHzY7FOAaStrZN5eQJIFLra8zYWjFpkik5rtmwT_rLEKItoDSFlcOgBUNqVc77fOKhk0eXSdOom2_f3BlUNJe0HQopEgRfiNmTJY4Pra9dWFbLHR1MYQEd5-zHr6Wz-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6Yb1-F5B5z89RI4iwUR9cXXW3b_REbf1WkSz3z4r89bXVsyW4UCtDbhZssv5kJuYQBGtIuJAa7Lkd1CUy_o5xRJrtDMSApyD3J4duxQ9VFTbea3e6apvF2zpUOFKPY0g_wTGKu0CSSKYJM0ylp1__yoTJtHR5geEDVq49NyU1mpV5BHYx6Yu3deLS7M3WVlLNOBwHHJIC_7dOk7LVX-XI8XTWQ_tykXMy9PHLGBt-EDXWQ--QNq75ZGJdRXJdu1xjzXKIARp2DbStWZHWU-0QgGqkKruGKI1FLapjRB67vtpmy6rt2yWfVb77G-wNpUhpKDwu8D3V7wllf8iFp96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXwRBNtTUaOegsxsJ0LwIgFIEEjQApTdo3ERCvpzOeYow6VBcb9a3aEtuhtnFyivTnx9Z3A6nLrgRp_0nkKoKg_-gZCP3iCGU-Xmh8eMmbqgjFzHI91l311QeHBSyl_FSwBtFhWdu_mBFQ5f6uCbugXSOOfY405zkyyBjKsxHGcPyTB4yF6vv2_qOQs4rRNQ3SapErosSE3HKjNjNZlX-922FmbfD0K8baIutYIVaOUwQGG5BgiyQ1g1JUCplTvyGqjLN0Dm3fuLyDYzqvgyaI45hSHxaOqrZX3m5_FwSLpM_RdPh1vwlnk0axeE6rVu0Bb81tPW7gsPVQ8HYItrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxE_2iVbO9TGgQs3iuaSWwzvsiR9VlT4vLdOt7noddL-B3y1wKX02zlIKqaFTvpgF2DHPScepfqP3kfAVvmcBfJjozBLitHVFMI34QmHW9zviec-U4zgdtMQm1sD1WTkBsdAMxcnKzKSa23Z1-4-LxI_EvoLiC5ZYhy-atoAVkcfjUBCq6r346V63IKBOHQafO412EbmAj0vTUHrqDXrxzacAM4pGVy6s5-ERWlf7Ur_9WpDdcF7kCpYcHja56-Pv4hqv5bKuctjV4XoiEKbw0gAqcT7U1UhhlsNGgC19pt73H7fEzzLNvNMmFIp2Xah1L2e8_jfalLDo9FfYVIZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5krU8nhyDpnP5Xuxqc8nJq1OUFIz_KflLuA3LsChn8MUmE06wjoNT1ZQwI2uIrjqhIdni-53BIEb1NJkn6ne-Hz7qZIpafUo5aoBcdrtE2gU7FQcvWMG0bWeUpdhmr8tXs0qLWOsvgY8hj-7t621KSFBXl8koSJFqvLbsIoFWP3OlK6-eHj396CCMe7uSzpc8Ke9RP1Wa7zD4V2iTnXklTnZQZAFp3ytWYg7e9pGe_YOcMlfdVgXQhSrb2Adhnum9kPKWramWoXqHC5p1gKSzdTsw6P-iuNMxTDN44WDm-LV34CdUOXMb4hdkqRgVB1cLO-mgkVS0emcurrNmKfdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از نخستین تمرین تیم ملی فوتبال در ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/436466" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استانداری هرمزگان: پدافند قشم برای مقابله با ریزپرنده فعال شد
🔹
صدایی که ساعاتی پیش در جزیره قشم شنیده شده است، ناشی از فعال‌شدن سامانه‌های پدافندی و درگیری با ریزپرنده‌های دشمن بود.
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/436465" target="_blank">📅 22:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftkcwDt9Zl0H_AAk2Yf6mtOllUZbsvPO50rwOaE9h8fgDQIwxFDHwUeIwVJfxTClsGmwm8Hr7ks5Zzka-Gbnbz-EPhcrpjRd-F96LbqzjEmNBbHgy7BwODL3mWu1wUlWtn9dR6poE2WvnCT4ti_Wvqgtj46PvLk0P7El0bp1ytlAx-9_60adt87-sCpCdiJfulkQBdubAh7Ig9Pd11KpwS5SJ63qcYYmA8ImXwWvpVrRrwxECmspYcEwB9BKkh38c1KnYT2AGitA-SRnwVf627FdqmVATmQk19KL7mg51xboDQr1Bxe4T6i7QiGIXmnAWbUV43ZSbcLAPVAC-erPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/436457" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7abf04a1.mp4?token=C2RGbAnBbd9aC9BvZduUQ4GMVk52JgiJ_r2O5nmPrk6RUs-2DyihDG1n9L8mmcO6pXdTNCgiYndVnK6F_1cW854vZP_R1_pBY_UidJMNoafhfHtvjrUj-eQhDuN8aBdNraWP8jVpVDceI6ii03y56ATT8Qz_o7LQkmuegYArywfDNRnT579A2kqx8JIoVTsxNj6JrW4sLHrfgbL5fZrJPLNBZjLOwh87RlGZUSiuhHQRGuCC5mtX6CTqadJ3CZFF0i048EXwmN85qITLcOQNaK2eedauL9lDVUDhTw4A_LkFJHEsy_m6IFvIaTCZ-EWLhRQMlXtelWI8o5Wx9eXZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7abf04a1.mp4?token=C2RGbAnBbd9aC9BvZduUQ4GMVk52JgiJ_r2O5nmPrk6RUs-2DyihDG1n9L8mmcO6pXdTNCgiYndVnK6F_1cW854vZP_R1_pBY_UidJMNoafhfHtvjrUj-eQhDuN8aBdNraWP8jVpVDceI6ii03y56ATT8Qz_o7LQkmuegYArywfDNRnT579A2kqx8JIoVTsxNj6JrW4sLHrfgbL5fZrJPLNBZjLOwh87RlGZUSiuhHQRGuCC5mtX6CTqadJ3CZFF0i048EXwmN85qITLcOQNaK2eedauL9lDVUDhTw4A_LkFJHEsy_m6IFvIaTCZ-EWLhRQMlXtelWI8o5Wx9eXZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات حجت‌الاسلام رفیعی درباره صوت منتشر شده از او
🔹
رفیعی: صحبتی که بنده بیان کرده بودم صرفا یک نقل‌‌قول بود که می‌تواند درست یا نادرست باشد.
🔹
منظور از این صحبت نشان‌دادن خباثت دشمن بود که در آستانۀ به نتیجه رسیدن مذاکرات، حمله کردند نه این‌که بخواهیم به کسانی اتهام خیانت بزنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/436456" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📷
یادبود شهید علی لاریجانی در مسجد بلال صداوسیما  عکس: صادق نیک گستر @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/436455" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d0fd3957.mp4?token=agCIdvyB4bnJjYcoZ7HCxxREJsPS9deIX5RqOX0UUW9zXvGddMAKdjE_fkre2RBuMdj9-JTzj_rl5ooN9YjiHlq7Y4wpMyF6NcRVZW7X5d9mGkLM10jRu8SSRDbAqHyaB17sAdw__WWD5fH5lB3Provy9x5kAefs1NFLSchC2O_oIAdy6G8K8aUkY3euvHCbvAkWHWHVI64OVPkDtnKLNrRqP8bzLqM9s7pR3XSv7CE-PFJneG3bibUh1-AdH2mo3ubGUDNnPtxHCFcwQPYxG5VktOrJrmLeHq6RlaYpYtQEm33WVslXL-L2kthYUaD4WqrTwcQfJ58Vy-W35L84ZyOyq1ubmFBv6JWlJj0WH4bwaVzhAM0FmTLYw4j2P_UMO6t4HsHyEz9UV5l2ufoTP5MGSfyv6eFdC_a9VprwdDSulPTwZz-0QKwUhfCud-FvLU_jjrC8g2GCkW4u4vgU7vb-O3rS-JBg8s6cWklIQnermBt_Fa7Ys-IlJ9XomjXu7xy70NYUG1ZeqJFOTOFDN0IFZQWrxSoY4gHG1hebIgDljpgQ1EET9NK23uB3TcXrqq5dUCcrE0wbvyzl43QIdSb-E9qlJbLjQAPtpUsshya1UjqQlVEkKAh0ru2n2gTLpBjLHY7kprB2sYYDcfyrlnpqU9YN-s5h3CsoBcoSu-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d0fd3957.mp4?token=agCIdvyB4bnJjYcoZ7HCxxREJsPS9deIX5RqOX0UUW9zXvGddMAKdjE_fkre2RBuMdj9-JTzj_rl5ooN9YjiHlq7Y4wpMyF6NcRVZW7X5d9mGkLM10jRu8SSRDbAqHyaB17sAdw__WWD5fH5lB3Provy9x5kAefs1NFLSchC2O_oIAdy6G8K8aUkY3euvHCbvAkWHWHVI64OVPkDtnKLNrRqP8bzLqM9s7pR3XSv7CE-PFJneG3bibUh1-AdH2mo3ubGUDNnPtxHCFcwQPYxG5VktOrJrmLeHq6RlaYpYtQEm33WVslXL-L2kthYUaD4WqrTwcQfJ58Vy-W35L84ZyOyq1ubmFBv6JWlJj0WH4bwaVzhAM0FmTLYw4j2P_UMO6t4HsHyEz9UV5l2ufoTP5MGSfyv6eFdC_a9VprwdDSulPTwZz-0QKwUhfCud-FvLU_jjrC8g2GCkW4u4vgU7vb-O3rS-JBg8s6cWklIQnermBt_Fa7Ys-IlJ9XomjXu7xy70NYUG1ZeqJFOTOFDN0IFZQWrxSoY4gHG1hebIgDljpgQ1EET9NK23uB3TcXrqq5dUCcrE0wbvyzl43QIdSb-E9qlJbLjQAPtpUsshya1UjqQlVEkKAh0ru2n2gTLpBjLHY7kprB2sYYDcfyrlnpqU9YN-s5h3CsoBcoSu-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش‌های نظامی به مردم در شهرک رجایی مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/436454" target="_blank">📅 22:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e295e864.mp4?token=tG3N7xtughk0iJFzm7nNA2nyufm9yLxr8vIZZCxOnUqJBwf7fHJuralhfu3oy6v1K92JiDEh5NWMVyBXqjZCxbbMhGMJDC-7MxqBhcbjnXaW__HZ-F54CVyakhCxDA0yyxJ3MqhdmF4DLP6VP8cXrlrephR697vOV7uiLHewRM-0d78Dl-EQx8vNwVAwlnOAD8vDtmfMlnXvIWug9LcwdAB3O2-tX7fpZDtjCHCM5xsKfXm_p0iE0PJtNjG_y1sCWKg4ueaLLCTHuQaTSyXMnE8qErvdvrZ2qq3HyC1XfVJOjoZ93_sXRvxcgB5JbmxaqbJYHV4jkr6GMayNvRFTqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e295e864.mp4?token=tG3N7xtughk0iJFzm7nNA2nyufm9yLxr8vIZZCxOnUqJBwf7fHJuralhfu3oy6v1K92JiDEh5NWMVyBXqjZCxbbMhGMJDC-7MxqBhcbjnXaW__HZ-F54CVyakhCxDA0yyxJ3MqhdmF4DLP6VP8cXrlrephR697vOV7uiLHewRM-0d78Dl-EQx8vNwVAwlnOAD8vDtmfMlnXvIWug9LcwdAB3O2-tX7fpZDtjCHCM5xsKfXm_p0iE0PJtNjG_y1sCWKg4ueaLLCTHuQaTSyXMnE8qErvdvrZ2qq3HyC1XfVJOjoZ93_sXRvxcgB5JbmxaqbJYHV4jkr6GMayNvRFTqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش پرشکوه مردم غیور تربت حیدریه برای بیعت با رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/436453" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgFknmp3lOKEvJx26_C_T5ShR3jWB6pvn8bZldVTelKt8OJU5rKv_PZlbQxjFuZq2aESOZa1AsyqVM5YxmvhRIz4J6o-tHy2HNWCTil1f3WnlgHuRChyV4vAwd5--OpFtBK8qtO6kR6rcw0IMHge52MgLMnYGG68jI3TzPGcJrstdAQCotXxk6mJFDYM9jKuiVBgx66IsNllPBuEHXMh_uCSCBrfwwlgj0p_gUdUWYwbqaf2zP1HFSEkLhnK85IffI9xzOAiwF8IZBXEmLcj74N-aPDHifSsCtJ7KF-d_VYXGPHAqVk09L-ny5TwDalOqqDsZHIpF0_MpaXi1USCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: گفت‌وگو به معنای تسلیم نیست
🔹
رئیس‌جمهور: گفت‌وگو به معنای تسلیم نیست. جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود و به هیچ عنوان از حقوق قانونی مردم و کشور عقب‌نشینی نمی‌کند. ما با منطق و با تمام توان، تا پای جان، در خدمت مردم و حافظ منافع و عزت ایران خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/436452" target="_blank">📅 22:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تاج: متفاوت‌ترین جام جهانی را در پیش داریم
🔹
رئیس فدراسیون فوتبال: متفاوت‌ترین جام جهانی را در پیش داریم. شرایط جام جهانی را همه می‌دانند؛ آمریکا دشمن است و دشمنی‌های خودش را دارد و از دشمن نیز جز دشمنی انتظار نمی‌رود.
🔹
ما باید تدبیر و برنامه‌ریزی کنیم تا مشکلی پیش نیاید. خوشبختانه تیم ملی شرایط بسیار خوبی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/436451" target="_blank">📅 22:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/436450" target="_blank">📅 22:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed04e9df61.mp4?token=NWM2VpZKL9HceLyixtjC2k7N0tGCiNbV8csmtn3Jx1VuoXoC_dSZf1NrFNShkttwjTIEVyza1txoZtKHugtOzED0xQRqYhf7YeOwG4VOvJX4IrmLRGSm1i6_dLf1CD8FpcNkot-bSqHQUjEUNonJT4TbH8AB7DqEiWZiQAiSYg6BK-WqI0t4F3eFKc1ldPALAn91WfQAV5vaD8OoRuNnlFrIkscM4SC9Z-DSWHorXZldwi_9QZ1V0pvOpVI2x1WUqt7-9M9k2R6u2i4-rmZsbcNf8zHBAsbRJJDzytbYi05CjFBkf-DXNzc6b1p7r4847YVIS_-VKrWNSm7d4uremh7fPTjKVMMomlntLNKjUNraM5ueb5Ru4lu4pui_lMDD04LHndMamX3t7-MC9p_zkJIkjzbePfHkIX9YCmpgr4xghuSxTIW-jbqccc5a79lJQM_wkoxVdySQU8IunyTDyB3sNXGGm2JdFkuU1gmJ5EDl7_-ED_uxRqJr1DkrppJvqjqjFQuQjbViNbMHfs4XotN0DQVAFQbyZOk8AUB8jVnOmhwacmd4Z9Ym0Upah9-6xny04dW7SixlgRsmmyAKolSn-CAfY00jN9kluR31jo9rEjVS58iIz-7GZ8LWh7mRTMGDA3IeQQBOzIgkX_vDATV6So7Ip-Wa7ogaQ2M5M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed04e9df61.mp4?token=NWM2VpZKL9HceLyixtjC2k7N0tGCiNbV8csmtn3Jx1VuoXoC_dSZf1NrFNShkttwjTIEVyza1txoZtKHugtOzED0xQRqYhf7YeOwG4VOvJX4IrmLRGSm1i6_dLf1CD8FpcNkot-bSqHQUjEUNonJT4TbH8AB7DqEiWZiQAiSYg6BK-WqI0t4F3eFKc1ldPALAn91WfQAV5vaD8OoRuNnlFrIkscM4SC9Z-DSWHorXZldwi_9QZ1V0pvOpVI2x1WUqt7-9M9k2R6u2i4-rmZsbcNf8zHBAsbRJJDzytbYi05CjFBkf-DXNzc6b1p7r4847YVIS_-VKrWNSm7d4uremh7fPTjKVMMomlntLNKjUNraM5ueb5Ru4lu4pui_lMDD04LHndMamX3t7-MC9p_zkJIkjzbePfHkIX9YCmpgr4xghuSxTIW-jbqccc5a79lJQM_wkoxVdySQU8IunyTDyB3sNXGGm2JdFkuU1gmJ5EDl7_-ED_uxRqJr1DkrppJvqjqjFQuQjbViNbMHfs4XotN0DQVAFQbyZOk8AUB8jVnOmhwacmd4Z9Ym0Upah9-6xny04dW7SixlgRsmmyAKolSn-CAfY00jN9kluR31jo9rEjVS58iIz-7GZ8LWh7mRTMGDA3IeQQBOzIgkX_vDATV6So7Ip-Wa7ogaQ2M5M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا می‌شود با انفجار یک موشک در مدار لئو، ماهواره‌های پیشرفته آمریکایی، اسرائیلی و اینترنت استارلینک را از کار انداخت؟  @Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/436449" target="_blank">📅 22:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
خیابان‌های خرم‌دره زنجان، میدان نبرد اراده‌ها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/436448" target="_blank">📅 21:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خطر بزرگ در کمین افتتاحیهٔ جام جهانی
🔹
درحالی‌که کمتر از یک ماه به شروع جام جهانی باقیمانده، نگرانی هواداران از حضور در مکزیک به‌عنوان یکی از میزبانان این رویداد بزرگ بیشتر شده است.
🔹
تیراندازی جمعی که روز یکشنبه در ایالت پوئبلا مکزیک منجر به کشته‌شدن ۱۰ نفر شد، نگرانی‌های امنیتی را تشدید کرده است.
🔹
۶ مرد، ۳ زن و یک خردسال قربانی حملهٔ مسلحانه در خانه‌ای در فاصلهٔ ۲۰۰ کیلومتری مکزیکوسیتی جایی که قرار است بازی افتتاحیهٔ مسابقات در آن برگزار شود، شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/436447" target="_blank">📅 21:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce5ec67af.mp4?token=AsLWLXOT_uB1EonoPo6RNwQKRmQJPpS9OjAuySAkVUyImCASUnqL0k1U0f_zqvZ4NO5YH02uPfgRtdhu4UT7XzlbPc6_kTczF5V3HBSkM9vqIaktNBjL00ihTjRQ_J07pBt5y3FH4OWghN0DLKJK5thfup5fF7DGHRJ0vchlDxaAPa29rLEvxuFpmE3D9rmgQH0sXkpLW--qvDysStmNBH6xGiMwDs7KwwOQZplYhwqmVnX5JRH9msKucpdfIkquNkMnCSeSRXWH7AoGIWevXWms2nwQ01XDI6Lw3GEDwrVoOu54IovnB4dgG4ccyv7DM7cumhUgwf5c40ibk2ejYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce5ec67af.mp4?token=AsLWLXOT_uB1EonoPo6RNwQKRmQJPpS9OjAuySAkVUyImCASUnqL0k1U0f_zqvZ4NO5YH02uPfgRtdhu4UT7XzlbPc6_kTczF5V3HBSkM9vqIaktNBjL00ihTjRQ_J07pBt5y3FH4OWghN0DLKJK5thfup5fF7DGHRJ0vchlDxaAPa29rLEvxuFpmE3D9rmgQH0sXkpLW--qvDysStmNBH6xGiMwDs7KwwOQZplYhwqmVnX5JRH9msKucpdfIkquNkMnCSeSRXWH7AoGIWevXWms2nwQ01XDI6Lw3GEDwrVoOu54IovnB4dgG4ccyv7DM7cumhUgwf5c40ibk2ejYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بات‌های تلگرام از امروز باهم حرف می‌زنند
🔹
تلگرام قابلیت جدیدی اضافه کرده که بات‌ها می‌توانند مستقیم با یکدیگر صحبت کنند.
🔹
این ویژگی به بات‌ها اجازه می‌دهد کارها را به‌صورت خودکار و زنجیره‌ای انجام دهند، مثلاً یک ربات اطلاعات را جمع کند، ربات دوم آن را تحلیل کند و ربات سوم نتیجه را بدهد.
🔹
توسعه‌دهندگان حالا می‌توانند شبکه‌ای از بات‌ها بسازند که مثل یک تیم با هم همکاری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/436446" target="_blank">📅 21:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e688626c28.mp4?token=F0HT77rOfQsQHlsjXNA_Q82wXvzt62RZbHkzl3vAwjND0h4VuXbLi_81l0DGyjBbj01b8IQ4pYKAE-ZuQBk4lehpFoRZO_kYtSt9jDZbQJyxr_kbfBX03ANb2bfT_DXK5B_kKVlUGutBcCvteUR2gebcXCujpMYMJ80Y13g10SeijbgoYjdkefSZpvsrOU5NGJERu5vuWWiyj9TYgwvvHZnMFP2y2wjthglUrMB-ZPXbxT8s33nDXtE8pxhUZzMZiYIAiJe8IbA9-GY0wwIknlapJz0AUJNrPpseKcBMlSUpa_qWbpbqKDCLiY71Rj7Vd45Y3wyLn1rhySXPuu5htA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e688626c28.mp4?token=F0HT77rOfQsQHlsjXNA_Q82wXvzt62RZbHkzl3vAwjND0h4VuXbLi_81l0DGyjBbj01b8IQ4pYKAE-ZuQBk4lehpFoRZO_kYtSt9jDZbQJyxr_kbfBX03ANb2bfT_DXK5B_kKVlUGutBcCvteUR2gebcXCujpMYMJ80Y13g10SeijbgoYjdkefSZpvsrOU5NGJERu5vuWWiyj9TYgwvvHZnMFP2y2wjthglUrMB-ZPXbxT8s33nDXtE8pxhUZzMZiYIAiJe8IbA9-GY0wwIknlapJz0AUJNrPpseKcBMlSUpa_qWbpbqKDCLiY71Rj7Vd45Y3wyLn1rhySXPuu5htA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«قلب اینترنت جهان» در دست ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/436445" target="_blank">📅 21:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd3296632.mp4?token=IVwEZe9K7cPj8vEEgxRErm8Ct08-H_BGYVEe7eC9c1cf6kv3hUbzCvzuq0qiIg-uGwoJVDi091Yfybn-UQ9BekEbE3kJQwnjRqRZUcFjE70z_aBRfSk21nA3dOEy7dJ05E_qw7ERbq6Lwm6i-PG2mOr-uR_Y032tNrJFfXmv-0J8G7pgv8Pvmx3QayO-39zUcPR62Q2oKBJn_D41v3R9_IRaF3ExPjgh-FiYW8E7FN3ACX8UxRNVrWYWBVTsL5UvJA5vAZUmASZ4A0ruOy3LF3KTWnSoXZr-c4QYRBCdjH3DvBZ_iCVPgCTjFmZjkosizbZWhcsPAfk5F57iBAA3kEWRIMUx5VfvnQ3CUnHL_AfSUIdfmA1-ZqJTiAUMnwA1TQDHSQjQ8fAlQekSZHsum0QQxUjGW7QjZqi5MrA8aEZQIhiBtT65_MMskYGI52eqQecV9OEsZ6gbtkxeHID-QWU3jlUIIrc-Jt7-Z401hAATWnBmalRM96LGFSYlKPo7U783EzrJ1daediY6M1LqgD4x22PEPa-DB32qBTYYFL0qCI6h68UY60ZpP3f27JHgtDhODrFbuN4OU6LHu4dCgXKt9P9PmvHMA-2LtUkxLdKMw9zPHz04UdF5Df3QZDtOjMEUoJeACcsX-bchIz1l2H_kTqGNjcD22-Vba33EyVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd3296632.mp4?token=IVwEZe9K7cPj8vEEgxRErm8Ct08-H_BGYVEe7eC9c1cf6kv3hUbzCvzuq0qiIg-uGwoJVDi091Yfybn-UQ9BekEbE3kJQwnjRqRZUcFjE70z_aBRfSk21nA3dOEy7dJ05E_qw7ERbq6Lwm6i-PG2mOr-uR_Y032tNrJFfXmv-0J8G7pgv8Pvmx3QayO-39zUcPR62Q2oKBJn_D41v3R9_IRaF3ExPjgh-FiYW8E7FN3ACX8UxRNVrWYWBVTsL5UvJA5vAZUmASZ4A0ruOy3LF3KTWnSoXZr-c4QYRBCdjH3DvBZ_iCVPgCTjFmZjkosizbZWhcsPAfk5F57iBAA3kEWRIMUx5VfvnQ3CUnHL_AfSUIdfmA1-ZqJTiAUMnwA1TQDHSQjQ8fAlQekSZHsum0QQxUjGW7QjZqi5MrA8aEZQIhiBtT65_MMskYGI52eqQecV9OEsZ6gbtkxeHID-QWU3jlUIIrc-Jt7-Z401hAATWnBmalRM96LGFSYlKPo7U783EzrJ1daediY6M1LqgD4x22PEPa-DB32qBTYYFL0qCI6h68UY60ZpP3f27JHgtDhODrFbuN4OU6LHu4dCgXKt9P9PmvHMA-2LtUkxLdKMw9zPHz04UdF5Df3QZDtOjMEUoJeACcsX-bchIz1l2H_kTqGNjcD22-Vba33EyVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتاق اصناف: پاک‌کردن قیمت کالاها ممنوع است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436444" target="_blank">📅 21:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8f95cc9c.mp4?token=DHkaoiF9J90gtpvKwiCPWnijpb7CkM0T-YRLcAJ8zG_p-2WBugqurFuXwYfdeO81Ox6wvI_Px5ZsbAKUIt91wUQgIZUU5rLuWPygAg5blgiLis1uwSPAaY3km8d4gmnCRtooAeWvDs_ZfbcPZZ1Lcg_W_zrfRBDW1ae_IsHtTyYeLUA27mDD9eClFVoeOqH66j_59SFdxZO-4us_aU9xGlmU8QooVb89cwQFz6mmkhJBBMyDsr0FZW4aDtBlTXGJvU5cUQkd8bwFSxRgmto4uQvRt0TwgO9gpKYf63kunF8KKUWNO5dLqGznVFGaHGaCNvn1jePEp7ALHn1WNzLvBEvPH1vEj9BrQodM3hPHEsrZK8CDahF1QgB8_nvLGK3OA929qlPgXlDR4GN6zo17OzRDLEI2CiZocU5xI5xbX_dPpeCwm0yMeDwKlvSApolsdUGe0QZS1AU35dEoY_3OhS8xyA3bG_del7pCtHdGjMzaOuvMTj3Q-Z1ClZwLMAQsOtrtqSgdMYC4qAktsM4dWKga8BbDGSDBAf70Ym2ENsyNASRQM8k9Dlmjwa075J8wc67pH-Ml0Mm41kkUVP4rSeFRVwKdSA6EEEtn0gW4Gaq8CgoTUSQeCv6HUwlASgSZ0DI13AuNxI4mTbs-LHaDNrA0HEJddSlOZbYAQFuszUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8f95cc9c.mp4?token=DHkaoiF9J90gtpvKwiCPWnijpb7CkM0T-YRLcAJ8zG_p-2WBugqurFuXwYfdeO81Ox6wvI_Px5ZsbAKUIt91wUQgIZUU5rLuWPygAg5blgiLis1uwSPAaY3km8d4gmnCRtooAeWvDs_ZfbcPZZ1Lcg_W_zrfRBDW1ae_IsHtTyYeLUA27mDD9eClFVoeOqH66j_59SFdxZO-4us_aU9xGlmU8QooVb89cwQFz6mmkhJBBMyDsr0FZW4aDtBlTXGJvU5cUQkd8bwFSxRgmto4uQvRt0TwgO9gpKYf63kunF8KKUWNO5dLqGznVFGaHGaCNvn1jePEp7ALHn1WNzLvBEvPH1vEj9BrQodM3hPHEsrZK8CDahF1QgB8_nvLGK3OA929qlPgXlDR4GN6zo17OzRDLEI2CiZocU5xI5xbX_dPpeCwm0yMeDwKlvSApolsdUGe0QZS1AU35dEoY_3OhS8xyA3bG_del7pCtHdGjMzaOuvMTj3Q-Z1ClZwLMAQsOtrtqSgdMYC4qAktsM4dWKga8BbDGSDBAf70Ym2ENsyNASRQM8k9Dlmjwa075J8wc67pH-Ml0Mm41kkUVP4rSeFRVwKdSA6EEEtn0gW4Gaq8CgoTUSQeCv6HUwlASgSZ0DI13AuNxI4mTbs-LHaDNrA0HEJddSlOZbYAQFuszUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروسی‌های جنگی زوج‌های جان‌فدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/436443" target="_blank">📅 21:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تامین‌اجتماعی: واریز حقوق بازنشستگان از سه‌شنبه آغاز می‌شود
🔹
پرداخت حقوق اردیبهشت‌ماه بازنشستگان و کلیه مستمری‌بگیران تامین‌اجتماعی از ظهر ۲۹ اردیبهشت آغاز و به‌تدریج طی ۷۲ ساعت به ترتیب حروف الفبا انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/436442" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b01e76f2.mp4?token=euRDPBxPswaVWk7R8bR9ZvHVm6m3MrHuJUiIfFgCSuzwWzmgao2MPT57-yjTwhQwxvAU6OTzG92XI3SxeQRFFvBtqkZbADVQ2rVIquGtFqPKUA61ACPMBgjvmBJtR2clegGNc7U1QBmBjWAq80g0-B9tC4c1ZuNaRdPgXUMODcRf2lBseQOZZQpEprJzFRXROy-PM4fs8RrNyOWeFA4Iy-DtATY52kJl-MtgpAev9oYJKihUrnOAKYTd_lqtuuvM1inBV2thnXvBshGJYuySMIb8nns24P2A5IkT622sczB1X3A_7I3Gqpi_ol-71BTczFCoYiuxqnKRmn3SfYhKejBazwKyYzPWnkeMheWakvxO2Y3G0mlJO3VtdynwNkqNEseyI-5EMTI22VhjS_KzmfzHfNKQHEsUn5HQGbvgzdw1b9OWMTzNspBuNObHBEhs2SG57FprWjDf__HeWZbFdpkHTdirFxaKXBSgeAc9BWjT7sEeWF9g9IcCMh-Mwg2VODPCfgsB3OQFVrbX8OJF_2i8UtXdeRV43g7-hvYLirhiCerHkScm-NNjOo6gOv1WG9A89O3Tzy7Y1BtVwl6MT9WW7OMDrwsfM0IvAcEzCXPSmNxsceVxYu5C-u5PGis8gOrndG7p-kDG4iQbEIoSGP4Ob7ZLlC6w2OqKIIp0Kao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b01e76f2.mp4?token=euRDPBxPswaVWk7R8bR9ZvHVm6m3MrHuJUiIfFgCSuzwWzmgao2MPT57-yjTwhQwxvAU6OTzG92XI3SxeQRFFvBtqkZbADVQ2rVIquGtFqPKUA61ACPMBgjvmBJtR2clegGNc7U1QBmBjWAq80g0-B9tC4c1ZuNaRdPgXUMODcRf2lBseQOZZQpEprJzFRXROy-PM4fs8RrNyOWeFA4Iy-DtATY52kJl-MtgpAev9oYJKihUrnOAKYTd_lqtuuvM1inBV2thnXvBshGJYuySMIb8nns24P2A5IkT622sczB1X3A_7I3Gqpi_ol-71BTczFCoYiuxqnKRmn3SfYhKejBazwKyYzPWnkeMheWakvxO2Y3G0mlJO3VtdynwNkqNEseyI-5EMTI22VhjS_KzmfzHfNKQHEsUn5HQGbvgzdw1b9OWMTzNspBuNObHBEhs2SG57FprWjDf__HeWZbFdpkHTdirFxaKXBSgeAc9BWjT7sEeWF9g9IcCMh-Mwg2VODPCfgsB3OQFVrbX8OJF_2i8UtXdeRV43g7-hvYLirhiCerHkScm-NNjOo6gOv1WG9A89O3Tzy7Y1BtVwl6MT9WW7OMDrwsfM0IvAcEzCXPSmNxsceVxYu5C-u5PGis8gOrndG7p-kDG4iQbEIoSGP4Ob7ZLlC6w2OqKIIp0Kao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر یکی از دانش‌آموزان شهید مینابی: دخترم روزه‌اولی بود و با زبان روزه شهید شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436441" target="_blank">📅 21:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تامین‌اجتماعی: واریز حقوق بازنشستگان از سه‌شنبه آغاز می‌شود
🔹
پرداخت حقوق اردیبهشت‌ماه بازنشستگان و کلیه مستمری‌بگیران تامین‌اجتماعی از ظهر ۲۹ اردیبهشت آغاز و به‌تدریج طی ۷۲ ساعت به ترتیب حروف الفبا انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/436440" target="_blank">📅 21:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1ea73aef.mp4?token=MnzEqRf02qtDYfCsQscNcduNfGXCzM1uqATjHDeRFebtPvDhFXOtbVB25ZNuGgaIefgnyclGu_60F6Mbr1UXvcrxCdS6K4eq8KGaWCKMCL_0XYB6x3MRxjW0F4_cq4zTYVXTj9n5t1N79E3bGaD0OPG1Bzr3nCNhXCbxe4OHZuVx03zwLLnjBgrO4lsZotLlTF2jDAf0hGfW8IuMr_r6yCID90xwTUtNtbOQrn-5Ci1rkU_uCALDPKlth8H0uCzqRPJS3TqDPHpw5vMKed9MmpmRsplwY2Ji62o_9raybBZxngjnFOezONkN5CewNEtgJtwphzgeBvujltJmWoAPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1ea73aef.mp4?token=MnzEqRf02qtDYfCsQscNcduNfGXCzM1uqATjHDeRFebtPvDhFXOtbVB25ZNuGgaIefgnyclGu_60F6Mbr1UXvcrxCdS6K4eq8KGaWCKMCL_0XYB6x3MRxjW0F4_cq4zTYVXTj9n5t1N79E3bGaD0OPG1Bzr3nCNhXCbxe4OHZuVx03zwLLnjBgrO4lsZotLlTF2jDAf0hGfW8IuMr_r6yCID90xwTUtNtbOQrn-5Ci1rkU_uCALDPKlth8H0uCzqRPJS3TqDPHpw5vMKed9MmpmRsplwY2Ji62o_9raybBZxngjnFOezONkN5CewNEtgJtwphzgeBvujltJmWoAPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از سردار شهید محمدصالح اسدی، معاون اطلاعات ستاد کل نیروهای مسلح
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/436439" target="_blank">📅 21:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
حزب‌الله: محل تجمع خودروها و سربازان ارتش دشمن اسرائیلی در بندرگاه شهر «الناقوره» را با پهپاد انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/436438" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f395efd8.mp4?token=Qz-lwk2uQeXvIetheLoGdH612qBeyABDLpQGCpt_UqQNAomYtJ3mWJ8x3rKUXfFaRbY43sCDG1bGcStLBNGh2oy2K9LaM6vek18KBEy3oCs3y68HnwGIABqs6o1Dmn6t8_VCNbnBU8BoyLn7DNuS5PxryrTSshphgTxbQGqQDMF7QmW-iKqMLXgVc99VvDcpBi7ayCKG49FAF9iTcDFd0IgikuWDzuePEaSdn0DP70wASCJgjCL_zCJ-3fr8K_vXQdLe4zXboTqE16Bo2wxjt15oMeNi4VN4LYr4_2fClZqvuPK9K6Rs383MqPHrrKQ7FrXQHXyyyRoEKeGgc3j_HDHaj25addbe5DG9O50PtuZaok-vMhfJAf1opYBE1NMt_pNnUp3n5TFs27dRa8RTdhalSCjX6Wr-6mtcI6IDSu-GSLqGrU0-n-qIfJA6IczRchB5JR8IgclQmUuqRqyaUK6v3EPY5vDdN6RASe4zEC-P0DXdY0zgwnOW9e_lSvIoKdFjmyaIy6p-ZB-EUFpqB2F6YRQ4BZ7tEfjj2yExcKtZ4bimY3X4i0dK-peyRvEvJpYirGbjNHVeVE8nf6JuyVuHX20dnJtxTILFB-o295XqWwZWiHGa48tP_12pqB4ewcRPhQhDM_sBkc9bEvYAfjC0_704o0J4tCEAeji5ZTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f395efd8.mp4?token=Qz-lwk2uQeXvIetheLoGdH612qBeyABDLpQGCpt_UqQNAomYtJ3mWJ8x3rKUXfFaRbY43sCDG1bGcStLBNGh2oy2K9LaM6vek18KBEy3oCs3y68HnwGIABqs6o1Dmn6t8_VCNbnBU8BoyLn7DNuS5PxryrTSshphgTxbQGqQDMF7QmW-iKqMLXgVc99VvDcpBi7ayCKG49FAF9iTcDFd0IgikuWDzuePEaSdn0DP70wASCJgjCL_zCJ-3fr8K_vXQdLe4zXboTqE16Bo2wxjt15oMeNi4VN4LYr4_2fClZqvuPK9K6Rs383MqPHrrKQ7FrXQHXyyyRoEKeGgc3j_HDHaj25addbe5DG9O50PtuZaok-vMhfJAf1opYBE1NMt_pNnUp3n5TFs27dRa8RTdhalSCjX6Wr-6mtcI6IDSu-GSLqGrU0-n-qIfJA6IczRchB5JR8IgclQmUuqRqyaUK6v3EPY5vDdN6RASe4zEC-P0DXdY0zgwnOW9e_lSvIoKdFjmyaIy6p-ZB-EUFpqB2F6YRQ4BZ7tEfjj2yExcKtZ4bimY3X4i0dK-peyRvEvJpYirGbjNHVeVE8nf6JuyVuHX20dnJtxTILFB-o295XqWwZWiHGa48tP_12pqB4ewcRPhQhDM_sBkc9bEvYAfjC0_704o0J4tCEAeji5ZTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چهارمحال‌وبختیاری با برنوهای خود به تهران آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/436437" target="_blank">📅 21:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حزب‌الله: محل تجمع خودروها و سربازان ارتش دشمن اسرائیلی در بندرگاه شهر «الناقوره» را با پهپاد انتحاری هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436436" target="_blank">📅 21:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65ee77392.mp4?token=iElKSMOclewUTQjuyoL3Nc1bbzB6BKfJBc87ZaDTp8fK6MszHvTlpmzKq8GBFoawFUajxbwGXfd6D2HW8Bhbo34pcCe_lE0Kgrmr5MU2PZ5wcdPj9m4pkUMFPRNvKFXB3ElUBW2AsKJORF_CvoHlXzIoFNRJlGIry17tzd9omLuTT57k9oW-Ht8La8wYYZWGM02BKIzqZLzHM8lnc7FXODXidl0LV2yy-OgJVsR7V4DdRVYX6mA5QGrSB2xz3UEBfsmKCmbE7iogzMmIGsZ-BGKYHsy5fCmV26sHxF5VeHbZK5zOLq4y1DKO4ifoo-X1UQSOZ8HiAg5NmkLbmVkrY4xbB2rYgBsEqFi6JbF_WoC1bd0uBuBFAY-ZiTPpBBca0MPKS-3nsQ9SEXprxHg4EwpAbYpIQ32ycb4zZxy06FlForXn4zD-CbKpG1lKNKBEXtF94WB6GupYrIfi5MMeH1cW3m6yNmPhdJssfceSnEOgnIWAqnYpRHFTBZ2sP_OK8R3mFEtSNMaFY4jt0lw0yJiX0QHRZf0HKqA2cMmCOa0y4q7PqhPkch0lQBssi4RroKWlIRWqCuDvzK7KK59DAEEC2C2aniXQE9uBrV_OrwP-wPs3DJG9WGDZTqpuocWxnDgWQSjcvXBMaTDVXwatcemYCMRaZ_9DF1hDo98D3is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65ee77392.mp4?token=iElKSMOclewUTQjuyoL3Nc1bbzB6BKfJBc87ZaDTp8fK6MszHvTlpmzKq8GBFoawFUajxbwGXfd6D2HW8Bhbo34pcCe_lE0Kgrmr5MU2PZ5wcdPj9m4pkUMFPRNvKFXB3ElUBW2AsKJORF_CvoHlXzIoFNRJlGIry17tzd9omLuTT57k9oW-Ht8La8wYYZWGM02BKIzqZLzHM8lnc7FXODXidl0LV2yy-OgJVsR7V4DdRVYX6mA5QGrSB2xz3UEBfsmKCmbE7iogzMmIGsZ-BGKYHsy5fCmV26sHxF5VeHbZK5zOLq4y1DKO4ifoo-X1UQSOZ8HiAg5NmkLbmVkrY4xbB2rYgBsEqFi6JbF_WoC1bd0uBuBFAY-ZiTPpBBca0MPKS-3nsQ9SEXprxHg4EwpAbYpIQ32ycb4zZxy06FlForXn4zD-CbKpG1lKNKBEXtF94WB6GupYrIfi5MMeH1cW3m6yNmPhdJssfceSnEOgnIWAqnYpRHFTBZ2sP_OK8R3mFEtSNMaFY4jt0lw0yJiX0QHRZf0HKqA2cMmCOa0y4q7PqhPkch0lQBssi4RroKWlIRWqCuDvzK7KK59DAEEC2C2aniXQE9uBrV_OrwP-wPs3DJG9WGDZTqpuocWxnDgWQSjcvXBMaTDVXwatcemYCMRaZ_9DF1hDo98D3is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگی‌ترین غرفهٔ مردمی محلهٔ فلاح تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/436435" target="_blank">📅 21:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3fecf0229.mp4?token=YEVcMf8Mi8_8sJ8Teo4e5Mey9CHIxEKUdyErp4nZX9pMW4FCfx-zRBUbug3XA1YZ_j5pkyQe1ZGZIB7NucSbVCXEbQgWP0i6LU9c7Lyny6UwQI-zzqtd4SrrDgl7XPraxTYOh5KuLoHj-OxyfC4CpX_UTamliPlDcIm2Pupy0vcl9NExT1T8v9S-QculNVA5Mh9QOheJlWGE36EoWKNegM2ep_q23NkJXmNYKsr_hS7OTOH-hQNvPxg8mqY2-QuhkRF7oj0rjkxWl1auray0NTDb5htFUHlJebCOPBTDcAbD5uyvWYc2rffg1xpguOT2Z9v1AvoVFh8n8i16m7iK9qE1EmeDXi7tOG_qgbXy8EUusKwYBddhK7DxqDhz-527djEXZhmDTlcu0fYdbpCSAu9QR_n7IlQI8lmQQ6LHOv6cKve9uV4RNS3KXNlkIYmppsq4-WZ6rwfOqzsWuiB2QD8Jr5dLOgRitKaiqGR3MjpwJhJoo8FSUAhnk8paD0tjpOLel7Ia1lZboB_11n3ozw8CHZt7LDvb20b2rslovtm7kFZMyEGuJvxbV0Gm0lFWaybhFi-sHMcPg6JwVrcpcK4Qr2aQ_w7JGakz9TUdBtsBArgY5BJ0jQggc3Eg-4B-l3PTphn48nWSG0oo2K7UuPd-lPFQrJB3SYG3BYXHBDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3fecf0229.mp4?token=YEVcMf8Mi8_8sJ8Teo4e5Mey9CHIxEKUdyErp4nZX9pMW4FCfx-zRBUbug3XA1YZ_j5pkyQe1ZGZIB7NucSbVCXEbQgWP0i6LU9c7Lyny6UwQI-zzqtd4SrrDgl7XPraxTYOh5KuLoHj-OxyfC4CpX_UTamliPlDcIm2Pupy0vcl9NExT1T8v9S-QculNVA5Mh9QOheJlWGE36EoWKNegM2ep_q23NkJXmNYKsr_hS7OTOH-hQNvPxg8mqY2-QuhkRF7oj0rjkxWl1auray0NTDb5htFUHlJebCOPBTDcAbD5uyvWYc2rffg1xpguOT2Z9v1AvoVFh8n8i16m7iK9qE1EmeDXi7tOG_qgbXy8EUusKwYBddhK7DxqDhz-527djEXZhmDTlcu0fYdbpCSAu9QR_n7IlQI8lmQQ6LHOv6cKve9uV4RNS3KXNlkIYmppsq4-WZ6rwfOqzsWuiB2QD8Jr5dLOgRitKaiqGR3MjpwJhJoo8FSUAhnk8paD0tjpOLel7Ia1lZboB_11n3ozw8CHZt7LDvb20b2rslovtm7kFZMyEGuJvxbV0Gm0lFWaybhFi-sHMcPg6JwVrcpcK4Qr2aQ_w7JGakz9TUdBtsBArgY5BJ0jQggc3Eg-4B-l3PTphn48nWSG0oo2K7UuPd-lPFQrJB3SYG3BYXHBDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان متفاوت عروس‌ و دامادها در تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/436434" target="_blank">📅 21:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خسارت خوردروهای آسیب‌دیده در جنگ‌های ۱۲ و ۴۰ روزه تعیین‌تکلیف شد
🔹
یزدی‌خواه، نمایندهٔ‌ تهران در مجلس: خوشبختانه با تلاش‌های صورت‌گرفته، خسارت خودروهای آسیب‌دیده در جنگ ۱۲ روزه و بخش عمده‌ای از موارد مربوط به جنگ ۴۰ روزه رمضان تعیین‌تکلیف شده است.
🔹
خسارت‌های خرد و مبالغ زیر ۳۰ میلیون تومان عمدتاً پرداخت شده است. ارزیابی موارد بین ۳۰ میلیون تا یک میلیارد تومان به پایان رسیده، منابع مالی آن تأمین شده و هم‌اکنون در مرحلهٔ شروع پرداخت قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436433" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC1fSJCZQOjgzDl-nJCaSCohdDOh_ID-tcKMikuxlm2-380e6qHsXh8fHG4mzkA9j4mSADo1VLFMrx1d_otaThz1Vtp_M5NdkQVCKDUa0gvlf-aMDQ3tXUnURSX2bSVx78PuIGgJoeLOaDR8myPIqaosQkCSylNQ9bcBwvOa6j-m-rddsJG5xYFcGcKIX3T9G92prD96CkHpTIodYyb8TZK5b1BqZz2SptD-EDNwRa10DorzrKrOsXeOroiqZfHhGuHWls3lDsdBwLkBvkKqNtd2Cf9uqSuDGYr_Hz8ElG5Aj9kkKC9vsrDK5Vb9JUpAYm06f2FYnjGbgFxdB7ZsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حاضر به دادن هیچ امتیازی به ایران نیستم!
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/436432" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261e4d84af.mp4?token=lsi7mfMzTJeTWfxf5YlWdbwbOzLVcLRZp8mB_6d0fD5d_dNEtD3nNGXcRFabXUDa08NKhQtdEbBt9F-JHwMZlMXMUwW97q4c0yO3zJtEGi49VNhdTevFU-jQdSyIPZmhW8eacJ2r6oFv504HV0EhcMSTPAHK593weMRU-Jes8r7-XyT5bK8LU9MKPaoraKg4CnYdTni86t5vZzGcNOCMWFGRNTIAU73_MyUJKM0zBgSTUJQeWWq8Mo0V8YIW6SiaQHC_elPI3cVYxxuxNUgPL6VGAg0w-o58HBt_bYmvS8jDMW4A7vTXQI9ngHlhnuRMDiSZ9-StZmAxREYqyEk6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261e4d84af.mp4?token=lsi7mfMzTJeTWfxf5YlWdbwbOzLVcLRZp8mB_6d0fD5d_dNEtD3nNGXcRFabXUDa08NKhQtdEbBt9F-JHwMZlMXMUwW97q4c0yO3zJtEGi49VNhdTevFU-jQdSyIPZmhW8eacJ2r6oFv504HV0EhcMSTPAHK593weMRU-Jes8r7-XyT5bK8LU9MKPaoraKg4CnYdTni86t5vZzGcNOCMWFGRNTIAU73_MyUJKM0zBgSTUJQeWWq8Mo0V8YIW6SiaQHC_elPI3cVYxxuxNUgPL6VGAg0w-o58HBt_bYmvS8jDMW4A7vTXQI9ngHlhnuRMDiSZ9-StZmAxREYqyEk6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که از رهبر شهیدمان گرفته‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436431" target="_blank">📅 20:43 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
