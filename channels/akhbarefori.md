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
<img src="https://cdn4.telesco.pe/file/FHadioX0GrbajPg9EV7dJdGyH5-KIOqcUbiMhmHC9gRh-FTSQVeZpppE9G0ADWLYXehZKjpSzvcPxbKfmc3XtOCnSlFXsXfymYTJ9dE8Vw2B-x133CPALaBhHEZbuWXHUY4QMsAqDXPZ7EZrAgZMnmPotxeutskqHbQGtfORB7JQznGB9ny1NP2raqffJBLquzvqgFjt0WSN95jqPZm02TeGSQFvKv3vxPaPYHRoVxV26OT72x2qVakmigMh5tQHvbH2hLIvH_4-hGT2Cot9xAczd7v6_jJMi6tWyJ1jyvb-0dvXH8BNOo76MtUsNwEf4pj855Vg--OTEpVaqAn0gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 12:59:04</div>
<hr>

<div class="tg-post" id="msg-675090">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTkNgVBEXWFLZsyMffm31HMZ96Q_13duIdbFxgczqw7yeBA7cfr1jnwcIgk34JEQ14rFJ0gxPK7_gCk3yG-VIuq9Ef2QZis4s4N7QBLG-I9zCnKtx0AhgdbusAm0b-KmT22_REkoj61esoonHXa6FaRHhJzovPj2nApjwz2kQpLF54L-TMqpKXt8WdrymYnIUG0D3N1XsXcCidtknTLh2ZkCmAGqtHdezUy7FJGyd1anmJpvs4VTsjRrUNKoFeet3wpBXSETU-kyVJJjFL8ihDvdyJadQWtdtD9-ipJRaRBez8F_AV87k_3iIQcbkkJNzxgOJGn1ICbaTbzBwJy3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر فرماندار کالیفرنیا: ترامپ حرامزاده است
🔹
در پی اتهام‌زنی‌های دونالد ترامپ علیه «گوین نیوسام» در ضیافت خبرنگاران کاخ سفید، دفتر فرماندار کالیفرنیا با انتشار پیامی در شبکه‌ اجتماعی ایکس، رئیس‌جمهور آمریکا را «حرامزاده» و «خوک» خطاب کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/675090" target="_blank">📅 12:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675089">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snZoLh-WVDolkecH_WPRmoh9otYnaxhlKFhnNMOZw1wfwjR8g29MtpEi0GJ7DkXAQ8yo12Bw4m7MnNyenHXiA6xXrL-orqkg9pMbd_-kamptstcncVB8Pszi8pBOBF7nAaJk95WlCDmfavwgNQvHlgcKIq3Eme7Blnn8AqsaqpoyJsE9_My-BMFbuLhHZL4-x53Lhas5MyjwU1RcBKjTLoSsWnbN_n87XI6B55qXsSc5bm5Ch3EVaHb8FOShl89EfpJebY87aDqBbWjb8ijeVBhNpjN77jMzj_7k0ji19hjRbjVpeXMjdyeHiYj_-dFb23Pu8CLkkKYK6MBQFkHpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماندگارترین نقش‌های اکبر عبدی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/675089" target="_blank">📅 12:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQDiTOwj-URxmCWdIufVLX6QzOkLEuG7SWNSdMl8xZmEAdih9pcAxnwsFAxx1LLnIJcjSkViawK5z_ls7Mkqf21My_OVX7YVqGsy7QsNp4M2wOhElg88I1ur_7vpFH1kWbMVnTGHEcntSM3KnT-ie7Ro_s-k85-vXndkmP2ojMY_vVPXfscT5aCoN7yU1LtzrEDMakK8HWW-BA6SZct6MEIza-Hj3oFVSG_CKu__B1I4MAqtYaIYXYNqzvamFIWVWn6rJ3ZP44KvYZepwXbVF0vj3wEw9jn4Z3CcVKGLktEBGwFAPLIxaoy5X9tLd6ybVaWfRPbz7kob25IBmLaXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY2UttxjI4RmGae2Vug0ZeWz1-zXuXYMNAt-0gPO8Xh_l1F8TEdkzXUArLgg0HK_3_duOTQae1Uvs1Ep39c_qKzrWwk70VEJmOxAyq3LeIeiudE8VK2fgIm4wVS4_uy_g2_bH4tvg_tdp-EtPr8Rv9h2SoRwn_hRKmOVi4gO2aFbylSx5yp7O1gIJOVGtDixputo8jWyZ1kHG9uZEk_Wks5L9-EkK8LtpJ3tQVOx4WXmBxMi__5Tvkcf8oiAIFGACUmfAeipmxIu-VYJeFa4IGFosdLyjEVRbh_LtlbeUgZUniv6nIT3wpYbybhZ-r6dM61Kdfi_lefXB9b3smSXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgz0w68PJPQ6_OMMTXu772n3TDZrtyfTFhzLiIwBLlV0oS3UtgIyZvp7HDOzXr7lqEl3JFD36_awjdCR0uporkRpn4VGd4iJHMoWUMfBwHmskVHj1syhuKi5P4H3owJ8RXY0cha1cqJFj1gjlsq6g4APMpE_P7NMJ2A_tiqnOP5tOSUiN_d99a6yNFDoCu9koRbHzVlJUhu63x8MjZO2cwqCmE-EktjH5RcuyuyazmgdU_cPZdkQ8Sz7kZ6t4pGCHnAuyFVkKhVvgudAtL8NHKUkxOzbiGYJw9cACoiKbU3N2qWD0y0bfuJjha5HGs98x7hvaDUyLtsF8Uo9R4ZklA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای انهدام کامل سوله مهمات نیروهای ویژه ارتش امریکا -پایگاه ملک فیصل، اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/675086" target="_blank">📅 12:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
فرصت دو هفته‌ای بانک مرکزی برای رفع سوءاثر چک و اقساط معوق
بانک مرکزی:
🔹
صادرکنندگان چک‌های برگشتی و صاحبان تسهیلات معوق در بانک‌های ملی، صادرات، تجارت و توسعه صادرات که در بازه اختلالات بانکی اخیر دچار مشکل شده‌اند، دو هفته فرصت دارند بدون ثبت نمره منفی در کارنامه اعتبارسنجی خود، نسبت به پرداخت و رفع سوءاثر اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/675085" target="_blank">📅 12:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای گاردین: ایران با فناوری چین و تجربه جنگ روسیه و اوکراین، پایگاه‌های آمریکا را هدف می‌گیرد
🔹
ایران با کمک تصاویر ماهواره‌ای چینی و تاکتیک‌های آموخته‌شده توسط روسیه در اوکراین، پایگاه‌های آمریکا و زیرساخت‌های حیاتی در خلیج فارس را با دقت فزاینده‌ای بمباران می‌کند.
🔹
ایران توانایی موشکی موثری را حفظ کرده است که رهبری جدید آن مایل به استقرار آن است.
🔹
موشک‌های ایرانی دارای ناوبری پیچیده‌ای هستند و همزمان با پرتاب به سمت اهداف از GPS، BeiDou چین و Glonass روسیه استفاده می‌کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/675084" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادارات مازندران فردا تعطیل شد.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۱۰ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید.
🔹
وزیر خارجه مصر با ایران و عمان برای توقف تنش‌های دریایی و حفظ امنیت کشتیرانی رایزنی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/675083" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg8vdoPWvHjkYtC3BhBQP5Roib4HQANRzHdgH8HwJ_QtoyXxi57SS7txX4_UnbC82oiyfrsy7wxYej2FsJY5g2lAnZbL7raAPND-3UQY04z33gaKTKDU5G-FbDSl1Guh_VEUghhIbDxYCw78xFvkP34LWPCNx_C0J7kmTbHXaKJrSlJj3YIiOtBr4sLvO_9kf1XWhAEtOe_2eBKKa1kv9bmuiCBOVyy4GTJC73WqxC6-gehveDXmIwQpDU2taUqxnHL3cBttWz-RnVY-Jz53y0zoEXbihqCNfSUvX04WuJR9Dx4iqiKqov2U-EGYryl-sZUnzUo22tWd4XkKJeAjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد گزارشی از وقوع یک حادثه مرتبط با یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است.
🔹
این نهاد در اطلاعیه‌ای که در ایکس منتشر کرد، افزود مقامات از این حادثه مطلع هستند و تحقیقات مرتبط همچنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/675082" target="_blank">📅 12:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVm3ttSSrOAcNssWdOEKIAnSG4ixCzsoAOFVbAMcI_B3lKiSFQOM-pcGVX-BBZjsxXQLdD3K0hA2NZp9Sms4xi2bRMYBru32SzPai9ea9zFG4VMBKaB1sB3MvJ0bRvZn-Jgpi3s-KAMvsFLhgUKM1BOYu_osUEEx7L7Ny1bIfWaErUgghfC8cShaHp5FPmoVE40QART-0zBIS9nPuhZDm8HFZ4YvIVDw9lBnFoVKgrtqSUnFYtrhdsqpSeoFcphdBXrZrnjpEiu6_k2wMWLskrW0dfdRuE-3rXPHhdjqiIhQqHI_aYFGhcqjyBC6hgbZdaRSmVwN_nALZnN6mPzrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت: شب گذشته حمله‌ای به کشور انجام نشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/675081" target="_blank">📅 12:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
واکنش شفیعیان مشاور رسانه‌ای دفتر رئیس جمهور به مسدود شدن خبرفوری @AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/675080" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795cca7353.mp4?token=jZ_BUs2F3pBWmqZUn000UeN6Rt2VXFBJbXmsIi0yRLoGtXtYtgfeGTB8_0-VB3Ywh5Cl7jFG6PFhprfJsLcjdtEXCYzULIFE7I7nn3dBlwp3CRfz3t4ZS5TZ4jOrZt0dDTQHh0nQJWNj-MAJavi-TSu0sCqH8Yx_KKUoYCSunggz4J1h6GzhUJNhBr4YtexmxLU7upDErhRS3PCNhCW5jtUPNntIghdngHuMeJTXyhVWqRdHVc3yvAQTtZn5NATakZKethNejXIylBtVOumPqeJm1HIkrIsWY5Qma6gv27PfOabh45qGVRB770Qw5ty1BeFrAFEuCmgj_y6t058DWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795cca7353.mp4?token=jZ_BUs2F3pBWmqZUn000UeN6Rt2VXFBJbXmsIi0yRLoGtXtYtgfeGTB8_0-VB3Ywh5Cl7jFG6PFhprfJsLcjdtEXCYzULIFE7I7nn3dBlwp3CRfz3t4ZS5TZ4jOrZt0dDTQHh0nQJWNj-MAJavi-TSu0sCqH8Yx_KKUoYCSunggz4J1h6GzhUJNhBr4YtexmxLU7upDErhRS3PCNhCW5jtUPNntIghdngHuMeJTXyhVWqRdHVc3yvAQTtZn5NATakZKethNejXIylBtVOumPqeJm1HIkrIsWY5Qma6gv27PfOabh45qGVRB770Qw5ty1BeFrAFEuCmgj_y6t058DWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/675079" target="_blank">📅 12:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
گاردین: در توان موشکی ایران یک تحول واقعی رخ داده است
رسانه انگلیسی به نقل از کارشناسان:
🔹
پاسخ ایران به حملات متجازوانه آمریکا نشان داد که ارتقای توان عملیاتی موشک‌های ایران با تغییراتی در فناوری و سخت‌افزار این موشک‌ها منجر به «تحول واقعی» توان موشکی ایران شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/675078" target="_blank">📅 12:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCITuzzXTXNl5s6h7AzRj-3YTOI705i67GpJhZsd1AEiHWqIrmYBRTe5r5Tui7Rz3LYUQl8pPuE9zIT9uW1OkxSgTp0YvcskgFDusVLTWfHsYFrC06Od7JGhJo5tuBVHFrrpncw-p94FvpeBjPqMTC1M1eOsUnHRHCbKFmKK1Ipg77Gy46PlzBoHOPXtS4Q0e_B_f5dZP6Cs7knfbvydKo-VrH8dHV8-sJaGfNXwGuAc5ic8cgFtlNkaqLHNNzDd11lqmvfKSn5Z5q2ave4I7Md_7wVFQZqnyFzm3WQgOrOSq8UIbsid0VJwNh4_M9pMozeX1mzfSF42I2Pbi0f-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/675077" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e498ed3d63.mp4?token=eBQAbySaJ6vOb53jsrkKEJ7uXrILPlwNYLbYWby75vsJd7E7TCo2q-lWevFtspCokW70RPsBJDkaJTR45Vka_-F-Mer1HSF0qDpcPnxmPTgXTvktLTyOJMNwxdddTaEbTbwV85gqVOaAdfffLhxoQEIBapASUFZ0NciH8T56crA3aJBGRG0a8Zzd9rrE3gFUHCPelKYG68FLh9uj_XXJfBYDvx_H1gQkaWwxhmwb9AoD1trHxrZrkIwfSC_cnxA0KpS6BQGOAwLY93zRO3NCEUqhj3ehodg3O7UZHA_FVf7XpWUaOiqCs7wU7GG9OsyJgOk_GlyKV0hlEwbf_sA7Txw1riCKRTRcA3aM1mW0oSM9UMNp0NQWTE_jMzoZQw2DHbID6AOEQvscjRpHFMjj2vcVHoP4jf7iAep1CpEuEVvVGPkPKw_5HmAi3OTJvOkY0iSiJD2e-lv__OehX5a_rJo4_Pu4f5LYet3JktHoXY5KOxLJf3-VyCXM1yuz7oA3IN7cqyiFlVC3O4uVjN4n2X0G-dvXfJJ54QKDqNAIkOhgD-Eb8HfoBEWBhPZhzs1vC_G_M-GG8xtZz0kwNz6S7iX0uKMv41ONHUFiFRLe-2Xfb25VTPFzT_KBbZgL7fUt6eEmjXHkGF8bMKPjN0vexcKq9jM1IVNC3BwQgBNjdXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e498ed3d63.mp4?token=eBQAbySaJ6vOb53jsrkKEJ7uXrILPlwNYLbYWby75vsJd7E7TCo2q-lWevFtspCokW70RPsBJDkaJTR45Vka_-F-Mer1HSF0qDpcPnxmPTgXTvktLTyOJMNwxdddTaEbTbwV85gqVOaAdfffLhxoQEIBapASUFZ0NciH8T56crA3aJBGRG0a8Zzd9rrE3gFUHCPelKYG68FLh9uj_XXJfBYDvx_H1gQkaWwxhmwb9AoD1trHxrZrkIwfSC_cnxA0KpS6BQGOAwLY93zRO3NCEUqhj3ehodg3O7UZHA_FVf7XpWUaOiqCs7wU7GG9OsyJgOk_GlyKV0hlEwbf_sA7Txw1riCKRTRcA3aM1mW0oSM9UMNp0NQWTE_jMzoZQw2DHbID6AOEQvscjRpHFMjj2vcVHoP4jf7iAep1CpEuEVvVGPkPKw_5HmAi3OTJvOkY0iSiJD2e-lv__OehX5a_rJo4_Pu4f5LYet3JktHoXY5KOxLJf3-VyCXM1yuz7oA3IN7cqyiFlVC3O4uVjN4n2X0G-dvXfJJ54QKDqNAIkOhgD-Eb8HfoBEWBhPZhzs1vC_G_M-GG8xtZz0kwNz6S7iX0uKMv41ONHUFiFRLe-2Xfb25VTPFzT_KBbZgL7fUt6eEmjXHkGF8bMKPjN0vexcKq9jM1IVNC3BwQgBNjdXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی‌ وقت‌ها زیر چشم‌مون نبض میزنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/675076" target="_blank">📅 12:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_YZnPMFeERjML_eaUvyRkdyvPS8r_fgXus7IF9lbyWzFYiLrWK08pwNEPKu4-ZWBchDRZt5GO_tmSRB8eDQoRjtkN0pT0eK1ZmISSMnBA9HabmxSCVJYc-4oRAQuxMeWKoBvbsp10Srecax8LHrElm2PxUERlc_f8QnBH6iNqIgEg5ZOTNXYwIBxv5eZp5lX3f5otxTDjtOxWcA_nmSSpIqKQkX0qYyxb2M9QMSfAAqT4fE5dzaW6vBgvmQx1IIeiXk0CcUbBcnvIcs3YG79q8VW0lKhCzyqcwlIM-3jGmMEmgr9w8QSMYsIG6yqKeIrZAAMDk-28h9-syCNFCfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز شنبه ۳ مرداد ماه
هموطنان گرامی می‌توانند اقلام مصرفی وارداتی را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
مراجعه به وب‌سایت رسمی سامانه تخصیص اقلام مصرفی خودرو به‌نشانی:
https://iranko.ir
.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/675075" target="_blank">📅 12:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974a8f67a5.mp4?token=bkT5GP5VEkF5b3zPETT_n225RLMczHd-8K-Wj0VexAunnU6IW6rNH0o5CpTE7q4qmLcEq7E33CMr0JJa_iKYTKaZe56GCwD9Dw7hWoaPrbT5a3p8iZG8rJQy59dGNu_V7Ksec504DBplIX7mxLbN374cETf_YNmtngR9T8Ue2Zvnn2oV2umGAEC5MrhHWsc8Mg0mYgBqd8LN-QUwMKG6eBvRCrnOYkEHBkwxPi7vm4L_1wvKzrV6aUseVfH-Nr1aoUPro4l2zUnpHEFCyZgazgPg5XnMO8Z0QuA5eO6vDJNEm8pIDr5T-QYiOuJemq_VUzyHxocQoLrKOFZEsVDxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974a8f67a5.mp4?token=bkT5GP5VEkF5b3zPETT_n225RLMczHd-8K-Wj0VexAunnU6IW6rNH0o5CpTE7q4qmLcEq7E33CMr0JJa_iKYTKaZe56GCwD9Dw7hWoaPrbT5a3p8iZG8rJQy59dGNu_V7Ksec504DBplIX7mxLbN374cETf_YNmtngR9T8Ue2Zvnn2oV2umGAEC5MrhHWsc8Mg0mYgBqd8LN-QUwMKG6eBvRCrnOYkEHBkwxPi7vm4L_1wvKzrV6aUseVfH-Nr1aoUPro4l2zUnpHEFCyZgazgPg5XnMO8Z0QuA5eO6vDJNEm8pIDr5T-QYiOuJemq_VUzyHxocQoLrKOFZEsVDxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب برخورد صاعقه با موشک چینی در حین پرتاب!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675073" target="_blank">📅 11:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvk7CEYBBWF1ul3LxD3CLeUiNGMKuu-3ZgB3LLpCFl_ZIa2SC_yL6p7O_SCi1fBEH9qgtg_YeHepMuXcK36GQuPsxTwW1Xk2fMgyDzaKBiIREfobLwaHnMjAzDjbO8AYvaOM2vuXoB_GgBY1d3O2FJ9Lk9TK-m-f1OVXGiSgmu2Hu-UJNFqZesYn-V-1dXT0HhadER52dDW7NNqoZkyOBRKaKZlKxQ-oOFP-A7TleFFsWZ2j3hFn-swHLkOwI4bl73trOhaUVc-pv_GCQeQ6zIdbYSkMRWjF0vbPKgcjU6fwLwLLbkvybKBdgxg45_GXt_xZcB-NXZ6ZoGErq18pCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون تعداد کشته‌شده‌های آمریکایی را کم کرد  ای‌بی‌سی نیوز:
🔹
پنتاگون تعداد کشته‌شدگان و مجروحان جنگی ایران را کاهش داد و این امر پرسش‌ها و خشم زیادی را برانگیخت. این پایگاه داده به عنوان سند عمومی و معتبر دولت از کشته‌شدگان جنگی عمل می‌کند.
🔹
مقامات وزارت…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/675072" target="_blank">📅 11:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نمایی از سیل و آب‌گرفتگی در آنکارا
🔹
بر اثر بارش شدید باران در آنکارا، خیابان‌های پایتخت ترکیه شاهد آب گرفتگی و سیل بود که باعث شد رفت و آمد خودروها با مشکل روبرو شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/675071" target="_blank">📅 11:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3f4438.mp4?token=GKDByJVZGes47_w00Csl-vxeZR4INeZtL2kNJYMWqbwmSYfpkObq3nSuFZrgqwHGrI9OfvpXxf09l6dZlE0aXMqF_qdWW4hJfAkH84SvhB38rw5Se-HSAcGwjMM_hu3F1issN6m7VgKeKDVRRDbcEqcaIVvGr_6sKlLzk0-nzTNcRIeVVtYa6UkCnSGQlTKN7A4kRxuPiiOo_FN9rAykPAh3TCksIkYZiMxaPtLMPyIO6jjE8kUBlur7PpN0kuDAWhS12J92n6j9NIQ6-qCIfgIpebP7wCOV8X4BalqVGeTCvee-rsY3JcUHHD8yDP67ExTlKeQtD6R8_5Mi1zIIWbGLC2CUP7y73w-m8lEwtBb4RgUN7LbrwNj0JVPJ7YGFKeoZavAYuHcbBwrUs_X6DmwWwZ32ieAEaO2eI4o3fTaHKcClhKIQRQxDaLXuNO1y7B8X2Gh7j_gS_lOvx2LCpQJUKbsyfFWznp5b3RgycOvzrFf1w1f7OPlLvy0N-dKK6NUG8UEmdGEYYXSsemyNxmhsu7ktIvpFhKNDMWDIoL6pKMeMt2rvvZxSKLTRwDv6mVaNOQuYZAMjINnW5tWPr3dJkiRwhg85188S0klt9CUe4pJLUyMzXK514eHMbRONe1RVczZbqB8v7fraCspcQpzHR4lQsilrtNLr8Hz8E6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3f4438.mp4?token=GKDByJVZGes47_w00Csl-vxeZR4INeZtL2kNJYMWqbwmSYfpkObq3nSuFZrgqwHGrI9OfvpXxf09l6dZlE0aXMqF_qdWW4hJfAkH84SvhB38rw5Se-HSAcGwjMM_hu3F1issN6m7VgKeKDVRRDbcEqcaIVvGr_6sKlLzk0-nzTNcRIeVVtYa6UkCnSGQlTKN7A4kRxuPiiOo_FN9rAykPAh3TCksIkYZiMxaPtLMPyIO6jjE8kUBlur7PpN0kuDAWhS12J92n6j9NIQ6-qCIfgIpebP7wCOV8X4BalqVGeTCvee-rsY3JcUHHD8yDP67ExTlKeQtD6R8_5Mi1zIIWbGLC2CUP7y73w-m8lEwtBb4RgUN7LbrwNj0JVPJ7YGFKeoZavAYuHcbBwrUs_X6DmwWwZ32ieAEaO2eI4o3fTaHKcClhKIQRQxDaLXuNO1y7B8X2Gh7j_gS_lOvx2LCpQJUKbsyfFWznp5b3RgycOvzrFf1w1f7OPlLvy0N-dKK6NUG8UEmdGEYYXSsemyNxmhsu7ktIvpFhKNDMWDIoL6pKMeMt2rvvZxSKLTRwDv6mVaNOQuYZAMjINnW5tWPr3dJkiRwhg85188S0klt9CUe4pJLUyMzXK514eHMbRONe1RVczZbqB8v7fraCspcQpzHR4lQsilrtNLr8Hz8E6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنسول‌های بازی از ۱۹۷۹ تا الان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675070" target="_blank">📅 11:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d163b2e8.mp4?token=BYfoCWiE2wZpWMCNvLANFY0mZoZT1Pun_wxK28q8VcmcAzrxu7HjFJknDl3DmUPCvNDvig1Wa_4p2F8nnM2yhyYhj2V8yaBm1ENwl6BSIodYusT7LoRgjCNmltuo54NVV_LxCnNTUTnyEoEqA9X9qPTAEBlsP8X081kehZyHb9BcUEJGTv1IDsCrnRZS0b1Nv3fefaSAdtvo4Kx-hjgctPxHlGyLhh3X4k_NnIpA2UpWgdo3SvnJcxVG3ibekfsvQCuzKyVI6NkkO23q8WieBEW-SAlci-881frz61EHFPlR9eBh-eb-0g8QnbZPYUgwJDFHln1HAmc3I7tm7tA3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d163b2e8.mp4?token=BYfoCWiE2wZpWMCNvLANFY0mZoZT1Pun_wxK28q8VcmcAzrxu7HjFJknDl3DmUPCvNDvig1Wa_4p2F8nnM2yhyYhj2V8yaBm1ENwl6BSIodYusT7LoRgjCNmltuo54NVV_LxCnNTUTnyEoEqA9X9qPTAEBlsP8X081kehZyHb9BcUEJGTv1IDsCrnRZS0b1Nv3fefaSAdtvo4Kx-hjgctPxHlGyLhh3X4k_NnIpA2UpWgdo3SvnJcxVG3ibekfsvQCuzKyVI6NkkO23q8WieBEW-SAlci-881frz61EHFPlR9eBh-eb-0g8QnbZPYUgwJDFHln1HAmc3I7tm7tA3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
استوری اینفانتینو برای تولد مهدی مهدوی‌کیا
🔹
«صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/675069" target="_blank">📅 11:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpgTdCNQsLwSYyYsrQoWPs9BClL-CP792dxJL-YiwoVh-IUaHnrZX4Twr6HLeA4W9gpvuHdnUg2nPbv5e50GUON6MIZl3Z5qJHVzDCietc6UQf_x3SRIoknYf9siTWmPkx5sc-YOoFO99HZMx1MvGtbuO9jl7o_bdWqfipzJUOXvlMynuGOac5fQ9AW46d3psIjwkJvcRlBnO25eyrxNPTuq2ocBRa7yo7wE_MFkkMYis1uJE5r5WsDhMgn1wLTjB-SZeY1w9o-2cBhFbICO3OYy9V2GdNA_XNy3td8FRwh2KhmxkRQFtWguHcPPI6tR_RxfgzRzVxPcwlBJD_8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره توافق احتمالی ۱۰ روزه ایران و آمریکا/ ماجرای سفر مرموز نخست‌وزیر عراق به تهران/ یا جنگ بزرگ می شود یا یک تفاهم غیرمنتظره
🔹
آنطور که از خلال گزارش ها می توان برداشت کرد، مهم ترین مفاد توافق ۱۰ روزه، توقف کامل حملات آمریکا به ایران و برداشتن محاصره دریایی از سوی واشنگتن و باز شدن تنگه هرمز از سوی ایران است. بازه زمانی اجرای توافق نیز ۱۰ روز است و دو طرف تلاش می کنند طی این ۱۰ روز مقدمات را برای گفتگوهای آتی و ایضا، تفاهم گسترده تر فراهم کنند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232847</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/675068" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YruttmoXYrE4HA7Pul8mhDb1AjvuqDCXJNzqi8gj9oj-LIXpMaPM_V9vNDf2rwGMKfbof-Esfbkfd2-L-C5k6zg74z3nakVJUgEKYXlcjBkzYBebFMEzJqeKnfBgIixVSyY0Yu2Wou6sIKf6SBFain0FCEsBTIrYw7qItDJB0bKkSoqaoT7kkp6R6vDCs9wW2wbni3JKvMOi2oGb-RhYuRaQkgaFCIv9kovaFJ1cgElDuMzTL3gZvrEGpPtyMl-ajXxGzV0lsOd29gvWRDfwUTBkvNzh_EJpjmr9mHxtQtQfbargNT2jw7ayaMVgO_J5Fsu4i6YwBi7qAtsobTdt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/675067" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6752602.mp4?token=ZazawTaJAVN6_ZDnFT4p1vp_e0-Gr1v2-03WYQjeLVxLX2U58-kC_gtsofnMxi5ar7iyZhxb-2g8AX8yzG0OPPqRs7h4g04go9RhnWoIH5OfplfQXtvhgxVwtZmqBxWRGD57tGR5JcDrbDDJ_1hsuXep-iimfcY7NxAecMMZcdaQhXERKEaNgKOoR6AGQz9yYt4mEFkbt9xV-uR4eivn1SWnwAOB8jMWD52YUHBRvjWFUq1R1LmpOpR8pYqu2xvdoYouJx5IvVBI_XTro5MdrDClSd1HB78A5vXr3pfPbIyckLVXMYFHjeOYpMZHk8guIP91raUvBFALmHnrFYFkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6752602.mp4?token=ZazawTaJAVN6_ZDnFT4p1vp_e0-Gr1v2-03WYQjeLVxLX2U58-kC_gtsofnMxi5ar7iyZhxb-2g8AX8yzG0OPPqRs7h4g04go9RhnWoIH5OfplfQXtvhgxVwtZmqBxWRGD57tGR5JcDrbDDJ_1hsuXep-iimfcY7NxAecMMZcdaQhXERKEaNgKOoR6AGQz9yYt4mEFkbt9xV-uR4eivn1SWnwAOB8jMWD52YUHBRvjWFUq1R1LmpOpR8pYqu2xvdoYouJx5IvVBI_XTro5MdrDClSd1HB78A5vXr3pfPbIyckLVXMYFHjeOYpMZHk8guIP91raUvBFALmHnrFYFkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی روسیه به زیرساخت‌های برق اوکراین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/675065" target="_blank">📅 11:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675064">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
یمن از فراری دادن جنگنده‌های سعودی خبر داد
وزارت دفاع یمن:
🔹
پدافند هوایی این کشور با شلیک به سمت جنگنده‌های عربستان سعودی آن‌ها را فراری داده و مانع از ورودشان به آسمان یمن شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/675064" target="_blank">📅 11:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675063">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13468f98c1.mp4?token=LMACPLa6C0Zi3N9WWrWXUsto9c8CJw4mf7IK78n9zoD59d-sJE60EJC_q4RCXLdIXsdgJye40xcLMVsRUhHtxBei-D6DexD7f0KwP2C6_FAnDxsQrsATvdogAVYpjrUVe8T5CryfMs20xoFtb4aXSA9U1M-XKbuoK8djBDc8wiOlohgv2ENBBqPNhM4kc4j1-qAc2sMxiIdS1SB5hCUBnmJKrIsWMPfbtzlaA4ICTiBEF_yck-1Yeru2bc5Z4nE8WNSpadc_egyD_ojsHT5OFMd0KfcPx8doWW4cLx706iU1xc156esu9gjedvpWBgOD4ipn3X8HRN9yTRXaBDPNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13468f98c1.mp4?token=LMACPLa6C0Zi3N9WWrWXUsto9c8CJw4mf7IK78n9zoD59d-sJE60EJC_q4RCXLdIXsdgJye40xcLMVsRUhHtxBei-D6DexD7f0KwP2C6_FAnDxsQrsATvdogAVYpjrUVe8T5CryfMs20xoFtb4aXSA9U1M-XKbuoK8djBDc8wiOlohgv2ENBBqPNhM4kc4j1-qAc2sMxiIdS1SB5hCUBnmJKrIsWMPfbtzlaA4ICTiBEF_yck-1Yeru2bc5Z4nE8WNSpadc_egyD_ojsHT5OFMd0KfcPx8doWW4cLx706iU1xc156esu9gjedvpWBgOD4ipn3X8HRN9yTRXaBDPNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعلیق پروازهای جده و ریاض در پی حملات موشکی یمن
🔹
ساعاتی پس از حملات موشکی و پهپادی نیروهای یمنی به جیزان، فرودگاه‌های بین‌المللی جده و ریاض تمام پروازهای داخلی و بین‌المللی خود را به حالت تعلیق درآوردند که منجر به سرگردانی گسترده مسافران شده است.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/675063" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675062">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بیش از یک میلیون و ۷۰۰ هزار زائر در سامانه سماح ثبت‌نام کرده‌اند.
🔹
فرماندار ری: احتمال شنیدن صدای انفجار در شهرستان ری تا ساعت ۱۶ امروز وجود دارد.
🔹
تنش آبی در ۵۸ شهر ایران؛ ۳۴ میلیون نفر در معرض کم‌آبی هستند.
🔹
بلومبرگ: عربستان در تلاش برای یافتن جایگزین باب‌المندب در پی تهدیدات یمن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/675062" target="_blank">📅 11:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675061">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9eb476257.mp4?token=aqB-LGwrKGvHrb9GELALOUt3QQoQ1CV8jQNJ768NY1mc7NF9TLTEnNNBonYmTfWmFZjijY7Bi-bM-E_dO4K5NeEJghKrR_QccY1G8DzR2-B9tpM771BxKVBOI1jAyQ8PnMioWYMYDnspAhlMLNrwOZymDd6PFoIep1l7A8HibKSrpzfzMnVLJ1CkkctDjJbDrtoaq2vlsA5KLbllwqcscx4diDo2uAi4ePRTVK_YkcPi8wdrt6TIyRlNl-I_u9Zo23ufkmMDOL__6-FkRyB1ZkzJ_Dco5B-6P4gbx_y9kNj5OJdH1owyeE5ScHE9_CxWvR3QQoPG2EOJ9CCAHXDnqimcIyd0jtg2fMLsoRFb1eKf_zy765UQQTlDHJFlmEYnHTR0PjGd6UrocG2wiEIwm1EBnp4YEhn58Vjpn_3MotAplJDbRrff0D0hh5rq8u2N_D4TCIQIVah95QKMnM2Ec9sH9Hpo70amIBQLfHoD-OJVjkjxHKYg2XMheB_uX0xKzU5mTzZ00Ti_KgdCBstSbNbeRcZxpJZWxsgwroWwM8GVcpjKlORCfRlMLkXrmZSjQYmiMkD95WCCVDT-OsGhg7J4YUV29OSeWhXirllNHh4gqbUarOHF0_CMAtqPELGU3atwApL2i_x04hUlA7gy9YpnW-AhvRaNxHTOHqhuawM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9eb476257.mp4?token=aqB-LGwrKGvHrb9GELALOUt3QQoQ1CV8jQNJ768NY1mc7NF9TLTEnNNBonYmTfWmFZjijY7Bi-bM-E_dO4K5NeEJghKrR_QccY1G8DzR2-B9tpM771BxKVBOI1jAyQ8PnMioWYMYDnspAhlMLNrwOZymDd6PFoIep1l7A8HibKSrpzfzMnVLJ1CkkctDjJbDrtoaq2vlsA5KLbllwqcscx4diDo2uAi4ePRTVK_YkcPi8wdrt6TIyRlNl-I_u9Zo23ufkmMDOL__6-FkRyB1ZkzJ_Dco5B-6P4gbx_y9kNj5OJdH1owyeE5ScHE9_CxWvR3QQoPG2EOJ9CCAHXDnqimcIyd0jtg2fMLsoRFb1eKf_zy765UQQTlDHJFlmEYnHTR0PjGd6UrocG2wiEIwm1EBnp4YEhn58Vjpn_3MotAplJDbRrff0D0hh5rq8u2N_D4TCIQIVah95QKMnM2Ec9sH9Hpo70amIBQLfHoD-OJVjkjxHKYg2XMheB_uX0xKzU5mTzZ00Ti_KgdCBstSbNbeRcZxpJZWxsgwroWwM8GVcpjKlORCfRlMLkXrmZSjQYmiMkD95WCCVDT-OsGhg7J4YUV29OSeWhXirllNHh4gqbUarOHF0_CMAtqPELGU3atwApL2i_x04hUlA7gy9YpnW-AhvRaNxHTOHqhuawM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت در جیزان عربستان بعد از حملات تلافی‌جویانه موشکی یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/675061" target="_blank">📅 11:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675060">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بغداد: جنگ ایران ۴۵ میلیارد دلار برای عراق هزینه داشته است
الحره:
🔹
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است.
🔹
پیش از جنگ،  عراق روزانه حدود ۳.۳ میلیون بشکه نفت خام صادر می‌کرد که حالا به کمتر از ۱۰ درصد سطح عادی خود کاهش یافته است.
🔹
نفت برای عراق سالانه حدود ۸۸ میلیارد دلار درآمد ایجاد می‌کرد./خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/675060" target="_blank">📅 10:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675059">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2mTBCIL2amIc5X02Yecj3N_-cZMte2fct-bUV83oBRt6aDERD8wCGkB-Ehxtb2d3tqlh7V27Z9GMdEvNM0b9j0QsxEK6T8J-KR8ZhLjtNgHDfzekPZtlrUxh9CEOqa9998yun_vYSulUL26M0uqNfI5S-C3dVyC9YjhoQ11lMVlY0We8smKIa70oxW9PNzhVUfxuS3zy2ukxTeQyoqbFjuU4c4jcZeeC2SyljPFGEZa6IUpgZoVSwkc8fkNVy61cpYhO5WLbyOHYeiNJ-gaDslZcK4nLe0ZDPdJ5kymUtJztgGZTPfejxxrqcq7WuXw3jVd5BCIR3kbe7AaKNhkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جامونده‌های اربعین، این فراخوان مخصوص شماست!
🚩
می‌خوای توی حال و هوای پیاده‌روی اربعین شریک باشی؟ با شرکت در پویش «زیارت به نیابت از رهبر شهید»، هم نایب‌الزیاره می‌شی و هم می‌تونی مسافر کربلا بشی!
🔸
۱۰۰۱ جایزه سفر به کربلای معلی
🔸
برای ثبت‌نام در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ ارسال کنید.
این فرصت رو از دست نده
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675059" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675058">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ffd72ba.mp4?token=ZfJCeqZ28ai2nk1AdlmodXYanG0B8nHmW8LwBPvJblu1Sn-mhULzHlx1OLvghlDi5TIpsswLZCophGDaZ3R6H2jZa8Ivvo8nov5bbXqCfVkPNA_mMq-ZE43cuob4Q7TIivfDmekH6Kq7ZFMvZZWCbwrwLN1K6c5bBnNL9t6CaLhbj6U1DeMRYAdq1-cWhH8uSyHgXGBxXmxt5fUKpcSng1JuZ5tD6p2f8mhozZW2SK_hvoGQPWGXfFJhVxzLDg_oSgVmOMU8MG1Bfi3IU_4bq1xOXmSprAuIQ4fER6ZPBAy1JZPYhTu6BPM6xh29fnGHyoFkEpS66Aw6Cr_HCO3d8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/675058" target="_blank">📅 10:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675057">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TivZAcFfc5u-gcSULSNUeEVe1dOAzXRLaCQUaVGZmSzRxtolmidFHY7AwB0egKRdpOv9obSiNFjyZvjnVXsc9RkrVSVAGU6XyQoAg0ELdgM068_SNRW7itVQj1VoEuqhztaSrll9l59-Y2MYrtdcJVZzsV-efrlTzV2dLryaP7sYySlPIi259aGHVj_MKI0erEQFy3VpTEtESCM1muP5-CJ7GcEy1xqXOedC5urrUTAZrCvIC-g-6Q3Y10DrFm4_whrKvy1yOuIm0qX8ac7ue1hcNhzU422fa144d95m-pTpGfl2Qq0KT1EMCnvv8kO1gtThVOzoxuWBp_xk4lsohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمان را خلع سلاح نکنیم!  مهتا قره‌داشی سردبیر خبرفوری:
🔹
دکترین رسمی دفاعی آمریکا می‌گوید «رسانه، بخشی از توان رزمی نیروهای مسلح است.» این را پنتاگون سال‌ها پیش در اسناد راهبردی خود ثبت کرده.
🔹
رسانه برای آنها فقط ویترین اخبار نیست؛ یک سامانه موشکی در «محیط…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675057" target="_blank">📅 10:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675056">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در اصفهان
استانداری اصفهان:
🔹
احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675056" target="_blank">📅 10:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675055">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d6e30712.mp4?token=lFn6e8IiuHEGnfMLUtDHo_Jk77VAkJwWzQ9IweX-IMy8YbyzO586r58eZHVIyqCW-wDtfuncD6-lB7A6LppOR_g_cBJTliKyOgRd1y-1AOXciykH4Q67akPASpnnHeSubzA7HqQA3N-lLmHged6DYHnueCB7Raz4jzi6W76dQ_BL3fBhviHcSSR3va7lUNOZ2PN1vW_RUgVWBHSVWFErUtZgMQjRE_RPDkY6J3yFogaFmTMeHeJ6JB0Mf5A1se_fNbWY_n4RO2CrTOXAtHnR8Zz_u4SCWPAHQ2D63lBT6VvsmHiF_vPJYzWA4xTX2uAnywol7bjc4Tt9Kq_J-OSK9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال شدن آبفشان چابهار در فصل مونسون
🔹
آبفشان چابهار با وزش بادهای موسمی اقیانوس هند و بالا آمدن سطح آب دریا، حدود سه ماه فعال می‌شود و از نیمه شهریور دیگر این جاذبه طبیعی قابل مشاهده نیست.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/675055" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675054">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74dddcfba.mp4?token=G8LK-Ny_aQXkuAaD1MDthGBAc3GfHLsyRsn-YFRdmp29dHww3kwDICukZwZFZqA6xZeIZTXnZeADMq8kpGRADhl3Ws8x0kmxGWMjduGwyBHhZVyTOPZCuk2SJkPrVdF6sKw3CWO_sWTPG9kBU3O8LsiPC3z76lCLekt7qvJa3qX3AhnbR0TLfzrov4dgxInZlnGBzntw5S4EQ9ZShkDHhxqpX1wc5T2_0pFsuWrknRfZud2GyiEJ34cYSLafE3GF5fCR8mPpQUfdLFFmy5nNGbPggDpXbyz5mLHe9hdocMCxXocEQ9ubG2xb_NXFKkHP4YB_6orGHKEZgXwEOcOqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالاد سیب زمینی خودش یک شام مقوی و خوشمزست
😋
🥗
مواد لازم:
🔹
کلم قرمز
🔹
کاهو پیچ
🔹
خیارشور
🔹
نخود سبز
🔹
سیب زمینی
🔹
سس مایونز
🔹
ذرت و جعفری
🔹
نمک و فلفل سیاه
🔹
پودر سیر و آویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/675054" target="_blank">📅 10:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675053">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiIjR0c-AabZ8ggrD1tKTbUeoKpPtBwuwchP_BImqEC_iBCyh2Aspe8wFQBBHRQui3uPHlZow-45NL-op4A4S2vroxXov_Qs6xf_PdvBBpaRsYtf_74muqK8rg-sntoxPT_wb0m3HbuOEyUk-Q-K4i8sQqcOsc6124xu2Tg47d6TFmM193eILRMf1p5Gzfeplj4zZv-jN1KeeEqRnBjmthhgDN3USD62mg5yif0AmgFcSKjTMqLYdjhkvx5hHyAYOaPmWJBEl7zXbeMaH9udhW4bnMw4pY62x_bvIiKBopgN7gUAI5DOjyJJweaxPzwKfLcLoBUpxYWaqYbGutwqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پنتاگون تعداد کشته‌شده‌های آمریکایی را کم کرد
ای‌بی‌سی نیوز:
🔹
پنتاگون تعداد کشته‌شدگان و مجروحان جنگی ایران را کاهش داد و این امر پرسش‌ها و خشم زیادی را برانگیخت. این پایگاه داده به عنوان سند عمومی و معتبر دولت از کشته‌شدگان جنگی عمل می‌کند.
🔹
مقامات وزارت دفاع این اختلافات را به یک اشتباه فنی نسبت می‌دهند. قانون‌گذاران می‌گویند دولت در حال مبهم کردن تعداد تلفات است و سعی دارد با تغییر نام جنگ، محدودیت ۶۰ روزه اقدام نظامی بدون مجوز کنگره را دور بزند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675053" target="_blank">📅 10:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675052">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تا ساعتی دیگر بیانیه مهم نیروهای مسلح یمن منتشر می‌شود
نیروهای مسلح یمن:
🔹
ساعت سه بعدازظهر به وقت محلی (۱۵:۳٠ به وقت تهران) بیانیه مهمی درباره انجام یک عملیات «مهم و گسترده» صادر خواهدکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/675052" target="_blank">📅 10:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
پایان دوران مسی در آرژانتین
🔹
لیاندرو پاردس هم‌بازی لیونل مسی در مصاحبه اخیر خود در واکنش به خداحافظی مسی از تیم ملی آرژانتین: فکر می‌کنم مسی تصمیمش را گرفته که فینال جام جهانی، آخرین بازی‌اش او با تیم ملی باشد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675051" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEgzrOf8QfC2QZ7NzoSIMSHzUHUFhppaA9mPdF4OIVAqwJjahb8NPPCDEJvIAQ3y_pf9NAEzh5Imv1_f-AHRVWt8uoLSaYah-Le5yFX_BvkVMHDqJlNLzrHVTqdfbisRbJd2YQwyvyoBWO0h4rvzpjiw_I8bB552tpx2ohMxqdUOfPuOV-lqtWysDKjzkac0wPEKpzISiDx7Asp8vHviFhmPIpfd6qzfDcPjRl6U5zqkD6JE9eAKqu1D-blEkUPbdg6t5l0IJczD6EwCLfiWDrVLRaRbVe_wShJjjAbwJuO9QmdWLv8_zs55KCSRMfO2Jsp25AZ1L-r8iilbY5_etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/675050" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxSUh0LzkBpVkvnyF9VaFiHmOf3J5oqemoDyf_mDehILOIgKbak9rCEsB6zK-sOaMjveBF1Ot4VKqHv59QArfZ2rAk086nh6m9bYxAC9lKOUUX8vcJK1Fp9WoIdlDXiepFIomGviMoM9pVvPWxn0Y0T9GGH_2GASrSJeI3OMhozKNrx9jXWb8GxKp1V9m_lDrEz7trXiGd99_9b2AlJSOSqmSnKcv0P9sw5sYY3t3XD4Qtgh-KLGPqt1y2CpTItN6o9pYHnrL7l6YumdjGYzjKQQk8s23gCauLbKaK_i5o7NT1HMe5krjfLmv19r_ec5NPc1hRmE75b-K4s4Dh91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلمان از جنگ با ایران عقب کشید؛ کشتی‌ها برگشتند
رسانه نظامی Defense News:
🔹
با توجه به اینکه پایانی برای جنگ ایران متصور نیست، آلمان دو فروند از کشتی‌های نیروی دریایی خود را که برای مأموریت هرمز در نظر گرفته شده بودند، از این مأموریت خارج کرد.
🔹
مین‌یاب «فولدا» و کشتی پشتیبانی «موزل» راهی شرق مدیترانه شده‌اند و تا مشخص شدن اینکه آیا اساساً مأموریتی در کار خواهد بود یا نه، در همان منطقه باقی می‌مانند.
🔹
وزارت دفاع آلمان صراحتاً گفت: «با شروع دوباره درگیری‌ها بین ایران و آمریکا، دیگر شرایط برای مأموریت فراهم نیست.» /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/675049" target="_blank">📅 10:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3R5LsQR8yPy2eqjtpFpENLOW43HDGqfhOER4jfk_NDEbo8-xAen-R_dbwfENQzXMlUE6jvElkydIPyAxrF-1idTSnFafENYuCbwQOBJfOlzIcZg-yPAgWL6-MhV5wFcBCKa86QQKqUmemm70yV76jcHt-2TDowypoY_LSw8UPUzL4RmENZt0LSgse5R1Team83vKSzdllbnZ6emla2rnDaQKVVFHUyowkwsiMDtiRGYPrRqqGDfgZRI-Y3QscGg6_YtuiuXl2Gi4POIL90KnoCycCVlFNKz58EyKtKLSWA4kz5O8MpkjAiZlQ4i6ny8EkkZMu_uJicu_4NjDZX3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
UPGRADE YOUR STYLE!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/675048" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تعلیق پروازهای جده و ریاض در پی حملات موشکی یمن
🔹
ساعاتی پس از حملات موشکی و پهپادی نیروهای یمنی به جیزان، فرودگاه‌های بین‌المللی جده و ریاض تمام پروازهای داخلی و بین‌المللی خود را به حالت تعلیق درآوردند که منجر به سرگردانی گسترده مسافران شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/675047" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm4DDfNd3CuSu2SYtX9T4hYwLppDIrH3nvCzYEheksAKrc921cJJb8Sl_WGnSaxyjqWYeUNa7LO0jZXXsxsVUqDe0K3PZ9YhBrkvjyi9r5WjlT0yGPDHpDQ1kuuYMsC_U33qyEl3Zor1uG9cBHnkxPmRxtzJLRgdHueCM4itZbz25k45n6KAnBvDtecISNYyDP_tQlCmbfbGFChO-8hiwMBW9kqzAu8NSLZDx1fkQtarojHE9qdt_ttIuMEznT2jxwBefT37NIC1rFgHPauE7qRpgXRN_TBgQ3XbK1l5lTGqFcZtipkGxE00lydRGOyZB3KVBTaB5voGNT0GNadVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری اینفانتینو برای تولد مهدی مهدوی‌کیا
🔹
«صمیمانه‌ترین تبریک تولد را به یکی از بزرگان فوتبال آسیا و جهان، مهدی مهدوی‌کیا، تقدیم می‌کنم. دوران درخشان بازی تو در سطح باشگاهی و ملی، به‌ویژه نمایش فراموش‌نشدنی‌ات در جام جهانی ۱۹۹۸، هرگز از یادها نخواهد رفت.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/675046" target="_blank">📅 09:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675044">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نیویورک‌تایمز: نیروهای وابسته به ایران می‌خواستند در ترکیه هواپیمای ترامپ را بزنند
ادعای نیویورک‌تایمز:
🔹
ترامپ با جت اهدایی قطر، بدون سیستم دفاعی پیشرفته، به آنکارا پرواز کرد و با ایر فورس وان قدیمی به خانه برگشت. سرویس مخفی امریکا پس از دریافت اطلاعاتی مبنی بر طرح شلیک موشک به هواپیمای رئیس‌جمهور، تصمیم به تعویض هواپیما گرفت.
🔹
به گفته منابع ناشناس پس از آنکه مقامات آمریکایی این تهدید را شناسایی کردند، سرویس مخفی به ترامپ توصیه کرد که قبل از ترک کشور هواپیما را عوض کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675044" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675043">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/675043" target="_blank">📅 09:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c3f4524d.mp4?token=igPVUkQAF9F-jYY-XV8NsdSnhvYXjIWH1myyHB4qGbFLYrpUqE7PzbPHW1FKljfWkD7lUJusGN_njBw8tcuI1lqOiWSM6qXT_EWRkZlv4uQ6rFd2qlyex0k7MV5mQVn7Nowl17O8r5LxoII1H_BfQV4skkr8K-zcCb_eTat0qoYI4x082yBF0exKYlazfH_JR86LJDPJ_VnXZbBEtpNg7T60Zxzvy4Q3t7oB_g_LApWhEBvOE0b4SRz5sKnEayaql5jgNTMAMFCetTWLEN1BGNc9pqQF7mcsdM8Ia_wQVmVkdsgeKHMLw3wogBb7CmBPjB_TwXGiqb7MfmTrAX0Wvz2U_UeIqLzExUzn8vivIiVVfsiGJOAxqoVd3sn7wlI2lyk-eNPWowx1mu0XfcawCM1NTlYi0E-GCYE2xmWUftK1AjYW02OGKdLgtAUnOBW8gev9f9jC9oxIzDd5mKlSiXuJo6cwv0Ho0SUWMlA34nhfeKgzE1EpLu7whIyDW0NWIxwVQwpa02t_P7G2-jckVy64YqIwWhZnYjhyZQAtldLqGbuBIVUUP0REbBTfWszyDDSXfjtWMp0Yxq5UA4YNMnkbx1RYZD4E6HPnk8KmKJUzC8V6NIinaGV1KW-8_ikreru2VeOHTXghj0pTLHDxH1zm1IxFQn6ESWMjmfOqOco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675041" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف ۱۳ شب حمله پیاپی سنتکام به ایران
شبکه سی‌ان‌ان:
🔹
پس از ۱۳ شب حملات متوالی آمریکا علیه ایران، فرماندهی مرکزی ایالات متحده (سنتکام) روز جمعه هیچ اطلاعیه‌ای مبنی بر انجام حمله جدید منتشر نکرده است.
🔹
هنوز مشخص نیست این موضوع به معنای توقف عملیات نظامی است یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/675040" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675038">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNgIuvnJpHi-ovH_6B1peko3NP3VhWZSIodZy2sEwEyuYutwIu71kSM8rqMJ1OhlCTQVan4fEgeIXIJYXfIR1Ete4X9yW7FhyqjBJPUdqVKwM77JatWaug-CTGHOgO6FJGx2FsqNGKCSIZg71PR1UDKb-XDbyi1OYbSKkiGDVXmU-XL-b1NhWTPOzlwwBbOQs3DcE8eNqtsAAIu_qiLJ6bW5HcBxPxTxam8zWRtYH0izRRh4YmhK8Cp1uNhUKGJ64xvIn1m8tdXEYkO_yfRV3edCM8zcBhx3EzYj_WnffWOStPJTwOewAbJHFrzY_kJTN_8It0v5jePfnf7nU3_Bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ نشانه پیش‌دیابت که باید مراقب باشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675038" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8878ba219a.mp4?token=paXoxQZVCzKncdZ7C8nKveetkPFkObt7h49uUnSFckS-SBigjcYeCWbFMhvrhrE-K2zfe-aiwddmhw-hlHoAOhrWvTPx5HX-5kFXpcD9pVUNghPiK_OjEM5ovZ28Pobqjyp5bbuGwcyxeVAsrNNe2ekWf_OILaEUMRYigB4CKcfpsZBJljWVdc7LOgYsnALEUYMuSYc_lnUP6SXg28mseROv8tKWCHS3KLKn8tKOmYIu0TFzl30KTpJzCCywhvVM_-bf6cu-Q_M_3mfs_b05PZo_72TOPrpKpAVJBdm8oxQ891vG75J3rbwgC1JJ4tjre0xQ8Dpoqbp5ouDv2AF9AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8878ba219a.mp4?token=paXoxQZVCzKncdZ7C8nKveetkPFkObt7h49uUnSFckS-SBigjcYeCWbFMhvrhrE-K2zfe-aiwddmhw-hlHoAOhrWvTPx5HX-5kFXpcD9pVUNghPiK_OjEM5ovZ28Pobqjyp5bbuGwcyxeVAsrNNe2ekWf_OILaEUMRYigB4CKcfpsZBJljWVdc7LOgYsnALEUYMuSYc_lnUP6SXg28mseROv8tKWCHS3KLKn8tKOmYIu0TFzl30KTpJzCCywhvVM_-bf6cu-Q_M_3mfs_b05PZo_72TOPrpKpAVJBdm8oxQ891vG75J3rbwgC1JJ4tjre0xQ8Dpoqbp5ouDv2AF9AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنوب؛ قصه‌ای كه موج‌ها هر روز از نو روايتش مى‌كنند...
#همه_باهم_برای_ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675036" target="_blank">📅 09:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS16oApbpQ-6r6J0YMQr87-_o-UNigVMZS-xpL9sM6NHEEIAdbUrMR-CrpH50qgLDflsyGWbUHuY4Jsipvfos0wfL531-LDE_8Mz7oJAFSEPuoZ5xR_M0ehep5Y-93zvpQ4a4esd9uwB2SBdIgEsnfj1nNgsNqY2Y9TwG1kjVToFnyn04NCuBqAFHPCrOWJxuGprwO-LmiR1RWClKjBC1lP14hCMM8KbqatRNSigIb08BAQ8_m-2L6lGPZ2RK6lb8nrpKu38SYjyArDczrej6BD50WvTXEzixCpNZbwpnMeM7_Rm6oEqq18Jf-zaSI9X61FxrME2mi6ULJtdKjl8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ازدحام در پمپ‌بنزین‌های عربستان در پی حملات موشکی یمن
🔹
پس از حملات موشکی و پهپادی یمن به تأسیسات نفتی عربستان، صف‌های طولانی خودروها در پمپ‌بنزین‌های شهرهایی چون ریاض و جده تشکیل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675035" target="_blank">📅 09:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3920d4655.mp4?token=jcegKoSmeD2TYN5qnkWHWyEDQhqkKuS9l5USqU1gVHIUK1uazpIk3BzAVWLIrK9CZPl6ZdzCoLFyDryLaMQIa3C_N_2MozpKxRo-j5ZDZC6OXaacx1TCYRJTKYW9HZHhaTDSRaAl7M2BcG3ZR-4i4TBqpCNgGe7iblHhfns4DPukiUZA83xwHSyI5_Hpkd9ZfHgvZXIas1hIjLIdx8wnNtTuX_9MkBdT19edRftVJwnuTDLLhT7TtuZSwXR6tzKtxijf7HZJBfkzCaD5Jyyva1xYHGATzRWtVcYvwgy-Pmjzm3NIJ1J5KRxcVvqpcOMtLEKji8_c7DtXOtOdugvRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3920d4655.mp4?token=jcegKoSmeD2TYN5qnkWHWyEDQhqkKuS9l5USqU1gVHIUK1uazpIk3BzAVWLIrK9CZPl6ZdzCoLFyDryLaMQIa3C_N_2MozpKxRo-j5ZDZC6OXaacx1TCYRJTKYW9HZHhaTDSRaAl7M2BcG3ZR-4i4TBqpCNgGe7iblHhfns4DPukiUZA83xwHSyI5_Hpkd9ZfHgvZXIas1hIjLIdx8wnNtTuX_9MkBdT19edRftVJwnuTDLLhT7TtuZSwXR6tzKtxijf7HZJBfkzCaD5Jyyva1xYHGATzRWtVcYvwgy-Pmjzm3NIJ1J5KRxcVvqpcOMtLEKji8_c7DtXOtOdugvRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع قوز کمر با کش پیلاتس #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/675029" target="_blank">📅 08:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiSN454sJfpq4k5yOJjBIETc0K3I4ZPw38JIBfnNI3k3DVR8-msn54vq1Zwc4dQjXNI5MBpD9QI9pD7Jsmh93TxR2thzzUFejL0qUtYYxk7E0LHJsos6H7cdo9UhxxhP9plEp7j0ZBLbtDeqv4uhR0ihUB1zT8lchC_GVxgeXkO8MVuP7PmVP-hPb3pPNzufRmIeOXhhUyU_oV7gzFmcXrJtBvG4x6oNECuIFmxu__ymLwgqshYADbLuh_1_5csT2ErgTl1BluSY3pvZ1ovy1753FFa_rex7f8GhN9ToTyWi1IYsdGQhgIGELES6NEcnE9Sbm1GcV4nWP1aoniM7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4OVip7mXFtBCp33165YgpzqEqfEVDet6bPE2gbBR2tIpb3-niAR8MHMNZqaXy1Jyvtr5Xau8rm_lLfv2jbLHtVAaKFJUEswojpv0hxuWR3VCAnhjtZyL3HG3J7ZcAIlII2ggam0hbqWARJW2S2fgV4W11wLvH-HExXVQA0FxbcFDI8XhDNAqzzZ0gCn6AU7K1Kb_InF3q6IiPKbB7Qp0dvOMOYWK8QwPWpddM1BAD2efPaIataHud1uLeoy17yHI5OO_6cO-Dx-lRVCrTTOHv_qyTc5KBauD_08CAjA4ybbVeqzjs7lK0dF3q-iD0cIN4Nv1uwc6Tr6h57QUKyk3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شادی خیابانی پس از بازی ایران و استرالیا و صعود ایران به جام جهانی فوتبال، آذر۱۳۷۶
🔹
آرشیو آژانس عکس ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/675027" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99a19aa4.mp4?token=UcWFHORsugRNeT9-xYopQ6oU8lu_9GpJ_JEuPsVc7hZ0rdH9Xn8Ii_5LkP5dp4Hv4Klcd0T3Zlq6FusoKjFJt7d5POqNqO2Tkx7uWNPoD_9-LeF6aHes5H0tskuP6GvuiHUTgMlZOrXg32idPL1pAc0Cs4nH_qbGxcbKckgOqB9xBn-D70ZQxyUy-pIg76i-z3TnwUTL3z-F2WBEotGnRBdj-FFL7wV3gsM35DHKhXGrn5LkyKGgKEs1KFEzhfRMB22gaKwpmD5NI_qQlDHOqXB3s_BW1SiWWZr8CflWNQgF8bbHDtw0p3MHtOkBV1m0tPT7hOV1KPUgG9cOicua5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99a19aa4.mp4?token=UcWFHORsugRNeT9-xYopQ6oU8lu_9GpJ_JEuPsVc7hZ0rdH9Xn8Ii_5LkP5dp4Hv4Klcd0T3Zlq6FusoKjFJt7d5POqNqO2Tkx7uWNPoD_9-LeF6aHes5H0tskuP6GvuiHUTgMlZOrXg32idPL1pAc0Cs4nH_qbGxcbKckgOqB9xBn-D70ZQxyUy-pIg76i-z3TnwUTL3z-F2WBEotGnRBdj-FFL7wV3gsM35DHKhXGrn5LkyKGgKEs1KFEzhfRMB22gaKwpmD5NI_qQlDHOqXB3s_BW1SiWWZr8CflWNQgF8bbHDtw0p3MHtOkBV1m0tPT7hOV1KPUgG9cOicua5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت در جیزان عربستان بعد از حملات تلافی‌جویانه موشکی یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/675024" target="_blank">📅 07:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzHD9woSXItmPTzIeSIp_CYPD657v02wDPl870f9aoRevcjfgVLwN_4v-SEchfPdqK70ozZXa2yFBoL02XPuZVWZS7zkZF1_4gBJR8BLg1rNWj4TiIVd6SSU-eAFSMRtf5vSThuowixvE5Sd5xMCOLaNg8oR6SIukTtPyhOSZaruaAx08FH4vKRy8BqeepQFcqGkBDdHay9RhDFCt9mhJ_Vhwz-Y6jtO_QJu4K7QQ2FPw0GNDzwJlQGekq22KIXf1YIaSjky2kQbqZ8WK07MmbpvnFmjg6dyreCaNEKisb-DMIAXG5brDmtf0VMkUfgFx6Bvs3Rj0ERxFq9FFByZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر اکبر عبدی ساعت ۹:۳۰ صبح روز یکشنبه، چهارم مرداد از مقابل تالار وحدت تشییع و در قطعه هنرمندان به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/675021" target="_blank">📅 07:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675018">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98391a474c.mp4?token=oOvR5zXYslDfiw4hGIhZNt9160hzsK9CbHg4xQ9E9xGs_bQJEyd2xMMTlEj2Kn1pNJvfW99n65XJ12IKlgF8HUrJR5oAw4HuVHxGmrBcnQDNv2vWPBARwlnyho2RUef_DUsD7yI0omH_ALq__6jeKJFB1bioNI4R7Of_RNJtxUGPp9FczVap8myICGSzNsV0XduChxD7laO1Ov0YJkAdLLwGeQPBQTrMW7RptacHfeCAYI2849B5J2IpEOkjj73CiHqXwlumw6jde8tggBouzwUwpmeVw6eWEIojNwMGfl_021tHeYVTC60m0f6VZOjxbzc3sI9PaQhjX0ekVKTwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98391a474c.mp4?token=oOvR5zXYslDfiw4hGIhZNt9160hzsK9CbHg4xQ9E9xGs_bQJEyd2xMMTlEj2Kn1pNJvfW99n65XJ12IKlgF8HUrJR5oAw4HuVHxGmrBcnQDNv2vWPBARwlnyho2RUef_DUsD7yI0omH_ALq__6jeKJFB1bioNI4R7Of_RNJtxUGPp9FczVap8myICGSzNsV0XduChxD7laO1Ov0YJkAdLLwGeQPBQTrMW7RptacHfeCAYI2849B5J2IpEOkjj73CiHqXwlumw6jde8tggBouzwUwpmeVw6eWEIojNwMGfl_021tHeYVTC60m0f6VZOjxbzc3sI9PaQhjX0ekVKTwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بلند شدن ستون‌های آتش از تأسیسات حیاتی در جیزان عربستان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/675018" target="_blank">📅 07:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5zV4wBvf0rXqi2yiKz8FGocU1lOylQjVTc4Ba-6pYGDa-O3PLHH5Myg0glMImaR27dxexCl50iveXqz6qPIbUz9yDvU8U-WVnCJ7L5Tw_QdXrlBDm4YOjfRpjdwneDKAUgltxui8tzOTsIzXILcdymJnMu66k-8njADf2GsDSbL7j1860SzEqOee3BaAY12uspDrx5lrTxmP847EHs1z5o8cYs8Js4qIj9-ZzIN8xqO5Ju7xDlipoS6208aKCdGYYWSXaNoKMLVBUqjFk4edXYgSyd-g_b48kvLJH6rrb4tTooaoeBu7p-W7kzzZEe89ZXxO1yzYxa40HZFMv_jQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۳ مرداد ماه
۱۰ صفر ‌۱۴۴۸
۲۵ جولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/675016" target="_blank">📅 07:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299ed3562c.mp4?token=Ssn4j4atDPWKhHSA2xO3eP_h4Ztap1esmQkFTJTdWuFNx4OHvR93bIfnzYWMo-VCG-E7_9eqB6rwPIEEWCnyA1PhvCRaqq1geHkJ2e--wRsS2KGiIb9moJVjo0tXdF2_KLSXHsDqrox7pE_AoYfccfcZxVhqrMkam1vzDx4VqEtXU-uEsJOb206OUliLnhu20ZiKUQ7ncOjlU6cIePNRmIop7Adl6y75kXmu-j_YyyDMXtwq9SbVm4HEe_p0yLkafKz1W_OhaLycMOgi3L0qEd-5u7nvilAbg1bnouWQBm5XeDUVcGA3gUhGohWNGtsaSqFbHZrKt05TWddaeMFHAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299ed3562c.mp4?token=Ssn4j4atDPWKhHSA2xO3eP_h4Ztap1esmQkFTJTdWuFNx4OHvR93bIfnzYWMo-VCG-E7_9eqB6rwPIEEWCnyA1PhvCRaqq1geHkJ2e--wRsS2KGiIb9moJVjo0tXdF2_KLSXHsDqrox7pE_AoYfccfcZxVhqrMkam1vzDx4VqEtXU-uEsJOb206OUliLnhu20ZiKUQ7ncOjlU6cIePNRmIop7Adl6y75kXmu-j_YyyDMXtwq9SbVm4HEe_p0yLkafKz1W_OhaLycMOgi3L0qEd-5u7nvilAbg1bnouWQBm5XeDUVcGA3gUhGohWNGtsaSqFbHZrKt05TWddaeMFHAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بلند شدن ستون‌های آتش از تأسیسات حیاتی در جیزان عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/675015" target="_blank">📅 07:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع عربی: یمن یک تأسیسات نفتی متعلق به شرکت آرامکو را در منطقه صنعتی جیزان هدف قرار داده است
./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/675014" target="_blank">📅 07:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/akhbarefori/675008" target="_blank">📅 03:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ از جنگ با ایران کلافه و خشمگین است
وال‌استریت ژورنال:
🔹
دونالد ترامپ با ورود جنگ ایران به پنجمین ماه خود، از طولانی شدن نبردی فرسایشی که می‌پنداشت ظرف چند هفته پایان می‌یابد، کلافه و خشمگین شده است.
🔹
ترامپ که پنج ماه پیش با اطمینان از «پیروزی سریع» سخن می‌گفت، اکنون در باتلاقی گرفتار شده که نه راه خروج روشنی دارد و نه افقی برای پایان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/akhbarefori/675007" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675003">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15c04c185.mp4?token=YI0hwVeTCHI4uX_4OM5zkNSxwUvySUgI5rB7KHfQle7ML7evPEI6lwamWbmeSfCqvecn2pBCHLBmktOikIeIzcgtblCYfQM5q0dAhlZiv1Vo625X4kbbEztvMQHhbmGX8ehvDTWtorIrLW3LGIIIIMGrjNuYqQ45oEPvWUS9OF_Muzd3UAdd7eO6y4WpRpQJ6JRQ0cOSv8HMPUJmNTH68e5oH7ZBntROhvWIbIWbCg795ZwBxrTSaLCutYBhoRF7xCTcwYx016fJtLn4FtYCljssYms3OpyjnLZH7JA9v1Fq3qxQ8KZxilrLvvst6PglOtj4WrIEWl5UblZ5790z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودزنی پاتریوت آمریکایی در بحرین
🔹
رسانه‌های عربی: اختلال در سامانۀ پاتریوت آمریکا در بحرین موجب اصابت موشک پدافندی به نقطۀ پرتاب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/akhbarefori/675003" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ROAezXp5m2G8qAuZVi_Gsw5YjMgeYDcTKdgdqHEGjSOvVa1VfONFe2seW7WS7cn9gv-e4korA9sNjXYa_nofuJweFbCShZ2u2iSNfE44at6lVn-iuYQQCA4kw1hGJjwky56FCBcNs_Wahp1MObcBCRDkoYgxtjRXQfVV0VwRfKCAnNtZCzU0eULLG9takpyB8bHuyRIXkQ5M4n3i5jnBaCBzI3fewMtbN0Nq6tyEaj68ceqGv44cCZAlO9dAz07fVTX_Al6LKZTwNNfPFLfpaKhTNL56Zwu0flie_alY1PDeQ6mo_RMw_bgpHV0dmJPjpB-Lo9hq59rTpvYNinVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اثر جدید کمال شرف، کاریکاتوریست یمنی در کنایه به عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/674999" target="_blank">📅 01:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD5IUOOClO4OsRI-AdVwOHjrXKaD0GbncaFA8BJiT6ZfgCLTklIw1DAX8bF5nNHEckLKO_3rNIE20eKa-lRhjII5zGFc5yMSCVykLb1qsJ1MLw1lQggYqb80hyTA0SdeoL_mQtE8zFTNrbJcGxdlxb418oHFIrODQKlvVPnLAe4iilu99QiKRmir8V_wBDNQAUlDftBOINIYmTa7zAq6LxSNzwbSEcIMJpOF0_cKvj99lZsJmSU6qQLwcXBsOtgUJeqrl8UPvqHDYlyfQPoceo5lQJ6ePR2jbKSbvRuX6AY-5nvD-2XMlbLw_P2qdJjybq9mQeCBKMdIFjKKrCLxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلند شدن دود از مقر ناوگان پنجم آمریکا در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/674996" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عملیات شکارِ شیطان خونخوار و نتانیاهو کودک‌کش
🔹
انیمهٔ جدید از عملیات انتقام علیه وزیر جنگ آمریکا، نتانیاهو و ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/674995" target="_blank">📅 01:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e200a8d21.mp4?token=q_igR1YDCP2y6KyUD5WKYL6LA8iGoSQR9Wpmh9LioXveNl_0UzYt3QlzzK1j_dn44uoMT3PumZPMOgyvVDBZHRMKbyqa34r13z_KzwcStkC-eiGiY84C4DLsprQR7D3yq7Z0W1KXYtWJ0HjHthkyoBQMUJa8C1TP285Ko2RjIu4cNeBjwUF7w2ff1NvjSNY7FqU2zieO_Jfk9ApmckpvmnmZuyOfIfaRKQyq6NRXycF9LPRgy6FfeSPP3pZvmFaH9nwIV6JZAYraDR7wmGFsgFXRljVLsEk39s7yGfqwEli_S5KEyfz2e1dslAEe0xqFqG2XzV6Rho1mfe0cAa-OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامانه پدافند هوایی بحرین در رهگیری موشک‌ها و پهپادهای ایرانی ناکام ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/674993" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7eda22c1.mp4?token=qrYrcf61BS44nyJcTMKjA6yfQ6dGF1GoKFKHWE1XHSsZ7A4JS7F83bG_tPBPOYXfgAO5mohF9T-Ti8byo552uVrDjw5NnBc92ZauOGonJrZw8FlLgxEilfTkWjch9zz0xTYRBH56d0lU_k8pAunJnGElVmCtqj-0HaFxsUOkUE_DnwK9D05Leom8l_0kL1ccujngALiRznmpuBj4QC366wAMPJXxiPzJPKIBhQrqIevKDLZL9SzCdpe8JsIatToXow6arGtqCY3Y4lryJFfHmiXBsrqtSJ6qR87vXtUWnrI4LvzqD10GgtO1xb88Q69i6wVr-01v0unm5ONXXZayWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه انصارالله یمن خطاب به دشمن سعودی ویدیویی به نمایش گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/674992" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t03o8JrbEhQ3uryOFlmlI_RQLWI0rD-6PePEplDtIGo3NybLoQs8vQr5-FLVdmgbqNuRkZqKQvEEhyrJgOT4EWT8nlJgmnyppG8mSJWRlPgh3gwQCDwEtoMhPzP5n0IETJNNSbKMV8gweKTDXTFrV8LmItDGcuzzgl8Aoj375wisyQpXt5g36UtKYkH9yN1ePf8BVdFRa9JozYUb6Rpf2JIBRzwQOG7c3xmx3KvW5sm137d89f2JHEW3eJ5t8KlGv5KW8Um_6Cy4W4AZdO-lVMoefexBSEcqg6xN5tV63NNxXL9Bjnj9xGHa8z-Rfrl2EdvsneqXtVFe2HCJVQHlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXDrn1CttrsfpldFpcGAZbEaljulnwm6S5AoovXrcIedH2uAcdbIvYYfQSo3HZgmyfCubaDcBGdltYDJqjVrULzy_zynZ1_6MEWta1xfIC4AfhY8FPG4EeN5NBPJuOKsul3gTtYUKwz6DbxOvhda98SvIqnrqbOnJz6YWB1lc26e_qc81I_hEcQ5S1qNqsy27j-Hfx_tU1lfTy8KxYX4qVm9ZcUL6ELof5B9fs4d_sOjleR_t3Ey1AcNgaZB-VqayEHQSayBnFI1VUOHdzjrOFqowTF-pePVEOBgVoBHgGMc_Rjyv33sev2Dke-e_yGI1YSCY9muK2MeGBXuKCRcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjxU9o_DddLDiuIk5E8fgjBiUWcxkkjF6IOFLFdcAiVEdPNTl1FCiZ4hTeLgUrE7fvCGhB9l20eofdmRPGJBf_3V1u_cY6w1OjaSEoIiK4yg3SU3IKZBQB14gZBUJoWHSiZWqY11qic0UMs1trjqeny5HaCPFzQe493FWWo8I0pJm974WDPLW4vtsZ4m5mqP6bjvwHKknsQCBwc7SkmVTvGwt9_InVdGH-yNAMsATy-WWnlvHfOJhpmK4ful_bxstvvw3bllHriZn5SfDKe0qNx4Uc1WlVTwoDy3pXHnQ3AifOZAR5Pf9kUjqiKUHJ2sukQEwl1DJrULsQbcHw9WFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTw2Bm7-8d1fFVuVzzdHeq4OWrtx5rnmE4UUwjweBelS3Hl3f8sufMZ7jP8WmwIzLbKLqSjVrDwGLUpRjdsgg1ixNv-YElIDbPc8JOpgNhCvBgUvbWdAohSZF5d8Lip1NPCpSg9cSeS-W-L4HW8hAkrfGrBZrquYUYD8hDkTvoHHx2TlXpEqX9BjUyk7hSJWtaiSqeXzM2EJMsYW0w3ilxBE3-VjVm9YhTvgtmnLjJAxZb-uRlv3-dnufpg8257YEw5DawFdGkJPfD5Rii-okwElPsxXNTZDVYCQpso9EeNmupALx1AWvQrgUAgGxX9K4sS4Rc3onYXo365bSb4mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEEx56NYmDGxHvxdmy1ru9JJXtieY7QQD5n-rDBFe_-kZNqy8rP6IyOnJBpClsKFsN2AwFYU1L2yGunj0YJXNk394Ipm5lOlLOedQjyARX9wUL0vzvS-bpq_aXaLOrFe3eCdDxd-7psIROA1P6C0rpfddM8YfE9zG6VpiS10C83OEpwj_WMNS9MNL1eu6jsbnM0cKQD4M7-AodiZr0c6wzsCZITqVWocYoMbOK5jOfOqvW_va3clGOzVGtbW1HIEHRivyBrbEy-wWA7Ze-AYOQldSJ2iOBlLn9phquPZHafMVfAWa9-eGQ3W3CtAHRFSVWa-n0l9LH2NyNEJ-LUiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lONhsDHbCq_RtkYho00NVb7AMS3Y_oVC4yjjvjUaAbn0s2XeNMZPonHz6FQFsX_-X2hNr6TvYjRakXM0_UbgGZOtWHkWCmiBuacTW4z_xKHLoJZLH9MzToNK7EUTzdhrfYpPDtQ-I8ExZlUwfAPWSO1xU0jJXQC_ltFdUFjjAwEV4rA6X3aM_kx-NWqFbewXjU5RNtnYIOF-chXYBwNvWR-57SAWBjw0FX8vhVykeRZC04XnV7oS28rEmhlMMJ-bslqilYQ4EZvTtFdc4v1MhwCEPwDbm6kavMFb7-CN9vdl4CgNKbEiVN9SqK6s7wp9MYp3VUS1gZMGHAc0duCh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3UK59O4fwg_YRdf6Hns1RQeCtHo_lirsgkg6AorNnsgCkkpxTFtZitCwgIFj_qcStClEfXroW7j4W0nIXco0ILOi12GzcBUwi3wjHHcKhp012S4OKaODsWz8M4CqxIgYiJqX2-bRImKcCU0cNre8j7bCIWoZzIXTQXW3OyejXve5v9OGx1KPnmrMkitg7tYA6O1VP5pytb_5uzqbUlrAh1SRl5v841GJZFEyIc6nrl8GmU7CMeSUopp5HL-NOdK8jFXk_YslL8qrHSvwsCCk1xKrkJgCsPQQFcOIAMNxgLUbbPlpJjLsF-UaE9En53ZfTUbqvzFjv8UqQvNhvdIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtR-q3e_UPQG_zB7GL7yj3GqPbxbwtA5CJ0ZjlxR-O6JJIQHeTXC6f8n7byGhkX5Iu5DkjTks8ihagpa0ROUxXrchsjdJhMH3ucvAxZGtUS8hBPzU_zeoXeOvkzB1FAgBb1l3hsm51usQAMz4TyRA7XiLLYuK9QzemuuNGT_rYbDFaGoFUPu8n2i9Ue1DaUgwhTcY-XfoD1TgihLI32WiHIWR_5tLW8Mphm6mRxIBxwIEzsIcRiqAq00udSIUOXJ4uXKgs9fesuCANqKfIihc38PNn1dk4DOtKw-8zYcpMSISfs6Pwvzhq6OACCW-xvcwUfm57Y4yT1Lo4B2dvvmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep68DufjcHXdN0AoOH7QZncQVzPD2VhnSiymvtvmiJq3BxZpns5H6OgJeVMmy83xvJgWBzHvzgafyzxHRujnpIndmsugvqwob5q5jHNTNdhjhD63Aobzo04UySOscQbrTvce-2h_z5DREy6SUkBKdehzTOiR77AoFX5QOudkEMb4CYBNPPO_rghTbKFYWtDELnNYMMhKIqFdZOxC1a8rUCQnaUBw54EgZVKyY57dYKiCH-ZwCktk6IGFJb43nlHO8vf61ctl3RfzuhkDB-kMCj-dnxTRqAB5OOx3qNPcexXS58X9h91tDhHsGglNOgOiFfcNGuNeqsecvj3eFzPS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nni0DTEUWAfgEmazToZgNLoFBs73aZ16z3Z9dPLVypciDYbFRbo5eGT6279kqziMkLSS6L6KF2KMhTYe-zMuDvhzJHVukF4JXbL9b_ohGsvixYI8t2Dj3u_wYee72ttSMcr8GldLg6XexZhp8oId9zHFxY2nkQGfRlRZqDnATlvYE88QZ2AjOT5i7pg-Uwxc2KyX_43MQTQMqnDpes-OCDcxOkjKKmsJZa7ZZpjsx6Tojz3sf7s36CBnQ70tmCaCllXiDHt2-Qi-fqlbC7C5Y_J8D2sLe-seep5zHCeJDnsXFzj9bIbCQHNToTi5S3bQi2-EKhZu90y6CoEE1jnTuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لامرد؛ شهری که قربانی یک حمله شد اما روایتش جهانی نشد
🔹
پشت آمارها، انسان‌هایی هستند که زندگی‌شان برای همیشه تغییر کرد؛ کودکانی که دیگر به خانه برنگشتند و خانواده‌هایی که داغدار شدند. لامرد یکی از روایت‌های تلخ از آسیب دیدن غیرنظامیان در جنگ است.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/674980" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1bf73fab.mp4?token=ezWZMHQI9PENIht5rkp85WDamQWiswymvUCPZroBkezpSBnGpg7QV3lrk0jRGuh5v3uXvmCeWPyPKPdjnFwmE2Guxi_Ma69Eq3f9BLl0_iSUSab74b2mvYcY5hwXcB08qSkY2wCy1ovPgzjoWY60HxRWR5v6HjHOWXHsdTclSgJZPAncUeYMc7tT3-yhK6J6TzilNQsmZoYt2qiBw4kLzUqYjW768rFhZt-Q8qh2qypuV-uTCLPXsWq9ltCYwRFSKcJERt90DYpW1TckVOWluuGZUXX94fG4GooUgawNSKbm1Suw4MoI-sOTszwm6X1a4S1CaNrYFmeOQ_H7EKqwMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: روزی می‌رسد که پول دیگر ارزشی ندارد!
🔹
با رشد هوش مصنوعی و ربات‌ها، زمانی می‌رسد که تولید کالا و خدمات از نیاز انسان‌ها بیشتر خواهد شد؛ در چنین شرایطی، به باور او نقش پول کم‌رنگ یا حتی بی‌معنا می‌شود، چون هدف اصلی پول یعنی دسترسی به غذا، مسکن، حمل‌ونقل و خدمات، توسط ماشین‌ها تأمین خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/akhbarefori/674978" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3245f5ecd8.mp4?token=aXOUMNlZvPEtAoXLa_PDm0wPOADJQobGF89MPef28-nWJzSbOV748IAsOdMVNlhAS_MTzqKbJUc0pYKoj7EC242IdPXcVAcTe3x7R2x12nk9Dw2ntS3xrHmJmr3l1hEzPwtjMoGJ705ZIgUqQKr_SJ60sqaOtIMZ4Ez6C_0I9B61k45HqlVatGFOFPtrm34Rncaj3XfxEDUsOdAlSRM9RcLYMVKYLmp3pYjxt_aicWIo88ze0-tAuA83xEzDG2He8i3USGYBI5KxPlaTJG9-gfEfCSKO6XwrqWPzPqT6FsoiPoDLQDpZD928DXimpfWHY5HQNd5p9cl_y8TO2ccyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک زرد: ایران برای بازسازی خود به ۲۵ سال زمان نیاز دارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/674974" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da21f30e2.mp4?token=QRz3PZO70lkDfnnw7BkQ34-H8ZxePho_bjhugQOK9w-EJDFr7nP4Uh6OVedxFfhFGkzZdPdrxh7PPNDOLqSZlQCH1Z8w5VVi4FTBw9vqGhwfF9Z_hTDkYWLL84d_rsgx0nGbVqr_AfOBAQIwOlKAer4fpNLb2OataJlJOE63eNeCC9Dcirqul-I47ys-W70fVaNq0Und4rkFm4WK-yfiDgrpZNCBQUCeLK_yzGuvyRiTT9Ir-4FFr9gi5OfIdGxYnj7wZOfz2X9QXxWBaB1nvGIgU0OXuuk8GiOFgcr9LFB2J7Fo6aDlRUwzyxemc_wxnq-gFIoLxLwYyqpO1FKPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت کادر درمان هلال احمر از دق کردنِ کودک سه‌ساله‌ای که با چشمان خود شهادت مادر و برادرانش را در جنگ رمضان دیده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/akhbarefori/674973" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c795d247e.mp4?token=bVBHXjQpLoZgxSEBsIO9U7qOnHEqxNm6qKs04C0gVMXDUo5nry3n_jkGgyDANsHVZrAkGII8gIr3ehprNINi94fKVLThjsJF5oZlgjX9WGOtXt47Xd1StVZwTOYNpJmWq2bd95-xMhFEIwjEL6_y2TGRAMmOB6ERmRnFhE4YoGAQDKHsvMjLTo0A-8956IvzrK3UTbhCGATmpH3YuT-UnnZE2q5vBwiHQKlKi65eocfJ48fQ6mnTH0-9j2DBZeMDrHCwMtuHxblgdYybQKGD04gnC6_LyENaF81mznjhEFFvkuUsC1g2ry-Wxd2btWAkDScSG7bT1e-R3U4NcgaK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/674972" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
فشار آمریکا به کردستان عراق برای ورود به جنگ با ایران
🔹
رسانه‌ها از فشار واشنگتن بر مقام‌های اقلیم کردستان برای تقابل با ایران خبر داده‌اند.
🔹
بر اساس این گزارش، آمریکا تهدید کرده در صورت همکاری نکردن، وضعیت خودمختاری اقلیم را تغییر می‌دهد؛ همزمان برخی گروهک‌های تجزیه‌طلب خواستار حمایت تسلیحاتی شده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/akhbarefori/674971" target="_blank">📅 00:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن  حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/674969" target="_blank">📅 00:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1oGL_K4j_M9RDUopAJ1BJNbR0RiPtZQRAQ05g8MMtPuWA4_hsQlK65QzFVIJEWUCU2ZrNwSOK0q25jAYvOm8xBDPrxOadNtwasOYEc33F20FyWcOtWa1wURn23uWKmLoVOYQ7ZXD3RHErTHJWs0as_0zgxR2xxr7rWIBsBOzFfcZClKV6AYnoE0kX5qjfGx8XOeJis1kCDVrLO9r8UOcWJ6axGjH7m3ubq0ssOerg_YZ_qy_sAVyQV2FcDaExlY5RYVYAVYOWOQ_o2mijoGDFxIkgG6r2-fQ2Y3U9c7QN2j4Fqlbt0WjIp6z14VG4V07lE2WYxVMTdNc-cGNNV9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش انصارالله به تجاوز سعودی به بندر الحدیده یمن
حزام الاسد، عضو جنبش  انصارالله در واکنش به تجاوزات عربستان به بندر الحدیده یمن تاکید کرد:
🔹
بندر در برابر بندر، فرودگاه در برابر فرودگاه، هر تشدید تنش با تشدید تنش بیشتر روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/akhbarefori/674967" target="_blank">📅 00:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShbaacsekBTJSn7OgrCWfZO1wfOmyyz55_1txvhFw3HzWWm4uma0zMHT9bSKF_V9I18NAkGsLWEx_ITfLTMD927OuvrkKbshz3EjDId1eQjrABP9rD1IBhNXk6lAjAy4pVKDF3F9b-_d59NOGY1XCvCxUXmzb0vpNvSyX8xeiQU3ywc2GfMQ-Gs2XMp97tOT7oiDnKpY1mcIdUxqnrqTvyKecAXkWjBBdYdyyw1UYXL2v41JwNMc5bU1o7oFEHBoNbloX6zCI_6I-FBYyAzQJwMMVjdcU5nFPcLwLk_J8OYpbPJEMJL4V7vkIsUP7cEVy7UJm6YD3Q_Cr2LVtkoKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/akhbarefori/674965" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKV_BEI2CKY73ZEnU_kVQjrRiRgJn0XA06bMBTzbIqYQXwRH6VocbTldvRpjXiZE0YaNnOGjSfXkT8Xuq5rKokkgvd0dpoW5Jx-KAA3zgF5mHDhP4J1YTcahzlaOg2qdsfcmu_6xQNAEo0qy2LG_-xwEC7xzbPMasjZf-L0ykRtTr-6MM-0iVCqIahal8ROd1wvBKULpPG_d6JrVVI-780E1vZMehSloLxOnlTCQVRgO1P3QmP4OX8zr4frh_mMlckwxJItmRyQ3EtedyFyTLyW2AapwVlPEAIGf-658PU3_qYY4t60Qid4GYBq5QBcNj2onNKBPBlMbhGXyVXwLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/674964" target="_blank">📅 00:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
راز آخرین‌جلسه شمخانی فاش شد
👇
khabarfoori.com/fa/tiny/news-3232741
🔹
امروز کدام شهرهای ایران هدف حمله قرار گرفت؟ + جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
جنجال بازیگر فیلم‌های مستهجن پس از فینال جام جهانی
👇
khabarfoori.com/fa/tiny/news-3232778
🔹
رایزنی‌های فشرده برای آتش‌بس ۱۰ روزه | ایران چراغ سبز نشان داد؟
👇
khabarfoori.com/fa/tiny/news-3232805
🔹
اختلاف پزشکیان و جبلی بالا گرفت | ماجرای توبیخ رییس صداوسیما چه بود؟
👇
khabarfoori.com/fa/tiny/news-3232771
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/674962" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674960">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0tRzTHH_ZdTOnvqPcIz-UkzNUqaK82POG-uD9pbZu7xKKshUay-KOUTBiMavA42h5kWQY4ahzwhD3M95AIK4keojjq_Vkf2ONiMHdTfPZ9wx4xYUbiPhXq-4vsnMW7pWS5K4s7apxITgrDs0aodVrUDdvYEAjIlCl4Qn4nFMaWQAyISeEOuAHMyhB4nheS8PgvE40CPZ_JtlTZCoh321As2BkV9RT81iS9fDa1pT_DvqSoCOcVN2dp8gmFkbWYExsDMlvJnBE7Ipx1oab3ALjx7rX4N4Kt13vUf0f9EtPFGlhwA8SRnBC_mpr65uxveqhsaYrvuQgLC6qjA32-0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: کارشناسان هشدار می‌دهند که فشار اقتصادی واقعی ناشی از جنگ ایران در شرف وقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/674960" target="_blank">📅 23:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f63abf7f.mp4?token=WV3ANhLnbcZ9YOrsdnBCbifsEjKjVEn4ZD8ZaoJB4nnP0SIU1oRmw2Lk0Ivah3xJ0RJDmLIYJbrLO1xbjePYM3XrpSWJL0UtkAAKFJRWQubbx3um6xsaEs08qrw3UgNHfxzwwEYkzYpWjNpThn_giqVCx79foMiIzy44Y7a-A4O_ENuosJOdbpxUk8vxkcJPa6YmknLfXtxtaLGqar1e7OD84B_vUACLCwXz5EnhDGIpZ61Nl29QUzzNqglvXAJALMQzao6djwscPBkQ_tZCK5g-fMbrpY6idJb05QqTw9zqllqsKZx0fbaHA5V6DWccjSqeYxJM7Pu1jGBkc3Kb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هـــــــر جا کـه هســــتی</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/674958" target="_blank">📅 23:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a642cea0.mp4?token=R9CSuqUUhOUdofK_jXO1RaA49F4o9Y9Ly8weUKg_Q15FZQoUpqK4Nxm73N3byfV6P8oO5N2DbQHnjiH-vfKzQGJ0cqOL4bElkEEDDT81my1dia8hlqUmIr4wk5JcbKHba37nBoOhGYmR4nnF5daQQrh37SJFmvGcijoWEgzm5RSqwpw6fW5LBhPfVm5_ESBR8mXFBMApO_ZZqOsXvLcZ66JEOHPV2I2SpduBqyV_jPpTFuBe3SM9RGcINoKzCg35SYRwmMSrOcCargjzzyNg-t3BRDNWhEWB-nnMic2K2UY-8oqIZ4fL79LAYsQ9kGZql9bEHTGZHeH5SauMKTzPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تقابل ایران و آمریکا در روزهای آخر عمر آیت الله حائری شیرازی رحمة الله..</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/674956" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URmsXRXN2cmFGO-5QX44q6BsjhjE-2XsDJyxVP_bqac_3IiZiyGWNFKCIAO9FaucQYn46lsfS-d37iOSqDd5vc-1fVLXQM_AqIGvcP_cKfdKwWSwdX0SU3U34G53dFRyca8Vk57PjgOkEugG2E_J7Wzr84ioEYLoQbVJ_tATs21ilNaJ7qEIYZ1-8TVcT1Xcrk82r8D727h3hsiPD1V6tZCieValrk9y5NhhdjqR63igKtMwpVrvmPZeR8Y3Hpuh6tNKA1iR0Lm0OTfsecu4YS9L42sBj_QNgomD82_Bog6TWFfFDWp96L_90UDwRu7EaxqVLPztNQQ2gG6_OEtxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4d128eee.mp4?token=h2Tv0N_jx3mDE-XFEvCPSBRLZF5cA5veSNKUiruCrqf8E9nK0DV4xNvhRhGISae2NzEfkuViPipb4xF4-iVGUFoVk2noiwEFPnRnnFoexAQNd_NSLmPHEqQLEtc8yhS88CjuYoVo_968ZxqQlpz3yea7hmVGn2DfWPlYD9syVJR84xAkeF-odOZhf0nI3SKcYAamO72okQyQUsMwD5SkNrqcRA6WccKfNTppE_uDh2-RIa6BaEzTAFSABF23z_l649NDimpRDSxcvXRTimE8oeP7A73l8Tyw7xVkdpj4DD-4pra36JJQdPvMeMu7-hrXy2XBY_bJQMFf2mtZU_IUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشرشده از بندر حدیده در غرب یمن، زبانه کشیدن شعله‌های آتش را در این بندر پس از حمله عربستان نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/674954" target="_blank">📅 23:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSoMgPU6CStF_axzhbcmhiN80hRFMG4ctnSj9vqGaEj58mFYrIgM2T3MCMvVyJu1gQT4uJYiYuAJX4sw1Y3XMMc28Ql2vpDW4WVm_pF97cOrxaTjPQWyohBuHYaMpMGwhXpYQyImRZieaKb4rF6kxb_pZ67bUMQAx2zPEEvDrM5fmwEgRMpqPUvxN2lxsiY7kT4UO2HdlMHMhecB7KCmsQhWW9uj7_8SdSoE4sIstIgoGPjb6Sv0VPzeYEErEwdDRIoPbytrSb2tV5hBDvYniXgqJo-DBSlthLZE6dWsHDUhNeP4ffGNfMpw14vX1Q_Yo_mHW6YSoQWiBpeV0HcNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنده یتیم شد
🔹
هشتصدوهجدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/674953" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2oozt6LJvSXI0MearO5HKB_HzG4PT-fPStXxoKsvIDzfIXJWLX9yQ38mspy9qAlZENjPnT1INOtyJEkY1JTuQwTsBfESfuQvKwqyQi2rSkNfORorZtSK8Qv-XiB8wkjnzWuMG4o1yEiOwLP_KeqbVMrDCx05s7wjPekqAknh5jOssaBjlqWSqb-Yg7pc6AYFf4CqdfI3Sx4Tbzuz6mzDrjlIXOZCAI2XAhGvG3rLYsq-gJx8tSi0k9bj8Ow_60Fuo3iWk7rdXkDAZE3jChL4hGcrEMrjh4K5cPi8korbENgQZweyhImMmU5TCcIcqcvDGWMbRs7jagr262V8svCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674952" target="_blank">📅 23:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7460a8d557.mp4?token=AlCKGT_cteERrE52SrOhg8TEUK6B5wx4ortAGPiyNe2H9pyvGIZOl0tZEN6reS5IscL1nlm8V6HiSpv7s2agN3YNl82IcAN2EnFau2frquwbnG7EmgZTcDjhdc4-UkQkjVkvl01q1C2fTx1kB_WmSKE3jU3utIOsfFTogyI6O3kulc4m6uUB-F-J-kPbIlJEoT5SSlthJ2GKitovZeB_g2WhaeCScEruosFAhGUIoVSH6IAp9wvYRvnhw_s2ad2u8TkeVU0Jv-_eEBl_4TpC_x_1C9in94waDaIyN-ppsmZVqysiMuJLLseY_HkVMUjyiQn34FS6jNuyTOsljFoWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد مدعی شد: ما در حال حاضر در حال مذاکره با ایران هستیم و ممکن است به نقطه‌ای نرسیم که حمله‌ای بزرگ ضروری باشد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/674950" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNfzxx8Eksfp3REUTJoADiAPYoRXTuTLRsw_sM8trfm9sMD9MJaAgl3emmlqeHHfJQ_MAiqcnfMStskF4pCYOYE8dHpPfu9aDxeqiidzNMRS2mPHkvH6afD0me8NcOJRbgk5C3uagv08gJn4EQ6cXEcSsJU6LlqqKWVyWxPBGkP83x9dBQ0lOniCzOcJjDeDmypfHbeLz1ohd9H4DoOxg64H6J_qPpxE986XyioOasiFHIBp6_431SE2s7AZiYD90h8yRgz2JBJutA6B4qVxsI4UlKZnOa-fwxeCxsO483YEcD4ykewdqK5G8NI7RfwwkMQ-oUjCnMgQ-mAgJCCyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/674948" target="_blank">📅 23:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/674947" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
خوک زرد: هنوز درباره حمله به ایران تصمیم نهایی نگرفته‌ام؛ مذاکره در جریان است
🔹
شی و پوتین به من گفتند مشارکت نمی‌کنند و به آنها اعتماد دارم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/akhbarefori/674945" target="_blank">📅 23:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674942">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4507e042.mp4?token=EabzO5CrYp7T2sv10T9fqvMNWMTgQgIDTetvzOZprJkOSBf-T3C8dpnTPVjDN081U5S791_bl1PWUszl1HDNP8RuMKwJz0rkKJNQxIpwz1IGSJc3U8rECTgTu-uJ8VVaBJ3wJW-2cYsC_rXcJOnJHX9lThIjJfsd9XoJhI6nGIR-Km1kV_T56H4azYQOjWL6rUIRmqMNDfqHF4FdX09x0WLgOGQYtuaCh4S0D06YmlyhMsw4QOvoDJM-MjysrkjNRZORf7jNH_21WCSgPsyU08fEc9tS7153fRRHnhabD3pVUc4c17UHMX2GBol0J3ZBhgCPZBFigFPWjl-NAYd1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفره خوک زرد از پاسخ دادن به پرسش خبرنگار نیویورک تایمز درباره ایران
خبرنگار به ترامپ:
🔹
شما از بمباران نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری در جهان متمدن آن را جنایت جنگی محسوب می‌کنند. شما هم همین نظر را دارید؟
🔹
ترامپ: به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔹
خبرنگار پاسخ داد: نیویورک تایمز.
🔹
ترامپ: حدس زدم. نیویورک تایمز شکست‌خورده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/akhbarefori/674942" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674941">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3427ceff0.mp4?token=ohtsKInPhrHhGXcQLwjd9vcgmky-vP3hl-2A0ySfbql9ScBNn7bn-LB5liCxtq9fmd5RtA5x98_w8GxrSHW67eB1gAsM3i2ricQgjyktr2EoEkRSYPPThFrfk1C-JpF9ogIdSkkaGlRnSr081YlQCF8jJUwk-siy1hfKy_QaodFLFw8j5hAwj5l3ZbK8pK58TJRU6T5SZV200TlYELHcmkaRlWgSUo9Ur8BIeoNLtGGdPNCyoLWnUerw8IhdPSkzNaqmuwhw_OuX06VK_ZSBzJeey4JaBGZh4xvT_Z5RphhSW0yRPLl4XOXZhY8Ix0VRS5GKbYf_8DD0VfoOYnyypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: کمتر از ۲۴ ساعت پس از امضای توافق همکاری هسته‌ای غیرنظامی میان آمریکا و عربستان سعودی، دونالد ترامپ،  عملاً این توافق را با اعلام این شرط به حالت تعلیق درآورد که تنها در صورتی پیش خواهد رفت که عربستان به پیمان ابراهیم بپیوندد و با اسرائیل روابط…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/674941" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghreR_N5pXJl9dmw_bN4YBKWnrwImIuOuJldAV3CXkL_m0Kwp5xce2O5IBlW-dsNxjzCKc7t3FPQvwo0B19_3pGzk81mzaUrlfim7I2Kl6wPzuBJhO6Z2vm8aqouI-Ykd5O7K6NP3XxkaYk_mRMFNqt9XIGE3fhhj39bDFQVWuKcEvBfqVOAxTgxgRIuMaZukxZUJCnUUCY75WzAmZGXzPhZ9xxhqOL2BXU867LKtJhL6g6KcgQp_csizUxDuRdmZRaOExxkFulZ0sc6uPCt7B5LSFp_dH22aS8KfuZ270OVtWNGN0ZjvSWw_6WbQErB8JyMAa8HX_9dwqqsX1rxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برسد به دست زائران اربعین
🏴
🔹
امسال هم با بسته‌های ویژه رومینگ اربعین همراه شماییم؛ از بسته ۱ گیگی ۳۰۰ هزار تومانی تا بسته ۵ گیگابایتی ۱۴ روزه و بسته‌های ترکیبی شامل اینترنت، مکالمه و پیامک، تا در طول سفر با خیال راحت متصل بمانید.
🔹
همچنین می‌توانید در آخرین نسخه اپلیکیشن «همراه من» به خدمات جامع دیجیتال اربعین دسترسی داشته باشید؛ از خرید ارز سفر و استعلام گذرنامه گرفته تا مشاوره آنلاین پزشکی، چک‌لیست وسایل و راهنمای سفر.
📲
روش خرید بسته‌های رومینگ ویژه اربعین:
🔹
کد دستوری: ستاره ۱ ستاره ۴۰ مربع
🔹
اپلیکیشن همراه من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/674940" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cd13bbff.mp4?token=SufpvLLdYU0WhyrwOXU1Cu6p0Ng5ZPUhZwUdpuC1gqSsfUAV7JC0FIvaeufUd7LL2RfqZPK333GGdKRqT3SUSG_XAyUJs5QWVXB2ONDbjRBgSizCfuvnH-a4cJODNdXeIVyLcPta7PUuU54vznHrnjHlIeSgFCGfI72UpMOsqTQ8yKAV0KeXa0sYN_AvoB3Z3WVdprNLrptnefNQVS4gXgGSP4RlPzuZa0ZhrTLI54iWXZEkImiBaW6wT1XT4z2mYjdzD8FipyIuFJVFhXL7ARnsB3jA8rF8SdNcsgAjrEeH1w-rD0wYrR1ikgZcT8j_pqQSyXLD4reO3kwVIQ1xZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاج قاسم سلیمانی: اگر آمریکا جنگی علیه ما شروع کنه نه تنها تنگه هرمز ارث پدری ماست بلکه حتی ما در راستای دفاع از ملت و کشورمون به دریای سرخ و مدیترانه و آتلانتیک و... هم فکر کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/674938" target="_blank">📅 22:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
جهش تاریخی صندوق ذخیره فرهنگیان در ۲۰ ماه گذشته
🔹
تسنیم: حد فاصل آبان ۱۴۰۳ تا تیرماه ۱۴۰۵ اقدامات ویژه‌ای در مدیریت «علی صادقی» در صندوق ذخیره فرهنگیان رخ داد.
🔹
تشکیل و فعال‌سازی کمیته‌های تخصصی مانند کمیته سرمایه‌گذاری، کمیته ریسک، کمیته حسابرسی، کمیته انتصابات و جبران خدمات، کمیته عالی ارزش مالکانه، کمیته رفاه و منزلت فرهنگیان، کمیته مسئولیت اجتماعی، کمیته بحران و سلامت کار و راه‌اندازی یا توسعه سامانه‌هایی چون، سامانه جامع اعضا، سامانه برنامه و بودجه، سامانه ارزیابی عملکرد، سامانه قراردادها، سامانه دعاوی، سامانه املاک، سامانه حسابداری، سامانه معاملات.
🔹
بر اساس صورت‌های مالی منتهی به ۳۱ شهریور ۱۴۰۴ دارایی تلفیقی صندوق ذخیره فرهنگیان به ۱۴۴ هزار میلیارد تومان رسیده و درآمد تلفیقی به ۵۵,۴۶۰ میلیارد تومان رسیده است؛ پیش بینی می‌شود دارایی درآمد تلفیقی صندوق در صورت‌های مالی شهریور ۱۴۰۵، رشدی بیش از ۷۰٪ را تجربه کند.
🔹
سود ایجاد شده برای اعضا معادل ۱۹۵ درصد آورده گزارش شده که رکوردی بی نظیر در تاریخ صندوق است.
🔹
حدود ۶۰ درصد درآمد صندوق ذخیره، ارزی اعلام شده که با توجه به نوسانات ارز در کشور، کاملا به نفع فرهنگیان است. میزان تعیین تکلیف و پیشرفت پروژه‌های نیمه‌تمام در ۲۰ ماه گذشته خیره کننده بوده به عنوان مثال پروژه سبلان۲ (بزرگترین مجموعه متانول‌سازی کشور) ۵۰٪ در یکسال اخیر پیشرفت داشته است.
🔹
هتل جنت اصفهان در این مدت افتتاح شده، پروژه هتل قطب مجددا به راه افتاده، پروژه پل سد گلورد افتتاح گردید و همچنین نیروگاه ۱۰ مگاواتی نیز به اتمام رسید.
🔹
یکی از نقاط مثبت ۲۰ ماه گذشته، بازگشت ۱۵ هزار میلیارد تومان به صندوق ذخیره فرهنگیان بابت پیگیری پرونده‌های حقوقی بوده است که در سابقه صندوق و همچنین بنگاه‌های بزرگ کشور، بی‌نظیر است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/akhbarefori/674937" target="_blank">📅 22:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4498bf9a7a.mp4?token=mXfIunJPiYLkvSgtOW3N5mhfrsF7JdcUBrH9ktUFc42aDlx-AwwFOfjZgrZyw7fvm-EXlcsLQAM-iWu18_GahW1ikqBhn05tClUL2w9THvkLsL0rU6hdSGiKIown20EzjAmgeqKkEhNCfNgxymLeoi3jIrqxmMj7TzAVeID4Aqelh2b1cOMlD9pF4Nw9gBPDe8P8VLkqy7XhKr-v3NcmzUnUChnV9gI1Rlf_7rwKZHDSC-zRHgt74vR4gmZNde5vpN2q0AnCE6SePBBmZrZfxZoT2ACgzqdwBFNfYNskCwwK_Qp1BkOxPGKMzIhQXE7a88KB0dQIm68WmfMTTkMieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار عظیم در یک واحد صنعتی بزرگ در رتندون در انگلیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/674933" target="_blank">📅 22:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2SAUr_59v9VDoxUeOZ80g2i4nR8_fa-lxv1nvxWdKNmlRbW3aHXK1_4ANY51B6iWh5QsyCMnivOnCIB2sAw7y3xGFUdJtjvEkAXA6gP9UEYKEkv5t0ufzA9yWsgF7TJbgkuSeAUDw0uUvKtie2DfTmc-q53MP6eBy4a1wDHPztDsUbFqrQ1qF0-3fdzZcy3Sv0oZsAW5S8aghmQOeqazG6OsL3FRPBUYoGpOD_5NMv-vwj20wu6FZ6dTPnMiRkHcWR4fAjAPx4asdDZyA4mzgTLIvD21fs9SmTdMm3iE9qyRreOrvHAcQPwK5lCGPskYtaoxj6e6DM9HVXk1ampzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZw7qgXkl3Occhh2hvnBsUGx8V1B0o3Th96wMsJo878a8CUqz3ZPvHrsG9ssjb3kjFeqiU5p7lA6gQnItIN_n_QxjLYbV03urnFoX9OZ2D3w9ExX8X3jmv1PT1kqwxjijUXWUJorksCs4kCTmCU-tFfc2wwsBQUZiFQWpdD1kqu6gXTfcNHmCjZywaZgiUbosfHgPwr849eLGCKEQezVisL6saxhx-7UUkJBKqrOhTPXL5poYwBM326OWwcl8Mr3gIC5eAdO6H1DMacjO2JV4zvGmu3YQI_-Jj59ebLjNPTT8Wx4A1JZ4WouKERXcnq8Uvo5VaaGTDkKAM9Y_Wa_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEcvTgCb6fY-GZ5Ab1lRnXjKXtR4bg19Hwn9Lp9bY6XC-rSbI7JhZR_3obfaCZuqMsFPzZQqjslCO_M2DVQEfNeAbxAyTLJZOCuiKYBTWLV1h5zdIj5eDovicIniVVwnj0blxYOHgSqJE-3z7-f-mMed_DpKcZySqrk6bw6Lm7vJULG4505agQNXmOXqDbHV1a7e8GAhxFs6tuE-QnFckWEZpPjHQaUMHqS1GqjntW7fKIdLX6GLnqGrmwpTvQyOgDH4_2OibNXS1P0JLfvji3B9dfhuupEHF1qOFQu20K8-mxqpf9f56Zib0EYmrQYNcsRFW2-N7nE16x5q9X1NdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/akhbarefori/674929" target="_blank">📅 22:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
صداوسیما: ارتش آمریکا با شلیک دو موشک به یک تانکر LPG در دریای عمان، آن را هدف قرار داده و دو نفر از خدمه کشته شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/akhbarefori/674928" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370fbc2f00.mp4?token=AzpM6FSSTaPDpvPTk1PpByMcsrVETFwmRBVuyEL5FocINsIljcqUPNXS9YzV6JZ3JonBZuOqyxJrAkD8jUuf3WSYqB_2sJ6YCJflzCQjfitCVwmrKaDhCazzoa3qOtLXbHzFpp93LS32Cr6HpfkYzoS1HwuySbyg2SUHqh3zmvHiKKTKz2fyn-trIFZb6RUMTZljpYQRhKNNLKdrOABlFBiMo7NEmqptNHPxhpzjnZMg_is02QCi8attrH9p9dcw6AocBOQaf5cjnv-g6as95EJz03L1g2ajEujkQSBKAHGLCa3aQhH2ZP4M6B274KVUb7V2G3Fm20Ym0dqIpeB_CEiBBLIcCmGrD_s0zNKjdwEZcuj9c_ZmM7u34VJlX6N1zpD6dL_3RXXzLJFt5MgRWcYtg3MpTrTE1KOEIE74p5c4CfBzpjcmH_6Bide6Rt3GIRL2ErTBWL569OOvJSS9RrC_CQ2FigaF7pvEyrHDPzv4LTx47owvfsTxBWuhBFOz3fw4KAyOPoxdbMyh_K7q8_gmiQ8JvLTNnzOV2-6pdoSuamJmGiPJXPDS6Kns2l9Fx6bLMVfjP1Z8rETvQU74TNshpgEKAyV_l_ohvzbhdDWr2d48xmk7KV_DRzs18FTfc196ds3Nn9nJsJ7IuVwINarp68U08dL9Flmp2Y4nBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صلاح یکتا به دلیل دخالت در امور پزشکی بازداشت شد
🔹
صلاح یکتا با کلیپ‌های شکستن قولنج در ایران و امارات در اینستاگرام مشهور شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/akhbarefori/674926" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd09164e.mp4?token=rjOVuQajLlNV2VkCLUlEYlDFLhC8cHgOerpeGHrdfV4_6odyY_bSev0-em5UV2R7hNMILWq5zsuarD8kA3oP_huNuWs48dXUF3bF0KV8XOdk5Zr-R2p0eTrcDPgC_RDbAf1xg1-jdYBw9Y0zcXghdq-2yx4_pHn7DpD4Invy5LOahYm8J24SzJUNN3G9hGUKdKyaPK7rlqMD-1uMSxyRQzmgoYr67WUQsRQtlTk8MUKI1nGJsXQ-S9pUqnlYPXw9BUzj6mYJtpouFOLR7ZaWI0kZRz7UcgmDQm9jZo7rCKkW_belubOzF7aJmxD_g0PLqaJGfXXInDtC4KAqJWdNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش ده‌نمکی به درگذشت اکبر عبدی: خداحافظ رفیق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/akhbarefori/674925" target="_blank">📅 21:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
المیادین: فشار آمریکا بر کردستان عراق برای ورود به جنگ با ایران
🔹
واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/akhbarefori/674923" target="_blank">📅 21:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYhW0opZnRm72uAKUWaXILAkQ2VccDaXpgDjl3xQ6qwpwCTN0UXMu5DpSWyuL3IRR_RyWVAh-fuV4j1zdjjIU95qvBYlhUBTW6oydEoo5dCrSZLxKWA38h6NGWNiPo8eatYv4B0Kjm5hPRu3C7MvwwRo_28MSKrurb9lDe2GR3aqFf_aM5PcEv6LA_fWdF8ohn0lcqvNzqYsSdA4Y1FvCshcXb1XZSmDJTFH3Dpl-GkoxO-mS9f9DIA31xEsVFLJ4inl1H0BMegNd1HjTpORugwiAdRiO9EWD5mOetcp25KzFZwtsusia-Ei3Lvh_NpBK8rWO-YC6x8Z9U2PRgzsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/akhbarefori/674922" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674920">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c96e0588.mp4?token=uWrOYyoyExoAVf2gXE8pJImHtlTIku8kiqOItnBhGDDaS9e654pXvmy4iVCa4SqKG77nWQenlrHAP9RFr4PTwe4iO85KKEauekT3fpv3GZ-AQ44ocTHP4u1rbmHeo11TniRpHmdHGseNW-NDzEYilLy6EkeplP0ykw4EziuvivNT3ahaZzWgVsR192DoMKC3_rjLp7LIbGmbpOMpkQHskhzf1M_q0wQpyMeV0gISiKCzuXTIz-ABmQn9FfNlYES2AmwW0hSBG1q_ojueK8AevCTNK0K0zu5FE736IfgHLsIIm-lOw82MLbOw9CGxthzpY7C6D_OpPFN5eOulBxKRgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی درگذشت
🔹
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/akhbarefori/674920" target="_blank">📅 21:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82bdf2a764.mp4?token=quCySdjQfbrADX1-xUKU0N2ACGnVAvKbs4GfVNPjdoPf3wJ9lp-84_-DZ8EZgx7eYanWrpfEUVFB8Aiconu2NDvQuaicFKxhW2qbUA1YfUEQQNVKkatf1zTsHGYjrc-McQ-ouC0vUe1GzynuMLotFyI8IUK1fjEEo6ScuVZHIt-UJLqT2j2KMvFf24gP5vZY_tZO21oOr8Edll8quBfI4DbsTHIdMg_A-h0GvLLpiOBGghAj3lWC25gssVK0B_GTuA6jk9599pDhyux0LswzjmmHxgfYt2_OAt89F09uKd96fSLI5e3HdpAF9nxL4HRdt7p5l5_kxFCeZwVyrYVFaHPgSKSHhkUrTDT6fH02LsR78k68B9GQBzA2u8P5G6Pz5Yvwunx_xwh4m3C93fNsrVyHlbwAk-Hl2v19bT2KjNyDNbD1CjAvsuC8B8LBLJZRoteaMVtpzeGURppPI-5i5bnkKE7anCM9v9Qlnd1GVKZnwlLSzLJO74U56MxWzhdnFw_zsaKg0vGrewWGgDM2i00Wqj5NBvsz9hVbWuw9JReH_6x_TeQ7DTL6Y65pT38tX_w7clgS4Fqs5uMwpnCKmrgyR4-Qci_6zZ0byIipNCeoVKm6TvUS6ut_8FTvE-TDosN0CNxKd4jKODUg5OELSL9BWDOuYLwY_3QhBCwyEOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از نماد رواق دارالذکر در «محرم شهر»/ درد و دل های مردم با رهبر شهید انقلاب در حاشیه رویداد آیینی محرم شهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/akhbarefori/674919" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/akhbarefori/674918" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
