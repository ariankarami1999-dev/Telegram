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
<img src="https://cdn4.telesco.pe/file/Dkmr1q0qIDesOoir0qVyT3LhdqKNetpIr3uPxft_lPMqsw83MPrKlMuA_7FYtWoIsWCm69LuNjIjeMdWa2qQMQ_jDg1iWkJxkM74ZyhT_TOXdXWflbDsExTNrdBnmC_WfVhSi32zzTNK4Xu0zfC_gVwn8RoaGNxuTwuQ8IhgxSLYWry4ceO2v8hNZ7uuKszCecpQyOlvQEnIR2rWiNg5lzbpjHobunc4dAivlZD4x9TlmaB-aO1Kn2GgKcKjxqS0EixK6qcD3r5kZEXx80w_aWI1sG74IvUXzqKZbrzxI9R_AnGGP1r0ctYfZg9x1sYk0m1KoF6h2jSsVX0nyHFCYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 182K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال‌استریت ژورنال: ایران در مذاکرات با آمریکا، خواهان آزادسازی کنترل بخشی از ۱۰۰ میلیارد دلار دارایی‌های مسدودشده و دسترسی به بازار نفت جهانی است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/funhiphop/76047" target="_blank">📅 09:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=gqddhiDVaTfmy7KMMEk-rVyXCHTASj8_WXorlXLBFF8wwiRiu51mSrFK8v_xIfag8Lo8g1YQ7pIF_gw7WofTHnoh4RidkoygtVUa12noUPLvtViJj6L5Y8K6LDXuT-tPVti-B0dObWUkQCLPDnUjz5SsJBElmZJ3tIbnkPLJ3E-kmz2Dgs7j3Q_OCYF4d-VTJvO7KZH8BUPtoeyt-WXxwMTPQ8v0kV6kq9m_OcLRdfZnKxh-TOLuJ8pLW1VQuTHdT0re2rV0a2FvddNnxiwNds7rI6HtwH2Lf6Z-RPqIVPW6RPaanZpVr8AQtSy7nDR0wQ7YNGqiVHu8eyU6XaBZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=gqddhiDVaTfmy7KMMEk-rVyXCHTASj8_WXorlXLBFF8wwiRiu51mSrFK8v_xIfag8Lo8g1YQ7pIF_gw7WofTHnoh4RidkoygtVUa12noUPLvtViJj6L5Y8K6LDXuT-tPVti-B0dObWUkQCLPDnUjz5SsJBElmZJ3tIbnkPLJ3E-kmz2Dgs7j3Q_OCYF4d-VTJvO7KZH8BUPtoeyt-WXxwMTPQ8v0kV6kq9m_OcLRdfZnKxh-TOLuJ8pLW1VQuTHdT0re2rV0a2FvddNnxiwNds7rI6HtwH2Lf6Z-RPqIVPW6RPaanZpVr8AQtSy7nDR0wQ7YNGqiVHu8eyU6XaBZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شببخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/funhiphop/76046" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ممنون از آرتیستا و سلبریتی های اونور آب که در تمام این مدت قطعی حداقل با بخشی از پول هایی که از همین مردم به دست اوردن یه پنل خریدن و کانفیگ رایگان دادن به ملت و نزاشتن این حکومت خونخوارِ دیکتاتور اینترنتو رو همه ی مردم ببنده، کمال تشکر رو دارم ازتون عالی بودید، دمتون گرم و کصمادرتون اگه فردا روزی باز از همین مردم طلبکار شید
ما که کیر در بساط نداشتیم ۵ گیگ کانفیگ دستمون میومد سه چهار گیگشو حداقل به چهارتا دورو بریا از همین ممبرا میرسوندیم کارشون لنگ نمونه، عرضه همین یه کارم نداشتید جنگجو های وطن، بشینید اونور همونجوری بزنید تو سر کله هم تا پیر شید</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/76044" target="_blank">📅 03:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تا کانفیگا مفته بخرید که خیر نیست
صداوسیما: بازکردن اینترنت تو این شرایط خیلی کار خطرناک و غیرقانونی بوده و سریع باید راجبش یه کاری انجام بدیم. حرف پزشکیان مهم نیست و بزودی اینترنت قطع میشه چون حرف دیوان عالی انجام نشده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/76043" target="_blank">📅 02:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رپرای محترم اگه میخواید کار بدید الان گلدن تایم کره گیریه، از من گفتن بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76042" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=a2jmMCGhGKsmZgm4_mHxVnOys4T007Y27yYw-wyKRsZio-94QliTU5wFLWagRDfLt-RX_LSo84utygOurOIYlnkDcl33ANyJxDrU9Gn6csi3jjtCXZB9yOVSEc2fI779I19XpRGy7jSLMvVi6xMzeFgBdX-qVzPLX11JqMtN0jpFfCF_1Yn_zuGK7OccwKzueF9GUR9HUMam2kkl1zcX8fsPbcDsjw4elpEKtkf_2Fmwul3KpllAmrdNvWA16mIiwtX9_pCPbsHTX9xLHVPCKeRXywSiG6m2lo2Geyn1__0_eLtRGTZ1YVVpz1zu70eiir2jxQQnfadEGNYA0QzTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=a2jmMCGhGKsmZgm4_mHxVnOys4T007Y27yYw-wyKRsZio-94QliTU5wFLWagRDfLt-RX_LSo84utygOurOIYlnkDcl33ANyJxDrU9Gn6csi3jjtCXZB9yOVSEc2fI779I19XpRGy7jSLMvVi6xMzeFgBdX-qVzPLX11JqMtN0jpFfCF_1Yn_zuGK7OccwKzueF9GUR9HUMam2kkl1zcX8fsPbcDsjw4elpEKtkf_2Fmwul3KpllAmrdNvWA16mIiwtX9_pCPbsHTX9xLHVPCKeRXywSiG6m2lo2Geyn1__0_eLtRGTZ1YVVpz1zu70eiir2jxQQnfadEGNYA0QzTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76041" target="_blank">📅 02:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">@Ali_nor30
یکی از هزاران نفری که هرچقد هم منتظر بمونیم قرار نیست آن بشه، اونارو فراموش نکنید.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76039" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تو جواب سوال چرا نت پرو میخری؟ طرف میگفت چرا میری فیلترشکن گرون میخری؟ یه ناموسی هم میکشید بعد بحث تموم میشد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76038" target="_blank">📅 01:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBLpbLKqQD7Sq90jrBNATvySmBBzhbS-zmZwZA5nHZ5SeP3_vjzzGDkIB3BQbNqOnzQEX6YMjWVYkGgnyiy5xZD2_znWVeJLHHrcfkikJlH1hZ7jjyH5VaPPwCvDkrHtUT9Ma6iCAFEIMW1pamaUZf8iyiMH24mYvNRXn_z_AccZKl2BLC2e4Dik41GCdm8w-LNQTOsAdYi9_WA1jg23_txbZ2Ns6TUT2sJe0bPwe7JwfDI7O2OW-jDEZ7s7v-kFM1Z-14ivjJ8ezhE6qLdy26PLMJEOib5K977u1vVRR2qBL77DZ0hQiEWld7gqteLeYXhcxC5dEiC0VxAaS5H3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop | MEHI</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76037" target="_blank">📅 01:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP_FaPjLRtRKGzntqTtOT-Y1PdLx5oQDmBVkavF50GvfB7pITlR978XBwSw5HdaoC_paf0kuWYlIlpfcUW3HluPgQrN1QzKjQHQhgjwvC-PxCNY3Cc8W8qGu8KNBvbIdM-AUg_FCLgupHgqhxRiZaFR6qN6p02Kly7nezqdSrdQo42zwjj4VExv0ldYDJkEFY2B5odQ6gAWKt_PO6nWAmETGRJ8iQedu6_-6zRiAs1cmFYIERRRyoCgruJMVtW6WK4VSRvm4o1fm_dBT4NqfN3GPEK40CyB3HcwATfHDihTrTtwDaz2rUb-Y-MWoY-GtjkzQLiRI0Oe8ShJEJkUzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop
| MEHI</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76036" target="_blank">📅 01:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پروکسی های جدید مخصوص دانلود سوپر از تلگرام:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@Funhiphop
| Siavash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76035" target="_blank">📅 01:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyD0cMe7sNvWw0sS7zdNMGX3xD9vF1iz8CF0i9hHI2G37cJqDe_dwcwa8280RlsheZ9rASYNpwvSOJMrNYzCbcNVGgW5QrsGioIAV5rmLOaHE6H1VhfklXPqARM-79pHaTjU-zpFdsGrfuUTgSorcjMTH_cUQeAkTVoVbRtwEKLQYM9-ZXDZ8-uciu07B8mfEGUJx67VV-Xc7MSH2o-NIHhoeAmq4OQOH6YKXf21G8lUYBsaujbIsDwtL4q3TmGQo3Li97uWNxVKwHco2qjICkSV5Qc3mpH1tDlyA5gHVk0aWjBOebnczUaG0HO2yDKV9XXmH9cX56SRoO0wu80-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😠
ترامپ: با توجه به وضع بد آب و هوایی فردا، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق میندازیم.
موضوعات کمپ دیوید: ایران، دستاوردهای اخیر دولت در زمینه اقتصاد، کسب‌وکارهای کوچک، تلاش‌های ضد تقلب و تحولات سیاست خارجی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76033" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقامات آمریکایی به CNN:
وضعیت گروه‌های نیابتی و حقوق مردم ایران نیز بخشی از مذاکرات است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76031" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFqH88gT15O5pfsqCR6KOrEVTvK4mLxrOYSNp9AkLz5tAvZ_poc0ZnmFNRMJettC3jds7ifENflTjfjp8UsNhDEnJGzw7r9I5IPRKUpKP4hZFCzYktFIzGsPd9Ag4y9Ual1ybQVYCKsIFFNg_vBmZokfKoiVlH7RTqSs26xmkkdBD4O692kro5tvJYxYMzyj0sdN7xXRVvHAjYTAWlwjYeY8MHo3pYLiYKZKZVwaButpvULHxuLSyl8DUSINNq2Gcs7rQ4OTIZNR7DmO3QFRUAunZQIXC9lbuN1b1Ok-NzKIVY9DsmHGkeKwZ9WsAfpv6mb9_3rrP724cIwiOYTM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76029" target="_blank">📅 23:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTiemlPTYj0TfQhp-69JgPIgen8D4RnlBb9LF8_sVfJUdojstve0ERwWgTydo3GMX5sNFLSEToDy3lMPshT2F6cFUHIPl9Zun1Ur_sAVmOJxN7MLSa7L540BR98QYMZTt3JX6NEiByXMtIZRtnQcVm687t1Gk-K7DRmg8at-bjwi2NpcBNi8Rt2IW3aQkRxgreVw5VRIb-3MPavrmrxMjjWPDMdgQmwbpn9Y1qq7rDUO7Evlsr-4iUjFVjte_Zq_d-JsFcyINcZ9ZMeAF55e1QU0hld9dzQ9b04sluRcVEA41jq96lQrVKsr2Ay7xjVN5hf_Ucz5mvZroOXDoB_KMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست فارس هم جاودانه شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76028" target="_blank">📅 23:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوباره سرور تانل شده موجود کردیم!
🧃
اونم دوباره زیر قیمت بازار!
😈
💎
30 GB - 240
💎
50 GB - 390
💎
70 GB - 550
💎
100 GB - 790
💎
300 GB - 2490
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76027" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">دوباره
سرور تانل شده موجود کردیم!
🧃
اونم دوباره زیر قیمت بازار!
😈
💎
30 GB - 240
💎
50 GB - 390
💎
70 GB - 550
💎
100 GB - 790
💎
300 GB - 2490
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/76026" target="_blank">📅 23:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOhRGa_En5ygKEjwoyjquA7aoVK3PPQV-AYlacL7lSDjiK5G7VUSvBTdYgU5asPR8ob6JB_T0mqkAUKwBY6OA7OXUTGBLIPHB4aEdF4SHbNog_oJ_IrskhAy1_7N_HxaSPqyq_gFH-CzKAH677rs7stAe_lTO_A3JOsKH5HFev4qTOyQL69uXBPLBHd-DIIx_mInPgZkpoKoTVQPegG--uemiIAJfbeaYGOIUXqO3WnZ08Zns61C8kAFZUFCyqtWx-8mzLWafGu6NGt8co_IoxZUWmT4u9mJtFx3TFd8x03gtfnBPTZ4m7-CcHY3zxN7m-ET2Qz9ETsQmlQLB5S2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76025" target="_blank">📅 23:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانفیگ فروش اوپن وی پی ان نامحدود ۱۴۰ هزار تومنیم هنوز نیومده، دارم نگران میشم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76024" target="_blank">📅 22:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتم که وصل شد
بریم تایم لاین رو بگیریم دستمون با هشتگامون
✌️
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76023" target="_blank">📅 22:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نمیدونید چه حس بدیه از کسی که به کانفیگ میگه کانفینگ، کانفیگ گیگی یتومنی بخری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76019" target="_blank">📅 22:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانفیگ فروشا انقدری تو این مددت در اوردن که الان میتونن پول بدن از آمریکا F35 بخرن به ایران حمله کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76018" target="_blank">📅 22:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76017" target="_blank">📅 21:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حاجی دوتا2 چرا برگشته به عصر حجر شبیه دوتا 1 شده</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76016" target="_blank">📅 21:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تا دو سه روز سعی کنید با کسی تو تلگرام ارتباط نداشته باشید لهجه اپ داخلیتون از بین بره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76014" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbgcZDor7K-jSae2tHR0weZScaSGtVS293HqGuhvAyxwHHv6aszVgWNgjT1DLRXdST35KIwimrPk_BAHd7qbx2UWGL15GqAUzvBuRNQY-sEorkDZfY-EySUXDUXrPdlwZI3Re5Xm6z3oYzEbIcZbz1DnBtBjbDNIcPUIRhcx-fdcruhTb253WaCISmZsGK6ohmgg2hgxurgXzT-vJfeHFsJO1EZdHq3RCi0PKaGa9Z4G4FCFmAuHgxAqT_XGQiS51Z0qZn8GL11elz6-blASOfPsrkrSiMSPmqf19m3fv2WiRZk8vqZrIa7e4KduwFw50AR0H5Bzl7_ZU6eQgq9ZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">NetBlocks:
🫶
Welcome back Iran!
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76013" target="_blank">📅 21:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از منابع:
حمله به ایران پس از دریافت «پیام مشخصی» از آمریکا، در این مرحله از دستور کار خارج شده.
این منیع گفت که جام جهانی پیش رو و جشن‌های ۲۵۰ سالگی استقلال آمریکا عوامل مهمی در این تصمیم بوده‌اند، هرچند اشاره کرد که وضعیت ممکن است در آینده تغییر کند.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76012" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اومدم بالا پشت بوم ساعت ۹ شب
هوا چقدر خنکه واقعاً
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76009" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جدی جدی مثل ماست وصل کردن، چقد عجیبه اوضاع</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76005" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کصکشا درسته رو دستتون مونده ولی چرا باید کانفیگی که فردا قراره ۵ هزار بخره رو الان با تخفیف ۵۰ درصدی ازتون ۱۰۰ بخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76003" target="_blank">📅 20:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چی میشه که درست بعد وصل شدنتون اولین کار تصمیم میگیرید از فان هیپ هاپ لفت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76002" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نت خط هم برگشت</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76001" target="_blank">📅 20:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اونایی که کل این هشتاد و چند روز و آفلاین بودن بزرگترین کابوس vpn فروشا هستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76000" target="_blank">📅 20:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگه تازه وصل شدید و موزیکایی که چند وقت اخیر اومده رو گوش ندادید بیایید برید تو پلی لیست شیپ همشو گذاشتم
https://t.me/+7joX3IWJYepjNzFk</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/75998" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حمید رسایی، ستار هاشمی وزیر ارتباطات رو آنفالو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/75996" target="_blank">📅 19:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت ارتباطات: اینترنت خط های همراه هم تا ساعاتی دیگه وصل میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/75995" target="_blank">📅 19:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان به نت مخابرات وصل نشید امنیتتون به خطر میفته بد افزاره، بیایید کانفیگ بخرید گیگی ۸۱۸۹۱۹۱ از من
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/75994" target="_blank">📅 19:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب نت وصل شد و میتونم بازم ویدیو های مورد علاقمو ببینم تو اینستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/75993" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmd1BThrtYpc8nDo4Snir_wi4MGgtwNDYHySpmEtSlO7q7HT1_n5S3Yt14fNkUhKVJhWlogUHuKLLiuQKmImhRhcd3pUKR6JgEG5-5jyqneZrIJX7otqQ3Y2mUkfZqxsGJ-XSbGGl2mrGYbxkutwbujQpzuxGROZLuz9DhDIv3B9xCQwcPetUYUB_xJ55xLAStpesXWYJKSIpHqFH1OnT1CNSbWqQckoF1Fuct6wrfDXw1rYVRy1dY-eo8KHY9ap3H2tth4gLdiUdvPtunbz92olSAuTCys-WYJffPMix1CCjokEqSjugnBS5jYMh51jeFe1SOeBcbVFndQSsAXpCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g5
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/75992" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده بدون اعلام رسمی، کمک به عبور کشتی‌ها از تنگه هرمز را دوباره در قالب پروژه آزادی آغاز کرده است. مقامات گفتند نیروی دریایی قصد دارد در روزهای آینده به حدود دوازده کشتی، از جمله ابرنفتکش‌ها…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/funhiphop/75990" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وال استریت ژورنال:
به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده بدون اعلام رسمی، کمک به عبور کشتی‌ها از تنگه هرمز را دوباره در قالب پروژه آزادی آغاز کرده است.
مقامات گفتند نیروی دریایی قصد دارد در روزهای آینده به حدود دوازده کشتی، از جمله ابرنفتکش‌ها و کشتی‌های کانتینری، در عبور از این مسیر آبی کمک کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/75989" target="_blank">📅 18:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ عجب کصکشیه، بهش گفتن پول بلوکه شدمون رو بده اومد گفت خب اونو نمیدم ولی ۱۲ میلیارد دلار وام میدم بهتون، گفتن خب بده  گفت نه دیگه من وامو میگیرم دادنشو قطر میده بهتون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/75988" target="_blank">📅 18:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ عجب کصکشیه، بهش گفتن پول بلوکه شدمون رو بده
اومد گفت خب اونو نمیدم ولی ۱۲ میلیارد دلار وام میدم بهتون، گفتن خب بده
گفت نه دیگه من وامو میگیرم دادنشو قطر میده بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/75987" target="_blank">📅 18:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رویترز: قالیباف و عراقچی با پروازی فوری و ناگهانی اکنون در قطر حضور دارند. مذاکرات باقرشاه و پروفسور عراقچی در دوحه بر پرونده تنگه هرمز و اورانیوم غنی‌شده متمرکز خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/75986" target="_blank">📅 18:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وی پی ان فروشای عزیز چرب کنید که قراره از این به بعد ساعتی ۵ تومن پول تبلیغ بگیرم ازتون</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/75984" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-xsQ-nPh7u-DjqX0BwiAxmcs_TxVJoPisE9MvEATpz2PkRriKFlT1g0C7XOFpsSnFhLdi0Q4t6BbCx9Ig7HHbYsI-ljsc9P_egr1nUqItAihoRbnKKlpOjWjlfxxsVw2uGSKPgpaqD9H9rJ4hCWkTLYzUtjuY7nP0EvITgVi6ugHEadsu1V_V3YQu09NSdgKRzJF3It0ZEqpz2-J5LVsyi6A4L8iQJJSMZ0R2Dyvv6ZvlKs9it6onYeo_QdMUo2CX8CHmhCCbDC_YzSjL7uK4-IHZaZvBLbtXTpMNr331ovcyCEw16Q0JbeMnnBj5Pux6OoD5NYjjm6y0YxrxAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعش کنید، قطعش کنید خار این اینترنتو گاییدم قطعش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/75983" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلقک بازی میکنیم ولی حقیقتا من یکی نمیتونم بابت برگشتن نصف حقم خوشحال باشم و از کسی تشکر کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/75981" target="_blank">📅 17:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ای شیر زخم خورده، به خانه خوش آمدی
📱
ای پیر درمانده، به خانه خوش آمدی
📱
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/75979" target="_blank">📅 16:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:  من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند. می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد. توافق بد توافقی است که می‌تواند به دولت اسرائیل…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/75978" target="_blank">📅 16:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:
من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند.
می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد.
توافق بد توافقی است که می‌تواند به دولت اسرائیل آسیب برساند، و ما اجازه نخواهیم داد این اتفاق بیفتد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/75977" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وای اگر پزشکیان حکم جهادم دهد</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/75975" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آقا خوش برگشتید
به یادتون بودم، همش میگفتم ممبرای فقیرم بامزه تر بودن</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/75973" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تا 1411 با پزشکیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/75972" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ore7p80IHfdZfctPSmOmkfN862fTfKaUVEngC_WGg4ZULsyOtQiI35Jesj7rMeJhdyIm784ypXPaVxdI7CMVpIxvypTOK4JVWoXXL7KZvgYXHEHR4va253qqrY11AuZiOubfD8VmKtgnWRXmCzTTpLVcgfaIY0vfAdcSUpEVSR3v_5728x0u6VYe-pfhnPYSy6DKqABkk-s3XlY1jUv8JJdyD8wP2wf1qopwj6uDhuLwLqJlFk8ZYxywoTdiEqwTCOVEvGN4g6sFpwAv0VWWuRVkywOvGZ2AgpT1jAaFJjuXAKICzu1mPTeF7jIrUJrR5POvD1ug2RN2mwhhRcL7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت مخابرات وصل شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/75971" target="_blank">📅 16:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حاجی من تو اورژانس بیمارستانم
کلی ادم رو دارن میارن از رنج سنی ۱۵ تا ۵۰
بطور عجیبی گروه شغلی همشون تو رسته وی پی ان و کانفیگ و ایناست
@FunHipHop</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/75969" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آسیاتک و مخابرات انگار دارن منطقه ای باز میشن</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/75967" target="_blank">📅 16:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات : فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/75966" target="_blank">📅 16:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات :
فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/75965" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه یارو از ۳ ماه قطعی نت ۲.۵ ماهشو قطع بود، الان تو چنلش زده تو شرایط سخت کنارتون بودیم از این به بعدم هستیم</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/75964" target="_blank">📅 15:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه آپدیتی رو فیلترینگ پیاده کردن که یسری از کانفیگ پولیا هم قطع شدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/75963" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عجب ماجرایی گذاشتم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/75961" target="_blank">📅 15:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کونیا من روبیکامو پاک کردم تو اون ۵ دقیقه
نمیزاره اکانت جدید بسازم الان</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/75959" target="_blank">📅 15:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/75958" target="_blank">📅 15:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/75957" target="_blank">📅 15:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یسری ای پی کلود فلر باز شده که دارن روش کانفیگ رایگان میزنن، ممکنه اختلال باشه و یکم بعد ببندنش.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/75956" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خر کونتون بزاره ولی الان جای اونی که تازه پنل گرفته نباشید</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/75955" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یسری ای پی کلود فلر باز شده که دارن روش کانفیگ رایگان میزنن، ممکنه اختلال باشه و یکم بعد ببندنش.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/75953" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd-XQ577wibpc5IkDewj2DN8oag8yNhRpCuJ0XZFc9vF2hP6QLF8ykfx69xJteeBsQ6YODQy6VayzyVjuIj0owWP9013LczmAZDPzjHCMxf5tDtCZI2cCzpntfDX5Xk__zSUagFCyF3MepkdRPsDZt-mjfBMw6p7HCZIOYqH5qAvPOK1OR8FW3Gv3A2lQ01IsI9a6JQ_yQ5WB9DJBUEXorg_lQgpnR7UfkSFg0UNWgfv0n3ZRBqePp3UPxFLcEB1KHGR-wbgy51tE5Njd6ECpNGttui2sM7N4kjp-Tm1In_q-wKtuCap4V3zI8I9_PAWe2_eBnU7IdkwEPc6oHGdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه:
آمریکا دیروز به طرز فاحشی آتش‌بس رو نقض کرد و ما هم این اقدامشون رو بی‌پاسخ نمی‌ذاریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/75952" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این مادرجنده باز شروع به کانفیگ رایگان گذاشتن کرد، فک کنم داره وصل میشه</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/75951" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بیایید به زبان ساده کیری که خوردیمو تعریف کنم براتون
اینترنت رو کی قطع کرد؟ شعام
کی میتونست وصل کنه؟ شعام
رئیس شعام کیه؟ پزشکیان
حالا راه وصلیش چی بود؟ پزشکیان از طریق شعام نتو وصل کنه
اما پزشکیان چیکار کرد؟ یه ستاد غیرقانونی برا وصلی اینترنت ساخت
نتیجه؟ از اون ستاد شکایت شد و رسیدگی به شکایت‌ ۶ ماه طول میکشه
و اینطوری شد که بطور
کاملا
قانونی وصلی نتو ۶ ماه انداختن عقب
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/75949" target="_blank">📅 14:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75947">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پزشکیان: ۱۶ میلیون رای در انتخابات ریاست جمهوری
رسایی: ۲۴۰ هزار رای در انتخابات مجلس
قدرت اجرایی کدوم بیشتره؟ رسایی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/75947" target="_blank">📅 14:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وضعیت آیندتونو کامنت کنید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/75945" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابع آگاه به فارس درمورد پیشرفت مذاکرات دکتر قالیباف:
گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود که با میانجی‌گری و ابتکار قطر
در حال برطرف‌شدن است.
براساس این گزارش، پیش‌تر آمریکا نسبت به اجرای تعهدات خود در این زمینه عقب‌نشینی کرده بود، اما ایران با پافشاری اعلام کرد «تا زمانی که پول‌های مورد توافق واریز نشده باشد، هیچ توافقی ممکن نیست». نهایتاً با رایزنی‌ها در قطر، پیشرفت‌هایی برای حل این مشکل حاصل شده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/75944" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسعود چقد دیگه باید کیرت کنن استعفا بده برو دنبال زندگیت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/75943" target="_blank">📅 14:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیروز پزشکیان تو ستاد ویژه ساماندهی و راهبری فضای مجازی کشور، وصل شدن اینترنت رو تصویب کرد.
الان فارس خبر داده که یه سری افراد ناشناس شکایت کردن که این ستاد کلا وجودش غیر قانونیه و رئیس جمهور اصلا اختیارات لازم برای ایجاد این ستاد رو نداشته، پس تا زمانی که به این شکایت رسیدگی بشه مصوبات این ستاد قابل اجرا نیست اصلا.
😊
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/75942" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPhMucoKRU2wiF6ydwyiInIuTBttG0AVqV-d5wF0wlP27Du-UfzGJxW61FBrx25jLoJDFwcrq6RixYuxEqYtZMLsX5IZzRVnfzlY30Jk2TJEYKllpBCEXgQf-vOizS6p3PVYaH3eO2ooZMzX8HuiSORuc9-wK8DM5vqU1MLeSCdRM5q1YY3Qw4xxhaAxC2L20GRmw18JHtu_sp_5DTWjbh8ueZ8vH7hRljhOURFXK-lf6d-n7UZ49V0DCvteg0xS0kXVw-Fi0uYr3UkGKz_vUhW_rq4e3ZPdITGE2CjWvKav2yh68NfsLEYFFeSO97j0BmRf48b_KssgrAZMII9mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی بمب اتم میاد</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/75940" target="_blank">📅 13:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بوی بمب اتم میاد</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/75939" target="_blank">📅 13:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اقا مجتبی:
همانطور که پدرم سال ۱۳۹۴ گفت اسرائیل ۲۵ سال آینده را نخواهد دید.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/75936" target="_blank">📅 12:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حس میکنم پزشکیان تستی ی چیز گفته ببینه تو نظام حرفش برو داره یا نه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/75935" target="_blank">📅 12:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خداروشکر جزٔ تنها چنلایی بودیم که اصلا تبلیغ کانفیگ نکردیم و مهدی هم بیخیال پول شد تو این سه ماه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/75931" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERKOVDxDACorFJbB8dy7R3zHRjSjiVoI1bBvZNnn2fNAu7NrcnC-CS8ut57CSR6yUuHLU11iWxPfaAmqCRCtJ8r8wVdpxQ8I-n5oG7d_Y203P3iJ1jB8wyg2t-4DQL1YiwKf-JWyipTyWjyoJzjXz37821P1vY8ReHFugYwVmQOCRjzldfGEhslsrmpLQd6pYMgIbEyPk2agY4CbkG2u5VyT1baJfbexm5TKP9V_5ScorB1vEffrpHYzH6cDB7FhC6v55qifT0fcpJRHPaduKlhxaPGO6EEfB9-hd7tYuTWI36wsLvcKTvbW_VY5xXdXCBiSG4FNKSJqf2XIIIDoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار نت بلاکس که آمار بالا رفتن وصلی هارو نشون میده</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/75929" target="_blank">📅 11:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خوشم نیومد
از اشتراک معمولی ChatGpt استفاده شده، زیاد جمله بندیاش دقیق نیست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/75928" target="_blank">📅 11:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کصکشا گوگل پلی تو حالت عادی هم فیلتر بود، یعنی چی که میگید باز شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/75927" target="_blank">📅 11:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پی دی اف بزارم براتون؟</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/75926" target="_blank">📅 11:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یادش بخیر
ماه پیش همین وقتا یکی از ممبرا رفته بود کانفیگ گرفته بود برا پورن هاب، ۲۵۰۰ هم هزینه کرده بود
بعد لوکیشن کانفیگه فرانسه بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/75925" target="_blank">📅 11:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یعنی بالاخره پزشکیان تونست یه گوهی تو این کشور بخوره؟</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/75924" target="_blank">📅 11:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75923">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شهوانی رو یه سری از دیتا سنتر ها بالا میاد
باید ببینیم اختلال بوده یا جدی جدی دارن نت بین الملل رو وصل میکنن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/75923" target="_blank">📅 10:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اونایی که اینترنت پرو خریدن دارن کیر میخورن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/75922" target="_blank">📅 10:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ظاهرا جیمیل رفع فیلتر شده باید ببینیم اختلال بوده یا جدی جدی دارن نت بین الملل رو وصل میکنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/75921" target="_blank">📅 10:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کصخلا بزارید کامل اینترنت بیاد بعد برید پیوی وپن فروشتون گنده گوزی کنید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/75920" target="_blank">📅 10:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2o_TJzcY4rYodeLkeDqt1YTB1FNoIDCFxUwmt_c2eZF8de7GBfk2e47LddX4cDydXNSrIhEHkuzjEgqTZmmPOF8AdrP9FZ4haUKXKuswLnLwGDSi_-kUNZLOfan-HaxJcknhG4_IB1vumYTN3bEJuEpVoOXTvOlmmOVNvJteyM7a3lmIVXjxN3BwN6dz2hIpN5mBe0CZHLLTCfkI819iIPJnY7wWHtK6MTFWF1rZtPGm59Om2hazTwQBZtfCp-fZsC17n21BPegRKujzRa1zWFBeO5VdHhCXiWLSkHKZF2ZI8NYYDufxY9h1R6cCw2OWjbgw40kHUhrPBNaVpf50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا مادرجنده آلوارز چه گوهیه ژائو پدرو بیار  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/75919" target="_blank">📅 10:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لاپورتا مادرجنده آلوارز چه گوهیه ژائو پدرو بیار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/75918" target="_blank">📅 09:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbIPC_GI21PEdcu1LxZ5yB3-HrD1qnSQ0Jp8Nh5_KrGu4aW_luXLo5UEtv0zpUghweb9uZIO82c_tYne2AVCO12Xmp988P0MnLg4_3HxKBVGq8_eVo90SNjPAv8Q-L3_QlkhJ7ZHS-tC3lGxpj6aP4KMzasIP9uIUn3oweTaxVAAgz7ysmcs29mb1owUy92TDrJMZXy8noyXQx8YRZvVhhElBy9L-YX_Y6ti2j2Qy0n8OsdqI4dTbYzBQJ8txZKePuiq5-lF8UNBLvd8vXSV6UrYGI6vMov-CedUME4YNkF7PtdbZencNnBhgqXE-T7nPkMiYNgdHvQSFhd3RGKQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ 2014 یچیز دیگه بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/75917" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/75916" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن اندروید سایت جهانی دربی بت
💰
اولین سایت جهانی با امکان شارژ و برداشت ریالی(کارت به کارت)
🔗
برای ورود فیلترشکن روی کشور مناسب قرار دهید مانند فنلاند و المان و....
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/75916" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJmVR6JIHEI9jNRs9B53Cb5jNdNZrZhy9No3D5qZwipqrAtv_2pvgbF4Ekh7VBU_70ZRIqRw4NGs4athwz-jJzqOtNHlwaVKbwWAvzLw79L3-3F0epOdNsGhsZYWkIEerd3XgBQ2_kn9SM02MHEZrUhbkxcBIDEmXWK929I1v0kTF3J843SWiZs1Ig91f5_JjqvB_Ql7TQwu4gWTe84Ztr3yUum57sM87GQBPQYib-Fq5AfPBWpsX_8H90iEr-OecEQHs4Z-wyuvrhsiShf30dySIpxgrU3g1ggwJ91b4vHA04BFCmuqmq0yLCpXVJIn6IsiYIl8IZVQP23wBwOsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :r5
🅰
🪙
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/75915" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75914">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ369zuG87DtdWcRwWpq41blT0X82CrVxHEpblJcPwHvuHoBJqkota4u6Rjr0B1M8BuajWU0YO0jQcaOBLUwbY-AYsaXB2aAUv0tXIzPXlUf-UtMokYkmZL5OwKId6l2AStWag_MwqiIUVD5SJLXc2hEGoqgCShW9ST4hI7KULYpQjf2f8UKO77bq3bLzcgOYaNKw75bEvHEdOs8teOo72dZ2eWHNl9QdCbbj51-N0TuClrCkGP7NMXS5OvvRAerquKWdLsEKuIdoZTg0JSM5dlJo-7vr0GSHEwJEz7PbNWbokoUeyEmQaNXlxrQdmq_BVRUwGULlsOBWPG6xjF0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/75914" target="_blank">📅 05:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli .</strong></div>
<div class="tg-text">داداش من خودم قایق مین گذاریم ولی بحث بحثه وطنه</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/75913" target="_blank">📅 03:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75912">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خلاصه اتفاقات به زبان ساده:
تو ۲۴ ساعت گذشته سپاه در جهت اطمینان از روند مثبت مذاکرات، سعی کرده با چند تا قایق تو تنگه مین بیشتری بکاره و با موشک‌های زمین به هوا هم جنگده‌های آمریکا رو بزنه.
آمریکا هم برا نشون دادن حسن نیتش و امتیاز دهی، اون چند تا قایق مین گذار و اون پایگاه موشکی‌ای که ازش موشک‌های زمین به هوا لانچ شده بودن رو نابود کرده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/75912" target="_blank">📅 02:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام آمریکایی درمورد روند کاملا طبیعی آتش‌بس به الجزیره:
ایران در ۲۴ ساعت گذشته تلاش کرده است به نیروهای آمریکایی حمله کند که یکی از این حوادث شامل شلیک موشک به جنگنده‌های آمریکایی بود، ولی هیچ نیروی آمریکایی در نتیجه این حملات آسیب ندیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/75911" target="_blank">📅 02:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی سنتکام درمورد زد و خوردهای امشب به فاکس نیوز: نیروهای آمریکایی امروز در جنوب ایران حملات دفاعی انجام دادند تا از نیروهای خود در برابر تهدیدات نیروهای ایرانی محافظت کنند. اهداف شامل سایت‌های پرتاب موشک و قایق‌های ایرانی بودند که در تلاش برای کاشت مین…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/75910" target="_blank">📅 02:49 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
