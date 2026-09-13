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
<img src="https://cdn4.telesco.pe/file/hJBRH9lDJyOGbC8Is5ZAGJ_QGXwnkWVkOleCh9R574s3MBNs1gNTq85WNP5SqWFMuhVzkzuCP283ERNJtgwgU_zixbaq66ifZSaXY8mD9vFMiDERmB2Rzfbsxk9gc5mUIUU9mKW8NLLENO0dZACWcDiQpfA5E28gakk86J96Y2Hh1abZM2rtVH1Nja35BtJ2-GiADNTHluZiVqFxZNh1lS8_RFcp0lvFWdlWY0vf1rvIrv_VT2KgljvbIyrxQEoXKfr1VWJ4c45KAR42PyQtuyBL_hxhO4nmk7ds7pnwn5HfSxB3gQGiuhfEo1-PXZXsE83ahS6V5DsD4mpJUqOwHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-461807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام بانک‌ها کجا رفته؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/farsna/461807" target="_blank">📅 16:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکار سفیر سابق ایران در مالزی برای دور زدن محاصرۀ اقتصادی
🔹
زاهدی، سفیر سابق ایران در مالزی: محاصرۀ اقتصادی ایران در غرب،  «پروپاگاندا و هیاهویی بزرگ» است و اجرای چنین طرحی عملاً امکان‌پذیر نیست؛ چراکه کشورهایی مانند چین و روسیه با آن همراهی نمی‌کنند.
🔹
دولت باید با استفاده از مسیرهای جایگزین، به‌ویژه فعال‌کردن ظرفیت سفارتخانه‌ها، تأمین کالاهای اساسی و دورزدن تحریم‌ها را دنبال کند؛ حتی اگر این مسیر هزینه بیشتری داشته باشد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/farsna/461806" target="_blank">📅 16:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح برای دفاع از دین و میهن هماهنگی‌های لازم با نیروهای مسلح کشور انجام شد و مقدمات مورد نیاز برای آموزش و سازماندهی ۱۰۰۰ گردان مقاومت ملی جان‌فدا فراهم گردید.
🔹
در همین راستا از همهٔ علاقه‌مندان دعوت می‌شود در روز سه‌شنبه ۲۴ شهریور از ساعت ۱۷ با مراجعه به سامانهٔ
janfadaa.ir
یا ارسال عدد ۱ به سرشمارهٔ ۳۰۰۰۱۱۵۵ در دوره‌های آموزش نظامی و امدادی جان‌فدا ثبت‌نام کنند و در قالب گردان‌های مردمی جان‌فدا سازماندهی شوند.
🔹
فعالیت‌ها و اقدامات جان‌فدایان برای ایران آینده به‌زودی در سایر حوزه‌های مورد نیاز دفاع از کشور اعلام می گردد.
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/461805" target="_blank">📅 16:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن چه بلایی بر سر پیمان مکه آورد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/461804" target="_blank">📅 16:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفت‌وگوهای سازنده با بانک توسعۀ بریکس داشتیم
🔹
چشم‌انداز بسیار خوبی جهت سرمایه‌گذاری، تبادلات مالی و ارتباطات اقتصادی شکل می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/461803" target="_blank">📅 16:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/461802" target="_blank">📅 16:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حمله به تاسیسات هسته‌ای و زیرساخت‌های ایران در بیانیۀ نشست بریکس محکوم شد
🔹
در بیانیۀ بریکس تجارت با ارزهای ملی یکی از عناوینی بود که تاکید شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/461801" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند.  @Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/461800" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnDqYl9a4Vw6XS2QTSo7Biwv2-WvRsUrFqbDbSA8hrA-26MRVE6Afmx9UTD69GynukLz9qEfNtRa1NbjyvNeR0UJXYroklINDAdDU-XtZv2RhRCycia8z7hOpaGMnsAmB2tqUmJmjItsK6I46u_wNQaApF99SZgPf7kVmZOdgV12dAXZPWdEOFCILto3rU_q-r5ZPrCZ5iH4vvKYV9IpmlHtEW017PwkG8ac40cXZihNHpiA3GVbYFYIGX97jZFfZK-JKhS01A9AguGlDeZFwvrkF5Uazxp385GfjFwzbPWcouyWYkTUtL5FvIirEKAtufBBAUi3ipFpb2pshVRc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر از جنگ‌های قبلی عمل خواهد کرد.
🔹
کسانی که تلاش می‌کنند استمرار فعالیت های فناورانه و خطوط تولید و کارخانه‌های تسلیحاتی کشور را صرفاً یک روایت یا تیتر  رسانه‌ای جلوه دهند در میدان به خوبی توان نیروهای مسلح ما را  دیدند انچه بعضا به نمایش گذاشته می شود بخش کوچک از توانمندی واقعی و ظرفیت‌های موجود در صنعت دفاعی کشور است و این مسیر همچنان با قدرت ادامه دارد.
🔹
امروز ایران قوی‌تر ، متحد تر و بیدارتر از هر دورۀ تاریخی خودش است؛ توانمندی‌های دفاعی و فناورانه کشورهای نیز متناسب با تجربه‌ها و آموخته‌های حاصل از میدان، مسیر پیشرفت و ارتقا را طی کرده است.
🔹
آمادگی کامل برای مقابله با تهدیدات وجود دارد و این آمادگی کاملاً از جنس توانمندی‌ها و راهبردهای مستقل خودمان است؛ جمهوری اسلامی ایران برای تأمین امنیت و دفاع از منافع خود، متکی به اراده، توانمندی و ظرفیت‌های بومی خود است.
@Farsna</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/461799" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ga8Y51pBwrA9WQNNYraGLXwmmgPM35VIOx1LzP1tmcj9Oxnl--s7U_nSV-Mbauf3VvqFCYUVe7M1svJOjBB_zolTT93DXZGzUvg9C0-dCHMv7ROLZk2P-JKyoWHvdcN2JAGeoC3fzgaLlH6VKBQJPgHOV7VRSGzzBJwlkypPMilfj19v6HU8ulfvmveScLxTzBWD0cbUIbwb9wwOsMBDXb_lklvme9jGu9RgQT9aDsHQGJ6TQphPKKj8STrl9S9ks6AQIsAy8ekieKPOZhq-W9QtVDpybR1V69CW0oXmzvC-vI-WM78ahIwHR3qA8qEXIrAAoH5s2-5LPNKn_3xduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhW9a-3wjttNOUf92d57hs5s86FypwQOgLIn1Z46G0TcPGry3KViWncmR6gsBleVeIW99X_Bxy1xKd4hy4k3wpymiqL_Q3W_Q3sv_tgS8IlibaRymT_HWCQ7uVbebieZNN9F3uWsjX6OHrCl1NytSpG5l2ViLlwAundswWevhPzOVn6yhNr9XRe6WHPQtYWxepvsTjCzfUpPXL40HvRa6_oylWIc9vYbOhzWeREj1I5bdkzJpT0AhTSSTKyW2punY9S5WfVLyHjffFZT9ZW9njHsISgXIpCtyj3FI84tmBsthmlx0N4v9VMotwlz6VahV060RXATN0ecDHHq9VCfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQdbi7i55gkiOyoC6am4ekwNm6AY7IYMN-dnshO9qwtVe5JtHq5x9PosOK-I2BoF9EQGhAf6qSxworYfHTB2GKlIOosjNjD5vIJXW1DnpwR_OkREYN_kPCwyXPz1QvIFUexJYcAHfn0NoTQ6LAEjK6lwqE5a1HSBqJlI6BI_D6MK-mholjP7aZwsiXcdMRSgvi2oZeUZmZMghP7iyKb21hRwe8gqZSmYmfvMOb-AzuHmcGMgKWhnw-4aPT9ZMpxROkvEj-rVkVBdZD3qEwn0Kzq6WdD0hEB0xg8-55Veq-YCDg58Y3Z_r9GYVKk5G-xmRdaTmgiBhlp3jVPqzP5opQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3gLoTD0LazPlS4dWxEqp4NpyVxHCXaElVP4oW7dtr1ZKf80XRGRnH7M56Ngls9HGVILa-d7s8rR31-MygofJKlLph_e_lUyeSi8dfXPs5bbRI2H28bq63UAFt_vhbN8Ko_bxeI1Et6WAruZQY71sw30a6kp1peP8IAaONm9tGgJo4x8UKnlRZ-3HAfJBkcjBG-yY4J7gdQFXOFPrGqa_Ix80lmEe90qvWYsURb846oAnU8R2GQ_J5IVfN0A1GuMi3iSNQDKhEj557GFgzX04d652OKQtKLWA7JtUMNuFNqJYkrZIhNwmFCnglB5fd8f8E4vtAzQvVeTbKcooYUDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRN56udsJy265w78BNZiZOuJavHdCz8Jg5gTyf3vVLesuCaHtmF0m6q3R7kYKL7rxnPdFa79jZvXIxKuoBTTXLIsTR1MB__3CeYnJoiuOCB1BQy1dTVipQax1eLWMpJaOTTXm4bhyA5KSEx8sr2xeCaS7BaLRvooFFHG7Hj57j0YW2sVVuCLcbgdQXHiCQnfPrWv3SXYh7B3aQT7MlVbnwDjclz4xkWwUzYeaYtsasLUehp_WL6GcKWxjMnQI4irhk_x9rujJLPjCHbYrj6Gy7I81u6tNi_21tYnhTJ8tlrPoSdeNSQEguny3iJ2Zt_J0N4-cdvPlMxWTxdpeGXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWcBlNEckcxliRgYszOLNvm94xMHwV5oTnZwTRrYazrKLuxqp27C-YB-d2FP9fM3GfDTz9qd3Sgv-f22jc25SOC9iTroS7morTLEqIaiAsXqt-OG5Z4w-LkUICTaZjyxYqX6ByneUwS-qFBcibHtc5lLE6bUSdj0ESTmTUHQEzVU6cbzgE-7WzD8sdRvO4PlzOg0pJrhJLhug_JWDuf5TGin1tYOitUy8MSdBuQw4uGBEu3GMvADvIqGPjXCfnR7RXHuJ99ey7KezJ-NxFp15lGxFn_vPY7L2XmYvNgS5xYL57BrE-D2bHHMaU9tPwFHItCKm51VH9Jjorys_k96jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-gToslejSu8fG0RLX4wXJoafUSisDqOIPc6FKOVmElrO-bNrYtHCuYtxZtMd_-rbiNE8EliXRdsIIFhopjEfRw4FMPHFbNA9FcGOE51YFannTiJZy-e9Lm9YyNgliqf4WyAA0RHf5ZWSviwFdSjgzz_T0xe6B6r9f2eYFExue5ujpK90pGok9aPL3C3UP1OX4M_gWo-DIawqk8-HdAqkvVWmRae330_rJuWAgXkEsH-Du1d88MuY3EOoxB_XjisK7y5CryF-Y_qaDODutaTUR_vB5W0vX02Hwv4ljXvEiUSdJxZhhKqbYgWY6BRgjFw96RImK8dEPrIeAqh5iJ4kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ضربۀ پلیس البرز به سوداگران شیشه‌ای
🔹
پلیس مبارزه با مواد مخدر استان البرز ۳۹۰ کیلوگرم شیشه را کشف کرد؛ در این عملیات ۳ قاچاقچی دستگیر و ۲ خودرو توقیف شد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/461792" target="_blank">📅 16:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/461791" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/461790" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/461789" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trzBB7mC8YCYA7cSSPeNnjKv4LvNjeQt65Isziuq6K4UXzyGUgjhTrEiJj6_tv__i0EklBBnEDuW4To31Vh_tunf4Zpg57Qt6i-GqXJarIAbLtc_Z1EcZIgxcA6AXMhMXO6pJ8cU1LI631hLdXt55R_Yy1j9SDxPasrUM-SfzD_4aPEB5qmvD7TFMAb6fec2YBjFzVxzv_IBMUXlQIOVuk2Z9q3-xE917L8JnSMi2Z0Z5g0QyjEQ2EK1FvqiashVTlMC1ZecKKdZnNdxHeyZO02jasCd_qLaHRiMpGpYn5Q8P50XexcAe7Ci1CP866vFzKCLT1iS2ZaC-DfAs-zx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات از تکذیب هشدارش به نتانیاهو خودداری کرد
🔹
روزنامه عبری یدیعوت آحارونوت گزارش داد که از امارات خواسته شده بود اطلاعات مربوط به هشدار محمد بن زاید، رئیس امارات به بنیامین نتانیاهو، نخست‌وزیر رژیم اشغالگر درباره عملیاتی که شهید یحیی السنوار، رئیس جنبش حماس در نوار غزه برای پیش از ۷ اکتبر ۲۰۲۳ طراحی کرده بود را تکذیب کند؛ اما ابوظبی از این تکذیبیه خودداری کرد.
🔹
این روزنامه عنوان داشت که امارات تنها به پاسخ‌های دیپلماتیک بسنده کرد تا در اختلافات داخلی اسرائیل درگیر نشود و تأکید کرد که «اگر امارات واقعاً به نتانیاهو هشدار نداده بود، قطعاً این موضوع را تکذیب می‌کرد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/461788" target="_blank">📅 15:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپن دست دوم را هم از ایران برد
🇮🇷
۲۱ | ۲۴
🇯🇵
۲۵ | ۲۶  @Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/461787" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809653adc8.mp4?token=hi82Ghm8AfsA5tmdXiTeVNbNdPkVd-09LW3Cev7VSJnE_Vr3lEgEq7XvH9wPCiAnioySNfK2K8xxnQUvQh0PRQyL_Wov5cEPB4Psc8GbzUlE-vFuED-VeO8v9qhK05vJlk4crNmfjNncgZzYH5k7qip0rNGrpufawP-aKFMpRbPhulNAuitThV-6RDDsH5TdINGc73C9Ro3RWuTQ_vl_ejcn7_bPFjHzkhnJ51cxwYJeoHNaHeL5KneqA2wOphUxQh5cqVc3atFgRyaGKI29O7LJUEWYixQZfyJhoaPnTvf53oj7vZgezc9ewluTofCk9FEmemz24mBshCDYheC5fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809653adc8.mp4?token=hi82Ghm8AfsA5tmdXiTeVNbNdPkVd-09LW3Cev7VSJnE_Vr3lEgEq7XvH9wPCiAnioySNfK2K8xxnQUvQh0PRQyL_Wov5cEPB4Psc8GbzUlE-vFuED-VeO8v9qhK05vJlk4crNmfjNncgZzYH5k7qip0rNGrpufawP-aKFMpRbPhulNAuitThV-6RDDsH5TdINGc73C9Ro3RWuTQ_vl_ejcn7_bPFjHzkhnJ51cxwYJeoHNaHeL5KneqA2wOphUxQh5cqVc3atFgRyaGKI29O7LJUEWYixQZfyJhoaPnTvf53oj7vZgezc9ewluTofCk9FEmemz24mBshCDYheC5fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/461786" target="_blank">📅 15:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d825e7a2dc.mp4?token=rqp20yZBwemS2LUGZqEK-p8cD-Dnq6_g4_svCTLGkmRksOQ-fyEJxP5IQa7C-S6w6K-gJhf9gOXUk8gr-RAwDzrfZeRwnMA23nxIU3LixAZEKQlF8X5m09AOSej9T1Z4jBNI7ISVJwyhPTfFF6wCd42-fkh5PSmkWjWiUAAlmWedqHAl7omSgqnBd4Xtxyc2Y-xg0crgacG8om6KEN1xWYt8VTWoyQqk_TDvtA5AnAVIoZNSrF_rLPK0feFsrE9O7eW9-nr0SaX7duFHeI3RFMjCPbOd-6PTJMJ8a6Ajdlxb29ZUBSepVnAN5jcThi--zvUHGHX6uPYGtGaFd630uqKBo1Fi-aIBA2XzhaIe5IGvZMBQJ3V31ln7aQ7wDwGXQB6yRyWbMwAazcUCnW9Cp9hsVrgH8bmqpMmeoV2m0ngUn-CjR-GCEG4bSf91zOk-jwKf8O2KJtIt5_wZewZjVx2-msvBAjGmG7u5OoutcYYSffyym_A5Hh4n_H3u_c_u2RgkiG15ifjWQLB7hnsVMcHNWNkEQ_3VM0P9D_v06FM9SqRuwOkRXonh39mOYudBplNhV2g1AWqnvG7n1ENVfiLWyPJElGycFHIGOoVxulZ9x1y6oPuEtu_InmVG5fCfzasQJlqdAHJMN4p_LDXScbAz4Gt0Ov_ghTKVxDsCkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d825e7a2dc.mp4?token=rqp20yZBwemS2LUGZqEK-p8cD-Dnq6_g4_svCTLGkmRksOQ-fyEJxP5IQa7C-S6w6K-gJhf9gOXUk8gr-RAwDzrfZeRwnMA23nxIU3LixAZEKQlF8X5m09AOSej9T1Z4jBNI7ISVJwyhPTfFF6wCd42-fkh5PSmkWjWiUAAlmWedqHAl7omSgqnBd4Xtxyc2Y-xg0crgacG8om6KEN1xWYt8VTWoyQqk_TDvtA5AnAVIoZNSrF_rLPK0feFsrE9O7eW9-nr0SaX7duFHeI3RFMjCPbOd-6PTJMJ8a6Ajdlxb29ZUBSepVnAN5jcThi--zvUHGHX6uPYGtGaFd630uqKBo1Fi-aIBA2XzhaIe5IGvZMBQJ3V31ln7aQ7wDwGXQB6yRyWbMwAazcUCnW9Cp9hsVrgH8bmqpMmeoV2m0ngUn-CjR-GCEG4bSf91zOk-jwKf8O2KJtIt5_wZewZjVx2-msvBAjGmG7u5OoutcYYSffyym_A5Hh4n_H3u_c_u2RgkiG15ifjWQLB7hnsVMcHNWNkEQ_3VM0P9D_v06FM9SqRuwOkRXonh39mOYudBplNhV2g1AWqnvG7n1ENVfiLWyPJElGycFHIGOoVxulZ9x1y6oPuEtu_InmVG5fCfzasQJlqdAHJMN4p_LDXScbAz4Gt0Ov_ghTKVxDsCkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی زیبا از بازگشت صیادان مفقودشدهٔ بندرلنگه‌ای به آغوش خانواده‌هایشان  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/461785" target="_blank">📅 15:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ea1595f8.mp4?token=YSsVPWZJ2n2q3MKM7IU7UfWzlMxhaynzdc4TozcgMGxqnog8g6P-W0JCS05qbI82oWc-C8UDCjDZm-6seGzBjxfSyM2VGuGXu3rII_0C2p33HQkBnLDRnPY0yDKBukCX6YD6qP3_dRr0OSszUGk7Txbg4Gy7feewhkyVvwuJaed29tzhGQ9HoHQE3KReT-7AUO_A5P0Bw9_90zfMnS_CxO_sds9CznK2eLT9aqW4VZXmZLaC6zLOxBHb2d0V2PFAp2PRFawsd02Vpi8zO4vqEXnkNMDxdHxEgVkjcR-43fzdzwQO9pLg7CTtRm-TIhM3lP4QDBwVuz4f5gS-iTWECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ea1595f8.mp4?token=YSsVPWZJ2n2q3MKM7IU7UfWzlMxhaynzdc4TozcgMGxqnog8g6P-W0JCS05qbI82oWc-C8UDCjDZm-6seGzBjxfSyM2VGuGXu3rII_0C2p33HQkBnLDRnPY0yDKBukCX6YD6qP3_dRr0OSszUGk7Txbg4Gy7feewhkyVvwuJaed29tzhGQ9HoHQE3KReT-7AUO_A5P0Bw9_90zfMnS_CxO_sds9CznK2eLT9aqW4VZXmZLaC6zLOxBHb2d0V2PFAp2PRFawsd02Vpi8zO4vqEXnkNMDxdHxEgVkjcR-43fzdzwQO9pLg7CTtRm-TIhM3lP4QDBwVuz4f5gS-iTWECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین جلسهٔ رسیدگی به دادخواهی مردم برای جنایات جنگ ۱۲ روزه
برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/461784" target="_blank">📅 15:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3d048989.mp4?token=q3sE4SpU_ZPfxesnbglyh4b4Rb3_x6AfK7-qawbQPCsuet6J0PwgA77q1LGuYhJPtQGm2CGe5-En8DlCs23qXFNSao3b1j_RhEWijKbzBf5wY7QpcS3WylLMrFFFdc3Fs2CnOXkh848faPQegNDtCo9tFslAXSpupJ-MshJMEnxkzOYwsDbKgnU62Ysv2RFGaTBwFKqCCXDMMlJbsYdB7QWz-G8A6slCJ95ZPkks1ApFjtJFnc3afj3XaoTUtM2TnoX8wB3TEHLkYybRPXGwsi66XYKbZnYNPfnNWxm6AFjeUfaaJdBcxvddcya3twhNGUNl7X0fM7I4KA5O-coRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3d048989.mp4?token=q3sE4SpU_ZPfxesnbglyh4b4Rb3_x6AfK7-qawbQPCsuet6J0PwgA77q1LGuYhJPtQGm2CGe5-En8DlCs23qXFNSao3b1j_RhEWijKbzBf5wY7QpcS3WylLMrFFFdc3Fs2CnOXkh848faPQegNDtCo9tFslAXSpupJ-MshJMEnxkzOYwsDbKgnU62Ysv2RFGaTBwFKqCCXDMMlJbsYdB7QWz-G8A6slCJ95ZPkks1ApFjtJFnc3afj3XaoTUtM2TnoX8wB3TEHLkYybRPXGwsi66XYKbZnYNPfnNWxm6AFjeUfaaJdBcxvddcya3twhNGUNl7X0fM7I4KA5O-coRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ربات‌های پست‌چی مشغول کار هستند
🔹
با جایگزینی ربات‌های هوشمند در پست به‌جای روش‌های سنتی، سرعت پردازش و تفکیک محصولات پستی ۵۷ درصد افزایش داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/461783" target="_blank">📅 15:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPoK9-lIz8CUfkN1vu1Qu-LCrkTi-M5lmeQKeYynwvyRzQmfvE-TojXu5-4BtFQsDzmVAM5WGzuf-4bT0zxptoKvu8GOarEuto1zE0fbw5O4gzbY_oJUos7EEA240TdPMiv8fKktMDw9fRW_S1uI_fOiJSDKnfQ5OyK86GAEevT4RyJvjlWXLJp_9b6zIynRkrkDeB-vsN7RlmD4XUIkpnBTz7ufO1uNWnj110tpSIbCMOxTz8pzODUltG_j2daHisx8cSIz9-r-Zhy9al2JFkqZ9POfaG57_YtKIXB7gXOQs8ziS0OMp7aqJ2MIFqqzp5oY1kaFA1_EYaQ8gGblyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۹۷ درصدی تردد در تنگۀ هرمز
🔹
برخلاف ادعای ترامپ که مدعی است «تنگه در کنترل است» آمارها کاهش ۹۷ درصدی تردد نفتکش‌ها در تنگه هرمز را نشان می‌دهد.
🔹
آمارها نشان می‌دهد که روز جمعه ۱۱ سپتامبر تنها یک نفتکش از تنگۀ هرمز عبور کرده درحالی‌که سال گذشته در همین زمان ۳۱ نفتکش از این آبراه عبور کرده‌اند.
🔹
حالا اقتصاددان آمریکایی استیو هانکه می‌گوید «به لطف رئیس‌جمهور ترامپ، تنگۀ هرمز عملا و از هر نظر بسته شده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/461782" target="_blank">📅 15:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e242469d8.mp4?token=W5IhgdkbmZ-QxuQUH8NxubjJo2ykqfvsrabUiyjN-BNRnoHx84NfKkjyMj5XzIq9dXlYmdvPg3xi3DfaO8THDCpQn0Meq1Jo9jP51cZKI2qKMm-BBaqVHJBMBdtQE74FGQWE9aAeCmT9vcAqZgExa3yDdYcJS5xVQTCeLwaVWcd5IuyosbZbiowEdzMvAyp-g2oIbVIiT_tTciabJViti25MqnImUTNfmIK02IvpLEwxJ35pTw-KFJRJ7CPwMe80ruOD0Hy9aESJZxSr0TAjHZgB2qpCIw2rwH8DlX4oWUH4ZU5nL-Jq5tWUcxbuILlS5TBWnxMw7_chmoIHcLxnLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e242469d8.mp4?token=W5IhgdkbmZ-QxuQUH8NxubjJo2ykqfvsrabUiyjN-BNRnoHx84NfKkjyMj5XzIq9dXlYmdvPg3xi3DfaO8THDCpQn0Meq1Jo9jP51cZKI2qKMm-BBaqVHJBMBdtQE74FGQWE9aAeCmT9vcAqZgExa3yDdYcJS5xVQTCeLwaVWcd5IuyosbZbiowEdzMvAyp-g2oIbVIiT_tTciabJViti25MqnImUTNfmIK02IvpLEwxJ35pTw-KFJRJ7CPwMe80ruOD0Hy9aESJZxSr0TAjHZgB2qpCIw2rwH8DlX4oWUH4ZU5nL-Jq5tWUcxbuILlS5TBWnxMw7_chmoIHcLxnLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ امتیاز پیاپی پوریا حسین‌خانزاده مقابل ژاپن  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/461781" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793dbe983d.mp4?token=pQMix4KK-PLNpJYk2H7fvcrl8m8kuoyX9blDiAu7JZpLwmftqtZeNGHFlYHPcrvYWq2AFuaH8cHp4XYqqvfYSpuRcJtvLiWp2if-O6tSOSfDoysYJSnE_2-eXP7htnzaCMcBAUFgvZbZ_CpW8bfn48lCTNpcgJoFXmyV_K87RDn293_KpYm2cTeE8YXsi11FZA_W7VmGy-_hO1ANtP-kI-0ttZuILVIW1YFTe9r4rfI4lVYUj9YnUxz80OakZ-X5HNx5NxaVti62tw1CRWOXiyfqkFTCdLdCkkfa8iBYiPkW2tn_izLBckbyOJfG61HcpifJXE910ONPTJRgyvZ13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793dbe983d.mp4?token=pQMix4KK-PLNpJYk2H7fvcrl8m8kuoyX9blDiAu7JZpLwmftqtZeNGHFlYHPcrvYWq2AFuaH8cHp4XYqqvfYSpuRcJtvLiWp2if-O6tSOSfDoysYJSnE_2-eXP7htnzaCMcBAUFgvZbZ_CpW8bfn48lCTNpcgJoFXmyV_K87RDn293_KpYm2cTeE8YXsi11FZA_W7VmGy-_hO1ANtP-kI-0ttZuILVIW1YFTe9r4rfI4lVYUj9YnUxz80OakZ-X5HNx5NxaVti62tw1CRWOXiyfqkFTCdLdCkkfa8iBYiPkW2tn_izLBckbyOJfG61HcpifJXE910ONPTJRgyvZ13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازسازی پل‌های آسیب‌دیده در جنگ ۷۰ درصد پیشرفت داشته است
🔹
مدیرکل مدیریت بحران سازمان راهداری: در مجموع حدود ۶ همت به‌ پل‌ها در جنگ خسارت وارد شده که تاکنون ۲ همت اعتبار برای بازسازی‌ آن‌ها اختصاص داده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/461780" target="_blank">📅 14:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf247b98d2.mp4?token=NaIs4efcx80DlxavSccbY8tOW8qINj_8Czg8og8SL7lQfuEJ1pyzViT4tn6nFyx6adNPAyJHxphnXH0jS1zm_1uRBIbDmlT7P1GMaFeykv6ZirAgrABfvCRE2YQNmrQiIu5mxmdq4F5vKRzH8MN8NgZ0V-evQPtDP1WSAS6RJ8Jdy842x3upvWXr--lmP_2vJlQTove3zEwhxoVS-vhS4xfBSGiXJeUEXjvcA39eT45329gHqVs7iycYFifPY0VtBpFoeGtaX8tfyShx5tcQ3Eltre6niNnnFv0Chpgnj-vTUGWQTOXd0YVdTNINaYx-4AMSJ9upgL7wL2sGkRtVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf247b98d2.mp4?token=NaIs4efcx80DlxavSccbY8tOW8qINj_8Czg8og8SL7lQfuEJ1pyzViT4tn6nFyx6adNPAyJHxphnXH0jS1zm_1uRBIbDmlT7P1GMaFeykv6ZirAgrABfvCRE2YQNmrQiIu5mxmdq4F5vKRzH8MN8NgZ0V-evQPtDP1WSAS6RJ8Jdy842x3upvWXr--lmP_2vJlQTove3zEwhxoVS-vhS4xfBSGiXJeUEXjvcA39eT45329gHqVs7iycYFifPY0VtBpFoeGtaX8tfyShx5tcQ3Eltre6niNnnFv0Chpgnj-vTUGWQTOXd0YVdTNINaYx-4AMSJ9upgL7wL2sGkRtVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپن دست اول را از ایران برد
🇮🇷
۲۱
🇯🇵
۲۵   @Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/461779" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116b60a2d8.mp4?token=GxoNl-Uz_9RALk3tJ39DuqXA6onUNsXu2FQn1eS6B5QO6edITAuSAThFAlHNfByA4cF8MUVV3pF_4DUArxPnqD8l-89pJ7pflvUP0q4ju9Ksz5QVMnqy6YbEGc4Fl8XHaTWbRjrNab9uYI9afe6604v1NcAIyBTFE9lADWi8UkYj42bCFgey9wjHD5R1w2fUN1OeEzj1dI6KjmyCfuS0ceIRs2F90EoO0KNOaJiN0p0V1498ErAzffdvA9mTWMYPOqAOXXqJjAzsg1ZK5DSFVu8k-Y8HbhHO0O31n8x4Fnv3X92h67dYUsc7QePox5aZSDW8BtSaVrQPnKzlbqjz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116b60a2d8.mp4?token=GxoNl-Uz_9RALk3tJ39DuqXA6onUNsXu2FQn1eS6B5QO6edITAuSAThFAlHNfByA4cF8MUVV3pF_4DUArxPnqD8l-89pJ7pflvUP0q4ju9Ksz5QVMnqy6YbEGc4Fl8XHaTWbRjrNab9uYI9afe6604v1NcAIyBTFE9lADWi8UkYj42bCFgey9wjHD5R1w2fUN1OeEzj1dI6KjmyCfuS0ceIRs2F90EoO0KNOaJiN0p0V1498ErAzffdvA9mTWMYPOqAOXXqJjAzsg1ZK5DSFVu8k-Y8HbhHO0O31n8x4Fnv3X92h67dYUsc7QePox5aZSDW8BtSaVrQPnKzlbqjz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشنهاد روزنامهٔ عبری به جوانان آمریکایی: با ایران بجنگید تا بدهی‌هایتان بخشوده شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/461778" target="_blank">📅 14:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiRCH395-P4-C5_kr09IkuLml_YyckQNopJjYHzPuJewWOBN0V3ik8C0PY9iibNNfHQcfn25_342ZtKlWE52xF0CRCoDAWA1CZhrSC-hhfIoi_j1KFb2P8u-LbLUIMqTtQcrU_moyE4b4aubyAO6zt4s95o15W4jYcnhh9UhlEFKSEElei179GsjRcZ9dLmq2m8rQPdOlvyndAC2Vaaa9NCIxaED6C3cryTN_TLXnCgCTTi0Gqq9nhNjwC2KP7ZyTi9Km67eDKjD2E9HCXOIW8vk0yh40c0QJ-F0rL2rwgJtXCIZec3x3xhE2ERDwyyQBSTnnOni1emAWrwc8_Fk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/461777" target="_blank">📅 14:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0932c80.mp4?token=WaxVZ1SH7LGF5k8Wdk21PwksHJ7g1vq5hDITfC_om7CDJYo32pXUBDWgu97Avn1InwHdeHbRPvRafiWaPTKOmf0wwlTZ6lJrE9C6wWeNJXdyOdw164qsIQGNUTYAsyBV5mGqF6miAsbuAps8s3-IUvgNc_97Pu-xhyt17l_GKlHM4bTMyZrSuRH2QRvIpRS0XVx1-jfgmRy7TV4cuemkfiJ4tt7HnZCeaciJHLK5C8MLYCSuXo93ga4dt6fAysQucTaO3-6r_dhPMdYR0XARp-vDIgokeVKwfpbx-0HHAdXh3WgjUZZAeXTov2tMFR7HRBRvD8IxqULFnqwlYyo6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0932c80.mp4?token=WaxVZ1SH7LGF5k8Wdk21PwksHJ7g1vq5hDITfC_om7CDJYo32pXUBDWgu97Avn1InwHdeHbRPvRafiWaPTKOmf0wwlTZ6lJrE9C6wWeNJXdyOdw164qsIQGNUTYAsyBV5mGqF6miAsbuAps8s3-IUvgNc_97Pu-xhyt17l_GKlHM4bTMyZrSuRH2QRvIpRS0XVx1-jfgmRy7TV4cuemkfiJ4tt7HnZCeaciJHLK5C8MLYCSuXo93ga4dt6fAysQucTaO3-6r_dhPMdYR0XARp-vDIgokeVKwfpbx-0HHAdXh3WgjUZZAeXTov2tMFR7HRBRvD8IxqULFnqwlYyo6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمنی‌ها معادلهٔ جدیدی در سواحل غربی رقم زده‌اند
🔹
رادارهای پیشرفتهٔ آمریکایی را که عربستان به مزدورانش در یمن داده بود، تحت کنترل ارتش یمن در آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/461776" target="_blank">📅 14:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72852729b1.mp4?token=bq-Df72EKb8gGNIkvCP1BvJNt3s9IFNIeb_loKrrwhx0zHq-x3FRcnYpyaGBSFAjSqOJiqFJYMJGKviltucHIdA4R_HNR3rwjAa2vZCJLWnM4va-hJ7JhYS1i8gDdnmvRF4I1-w4ZgCEERrzlz_Jd0VBbJu_2KNUQsFPaMx4hu8cHW3U8fSZv0TmsmXspDgRTM8-tHk2N8cGin3UgaImivCBhgFU9GZer7BbJze1PKvrKPusYcfhMDAAIb34sQIbuScfCP2Fnc5vBJ8-uSes_S5ttrqXjK4it1nFdInJNPOmT9woZGUKa5wfDt_WVOCS0aeGdbNZ3AgmC3cY3bDtzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72852729b1.mp4?token=bq-Df72EKb8gGNIkvCP1BvJNt3s9IFNIeb_loKrrwhx0zHq-x3FRcnYpyaGBSFAjSqOJiqFJYMJGKviltucHIdA4R_HNR3rwjAa2vZCJLWnM4va-hJ7JhYS1i8gDdnmvRF4I1-w4ZgCEERrzlz_Jd0VBbJu_2KNUQsFPaMx4hu8cHW3U8fSZv0TmsmXspDgRTM8-tHk2N8cGin3UgaImivCBhgFU9GZer7BbJze1PKvrKPusYcfhMDAAIb34sQIbuScfCP2Fnc5vBJ8-uSes_S5ttrqXjK4it1nFdInJNPOmT9woZGUKa5wfDt_WVOCS0aeGdbNZ3AgmC3cY3bDtzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب تیم ملی والیبال ایران مقابل ژاپن
🏐
فینال قهرمانی آسیا
⏰
ساعت ۱۴:۰۰  @Sportfars</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/461775" target="_blank">📅 14:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75af81f13.mp4?token=KB-5pgjOws0INSwIfxPEFfvj6_grxlC7K0ZZ9pnhzIrQXcxDHJMnsEWR1w_8C4tNRUKdqPbsBA0Xh7HhoT0CcmB5efB-ij8Nr8E5wUMuSHwsLavJ53EAGhV76oxrJQGI6euVmPTDZqPLVVQT5XzTIATiFPEbRGUzb2eyVmgjvDIat7ErmfNLtRrjtQIT8g9gr68jVTwhYJI9phOXLKml_n_w1SbGAIoaL_dIbNp0UnVWvSjU7zWTJ6d1fISYOSHh9x5ypttwwCWDi8XcXOIRg4M4HoMtNZ6BVvMGYzE6qzRWdOxj_wAhfTvw0Df_Ikce-6KHjt3SIGZOGyI7NNal852jWQyNh2uTiWh2M93eUb8ZSgn-7kF6caUfSWyNWZhBXJEq4Q_a_MDNjMH-oPrgPm5d71R8ijgKpzBBK11_kjfvoZazLuHrq7zQju1_otXkmXcjwWLPBYUqxejMdfVBHIgmWccXP0X8J6D-gP3vAvkELBLHmBSsSbUvPEiVHUi83VgUFMhNFIGXPOolYTOmZGwKJd_8NVI6o-KOynKBdimy36N_Cm4_lVZOUrM4CHppb8lrZ0cgGIvqiBMEG_YQux4FQvk9-ou6AtYyFlEpMoTy1klUFr_wP7M4zrd_pUFuTfTGhXM9ceP0FdtVycN26HWvqf41cARC7EwW1S2t2Z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75af81f13.mp4?token=KB-5pgjOws0INSwIfxPEFfvj6_grxlC7K0ZZ9pnhzIrQXcxDHJMnsEWR1w_8C4tNRUKdqPbsBA0Xh7HhoT0CcmB5efB-ij8Nr8E5wUMuSHwsLavJ53EAGhV76oxrJQGI6euVmPTDZqPLVVQT5XzTIATiFPEbRGUzb2eyVmgjvDIat7ErmfNLtRrjtQIT8g9gr68jVTwhYJI9phOXLKml_n_w1SbGAIoaL_dIbNp0UnVWvSjU7zWTJ6d1fISYOSHh9x5ypttwwCWDi8XcXOIRg4M4HoMtNZ6BVvMGYzE6qzRWdOxj_wAhfTvw0Df_Ikce-6KHjt3SIGZOGyI7NNal852jWQyNh2uTiWh2M93eUb8ZSgn-7kF6caUfSWyNWZhBXJEq4Q_a_MDNjMH-oPrgPm5d71R8ijgKpzBBK11_kjfvoZazLuHrq7zQju1_otXkmXcjwWLPBYUqxejMdfVBHIgmWccXP0X8J6D-gP3vAvkELBLHmBSsSbUvPEiVHUi83VgUFMhNFIGXPOolYTOmZGwKJd_8NVI6o-KOynKBdimy36N_Cm4_lVZOUrM4CHppb8lrZ0cgGIvqiBMEG_YQux4FQvk9-ou6AtYyFlEpMoTy1klUFr_wP7M4zrd_pUFuTfTGhXM9ceP0FdtVycN26HWvqf41cARC7EwW1S2t2Z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها ۴ شب تا ۲۰۰ تایی شدن میدان‌داری ملت ایران مانده است
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/461774" target="_blank">📅 14:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa721fc17.mp4?token=hSa3uknicgx4Y9t2wrT1aR8CO0NoGjKojRQYUH7BNwpn8E4w3Y1UhYkDug3INEQvgcbFWHZLzYRbO9wfuyiIX3m1nqNPeNGGypwbNTGRHpiy3_lm61Eo6exQhC7beFt24BWjUtWsoA5BuJdp5AwlUKCi4uE5RCvtaDspINyLoXF760c_ZBLCDfVr_TiHGjaolrtQu8_Aw_QYv1wwV1MvgMqA4aueBQXDeTNv0nxIyGxkfHhSCEu8GGhPNf63RpA4Wn8k9Sz_fOQKATZ5QyVreZdiheRdpmD-5JGCMFdw_axKTIO6VCtcvahU19Vdzghrem7nE5XiWzHHo1TvN9iJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa721fc17.mp4?token=hSa3uknicgx4Y9t2wrT1aR8CO0NoGjKojRQYUH7BNwpn8E4w3Y1UhYkDug3INEQvgcbFWHZLzYRbO9wfuyiIX3m1nqNPeNGGypwbNTGRHpiy3_lm61Eo6exQhC7beFt24BWjUtWsoA5BuJdp5AwlUKCi4uE5RCvtaDspINyLoXF760c_ZBLCDfVr_TiHGjaolrtQu8_Aw_QYv1wwV1MvgMqA4aueBQXDeTNv0nxIyGxkfHhSCEu8GGhPNf63RpA4Wn8k9Sz_fOQKATZ5QyVreZdiheRdpmD-5JGCMFdw_axKTIO6VCtcvahU19Vdzghrem7nE5XiWzHHo1TvN9iJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همچنان تنگهٔ هرمز با اقتدار نیروهای مسلح ایران کنترل می‌شود
🔹
تصاویر ماهواره‌ای نشان می‌دهد تردد شناورها از تنگهٔ هرمز بسیار کم شده است؛ طوری که روز گذشته تنها یک نفتکش چینی از تنگهٔ هرمز عبور کرد.
🔸
این درحالی است که آمریکا بار دیگر مدعی شده که کنترل این آبراه در اختیار آن‌ها است.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/461773" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79704f060.mp4?token=Wy8ZQzX8zA8I_hSpHdlwWxESHPBeobavnzcFpq_sUwx6HN76HHXAVHuBmDDfbz56SQpqJjNUyPlxOT0BwWCmqqHZ4MuyWWUxN_hR28KuDeJubZ-Sj4MoRrO6NtN_B_nswA93qMngeWlHBU68TXc-EtyfY0TNdy2cg4wIX3hgaYEMV9Ua6k7FFbKtU4ywC2SMho5ZXckn01vB6sYG5Px3kG9IjgQEYDzaIgNIdf6VnKeKVWDT58MxWL4EjJ2-ZpxEZcW6X-SFCX_1uLe9ubaZQDqyifWRNAab0RcYa-sZHngugEmAneDiUjP3LPdtp8uZAFo0TdwKrb5NV3JACLhDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79704f060.mp4?token=Wy8ZQzX8zA8I_hSpHdlwWxESHPBeobavnzcFpq_sUwx6HN76HHXAVHuBmDDfbz56SQpqJjNUyPlxOT0BwWCmqqHZ4MuyWWUxN_hR28KuDeJubZ-Sj4MoRrO6NtN_B_nswA93qMngeWlHBU68TXc-EtyfY0TNdy2cg4wIX3hgaYEMV9Ua6k7FFbKtU4ywC2SMho5ZXckn01vB6sYG5Px3kG9IjgQEYDzaIgNIdf6VnKeKVWDT58MxWL4EjJ2-ZpxEZcW6X-SFCX_1uLe9ubaZQDqyifWRNAab0RcYa-sZHngugEmAneDiUjP3LPdtp8uZAFo0TdwKrb5NV3JACLhDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/461772" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POtwToMm-nM5I_Om5fxUhZz9_Xjzza0r5nSAcHyj5xqhFsdV-uDRNyKKEiyiVh42IMG3Wbqx0Xj5SsFJXdllWDEiL-8sj7e6c5ixrjpANZklTTGMZhMY8gf9ted2hx7es7mnlPBt1tcajJKEG9EfhyZET8KqOPMUpsd5UE39XKdGV0WcWnmboo2hjs8ST_YGwR2S8SF-bjBMDsFJH0FfnZVEuUlp6CQfXqmaXpfkI915Rb4oRAtyy4TAd-q8cFvYeAAt_D3WDo3p0YUGl7UgP9hPRJ9PZT7eBCiW-Y44NlNo2wMgBK8LhIcgetbdjO7DlCv1ow7rHfkBR8G7ZDPuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم ملی والیبال ایران مقابل ژاپن
🏐
فینال قهرمانی آسیا
⏰
ساعت ۱۴:۰۰
@Sportfars</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/461771" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVnurcCvJZQpJjtdoPrm_szc45cgScP4K_ojSenkyqPTsp5sbQK8ye5U-15PKAjgUOm3woyqwUtuAor3mcRiQ_NopICD3QD5BQo7K9p-Gg-vf5XR82vopZ5UqLkmkQ606QM_L3ONPfavRolVKPEJxflKderGpulPjVeJfiRj3japkXTijqq_q9u0yZ6aHnWn0yTTR4-WSzjm4A-sXA5UFf2vvNPGKpVvakrvIN_hsnvLGCeQxBudjzrwv8Ye_ranVmTtEl252QalsJCtUqls4ySYlpRF2lFYqHFo_c0hBLR-dlJYf4zyVhFxpU3k9n9Pg-UZnFunvevxs-4hluc6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف
۱۶ سلاح و ۵۲۲ فشنگ جنگی در یاسوج
🔹
فرمانده انتظامی کهگیلویه‌وبویراحمد: در بازرسی از یک مخفیگاه در یاسوج، ۱۶ سلاح، ۵۲۲ فشنگ جنگی، ۲ بی‌سیم و ۵ دوربین کشف و ۳ قاچاقچی دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/461770" target="_blank">📅 13:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f7a2729e.mp4?token=mFzOHBEwrrkiqwqApCdFj5M0VQThbBgL1E7zNZD0bgDtl5de2YaaDkVYP3YhurO5pUBOucU0YLMwqQwnV_hYMC_x76ue_L0ldt3iqh4449b7gmKa3Ylsnj4YCNT2OLEqM2PhmNkKFAEHguNscapaX_N2QMsMQhGnV2IV6xjH-k6dtzqkzyiheqfadtgnMefjHcz_pZfFaE3w6l62rHgzOoUHr-TEuBB33kns451H05KDqLPYzq8xf2x_s8F0Mokm1sCVfmm_lv8y-0z1nDTdDBaPZOXt9mPpFgeohQ7JAtF8n5iqpBVF5WKqp7fKMqc4AEAe9s8C8bnFtiWQZuAtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f7a2729e.mp4?token=mFzOHBEwrrkiqwqApCdFj5M0VQThbBgL1E7zNZD0bgDtl5de2YaaDkVYP3YhurO5pUBOucU0YLMwqQwnV_hYMC_x76ue_L0ldt3iqh4449b7gmKa3Ylsnj4YCNT2OLEqM2PhmNkKFAEHguNscapaX_N2QMsMQhGnV2IV6xjH-k6dtzqkzyiheqfadtgnMefjHcz_pZfFaE3w6l62rHgzOoUHr-TEuBB33kns451H05KDqLPYzq8xf2x_s8F0Mokm1sCVfmm_lv8y-0z1nDTdDBaPZOXt9mPpFgeohQ7JAtF8n5iqpBVF5WKqp7fKMqc4AEAe9s8C8bnFtiWQZuAtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اداره‌کل بنادر هرمزگان: ۴۴ هزار و ۸۴۴ تُن کالای اساسی از ابتدای امسال تاکنون در بندر شهید رجایی ترخیص شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/461769" target="_blank">📅 13:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwgqA_eV8LSRe37MRkZjTqVbOYvcllZDsssHMRheP7TEpqpHvVx9P-GFdKhE_b9B29Z3C21y-z-eM079kCzVkfjEvKavpucJiMrdAava7oVo-z-4goTJzYdSKqn2u2R_-mky2TpAa7MMwsw4P3lMF1etWi_gRhv2T32LXTA9DL-c_p9OCvBHcXKdIcozHNRrwSbKoK_CRzbvJLr2TWsW52X3W0KCnHqqob81y9TJS88uI-YENfSQQjtypSYHjgu6dX2nWyvB7jy4PBlAXt1BPa2lxq-9i91422LNucYLtIrWVJeL-Zcgiz0sWfwazBnFIeQI0MrIt1HcqLUw9yYrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار ساری برکنار شد
🔹
حسین احمدی در جلسهٔ استیضاح شهردار ساری با کسب آرای تمام اعضای حاضر در جلسه، از سکانداری شهرداری ساری کنار رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/461768" target="_blank">📅 13:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c3b99d9a.mp4?token=IvOTW6ckYHgrlwx4NLkLdhmMRakyg4bapdI5jR4VUYDW7tfQuR8OCgDyusJEgJkm4eTO0r51-M_JfWrXnnuvcE4UEoRVQR26c9mqRjPuozPpGxftMEeph7abHfuXeK_ffMjKM-iADkvS6BvKzsWhejYQCQuq0ur9XIkDlLnJg__AF4zp0HYvX8UsTn9aNk9JgQjjXQrWzel402FRIpQflNFdtJIat16iyIBvwq7BWeE6neJnIrvcWX2sZlK-jSvuG_Q-SJ9R4rAJnBmryHEdO9-8HW3lp0DkBNKByd5fHxkx5sXwX04U9MbeuFjBkw8SV7PH_HawOM3eF5UHUg9pAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c3b99d9a.mp4?token=IvOTW6ckYHgrlwx4NLkLdhmMRakyg4bapdI5jR4VUYDW7tfQuR8OCgDyusJEgJkm4eTO0r51-M_JfWrXnnuvcE4UEoRVQR26c9mqRjPuozPpGxftMEeph7abHfuXeK_ffMjKM-iADkvS6BvKzsWhejYQCQuq0ur9XIkDlLnJg__AF4zp0HYvX8UsTn9aNk9JgQjjXQrWzel402FRIpQflNFdtJIat16iyIBvwq7BWeE6neJnIrvcWX2sZlK-jSvuG_Q-SJ9R4rAJnBmryHEdO9-8HW3lp0DkBNKByd5fHxkx5sXwX04U9MbeuFjBkw8SV7PH_HawOM3eF5UHUg9pAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ روسیه به ۸۰۰ متری مرز ناتو!
🔹
همزمان با تشدید درگیری‌های روسیه و اوکراین، پهپاد روسی به یک کامیون در فاصلهٔ کمتر از یک کیلومتری مرز لهستان اصابت کرد.
🔹
این تأیید رسمی پس‌از آن صورت گرفت که انتشار تصاویری در فضای مجازی دربارهٔ سوختن یک کامیون، منجر به انتشار گزارش‌هایی مبنی بر احتمال ورود پهپاد به حریم هوایی لهستان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/461767" target="_blank">📅 13:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK5nJ0hcCJsJ4BOiBkVYntDHY4aQ8B0SR5RkiWSeiTxfn_JzakumNw11XhRsFfqxAEOQTW-sZV0z1_3GsBdhYzNEsdL_hCGBGRh43HeXzGKI_Ig21B8J3ZdyiAyar1eXdod98BBLlJ5jr5yFZ-1aOunWI4Aa24o_qkwDs66FVJ0XeknSBPLPPAridOz9-OuxzUm56KrBzqq9ZxxlSF6f0iFEjZx7tpoR0vaJ6WDHIot6gBH_lm3-lhNP3hRYSaRwFSxRv-agjEoTfJKJcZP_HVJrAFx1lETvvgLW6AzFTToWBbcu_1Fru-uvM6cDkp2ooShfxCrlfxj_9ohIEkL_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به یک‌قدمی ۷.۵ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۳ هزار واحدی به ۷ میلیون ۴۳۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/461766" target="_blank">📅 12:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs2AM2MTYVWJ7kTwIfL3JZ5aQmWqTs_YQQc4a6TP9Es5lSVTRO3WUpuzSXHFoGGL9H7ReCtbbazmrglMilYOVkg9gqeasWc0ko63pF0nBD42-gj9LhfVA-8EGvv4AnOMn0d5wKQJg6197nMojUjXBApUQxUfFYU5GXNtyGdG_dhZgJajGoUPB4ATAyi7kszNUSLZKcdlCTO8Dg9LWeSBSoyaMJuqLG0XXCQxrPh2XSHvqURJndTmM-Oi3cGhNa_YgxmYSPC6D1niMuWVNK2ztH0yYdhOUD9j28yyIZvq2TaIE1e1vfUEdDV2d8nE3XLnmZ3NLN-IKDs3J6p6b_VgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون برنامه‌ریزی شهرداری تهران: در بودجه‌ای که پیش‌از جنگ ارائه کردیم، قرار شد ۸۵ درصد هزینه‌های مترو از بودجهٔ عمومی شهرداری تأمین بشود
🔹
کل درآمد پیش‌بینی‌شدهٔ بلیت‌فروشی مترو در سال ۳ همت بوده که فقط حقوق کارکنان مترو در ماه ۱.۲ همت است. امسال برای پرداخت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461765" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52ec2e915.mp4?token=KFESwG7FGBUy9X5Xr06Vdym-8wU8QMZhkblFSSvV5lBl-4QS9NMZ8A9gWzX64Mzrpn0WHdcGbErQmHPHYR9mYesbduvBCHguWW6ZhbQATJISpMxGPWHclsbOa3OofXI1A5omlLeBeap0JMeYqUXPLPRN-eontaxM9NDDkw62qnTbrP6m1GDdacj64p8z59uuaeeL5cXQ-eigV4Q2wqFHsO3JUpmkWLamRYLYSVvMSpZKROUidtMS-uiJtgdNLbVJ0dgoTtUoiPKJJwyMN5VeU1UWfpWlAAZ1gt4tzOwKHvBxGyjuTWjqWYgpJhAE0NfRbEzPSa1xqXRU8TGkjcDBLJ19xeOA31KV65dAoeQG_xYOpZ_660HmBzqJep1dCWk7-yrO6w3UQJF0xwSuC4Ub3dEIANdDK4QzN7FmueKgcbw0NFmcgdk3sW9JneT62UP91WnhOOFXxXsUZnvwSoJ6I3KpfZXH7XdtzxjbTfBX4LtQ9bMx-Me9oDGASRgZ0u8RlofAvzH4pJ6SglQbSV0l253ZfzvCrkpIu7Vl4_mkO7d0cIRXBT6-CUy3j8lYHuad6ZOyAJBBdcjrDgZKzC-1BzLKMXJ4ylFHBdDR54sZwrgcy0kJsCdbWXNWVDO1cKNXbj6mXORTc34NJRzdKwfymJt43t_0uORFFIusfRr6BiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52ec2e915.mp4?token=KFESwG7FGBUy9X5Xr06Vdym-8wU8QMZhkblFSSvV5lBl-4QS9NMZ8A9gWzX64Mzrpn0WHdcGbErQmHPHYR9mYesbduvBCHguWW6ZhbQATJISpMxGPWHclsbOa3OofXI1A5omlLeBeap0JMeYqUXPLPRN-eontaxM9NDDkw62qnTbrP6m1GDdacj64p8z59uuaeeL5cXQ-eigV4Q2wqFHsO3JUpmkWLamRYLYSVvMSpZKROUidtMS-uiJtgdNLbVJ0dgoTtUoiPKJJwyMN5VeU1UWfpWlAAZ1gt4tzOwKHvBxGyjuTWjqWYgpJhAE0NfRbEzPSa1xqXRU8TGkjcDBLJ19xeOA31KV65dAoeQG_xYOpZ_660HmBzqJep1dCWk7-yrO6w3UQJF0xwSuC4Ub3dEIANdDK4QzN7FmueKgcbw0NFmcgdk3sW9JneT62UP91WnhOOFXxXsUZnvwSoJ6I3KpfZXH7XdtzxjbTfBX4LtQ9bMx-Me9oDGASRgZ0u8RlofAvzH4pJ6SglQbSV0l253ZfzvCrkpIu7Vl4_mkO7d0cIRXBT6-CUy3j8lYHuad6ZOyAJBBdcjrDgZKzC-1BzLKMXJ4ylFHBdDR54sZwrgcy0kJsCdbWXNWVDO1cKNXbj6mXORTc34NJRzdKwfymJt43t_0uORFFIusfRr6BiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ تماشایی بازشدن دریچه‌های سد کارون ۴
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461764" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
حملات عربستان به استان‌های تعز و صعده یمن
🔹
خبرنگار المیادین گزارش داد که حملات هوایی عربستان منطقه الربیعی در شمال‌غرب استان تعز و شهرستان مرزی باقم در استان صعده را هدف قرار داد.‌
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/461763" target="_blank">📅 12:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PokXQAFjukwpekKUKJwWkWgdgB2MCPH48FR7JN5l8-90RGxWDFpmGJzOA5EwiBIiDo2JmvtWzSidJltzZ0HTzGUfOi1gniU09Rww84wFUyJFvQUmnmoRWp7vPowKMMvMCcy8FXCpW8bxAXRRdjI6tZbVfjheoo6FgDFMTIEFXy-VerLm4sxEl3eZwGLDScQGAprlw_50HRp3_DmEe2dWa0Z8WDAXcXGVtXYyV0CXHZUA5fzgVcx8UeQGQsCVVM_-jghz0N3ao1Bj3gBEBHxlHs-DJ-61T3ycr2OnYml3XrIcytpmQUCatLYY9Vin5IumzHh22rXb0lT80N5aIoYAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف ژنرال آمریکایی به آسیب‌پذیری ارتش مقابل ایران
🔹
«جیمز پی. آیزنهاور» فرمانده فرماندهی تسلیحات ترکیبی ارتش آمریکا در اعترافی کم‌سابقه، حملات ایران را عامل تغییر شیوه عملیات ارتش آمریکا دانست و گفت واشنگتن باید پس از سال‌ها اتکا به پایگاه‌های امن و متمرکز، دوباره «پنهان شدن» از دید دشمن را یاد بگیرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/461762" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1cefead0b.mp4?token=klkkwLBtYV1airDIJ5DW2MVOjqNDIpCkkQvV1UMGmvO-TAS4vbF8A8dLAG-8rIQHD2nogub5SFyYMJMGI6GT9rx8vT9ffL6b0T25GOCFJxammia6aCqlnWB9cwW8t1PROPfuqylvcIdJ-qrjZMMcUKCukiAYogBFnhZ97wjFrt1jjikvXWL7jVI4kAhG4rsfqdV-xXdCjPdnIxYB1_p7AD5DAutUDOCbX1dHVw08ctjTbbbytrdhCzgB0WafpUOms_2yj84uGKf_lrMlCi5u3P-mnlhTQpz4Xa1tn3KdC94PWtkXZasAFpHxVcD_ZhGKEEVYLbZ7p0zdypz9uTIVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1cefead0b.mp4?token=klkkwLBtYV1airDIJ5DW2MVOjqNDIpCkkQvV1UMGmvO-TAS4vbF8A8dLAG-8rIQHD2nogub5SFyYMJMGI6GT9rx8vT9ffL6b0T25GOCFJxammia6aCqlnWB9cwW8t1PROPfuqylvcIdJ-qrjZMMcUKCukiAYogBFnhZ97wjFrt1jjikvXWL7jVI4kAhG4rsfqdV-xXdCjPdnIxYB1_p7AD5DAutUDOCbX1dHVw08ctjTbbbytrdhCzgB0WafpUOms_2yj84uGKf_lrMlCi5u3P-mnlhTQpz4Xa1tn3KdC94PWtkXZasAFpHxVcD_ZhGKEEVYLbZ7p0zdypz9uTIVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون برنامه و بودجه شورای شهر تهران: رایگان‌بودن حمل‌ونقل عمومی هیچ آسیبی به نوسازی نمی‌زند
🔹
هزینهٔ بلیت مترو در بودجه صرفاً برای هزینه‌های جاری مثل نظافت استفاده می‌شد که این هزینه امسال پرداخت شده و مشکلی برای تأمین آن وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/461761" target="_blank">📅 11:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWOhtoRwpG1boWLJizTzOwKM1dHfagTFsNasZKSwMJOMZ6qvqOiYclUnZpHYm2fEsKt8fpJUkc9zKD5PgJZo8sM-xtZNv7cb_Z9ZOeXAAZiY4zIvQkveeFfv6r8bIM1a8W5qekuuThDwV8iu1L8U_v9YvioopSbny-jtdEvixVN_2pl5_1RUxN8H020-qoFMyx0rx6h24QIYBzzh7C3mileKvwkFzEsajS8K00r9IWdvpo7AF2Uf5zFYHp9f3wSeYqBIHrI-fOJTiKiDp6DemIBoMoECODAUNw1pLX4hw2XjSdEYfXbNVI-oDrKIvh8MCe_4L2TU7o51BbEkCXUgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمان‌پرست: هرمز و باب‌المندب آمریکا را به عقب‌نشینی وادار می‌کند
🔹
سخنگوی پیشین وزارت خارجه در گفت‌وگو با فارس: پیشروی انصارالله و تسلط بر بخش‌هایی از نوار ساحلی و جزایر مشرف بر باب‌المندب، معادلات منطقه را تغییر داده است.
🔹
جبهۀ مقاومت اکنون از طریق هرمز و باب‌المندب بر دو شریان حیاتی انتقال انرژی جهان اثرگذاری جدی دارد.
🔹
فشار هم‌زمان در این دو گلوگاه، هزینه‌های اقتصادی آمریکا و اروپا را افزایش می‌دهد و می‌تواند به رشد بیشتر قیمت جهانی انرژی منجر شود.
🔹
آمریکا به‌دلیل شرایط داخلی و افزایش قیمت سوخت، آمادگی تشدید درگیری را ندارد و در صورت تداوم این وضعیت، ناچار به عقب‌نشینی و بازگشت به میز مذاکره خواهد شد.
🔹
اگر دولت هم‌زمان با اقدامات نیروهای مسلح و جبهه مقاومت، مشکلات اقتصادی و معیشتی مردم را مدیریت کند، گذشت زمان در جنگ تاب‌آوری به سود ایران خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/461759" target="_blank">📅 11:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIhGsmxIKZwO_h6lWp-1SDhXhxXsJpMjibsvM0XikrAje4W8R5U-p38dztECbwtOWDBRp_oJzR5KGNDfZnGdcQgjh75BlQCaGI8XKVLOhGjT3PZ5CTs1Yw0Os6_CdjcSMLP5x5hs1ejXc3IPKNkRO_nObmXxNQBgpJCBOqq4WtKSpFvnXyjJdx7YW8dbziy0hIIj5uoaN3wwuFDUmmHbmayJN0qOlaoB1I3Jqs_OjhpuHWsbHyx32z0rCUE7EkzSWUlrZIHOCpiHDkEHITSfpYyKFRZPOwekrDXmfWd_K_0LmQ8fE7SBdz1qEhFX2e97rgF99uMCQz6UfP5QNZe3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم
🔹
رئیس‌جمهور در گفت‌گو با شبکۀ خبری ایندیا تودی هند: روابط ایران با همسایگان از جمله امارات، عربستان، پاکستان، قطر، روسیه و چین دوستانه است؛ مشکل اصلی پایگاه‌های آمریکا در منطقه است.
🔹
ایران آغازگر…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/461758" target="_blank">📅 11:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82090b4fd0.mp4?token=TqwtvXsUBVbaKZGXrIwcAvo6fdfkPbTggr1NElOWmV8zK17jhL_V-fREhj6GR41xIX-NC66nHQT3CY3gWOPSV3dloUB68rlxgVU5or5YVY4RXoTiWuAFNJN-Zli5iL0fQg71nNtfjxIjSJGRjfGw-1EHOUqCnz-y3mZIAbIHPyKpbsvINPKz8SC0hn6sFcWan0i0ns6dIDrN1bahvuxbLeCqoZ1aKDuzReNupdFYyNvuomsVCZrEy9H4fQoSPnqI68w0xjtfOYGDt4e3Y8z9xEX9I-CdZesMFXeCZvDESc6pHUgBLSzGDnbLusKSA3wGTuDrvg9rX4XDxlN6dBs_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82090b4fd0.mp4?token=TqwtvXsUBVbaKZGXrIwcAvo6fdfkPbTggr1NElOWmV8zK17jhL_V-fREhj6GR41xIX-NC66nHQT3CY3gWOPSV3dloUB68rlxgVU5or5YVY4RXoTiWuAFNJN-Zli5iL0fQg71nNtfjxIjSJGRjfGw-1EHOUqCnz-y3mZIAbIHPyKpbsvINPKz8SC0hn6sFcWan0i0ns6dIDrN1bahvuxbLeCqoZ1aKDuzReNupdFYyNvuomsVCZrEy9H4fQoSPnqI68w0xjtfOYGDt4e3Y8z9xEX9I-CdZesMFXeCZvDESc6pHUgBLSzGDnbLusKSA3wGTuDrvg9rX4XDxlN6dBs_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمران: مترو و بی‌آرتی تا بررسی مصوبهٔ جدید رایگان است
🔹
رئیس شورای شهر تهران: لایحهٔ جدید حمل‌ونقل عمومی رایگان در جلسهٔ آیندهٔ شورا بررسی خواهد شد و تا زمانی که مصوبهٔ جدیدی در این زمینه تصویب شود، روند حمل‌ونقل رایگان ادامه خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/461757" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در دماوند
🔹
سپاه استان تهران: انهدام مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۶ امروز در دماوند انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/461756" target="_blank">📅 11:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4de85f3.mp4?token=ZXoHC7oOUrvhWBMu63mues5kbnGGQBxKniw_U_cf5cgFkgXcx2-fI8RWCsmHLU_TBZD50DSQYFX8oVSojXznvS6_Kpu7jGaIPg62MF6LAcNOpLwYllaWzI7eJIvmU5zt5yvG0uBjlzNrZ3zXB0qXDwf5HocmpXwMxFWWUfGRwFHcWhV14WkON-S5H9ey55N1h3dpe2sowg80JGMCC9NVDyxajb6db4XEb5PwTrwskekVqqJmvN284SwEaPoAK7Abshcq6JlWvPerPEriyh-U9vDnJXlOcyxPg6QNYoCDgrhGirBoDNxu1GVxzVwpzkZiZM-rXQ9-mF9K3tGlJyDllw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4de85f3.mp4?token=ZXoHC7oOUrvhWBMu63mues5kbnGGQBxKniw_U_cf5cgFkgXcx2-fI8RWCsmHLU_TBZD50DSQYFX8oVSojXznvS6_Kpu7jGaIPg62MF6LAcNOpLwYllaWzI7eJIvmU5zt5yvG0uBjlzNrZ3zXB0qXDwf5HocmpXwMxFWWUfGRwFHcWhV14WkON-S5H9ey55N1h3dpe2sowg80JGMCC9NVDyxajb6db4XEb5PwTrwskekVqqJmvN284SwEaPoAK7Abshcq6JlWvPerPEriyh-U9vDnJXlOcyxPg6QNYoCDgrhGirBoDNxu1GVxzVwpzkZiZM-rXQ9-mF9K3tGlJyDllw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مهم‌ترین پیام رزمایش ۳۱۳ هزارنفری، مقاومت، ایستادگی، پایداری و خونخواهی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/461755" target="_blank">📅 11:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvx8lNVR_6gO79xPeVf85Vq8XbQr5vubots-7PQrllyrWqVuX_WETqSGx79eEeAUjWPiTvYGGFUQ0XukbBOgrThMNCaJ7riZQnR-AJGPS9hunAdM34SfZWh4uK_iAspUBJVIhGDdB3R3_zkUxLC7JEGpOhXlkU_rKUre2nP5A2lJOylQk97p1sm_OYdvd9AJG1rlDuA3wtrRYdOBH4VMJKYX392OnGqWbKbfS2XeBMbGSFQDmKn_tqeTeMoiMN45UZpa1OIz2vIzTzH9AztwcFFamfe0ocCmxpmNTLaVZcnbDkaBBscv6WxywNuekKXjrGj1Gc-j94-HbhPWynneww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی برای شرکت در اجلاس روسای بانک‌های مرکزی کشورهای اسلامی، راهی استانبول ترکیه شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/461754" target="_blank">📅 11:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8b45019.mp4?token=tPXAmHQuBVcbQaF0TxwVpz90qFUVsBsVdBcnulUZC8dgdch2xG_nvoPR_A4T7J3IHxbpfNzvS_8eFQSnXWowj_EwZZULJCNIBD35pLisJ-fE5Itr4tBuis6E3JsH6OYK0IXFPPRdjL7bV71--HSnhIVDdZSZTTYgJXjsYw_Y9wm7769_R8gpVlRo1DACcswzSW9NiLKtFfepyxqBbXVAhMJNjFZJn5aMb8-tXrMuwVv7msf1DIssNozIs0pNlZX8QeG0anW90hPwRHRoKFNTOD0_M15LYv89osPBX3rr7b4SwJSe0JnOG4OP8hXIRJDOiBsCBi_CO7kGkMuzKVOxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8b45019.mp4?token=tPXAmHQuBVcbQaF0TxwVpz90qFUVsBsVdBcnulUZC8dgdch2xG_nvoPR_A4T7J3IHxbpfNzvS_8eFQSnXWowj_EwZZULJCNIBD35pLisJ-fE5Itr4tBuis6E3JsH6OYK0IXFPPRdjL7bV71--HSnhIVDdZSZTTYgJXjsYw_Y9wm7769_R8gpVlRo1DACcswzSW9NiLKtFfepyxqBbXVAhMJNjFZJn5aMb8-tXrMuwVv7msf1DIssNozIs0pNlZX8QeG0anW90hPwRHRoKFNTOD0_M15LYv89osPBX3rr7b4SwJSe0JnOG4OP8hXIRJDOiBsCBi_CO7kGkMuzKVOxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ملت ما دست از انتقام برنمی‌دارد تا دشمن را از اقدام خودش پشیمان کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/461753" target="_blank">📅 11:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/461752" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbV7wU7E5cNscHfckWfq7jUsnkveQg2FJPatWsTQCah1gTCe5oRN7EogU1sNodwGtieFqAZBkAVtj1PwPWCZWorcMcVYz6VYdtvHGRGj5C-SE6OrJETKxzvOF1tAmivCyGixwO-fDqHlUFkj-C3f9aMXiQf3ZJ1pqfD5gHH1nn4fDXfjVuTAwFO3LLwDvZbu7KxG_dzJTKjFSfZB0ZUxUOLl_QhvXp2QftlQ_Nyn2vhP9YO-iTtn_rcHIZ_YwqqRG0CTIgu3nHPqEedFM0vTJ0ku6xD0xsVj0xAbMzjggnbJS1eeczW9A9_88FwV624cXbR2TDlFH8W01ilDCtqnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: حاضرم در آمریکا با پوتین دیدار کنم
🔹
رئیس‌جمهور اوکراین در مصاحبه با دویچه‌وله از دیدار با همتای روس در حاشیه نشست سران گروه ۲۰ که قرار است دسامبر در میامی آمریکا برگزار شود، استقبال کرد و گفت: در صورت حضور پوتین، من هم حتماً شرکت خواهم کرد. باید باهم…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/461751" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما گردان‌های سازمان یافتهٔ ۷۲ نفره از باشگاه‌های ورزشی و مجموعه‌های هنری و مذهبی و تمام اصناف داریم که برای شرکت در رزمایش ۳۱۳ هزارنفری ثبت‌نام کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/461750" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تا به امروز بیش‌از ۴۰۰ هزار نفر برای رزمایش ۳۱۳ هزارنفری جان‌فدای ایران ثبت‌نام کرده‌اند.
🔹
این رزمایش جمعه از ساعت ۸ صبح از میدان امام‌حسین(ع) و تقاطع نواب تا میدان انقلاب آغاز می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/461749" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/461748" target="_blank">📅 10:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب به ۲۰۰ شب در میادین حضور پیدا کرده‌اند و بزرگترین مولفهٔ ملی را رقم زده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/461747" target="_blank">📅 10:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ صیاد مفقودشدهٔ هرمزگانی به خانه بازگشتند
🔹
مسئول دفتر وزارت خارجه در بندرعباس: ۱۰ صیاد هرمزگانی که در امارات مفقود شده بودند، روز گذشته وارد تهران و امروز از طریق پرواز به هرمزگان بازگشتند.
🔹
این افراد قرار بود ۱۶ شهریور به کشور برگردند؛ اما به‌دلیل اینکه…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/461746" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳:۳۰ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/461745" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شهردار تهران: قیمت گوشت و برنج ۶ ماه ثابت می‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/461744" target="_blank">📅 10:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNORXxGGZC-nQuMrcwEG4wMHsAucHwMFUDsf7mJwNJGxUiSLJynZdawEkLzHt1GlFxtoxC4h47HfN10MUKDNa5bROWBp-0iXZjlfi3tfBy_r56txsbLNldMAc9FLr2GqLlMTJS9C4DzoBKSkpQoQwdelFQmWLXW0EdTRfcBDKF__zqNmqfWLx10i00HHX8rbOgjq5DAkVWHYsphN5gWHgF0EiEIB76D6-Sz9e_u_ZdSrfX1eeBa9RlE3V2DtuK4hTNyZIi3sXi51WDcl9JxYwj5HzlaahyoGrurZfyvdjy6Jyaifw4RVfcegMS79dpp1ZNg0yJl_FJJl9ORahh6iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
بازدید رئیس‌جمهوری از جدیدترین دستاوردها و راهکارهای ارتباطی ایرانسل
🔸
ایرانسل، در جریان آیین «یک ایران متصل»، جدیدترین دستاوردها و راهکارهای ارتباطی و دیجیتال خود را به دکتر مسعود پزشکیان معرفی کرد و همزمان ۹۴۶ پروژه ارتباطی ایرانسل در ۲۱ استان کشور با حضور رئیس‌جمهوری، به بهره‌برداری رسید.
🔸
این مراسم، با حضور رئیس‌جمهوری، وزیر ارتباطات و معاونان وی، مدیرعامل ایرانسل، جمعی از مدیران حوزه ارتباطات و خبرنگاران، در قالب «خانواده ارتباطات»، ۱۶ شهریور، در سالن اجلاس سران برگزار شد.
🔸
در جریان این مراسم، رئیس‌جمهوری از محصولات و راهکارهای فناورانه ایرانسل، از جمله سرویس eSIM، سامانه فوریت‌های اداری «فواد۱۲۸» و سامانه مدیریت هوشمند ناوگان حمل‌ونقل و قفل هوشمند، بازدید کرد و در جریان جزئیات این راهکارها قرار گرفت.
🔸
در این رویداد که با هدف معرفی و بهره‌برداری از مجموعه پروژه‌های توسعه‌ای حوزه ارتباطات برگزار شد، در بخش پروژه‌های ایرانسل، ۹۴۶ پروژه ارتباطی در ۲۱ استان کشور، به نمایندگی از مجموعه اقدامات ارتباطی ایرانسل، به طور رسمی توسط رئیس جمهوری به بهره‌برداری رسید.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/461743" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdYGW3p9n2_rhSG5nfx2kiu3Ki7KfGffIEXflTQktVIOzzHEO15iCWsBjhu5mdEHcLnAstZVrxAV_ToJ_TK87SKusfCtGVnTz7o-pm7FvRhvVz4S0hi_05YAxcIWh6IwZkPbz6haLTOADQ_ry592iJeg8P75pRO1UQRMc5LF-FyJKMT2IRVl7jgVac5fvPWxI-y4Aeq1JrhEsd3CfE4jh4hsUxPGH_3TzQqT0fOGVpi7e2UrQcw99pLheXtQfDU9riT3oC3e_PHz9y0XjwUo8bwDF9re6RChxurh0tgHygcGCqWvfFb0Y9korGf6qKY4uhLTD9da2MNm9QjBuxeowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همزمان با ثبت رکورد ۹۹٫۷ درصدی تراکنش‌های موفق
سهم بانک کشاورزی از تراکنش‌های شتاب در سال ۱۴۰۴ به ۸ درصد رسید
🔻
بررسی عملکرد بانک کشاورزی در شبکه پرداخت الکترونیکی کشور طی سال ۱۴۰۴ نشان می‌دهد ۹۹٫۶۸ درصد از تراکنش‌های ثبت‌شده بانک با موفقیت انجام شده است. این امر در شرایطی محقق شده که در همین بازه زمانی، بانک کشاورزی ۷٫۷۸ درصد از مجموع تعداد تراکنش‌های شتاب را به خود اختصاص داده است.
🔻
جایگاه بانک کشاورزی در شاخص تعداد تراکنش‌های شتاب که بیانگر مقیاس فعالیت در شبکه تراکنش‌های بین‌بانکی است، نسبت به سال ۱۴۰۳ یک پله ارتقا یافته تا نشاندهنده روند بهبود موقعیت این بانک در شبکه پرداخت باشد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/461742" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/461741" target="_blank">📅 10:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNpIspWXy49V79tOGsWJgkj5zZZfCcxRiBkJyB5_9ZoIloVcGG0FiE3BT130z6LFAGAfNuOAdLwIUTmXaaligJSRqXY8Xg5ZNCPTHqzPb59UU5JNXDQE_d3VYFuJelg5T1m3gR0hCtEhim5-QCgsLgnjGL31CDyHvndr1q-Zp1v0arP6VH1x9tXcM2F_4BJn_RFJJbX4joVHlRfSe5aGZouPCkEZHigpuPMT6IvJgwnRivynEuEIjQt6Bf1gxSD81RpcFEc3tJroYsjv8gC_SYSyMXIbq9Q5vhx-xlyK0eqwWPcrFxeZeTNkQizkY4c6rs1E9X9deB9cZ8Geriz4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم
🔹
رئیس‌جمهور در گفت‌گو با شبکۀ خبری ایندیا تودی هند: روابط ایران با همسایگان از جمله امارات، عربستان، پاکستان، قطر، روسیه و چین دوستانه است؛ مشکل اصلی پایگاه‌های آمریکا در منطقه است.
🔹
ایران آغازگر هیچ جنگی نبوده و تنها در برابر تجاوز آمریکا و اسرائیل از خود دفاع کرده است.
🔹
ایران به ان‌پی‌تی پایبند است و دنبال ساخت سلاح هسته‌ای نیست و برای گفت‌وگو در چارچوب قوانین بین‌المللی آماده است.
🔹
ایران به‌دنبال جنگ نیست، اما با تحریم، بستن راه‌های دارو و غذا و فشار بر مردم تسلیم نخواهد شد و تنها راه، توقف تجاوز و یک‌جانبه‌گرایی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/461740" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی اصابت کرده، مشخص نشده است؛ بررسی‌ها دربارهٔ جزئیات این حادثه ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/461739" target="_blank">📅 10:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/461738" target="_blank">📅 10:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
مرزهای چذابه و شلمچه در چه وضعیتی هستند
🔹
ساعتی پیش مرز چذابه برای اتباع عراقی بازگشایی شده، اما هنوز خبری از بازگشایی پایانهٔ عراق به‌سمت ایران اعلام نشده است.
🔹
با اعلام استانداری خوزستان مردم فعلا برای تردد در بخش تجاری و مسافری به مرزهای چذابه و شلمچه…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/461737" target="_blank">📅 09:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uELaHKmOoUGPo68gWKdXNpgEflsqI5bIV85AaPyCjGbGCDOkN5Mh1HdpXdGtFxyHPMNtMqt8bJU-7Yi-F_hfvdjZXXM9YySxXDeoYxwIZPZ1TDPn2-w7GJxlYCUy5akLBlmS0VG0tNqJnlNTCWwxTBOk9UtlMV2qV_twsVRwSBhqQJDbmQTpL2baGtJaelm4w_R55bB1jxjcacFUVvxcMzF9HhBgBUSlHQD7XFB7kAOTaHJC29WWFts9T0Vxfmh9jwgexAB4mxS5KvpEeme5dlx-kDAu7t9wo05pcPmcUuGsoTJhCR6URcXwR_ccq1FdGA4mFpycbo-8lWtnubq0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصویب طرح ملی توسعۀ هوش مصنوعی در شورای نگهبان
🔹
سخنگوی شورای نگهبان: طرح ملی توسعۀ هوش مصنوعی که در مراحل قبل اشکالاتی داشت، با بررسی مجدد شورا تأیید شد و قانون ملی توسعۀ هوش مصنوعی تصویب شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/461736" target="_blank">📅 09:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461735">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67371947d.mp4?token=bGQfO6nn4Bo97G29tj3FF5_AtQXOB6UjQM32_IfKeMXKvujKKxXTHqjobM2HgWahkBJqHI1cbdRXNS-0NgrG-JDqJkYel0y7eGJq6mGVFGjbvTPcHch1denIh-dWsWDy9WzMgZz_aWMDR-6ges1mQBJ5VZgQPlj0u4QCQxYyc-nk0UkpHvNfzrOWk6aQ2CHNN28yV4vTzwnGpBzbpuRI9bgtWxNkJe-lIaNoo5RBr01ohqToSI-Ox-u7Gngaxo0s3x8kzUQ-vS8vQfocZ9MkuL4wx8wQ0eaFh1jngOTxe64Yx26Ya_5s1WVGOFJ2jX7hvTHflTIrdSU1rcdapONV8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67371947d.mp4?token=bGQfO6nn4Bo97G29tj3FF5_AtQXOB6UjQM32_IfKeMXKvujKKxXTHqjobM2HgWahkBJqHI1cbdRXNS-0NgrG-JDqJkYel0y7eGJq6mGVFGjbvTPcHch1denIh-dWsWDy9WzMgZz_aWMDR-6ges1mQBJ5VZgQPlj0u4QCQxYyc-nk0UkpHvNfzrOWk6aQ2CHNN28yV4vTzwnGpBzbpuRI9bgtWxNkJe-lIaNoo5RBr01ohqToSI-Ox-u7Gngaxo0s3x8kzUQ-vS8vQfocZ9MkuL4wx8wQ0eaFh1jngOTxe64Yx26Ya_5s1WVGOFJ2jX7hvTHflTIrdSU1rcdapONV8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/461735" target="_blank">📅 09:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWIr4mQbqPF8ClHq-EFMrxz71G-gjiJs9Vlk0jk-y2kuQYZfzuZjG02iun09UIbiqj6OXoOEN6cJg4z7yBEUfqmjYZ1oaA_zrXIvH4lz5YmHJKdPWd2C3mYusl7cdbNaA5e0BAsS8tDG-S9qaVpFYdmkYks89zAU6ht7PlGUilO2jB4fJ5L6UvK0iTGN_6IifjGHorZ2QIBo7PtZVBb9I4xwTgNq9NOs40x8UUiO1QP3l-P4rRd1liD7HhdOQyHysOpcPHJeKfqJ2LUqckKg4P7wXMNf6Yl7F-YkbLf2YIA0MiXlIECsriXNFbeo5DQT3aFYBddl9vqgT41sZKMjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fff5ddec2.mp4?token=BzC51TYHhm-nkeL88iJMFdB9hkPuv-p9T9x7gstsvKJ3wZAJPB46qHVFnTEr-29nNrAAGyPeQPwgCGrXzbOL_wQvphTpJs894pn6OeMQnTVn8lGV5z7SCZcsZ8mwG_ibcEOXXtP3R3WJIi9LypO4VSSQbmSKJYNgpQ-bfQRBymXKM4Q2KeCKBPAedne38wryvrbM3wksT6UYp_rMlLplL8Vs7IujrfWO_j58qygUgsrlV0gP3RndlhxLyHeCbA3HxkxCwmmbkUd1l6emTyajdrde49FywEHCYwyxqGEGxZQSk1BMQZQatUTHzlcIJpiE1X7Th16DSXqJGdQhB7WgpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fff5ddec2.mp4?token=BzC51TYHhm-nkeL88iJMFdB9hkPuv-p9T9x7gstsvKJ3wZAJPB46qHVFnTEr-29nNrAAGyPeQPwgCGrXzbOL_wQvphTpJs894pn6OeMQnTVn8lGV5z7SCZcsZ8mwG_ibcEOXXtP3R3WJIi9LypO4VSSQbmSKJYNgpQ-bfQRBymXKM4Q2KeCKBPAedne38wryvrbM3wksT6UYp_rMlLplL8Vs7IujrfWO_j58qygUgsrlV0gP3RndlhxLyHeCbA3HxkxCwmmbkUd1l6emTyajdrde49FywEHCYwyxqGEGxZQSk1BMQZQatUTHzlcIJpiE1X7Th16DSXqJGdQhB7WgpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ امارات مانع خروج صیادان بازداشت‌شدهٔ هرمزگانی شد
🔹
نمایندگی وزارت خارجه در هرمزگان: اجازهٔ خروج و آزادی ۱۰ صیاد هرمزگانی که از اواخر مرداد امسال در امارات بازداشت شده بودند، دقایقی پیش لغو شد.
🔸
قرار بود این صیادان ساعت ۱۳:۳۰ امروز از فرودگاه دبی به میهن…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/461733" target="_blank">📅 09:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozab2T8nnYABcQqbIEE4fvzHWaGULHiLC_HLjtyjzhEj5ZBKZXxaDTO-YJXycHs8JAT-6C5YPt7zmi6RMH5eREb9qBkkjt-O2hG8Riqq8Lz0WWgCAh8Q2dVvkSiY-_PfKCxvRZD4QQtJ0_nGGx7j4IGJEOkuyBmRX5bW3SJZg8kN0d7gcuW6ESuLjjRzJ1yx7auKxbtppoydMN2w_CNCkn3xZwDQ7aQhjvSS-weXENTvksP-kClbu1q6AsDEBQTYWRfoNFe1JsUCbFeSKPBVT5BYVfp-Pj1kNGfZTMYPY1e9pasYh0AmRCnt46114DxFYQlCSGXREFxmOAZaybZE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/461732" target="_blank">📅 09:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b558ee41.mp4?token=hxt_r8jYq23CXTYgJA2aiQG8bkI-byLZ2WcXROQ3Bg2TaMUysY7DFaDlY1dZCvOVW9ekTavZoBXd5getq-NWDBMpYjFafJMCwXt5i2mzCx9hYkkUy6wbuFJQeGyk--m9sX5uL6k97lYzXhnc-RncId2MQUsMjOg7qRUkTe7IvMl76ZzW00-nBFdQ9MnhV4Dzoy5EvJOVuSpIBucfn73Tl8iIzbpyE-8femWCaPv9jc58IYE1_tUpKltBsYd_74Hxf9aKnL99ANOY0I7qgjfqmfE532gmitOld7N8fLv0tE92XbbHB8H0HiTzdn4WflVG9NOCj2Dde0DLf3vicNbzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b558ee41.mp4?token=hxt_r8jYq23CXTYgJA2aiQG8bkI-byLZ2WcXROQ3Bg2TaMUysY7DFaDlY1dZCvOVW9ekTavZoBXd5getq-NWDBMpYjFafJMCwXt5i2mzCx9hYkkUy6wbuFJQeGyk--m9sX5uL6k97lYzXhnc-RncId2MQUsMjOg7qRUkTe7IvMl76ZzW00-nBFdQ9MnhV4Dzoy5EvJOVuSpIBucfn73Tl8iIzbpyE-8femWCaPv9jc58IYE1_tUpKltBsYd_74Hxf9aKnL99ANOY0I7qgjfqmfE532gmitOld7N8fLv0tE92XbbHB8H0HiTzdn4WflVG9NOCj2Dde0DLf3vicNbzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبار سوخت روسیه در آتش سوخت
🔹
درپی حملهٔ شبانهٔ پهپادهای اوکراینی، مخازن سوخت پایگاه هوایی تاگانروگ روسیه دچار آتش‌سوزی گسترده شد.
🔹
منابع اوکراینی همچنین از هدف قرار گرفتن تأسیسات مرتبط با تولید و نگهداری پهپاد در تاگانروگ خبر داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/461731" target="_blank">📅 09:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2WZGDcVtLL7o0IQ9UPsRnv33pLIOE0x91IInSCICbfw2h7_xSryxJGsoxRFtRxJjThNXvSiB11y9YFtgy4ijlaYfgt2E3tTZMhopqLf_jcGBtVFn4nWSZrUsihc6xjDSfrhV3lKZy32NcwgL2VC46ISGe4m8me2b9tzgyGpKHeTPhH3Lx1aB5SOE14W0ohOE0UBnCsBQt3DVj91slLDLMak-xnOEfEhbBNTw78cTG0UEyBjZu7st40khL_tn2SUvkmJ-Z4GiFSfvgdarvHMjYvxKkEmgwX3Wyb5qw7bALAEjqGKvUqxjuJH6k32E8H-ahcEHS7iLsmk2yCbPiGqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلبریتی‌های اجاره‌ای دشمن
🔹
یادداشت مهدیه شادمانی، فعال رسانه‌ای: «تازه به دوران رسیده‌های هنری» تا پاهایشان به خاک بیگانه می‌رسد، به‌جای همدردی با این همه مظلومیت و آگاه‌سازی افکار عمومی نسبت به جنایات رهبران باطل، برای «آزادی پوشالی» اربابانشان دم تکان می‌دهند!
🔹
وقتی پای منافع اربابان غربی‌شان وسط می‌آید، برای «حقوق زن» یقه می‌درند و بغض می‌کنند؛ اما وقتی نوبت به دختران مینابی و قربانیان بمب‌های آمریکایی می‌رسد، لال می‌شوند! این استاندارد دوگانه، «هنر» نیست؛ خیانت است.
🔹
این‌ها هنرمند نیستند؛ بلکه سربازان پیاده‌نظام جنگ نرم دشمن‌اند که در شرایط جنگی، مشغول عملیات روانی علیه ملت خودشان هستند.
🔹
ای کاش مسئولان قضایی و فرهنگی کشور پاسخ دهند تا کی باید نظاره‌گر باشیم که امنیت روانی جامعه با خنجر این وطن‌فروشان «سلبریتی‌نما» ذبح شود؟ و دشمن را نیز به اجماع علیه ایران تحریک کنند!
🔹
آقایان مسئول! قانون مواجهه با «سربازان فرهنگی دشمن» کجاست؟ بهترین راهکار، مطالبۀ عمومی برای مواجهه قضایی با این افراد در زمرۀ وطن‌فروش است.
🔹
وقت آن رسیده که قانون، «سلبریتی‌های اجاره‌ای دشمن» را سر جایشان بنشاند. سکوت در برابر این خیانت، شریک جرم بودن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/461730" target="_blank">📅 09:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حساب شهریور ایران از دلار نفتی سرریز شد
🔹
درآمد نفتی شهریورماه ایران از ۲.۵ میلیارد دلار گذر کرد. پیش از این در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از فروش نفت وارد کشور شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461729" target="_blank">📅 09:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obc3LHq_HzKwCqL_X-sD9wkof4-tKo4pT15ZmTF3EEDrlDt0ao7Ri9aUdDlsDH5mt_P-Fdunq5Fn9maXBOtOC5iOJ3DC1XXEtDurqspkg14iQTCRPbq_y-d-ZWKC3xi5ZwLB_SCKyFMCmIPAK4QVQo3MgnGhEhJvQ0GVKA2TvQOzU4pNHLdKL94YAICRBPZuQTYwUkuMl2d_r6gTsR-8yaJpFmKe4sMM5hUsqQjJEHamSnpXyvIy0LRJVZ1XdXzr2PKfNd1Wk-rz9gQu8tuzN7_uaDMepYmu8-6hJzvYxeBlU-wi3JIb65obJ6KxlwtuPcZURr5inbmsUTqtPdVirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/461728" target="_blank">📅 09:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4298f547.mp4?token=kTkfuW5li93l0OdFaakYj1J6xLvf_CgOrxURXXEvyqkTZ3Q2KF1vgZY-Haaw5ft_HCedNv-21yNCH_W6uDf4hHnnDV-s3E5OR2BSTOpTirqnoX0huEeW3ukzoi0GszwcEAcNHnSHWevrJFyV8UW296w6-j9zgbu5Qwo13z_Kt7NQrOSBjptceUoMa507X9UJvpYL2rQemO4AC0RF8lwbZsdyALQQuZH5ujtsRQ_0lRId-UEhdA4oMXXTd3-9_qbZ_AZYu8qhnhcstoXX15eKHbFUIwEnfx24DPmGHjq9ZFYqGfbeTSxEP9DG9cAqQq3dn1eHmdrLRLl5BODcfeSrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4298f547.mp4?token=kTkfuW5li93l0OdFaakYj1J6xLvf_CgOrxURXXEvyqkTZ3Q2KF1vgZY-Haaw5ft_HCedNv-21yNCH_W6uDf4hHnnDV-s3E5OR2BSTOpTirqnoX0huEeW3ukzoi0GszwcEAcNHnSHWevrJFyV8UW296w6-j9zgbu5Qwo13z_Kt7NQrOSBjptceUoMa507X9UJvpYL2rQemO4AC0RF8lwbZsdyALQQuZH5ujtsRQ_0lRId-UEhdA4oMXXTd3-9_qbZ_AZYu8qhnhcstoXX15eKHbFUIwEnfx24DPmGHjq9ZFYqGfbeTSxEP9DG9cAqQq3dn1eHmdrLRLl5BODcfeSrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی برای نیمۀ شمالی کشور
🔹
هواشناسی: طی ۲ روز آینده همچنان بارش‌ها در نوار شمالی کشور ادامه دارد.
🔹
امروز در آذربایجان‌غربی، شرقی، اردبیل، گیلان، مازندران، گلستان و بخش‎هایی از زنجان، قزوین، تهران و سمنان بارندگی داریم. به‌سبب شدت بارش‌ها هشدار سطح نارنجی شده.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461727" target="_blank">📅 08:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPCtkw6WDMZo_k_tCgQyWBCLQB3P77NGmuRWnWZapk2lhMmRojluHYtYKnogUqKWCATMslZaSUYChQG-jY2WXAPOLjBxjCJ2eupFeKfnXaOBSpIY_j8LbXjnv3_3hoIOOYsaCQClKaqyk3TuDO-FZPxBOWi_dQr6rmX3X05jnDOwitsuEO5D3V3itu-ivDCyeKTNHBsIy67hw6i0RQ5L6aNIys06o0SwCiEURs_O59x1Z0p5igz6OtwtkpoTab4--na_kTeQSaRIO488RrCWuKpJvAlprXlT6MYrgMUQngDZ4FA-_DF0994qW4N8oAUja6GLZNZ9G3Z34nQMq18Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوان ورزشکار شازندی زندگی‌بخش ‌شد
🔹
اعضای بدن[قلب، قرنیه، کبد و ریه‌ها] عرفان عسگری، بوکسور اهل آستانه از توابع شهرستان شازند، پس از وقوع حادثه و تأیید مرگ مغزی از سوی تیم پزشکی، با رضایت خانواده به بیماران نیازمند پیوند عضو اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461726" target="_blank">📅 08:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هوای تهران در مرز آلودگی است
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۶ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/461725" target="_blank">📅 08:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کشتی مسافربری با ۲۴۰ سرنشین در آب‌های اندونزی ناپدید شد
🔹
یک کشتی مسافربری اندونزیایی با حدود ۲۴۰ سرنشین پس از مواجهه با شرایط نامساعد جوی در دریای جاوه ارتباط خود را از دست داده و عملیات جست‌وجو و نجات برای یافتن آن آغاز شده است.
🔹
تا این لحظه گزارشی دربارۀ تلفات یا زخمی شدن سرنشینان منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461724" target="_blank">📅 08:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461722">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیشب که خواب بودید چه گذشت؟
🔸
ستاد راهبری تحول دولت سیزدهم اعلام کرد ادعای یک بلاگر دربارۀ شهید رئیسی کذب بوده و او هیچ‌گونه سابقۀ همکاری رسمی و غیررسمی در این ستاد نداشته است.
🔹
یک نفتکش هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفت.
🔸
نیروهای یمنی تنها در یک‌هفته ۵۴۰۰ کیلومتر مربع از خاک یمن را آزاد، و در این عملیات ۹ فروند هواپیمای سعودی را سرنگون کردند.
🔹
«طارق صالح» سرکردۀ مزدوران سعودی در یمن در پی شکست سنگین در سواحل غربی، به ریاض فرار کرد.
🔸
تیم‌ملی بسکتبال کشورمان با شکست ۸۱ بر ۶۸ اردن در ناگویا، راهی مرحلۀ یک‌چهارم نهایی شد.
🔹
سخنگوی هیئت‌رئیسۀ مجلس گفت خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای سهل‌الوصول است. در برابر آمریکا صرفاً زبان قدرت جواب می‌دهد.
🔸
معاون سیاسی نیروی دریایی سپاه دربارۀ ادعای ترامپ که می‌گوید تنگۀ هرمز در اختیار آمریکاست، گفت: بسم‌الله! یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنند تا با پاسخ رزمندگان ایران مواجه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461722" target="_blank">📅 08:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLaLYz1Vz5pm4IogJABgp8ACHx6x2vUvOPo18qPdzA6eUWbQMVCfmtX3k6Z_mzho1bVJgo--rvyALYOLO03b_7gwMvXZ8wD76yP-rmHbinGiGSyeNJlT9jj1A2gqvjJzla8mwaZ3V251WMqEdq1bS8R8RKNihrMlTsc6EpKfVp45CrGN1ffRi83RBvUOKz3WeOD7KJ7jHlbpu83PXZP0mi-KoIExS9qG9tQLUnv3ppUu1ZjkIIvevmcO-JU8uiXCztzMAHH3PtYUniPgkGV9UKpX2bjxe7VU5zVp6SccQFTEV-jFMOLx0k_-bBIzJUj8lLveDZDPWDoPQ5AXMPng2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای سهل‌الوصول است
🔹
کسانی که از صلح با آمریکا دم می‌زنند دنبال تجویز و تحمیل نسخۀ تسلیم‌اند.
🔹
اعتماد به آمریکا به معنای پذیرش فریب و حرکت به دامن هلاکت و نابودی است. در برابر آمریکا صرفاً زبان قدرت جواب می‌دهد.
🔹
خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای، آمریکا و اذنابش را تنظیم می‌کند و سر جایشان می‌نشاند و این امر کاملا دست‌یافتنی و سهل‌الوصول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461721" target="_blank">📅 07:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d29d2c80c3.mp4?token=KeXHJ4mPx7BJ-hQbkG-IakwqZdMnyxh-r_0kkufA77grVf0mmxHwoVw4jOZ6hNE-ZrqJxgL_jRAwuA3aJI984bkDrM1tdeaSeMd-GkvrsQgfjFuKi4eNPGlfOLl_RPilHiSKkF1-V1zsqs4mD9d0e23NDJjOlXuvMttg6XIjRYQvdoYfRUEa46ArtA2uDjNmpay2URbac49cgISgpgr-__EhoXCWN6ovU_6XrlYYB-cLleV_PUJJ884yZ8LoAbaVAIZDBbqRRMjDLyKHwNJFazKRG25tTiW-TwOWvg4oJXGq2q6ka7SRm9KmZo9rdqXBBhKZ_ZpjL6UUAWhcLHwB6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d29d2c80c3.mp4?token=KeXHJ4mPx7BJ-hQbkG-IakwqZdMnyxh-r_0kkufA77grVf0mmxHwoVw4jOZ6hNE-ZrqJxgL_jRAwuA3aJI984bkDrM1tdeaSeMd-GkvrsQgfjFuKi4eNPGlfOLl_RPilHiSKkF1-V1zsqs4mD9d0e23NDJjOlXuvMttg6XIjRYQvdoYfRUEa46ArtA2uDjNmpay2URbac49cgISgpgr-__EhoXCWN6ovU_6XrlYYB-cLleV_PUJJ884yZ8LoAbaVAIZDBbqRRMjDLyKHwNJFazKRG25tTiW-TwOWvg4oJXGq2q6ka7SRm9KmZo9rdqXBBhKZ_ZpjL6UUAWhcLHwB6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم آمریکا در ایرلند به آتش کشیده شد
🔹
همزمان با برگزاری تظاهرات گسترده در دوبلین در اعتراض به سفر ترامپ به ایرلند، گروهی از معترضان در دوبلین پرچم آمریکا را به آتش کشیدند.
🔹
معترضان در این تجمع شعارهایی با مضامین مختلف از جمله حمایت از فلسطین و ایران و اعتراض به سیاست‌های آمریکا سر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/461720" target="_blank">📅 07:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیرو دریایی سپاه: اگر تنگۀ هرمز در اختیار آمریکاست، بسم‌الله!
🔹
معاون سیاسی نیروی دریایی سپاه: ترامپ در فضاسازی رسانه‌ای خود مدعی شده که تنگۀ هرمز در اختیار آمریکاست؛ اگر چنین است، بسم‌الله. یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنید.
🔹
آمریکایی‌ها می‌دانند که اگر شناورهای آنها نزدیک شوند، با پاسخ رزمندگان ایران مواجه خواهند شد که نمونۀ آن نیز در روزهای گذشته اتفاق افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461719" target="_blank">📅 07:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q01QJwwopNJK0_zNH4qUVqpIKqQEGFP7hqQJb0vJg-TcyuoHeHYrWxY-vrrmLStV9AzKQ1MyRoPTZH0p54OY14-DcMWwjyZUI62YQDKOM95P0BWgXI0GIDb6ZKRw21WfKy27GtRm46nAO4CsMBfO6ydxVmZkgvXrRia1lFkCP5ZCoJOeYTid_ee98-J-9VgFNYgKlfUH1XovxdoTMbdc1FJiiBmEUDDWYYqXR0NVo6Ipgb1hp9VuprzFj61aEY-6pfflDmaYt6AShpeWNEJegF8h5QxexYHIZ1MScGbcdXtgNH7jz9nvdXV49ttLgdYDB3jdQsUVZiGm3_hsjJLXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OULf7WUtt3ePvYGUhrXCyD7pFz8c6njK4zTrQXmQNFkuXt1WHo1NSi8QVP63r7dL5nT-7Aqz7Akdf-ZUmm4fnJ9fDVLtUvZyZYlqdFQEH1nBv_Abq2be_HstCJ1TEVAZe0Jbi9pcCUubyKpTyGUltYTo1Jf4CtJ4yw64g6e849bnWbGFBhVd5EqbzFy9x_Vc3v0oV8Z-hAk-6aAoKVZ-buql_bX4KiF08vgXehrsJj7J-pjqhVJhhjY2YJKYstKBK8DQq9iGDW1AM0iK9ulHR7Zo-kSX-e5M8Ttu2bOD4L4CopASH3XbPX4Fpv5QfO2ueUPBObJ5ndXyfvGrQqkAIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عراقچی با جمعی از علما و شخصیت‌های دینی هند در حاشیۀ اجلاس بریکس
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461717" target="_blank">📅 07:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b76ddaac.mp4?token=kyOkkz4mYPJX5Z8V3-M-B7COxAXsVFTW_nbQVNGURACXxyHeodnLQTfrhpbelbc37g4YLvc7UCa5n-eZJWdO732y6wkm3CNY0T5gHyduDFuBLY3DygAgrhEMZoFxhPPGOmG3TVeW4PvyK7n9ZAEk5KQik3cj2UeAAMoWgHZVrQebUrO2ibJCJ_TAcLSc9yBSJeqDhgBYoIi--jlvAN_huqHkrP_PuyxHitftJ1kxK_A6r0_ppR25g52dK8KlD2vK_gXHIOdNBbm2hJDbYh_HaL-fAFmUe8oRHESmuUOxCuqYYMQfSfma_EiSzXOC6ZuYgFGmYj2jJS8pIEwTQDu9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b76ddaac.mp4?token=kyOkkz4mYPJX5Z8V3-M-B7COxAXsVFTW_nbQVNGURACXxyHeodnLQTfrhpbelbc37g4YLvc7UCa5n-eZJWdO732y6wkm3CNY0T5gHyduDFuBLY3DygAgrhEMZoFxhPPGOmG3TVeW4PvyK7n9ZAEk5KQik3cj2UeAAMoWgHZVrQebUrO2ibJCJ_TAcLSc9yBSJeqDhgBYoIi--jlvAN_huqHkrP_PuyxHitftJ1kxK_A6r0_ppR25g52dK8KlD2vK_gXHIOdNBbm2hJDbYh_HaL-fAFmUe8oRHESmuUOxCuqYYMQfSfma_EiSzXOC6ZuYgFGmYj2jJS8pIEwTQDu9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازهم تیراندازی خونین در آمریکا؛ ۲ نفر کشته شدند
🔹
در پی تیراندازی در یک زمین بازی در منطقۀ بروکلین نیویورک، ۲ مرد ۳۳ و ۳۵ ساله جان باختند و عامل تیراندازی پس از ارتکاب جنایت از محل فرار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/461716" target="_blank">📅 07:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzB_BKS3nmoZ_hy_ij9_UbTALz271IlTiZEf3NZgxOcjrtZT9V55R6KotyP0TBNCRKLMeBHprbcfBwP7NyNmpWT7RVjf8CqzrMRyIu-XL5B_ETIK4ivOqFxJmN7gdDKc747UPBroyDMR5HpE-N7pOCMCbG5VqAaVDsBPm47oZk98alB99tjmz3Olr2UCZuTutdJYUqqZrMDpy6rQgn1eDl_LUmT8bZswIP44LWR1x44UOAnPKpyMLUDXyVTC9PcF0F6p-TRodB0aZ925ytYYyHbS7dAvsgFzQ9tSjhINIxaygg6IDfPI_oJ5K6BoTo0HcFp3y8sSq5-Y6us_ISNcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار قربانیان آتش‌سوزی کشتی در فیلیپین به ۷۶ نفر رسید
🔹
در پی آتش‌سوزی مهیب یک کشتی مسافربری در آب‌های فیلیپین، عملیات جست‌وجو و خارج کردن اجساد ادامه دارد و شمار قربانیان این حادثه به ۷۶ نفر رسیده است؛ ۱۳ نفر نیز همچنان مفقود هستند.
🔹
هنوز علت دقیق آتش‌سوزی اعلام نشده است. با این حال، سخنگوی گارد ساحلی فیلیپین به نقل از یکی از بازماندگان گفت که احتمال دارد آتش از محل نگهداری بار کشتی آغاز شده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461715" target="_blank">📅 07:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lasuZ7BhiPyGrKTk8c6nfAIgnPS5JaPjPqcE3NA-cRhH1drQlxyTZTX2bke-7A-cYd6-5xoMRgTAGBgECIW-Z-_iQbmBYTYjtpeZoucO4TtFLx3CQdqRB745kesFI6GYIKAaQ1YTkMPGz-KJc1Dgo9CqNIkBPa7fgHm_pLqupJTN7kK4YI1Z2NEXQFblIAcakVNBhvtdQnlErA5FKQ6gm7M9dzCOL0AIuu3TcTIbguLeFXgC5Eh5N_SfuIbz3R6NMvJZo7TeL9SC0knderv2CcQLO0UQkPIP3TnAJPs4ogg1jJiBXPcO1AZ__rXfcecc0Luri-EpO02YWdVRFAKbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تیم‌ملی بسکتبال با شکست اردن در ناگویا
🔹
تیم ملی بسکتبال ایران در سومین دیدار خود در مرحلۀ گروهی بازی‌های آسیایی ناگویا، بامداد امروز برابر اردن به میدان رفت و با نتیجۀ ۸۱ بر ۶۸ به پیروزی رسید تا راهی مرحلۀ یک‌چهارم نهایی این رقابت‌ها شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/461714" target="_blank">📅 06:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9Vif6YkZiZC0fsSXUEgSe78oJD5CZqBItTHpa0Wvys-PrVNX7mwOOWlM6IZg6MoWmKTz7Gvej1gdbNmgUa5_B61O0JZN4mMAlBrnf_Uq07YLJRpsvb1W3fkNzckLUTH_Cz9ZS1bDNaDgy-dZ8zRtIkzYpAw67dNCc59Ir63vCgB7uLfYTUSt3GGUgfJfrpNhNyCaNfga-Ps48HOv8h7BTS02_leYkGW_BUAe70FUK_6l4WYTCT4AdhP8yCXFmuicMjQNf1ixpgX716CC8xvYtZjtBV6G6eYVd5PsA2PDCYq9CKNu62nUrum_8FMhdGN1fzuLG_Ihml9qdoLRo8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن زمان سفر کشتی‌های سعودی را ۹ برابر کرد
🔹
یمن در ادامۀ محاصرۀ دریایی عربستان سعودی در دریای سرخ، کشتی‌های سعودی را ناچار به تغییر مسیر و دور زدن قارۀ آفریقا کرده‌؛ اقدامی که زمان سفر را از ۴ روز به ۳۴ روز افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461713" target="_blank">📅 06:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce80ed84b.mp4?token=hoMxDQ6FLE7Yxt2I3eqIPSIESJyMm6eDufIWMQOi2ixCrOEd5S45apt9hLRiJPL4kYDibK43X_xntsVYI8CPsLBFVlt4sUv4kV77qYrJQb-FbowbyuIp6c-gJ3grm7ofL0f6L0j3TbxYyMgbMC_F9wgA42UoO4pjEgxZZIShra7DaxOOTKZgMdSWS0kFdRxyzG7xOVQ2mnvzUs2774ndgpA7dxyyix6mD-VhofK21ERIZwGWdIG_3neQt_w_8hAJRKY79gLj1GA9YhYDF5EQlhLDjxRpXDZfh_VBkGXkZ-csD3XENpt8n7kv2uARwcqDxukhFuJ3Dp6y2IZ-wbDZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce80ed84b.mp4?token=hoMxDQ6FLE7Yxt2I3eqIPSIESJyMm6eDufIWMQOi2ixCrOEd5S45apt9hLRiJPL4kYDibK43X_xntsVYI8CPsLBFVlt4sUv4kV77qYrJQb-FbowbyuIp6c-gJ3grm7ofL0f6L0j3TbxYyMgbMC_F9wgA42UoO4pjEgxZZIShra7DaxOOTKZgMdSWS0kFdRxyzG7xOVQ2mnvzUs2774ndgpA7dxyyix6mD-VhofK21ERIZwGWdIG_3neQt_w_8hAJRKY79gLj1GA9YhYDF5EQlhLDjxRpXDZfh_VBkGXkZ-csD3XENpt8n7kv2uARwcqDxukhFuJ3Dp6y2IZ-wbDZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لگو انیمیشن جدید از شلیک موشک ضدکشتی ایران به دشمن آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461712" target="_blank">📅 06:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIreMnlNtUt_wWDMj2J3vFttzBRymh62Hs3__fkOgQCHOxNaxqIOQ-k0da3xiqS6JbJHcb2Y9k025rb8goiSuAi0zFpMJZ-LLaq6R4BPVe7s5Scj2N55HzSJm2z_PjjNHySPSjsFgYMLYuJf7YABSK2ryI1o7rpsHY4wxLoq3SASE-uMEEA7rmCurB0hAyMJ8QtvF4szcDSgL4AwuzKK2-_Eu8BxXw6ODCV4GqfH0Q0SQBHDBVEUdram5Q_gyI0iaYCqfxa8HHbc26EfPBamdm4AUqHNMBvbELZqKQQnqkktDHKZNQ2GUOb0wnQN319UwPlc4bZbEYAUv3eFJ1LefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کم‌تیم‌ترین لیگ یک با قوانین جدید فیفا
🔹
مسابقات فصل جدید لیگ یک با حضور ۱۶ تیم و با قوانین جدید فیفا از روز سه‌شنبه آغاز می‌شود.
🔹
بیست‌وششمین دورۀ مسابقات لیگ دسته اول، کم تعدادترین تیم لیگ در تاریخ این رقابت‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461711" target="_blank">📅 05:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icaGpSU9GoC3Qn26xftHdopgvrdiwsTzrQsx5mgb6-Ldgqbv7ZDzB941MyqL7Owo_eJVFTVLTpcLmhuMWe0NcTFecXT_izaaxBTzRRkJUXi4_YI77mBWE03joSZCyU_Zw_yttVztZ2KF-BoUSrUrqx92-zJrvVDZSZEbR4NSkB5l0c-c4qbcK2odgnzKBeQZYHLdZEzbBo4V_0blN462-fSj1Z7twm4vHwB0WrdxJRnpO9wtJ6SA9AQrBhs42tAvM8pKpLDQSdZX_3Tadi-A02ZCXpcJjuDEW8pmzU5KH6ZUaXmZ3I44qy4QWZBI7PuVjT4IuC96WQ_ZNiIv8PZVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرکردۀ مزدوران سعودی در یمن به ریاض فرار کرد
🔹
یک منبع دولت عدن (همسو با عربستان سعودی) خبر داد که طارق صالح، برادرزادۀ رئیس‌جمهور معدوم یمن به ریاض فرار کرده است.
🔹
طارق صالح، فرماندۀ شبه‌نظامیان موسوم به «مقاومت ملی» است که سال‌ها سواحل غربی در جنوب استان الحدیده و استان تعز و در واقع کنترل باب‌المندب را در اختیار داشت.
🔹
این منبع گفت که شکست سنگین طارق صالح در سواحل غربی او را مجبور کرده تا به ریاض برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461710" target="_blank">📅 05:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5w4Tsyz3d0mpcXtIE-Q-vl5vTzuK2TpOcg7wBtEteufwQvUwhGTAcsqJKogoE-YfBGI74vRQfLzXpObW_GArGjoEAey7p5uxGJyOuUMCroQM9jWKZp0bdmoHt9g7_eI6IhnARExDsfSI3LaWuMNarCwMiBXgnx4DZBid1EpD0LIQ1Hnne7z-VVwhqzbfNZXWGDliTCuidwmY5Q-Pbc_Jp4ceiDzlX9fFTwGfjvZqFNHgaGoAksFI1vpqJBEh09raEGqW5OG5V4VZAStC0arQ6XoIfqJ8nmPYSnGiIsFjcs2ViHWxNx_gRsfa-IYFpmsm70P3OnTDoywM162yGIQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از جاده و آب تا فناوری؛ چند گام تازه برای ساختن ایران
🔹
هر روز، بخشی از مسیر توسعه کشور جلو می‌رود؛ گاهی با ساخت یک جاده و ایجاد شغل، گاهی با مدیریت هوشمند آب و گاهی با فناوری‌هایی که تا همین چند سال پیش دور از دسترس به نظر می‌رسیدند. این‌ها بخشی از خبرهای…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461709" target="_blank">📅 05:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اخبار غیررسمی از سرنگونی پهپاد سعودی در آسمان یمن
🔹
برخی منابع غیررسمی از انهدام یک پهپاد عربستان سعودی در آسمان استان الجوف در شمال یمن گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461708" target="_blank">📅 05:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e663193587.mp4?token=B4MmJAFgcMeArRAr0ZscEf54lppVJbHsGRDjGZoaMMXnGbc6Qi7_uCoCu1CNal2GafuoJt39Ig9UU5y_sr0jJtieo8YvwRFFNWOUlfiChmNmVS0cDfIN4hZ0lBQ4NdeFAz_ddxgy392vIeJUazV7USY8IEfDebVVJjl2Dqq8NhKkwEwXeHaDMzZQ00D1fSiFvbWrWYczHCW5ClaFK-LQX_kkWXgr_VIveyG_jZbkYrNPDK332fQJChrAhLagAxAYKYxAWfUwT3J7auxTZywloRM-BjX3wNXJoe4LnsIUgqhc3OMYzr_OXPva81d2TqiTBXUTyut86NGa44PuSqt3rDFg0mxk_u0XDLATscXHyrT17oHnTGY3Z2q8lHG92x2YEVEYBt5eJh_3QM77pftM21zzQoIaaVe2rucWzuYlFmi0b74-pfjbqmGTQxqaHjEowqk8HJ02j_YkytD_KFDKZU7j3PtBKImM_Y07g2NPuYOO6NQw-ZCqi4AL38zfPkaEeht6b0bA4mbXYGmWH2Fc3m9PWYzkPTUBE8a7bew4PPBO3JD5rJbaSJpwPxy4dJm0SIKBFTqRT6wqknzDCASEDFN0MrPKu0XFnI6rC8d3nB2Whe9topvMKVkXMWX-6dm3d60FiEtUPeEp_OXoAKpbEye3uqlIVOAN6lqaJQ2ns74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e663193587.mp4?token=B4MmJAFgcMeArRAr0ZscEf54lppVJbHsGRDjGZoaMMXnGbc6Qi7_uCoCu1CNal2GafuoJt39Ig9UU5y_sr0jJtieo8YvwRFFNWOUlfiChmNmVS0cDfIN4hZ0lBQ4NdeFAz_ddxgy392vIeJUazV7USY8IEfDebVVJjl2Dqq8NhKkwEwXeHaDMzZQ00D1fSiFvbWrWYczHCW5ClaFK-LQX_kkWXgr_VIveyG_jZbkYrNPDK332fQJChrAhLagAxAYKYxAWfUwT3J7auxTZywloRM-BjX3wNXJoe4LnsIUgqhc3OMYzr_OXPva81d2TqiTBXUTyut86NGa44PuSqt3rDFg0mxk_u0XDLATscXHyrT17oHnTGY3Z2q8lHG92x2YEVEYBt5eJh_3QM77pftM21zzQoIaaVe2rucWzuYlFmi0b74-pfjbqmGTQxqaHjEowqk8HJ02j_YkytD_KFDKZU7j3PtBKImM_Y07g2NPuYOO6NQw-ZCqi4AL38zfPkaEeht6b0bA4mbXYGmWH2Fc3m9PWYzkPTUBE8a7bew4PPBO3JD5rJbaSJpwPxy4dJm0SIKBFTqRT6wqknzDCASEDFN0MrPKu0XFnI6rC8d3nB2Whe9topvMKVkXMWX-6dm3d60FiEtUPeEp_OXoAKpbEye3uqlIVOAN6lqaJQ2ns74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با فرزندتان درست وقت بگذرانید
🎙
هادی زینالی
#تربیت_فرزند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461707" target="_blank">📅 04:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تصاویر الاعلام الحربی یمن از عملیات بزرگ آزادسازی مناطق ساحلی یمن
🔹
الاعلام الحربی یمن تصاویری از عملیات بزرگ «والله أشد بأساً وأشد تنکیلاً» در مناطق ساحلی استان‌های الحدیده و تعز منتشر کرد؛ عملیاتی که به گفته نیروهای مسلح یمن موجب آزادسازی ۵۴۰۰ کیلومتر مربع…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461706" target="_blank">📅 03:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اصابت موشک به یک نفتکش در تنگۀ هرمز
🔹
سازمان امنیت دریانوردی انگلیس خبر داد که یک نفتکش با پرچم پاناما به هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفته و از کار افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461705" target="_blank">📅 03:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCcKLbiMjr_uSZVqRGUWGckW2dpj4z2jejrO5MgrIu216rZ8fXWtpDX6grX07hM8SpMQbMNkKlsmpyVM7Xp8IwgqxzQrJ88_U7iOGj9n5jbfNC-m3Tujg9B-09Pf6A1kz3-d9wVA8izI6kAdOYp4XKW7hY6W4BrqL3k2csu22iDFPzSni2QRD9NLIjL8h8yOHgh5bPsVPoFu6ZDH3lCRTAcBu_67GAm8F-N_r3NiJ69CdTUTt5Se0sh8UzmFK_IMzYaZWQtzaaEMk4ofN97Z7FPow4BV3Cszi9Oowa13-9m9qYtQycK1qhZnXSTsfBOQD0-oWJYHdFjDoHUd5BrU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقق پیش‌بینی رهبر شهید؛ وقتی ریاض برای صنعا سلاح می‌خرید
🔹
این روزها که فضای مجازی مملو از تصاویر غنائمی است که به دست رزمندگان یمنی افتاده، پیش‌بینی چند سال پیش رهبر شهید انقلاب از آیندۀ جنگ تحمیل شده به مردم یمن محقق شده است.
🔹
فروردین سال ۱۳۹۸ که چهارسال از حملات همه‌جانبۀ ائتلاف سعودی به پشتیبانی آمریکا به یمن می‌گذشت و نشانه‌ای از پایان جنگ دیده نمی‌شد، رهبر شهید انقلاب جمله‌ای گفتند که اکنون تحقق آن برای همگان ثابت شده است: «من از تجهیزات و امکاناتی که غرب در اختیار عربستان قرار می‌دهد، نگران نیستم، چون اینها ان‌شاءالله به دست مجاهدان اسلام خواهد افتاد».
🔹
و حالا تصاویر غنائم یمنی‌ها خصوصا تصاحب قطاری از ماشین‌های زرهی که این روزها در فضای مجازی دست به دست می‌شود، تحقق وعدۀ الهی را نوید می‌دهد که رهبر شهید انقلاب بیش از هفت سال پیش آن را پیش‌بینی کرده بودند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461703" target="_blank">📅 03:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRc3nkqjuwC5IRCWdzcltNoKFjNfUrYX7EvallTMkZlAorUOHyOoiMTLTSsM-JPp5puuC-NzhbXoFf73FOzi8uvz80LWS2zJDwpptggTWkCIPidUV-g3pujGdkXLUonGIezRsOd4gMKBylVoaJbjXR2k1y94VwH79COjundeNGolxwvxfQXUAnhpM20HjitW4BamqDk3D2ua-9mZvfnMx50iTFQSqxdjMYph5yT_yoqSE51j7LBA5KTwXFSozETDnaT0z8lLMh-puYDBUvsZwcWhf8NBkt8kEFRO04JHIUyo1GyxobCOYr12DSsPEERXms3lOOfAZFK-jTiy28ijuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QYHSDSEcFQGgbA2Bevp52btpxZvFQP_OfFfxMjeyVyTt8DATTVXKduipqfbIytOKT5dDKXEtFlbGOAaMO1WW5iUhYonLem2hmhzkHoEpSM0XVaqy7TvjjJsiriU5GJ0fy5VREaMCk3he4v_lc95ttiaPOfB_B0zOJ6HK9vB7-Cwz938dq1I1GTJe5X2zl0l-jvE-SzuZa7DZ4zcTnythP142qhG4kAkCgQkJw1Tj7PRPvk6mIHqOfjCU1PGp1yww2UthVfHPdKoIU8TAiPTGawbz-8kEWvOrUWTWx2jQ6X9L1bqTCcicsc40C7HtEqRnu-bevIid0xoLKCGkcY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEFwL6iWHq0qeXofEJcaqGlqKxySXFIzN9v92lA6C1urHcBMqY-wYedqWHwLAVLO1EHmNB0wg-2boGh6nJgGujbEe2BXY0dVeNqE0DgPlG1ZgoJhpL-LkCKrfZNvqwQpHAjLEpxfr9KgWw53eU6HUEN1h6VfP2MURyvvG6T4l5BW5FBw6RtJuBg0-BXz-WYQ8OZ811gYEMqCuFG5L1nZcmMSw4NPVc02Rr5Jts4DvxMIvHeaEDUb2ZTgdyJ35ARWa3jP81W0r9x69bO53SXR8BmtEO0q6I8tDyx90YM5QQrv0Pi7xMwilvqXTKX5kd13GUj0oj3abiTQBI43FZ-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJ35hr1DccCK6C-HH5HxX4j4jUtfehYkGqFEKD1wqlCJdOAtjjoTB0BV-Ioy8YAvJCsPGJbRcNypEpcS1r0XkeLCqbHGQjXjeqf_3WCRdtJWOf3L7HC0wm83GqznlrLTRGo2ggvHSNymhl56KJO5yCVkcjtQz_kwfDwWYc5GkWaenfgpKcqClKBiqGhnjMzmuCA0puLPTuyiC-dvYq4j8cfNd8LhRnYsYBlAkt99nUe0Au0ZEKE0dL0oYiK0AY8xCezpv5xJy3AU4I6GZRaDNIBUtX11ZSwSX6uuYtJmNT5v0gWMxRkwJgA1M3St0LVDjEecY1BQD42mIsZyX4n6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU064D0-IEldX2Ry7ncPny4_CPTJC1d0L3jaVLFZYpTnqy2Y-o5K5ZQkfs6ECtucVld8_391WFqkMOYHZMrN6ONEkwqjBQTmXZZagQ7DnJ1DwMWmfqP6K8pmmwEDsB_FcrOKu1mo8qIAREwOTXNG7jW5voejNBZoNMhckdmvbKol-FHaqjry0442Yj4Ucb9U-NvImLwNPSDnAH1tcCYvaU8MMUtgLhtk3qoOBnTTpPg-_nbMiZAqjTr6hQUuWdfx4s6tCblEoTJ4ATZRyoK4bS9E2wvSfTgUOmIr892dapH4Cr1sHoags9bEf3mNnBjCedcJj-8fNGjsDq_kmcGQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIGsUb4DQcSKUc-adYhJPdNQrr75Ny1G7CfScYs_wvoXwz2PDEjX7PJ2spyRN_6Is43GOiheDMrVfrots_kP_5Uq5fBD3rCC_a6EvZZU2yTMNHqWbZHegmkZcT45snpbHkRVSjFg4I4HUlJVuouZo-QBKsDez0epIdlfNdbm74einNaor9I4yZzYijBJd94OHqzbhgaaMz5VUO9Sv__FbXyxFNIbzNHZRLOrQ545egL_jF6HwSzCZM4QGzQNdRY9vAeKg4AGh6aTE96lziA0epcXxF9Ee8jLuFa4Hg6u6d1UdCKNSt_0ab-32ZY82VE4-6tunn86p-2xdjwXCdWFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_dsohs5ASXYiQQkMjy9kRqM2S8C-M20INMMhm0mkqMVw40k-nXxFpC4b3PQUMJKwbn1MjTfkKx7eni_oTCSPKdeRUSVGnLBpYnM1EWYgYLdYJ-R97xmIvZnqU1CW_9E1-Hlib2lxgo-8lFdENVdBM_s5kOlBM3r8KRJs5FC7TZ1PK3N5hCwxBg0qDDC9AiKSnBPZYfOAe4cghLP8NKlplVJ_sSF015RhqkNXm-mzNEZ3mWlreExAZh45AjcqCfz0ltMckO-E8Th0feqbayt_nH6pVdb5x6qRFmd6831YAxbpwF6xUFiI4pozdszZz-DsAecAsk-PbWkBCdli6Ngjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=om7uGzMs0P5HiCohTmFZTAotBtpwApf05Xh7BqCLsgfpl9LPw3ENKwRIfvnFILIjvkZqd9VXaM7z0AYcJBFOkAavRKYltdJvLpAC0McNYUA7azW1-jJyv84uePdFL2bBsfLfxQj9PjGWxsZbk6pwTOR5eYFnzYe3K73fbqwFTHOWXzviDRj8TmJCCJUiJHMbKllPzkhAAQ5hWpAWjLvX1zW4LiiSiP_KSEKpkb8Uj5n8UI-8ZKdBSl2DY-pIbVPMchoz7W6bNJCyei_wvm8jqY2fg7OBOp6tgvIQ4POKQmlifbIK6vMSAtj0oSrGpFejQE0WgSR8af1S4H3e60jAuC4bfp0CEdJLaqr04yMispLjMj8Oy-AOVEY2YfFteo3Fkjlxs2jdxhs6kRbYg196yaLXb8jLxkUSfJmN26wQqLNed0caf-7PkyBdBWiOwRxZp51bc1wvm1TizOHIPztLuQaf1LTgS1iuvYmk9t4_UR8NY1zWKX05MbOj4AR3VEj4JPEymltnwk3DKzanvWTFiTGkAtA2lE_xTY1n8yVP610Z88qOGBTKxwnXnFOaZt_gfs0nE-7lCjrdroaxMKxBfnQ-_oZBghQRp6Aev8Iutq4Vgd_JEzR5_aJkA8QJCvwXSsm1z2TRWo9-nXHxNUgUtv3CRhXnvt-IL4F5XpNn9t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85060ad79.mp4?token=om7uGzMs0P5HiCohTmFZTAotBtpwApf05Xh7BqCLsgfpl9LPw3ENKwRIfvnFILIjvkZqd9VXaM7z0AYcJBFOkAavRKYltdJvLpAC0McNYUA7azW1-jJyv84uePdFL2bBsfLfxQj9PjGWxsZbk6pwTOR5eYFnzYe3K73fbqwFTHOWXzviDRj8TmJCCJUiJHMbKllPzkhAAQ5hWpAWjLvX1zW4LiiSiP_KSEKpkb8Uj5n8UI-8ZKdBSl2DY-pIbVPMchoz7W6bNJCyei_wvm8jqY2fg7OBOp6tgvIQ4POKQmlifbIK6vMSAtj0oSrGpFejQE0WgSR8af1S4H3e60jAuC4bfp0CEdJLaqr04yMispLjMj8Oy-AOVEY2YfFteo3Fkjlxs2jdxhs6kRbYg196yaLXb8jLxkUSfJmN26wQqLNed0caf-7PkyBdBWiOwRxZp51bc1wvm1TizOHIPztLuQaf1LTgS1iuvYmk9t4_UR8NY1zWKX05MbOj4AR3VEj4JPEymltnwk3DKzanvWTFiTGkAtA2lE_xTY1n8yVP610Z88qOGBTKxwnXnFOaZt_gfs0nE-7lCjrdroaxMKxBfnQ-_oZBghQRp6Aev8Iutq4Vgd_JEzR5_aJkA8QJCvwXSsm1z2TRWo9-nXHxNUgUtv3CRhXnvt-IL4F5XpNn9t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر الاعلام الحربی یمن از عملیات بزرگ آزادسازی مناطق ساحلی یمن
🔹
الاعلام الحربی یمن تصاویری از عملیات بزرگ «والله أشد بأساً وأشد تنکیلاً» در مناطق ساحلی استان‌های الحدیده و تعز منتشر کرد؛ عملیاتی که به گفته نیروهای مسلح یمن موجب آزادسازی ۵۴۰۰ کیلومتر مربع از خاک یمن (۶ منطقه در استان‌های تعز و الحدیده) شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/461695" target="_blank">📅 02:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce86fb43d2.mp4?token=TBXdvSxc7QhDcUxaO1v3AQCrSWBMuaiXURf3kxjJfg36j1SC8BFAukDtjD1Fb697n1-tkADaaqafsE7XDFllQ6lvidYoE1ZbGbQRZ2eWfOPjyWMvHYn_7_lnkHVdZwb7c_LmpfpQXJN8HNm4D16OgfUgBBX3IpT1uuNWk1xcTf31CSYG-fq_3aBUEOvilt6zId_pT5JiGSckaJlznB1tXkguGthPNrLLnCEK3XIdtif4RLRjilxg4RaEPy1TwJDXQnW98Xhle6vtNUlO4_QOXPPW2R_cx88CGvcuhjtBjlcHmJS0JaHP5itfLsGQTK-d0eN7Gts-clx2Cp85gQTbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce86fb43d2.mp4?token=TBXdvSxc7QhDcUxaO1v3AQCrSWBMuaiXURf3kxjJfg36j1SC8BFAukDtjD1Fb697n1-tkADaaqafsE7XDFllQ6lvidYoE1ZbGbQRZ2eWfOPjyWMvHYn_7_lnkHVdZwb7c_LmpfpQXJN8HNm4D16OgfUgBBX3IpT1uuNWk1xcTf31CSYG-fq_3aBUEOvilt6zId_pT5JiGSckaJlznB1tXkguGthPNrLLnCEK3XIdtif4RLRjilxg4RaEPy1TwJDXQnW98Xhle6vtNUlO4_QOXPPW2R_cx88CGvcuhjtBjlcHmJS0JaHP5itfLsGQTK-d0eN7Gts-clx2Cp85gQTbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ هوایی جنگنده‌های سعودی به غرب تعز
🔹
در شرایطی که مزدوران وابسته به ریاض کنترل ۴۲۰۰ کیلومتر از خاک یمن را به ارتش و انصارالله یمن واگذار کرده‌اند، اما حملات هوایی سعودی همچنان ادامه دارد.
🔹
منابع یمنی خبر می‌دهند که جنگنده‌های سعودی بامداد امروز، پنج مرتبه منطقۀ «الربیعی» در غرب استان تعز را هدف حملات هوایی قرار داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461694" target="_blank">📅 02:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2R5unbNoiQojECNtTN6iCjhmF6kUuyETtFl5jNwNjNFp47kGMMtLLBCT0_pqxEcq7MtyQgEQB3DKfxs0jD3Uh0SsaWoiQyerTXd5DUjRc6uDEyhLQtrwLAptD5cOB0TtbN38IzR2TPm0ZF-A2MxaTH1e1aqWZ0j5LyZZgQTSnihrriY60arrw9L97nbZ2sDj7kBvfthPY0Zo8Wfnvnuo5Qu9jkCRliZGhtS65zx1vyk5nlxYmeF2WLcedefZDb73TD_jivL3z7Zrrnc7ExWKoAM_3w6xb2bLaAVSBgPhEhPQpHpJXUOaaoe6T94wkvpeBxag94kAbQ9sWspkCsl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS4e8-RspsYUMH6ZJTiSSM_-AV199aIjKeUNtEqIMjSJ2R0f2qJJ9p8PaKX7mGFxVNM9-DSQELY98zkTGobe2An4S7f27FELc0UNEUqQvyYUnBGZGGRFVxnuSpHHiRvQ0mHr15XI5LLuBu5-nmaxGFmWfy4F_Vb3cKQ6b5WFz4NdCWHzJu4EmQsZVuFx3s2cQxWx3lTe64fP0M-kqEX7iUWenuZPDXYf6eEd95tCHd_dae-Lv6uyaF8fCpe5pL-hnIF28wOvDOoXCmcjL3a_l4sWKD4vMvFa-1RkP6o8l86nZrrcgT9TXNDKvVndyUL8dg5CA-rmHub4o4TENJcNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMcpd8gFGFETJ33TMt5RTqD3JZ1lqMdGS4eMM5sokKTYR7-Os0SPmk4t0Ilnt8LPbV66gWsaePy2yz2nxij3yn38qKuH4T5dIkf3vHwWol18OvhhmfPh93nn9ozyYUVZWwziElF5hgczsYbsJQHygKk0Yj_W55cznjE2ijX1XT2UqmmBAuv4xDOZo3y1enrrzAweBIay8Nundg3UnQawEu-Q7OuaUHlbNWOvy5WbwCCcxhVyQhDC0_IrRdsL00Kyyp57uO6Yw7GBPnmTWULXMrstZhZ-EqwWBr2CAGejxVs9gnlPkb_ZCGfhAZGbDLQbjNj0_UYzMShh53IfWoZl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMG5Xkg5edMh49AClSyFFEYoEgJRYMMHl5qmIuJzPRT1hcFaDXsQaAMpmhmrr386iP09nPOifPW-IscWAWOaiz5SXmoVhCJtg220UZagxcHX0gmzEqU_5BNujVRPITahm0tMLqitIz_SKKhSTq08g-0zRsppCNymwwgYi5_deU_s0QXQi44OvlRbG33rCVldakgO1QKY7svMWDo-9aFgzFs79_bhtC-faJmJqhIsuc5xD2o0CwLZZpZKhRKsNVObFrh4Z6miyTpfq9pTA_JWZFiQ1zIwWvUtzewDXuWR5T2bS4qf2JJXUZVi93yvBm6crY0MSVxymZcBvs2eRv0onw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scHiX-tCvTTNxxBESlcNCZl3N5YCwBHOBPY1PnbrEHu6u-au4n9280pDXWt-OaA3F8af_Dw0PQ9DNkBNj6wQst0mo2EC6qcNOxqYyNuzWLKWpzYZqriSicwrUv5bhBEXFzvumdR28N_8SELBHaHgAbnsdjTPJnWUwGrx7zS0yZqrBd3IyScvv907NCzquDSrPNQb8hYNtw8R2Zpu-BRA6miHWP4j4ZpcylVqiR47KVMvxVgVsd7VItgNf7tRZx91GPpDI9ktTdUsck_CdWq8zw08DA3wRFIL0ndm7sSk_Qq5zlpBfJy4l2usOQju0Gt51TeQoU3LtQFlHS4fmzmugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHhuYmQDC2Bxye19JBAdrei5hoK9G-ajYybrUG1qEVOU-NsJfuApvFwwdTwqVFfNYGYu1iKpNLzWSMK9BaLPHrWuZ8GLD7TE8CNuILLlPANKV5LRKTdiL9lXHB6xp2FNd1DP8ngMZwrBgeAlcrajJbZiuf399JNDKUJrlj3nimneuaGUdFjtz2O2NyguEor7scrkvaHL39NXgQuzX04ipzSve86v7cad8uVqniZZBkQDzBiHKirUkEDvnYKrmAf7_Oh0W9sU94k8R0Tbpka85xVd2QO1V7sG5puo3hktA7EYTa-vFmmc8EA6PEkN2Ck2rEHADJrz6x_1C4zbV6Hx4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یکشنبه ۲۲ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461688" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461678">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnrGG7gto7lIG8VpZ4V7zMFfERCGFzBe-CkvETLEd8SIRMSHmpRhbs-zQ6Hk5jSczFQi7S0fPPV2lQ9OcJAAFUTbB5ROXvH8q7Bokr48NKtA68W6gJCNI36yXDzNGX5ZKkAKi7uH8bLxw5nCNCIIrOmt_7QUd7FDhS53cMpv0jPqwLiE0hcUewaEs6vZzBSeFQ3pGNSUMfaMQfzzlxYbA8o-fynQRLSSKTJGEhHOL_cOmPIQW6gABes_4dr95uJHXOJ6cKjWpWjBGpOUsPfNDcKl4FRYzlH4Jn7VZy4jiCA5rIACrp6LUx1qqiNlZ0dDWB9ozIG-NLDt-D63F4ixzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_fpO9DVOJGaYnbuoEWhiHHcrgbGmrAKFWSPELbWc_Ro9DYrukUGJW02yRWFQaQC15F4aNhOVz3kBeO2VFZiGPFUTs2UxTIFufWJlRQ8BuFEk7iLPvya55xGH92yyatBJFw4X9Z5cdv0Lahkfjblyf3W1CvNWhK-BgNhItgyoKHH9b_rhE_vWBZ_28n_l4k160f9N-yWoX7W7ADDn2B3kUcPq1jz9fK9y2-yaVTwWq1Fpu8QNFt315IXLVyqWMqAeSJw50BnBUdyMWEq3QGrA3_aCDtg7PGdmjGylVskpq-IcC230_RwWSgy19E9C9q5yK3E_ZRak1VgCu9US3e2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRKgEgzur1G_qLbrqp3c5YsbqgURNLavuweYzx-pQo1G_cIKQssElkzvqMn-PQxv3ELs38aXr97QOf44yKxw95iE9u8ncuzKHYX1e6R2jGonGK4eANtH4fmKjAY5BQP4V5pLDMxH2GxrMJpKOBSLeshYt0W91fE1knGES2xUNk_Jf5AoPhk5mSg4KROTlanai2aYykdUIjsWJK9Vo4o1stT2X827AG2SLQTzRYdATyqregcFsPij_fSsq26NVnyQ7WJDn58N8qdM1_MRb6dQ0ghiaiFQUGZFhJBCA03eEeJ_FWXqlrjDtdhBibmrv3xDlTcTQjOuuHAFtduX4l79nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFfKA5na8MUUefUFiO4PFwSfI6aUiXNdvpTkHcfFk85uz_HZWOPYVkEumnbFraEdH05D0FHcd553VeDzeYHPCwT1KIdKoEgk9HVoyaasH2NM_ZeLLwAN199H0GABQfyAD9stcEDtQF51KNmjxxMo4-et2rBNJslFa208byylfXj_GaX-s6qgH6PGDl0DRdxBENTcQLGxU2AKmTo8znXc20CKYBgoZxw8PD8h_2jnlVT1su9U_HaQMlOVm0Zl1RK14WICDeS9u0gDL8AVp91QmarEKXxelKKQar_rmT9gS7xPbrP8vvUA0F_g3cKshMcNTiRfs4AAuMpOesKh33D1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osVgEL7mLUl_Hn5jZBlz-ag2WVUW9KNmuPGeeh9nlai25Jc6kUyJtZoja50s8bcOgVN3OfxvZ-l-UYmzeyOPrDTR_HW5jwB5H9vfb1p_ZjUCri2fcHtRwqTxZWcGFCsTZoZYpxqZTdItM4jTHDGvYwK-PJcgWu8OD17tHkbm8fUCyJYei84o68yC0avJYqPm5SjX7Jlm6sz9Zta3tXLerPzlwCNlrbnkXhF3rPnWkY7bRVBo5cf_-Q8MAFCwJc5IqkPTIcM0cJNFAKVKlXKCqHLeCRPNLVNjbVbsq0gMzfjWazhVS9i4_Ds7OGbKnxFjFrAt7qfGq8yGfYL4EcTd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBZVDeenjiiIwd1BGPFdPSB4stO6QDfx9hU0rmZf70hBBGS5t16wCfL0ZlHxt3Bf910XVm2mUkfxDEXJ80R8N9lvNJAca52uYgAYKeQ0odKeyaKp1IEf0zl8iMkDM9GS1lTIbmDshmTJbxgNW5vX6T_I9IkqVzUX06giRRoLm1UJT76p1pyPB5HEHtmrHX9ocMVlAjUcsokTEe05JzvXHf_xk0z2UU6xRdGLIgVvJlid-LSR1fv1o2CQxUp0XcZLnT-pcc4IFPqPiEGlt6jOXCTOEPqM1iu7VlmFe_baXyT3Bddvc0BqZLlU3r6tt0TEMNsdzk4F7gCRVCLNEQgIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vh-OzCVQq9z5TrD2rsT0ajByxVTgtdXUkSBIM-fg4prj3sEcW4f0GGvJUoUbwRrjug1k9HQUfy6-1oz6BKILNow0JLcQdg1ad124cEweFC9LCD3IipoxaQiRhnizPyxJpsLeP0yaivUkB_oIGywSa4OBOLgCab3FCJGyH4y2ujxjmYrTbjXUKfflTvEmU0NX35PHu23hBP5zse7raUInaRCWkUehVZsdjX3BcEw4qPJANdrJQNTvZmlsczg-2OblXUmnoGEAM_gwO2zKne3dmPZPI_6ipgi2y0UId7ER5p2PZ7TJzfddBwjITcJ-OcGD1aZh8Gd6GogwrknvsyGbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmsVsojDF0_yD23whImTaq7jCtEEYgEozg5lnsj6lk8DoAhB9pf0PhpMyL8h7kCZwp5UMm_6XoWo_tLhl6fbz9K3ueEjDFfiWiEjdXWRnZ_HeayYRG_FyKPlhooSGaD2p2IKEogEbnT_wg0_pou0sKJMEGFUZ5ctbWQXfnAcMCFeRBDuWVKv_ehyI841vO41VtPt6BiMQq9G060sEccmiF2IfOgbDFCRyT3d2KEQT9DRo3cT4iI3ZLbXMC5OlAZ-Wg6zO6mS8dSxYSrfHnmAm_Tx-NsQSDGTkx29NuTQIDCf9HAzvZhux5DouOZtvw503gqv3uRi8p-DeAWsuhEakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCIfoHXQGNHy0BS9vXBVN0-spSlgbsSFDf25IEvib2mKMF89fS-Rb-ct8s-KW3yCwqd9aSZ0dSpTlVlT_3vY1uhwXtc-y6rDYTgpRx9XxLraXK4oH8zIpviZBFTG9mw2s0fEHpXyh6Dof0ATf0M7c1XiIUMrn6DxGtMgWjrVnfM7HMo0qHVwYmWQm9U9a2cmk0_nBqAM4A5nOYKFjVOHFGSFgeypV8yJbwCXc8Sd_o4OE8vMxZO5eVBPUVZZv50I0cOYMC6NoyAJSMVUGxjLF-GoFLMHPavHVnscGSdgAPCOsyS1Jwt1SU8lmXMEVSdgiSLETSIt4Ldv95Ahad3J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skytA-Pc_Lx1EsC5ByBzeJVohskqpUGllIpySUQG0GWpVTf6oOAKyRyEqUZ1RVMn1JSOGVHNtCdlzy2NNwIFr8EK4I5cIuMoSPUEayqerVXr9z4IlnshgRTxa8MoykVQbF9cFrn0RUC5Uem7nW5WR4LiSevh9t_v8m80poIIvHqLFMDjVC3JNOd3I2Ym6V03Qrykph3nAYfHLGK1ynfuGumxgChgyd8THiZzd3ouGm2keiAE0MukRw3YTz2x0bXzkMNUi-si5aavUf9TrUQmzxITOvzZshWmqFr4iD14DrVXV41VgsPnf___BBaeccbrWZICKPRBduIOLfmigZHpcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461678" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461677">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به پایگاه نظامی عربستان سعودی
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که ارتش یمن انبارهای تسلیحات و اتاق‌های فرماندهی و کنترل مرتبط با تهاجم علیه یمن را در یک پایگاه نظامی در منطقه شروره عربستان سعودی هدف قرار داده‌ است.
🔹
این عملیات با شلیک شمار زیادی از موشک‌های بالستیک و پرتاب پهپادها انجام شده و اهداف مورد نظر با دقت و به‌صورت مستقیم مورد اصابت قرار گرفته‌اند.
🔹
این عملیات در واکنش به تداوم حملات و تجاوزات عربستان سعودی علیه یمن انجام شده است.
🔸
یحیی سریع تأکید کرد، به دشمن سعودی جنایتکار اعلام می‌کنیم که ادامۀ تجاوزاتش علیه مردم ما، با عملیات‌های قوی‌تر و گسترده‌تری در اعماق خاک آن کشور مواجه خواهد شد و عواقب وخیمی را برای او به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461677" target="_blank">📅 01:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461676">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2y4gaTwbiusGPl1w1b0zeofzm5qDIhqUYve3Ept7gGR_KWN7EYIgEOS1qYVvGplVDSrf8eBJ2pbL_EZDCFkEmtzkVNDDHIcjkTRD9LN9WNIU1hFhWpCMDOYGjQ4yKhFMyAt_QYfVxE68rl5amCxIZUnxjU_mmHGl2XbUKDTYX5ynUCOPb2cxjahclKuGwneBITzhuNMmRAI0nFAEE1kTMZn6ZDXeZmWvbIwKioO6hIGJX0pGwylKZ9NDgeAe0BETycjB-gkJX742_7KtcR9g_Cqq9tqW8hyFJ7SDC5XtoRyE5FG9na0T9Q-QqySJVomH5EqampZfJ86jaMTUzQ-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: مردم ما را نمی‌توان با زور و تهدید وادار به تسلیم کرد؛ ایران تسلیم نخواهد شد
🔹
اگر آمریکایی‌ها جنگ‌طلب هستند، باید با نیروهای نظامی شجاع ما روبرو شوند؛ چرا علیه زیرساخت‌های غیرنظامی، منابع غذایی و معیشت مردم جنگ به راه انداخته‌اند؟
🔹
اگر آنها انسان هستند، چرا مردم را از دسترسی به آب، غذا و دارو محروم می‌کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461676" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
