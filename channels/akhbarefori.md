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
<img src="https://cdn4.telesco.pe/file/mQBaxr-SSSc6rXZlBpKSeNrbyOyXdaXfeSWmdAj8wC7jTq-KWUEXmiUYyAjmKB6Vno_tl8OjKZMw2KI_ZAuQHxERZgpi2wf07g0EOyT2xgZ2D-bIuj3ukA39VbthYLahoIcMOgVzPuzX0qfu-6eUSyAbx67rnSE5nYYZrsaGIE6FSUbi66RWf2YS8WdfLPuGOt6MBnxs0NPJ3RnXu3qxPQoVxAKKy5y1zgdyfIbK6rbuT1g5jdIKN14bK8gIQSzn1zDI-s-I5pseFv7gAO6T4eanqoqPLf-0LFbz_cP4og7LiqgqmOKtubHciKfvJJo0TEsEqsEBkrO1rp0GZxbMbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 13:51:29</div>
<hr>

<div class="tg-post" id="msg-654795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-VKMRcK6Z1LZdaFct57EvVBKzylK9Pb2pvIIXG5H5dkeQkwSCkwLfym_Cmcn59QxDfB2yM_Lm0YIDV2d4ElPvlkEJqPNGxb21_TspxilINgFnZinqy5yj8c1O8wtwIO-7VI_jg49KK8O0HuOqVU44qDEU3Io4oznhTyYzJT3yualm4_ZHL6F0mro8wscRiMA13yllaM3BOqlYqTrE-Xkyi5xrEawEbOWJY_R2lCbYx0XktTK4kHlI0IPZPcVVsE9TNysn1e4bIMMXlii8dck1IrZrG1NnvfEB34oqzd_UGm03NVSL-GAeundPH_0M-QGvmBFJrl2XdasWd4_cgrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ناخودآگاه یک چشم خود را می‌بندیم؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/654795" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72773a59c.mp4?token=QNxY8GeVnR5cro54blRq31d-Us72kBPsLmC4c2MKmz0AP3_AM3y0Tyo1tT7cqhOilsQrwIwVmL2ePf84l4uUtzauyVOYhnpOPI2d9Ai_tL2MF7yVttf2rZDIG4SmlIO1wPFjuL7ec739Mu5wndLg2JQfmkDCxLasBJDpEIFyJqASBCM7zoUB_pVVrQ6xuZcD2XmVltritQGpXy9QPul3RClVGXJhreXg3a6gGtqHU8dPlPRq44uYtTTdm61nJbYCLgcw5kLhl3pXr9oAhYEh6OmbrJc4iLY8fpzxMF06eg0F_1Y14TzlPOEdrYb-1FQeICCJRC21EkkL94XF_rXfaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72773a59c.mp4?token=QNxY8GeVnR5cro54blRq31d-Us72kBPsLmC4c2MKmz0AP3_AM3y0Tyo1tT7cqhOilsQrwIwVmL2ePf84l4uUtzauyVOYhnpOPI2d9Ai_tL2MF7yVttf2rZDIG4SmlIO1wPFjuL7ec739Mu5wndLg2JQfmkDCxLasBJDpEIFyJqASBCM7zoUB_pVVrQ6xuZcD2XmVltritQGpXy9QPul3RClVGXJhreXg3a6gGtqHU8dPlPRq44uYtTTdm61nJbYCLgcw5kLhl3pXr9oAhYEh6OmbrJc4iLY8fpzxMF06eg0F_1Y14TzlPOEdrYb-1FQeICCJRC21EkkL94XF_rXfaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزش باد شدید در شهر مودانجیانگ در استان هیلونگجیانگ چین، بخشی از سازه سقفی یک ساختمان بلند را کند و ورق‌های فلزی بزرگ را بر روی خودروهای پارک شده در زیر آن پرتاب کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/654794" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a875a5132.mp4?token=FT7CEqc9nCGeHH_E9sYvziWkrDay1EbhauGXKkmnotKkxp2wUZgs_sUTeWgeeEp_VDP1atuhslqCsnUtDplzpZBhQRbiybRRvaFy4VHqpAwnjjqVxhK_QBr52tT9om1NRaFKFrKdeJFGS6UjsFv4Gen59uIvj5NuieXIDSTcOEoRXLH_nsioxw6fozbe3h-GdEEdQeSDTWIcj2bmqfl1VombvOxVO8py8EztaiXHh_yDwKLTF-3yA4GozGw-0iJ96oTvQQ0yh1698xPKwPP6xZEuR3ScqA6ykpoP49yxZ2164_Iv9IzwbYOLVdQgZaZpN5Km9cAqqYJApGYc31bfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a875a5132.mp4?token=FT7CEqc9nCGeHH_E9sYvziWkrDay1EbhauGXKkmnotKkxp2wUZgs_sUTeWgeeEp_VDP1atuhslqCsnUtDplzpZBhQRbiybRRvaFy4VHqpAwnjjqVxhK_QBr52tT9om1NRaFKFrKdeJFGS6UjsFv4Gen59uIvj5NuieXIDSTcOEoRXLH_nsioxw6fozbe3h-GdEEdQeSDTWIcj2bmqfl1VombvOxVO8py8EztaiXHh_yDwKLTF-3yA4GozGw-0iJ96oTvQQ0yh1698xPKwPP6xZEuR3ScqA6ykpoP49yxZ2164_Iv9IzwbYOLVdQgZaZpN5Km9cAqqYJApGYc31bfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکورت هوایی پوتین در آسمان آستانه از نمای کابین جنگنده قزاقستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/akhbarefori/654793" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
معاون سازمان سنجش: تاثیر سابقه تحصیلی در کنکور امسال برای گروه‌های ریاضی، تجربی و انسانی ۶۰ درصد (۴۳ درصد پایه دوازدهم و ۱۷ درصد پایه یازدهم) و برای گروه‌های هنر و زبان ۳۰ درصد است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/654791" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اقدام ویژۀ فیفا برای کاروان ایران در مکزیک
🔹
درحالی‌که کاروان ایران برای انتقال به شهر تیخوانا برای برگزاری کمپ خود در جام جهانی آماده می‌شود، نشریۀ اکیپ فرانسه از امنیتی‌شدن فضای شهر مرزی مکزیک به‌خاطر میزبانی از این تیم خبر داد.
🔹
طبق گزارش اکیپ، ٣٠٠ نیروی امنیتی از سوی فیفا مأمور تأمین امنیت کاروان تیم ملی ایران شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/654790" target="_blank">📅 13:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc49f4bf9.mp4?token=hentuXZdJyDUVkShAJaKBcoucBcegrMg6w8-YFS744rat5AkzJ3tbFzwEgKSsfGuVnhAR_DhSwHg6Yj2kQ4r28i20U8wbPhrv7WsXLxuHvmwpxCKU3GyqJodQC9wKSi28ZA3ujGImoH4fSdET-MCp5-sz94aQXlEm_YwmTTJRkdD4X9sGLLTSpd4UPr9o-olvGFQLec4LwRl_sqWIb8DckQUUkXP-iZD1nWihKm4c0wX9tf8RnIp0s5ffBah4PrX9a9pkVqm4iUqDp721BG7WmH1aOuzlctAx4YIhlO91OuwaHyK0gPr0eXTHjHj-peUh7qvY1n86Kd8j65CWf3VDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc49f4bf9.mp4?token=hentuXZdJyDUVkShAJaKBcoucBcegrMg6w8-YFS744rat5AkzJ3tbFzwEgKSsfGuVnhAR_DhSwHg6Yj2kQ4r28i20U8wbPhrv7WsXLxuHvmwpxCKU3GyqJodQC9wKSi28ZA3ujGImoH4fSdET-MCp5-sz94aQXlEm_YwmTTJRkdD4X9sGLLTSpd4UPr9o-olvGFQLec4LwRl_sqWIb8DckQUUkXP-iZD1nWihKm4c0wX9tf8RnIp0s5ffBah4PrX9a9pkVqm4iUqDp721BG7WmH1aOuzlctAx4YIhlO91OuwaHyK0gPr0eXTHjHj-peUh7qvY1n86Kd8j65CWf3VDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست از اعضای AUKUS خواست هزینه‌های دفاعی را افزایش دهند
🔹
پیت هگست، وزیر جنگ آمریکا از اعضای پیمان امنیتی AUKUS شامل آمریکا، انگلیس و استرالیا و همچنین دیگر متحدان واشنگتن در منطقه خواست سهم بیشتری از هزینه‌های دفاعی و امنیتی را بر عهده بگیرند.
🔹
دوران حمایت امنیتی گسترده آمریکا از کشورهای ثروتمند بدون مشارکت کافی آن‌ها به پایان رسیده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/654789" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsDD4lxwcyaDPQbSf4eL6fR9zx9ffqGa67ClIssXXbxSx5JE282cGkZ0gFvzm66E4jCSkYzaBzkyuoRhkFHqU4hue3MjejQaLeMlYrd-MFPBulBeK41oD_QcHfOWZsyC_E_E411WIPXmdfypbMai0EFp-hK6eJTAlgZJTe2eh6CriALuvUao6slxONtVULSN-xn9c6P-H1fzsRXuX-IMAfM6qwikjiIeK79BPuNFUyI6L2foEWgrxUgU-bQU5VDozbhwSzK5F7rsTUuvrVPqZdx7-xyprrJ-HQFcjOVLw27NWhj89VOpbP48hnrYvDVmfBMcejH7YAWuBrH7jtMTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f1a9df90.mp4?token=vYVw9MWcfuvE_7gDnvdYj-gaYo4G9JclevFrybgf-OPG2VSr2z_6Y17d0R-omWUI-kU8cpHlmY_VLCvGkR5ZJb3hNwe2eAE1vrH7bBLUm6p4xpYwo7Od_x8XLiDJO_hPRF3s2feVkD7A6egLFxUL2nj1rqQAXFWqbxIFgH4p5YZg28HpcIE6pDXM28SoZxjxm5zsZAtqUrvK92aabp9v9ytAPYRGKN54mFrnCVBj8k4mvEq0v3iYMlkEcI5OLSCSy_cU1CELOT7o8xDCWOKz_B9MnAsg8ZUX8bkD8uG0vrprIeNRaeHyQ3w9XqovcNnG1gkOTnKYyZXZu6Il4Hr2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f1a9df90.mp4?token=vYVw9MWcfuvE_7gDnvdYj-gaYo4G9JclevFrybgf-OPG2VSr2z_6Y17d0R-omWUI-kU8cpHlmY_VLCvGkR5ZJb3hNwe2eAE1vrH7bBLUm6p4xpYwo7Od_x8XLiDJO_hPRF3s2feVkD7A6egLFxUL2nj1rqQAXFWqbxIFgH4p5YZg28HpcIE6pDXM28SoZxjxm5zsZAtqUrvK92aabp9v9ytAPYRGKN54mFrnCVBj8k4mvEq0v3iYMlkEcI5OLSCSy_cU1CELOT7o8xDCWOKz_B9MnAsg8ZUX8bkD8uG0vrprIeNRaeHyQ3w9XqovcNnG1gkOTnKYyZXZu6Il4Hr2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش برف در خاباروفسک روسیه در آستانه تابستان مردم را غافلگیر کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/654786" target="_blank">📅 12:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
برگزاری کنکور سراسری فقط در داخل کشور  رئیس سازمان سنجش:
🔹
کنکور سراسری و پذیرش معلم_دانشجو برای دانشگاه فرهنگیان و تربیت دبیر شهید رجایی در داخل کشور برگزار خواهد شد و آزمونی در خارج از کشور برگزار نخواهد شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/654785" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FReRDVSftVNCXnyqhXOqBq1pDWSB31y9NZZPEx-s4C7XbIgMdf5Tuhli-NWeYk6H1yELOODyaTS1X4Du0KW-WEPJX_TuYe1D-x-_WGY3xoM55tiF9ehh26AKA-OvX3iBq3NqWjnHq9601F514xYtpjOOl_wJXhyPTPfNq7RAx5survfCrrkDvP4b_Y8PC5HIYO51Qne0u9A9-FyJPVQ5OhD2y2E2NAac66UNbcu3uNel6zleUIJa0eV2eUVO8iO-XoE2JwCVb7DqTriPFjeoul5RcCKlN67pnFD72qM8172Sd50ZuCasaPAbQSOJuljRfq2c8G8rV-HhoFW7-fw2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار گرمازدگی؛ آب فراوان بنوشید و منتظر تشنه شدن نمانید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654784" target="_blank">📅 12:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
هلاکت ۲ تروریست در درگیری با مرزبانان چالدران
🔹
فرمانده مرزبانی فراجا از ناکامی حمله عناصر گروهک‌های معاند به یکی از یگان‌های مرزی چالدران خبر داد.
🔹
در این درگیری مسلحانه، ۲ تروریست کشته شدند و تعدادی دیگر پس از زخمی شدن به آن سوی مرز متواری شدند.
🔹
از مهاجمان یک قبضه سلاح M16، ۵ خشاب، ۲ نارنجک دستی، یک گوشی تلفن همراه و تجهیزات انفرادی کشف و ضبط شد.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/654783" target="_blank">📅 12:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
زمان برگزاری کنکور اعلام شد
🔹
رئیس سازمان سنجش آموزش کشور از برگزاری آزمون سراسری و کنکور دانشجو معلمان در روزهای پنجشنبه و جمعه ۲۹ و ۳۰ مردادماه خبر داد.
🔹
کنکور کارشناسی ارشد ۱۴۰۵  ۱۸ و ۱۹ تیر برگزار می‌شود.  جزییات بیشتر
👇
khabarfoori.com/fa/tiny/news-3218868</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654782" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654781">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jClo-f_LTYTgXvhi-SvTiFcMuQedlCNq1buTmiOhrmV5RPUA3VbwftMuAEHsQx_Rtv-Oa7EW-K5NLuadyf32FpnIXvIl7AEfxE1cneFwb76rhvN3TKna308iyvwt95DuOGHY_ELwxkoacaxdoy05PJRVZQuDQMkCUIwF2kym6o4HR2s3xQzAlExjCniwa67Bql209NfUSqQy0dZv1_c-JoifjJtV7MUyJpXl7sz8cmCD0mS9TjVYyRkrn5HUruT8WrA6CAkedSGEutSNi9BNTLye4QLh1TAzBkOB_hxbi1q5rK1OxGwuKT-XGbsn2hq37YDD7rFpGrigU1IvAT2n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/654781" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654780">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4NBbYWFlE-5KkKmzvmWgXMU-f-IQ8ewhWPWurBaAOSRG8m9WrdbSnsf0AxLyNk_RiN_thb-NCq8N2-uQ-Uu7Vx62giiu7TUTmzikA80DMyVut-JFA7TCaj7850yPUAZ9rc5jJgyFm6qM6vz28TdoZVbQFnGTu2zXiSNvoz4JvFPl_mrR9u_b1XuPiBTrFccK1Krn4CAKZUkdqoWLXH9p-4lmjSyGrtuIuGC4r-yaiC9QCa_wCkLmwQiQ21AVqsLKKYn64sGjEKGNK2IHRR7rOKgPd-bHmg8N2Agza689iBIBml_HvMDxrt9Vl5Gz86_XsifUTYDtc8z8PuNWyALnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامسونگ قابلیت «پاسپورت دیجیتال» را به گوشی‌های گلکسی اضافه کرد
🔹
کاربران آمریکایی می‌توانند اطلاعات پاسپورت خود را به‌صورت رمزگذاری‌شده در Samsung Wallet ذخیره کرده و در بسیاری از فرودگاه‌های آمریکا بدون ارائه پاسپورت فیزیکی، هویت خود را تأیید کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/654780" target="_blank">📅 12:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654779">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فراجا: زائران اربعین گذرنامه‌های زیر ۶ ماه را تعویض کنند/امکان تمدید گذرنامه به‌صورت حضوری و غیرحضوری فراهم است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654779" target="_blank">📅 11:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654778">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کشف لاشه‌های پهپاد متخاصم آمریکایی ـ صهیونی در آب‌های خلیج فارس
🔹
لاشه‌های پهپاد متخاصم منهدم‌شده ارتش صهیونیستی آمریکایی توسط دلاورمردان پدافند هوایی ارتش جمهوری اسلامی ایران مستقر در جزیره قشم کشف شد.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654778" target="_blank">📅 11:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
کشتی ایرانی با عبور از محاصرهٔ آمریکا
به خانه رسید
🔹
داده‌های ماهوارهای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کیوان با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی(ره) رسیده است./فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/654777" target="_blank">📅 11:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aaf6b7ee2.mp4?token=LiYvT_jrhy7VY_y6pZ8eecRi7Kwwdba1JPslI7XUY7V0IdLCqC5MaDo3VNOVLUjQevpp6SASMxTmKKPYDDUA3NEZbJ7nUvjherTQ_1hyGlN-CNUYkOjD3vrLGBV1iUTMdWAGBpdr-IPdZsNmw2M3Swhzbh8E9M3kWajcV2U7pe3Ie8dBI5kOs46648nm1EmLuiQ48k1WFSC5E4u4xZqOaC_Ys3g9YBDdeqGNPn5OO1HKsuQF0WVenRFd6ORhus4zQC1MQ-CelgSvTp64oPtWhXTOZR8lSONFtp8kTHbKbXQ0R7GM3-ZMYmDfvLlOJNDPquZrknR0fBKepb90csGftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aaf6b7ee2.mp4?token=LiYvT_jrhy7VY_y6pZ8eecRi7Kwwdba1JPslI7XUY7V0IdLCqC5MaDo3VNOVLUjQevpp6SASMxTmKKPYDDUA3NEZbJ7nUvjherTQ_1hyGlN-CNUYkOjD3vrLGBV1iUTMdWAGBpdr-IPdZsNmw2M3Swhzbh8E9M3kWajcV2U7pe3Ie8dBI5kOs46648nm1EmLuiQ48k1WFSC5E4u4xZqOaC_Ys3g9YBDdeqGNPn5OO1HKsuQF0WVenRFd6ORhus4zQC1MQ-CelgSvTp64oPtWhXTOZR8lSONFtp8kTHbKbXQ0R7GM3-ZMYmDfvLlOJNDPquZrknR0fBKepb90csGftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساندویچ سرد مرغ  #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/654776" target="_blank">📅 11:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911d825a4c.mp4?token=UhH-uigHes_vtQwdQtNtN-J4-W-_U4z_suwe1nQiLccF1bOT5A8aLl2gI7XHqfb4IEK8OrzA_BIo6KnJBN0v0tym3V25ywUvYAdaDaDGSvRROL8ezWaaSdGAWnCpiwy7rAcu96o_WSXl3NX-VeBVayxD_FVDseHUR_O6iVZ9Twl7QGyWw-4GxCqhadapkacGvktWzcGvWeB5sMxYojQ9tbNsZ1cYG46RPZKemr1BmrDPhBj8GE_7RfodMlSQ0cCr9YSs7kNbLO9Hno1HrpZCifFSWDieSOKUKBd_Dgh4TFWl3cxRs99KQOh5euUqd1jf5WlhE44GSC3Glhze4RMCJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911d825a4c.mp4?token=UhH-uigHes_vtQwdQtNtN-J4-W-_U4z_suwe1nQiLccF1bOT5A8aLl2gI7XHqfb4IEK8OrzA_BIo6KnJBN0v0tym3V25ywUvYAdaDaDGSvRROL8ezWaaSdGAWnCpiwy7rAcu96o_WSXl3NX-VeBVayxD_FVDseHUR_O6iVZ9Twl7QGyWw-4GxCqhadapkacGvktWzcGvWeB5sMxYojQ9tbNsZ1cYG46RPZKemr1BmrDPhBj8GE_7RfodMlSQ0cCr9YSs7kNbLO9Hno1HrpZCifFSWDieSOKUKBd_Dgh4TFWl3cxRs99KQOh5euUqd1jf5WlhE44GSC3Glhze4RMCJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پلیس هلند به زن باردار
🔹
در هلند گزارش شده است که یک افسر پلیس در جریان یک حادثه، دست یک زن باردار را گرفته و او را به زمین انداخته است.
🔹
بر اساس این گزارش، همسر این زن که شاهد افتادن همسر باردارش بوده، به سمت افسر پلیس حمله‌ور شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654775" target="_blank">📅 11:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb4y4wXffPmVAw3Fe9MjBXJb8-NYFhtWGp_GvnBDAdXjSrmp_d4fD-7BDRFs__uxefBs_VBzcEHogjTBRWSP3EQ7SSbcz5TX-RhpWmH5nyQxIxPxhXV6kjyinFnogQAREmwCd0yBDFLjDzBdOwiUBBEUoEJrEuu-VsC_GGgfuHeukDnQlwF1viFTNovY9Zk1YtmYivVZ159n0wz_xgFqoHcs82j0SUrwR2oONoZj3qqUalBeG9lf7X4NSLhwfvWRCgQDat8mDAk-9Op38aBsH7DhgL41OHT4w8FzGABO-Lg0p0vZQk5PcF-ahBtuNZS6Gm6M_DGpZY7vJsvl0B0vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا موتور سیکلت وسیله نقلیه «محبوب» تهرانی‌ها شده است؟
🔹
۹ دلیل کنارگذاشتن اجباری «خودروی شخصی» و «حمل و نقل عمومی» در سفرهای درون شهری تهران توسط طبقه متوسط جامعه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654774" target="_blank">📅 11:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2kyECA6bFZj0bL5rSUHBX72uEpLN-FNw66TFHAPkZezd0yT7qaQ_7m9B1q9J-EseyVTfWr0zO2bx6ZUkLTrpKNBWpLjCNasUDgPAlRrxaB4QDPMm21F6E45NGRXoAQ8FX9R7QLNSAXFzVv40XpQcbtUM7CqNA53HvY9v2UEApj3-IXwMmS_jOPffJtplJJwRQtq0Fa3U4R-nSRacX-g_ON2HaQhirD3uZvli6-CPsi6OTCV294-Gd4-Tp-HcNYFMJ7y92bEUT7gjLZbQ0tBOdB8VHPDkzjBdvL72LwHpqfZtzM6I5xQQdDQT2Mbdq8ZvRIlN7L3V6mCbCesIt3BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا زمان در کودکی کندتر می‌گذرد؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654773" target="_blank">📅 11:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDtaY3EB7aa98yi4lngcjdylX5bDIo4mnvUL1V4Dy1TQjlfdHZtJbhpMaiq96_zqSC2tQCjkXQyOGknYYfqcnrtsY9al1ASx9xCNBYZYFHgAFz3Sl9B3U-uoAksGIeF73lFNlqIUKvZkEFsUFcaA9jNaQ2asY0r-5Z0xyZg2sADbWZQ-iA4794UOVWsbM2mC1rKhOue7IDraPAzOhZanUnKqiUtxpn-3LDIf5kG1Ed3T8rsH_t0JZEOIUPa0uvBq5Rkzly5PfBuXhMIZ2m36f8uBX0UHU7QmLxA8-j43usedwOKH_8xDuRQdGxcZFm4q05t-kpKCY-vSwmB2XUE_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیۀ عالیشاه به بازماندۀ مدرسۀ میناب رسید
‌
🔹
محمد در جریان حمله به مدرسۀ میناب، خواهر خردسال و خالۀ خود را از دست داده و خود نیز دچار جراحات شدیدی شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/654772" target="_blank">📅 11:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
توت‌های خیابانی را نخورید!
علوم پزشکی البرز:
🔹
شهروندان باید از خوردن میوه درختان توت در معابر پرهیز کنند.
🔹
آلودگی‌های میکروبی روی سطح میوه توت می‌تواند باعث ایجاد عفونت‌های گوارشی شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/654771" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
کارت سفر در راه است
وزارت گردشگری:
🔹
تا هفته آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی افراد و بدون سقف تعیین خواهد شد و سودی به آن تعلق نمی‌گیرد./فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654770" target="_blank">📅 11:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITozo-PRuakOBzjH1NUwivAbSD7jqqOJnpqQHrFGNPMpSJG-_6cA-qFDHblOJHBozAw-q-7u9eEATCnDEZU-InSmXUGHXrlokGV2NqWSgPkJLfggEU4Cj-SKepOH7RlQEGUWH1zdRWvxOdFhcTJNoL1hxq40VR1cTLaaJXko2Zqrc5GkeeXq2zBEy5qgEWGx9HNxYsE-7dIwS4KeLQ7tML9Xj0x2prcOQhoXJriYeGyrUTHF-dC5PxZsCCByxRnGzRqn2bQEYlwb9FuAjI7Sz6E-i4Axff26zfrXOw2z2G5BtrMNAwf3S0lHfBDuNZHPqUI0t-A0jdsE32Jl4mUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد تاریخی بازار سهام
/
بورس ایران برای نخستین بار بدون حتی یک سهم منفی
🔹
بازار سرمایه امروز یکی از متفاوت‌ترین روزهای معاملاتی خود را پشت سر گذاشت و در اتفاقی کم‌نظیر، برای نخستین بار در تاریخ بورس ایران، در بخشی از ساعات معاملات هیچ نمادی در محدوده منفی قرار نگرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/654768" target="_blank">📅 11:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266a2532fd.mp4?token=FBtf0EtSKTJL2V6pQFatu51EfksCyYUVPKuK_xbQVZsWmAzpxpZ7lDGiPHIFzL74sjtxUlYdUj2PJVH4ZWSGClHVysivw3IQjinnRhZmncGfClqyI4OA2rgLToQLQBfCl4k9yce0p34GXBJpTmz9E2Rpz3GH7Ab1x8xW63eoyJLe3kU1KvwNNg8JryGJlDVFnk23y56amnXB-ghsCldRZdd5a9y7bsMwb4lyz3GHMsboJoKsmqJdGNkUrIvuShCG9AtgWCnj4Da2GG593NIItMplXw6nOuCeOUPmJtrgyg4-fwuIAHxKwxg_u_tXv_-guypIlxrdx1lSBbjFYVffOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266a2532fd.mp4?token=FBtf0EtSKTJL2V6pQFatu51EfksCyYUVPKuK_xbQVZsWmAzpxpZ7lDGiPHIFzL74sjtxUlYdUj2PJVH4ZWSGClHVysivw3IQjinnRhZmncGfClqyI4OA2rgLToQLQBfCl4k9yce0p34GXBJpTmz9E2Rpz3GH7Ab1x8xW63eoyJLe3kU1KvwNNg8JryGJlDVFnk23y56amnXB-ghsCldRZdd5a9y7bsMwb4lyz3GHMsboJoKsmqJdGNkUrIvuShCG9AtgWCnj4Da2GG593NIItMplXw6nOuCeOUPmJtrgyg4-fwuIAHxKwxg_u_tXv_-guypIlxrdx1lSBbjFYVffOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رهبر شهید انقلاب به فیلم مارمولک در اولین اکران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654767" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc91pbOlp--JKmUvxpPdtLQmqfBYMHMezTkZ5AaEl_LyHkVwa_uSIOzlQLiWkj4b45tSQp4KtOyGN2iuVNi279ijAP0mMgKi09oqgLwZ2FLku6lLjhVNtK797qyPud-NGcH2GUvhSWy37CR2g1mB0Knz203SJxcliG3V_9IiGi0bh6IXjXRYymCzoVV9vaEli9aJaRIvla4h_G0h9hqvoYvS3hl1fYdGwaCOPXL1lFqwFYXRHfBUpf-EzghyKxGut05x4w6CChY4QcjUcePjbD95hnkVIxZ-CrhcEm7u_h3qST9lU7KJXJtxGGqIG81pYMcK8Qz0Sr0TtVVs6BcJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/654766" target="_blank">📅 11:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZFmK_PoqMTGLOi2oZnGlqDgL_Jmqm3i31r0bGJBjbyu8GujRU7woAv7V1dOvJbg0mgURO93zRt-N9QuiFGIfsdMGsinUH84Ahr42vr2zS48IrFc74JdSvJI5883TNssHVboXJYtP7vTC_6fO6JONldPjQq2AXAycye831qtD4DaYbdgl22EAMZnDJYTbQJlhKaW3_onGrAXHGn6bYTg6C82e9-EDB8WKXzk3OxaZ4hbX0Dao85Q2ev_2qX5vkSahpncYlUkSpxIw3YX67okVGIMRtONDQWxIZQDSWYE-TayAQQPGTIBuirudiwPmV3P3QZR8r1HwdoN8c2YptBPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی هشتمین گلزن برتر جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/654765" target="_blank">📅 11:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e8cb4359.mp4?token=b0W7FH3Vxo97l77L19vUnzJ6YJwUnorU4-ro83Q0XRy7TfAmNX33Lde_fqM0hNilgdAhGY__g5GdbIJ9mL6h0n3FdjHcV-a_FI6hX_Dg6_1uIuoM5BC2AUwQbk3Gly0ovSIHub_LhYsSYOtphLZirD0upERPelLWy1Mzi1-lwtPVzk-MtILStRxJjmT4GgDGUX5w6T3AmEFabiWqz_CUwbykYn75ZiCyDwQ6px3TElMoTxBJGFdvHscCn_Xf-uQjMkN_ZN5FAd6UtyMCiP7TBK6vIg5zrnIs4rsjnP2N7SDrcz3WlT_zY0IobmWA312u93x_wLclUaS6r3XfZxjn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e8cb4359.mp4?token=b0W7FH3Vxo97l77L19vUnzJ6YJwUnorU4-ro83Q0XRy7TfAmNX33Lde_fqM0hNilgdAhGY__g5GdbIJ9mL6h0n3FdjHcV-a_FI6hX_Dg6_1uIuoM5BC2AUwQbk3Gly0ovSIHub_LhYsSYOtphLZirD0upERPelLWy1Mzi1-lwtPVzk-MtILStRxJjmT4GgDGUX5w6T3AmEFabiWqz_CUwbykYn75ZiCyDwQ6px3TElMoTxBJGFdvHscCn_Xf-uQjMkN_ZN5FAd6UtyMCiP7TBK6vIg5zrnIs4rsjnP2N7SDrcz3WlT_zY0IobmWA312u93x_wLclUaS6r3XfZxjn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی کامیون حامل مهاجران بازگشتی از پاکستان در لغمان/۱۸ نفر کشته و ۲۹ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/654764" target="_blank">📅 11:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
احکام قطعی متهمان سرقت نزدیک به ۸ هزار بشکه نفت در خوزستان صادر شد
رئیس کل دادگستری خوزستان:
بر اساس حکم صادر شده، ۴ متهم اصلی هر کدام به ۱۳ سال حبس تعزیری، شلاق و رد مال معادل نفت مسروقه محکوم شدند. سه متهم دیگر پرونده نیز به حبس و مجازات‌های تکمیلی محکوم شده‌اند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/654763" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354758e503.mp4?token=TnMEOGCitio7N6ea0OsAK2P1f1Np4xMHABkV3hCTMWGWTE4wCX3aKLnKdSkVSAWqBTHn97k7XcxyhsdhE0A2g8C8e6ybFAf7KAQw_4NCl22pFAIa3PIGuR1dW07nymn7Pd3aN0gTG6-B4TJ1_-qappfAyVJMOLB1joRYM4l8RV0FqIKT2lPTi4_zfcqVhjSx9qoCi6pM8_xWR-Ln0KrGOtwk6VQt6sPWcK5P_tg8v3OjWNJl-qB0IESiTNwPbs4MPSRr2a-uYeM7WwG4jr9Qx99yGqo-HluD_LXw6sLpMN_cmlm6obEqcyMKzPpc-DkLTJxS7ID8ALP0GxcpUL8qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354758e503.mp4?token=TnMEOGCitio7N6ea0OsAK2P1f1Np4xMHABkV3hCTMWGWTE4wCX3aKLnKdSkVSAWqBTHn97k7XcxyhsdhE0A2g8C8e6ybFAf7KAQw_4NCl22pFAIa3PIGuR1dW07nymn7Pd3aN0gTG6-B4TJ1_-qappfAyVJMOLB1joRYM4l8RV0FqIKT2lPTi4_zfcqVhjSx9qoCi6pM8_xWR-Ln0KrGOtwk6VQt6sPWcK5P_tg8v3OjWNJl-qB0IESiTNwPbs4MPSRr2a-uYeM7WwG4jr9Qx99yGqo-HluD_LXw6sLpMN_cmlm6obEqcyMKzPpc-DkLTJxS7ID8ALP0GxcpUL8qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رونالدو در تمرینات پرتغال با جت شخصی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/654762" target="_blank">📅 10:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شوهر عصبانی، همسرش را لو داد؛ ۶ سال کار با مدرک جعلی!
🔹
مردی پس از به اجرا گذاشته شدن مهریه توسط همسرش، فاش کرد که او ۶ سال با مدرک جعلی پرستاری در چند بیمارستان مشغول به کار بوده است.
🔹
بررسی‌ها نشان داد زن ۴۰ ساله هیچ مدرک مرتبطی ندارد اما در یک بیمارستان دولتی و سه بیمارستان خصوصی فعالیت کرده است. او پس از بازداشت اعتراف کرد به دلیل علاقه به پرستاری و نداشتن امکان تحصیل، با کمک یک پرستار مدرک جعلی تهیه کرده و مشغول به کار شده است.
🔹
رئیس کل سازمان نظام پرستاری نیز تأکید کرد حضور «پرستارنماها» در برخی بیمارستان‌های خصوصی قابل انکار نیست و حتی یک مورد از این تخلف هم نباید وجود داشته باشد. / ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/654761" target="_blank">📅 10:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f592SOl03BKW63r-kFt_alDWx7n2hklyJsjlL0zI8wytep0Mq2FRH_mfRuR4z28AD8dDlehZdf538SmvvsoZ9GqLjxYnV9thF1C9EWKm6A9dnNrZBdxRklJwKzwaaNibil_biT2HebGoX31Yfs2aCK4f7CG_uDmBFBmRCYXt1U1Ly47Id2PHAVUjZzPQI1n70_CWbPJjmMilYBufCaAAsCVrusu7juO8cbY4lRj0l8D9Yn08Ox7y3nXX9seUMAlPQmbEOM7MjNGtFWij270OdUlff4RqSAt8h-uM5YYfvY0LzXV07NEtuQGADSopZPDT-ftzjX5Jh1kYGqiKcdf0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردی که در تصویر زیر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/654760" target="_blank">📅 10:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huHaevfun_51sI7sb834NFszBF1Kv_IsQ9g5Ku8luh-ImWnqZwDmlYHZUHxnrteb1VXWRGxDk1I7m-4Sc6W_fsU_P6gm9P-atskvB3dJosGr_GDTo1PHzxZxdBHnpRVztiJkeaBuzYl3YovrSMdDJgOEqdX4C80q1b8NXwhkYWjBkivtzBtzUJDhFSUtWzwnQ5wjTdk7EU_9Dy-d8wHWndkbfYQc9dr_YB-Y63Ve6Qj-mbWYetdi-ptL9hysrD5otIS7HEmlJWlb8jCCupSf6Wi46mQONKfXS_aDlBRCezfSBr8fAvxp_xiFHTUf0AVQcMfzCqOhYYEkunDzOM2YHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تام هنکس و تیم آلن، صداپیشگان وودی و باز در «داستان اسباب‌بازی» طی گذر زمان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/654759" target="_blank">📅 10:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
از امروز محدودیت‌های چک برگشتی و لحاظ شدن بدهی‌های غیرجاری وام‌های زیر ۷۰۰ میلیون تومانی در امتیاز اعتباری، پس از پایان مهلت سه‌ماهه بازگشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654758" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
زمان برگزاری کنکور اعلام شد
🔹
رئیس سازمان سنجش آموزش کشور از برگزاری آزمون سراسری و کنکور دانشجو معلمان در روزهای پنجشنبه و جمعه ۲۹ و ۳۰ مردادماه خبر داد.
🔹
کنکور کارشناسی ارشد ۱۴۰۵  ۱۸ و ۱۹ تیر برگزار می‌شود.
جزییات بیشتر
👇
khabarfoori.com/fa/tiny/news-3218868</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/654757" target="_blank">📅 10:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ace96eab.mp4?token=RAn_20l45BOaf_uASb3W9UYmG9T2xiakNBO6zBsW3RtZUBMwrajuw9inFMJtDMRYtnQsds2Q4u9P7SDwqsHZ2lEIUVSUQ1N3dy3sOP231tje7Ie1ph_oQkuPqY76pEy_R4mxBa9kpSy4YBwrfv-j9onb4VP3W7j__9ssj4GwFplY9ZOE8r5h2Q0_PPHmhjrBNnSS1Qh0B9AhUIZHTO6obb8ayfmoUQ7AWg1gcWuhvMTW4m9rwdDMsdp-p2pzQasfbwAtNS0M7bFlAhipAU9MwWt11rvjPlsiwhq50wz2cpEFdSY46PTZKXE3cxaq0m3XrfskM0iGKLMj1JHfmCb-KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ace96eab.mp4?token=RAn_20l45BOaf_uASb3W9UYmG9T2xiakNBO6zBsW3RtZUBMwrajuw9inFMJtDMRYtnQsds2Q4u9P7SDwqsHZ2lEIUVSUQ1N3dy3sOP231tje7Ie1ph_oQkuPqY76pEy_R4mxBa9kpSy4YBwrfv-j9onb4VP3W7j__9ssj4GwFplY9ZOE8r5h2Q0_PPHmhjrBNnSS1Qh0B9AhUIZHTO6obb8ayfmoUQ7AWg1gcWuhvMTW4m9rwdDMsdp-p2pzQasfbwAtNS0M7bFlAhipAU9MwWt11rvjPlsiwhq50wz2cpEFdSY46PTZKXE3cxaq0m3XrfskM0iGKLMj1JHfmCb-KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای پزشک ترامپ: «دست دادن مکرر» علت کبودی دست‌های رئیس جمهور آمریکا!
🔹
کاخ سفید یادداشت یکی از پزشکان ترامپ را منتشر کرد که در آن ادعا شده رئیس جمهور آمریکا پس از معاینه پزشکی سالانه‌اش در مرکز پزشکی نظامی ملی والتر رید، در «سلامت عالی» به سر می‌برد.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654756" target="_blank">📅 10:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOkrIX0tFQL2sOLXQzHboREAlDfWMFSJraoWtKfR8Dd5PhjhE2AZBiPg8HAQjqIc83BckwiKp89Awa5WLahsHBdlAOIanHMw7iEHN2NFR4JJtXJlvtWfaaAHS-1FnHhuqgpOCO0SvR7SfW8zAdY4K6BbZCIXlxhNlBdraJS1lqXxiDZzXn-ee1Z57K3Tw_XVjxkLUx0uSaaIBZcWEvVo3EUuh6B09JK-YEQAOPC2JmL8qcIZDFaJZn-QAk4Pc7A8FNVgDQgIJYyOswnVdVXRYkfTo4M13ozZf9yTECPXuD4NvkCjVVnx_-UKfuW9HbxbaIEQGgQQQYc72bFmYeNt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دریاچه ارومیه در روزهای بهاری امسال
#ایران_زیبا
اخبار آذربایجان غربی در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/654755" target="_blank">📅 10:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4xb__FgbndVA-a2PI_gmSbkvCwZzyb6-t4dObWLuydMHCFMW4x_hnWH78SnNEE68lCNrythcO4ozwG1EMzvnCFfcSV4kxujihXrFbXWLS1elAOTtwFY4XyffaimjD7ZW3kZK_qv1Fde2TRD4zgFM9C4kxuWgzwsJckwjR3fVjwZe9WYFGl6lesxPW_HgJBTgCoIuKN01DDtV2CfqkpZ1Wl_yB3fHTzj1P1zpEB6birYqxi6XZR2Yd1cOEKtTU4DVuj6MlrCwXRi6f7sDydteTo6Q5OnMsDVFbicBMmQeWLxuSrvNFdBYVv2GJVXztJgiLRFMd7pmsVTvnUY-9enLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/654754" target="_blank">📅 10:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: توانایی ازسرگیری عملیات نظامی علیه جمهوری اسلامی ایران رو داریم؛ وضعیت مهمات ما به اندازه و کافیه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654753" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نشریه بلومبرگ گزارش داد که در جریان حملات ۳ روز قبل ایران به پایگاه ارتش آمریکا در کویت، ۵ سرباز آمریکایی زخمی شده‌اند
🔹
همچنین در جریان این حمله یک پهپاد MQ-9 آمریکا کاملا نابود شده و یک پهپاد دیگر نیز به طور جدی آسیب دیده است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/654752" target="_blank">📅 09:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbyEjplHms6E0QNhJ3bclII9gB9_T7U-jJi5kwPqvwhyFkhvX5hmWNzpNSe_O5J3zw-lEqZfJ3fUZGdzr38e3n8rL551hK779rtRqVy6wkvui3NiDmrTZ8iEHMu3-vXtLKu9_nuoWz2KFu6VJ5csWvWRngnBVsGqzwKMr6BDRyeKkCvnaKrEeLT4EW-SSQJRQqL-R1XL8gwDeXYFwR1Jb-X2FV86v-W67mgy-jYnalLet3gO4kDdcxmm7ti4fGqTCkORG3ogQrEXCtqoHtBkIJatbnW1NUB4cKE8BVQyhjFGv7DQPkzGovlRfXKgnYXfj2rYPNWYrTUQvmU-OEZBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز فعالیت بازار سهام با رشد ۷۴۰۰۰ واحدی شاخص
‌
🔹
شاخص کل بورس تهران در نخستین روز هفته جاری با افزایش ۷۴ هزار واحدی به تراز ۴ میلیون و ۱۴۷ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654751" target="_blank">📅 09:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw3PUmOhel0JK55UzsYxM7-R2bU1ys6X2eUyfOpd2XWEp0i0I5IiMF93N3vwvOML_AonrNWgfgSdgnOl4bBCsABy1vbUbG_kQt32uP2vwCYPr-vwF38_Z_cCWE4LEM7zg7xVEtvCvavRsYetBcLD6sbUHKsDcjaoVzBCztCCsg0KY33EBBBIEUtrSYWfPrViBMP9dqkaVYOk-_Fhn8d3zfLYDJe4nOssb-nUzOpspPkLht64jMncCeR0uZo7HjvTyrHQOoNF0EgFK-kHGd7EKhfpL2Htk8VHagthLyY87_dMY7X7viSI8G5LzkARPkeYq0h4bjS3wveo9546w6aoTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای پزشک ترامپ: «دست دادن مکرر» علت کبودی دست‌های رئیس جمهور آمریکا!
🔹
کاخ سفید یادداشت یکی از پزشکان ترامپ را منتشر کرد که در آن ادعا شده رئیس جمهور آمریکا پس از معاینه پزشکی سالانه‌اش در مرکز پزشکی نظامی ملی والتر رید، در «سلامت عالی» به سر می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654750" target="_blank">📅 09:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiSkHgUx9-M_rdCOO0vwU5gHS0GpqdFqwYBMSk3LJH0OIpqUkv93kt8lFT3fbVxtsanvooxTHUML3I56EshV-6rLY9jai5njB5zi4jYo5vra-58ImmyVauILB6E9h4jSovU1DTDZ7G6-ZAeDV2XIh9DykVSc4i6i2tyWnNPcFPCxKdRyNIIH3mFtBLy646amHBiYaXOBVZUVz41LyBDRduy-eISp1q1bXxWh4BwycJitHjYGY31g0lV4WWpyNAWGsuGvZ2qsPZuJd-A86ts0W5vcFUHZKAHZfa-1jl7kvTLKVZj9HPV5Rza3sP595AkaV_aJ_m0XSFShUi2xrwLBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8bCDU010YzlK0L0pRDKdN9MTNBJaqhYohR93KDOocESOWVIlgShe6ssJHoCx2d4VoRVkkkoCZUzfFtNlv3y99JNthP5rlAcOCo7MvhoPgTEI7BVbJmWrYlhMX3XwCpPE7S7Bw-9Sb1JsJOZ9mtNLxXgD7V7OH4sKhtmpUWMR7Uf1xj-h70QF-IkccGklJvIxPiJ9sfsB3CCf-WV9OtNy4U3r9S690zpGrEw18N8iCBkIdHOqxOTsAVIAiOzDR7M6PLvHJSMKzLw2CtqOqQ8XHT2FRYbFh10UPW5Q7TCaS5bJP1oypeP_-BW2ktAECPieRLt2pTEYu0zIUZWGuP7fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروی دریایی آمریکا: کشتی‌های تجاری از تنگه هرمز دوری کنند
🔹
سنتکام مدعی است ایران قصد «کنترل غیرقانونی» این آبراه را با «مین‌ریزی خطرناک» دارد. به دریانوردان توصیه شده از طرح تفکیک تردد اجتناب کرده و عبور خود را با مرکز هماهنگی آمریکا هماهنگ کنند.
🔹
همچنین هر شناور در حال مین‌ریزی، در چارچوب «دفاع مشروع» هدف قرار خواهد گرفت./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654748" target="_blank">📅 09:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: وضعیت فعلی این است که هر توافقی با ایران، خوب خواهد بود
🔹
ترامپ صبور است تا مطمئن شود که هر پیمان صلحی با ایران، عدم دستیابی این کشور به سلاح هسته‌ای را تضمین می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/654747" target="_blank">📅 08:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f854976f6.mp4?token=i8zt_OlCDUHfUVajRZiWc0HAtx8UDVUqxLhFY5AqrmFb5rAt63ly6zov4XsyFu8nZSM4qhigUErjMFCAaEXkxwyS9ZwF-a8bCEyK6HYk4Ljbr1Mkc2UFZm2BfswGCXOlrcW4x5jAgIKcS_DJ9YCUWvxz661rtmeR-k8TOUCAoTMHch_9V3OgeWdAql1yLWKLzI_6s4hxuipHdWZC_VXOVXHBDveKe1n1ap-5BLkVK-vJQihfYfA6HOAKIK50lY_AWYXN92Bg7CSYQvhHAZaEj0_OTxqHk6Z6VCSFxYOil6Rrn79vMbnApINFNsZZh42Xdq2omkJK2tvmj9OCu4trDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f854976f6.mp4?token=i8zt_OlCDUHfUVajRZiWc0HAtx8UDVUqxLhFY5AqrmFb5rAt63ly6zov4XsyFu8nZSM4qhigUErjMFCAaEXkxwyS9ZwF-a8bCEyK6HYk4Ljbr1Mkc2UFZm2BfswGCXOlrcW4x5jAgIKcS_DJ9YCUWvxz661rtmeR-k8TOUCAoTMHch_9V3OgeWdAql1yLWKLzI_6s4hxuipHdWZC_VXOVXHBDveKe1n1ap-5BLkVK-vJQihfYfA6HOAKIK50lY_AWYXN92Bg7CSYQvhHAZaEj0_OTxqHk6Z6VCSFxYOil6Rrn79vMbnApINFNsZZh42Xdq2omkJK2tvmj9OCu4trDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوی تازه اینترنشنال برای ایران: جنبش جولانی (داعش) در ایران راه‌اندازی شود!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654746" target="_blank">📅 08:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
رئیس مرکز ارزشیابی آموزش و پرورش:
🔹
امتحانات دوره ابتدایی غیرحضوری است و بر اساس ارزشیابی تکوینی انجام می‌شود.امتحانات پایه‌های هفتم تا دهم به استان‌ها تفویض اختیار شده
🔹
امتحانات نهایی پایه‌های یازدهم و دوازدهم از ۲۱ تیر، به‌شرط عادی‌شدن وضعیت با اعلام مراجع ذی‌صلاح، به صورت حضوری آغاز می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/654745" target="_blank">📅 08:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c176406e.mp4?token=kmIeX5ImsGsV9GvYxG4f_xI5-o8jNpYN9ata6UHPKwPMAh30RGtbs0q0iL5c-EgLPH1Q7ukDVd8mSDzTR0IQ9CZgR8dvULtnSGq_cmN5Yaw-Uy1N3WqsPw4lnB3hc-lKmx92m453FD8xuxC7kW9R4ncQKxhQnbgbxaf41Mz3ncq6fvqauDPFu2ala6osq1zwxO9SiTpoEVCd0aQszTQFoot4kwzHcD6kVLgUwhi7fulnpeHKgcoNF09BBLm9cyn52R2ArVMYQi3oZNp5uein52tc93tEOOGWIQOqjdaGcrdnLAiGG5_KD7Nx9IJlRDw3JLnR910f79X60DTbXzW6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c176406e.mp4?token=kmIeX5ImsGsV9GvYxG4f_xI5-o8jNpYN9ata6UHPKwPMAh30RGtbs0q0iL5c-EgLPH1Q7ukDVd8mSDzTR0IQ9CZgR8dvULtnSGq_cmN5Yaw-Uy1N3WqsPw4lnB3hc-lKmx92m453FD8xuxC7kW9R4ncQKxhQnbgbxaf41Mz3ncq6fvqauDPFu2ala6osq1zwxO9SiTpoEVCd0aQszTQFoot4kwzHcD6kVLgUwhi7fulnpeHKgcoNF09BBLm9cyn52R2ArVMYQi3oZNp5uein52tc93tEOOGWIQOqjdaGcrdnLAiGG5_KD7Nx9IJlRDw3JLnR910f79X60DTbXzW6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراجا: زائران اربعین گذرنامه‌های زیر ۶ ماه را تعویض کنند/ امکان تمدید گذرنامه به‌صورت حضوری و غیرحضوری فراهم است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/654744" target="_blank">📅 08:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI1q67xSz80GaT4UsjdesPY9FD2V9XyUrNWaGIBqCNW_DkPXMx0QLFgWw-oHsX8P2BjfSISTWIyrbqux-vunx5R0U0zdYnvSyJbUdb8PqHcFjKD10ekj_0lPi_9Q0zbTZdKJGev2J0BBEWFSQiSGqqwQ0EqECzEdS2vL1rOi_nZ65qtpjFr70YlFEYV5CuGlRhW3dT_upCyIDyaB0AlmJUQcc9lWbjj7LY4dheBCXca2RU5-au5Ju7qCnNIpGhhROH5TFQbLO1IwxHFHIPKSXP60qoFb2KsFVE_LtKxWvXYtaAv81iUX1qnP6xavmZDvsSOEQNOgqsyhOsvo_9xTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLfgMNi1HX3P4pdTKWGdYn_lZpliUkVZj_fvo36JWM1uJbdKwfnMqjPmSh2IrTdd31xF_yRKc2psebuzyUAEK3Uz-ndBEzbAB4SmXkmHA6eWvhCZu9VOaqDdWzOvIfkwzDrvLXVQnaHEDiu7Vx2Xda1srSl0Jbw6IA1GrHEgWWmo6bZr9dyhquoBv-Vs2sdOzHYfI2zblytS3ooPM0GQ2aHcEnjQsAyCTj0KoFNu6w-gWABw_ic3mpyCztaVDGKMC-dWcRQB4UZwARX9vg50cNSQoWg6-CvJSua-fSF91CcSPry-C3o4l-qk-qS_5ePtul8LNo6dJfk_vfPIIIA5qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برج ایفل پیش از فینال لیگ قهرمانان اروپا به رنگ باشگاه پاری‌سن‌ژرمن روشن شد
🔹
جدال آرسنال و پاری‌سن‌ژرمن از ساعت ۱۹:۳۰ به وقت ایران در مجارستان برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/654742" target="_blank">📅 08:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نیویورک پست: ۶ میلیارد دلار از وجوه نگهداری شده مستقیما به ایران منتقل نخواهد شد بلکه برای خرید مواد غذایی و لوازم پزشکی استفاده خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/654741" target="_blank">📅 07:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی به نقل از مقامات آمریکایی: ارتش آمریکا، با وجود انجام عملیات‌های جست‌وجو، تأیید نکرده است که ایران در تنگه هرمز مین کار گذاشته باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/654740" target="_blank">📅 07:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای یک مقام کاخ سفید به الجزیره: ترامپ هیچ توافقی با ایران امضا نخواهد کرد، مگر اینکه برای آمریکا سودمند باشد و با خطوط قرمز او مطابقت کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/654739" target="_blank">📅 07:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تحریم‌های آمریکا علیه یک شبکه موهوم مرتبط با ایران
🔹
وزارت خزانه‌داری آمریکا روز جمعه تحریم‌های جدیدی علیه ۸ فرد و ۵ نهاد (جمعاً ۱۳ فرد و نهاد) با ادعای مقابله با تروریسم و در چارچوب کارزار موسوم به «خشم اقتصادی» اعمال کرد.
🔹
وزارت خارجه آمریکا نیز برای اطلاعاتی که به مختل شدن این شبکه به‌زعم خود «موهوم» منجر شود، تا سقف ۱۵ میلیون دلار جایزه تعیین کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/654738" target="_blank">📅 07:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENNferMFdiwvFnr0C4l34btMb1P_stRSWbsX_FLV0UZKGq73xBsbVcz_jZGyI5dx8p-rycMezp0_35krJrIoY4C_dlNFSb64WI9d2Tt9EDeCQiJTJFZ8TqJEQBj6LM2RjyLzOP2v-_Szs7Gj7Hh34SBloUgS11bmqqfcn7IgBk2xTOjir4_ll8kfBAk4i7b01eO1yn3hKJCt47cPaqN50X4WUhAWFSTsGuZMPxoDWytUkahalUuqJweD9fm5tjcjwvraGlpnEcUOjxzd8lVqOFZFaBV1MGnDdaSv3-03xj83GqY2FuJN61iu4kjENcJiOY57SAFBTsC7yJjwzR1Owg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین پالیسی: جنگ ایران یک اشتباه آشکار بود و ترامپ باید اعتراف کند که اشتباه کرده است
🔹
واشنگتن به جای پذیرش خطا، همچنان از مواجهه با واقعیت شکست خود طفره می‌رود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654737" target="_blank">📅 07:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a42cfcf9.mp4?token=nPwl4BrAnpGUQXvyj-Z4SFvNvituu9Ix7IAxnLLdOjRb4JScTLuXHoE-vU_m4fQZhhLKlbrbQyZkMEnpC2YmRrpiCMn-0rOA2XCYcC2hfi0ivpPnnQ4sTpuNhUkFCeVj0Vh1OBj_8D5GkYO01YSm14PLHaUSmFFvKHdKy8Nj8ibRyitEuinVRd7WZbw8mPVzxvEI0eyg2YC7s9h3alDV_3kN_Ierd7X1v3oYeqvea_himOmV_QUjaQjhKm-DOQYljKcGGg0QFACGrGCBWcu56740Z5TvPOfKjY22Teh5Pnm_mHJk_TeLPdEqpdHwD04XipWfcTRAzonA2qkF8WfFXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a42cfcf9.mp4?token=nPwl4BrAnpGUQXvyj-Z4SFvNvituu9Ix7IAxnLLdOjRb4JScTLuXHoE-vU_m4fQZhhLKlbrbQyZkMEnpC2YmRrpiCMn-0rOA2XCYcC2hfi0ivpPnnQ4sTpuNhUkFCeVj0Vh1OBj_8D5GkYO01YSm14PLHaUSmFFvKHdKy8Nj8ibRyitEuinVRd7WZbw8mPVzxvEI0eyg2YC7s9h3alDV_3kN_Ierd7X1v3oYeqvea_himOmV_QUjaQjhKm-DOQYljKcGGg0QFACGrGCBWcu56740Z5TvPOfKjY22Teh5Pnm_mHJk_TeLPdEqpdHwD04XipWfcTRAzonA2qkF8WfFXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسنیم: انهدام ریزپرنده متخاصم دشمن در حوالی قشم
🔹
در پی رصد ریزپرنده متخاصم دشمن آمریکایی ـ صهیونی در حوالی قشم توسط پدافند هوایی ارتش، بلافاصله در عملیات موفق مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/654736" target="_blank">📅 07:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u98ddwos7BvNQvIYrfG6WcqR7oWw8m1M7hhhGtdw8xGmC0P1vUTVeQ7Qln2dKfAK4kMFiDEehuQuk01j89Io-im_RNPKUATjovtN5KUj_4Qwvv1BpV-OgBYRsMNYtHHf1sOuslffRhmwyaKa3mIAJhVGH9_LmwRm2NfiF-9RVAzFVMubVaHBjRP4GNHPycOzeR3kVy6rH5N6qUgFcWS6t2PCsUcBhLQJaqdArUI15-B9Qwyx4A9_yiJOHc0wu0SB3Oe3E5gOKzgXNW5WN6rI7sr4b1G90nBAVNB8NPbG5OybjQdyRcef8e6CmFmrz7aqPENS2p0z4xE6k3zRyq4Uzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۹ خرداد ماه
۱۳ ذی‌الحجه ‌۱۴۴۷
۳۰ می ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/654735" target="_blank">📅 07:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjuyFJPC-tGnr1xqoFuR8DtwVMOjzYf6c413folR5a4Mn7KAuzOma60o7CNFdDZV14wIIWT_nekfDIJSe4EROpcL6d0-trT35tOnzfnkRhwvrhFBgU-tSxw6v4Ygcd16ySmAooEsw7y_2euwU8r_sl1RQpIz7phqVTDVmWYbwyUAKqCBYFrgHA_NUYePCRTtQoCWI0vm9DsO8RX5vnTKenIcOYrL7xCq2za5RWTwpl8ZcnmQM1ov5WaY0X_qUWsHbcMNYHRkVemhtAZNRWolrGXKoUldYAadUmFHgG9kkIYRuwtBDkeQxMMLZt9rz4EFYwfgWypUESFXi_jzIJvp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/654734" target="_blank">📅 00:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=E_XtjjxsiMb-eu97Fzo4aphc--d0DlZCLcY-gAQLMt8caydaNSn52_4fhFVOCpZoGBggGOiOKzEYucDBbAKkzgV7m9fpFfKw5ecPW3NxMHHWBd3WiBKwRpC1cXeE86mOulZBDBZV9hYJV9-FLCS-t0obWXJBjnZgbtcpv8JVe4iWlFaPFwHsgKnngvp4H2Sridi9ASa6PH70lnkG3M61q5EDXeqYyppgefUxHG8YnnnFb0uKADYhEKZRuO26mBLHPgKiHSfhPkjQoOX8CQnt-v4DP2nIiCglSEUK85NtoxtS0zz9p00QdNkw2wFkO2c_VPZSpbWMr523gU7YErzsnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=E_XtjjxsiMb-eu97Fzo4aphc--d0DlZCLcY-gAQLMt8caydaNSn52_4fhFVOCpZoGBggGOiOKzEYucDBbAKkzgV7m9fpFfKw5ecPW3NxMHHWBd3WiBKwRpC1cXeE86mOulZBDBZV9hYJV9-FLCS-t0obWXJBjnZgbtcpv8JVe4iWlFaPFwHsgKnngvp4H2Sridi9ASa6PH70lnkG3M61q5EDXeqYyppgefUxHG8YnnnFb0uKADYhEKZRuO26mBLHPgKiHSfhPkjQoOX8CQnt-v4DP2nIiCglSEUK85NtoxtS0zz9p00QdNkw2wFkO2c_VPZSpbWMr523gU7YErzsnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف رضا پهلوی
🔹
کشورهای جهانی به خاطر چشم‌های زیبای من یا شما این کار را نمی‌کنند، آنها این کار را انجام می‌دهند چون به نفع منافع شان است.
🔹
اگر اروپا می‌تواند اتحادیه خودش را داشته باشد، چرا ما نتوانیم در خاورمیانه اتحادیه‌ای داشته باشیم؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/654733" target="_blank">📅 23:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان: هرگونه گمانه‌زنی درباره پیوستن پاکستان به طرح سازش [پیمان ابراهیم] با رژیم نامشروع  صهیونیستی را قویا رد می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/654732" target="_blank">📅 23:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt3h8yJ5V_Tt-brCYheuF7WNUrZGbZbssuROXe7n1aVYiE0DVXyNpM1rnZoQAs8F_gqM3s-JlhoAlJuXnWXjyGtUsatnzSl-DQvHxX7aIHb-3uGfKgLyU9fEqSm2JRjtjVslJpIt6LOVepeE2kZEaMr5vS75OpKiEBwQsOPaGTWOrDhNRFMpualXQohCBBN1zAJFImShy7tMhNujP9QU4ZL3upWZCBVXvO2PO-oTYOxUFe2iUWOrJwu-u-kZAtqBydLiY_ugHo7eS4ft1wpRBSFx_KlgKKWyyyPbtwXEdRM8iBva8lLJ2YFfbOlDFfeENPRaonuquFFYc7zXSLVdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ec2a49cf.mp4?token=CMo7ckAMZUl2pTKG_7lF_RCWaZr_N3XnFJ164JOOIKV8gOIPadZUTZUar8LGBuCqTelbeKcsyRO7cygKpuD8rxnPGvc-7KERcfeHGiT31U5AaOQHjaqZW8X0veKSNkP-Ju3kPZiBY7fCgLGIkW7I57gM0cmhUoVqTt2GGJtsXxiDW6Ec-NcWoGxsDY0zKD_WGyuRt1U4PUizB6Ik8iCQRlzo0VlkhCbgVwsE0bFkeuDw498gthS3sibznQVj4HEl1hJsYT9dE1E7-Z66YvlEdAOdnoPKD8QruGos41gmt1cpoQFNbbr33PBHzebD1vDgvSvKPgpJB-cQZWpdfmRA7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ec2a49cf.mp4?token=CMo7ckAMZUl2pTKG_7lF_RCWaZr_N3XnFJ164JOOIKV8gOIPadZUTZUar8LGBuCqTelbeKcsyRO7cygKpuD8rxnPGvc-7KERcfeHGiT31U5AaOQHjaqZW8X0veKSNkP-Ju3kPZiBY7fCgLGIkW7I57gM0cmhUoVqTt2GGJtsXxiDW6Ec-NcWoGxsDY0zKD_WGyuRt1U4PUizB6Ik8iCQRlzo0VlkhCbgVwsE0bFkeuDw498gthS3sibznQVj4HEl1hJsYT9dE1E7-Z66YvlEdAOdnoPKD8QruGos41gmt1cpoQFNbbr33PBHzebD1vDgvSvKPgpJB-cQZWpdfmRA7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی سیمپسون‌ها از جام جهانی ۲۰۲۶/ پیش‌بینی کردن مکزیک و پرتغال فینال جام جهانی رو برگزار میکنن
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/654730" target="_blank">📅 23:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4MJ4jdHVukbNupLu0M_mcLFLEh4utf4S3fRiKDd3e3-1n1Li16fQQfKFOT840a5m_qTxT00rgXgNTfxPX5N3FDhTBxYrSaAns-V2Kl7267CXTSY-5YIuhBCB0YMxgyzzJ_-6ysqq7x7hJJqaG1cmyFezORQQqUg4qdj9AFBHL475X299FtvCAxp-o0PhftzWvCympK1q4w_V71Hu-F7OEUOIudN4s-BZGMnMe-2agE1ki2bqnfD-ViCS4RfNmGuWn7OEnQPh2uIZ8nGg3M8pnGPaP2J-dFQpccYok78ovLVXSJQ16tv_llcGpG0DEJqFdUqvgYSAtzNa-tSQh8F0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8XLWoS5PhugRoPAn1FVbFmySwGja9s9NQrsXc594QG0igSCqn0W9i778vgsP70_RGlk4aUAtj2UyxaLOCyIE2dTAC6iYk1SSLNqQOF2Gnvk2_fMPwQSqmk6OVScnz8Wb2eydJACQ8K0Efi4RDTLshGTBDLskfmfCcqVRtLB6rasxej5HK7GKDkBDodcinTPuDvQ8CDWEuju76O8FkdE8LBhNH33u9T3lIw0_LDwLiHZM4w_T31YaEVGH5aoGWu1MfbYEVuAqLOMmIJuaA5dXf3fWfGKNdTINnIM4ch3uRIl6AHVAvyHLh5s11wM_He7-snLJ67RPKDZLY8RL8ihWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش PGSA نسبت به تحریم از سوی وزارت خزانه‌داری آمریکا
حساب رسمی نهاد مدیریت آبراهه خلیج‌فارس در ایکس:
🔹
وزارت خزانه‌داری آمریکا اخیرا از تحریم PGSA خبر داده. PGSA  ضمن محکومیت این اقدام، تحریم‌ شدن توسط کشوری را که رئیس آن به دزدی دریایی افتخار می‌کند، نشانه‌ای از عملکرد مثبت خود می‌داند.
🔹
علیرغم اقدامات تنش‌زای ایالات متحده در آب‌های خلیج فارس و دریای عمان، این نهاد در راستای تسهیل تردد، بی‌وقفه به بررسی و ارائه مجوز عبور به شناورهای غیرمتخاصم ادامه می‌دهد. به زودی آماری از ماه اول فعالیت نهاد PGSA منتشر خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/654728" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8e24418.mp4?token=qpMLZqkpoNSPpBSwwyDOuE29uT2GRCAHbTKlrLQjDboux-SYeyGBQeCXPMd7wp0XTgEZOE9ORtFGEA66XjZLUftS0syCC12EJ1_oW2uNTJhYu18auaAJs5dxNAR0OBky9wYdLSMpxNNdTzvAwlwvLFXHB7Ydzwzs05d1S9J9szYB92u6855YvMwCn8mgECX9tCCpeFH8jNjTfEMTx14IIt2sbU6VbUOPlvaJ4FvaSx-Ya9t5YMZMR0hUMQpBCb0Vet1yeS28SHLhxYmzHkUWIpvIyEW4BnAi9tnRSQPGS4WHsiA4E8R5MpQ1AI5ykqG-4rUAs31NvcamVo2xb84uFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8e24418.mp4?token=qpMLZqkpoNSPpBSwwyDOuE29uT2GRCAHbTKlrLQjDboux-SYeyGBQeCXPMd7wp0XTgEZOE9ORtFGEA66XjZLUftS0syCC12EJ1_oW2uNTJhYu18auaAJs5dxNAR0OBky9wYdLSMpxNNdTzvAwlwvLFXHB7Ydzwzs05d1S9J9szYB92u6855YvMwCn8mgECX9tCCpeFH8jNjTfEMTx14IIt2sbU6VbUOPlvaJ4FvaSx-Ya9t5YMZMR0hUMQpBCb0Vet1yeS28SHLhxYmzHkUWIpvIyEW4BnAi9tnRSQPGS4WHsiA4E8R5MpQ1AI5ykqG-4rUAs31NvcamVo2xb84uFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های محمدرضا گلزار در خصوص نمازها و عبادت‌هایش در نیمه شب که با واکنش کاربران فضای مجازی مواجه شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/654727" target="_blank">📅 23:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654725">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای وزارت خزانه‌داری آمریکا: محاصره اعمال‌ شده بر بنادر ایران به‌تدریج برداشته خواهد شد
/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/654725" target="_blank">📅 23:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654724">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdmb7se-hOrxR3ylS0ZIWXZxY1fH_wEmzvEP_axcxVaAUiR8US9nNKgV6k6LDuWdiaJHDN_9BzAPfc4A3jUXmllA_-BusuLakub3fhFDcIk5aUBR2zoAF1bmCzTeXcWzn6kxN2VKYQHwMizjFoCZHcV6iTAu6QF_FdKcSkZSMdCnoJ0AP-eggFFV6lKaWYl40wLQS8AZvCsVFiB863qCACLPWWD8UR79JuB43z2N4tDPZ51EJ6LZ9_nO6TOJalxLm60ZSzQlxHnUhdKlSiOQKbcxOmgv2Ee864LRsd2naUlsZ2OqTTu1jKS67g6XT8uEyxWm35IdzZZSHUe4DLEZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ برای پایان جنگ ایران چقدر باید تحقیر را بپذیرد؟ | شکست را قورت بده!
🔹
توماس فریدمن، ستون‌نویس برجسته نیویورک تایمز، استدلال می‌کند که دولت ترامپ پس از آغاز جنگ با ایران اکنون در موقعیتی قرار گرفته که برای خروج از بحران ناچار است به توافقی تن دهد که بسیار شبیه همان توافق هسته‌ای دوران اوباما خواهد بود؛ توافقی که ترامپ در سال ۲۰۱۸ آن را «فاجعه‌بار» خواند و از آن خارج شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3218302</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/654724" target="_blank">📅 23:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654723">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/654723" target="_blank">📅 23:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654722">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عضو شورای عالی انقلاب فرهنگی: امسال تغییری در تاثیر معدل بر کنکور ایجاد نمی‌شود
سعیدرضا عاملی:
🔹
طبق ضوابطی که از قبل اعلام کردیم، هر تغییری در قاعده سازمان سنجش باید از یک‌سال قبل اعلام شود، بنابراین امسال تغییری در مصوبه نداریم و همان اثر قطعی معدل یازدهم و دوازدهم پابرجاست.
🔹
در این خصوص نظر رئیس‌جمهور بر بازنگری مصوبه است و از این‌رو در اثر قطعی معدل یازدهم و دوازدهم برای کنکور سال آینده بازنگری خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/654722" target="_blank">📅 22:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654721">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdV-AofsK4XoJy2cumRfUO7PP5DhvRAd6FUceLCjbWQf4igW-ofCqR5f_d-1GAl6o3FfxNXtHP6Cw_w3_8q8VoYGbgltEC8FvWIi_KoYqOSHHXVG28l2ynEkLsdhBuUhzwk3xd2PyVPH5_DvAUF21FAy_Cis73PL60_RUucfgqFCuANFW5qYmXz1qTviwHyop1_FB0pEHLXm0QcXIr-Zr4pCN0qgnU4JVrI7wDYtZk7CDjm5XZoqmKsb7oKxJ7vbSidMqWnuhnX6jGH8_96vfEGrYleY0hkLNdEqg__hoxyXzWwE5Ch6cFTYy18900nnTRkNfn20kjHB-BPIZXA5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده‌ نشده از رهبر انقلاب اسلامی حضرت آیت‌الله سید مجتبی خامنه‌ای در سال ۱۳۶۲
🔹
از راست: دکتر علیرضا مهدویانی فوق تخصص آسم و آلرژی و رئیس بخش کودکان مسیح دانشوری، مهندس علیرضا خواجه‌سعیدی، آیت‌الله سید مجتبی خامنه‌ای، احمد غلامعلی و مهندس مرآتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/654721" target="_blank">📅 22:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654720">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رسانه صهیونیستی: تل آویو پیشنهاد بیروت برای عقب‌نشینی از لبنان را رد کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/654720" target="_blank">📅 22:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-IOv79KRwC7Hh1qYV6z9XzAVExVYUnTpNiBIxEhIsosytRPo0r9ueXEJ-ARsk88MjwFFRrsFqFrj5yt5CpyY6Hn4YCWu8rmpm5rUfITLiX9IPOOmCk_1dyAsBQTy59qUYwShkI-9TjBG22Tuv6phQb_b75z_bw0LH8gK7hcLNiw3VVdyJiBlE0I904te42MI72uBiQA0aZKP3vP_P_q4WN-pYIroAN1VIJqynWOWeXfilCqEGkAq_Fppu3sTgAWRHpvACwaSCbbzdj2f6lkpkWFXAbSShEFRXNUYzTnh8oe05D6nd9tXYFADLPa7FbRjU6nRqA-Rjri5EGelSFOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای المانیتور: تیم ترامپ یک صندوق ۳۰۰ میلیارد دلاری برای ایران راه‌اندازی می‌کند
المانیتور:
🔹
تیم ترامپ، در اقدامی قابل توجه، ایده ایجاد یک صندوق ۳۰۰ میلیارد دلاری را برای ایران مطرح کرده است.
🔹
این پیشنهاد در شرایطی مطرح می‌شود که پیش از این، تهران یک پیشنهاد تجاری مشابه را رد کرده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/654719" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
نیویورک‌تایمز: مسئله دارایی‌های مسدود شده ایران هنوز جزو موانع مذاکرات است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/654718" target="_blank">📅 22:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: ترامپ هنوز تصمیمی درباره توافق با ایران نگرفته است
🔹
مقام ارشد دولت تروریستی آمریکا به روزنامه نیویورک تایمز گفت که دونالد ترامپ، جلسه‌ای حدود دو ساعته در اتاق وضعیت را بدون تصمیم‌گیری در مورد توافق با ایران ترک کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/654717" target="_blank">📅 22:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzeRKnabsqU7azFAzI56RJDcwWtDY-Nv4o5a-TSaZq8cVpklgJ_Zp7vaDpiuvXKYSWU8hrZjNzKz3c4NiHGbMcrBdQAON-JECg_SN-Gey8WQQhLcn8d1u0p5Mbmi7VzkcyfnnA6-RykKQ0NBCZJB_BQo2ps16JM2V8GlAOzvAGiNMDjeFy4_Gp708Pz84ijVGRbfN-BmNq_VHLJdIoxRgwWSoJarx8cHiiOMOspXqduFqPKo9N_CgL0l7ITkOiD8RwPuoxrP_vNFjLoQ5X2wE4llhOBrCaA6MPv-P0yKQU5MQF7aNN_qtw8XdjIxYD2ewIeDFjoh1KZHeDGuTEmLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی جام جهانی ۲۰۲۶ / شانس قهرمانی ایران فقط ۰.۳۳ درصد!
🔹
بر اساس جدیدترین داده‌های مارس ۲۰۲۶ از سایت معتبر Sporting News  یکی از منابع اصلی در پیش‌بینی‌های ورزشی جهان، شانس قهرمانی تیم ملی ایران در جام جهانی حدود ۰.۳۳٪ برآورد شده است.
🔹
این عدد معادل شانس ۳۰,۰۰۰ به ۱ است و ایران را در رتبه ۳۰ از ۴۸ تیم شرکت‌کننده قرار می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/654716" target="_blank">📅 22:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuBvdcrhNo7A9reXfP6zUE3sf-Qx7aQT0BzV981ff8uaGGF50LUfWQgqCnRJJLsy0fPU4WyZSnHbVYfSfzCTruEg8KX5nRzVwv3K0wa4y6TAWObPPh5RbgwtHcdU3d-lOWQQlYMxgPIm8nWNrLu-WGI-G3ja5AvWT_7UIHKVQ58X5x5QlpYk39GYewAorRC3XSVXmgE2V5Xg7QpM-y1ZiiyD2hEAThP5Mh2CpR6Kq1mG56efNOuPdgJA20nsKiIh_Q-EjjlpgkIKypzTrhsSRksktLW4OP8aDUJFXR5dGXCovgSRepa9BAqzXnn24K3W_wHbiW2IEWELs5g0FIAzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی به اقدام رژیم صهیونیستی به قطع کامل روابط خود با دبیرکل سازمان ملل متحد به دلیل قرار گرفتن نام این رژیم در فهرست سیاه خشونت جنسی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/654715" target="_blank">📅 22:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krfzhk5HM1RPMuvPgYiOJu5QYx4u7G2LS1WZ3n3-xL8bnYhaoXoX7YPr8ugCjQcAYYsEw_zhfYZaHkI3TsYeRs8NCTKCsD7Pqh6Czfh-7wOR3pI9lpI1QPc7cST4HehM6zCXzv0fvcLdAG0V-cipYxIoUNW73_xzEREN6RexFEg4MHpttcxdKDKwQCvilXqusCeo_L2aNTu8HmBYym3sL7UYGEoffUo0tm7ogfQvF3HgylN2dERmBVD_k1IDAg3hWyY57m6jjc8dkmo2o02D6GI-BSQahlR8to1SVM96k6I9yduT1-P462B76FLAp5jJAAZcJQzZhxEOG9DCrzsncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور آمریکا: شاید خبر بزرگی در راه باشد
فاکس نیوز:
🔹
داگ برگم، وزیر کشور آمریکا گفت به زودی با ترامپ دیدار می‌کنم. شاید خبر بزرگی در راه باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/654714" target="_blank">📅 22:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 59</div>
</div>
<a href="https://t.me/akhbarefori/654713" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ونهم
رائفی‌پور:
🔹
0:06:50 عکس‌العمل قوم یهود، مقابل اعتراض حضرت موسی به گوساله پرستی آنها
🔹
0:21:45 رزم‌آوری و شجاعت امام حسن مجتبی
🔹
0:29:00 دلیل صبر حضرت علی (ع) و هارون
🔹
0:52:40 اتفاقات مستند انتخاب جانشین در ساعات پایانی عمر پیامبر
🔹
1:02:00 عاقبت تبهکاران در قرآن
🔹
1:10:40 مرگ جاهلیت یعنی چه؟
🔹
1:29:30 آثار خواندن زیارت عاشورا در زندگی دنیا و آخرت
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/654713" target="_blank">📅 22:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
شنیده شدن صدای فعالیت پدافند در محدوده جزیره قشم
🔹
شامگاه جمعه صدای فعالیت پدافند در جزیره قشم از سوی ساکنان محلی گزارش شده است.
🔹
بر اساس این گزارش، ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند./مهر…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/654712" target="_blank">📅 22:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
الحدث: هنوز اطلاعاتی در مورد «تصمیم نهایی ترامپ» درباره توافق با ایران وجود ندارد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/654710" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تدوین بسته‌های حمایتی جدید برای گرانی دارو
محمد رسول شیخی‌زاده، دبیر کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
با افزایش قیمت دارو، بسته‌های حمایتی جدید در حال تدوین است تا از طریق بیمه‌ها بخشی از هزینه‌ها جبران شود.
🔹
در جلسات تولیدکنندگان تجهیزات پزشکی، موضوع افزایش تولید داخلی بررسی شده، اما مسئولان می‌گویند راه‌حل سریع فعلاً واردات است و کشورهایی مانند ترکیه که توانایی خوبی در تولید لوازم پزشکی دارند، مورد نظر هستند.
🔹
تولید کیت‌ها و تجهیزات پزشکی نیز در دستور کار سازمان غذا و دارو قرار دارد، با این حال زمان دقیق آغاز تولید مشخص نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/654709" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شنیده شدن صدای فعالیت پدافند در محدوده جزیره قشم
🔹
شامگاه جمعه صدای فعالیت پدافند در جزیره قشم از سوی ساکنان محلی گزارش شده است.
🔹
بر اساس این گزارش، ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند./مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/654708" target="_blank">📅 21:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
روزنامه وال‌استریت‌ژورنال مدعی شده امارات متحده عربی در طول جنگ ده‌ها حمله هوایی را علیه ایران با هماهنگی با آمریکا و اسرائیل انجام داده است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/654707" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whb1ja16_pkUOeXOjqjp9dx6sx4ZMhSTxfA4ISWSX7JOrGFBj4Jh39xPagLnLpEihzwsSlLs9vOtQvAa7K1CgKXu15OtQYFUPnfZxwOSiizBWb8v6CYLyeh1w7oR5RvskGwf6wCXLZTHkVLuzSxFUacCMGhPhnQDipAOwQEXrRc3eIIj-5xN9RcT0rZNQG1VmFiTHCtvIgUF_1T9MuC8D-7VJmOf8DWdw4jEN7uRwoVcfJwL9bkQsjd1q9GnpNYJRGhq2IfQdssrJEFppdhjwL7VC_adoePReuu0_NDGVvHKFDxiD0_W3eFkMF1x38SZvU4HiC2KydJ04eaL_JsaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ رئیس کمیسیون امنیت ملی به ادعاهای اخیر ترامپ درباره توافق!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/654706" target="_blank">📅 21:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKRW_qC6BkOs3kQKSdPWlozrwGQdgaAr3TbsZsqDq4d46mwXEgDs02Z_KCltj--duon_y_aqS2kqQZVfI9-R-Df5CUKD_gPIXe1OwDosUGQ3XnpO2kO1AakNVC1HZsiPJ6ctLv3ytlCsXtbWHrBvsHg8dIsNP3mTQiG-9B0QBTMpr9j25E6wiOUV3pQgq_ULeTveq8u4TkSqEzqv0YcXZPxEgercxFRzMMwLcFzVnNCyew41EGetGWcAUcc9zgapG6uIucRhLa_02XYk2TzVXkVbtl-aBIdYqDdULyWK7p_bc4IEvNB6FdBEcxlAgISQ9mBvcRI6bTIJiNzVDk9elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWEeyTNg8-g824xSwe9Uo-E0gTjQ-Y-PKkmQYoCHli9x6wVADQGeRSN1GoqM2-IvChp8YAxUsl948V0N08FxCRDJkvg09M00dzfyiP88XgaIPcPDvf1fGX1dS5GaMbS00zUZGytEfAybD3OBf1oiMj615Cs1bcoD1-SQkFHW9eozMRSv5wKquVZZIwAp00WTYCC17f0aJCgThc29muLpWZGoaIa7cfU2pY7Dj82FEpetgz7qM89z0VBYC0hFIxIHveNLcNP97eSDX76EuWW6HZdr6nNDeN1renGgn5GmkDm1T7SodkhNM3tROYkZZikk4eeNdWjxXuq_tVtslzn6ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین تصاویر از ماکت آیفون ۱۸ پرو در چهار رنگ منتشر شد؛ آلبالویی تیره در مرکز توجه
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/654704" target="_blank">📅 21:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654702">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای «اکسیوس» به نقل از مقامات آمریکایی: ایران تنها در چارچوب توافق نهایی هسته‌ای، دارایی‌های مسدود شده خود را دریافت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/654702" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654701">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای بلومبرگ: یک چهارم نفتکش‌های بزرگ گرفتار مانده در آب‌های خلیج از تنگه هرمز عبور کردند. ۲۹ نفتکش از تعداد ۱۰۹ نفتکش گرفتار شده، موفق به عبور از تنگه هرمز شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/654701" target="_blank">📅 21:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0d8f9fa1.mp4?token=tQ4ZGOqkc41c1Quoi4IUl0BKZrSAZsdLqpZ12eOl6rB76ueLZny3sNtf37HVfQL9P4-tQSayieX5rzL1JTxM_HQisw5gZQsaUlGyCfkP_oMJvcuEaogIlWoOcGpFwkkcDqY6wF_KzHQM-MdWI0D4zzBABVcOpE01cVPwBHrjTHCWIS5UsGhZQV7YH_bdj2TowwYuqW5a0u3uXSwmCcGKwveVcbTZ0V8GnrsaRXV3uJlBX97OOhsThIb9N16auM7qHdWU7xBGe-VZ4GyixBzLzhP31cRpi2gToJpaLrRGRf-QX8S3QjaJqLdgGYeLbdDx6pvZW5AJWoHVA_g45F4DYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0d8f9fa1.mp4?token=tQ4ZGOqkc41c1Quoi4IUl0BKZrSAZsdLqpZ12eOl6rB76ueLZny3sNtf37HVfQL9P4-tQSayieX5rzL1JTxM_HQisw5gZQsaUlGyCfkP_oMJvcuEaogIlWoOcGpFwkkcDqY6wF_KzHQM-MdWI0D4zzBABVcOpE01cVPwBHrjTHCWIS5UsGhZQV7YH_bdj2TowwYuqW5a0u3uXSwmCcGKwveVcbTZ0V8GnrsaRXV3uJlBX97OOhsThIb9N16auM7qHdWU7xBGe-VZ4GyixBzLzhP31cRpi2gToJpaLrRGRf-QX8S3QjaJqLdgGYeLbdDx6pvZW5AJWoHVA_g45F4DYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
بمب لاغری سال 2026 رونمایی شد
💣
هرچی دوست داری بخور و لاغر شو
🧭
رسیدن به وزن دلخواه بدون ورزش و رژیم
🧭
۷ الی ۱۰ کیلو کاهش وزن  تنها در یکماه
🧭
دارای تاییدیه وزارت بهداشت
برای دریافت اطلاعات بیشتر و بهره مندی از تخفیف استثنایی، همین حالا روی لینک زیر کلیک کنید.
📲
https://landing.creditsw.ir/5UlSL
https://landing.creditsw.ir/5UlSL</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/654700" target="_blank">📅 21:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654699">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqd31nJ1_8-p5vhAnrX5CiKb5hjPSTOQ7trWxXwd1UD2kMSfglXRYyANCN_4gtK7-5mZUU9IsJVbb7Fl7DqPNLHDY6V9LWbgd9QUzNkpTgqPQxbRnHfcVzwAAXqV-J0CJr1EhDTM7peU0QNKVqogkJZCGehpY7pS7T4BdugCD0DF4R8Oj61TK4dyQAywqRwUfYQBVzedO8_quzQl5WLYbAr7VuhzQ2Xr73zoF3Ueu7uPdKT4mSInf7f3ld1UwcjNwOZBPbRs2nlV-g4j4yyfdHFZnssjiQLNTsbHrD5YHS99ysQ5-OhvnBl5NwNMgYRRvGf5sDaROfNjxqexH-sXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ایران با شبکه‌ای از نفت‌کش‌های پنهان، تحریم‌های نفتی آمریکا را دور زده است
🔹
بر اساس گزارش وال‌استریت ژورنال، ایران با بهره‌گیری از ناوگانی از نفت‌کش‌های قدیمی و انجام انتقال‌های مخفیانه نفت در آب‌های مالزی، توانسته میلیاردها دلار نفت به چین صادر کند. این گزارش می‌گوید پنهان‌سازی هویت کشتی‌ها و حمایت شرکت‌های واسطه در چین، به تداوم صادرات نفت ایران و کاهش اثرگذاری تحریم‌ها و فشارهای اقتصادی آمریکا کمک کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/654699" target="_blank">📅 21:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654698">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: ادعای ترامپ درباره سرنوشت مواد غنی شده هسته‌ای آرزوهای او است و ربطی به تصمیم و تعهد ایران ندارد
🔹
ترامپ بهتر از هرکسی می‌داند بدون آزادسازی اموال ایران، توافقی در کار نخواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/654698" target="_blank">📅 21:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654697">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رد و بدل پیام‌ها ادامه دارد  واکنش بقایی به ترامپ:
🔹
ما از ۴۷ سال پیش خداحافظی کردیم و دیگر بر اساس بایدهای دیگران عمل نمی‌کنیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/654697" target="_blank">📅 21:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654696">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تلگراف: جنگ ایران، سخت‌تر از اوکراین به جیب اروپایی‌ها ضربه زد!
تلگراف:
🔹
تحقیقات بانک مرکزی اروپا نشان می‌دهد که تأثیر جنگ ایران می‌تواند مصرف‌کنندگان منطقه یورو را «دو برابر» آسیب برساند.
🔹
حمله روسیه به اوکراین در فوریه ۲۰۲۲ باعث بحران انرژی و تورمی شد که اروپا تا حد زیادی از آن بهبود یافته بود، اما سپس حملات هوایی ایالات متحده و اسرائیل جنگی را علیه ایران آغاز کرد که منجر به اختلال بی‌سابقه در تأمین انرژی شده است./خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654696" target="_blank">📅 21:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654695">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1PgebOQTUlQ5sczuJqozh2fp3LRX4BXesTzXAKggsrxMmrMbHw3O0CzetAacDWdkr2ZgVZeyfBYAML9neRfUNd4vcHZC7SQEWgEGfTjp8mpmxyNOk3i-GiSRG6l84HNrzBHl7Hfpz_0mlITG4Rr9DSFFA5AUSMrV5Eb1WBtedVPo4m6Pb2hc0qIRxGCHO9T6yBzBuvgkoWFVZPtJoNtgru2d2ulPc1kwQFQkbl1n9dohZiJKb56xrxykpfeP1F6Fft04xvjDwXcsGp7M-GV8mvwhII-w6_Eg1QSzVhgF9qs74NxzFmHo40ruSLKnORg_1bLEAWTjSp0X2yT2iqTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی دوستانه| گل سوم ایران توسط مهدی طارمی
🔹
گامبیا ۱ــ ۳ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/654695" target="_blank">📅 20:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osbbJEU_sMB-pfhsg7aquctx8RnOqISF2aRXpdWFaacXkjYydrBpiNACcQq-ihQvPjBnZnPthL1X4zypj0NLIXSUM6S9w4XlDip-lvTStJuEEdGkqS1qHeGyZiV2VfISx-qpifUAdVy3ZjlIY3Q4PZj5CLgE_5B-rP3hxwYjhTgatkd5xFwcaxrQd5r4Q9DkwgamuoFKfW7NMePjJOniq1RSLOANE24xLJdpKxRaRKt3zLXfcRn3KowxqGQ3yJyyp7Lx_c3MDXzaUbz9RGn8kr_nlplHvwyiPSoJwXclLIYS3hACyXrkqnYbLVctU_sFKF0WacctDN05n5iqcsKm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تاکنون تفاهمی با آمریکا نهایی نشده است  بقایی درباره ادعای از بین بردن مواد هسته‌ای توسط ترامپ:
🔹
در این مرحله تمرکز ما بر خاتمه جنگ هست و درباره جزییات غنی سازی و اورانیوم غنی شده، صحبتی نداریم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/654694" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ خواسته‌های خود را فهرست کرد  ترامپ مدعی شد:
🔹
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب اتمی نخواهد داشت. تنگه هرمز باید فوراً برای تردد آزاد کشتی‌ها در هر دو جهت، بدون هیچ عوارضی، باز شود. تمام مین‌های آبی (بمب‌ها)، در صورت وجود، منهدم خواهند…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/654693" target="_blank">📅 20:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654692">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwzMxp8WbPiFdOai-LknuMsxQruoTcOvUQ0gJMmTpAM_ucWnQ9B8_x86oG6jeiaikmgq6wUCt4shglQwpHPa5JG3IcKlHDW4Vf7YmpOxlXajdAAl78EynTXUS2YU5rNy6bFOMRM6voe-XHwn-oI2KU_x8bMP7hXhmcbstHGhZM_G58DUE9X_GTm1WosvbLQOQ7W4r8lA-8pqgzEVbl8U6N5Q_3jEPHLoAK7VHwEPOVFsg1hmYbmDKF_I0piuae4jhoetSxAubbnU95z_M0b-uRh6XTgInjtCtuUN_NwEM_zbUb7WQhX_bAW4K_KzutBoNXtlPFsbjG9MaV6LklNMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه رکود در بازار مسکن تهران؛ معاملات به زیر ۴۰۰۰ سقوط کرد
🔹
بازار مسکن پایتخت با شدیدترین رکود تاریخ خود مواجه شده است. میانگین معاملات ماهانه که در دهه ۹۰ بیش از ۱۴ هزار فقره بود، حالا به زیر ۴۰۰۰ رسیده است. یعنی بازار مسکن تهران فقط ۳۵ تا ۴۰ درصد توان طبیعی خود کار می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/654692" target="_blank">📅 20:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654691">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
پیشنهاد گروسی: قزاقستان اورانیوم غنی‌شده ایران را نگهداری کند  مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
قزاقستان آماده است در صورت توافق ایران و آمریکا، ذخایر اورانیوم غنی‌شده ایران را در بانک بین‌المللی اورانیوم خود ذخیره کند.
🔹
«ما محلی داریم که این [اورانیوم…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/654691" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654690">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رد و بدل پیام‌ها ادامه دارد  واکنش بقایی به ترامپ:
🔹
ما از ۴۷ سال پیش خداحافظی کردیم و دیگر بر اساس بایدهای دیگران عمل نمی‌کنیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654690" target="_blank">📅 20:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654689">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db29ecf26.mp4?token=QjPgzzXNpReBfyJOkMC0D9k9ejWAQzAW_urXs8G1RST9kidjUQnr0a6Zn6BzVzx7yszKY-7nvapx8TYwr9tPSPXDZHT0wJnZ116kxSW4uEgQYdqCdfmCpKnPf4YP_hXxY4H2S5yU9L-ofopyffy1vRxxgPVfZ4bA--HCZ3xYyv_PCoDfq9fIP5a-vQsxjb35udXwywjLLunlubg6jgiVjoZ1pAQzYtu_OgoW3yWzFdomiDZKMTYbLwaoQseQP-f8Vki4jebjr9_MAMVOXv9Rh4wPWtTjo40AbI3gRLauPtV2eEHABnHwA5h2j1D9w-RIJkWntnyoMi7GA-I9q7-_rTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db29ecf26.mp4?token=QjPgzzXNpReBfyJOkMC0D9k9ejWAQzAW_urXs8G1RST9kidjUQnr0a6Zn6BzVzx7yszKY-7nvapx8TYwr9tPSPXDZHT0wJnZ116kxSW4uEgQYdqCdfmCpKnPf4YP_hXxY4H2S5yU9L-ofopyffy1vRxxgPVfZ4bA--HCZ3xYyv_PCoDfq9fIP5a-vQsxjb35udXwywjLLunlubg6jgiVjoZ1pAQzYtu_OgoW3yWzFdomiDZKMTYbLwaoQseQP-f8Vki4jebjr9_MAMVOXv9Rh4wPWtTjo40AbI3gRLauPtV2eEHABnHwA5h2j1D9w-RIJkWntnyoMi7GA-I9q7-_rTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داغ‌ترین خبرهای حوزه فناوری؛ رقابت غول‌های تکنولوژی جدی‌تر شد
🔹
گوگل و اپل چه در سر دارند؟
با هوش‌ مصنوعی ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654689" target="_blank">📅 20:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
الجزیره: ممکن است همه چیز برای اعلام رسمی توافق آماده باشد  نورالدین الدغیر خبرنگار الجزیره در تهران:
🔹
ممکن است همه چیز برای اعلام رسمی توافق آماده باشد، با وجود برخی اختلاف‌نظرها بین تهران و واشنگتن در پرونده‌هایی که در مسیر حل شدن هستند، و احتمالاً مشکل…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/654688" target="_blank">📅 20:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fb1f2f51.mp4?token=RVqty-5uoReg-KsosuhsKCqRubfgv4rbmjar-jFrxGNcbJJJwi2Mdw6WKLaPLWG2mwVIpWWxBLP6nxzwVehMZpp2wP6Y8qtQHQfsCvk3QvYmjaJIvGZYJB4W7awXKrY0RVJqZCmEAe9c3aJu5EpVi1nWLztGVyhuu0QGaglQ9goC5EbJX8szvfRM5stGg9Q_DUxndo3GmLfmwAkrhsMdrq5oJguHqkyYT4rZnz4l5s5L-7lo-2y1Exh4N_5iKEkDvYWKpfczATthh8vob0Abv45SaHztHNEACnDps1Dh-dY0uNa5NUtGs7WIJLFpmFuxKdln5Ou9IXn0kzyYc7fKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fb1f2f51.mp4?token=RVqty-5uoReg-KsosuhsKCqRubfgv4rbmjar-jFrxGNcbJJJwi2Mdw6WKLaPLWG2mwVIpWWxBLP6nxzwVehMZpp2wP6Y8qtQHQfsCvk3QvYmjaJIvGZYJB4W7awXKrY0RVJqZCmEAe9c3aJu5EpVi1nWLztGVyhuu0QGaglQ9goC5EbJX8szvfRM5stGg9Q_DUxndo3GmLfmwAkrhsMdrq5oJguHqkyYT4rZnz4l5s5L-7lo-2y1Exh4N_5iKEkDvYWKpfczATthh8vob0Abv45SaHztHNEACnDps1Dh-dY0uNa5NUtGs7WIJLFpmFuxKdln5Ou9IXn0kzyYc7fKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی دوستانه| گل دوم ایران به تیم ملی گامبیا روی شلیک رامین رضاییان
🔹
گامبیا ۱ــ ۲ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/654687" target="_blank">📅 20:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
تشکیل ستاد برای برگزاری مراسم تشییع رهبر شهید انقلاب
رئیس شورای هماهنگی تبلیغات اسلامی استان تهران:
🔹
ستاد ویژه‌‌ای برای آماده‌سازی شرایط یک تشییع ده‌ها میلیونی برای قائد شهید امت تشکیل شده و مجموعه‌های مختلف در حال انجام هماهنگی‌ها برای برگزاری باشکوه این مراسم در موعدی که مشخص خواهد شد، هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/654686" target="_blank">📅 20:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrU675l8EMELEbWeMOtmGoA7AneFM-L0pvKQhhcNMp1NBNYeM20IiMoce0S1sV-vAVGqs942hblF_-w4niwUvc_-hPVAeSlUUNWbiWCVxGIcB8sra3W7jNBqz6nWRIu8NtCN2XVmFF3J_K_bjoT51RoUrFEVoGRbVIwYcgOynAr2-TqFdweSFvUdvpbVcsU1b9XbYZL7dmOTOeVd6V7teYFMVOQ4XiIoqQAyAl1-9I1gk2lIjF2t1ao1sS89Ds6FisGuYYEsklDDLc_dp0Ltw_TTBAwc2tY6aatM6HBmmV8xdy_0EI5g0SMyXJ1xe3aaYqURFa0wyk2lvsaomLReJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر هوایی از برگزاری مراسم روز عرفه در گلزار شهدای دانش آموزان مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654685" target="_blank">📅 20:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654684">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d113573bf.mp4?token=oJEr556zc8wxa6qkTFJwgFowrkMcM_WIuEe9l32eSC861mQUjoiTCAoUB89gAYsWEmRACJY1srjhs4_Jei1ukVu7Zm5AiWpvhVyjmtRh8PkyscJaMjTQb09uyzHFBUXSa-re_ZFa_Ydn20EPgfdFAXgBB8SMlFa62i-iryklRhHd4hEH8hTe_z1AiA4jkjQWX72_DPlg8zXT1Lgrl3m0IIsZ_QDiriX2_2cAzjyueTQkN1-q7bKSRWqDhCpR9oS9r6xTgqLBQXs5JjTYyJT_opDmJzI2KgJzygPXYkFg-g3U3TAXtif1f9znlw-Tk7c958PyuPHI9KXhGvIcpvkE9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d113573bf.mp4?token=oJEr556zc8wxa6qkTFJwgFowrkMcM_WIuEe9l32eSC861mQUjoiTCAoUB89gAYsWEmRACJY1srjhs4_Jei1ukVu7Zm5AiWpvhVyjmtRh8PkyscJaMjTQb09uyzHFBUXSa-re_ZFa_Ydn20EPgfdFAXgBB8SMlFa62i-iryklRhHd4hEH8hTe_z1AiA4jkjQWX72_DPlg8zXT1Lgrl3m0IIsZ_QDiriX2_2cAzjyueTQkN1-q7bKSRWqDhCpR9oS9r6xTgqLBQXs5JjTYyJT_opDmJzI2KgJzygPXYkFg-g3U3TAXtif1f9znlw-Tk7c958PyuPHI9KXhGvIcpvkE9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی دوستانه| گل تساوی ایران به تیم ملی گامبیا توسط آریا یوسفی
🔹
گامبیا ۱ــ ۱ ایران
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/654684" target="_blank">📅 20:23 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
