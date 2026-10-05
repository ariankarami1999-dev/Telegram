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
<img src="https://cdn4.telesco.pe/file/WOpU48kJUupeyagb48xAeWQUlPMAhfJoWdL2Ax123CicIAlY9Jk70_rtsiusbwOxum5AdnXA3lpy09V40k9F1SP2qTdHwJtCLhW2nsjuDRttj2C3gj7IFGYvllsWVc5Xr0ptpN-EkiEip1OLSn-fsHlqYDNjj3AGFQ_VdKejzdZTBIUoZxzAxV9AvVv2ept5xYHreR7zGC2Ob9DoADmMdO0Dt0DhDFDC6E4vLJAlGDISBqFbMRmJQrLuqjNqiuC-2MM54EVR8Vmzn75npO18DY3_XrGJey8SWVgmlROuXh8ojLwIzQHPN6KybhecD9Jt7M_1x22ZLrvElEGpOrHdOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-695929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
امروز سیزدهم مهرماه، سالروز برگزاری نماز جمعه تاریخی نصر در مهرماه سال ۱۴۰۳ به امامت رهبر شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/695929" target="_blank">📅 22:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
افشای طرح محرمانه عربستان برای حمله پهپادی به کعبه
🔹
منابع منطقه‌ای از طرح تیم امنیتی سلطنتی عربستان برای پرتاب پهپادهای «لوکاس» ساخت آمریکا به سمت مکه و هدف قرار دادن کعبه و مناطق مسکونی اطراف مسجدالحرام خبر دادند. در این طرح هدف قرار دادن چند هتل نزدیک مسجدالحرام، از جمله هتل انجم مکه و پولمن زمزم، و همچنین مناطقی در اطراف مسجدالحرام پیش‌بینی شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/695928" target="_blank">📅 22:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0c44aaa4.mp4?token=QhbjLBjr1BHHzS3uOIoB3mUSwlAYZ66PfT2vISJXBX3OKnVeg9QF3QwPsY46qVw9MCg5RXwa7KtHw6KX9Zwakf5aw4yGmnJ5ubGfuPf51DnAodWd2CWOtfayeDc6IUdXi7_24JTAnGjG7EztHGi8I7pOydBuiGN7Kleu87DR3a9N0QX-cy2v1QYaXA_YWpwG3jVgK7qh9qTBKWJ45aPoPrWGrvILW9cTNfod29douekpzPscn2XSG86PWXQtIeFCdA-RHPsVYVaz4KUThrWxiKxkdx3-8SfcKQFoEG7sSl1n0LKg2PCxOX-8dLVVG6mhxMy4JK1gN1Yj8xx5_dGjQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفع دردهای مختلف از زبون خودشون
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/695927" target="_blank">📅 22:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a037aa0fa.mp4?token=eQOKRnHprxpeMuyhj5xm5E8RreRbOQHgRqKCMuPKmX4ZCXHYGTN4VerXzpKIzHcaQjNaeTGFII2AfHm0bhGVBcpLJatQ9ivkCdqaJoTouOyOu-IFcyz_rangHLBnfyEHimJ2NRoYFCvwW_PjTt3aNgeEzvmjBu-ZSjn_Vt6XwCKAXDxOJZ0-RqqXbeWv9YN7dnscm_n4fGaPDvPsvis2rETSfTdxchQiaJiVRkj6XFndP1qh9gjCg9gKPQzQYjj2xBibWcai41WLJHzos5Rh-YevdTdFzzUXp79oiyBCgfhcABVw5P4x4YPrxBKm5LTE5sd1gZAzdSQ5uSHdbSyr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئو از شهر طاعون‌زده‌ شلخوف در سیبری که مردانی را در سطح شهر با لباس‌های مخصوص محافظ سفید نشان می‌دهد
🔹
هم‌زمان گزارش‌هایی هم درباره قرنطینه شدن بیمارستان شهر و کمبود آنتی‌بیوتیک در داروخانه‌ها منتشر شده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/695926" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX0HZOctQuTi186tnvhSYM6hIR33HrY0vGGfQwF6DVgykyHuoGwiO_3tBm0jBWxdnvwMNo5MhgIEPZHOL4XXL_wT0x4dRf9X-S-FwOTOxRZdsUh_ED3kN8s_xEdGfeKK5vtX5Dv7iJAhuni8xTAiuDr9XQtAIt4KLvUjmi5BVVw49SXcHLNSebOrM-mJrwurG3IkxARiUDbeRiBmOcLblnsHRqSQtMwAXwi9v-SnCAf5ci50Zete3XXLrh0BTk-U0qePP_Fc_GZU86K061ju5xxb7XT_3KUOka8cu2GKad2Aw3mjJ53__znKe2slhcURXFCVw9xFsGVKOz6M86976Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریشه‌های شوک ارزی در شرایط جنگ و محاصره
🔹
پویا جبل‌عاملی ریشه اصلی شوک ارزی را کاهش شدید تجارت خارجی و درآمدهای ارزی در شرایط محاصره و جنگ می‌داند؛ وضعیتی که به گفته او، صادرات کشور را به حدود یک‌پنجم گذشته رسانده و بازار ارز را با عدم تعادل روبه‌رو کرده است.
🔹
او تأکید می‌کند نااطمینانی درباره درآمدهای آینده دولت نیز از مسیر انتظارات، فشار تورمی ایجاد می‌کند. به گفته جبل‌عاملی، تا زمانی که یک چشم‌انداز اطمینان‌بخش در محیط بین‌الملل ایجاد نشود، ابزارهای اقتصادی به‌تنهایی نمی‌توانند بازار ارز را آرام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/695925" target="_blank">📅 21:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
عربستان اعلام کرد که ائتلاف مکه توافق کرده تا در واکنش به حملات حوثی‌ها به خاک عربستان اقدامات بازدارنده جمعی را به اجرا درآورد
🔹
این تصمیم پس از برگزاری نشست اضطراری «کمیته راهبردی سیاسی و دفاعی» این ائتلاف در ریاض اتخاذ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/695924" target="_blank">📅 21:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR3AcaK2VXT-j21_pujrVXehOv4DRCPCH1GEUVaQS3RdSLogySTit3PVjIymTqjhQLMjgGBILd9E1Kz3eBekBVXcqbkAxyTeO1Uhc3iulSwET1-Uz4rptin5um5DhSIe8POE5kaHlAk0wGgb-ne6-9La3gVexzutiCKWvfGfytnSUsd-YGAjg1Yk2yVQ1ql5_CiiT5DGAU9sM-GJId-oEsUwjM71vB4K-dHlqvYgtgZeWR1eI8w5cRgfu2YjL0X8-MqlZ0Y5ZwYSj-aWjE1CaBfIzgRA9qC44lyCtpIahJV3vXBmm7c9892HK6ou3fv0dAVWhryoue0mylFp7hRQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورت‌حساب سنگین ۲۳ ساله آمریکا در عراق
🔹
از هزینه‌های تریلیون‌دلاری تا آوارگی، ویرانی زیرساخت‌ها و پیامدهای امنیتی، مروری بر میراث حضور آمریکا در عراق.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/695923" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آمریکا با فروش تسلیحات یک میلیارد دلاری به امارات موافقت کرد
🔹
این قرارداد شامل فروش سامانه‌های تسلیحاتی دقیق و تجهیزات وابسته به امارات است که توان عملیاتی این کشور را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/695922" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS_Z2uqJD3Hobew9w9hNoS5NicTIM3nNnShS7iF-I60ZMkknk7xbGiERBnrKQjMlPVu7vTQNABxqFBWP-Sq_4MftiHTQMpqUn0QsTr6trmQM0yx9LRnNlUwZkF6uppOl6jGqV03y8EnggCAVgmlOeZQ-DA2yyUyLxSp4WZmSkHgn3sHCXsjl9FJN9-EKyUILpuyETimKyLXWfzzW9UzxZJa4T0buyk7QAhzKo-PFxpLA1MjaindXXJRMbg4lI8lmXZfwXRxa8CYhzmwnX34yCLs8tc4omrVSyuze4Pcc7FvYCvyu02NToa8hfT5_kxppJCCC69HI_Z7bOng0zS9zng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعای خاص استاد شفیعی کدکنی برای ایران: ان‌شاءالله ایران سربلند و مستقل باشد؛ صددرصد به ایران امید دارم
🔹
استاد شفیعی سرش را جلو می‌آورد تا صدایم را بشنود. «شما برای بچه‌های ادبیات با کلاس‌هایتان همیشه پناه بودید. آینده ادبیات ایران را با نسل جدید و این‌همه تغییر چطور می‌بینید؟» می‌خندد و جواب می‌دهد: «والا غیر از خدا هیچ‌کس نمی‌تواند پیش‌بینی کند ما دعا می‌کنیم که ان‌شاءالله ایران سربلند و  مستقل باشه.»
🔹
یکی از همراهان می‌آید کنارش و می‌گوید: «یعنی امید دارید به آینده‌ این...» شفیعی‌کدکنی سرش پایین است و اجازه نمی‌دهد جمله تمام شود و می‌گوید: «بله. صددرصد»./ فرهیختگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/695921" target="_blank">📅 21:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی شهروندان در پل جکیگور راسک
🔹
بر اساس اطلاعات اولیه، این حمله توسط عناصر گروهک تروریستی جیش‌الظلم انجام شده و شهروندان عادی هدف این اقدام تروریستی قرار گرفته‌اند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/695920" target="_blank">📅 21:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695919">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiWaP9hTEYE66h9EOT2XAm0MuRwGouZ4YdHdqu0sePFvtiKgue2uBAAdKMHQA7uf-0AMLli-oQDjl98XPQ5TKZY5srRH96nITHWyseR71FLteci3o5afTwczzOPuTwwGNbFf1vOYevpd_snSPVWo7IR5sUuiVRTgKHYfPDKAfGZw8DpebyXzd0VW9BUiRTnC4LQGyEeHTM0xKFRsuMzPRPFkxiQ_Sz9kEcvZlOShhxbSUrPozneNoxiT-orgZ7U_QrRPtEp87k7oMB5hT_pfsWbRbOHKnp8n9ddcLBiceJVilIY28lWJo0WMfJEpwNUKQMfC_RwXddbbvX9N4pp9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجربه فرهنگی با اعتبار دیجی‌پی؛ کنسرت همایون شجریان در شیراز
🔹
کنسرت همایون شجریان به‌زودی در شیراز برگزار می‌شود و فروش بلیت این رویداد از طریق
فیدیبوآرت
انجام خواهد شد. دیجی‌پی نیز به‌عنوان حامی مالی این کنسرت، در کنار فیدیبو و دیجی‌کالا حضور دارد.
🔹
در این همکاری، کاربران می‌توانند با استفاده از
اعتبار و کیف پول دیجی‌پی
هزینه بلیت را پرداخت کنند و در صورت استفاده از کیف پول، بدون نیاز به ورود اطلاعات کارت بانکی در لحظه خرید، فرآیند پرداخت را سریع‌تر انجام دهند.
🔹
حمیدرضا سعادتی، معاون سوپراپلیکیشن و مارکتینگ دیجی‌پی، این همکاری را بخشی از توسعه کاربرد خدمات مالی دیجیتال در حوزه فرهنگ و سرگرمی دانست و امیر بهدانی، مدیرعامل فیدیبو، نیز از آن به‌عنوان بخشی از مسیر توسعه فعالیت‌های فیدیبوآرت در حوزه موسیقی، تئاتر و سینما یاد کرد.
🔹
این همکاری با هدف ساده‌تر شدن دسترسی مخاطبان به تجربه‌های فرهنگی و ایجاد زمینه برای همکاری‌های بیشتر فیدیبو و دیجی‌پی در حوزه هنر شکل گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/695919" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e78e0ce2.mp4?token=ds_Tv2p26b3pR8lSpJwjcDvH1JjO0udE4koO5wbpJOPlYvnE93Sdjqzr9WsNHaAvaqZSHuOThui6Y3OI6e0D0o2xPeL63xE7tOf2MYEPU-ED0tjNK4Snl_1WrIND3eGEbDYmoHFqXOjZoVL2pwey9OfYnSk1UqyML2p7cxYbpVK4izjPBXPH9JwgcfHdyFhCdIx7VqmhmkV3DGHcqpJMU-IIM90hhp9zDCJ12OB8KLe9uI4dC1LH0f1jJNfG0vNnhcOwv7C1SFVtW9SmNTXIYW8QHAgr8l4ZeYuEbbXBssYp7bcnWoAef9IPPpnq-Qm2WBYmKO0M0HLa0qZWGiVWJIVCSxKdH1qXZItNkXF6jFf6vFOVLpRyMBdADpi5e5-SOxMLVob6Ms3fgIzURMhZBfp_ceWsjhRqI4W5nt_mTdM57KQWSfKbAE-IzAxCadVSKeawjmm-kyJg1yew-o7FwNe2tLpx7V-BwzdS-ANKhtq3ZyLBB-EpY4-2sK-4utHFuZvaR3O70unS95fVh9uuHxDdrdUunE-adFHgaROHrt8u84AR6s_nJwAJr8MORoiGPRRl56yoETHje3DjDxUJuJ2EPAamMVbS4xnaoLfuCqAoui1rOeM7wwF-nSxT_qhJL0Nh1edmYfRrMSPr5n_0PLeVAkoDymcSGnZHkVizrV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطارهای معلق ووهان چین؛ واگن‌هایی که از زیر ریل آویزان‌اند و کف شیشه‌ای‌شان منظره شهر را زیر پای مسافران نشان می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/695917" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: کمک‌ خلبان فلای‌ دبی قصد داشت آن را به فرودگاه بن‌‌گوریون بکوبد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/695915" target="_blank">📅 21:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
یکی از فرماندهان پدافند هوایی خاتم‌الانبیا: ادواتی از دشمن به غنیمت گرفته‌ایم که در آینده نزدیک، به لطف الهی علیه خودشان استفاده خواهیم کرد
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/695914" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا حسین زاده؛ یادداشت ها، صحبت ها و سخنرانی ها</strong></div>
<div class="tg-text">#یادداشت
📊
داده ها؛ سرمایه های جدید صنعت بانکداری
🔸
در گذشته، سرمایه اصلی بانک‌ها را شعب، ساختمان‌ها و منابع مالی تشکیل می‌داد؛ اما در عصر تحول دیجیتال، داده به یکی از ارزشمندترین دارایی‌های بانک‌ها تبدیل شده است.
🔸
هر تراکنش، جست‌وجو و تعامل مشتری، اطلاعاتی تولید می‌کند که می‌تواند تصویری دقیق‌تر از نیازها، رفتارها و ترجیحات او در اختیار بانک قرار دهد. تحلیل هوشمند این داده‌ها به بانک کمک می‌کند نه‌تنها بفهمد مشتری چه می‌خواهد، بلکه بداند چه زمانی و با چه خدمتی می‌تواند ارزش بیشتری برای او خلق کند.
🔸
با این حال، داده به‌تنهایی ارزش‌آفرین نیست. ارزش واقعی زمانی شکل می‌گیرد که داده به بینش، بینش به تصمیم و تصمیم به اقدام مؤثر تبدیل شود. از این منظر، رقابت در بانکداری مدرن دیگر صرفاً بر سر جذب مشتری نیست؛ بلکه بر سر شناخت عمیق‌تر مشتری و ارائه تجربه و ارزش متناسب با نیاز اوست.
🔸
در کنار همه اینها، یک اصل اساسی وجود دارد: اعتماد مشتری. داده‌های بانکی بخشی از حساس‌ترین اطلاعات زندگی مالی افراد است و استفاده از آن باید همراه با امنیت، حفظ حریم خصوصی، شفافیت و مسئولیت‌پذیری باشد. بانکی که بتواند داده را هوشمندانه، امن و مسئولانه به کار گیرد، نه‌تنها خدمات شخصی‌سازی‌شده‌تری به مشتریان خود ارائه می کند، بلکه می‌تواند از داده ها یک مزیت رقابتی پایدار بسازد.
داده ها، سرمایه های جدید صنعت بانکداری هستند، اما اعتماد، ابزار مهم حفظ این سرمایه است که نباید به هیچ عنوان آن را از دست داد.
@Mohammadrezahoseinzadehh</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/695913" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9eb85747.mp4?token=JUIxMvOyqNRrjiOg3fsUm1xuTYH5-ZYOJ9JCS98p6z2rsrYEC9cf1qvXJ_XVqNzHE7dB3uQ6S5ZnKqM2EFPTGU9Y6pzU4F-XrNtIDqmx7qZdlkNQivScNh8wnlVjiC-B8EiHFZYjClWxrBwKPjOBGmHQ4Qk5n9Qf6FtlPQ33-Kay3jP1DJle1mfhwjUOmE0-Xjf5hw0loOyRqjfMcSNLxP4G-gw8N8DOLAGqVWY1I4konK0_yykJ8pNNWD1J5lrqG4EuZDrGWDhkPES-P6j8oJMi2wQLh9VjfnsDR3MpeNdC964WlKvzqzEAlByIb98Jw6PjB90RPKf32MdN0v9YcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های یک دکتر: حالا که هوا سرد شده به‌خاطر یک سرماخوردگی بلافاصله آنتی بیوتیک نخورید؛ بدنتون به آنتی بیوتیک مقاوم میشه
🔹
یک پسر ۳۲ ساله و یک دختر ۱۹ ساله به خاطر یک عفونت ساده فوت کردن. چون از بچگی به خاطر سرماخوردگی آنتی بیوتیک میخوردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/695912" target="_blank">📅 21:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اداره ارشاد خراسان رضوی، با لغو کنسرت علیرضا قربانی در مشهد، اعلام کرد: با توجه به «برخی ملاحظات» کنسرت به وقت مناسب دیگری موکول شد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/695911" target="_blank">📅 21:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9xHr1nMFZzCF8dBVkKNITfI1Kccz9Dg8GyBjxVGDkj5-kcknp7Cd_zU4qW3Q_Ywv6FEIAqi0lyqFImMf7NM-ngghHvWMFaZ2aMO1hUFg-h4QRQ1J6Yd5VV6J7pmwjZaA8v8cqXmGrcYKf8wHQyejLnpXg6C1mtznzZIyux8gQRjQn_dFZIPRKBbeN3uiGJ-gVsepvAS8aQJi5owR6GEYCpYB7Y187KTzwC5ElHRW6YqmJLXaJq2NHe-9aIEMz1Un0F-Z0P_Rszr9WVBJbZM9pFUNLF1eMukn3ltbaBomwqQWIzN7a-VuqYYXczDdMCyhzGltpsucvqB2dM4_zz8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر کاری، سراغ کدوم هوش مصنوعی بریم؟
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/695910" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efda9da751.mp4?token=td8jXMe0fnD6lxo4uPAwutkffOobiVcWtA0fD6T12E7c4cv5wdQd4GbkENaOYoTOATKE04K0TWsGHstN39uF3H3aanrWXqcNtzDdX59ml9Ldd5BgL4oH-IX-3V3Bw9jE7aBvy0qy4bKMJUHfdqsqPpeq0rkMQQY5zoexYrdVlAd_Q1qvcEM9GlKvC_hmBypM2gpn_BeJk4VO1zysXCRSrF4rBQNgVrmvFVIJm9vGpDQS8xWlMJkJfcL3qDI8hmuG8nHpj4CFAxYKEb8XABD8m6grPj7XtSQlxYK_MxzZoyVfm0x876WqrsRFYlOjW_007_DpeAjjWEvP_ny6CsYKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباهات پولت رو قفل می‌کنه!
🔹
یک اشتباه توی سرمایه‌گذاری هست که ممکنه باعث بشه پولت رو، روی یک دارایی نگه داری که دیگه ارزش نگه‌داشتن نداره،
اما نکته ترسناک اینجاست که ممکنه اصلاً متوجه این اشتباه نشی، چون این بار مشکل بازار نیست، بلکه احساس خودته!
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/695909" target="_blank">📅 21:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سفارت آمریکا در عربستان هشدار امنیتی برای آمریکایی‌ها صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695908" target="_blank">📅 21:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtMs3_qIy5BYpPrk5deIk4NvPetiJLhcPjTZ6esFVcRvCy9BwLBNswD_Xt5LbPycIrthDfaQDjGyzXoRv-F_2gLCyahOib71M84evqQhQ4TGawXazljnv7qNn5cBwCkcrYc_PgOBB8p3otB-5ayqe4NOlvfI6KQVKfSKlPvAybDfyXu47PsaaxXcgjlgssK-xi9k3hFpWfrR-PZsSsne9JZ2hH1Fp7v6BF5aByCfSh8r0wdEBtbqm-VjPSSPjWDlnarDvmHx0bCusEKEjex_FC2OpeTLTfcg0okAZRWS0fjmeWnsuk6hpMEBAjDAHiA8ZYHE_jQOfs4Gaw_NfYwybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جشنواره هدایای رویایی اسنوا
🎉
با خرید و نصب محصولات منتخب
🎉
—— بدون قرعه‌کشی هدیه دریافت کنید ——
با خرید از اسنوا، علاوه بر دریافت هدیه از تخفیف حین خرید هم استفاده کنید
💰
⏳
فرصت، فقط تا 15 مهر
❗️
🔥
برای اطلاعات بیشتر وارد لینک زیر بشید
:
👇
👇
👇
https://lnk.snowa.ir/snowa-telegram
.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/695907" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک گردشگری | TOURISM BANK</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzpjQAezmA0-vr0HN3XkuPXm56rF5IkawCe83D5f2ovb2Pfr_vsMwSdkZEuZlM4_aE5uS2FMeFtn63XLyg1mAcxUC65QOSPxJwBCUe-jOliUUA7OzrQR2u9Tt_DbnPKDwZbhDfy1A6QTCVDdIBry_BM8hb3ardSyOsy4rpEmmBAUc2nhoJ1sl8OIJU-bhHSCqqE0a45QGO15mHk6lN8aInduV-ugXpEfyiZQN8I3GPgpuUXYCKVimCr59MlD6v9tCVORVlOIiRduZ7CttC4YLQ12nRcQm_AA0YXM5rYdLCF1wLVgxzIqIAthJsJJzenkXsa_qNz8546leMXrQtxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تمدید شد!
قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک گردشگری تا۱۵مهرماه تمدید شد
دارندگان حساب قرض الحسنه پس انداز با حفظ یا افزایش موجودی می‌توانند در قرعه‌کشی شرکت کنند.
🚀
هر ۱۰۰ هزار تومان در هر روز = یک امتیاز
🎁
جوایز: ۲۰۰ جایزه ۲۵۰ میلیون تومانی، ۳۰۰ جایزه ۱۰۰ میلیون تومانی، ۴۰۰ جایزه ۵۰ میلیون تومانی، ۵۰۰ جایزه ۱۰ میلیون تومانی و بیش ۱۰ هزار جایزه نقدی دیگر.
📅
دوره محاسبه امتیازات: ۱ آبان ۱۴۰۴ تا ۱۵مهر ۱۴۰۵
🎯
قرعه‌کشی: ۲۶ مهر ۱۴۰۵
💳
حداقل موجودی برای شرکت در قرعه کشی= ۲۰۰ هزار تومان
افتتاح حساب و افزایش موجودی:
🔸
مراجعه به شعب سراسر کشور
🔹
آنلاین از طریق اپلیکیشن توبانک:
tobank.ir
کسب اطلاعات بیشتر:
📞
۰۲۱۲۳۹۵۰
__
🔴
بانک گردشگری؛ فراتر از مرزها...
@iran_tourismbank</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/695906" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSfMj4vMdIT3dlfHhTFWceXPQhtPNkjuQXzNt7hlMbl9jkzY8Yw7uVP1ztypHyPJTfS6ahjzJd10Y7YXgCO0_whZ_KK1TFm_Msr_2RCTBw6mIkcQ_BA0QBT2Fap9if2tySJgrCSqtKGnRnihpeFl4vXzzVqL3vAWseJMprCo8VslAx7jFJ98-E-wY-frhDCwx6AG7CtZxwnmvaHnwjjZNHtEpVqpJzZxENikiR4CD7R0nlurSO1wnvc42ykCF_Qdg3mERKFeHzz7PXrBZ_VxbsWSNTo-r1KceWuk9dwaGxgxfqaVnF2Gy8jNUUJRv20JmbFYUzDinvFYKn_S7MQzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRvb5kSS6z67vdOxwwgF_1dRQlhd417owVis4ILMMpu7CMS7nGA2gbqQY6l8Ia_VrVX0612YpN1fPxtxlTwTdC6cEKO1V7jY-3DCG_Hda6bZtIlWvVQ1UF2F3Iba_Zf6WOQHW3YboAlQh_-qxpd2L-3CpI4IH__7jIlCsD_WsU0jkJJnpc5ydg5YG2zQt3x1mARgzHAxj504eWL1am53AYGreb5hPMGFYE3FVffT7YntYUpFAj5OEOgGlmvgp1Pa205gbFuaEnEnAOCuvwGQc6RLdPPEgercG4tSyWHC3miJ8hSPAQT-iSF_dR9CiO2wIENP3su_4PWB0NeolBr5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIF8p6BK4f2U7CpUTR8wxUOUOcZfaJBX83zGxJJXOhEzqaJT152NJgHs-DiPJ0l197g9SDRqvnAcikaFyYUloAuuL8PCf9UNvBNrfQkPh_0JwyiLy0fHu2tPSfPFWK4cdpEE6DbeCXbMDX_V1M1i2kw2mLB_LZ4KdZz5B8og1hV84uRrCS_GRsjs4O9F2vKU_T3y3X5zb0KQ6LAM009s86f1YaoxOgEmhJe0wTSEwZdkhcMn3BBO4jJ97E3JS-oRZVZL4hnTOgpHa9SjCe4a8XTA840nMjPzyEKRB6YBFZxR9gYBwacNbqN51gHwvY2Wu08IlE15QdLVKHk1xqAwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgC3NW7TqU-dgZ3eKrekhZ6MUc_qb8aUurqU4LLjjw4dFksdfz3nF8xdtqQeDuLz369CvVxnUpTCf1Hoxf4r1Vv371bkPiDfWtPZ1bZ1tVBMZM2N8cJkgjnML8eLXynFeM2DGtmUWclRXL2aRUTuYnWCkMwdrxNRDgz7jYXr54XcG4qOvoPPM3JCyOEymUt2rR0oMHRSeNtB-EpDwMDBUiRXX1IlKJ1rXD0yUeRztpFT1aUyLiBkI_msOSeDduwyM_NJxAjcci1HD0E_ZZDkkFlqHilehd92JaB5qIbQoGargiciK6HUJuXaMeXluZDhtwlbE_8rvu2InFsAA2fjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB9U03riCS9I9JH9NPqamhUYg_GR6d8Uvh6u14TgT7vxmlPEoDpxF1HB-AqAlV0QQLFA2Hfk-vMfXUnQeV-UlTdHO7HrQIJAYoH7l6gHLv_Y0-21jOl-lotH-MqBvoKRHODOowMhXCCPUMQy26dMQaWAiOJreCyBNiv2Ca8_WQBGXlaH4b0Y1erc20d8kj295oXzvhWc5fC8bLxocxY3d5bgj5exhsG63SR_CnSNxcEuvNgMMnmNDaZ1C3lmMeWHLOF4oOazAPVum0sMGQQ3m-WrI1-_7f9bjdQDWka9568U_3vzUmnI5KL_b86NOWnuznulhNDFwas8LjABw1cM6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزیره بان‌وول در کره جنوبی؛ جزیره‌ای که در آن همه چیز بنفش است: ماشین‌ها، خانه‌ها و گل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/695901" target="_blank">📅 20:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGdITTRXQVW_qjCJ5U6VBClibYc03BM1pqtAVMbgVx38g45OPMnermXITzorv_4tgWXBrzc_JYHmc2k98H0YNVClR5QDEmNz1kI4fpjjNXXx56xqbtTOqDy8LM7o9ZCNujUJQXfWH_Fj_alJ-yt4L2O28E0q4foGhB5BRwJZrESZsvJnUTeYvmEKAhGpgPkPXr2qDpamh5rEnJxVMgdJd78ppu_4fjx_ogqD45hE_JFlNNRsMesLdcuVrOUpLj5QTDblP0OO1Oon-mvxXRhPwZKPNRpO8gTVLoUJflgRlRznUgfaDJqmWjgOfmfqriz5NLQx2K2xm_lhUl6OIXCiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌های نافرجام رفع فیلترینگ
🔹
در این اینفوگرافی، مروری بر وعده‌ها و اظهارنظرهای مسئولان درباره رفع فیلترینگ داشتیم و سوال اینجاست،
بالاخره چه زمانی رفع فیلتر صورت می‌گیرد؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/695899" target="_blank">📅 20:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VC_doKI7lbAue1gfUhUlRTRBxNCTqOl-lkw6NHAm92Yaj-68yUFEnnnJqgmrFYz1I-G8WIXP6XVLl6oL0G8HFBxQpkkgrm35MiV8l4zO_5MdTVFZp-TTo0HX1jyX87SHivS__b7p5M-2KXdtZcExqPa4EXUJ-oykPmtSh-dc7DogGmt0xofR5fSsA63SPps6PiXe6_29LWjSe8Ox_B-ke2KGk6JseYLGvDJtlpk2X7pfSLOI_m6glnar_iOZ0sfQfM88QQCyRPs6u4_szMz8zVNX6U_QSv0HvMqpYCIK0XQbDZZuihw_kNVtenHlgSuuSyQqrwtU_Me45DC4ysHzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB5EIToT8dIjIlh0Bk6k3rXZdpRBJyUpq4QFCGucpQT-LRW6MIhcrTHlUy2UXZuLJ9SZ0ex2tPSdgCQu041J2-cDR3xn-2OW-VnOQSBXS0z8Ax7bAZpXNH4uSrD2sUGgBZp7T7YD08QjDeC9K4I-MFbQFp9ACf9Cfq4AK5Af_sImXZ_DQ5k3QoDQNR90dhRGAP1M1FzS3GflfSF_B_YilvHcDcT7E0TaD9y-uiqlOZMtUYLAGj_FAhtLe3Sq82nlpvSl9Dbyc8hmZw8ZsU4O1-zV3Hw3ZFg9uv_08J_PnW9xPQzmOmXqNnW2dzkjD_buCXP6l6Z6jq2djfmPG1Mk7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع خبری از اصابت مستقیم یک فروند موشک به فرودگاه ریاض خبر دادند
🔹
در پی این حمله سنگین، دست‌کم ۱۰ هواپیمای مسافربری از فرود فرودگاه ریاض منصرف شده و مجبور به تغییر مسیر اضطراری شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/695897" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پزشکیان: آمریکایی‌ها تاکنون ۳ بار پس از گفتگو به ما حمله کرده‌اند و این نشان می‌دهد که آن‌ها به دنبال گفتگو نیستند، بلکه هدفشان ساقط کردن نظام جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695896" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">طلا و تترم رو نگه دارم یا بفروشم؟
از موج صعودی اخیر جاموندم؛ کی طلا و تتر بخرم؟
همین الان کدوم بازارها هنوز نقطه ورود جذاب دارن؟
نرم افزار مشاور سرمایه گذاری اکوتراست
👇
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
برای دریافت نرم‌افزار کلیک کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/695895" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okVdHwMNDQNFsb0EZ5J7WKE8wmyLvSlVnly5W3V3B1wEPt-eEvtqrmYKrfE_CByRKgUb7CGpzULxI7RosXQNSiEL-p1qNmZCJI1CHqeJuvqJo892s2l5zyev753BEzZYL7-PGUoGHEL5O4zwEWN9Kq4L_WDZKlctopOGWITQh63UomRAi1QccUSD2SDSORmb445PA0jZnqK8u8d60YbZnAZAovcAgKqrTLvtUzMgDkWFsAhZBUfHoAxzPJaezKsc9dOoOdKmeV6zLm2nkQJDpIsap0FiourEo_Ypd_tImG6XTS2k60CukBX-dwro88wDzNAOT7_Lw79-ril2lhkQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر بعد از موج شهریور، فقط ۱۴ روز استراحت کرد و دوباره وارد موج صعودی شد
🔹
ویس زیر رو بادقت گوش کنید
👇
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/695894" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/695893" target="_blank">📅 20:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پزشکیان: با دشمنی که هر روز ترور و تحریم می‌کند؛ مذاکره معنا ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/695892" target="_blank">📅 20:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6708cb5096.mp4?token=Qe1IacYnrxrV8zuSZTgJPDHcjoOD9B7gaVnZvBoiTL-9S5H8zdRw1PQZX1Fkted16xVvXXymuwhjbL-C9PkcNsdpQP815X_GFy1X5WCmbwojO7mtoazlpXXeBrJa9k2kvMRS56YPKCMrHfr_LNWEaAHPOZ6rDWEu9fi5EuBQGxwVMiQi3NqJnp_pCR6YRqJGGb7H8ZOH5tNehYIKc-CojupsWCK2DvzJaHM23nyHQWY5fRBjk6pHcYc8oFJic_PMddiVd5hvWAriYX5k939XkU10ztmaALGpr_u5dB1ZnJcWY-fu_wkaAuvv00nnC7nqfyIpXrLp6VKnb4Hu5Y8pgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6708cb5096.mp4?token=Qe1IacYnrxrV8zuSZTgJPDHcjoOD9B7gaVnZvBoiTL-9S5H8zdRw1PQZX1Fkted16xVvXXymuwhjbL-C9PkcNsdpQP815X_GFy1X5WCmbwojO7mtoazlpXXeBrJa9k2kvMRS56YPKCMrHfr_LNWEaAHPOZ6rDWEu9fi5EuBQGxwVMiQi3NqJnp_pCR6YRqJGGb7H8ZOH5tNehYIKc-CojupsWCK2DvzJaHM23nyHQWY5fRBjk6pHcYc8oFJic_PMddiVd5hvWAriYX5k939XkU10ztmaALGpr_u5dB1ZnJcWY-fu_wkaAuvv00nnC7nqfyIpXrLp6VKnb4Hu5Y8pgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از یحیی سنوار، رئیس فقید دفتر سیاسی حماس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/695890" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پزشکیان: با دشمنی که هر روز ترور و تحریم می‌کند؛ مذاکره معنا ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/695889" target="_blank">📅 20:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hY1EuGG3OBBpGZwktQ6y0obVqF-tMVLQg3ecJylvz1UZFqJKKMW7k1JQ_Kunax5RN_RM5tZlibKkwQrgW9zZW63c4LZcs_g6aohziUD4Ih6-7tY98mJiyQzMNeA-d_2OO0l6GokFjuwpudclL49YRj4HIcRPsC5ammzuulzDhJv1gjjWvvaTtM46BO71c3Bd9hx1L62P3Pj3PYzdbokRjWYK9hw94mrbFmx-xcv1HN6-BzA00_1YwSeoz-Z9lbD_RCXIMgC_LXSqqY3zBWWKwea0_hlUX6LjOxjHpbsTeAGgocuHsVl-K0iqrLsK3a-w9wTGZufMAbjyec-osH9jNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gopQNKXAaz7tTXVtsAv4__61V_NXWXtuljUAHmTmP_Wwu9n-7iSw8cLXi0g97vwLBST7HWZQGSy7BsYufwH-1OOtkJT0AVhYjUaraKbxCB4eEpJXM5JDpgm2fUr6gWKNne6mDbNvbjmJt3Bdp-83cWpEiUhc1SPTUMEXGcAxHXFJKIZOjKoshgLIwALpEZHJ0G6qr7idghx6eYKpzABcz6Led40SPMx00Qhv0dW_SXdmTaSxOMf4Fj_Zm_4ZP7h8WaQXrDDpaMtlfh87wfKJZZ-5NhooQWdb00IFT5oKVGwOygJqyvW9yDcbhXEN1EQhCo-bBdaAG8J051Xln23zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Ri9cTK31Ia2qhxaA0Ld4bpbXdSsnchunXif6S3iNelVc_N4nTbJxwK52HDlDqPjxZlRpStdpdE2nc-m2WUiFrH05NjqSLhVNtOu2dKyfyjNaA0PjtVHkB4Yc9xQwdBnYU6dF-2Zk8mcio6v5u3qd73uGP2aghljOISrb2xhw2RXrWuG2BfLadfe9El-LpeAMatBatdRMIjiQ05UjJuzjd-UQiLCydMRyxQGyO1yns3avb9B89Q9SM5ZlD-0KeqYIKIWLTo-aXwIRnXTpzyipMxk4GXRBA7UfoGWpC0XkItr0VxZPALgz67xuaRmr_Gx0eGMAhH3CkP6Wdjin__fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwmaJZod0M2io8Xu1Giz2ikVS3NpilprwHGe5QXHPxHEfuGJPOAZGt_CgEn_jPgITteKnSAIObr7eeDpPheZI6ihwb3EpsSA5Jfvi48ZBnCtJjdQKzTT8DodfWo3uhpKbqogGeCy0qc7bzRQp-6UMpnj45_XID7oXbCmFJzgff8FgWnmzX2tO0w0CZJc5adOH17qPLw6J2abNN1wwPTnvwdjJyZRgVghe72Z86VBeqc4tQp8schkyvXyiKdMQgRpLjsy-2DYGwlgkMFRIxuOqNvMlqjRWKIUQgv3A527gH-rCJfWCEaWPiq9i0ukJxlAx_wKTtGCD29z9bvQ4TiZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFLL5WWovwh0cAKU_1cd-KA6w2Pr5ArPCIRax1t2DvC12Y2VYuys802HMO1fSJPobp_uvO4PEoxAHuGUpoZqKw2ukFljTd8D3GfXH9fOlvVTtri4Msk3TbrgX7hJX3OMK3FE58oPZA8yr2OafnCFYtPOl22_iMHRt_pdSSC4aBo3X5OBajKLogGpQeUdCt6cgoIqRUOs38EZev3Nk6wlxgLkzeJsiuqd_WNpxlH313drW1JWxRC-MKRhuQtULL4qyf31XUqL0fGs3IvLE20NOroI1t1zI4r6SVn16TfVonYl49kzrS4OJ_1j3WJVwedfLMvPx0GtKSoWLF6EY-Llpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ورزش نکردن فقط فرم بدنت رو تغییر نمی‌ده؛ بدن از درون هم تاوانش رو می‌ده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/695883" target="_blank">📅 20:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بررسی دمای مسافران در روسیه برای شناسایی بیماران احتمالی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/695882" target="_blank">📅 20:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmKYvi27hGu1X2icHcD1r10uZ2XZjWS6_GTTvyPhC9QDvqDdDCkAJ68hNp2ri7bMXA1GMLHNg7cTBTY-zKBrzQwwPjFYerz3JFX_6OlVl18yO20ycqqfgmzRgKqu2AJhwrkxzkfu4yQzYadj-O_aZIWB_DRlqSNTrIRY5QykA_YoJp5wIUmzwEl-sLFQaa3c3zKxP6Thzi06pbMSnAIb94uqW9sRwnwZ1zFD2SZBncdxY865s1Ojnpb4-Mdane_GQvYBj8phuiImhsaVJFxIzdCON3GFccONBhe3ZPzRM_jqVQhoxAPWC7OSV5TPvwqAUOg1QJptlWl67nlOws_wiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کابینه تکانی
🔹
کابینه دولت چهاردهم در آستانه یک تغییر جدی قرار گرفته است؛ تغییراتی که پس از استعفای وزیر نفت، شهادت وزرای دفاع و اطلاعات و مطرح‌شدن استیضاح برخی وزرا، ضرورت بازنگری در ترکیب کابینه را بیش از گذشته نمایان کرده است. حالا پزشکیان با فرصتی برای اصلاح تیم دولت روبه‌روست؛ فرصتی که می‌تواند با کنار گذاشتن وزرای ناکارآمد و انتخاب مدیرانی توانمندتر، به جای آنکه تغییرات را به مطالبه و فشار مجلس واگذار کند، خودش آغازگر یک خانه‌تکانی جدی در کابینه باشد.
🔹
هشتصدوهفتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/695881" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
احراز هویت تصویری کاربران حقیقی ایرانی الزامی شد
مرکز ثبت دامنه‌های اینترنتی ‎.ir و دات ایران:
🔹
احراز هویت تصویری سطح ۲ برای کاربران حقیقی ایرانی الزامی شده و ارائه خدمات تنها به کاربرانی که این مرحله را تکمیل کنند، انجام می‌شود.
🔹
تکمیل‌ نکردن این فرایند، موجب محدودیت در دریافت خدمات خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/695880" target="_blank">📅 20:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StlaJMHWaCOJBbInB8Vm2jnjomXIASGGbHPbA8DWagFuJwVfnyeen-K8peRg8nrNBCkAB4uoeGoIo47bVMl3P1H_VE8BhSVcqPqFQK0HgcS3arvFkPumYuh8DveqV1usvCZgSKhjee-s1kqy1Jljyox5gtwgG4IEDusYy4a7Sk_AHBQjSAntZysEobo92qjubNl_X3GuChcvKK3UazNpUbYynuKImN2VfDhiGX_GkbgH2W8xb1389S5thS04lczTQQKIda3P9DuVKFj-bcG6jctghx3HStu6clSTzy6vmOWj9J_QZFpvUWLem_iFYCj9t2kPaM1MHHKMdTsOfzckgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه تراشی تازه ترامپ برای توجیه قیمت بالای سوخت
ترامپ:
🔹
دیگر تنگه هرمز قیمت بنزین را بالا نمی‌برد. حملات اوکراین به پالایشگاه‌های روسیه باعت افزایش قیمت بنزین شده‌است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695879" target="_blank">📅 20:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">22-2 Ane Manaee (1404-02-09)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/695878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ودوم؛ بخش دوم
🔹
در ادعا تابع، در عمل منافق! نحوه مواجهه برخی با مذاکرات برجام و توصیه‌های رهبری [00:00]
🔹
وقاحت سیاسی برخی افراد در پذیرش عدالت و قضاوت، و استانداردهای دوگانه آنان در مواجهه با نتایج انتخابات‌ [12:44]
🔹
معیار "بستگی دارد" در برخورد با مسایل سیاسی، اجتماعی و دینی، ‌نشانه بیماری قلب، تردید یا ترس از عدالت الهی است. [19:39]
🔹
وقتی ملاک منفعت است، نه حقیقت! نقد و بررسی استانداردهای دوگانه در عرصه‌های مختلف سیاست داخلی و خارجی [23:49]
🔹
برخورد دوگانه دنیا در مواجهه با تروریسم، دموکراسی و حقوق بشر در مقایسه با رأفت حکیمانه اسلامی رهبری [32:53]
🔹
تدبر در قرآن، نه‌تنها تشخیص‌دهنده بیماری دل بلکه درمانگر حقیقی بیماردلان است[37:30]
🔹
تدبر، سفریست پله‌پله، از ابهام به وضوح، از تردید به تسلیم و تفکیک میان اهل هدایت و اهل ارتداد [45:11]
🔹
فهمِ مکانیسم "تزیین سوء عمل" و "تکفیر سیئات"، آغاز هدایت، ولایت الهی، و باز شدن قفل دل‌هاست  [48:23]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695878" target="_blank">📅 20:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaab9ac46.mp4?token=IsZ5tzvVIaAVSNblrGVdWfVDsp8OlP0yi30NnTelUTTG7SLl0dPtvTKSclpFj3YC_bhTfgwi0UZxlhkrmjiAtlJZwS-XWjekc0jxsgDtiWEnc5Nz01vXQytV1oBdtScmZuwoBLc81n2j0uBGauRXyF_W2gYb3g-MUmEef8Ps-rUZqZ0fRK4o5FuMMwNy5IiaCiWzXxkzRnz2L35P4HR_y_fVTiArWP8tht_zxlZXcnD9sl5DdBb3XCIkfBmXfP-cQbKwAoMy4fTTJCLYzqmnVCH9z3WIWsuLjS_kyrWXhAC2yrL9dEWhaW7a1HMUUN4AxWV-dQ9ucogQ_Zoa0q-ryUb1DBc42erXfqYGlgiKCVV1907XuqtfMQqsbxULwlFeViCl41rZR_y-DrA_ExSmmIb1chTfgC3o8Q_JHvmfp5SUd2JdV9OuVXgjcv-volk9i9c2ZahY7tYROeU-E9toTrHBP4dX4U3buS1aR_uaO1vHBmCAZj1MAW1l73UJ5sJq1iZi-p2rt8-SVhXU9czy26uyN21k-ZNKUn3XswSRGMuMymFX4AVcLXmevsI_hQH9-kgTrB9rOnsgPtw6eFhgAVpKu5GE-6hJjzfcZCl4N7YbCqla_9c_TFVVig0YmeeRoBAnvqbijOp_mDTpTXpNfUOCg1jGSzSvDH9MEyEExMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaab9ac46.mp4?token=IsZ5tzvVIaAVSNblrGVdWfVDsp8OlP0yi30NnTelUTTG7SLl0dPtvTKSclpFj3YC_bhTfgwi0UZxlhkrmjiAtlJZwS-XWjekc0jxsgDtiWEnc5Nz01vXQytV1oBdtScmZuwoBLc81n2j0uBGauRXyF_W2gYb3g-MUmEef8Ps-rUZqZ0fRK4o5FuMMwNy5IiaCiWzXxkzRnz2L35P4HR_y_fVTiArWP8tht_zxlZXcnD9sl5DdBb3XCIkfBmXfP-cQbKwAoMy4fTTJCLYzqmnVCH9z3WIWsuLjS_kyrWXhAC2yrL9dEWhaW7a1HMUUN4AxWV-dQ9ucogQ_Zoa0q-ryUb1DBc42erXfqYGlgiKCVV1907XuqtfMQqsbxULwlFeViCl41rZR_y-DrA_ExSmmIb1chTfgC3o8Q_JHvmfp5SUd2JdV9OuVXgjcv-volk9i9c2ZahY7tYROeU-E9toTrHBP4dX4U3buS1aR_uaO1vHBmCAZj1MAW1l73UJ5sJq1iZi-p2rt8-SVhXU9czy26uyN21k-ZNKUn3XswSRGMuMymFX4AVcLXmevsI_hQH9-kgTrB9rOnsgPtw6eFhgAVpKu5GE-6hJjzfcZCl4N7YbCqla_9c_TFVVig0YmeeRoBAnvqbijOp_mDTpTXpNfUOCg1jGSzSvDH9MEyEExMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج ترفند کاربردی رانندگی که مطمئنم به کارت میاد #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695877" target="_blank">📅 20:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_z391mofX5CgoJ5sUL6s1-YQbugIxvc1O3tdkxBPnYKJMEu07Cd6uP0cHRxQvv7RwGNaUqfws_9IsdgitkQTb6IWJYBrlAZYvFiyPovLcg4sFdGUBVZIS5jzqDwHAS6K8Q2xD7ZJlVeG7X7koTTrnbGoFgPnE3XHjHgO8YRw7JHMQOsiniV-iD7ok04OkQhtf3X9wof4k4CX1z-RIciURkBA6SF2VuKasy1IeKNdF-fJeR7bjwVg1rw-k77DBxWgZrCaTirhWb7Nj7039BTyaSnKNkB4mG0TUg3l_K8OqYPerNMF8HK1CUU4VDdRu5e0w3mTen2jiqbLpLETj8bHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یک نئوبانک تا یک اکوسیستم مالی
بانکداری دیجیتال دیگر فقط به افتتاح حساب و دریافت کارت محدود نیست. کاربران امروز یک تجربه مالی ساده، یکپارچه و متنوع می‌خواهند.
بلو از آغازگران این تجربه تازه در ایران بوده؛ مسیری که حالا سایر رقبای نئوبانکی هم در حال حرکت به سمت آن هستند.
به نظر می‌رسد رقابت آینده دیگر بر سر «خدمات آنلاین» نیست؛ بلکه بر سر ساختن یک
تجربه مالی کامل و یکپارچه
است.
مطالعه خبر:
https://www.khabarfoori.com/fa/tiny/news-3250214
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/695876" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4_628VDq3Pay9wNuzUiU1agQ0hSHEp1MU5msY-HIyPhkoqo2YJLT9G-REtp3eSsJy5Xug1RZf60vvm_4xJ-ygRyZtpj5D9U8m8Y4Y7k9MdNqbfPfXypvr7L-a710Ec-Uqcu9fcxBG-p5dS5opXnBOO0s7ulIBoj746cTJPLFK0gzbbIizZ3z3VuegfATJ966zkoOTrKLJDkJJ9p9MqMGbZ4ZNAeJCmWDpeP0OB8dlBiCO89VPlYuLWeRHXJ-BbrtvJaQsq6SM9W-02p_D7n63v9E_ZPHQHJGzSyQhhnmLvG02sVmPTxUrICvTxY3HM1nataPRniHpMpRKIBQiwp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کاپشن امسالتو ۴ قسطه بخر!»
❄️
🏔
با شروع فصل سرما، یه کاپشن گرم، سبک و شیک حرف اول رو تو استایل زمستونی می‌زنه!
🧥
کاپشن مردانه مشکی مدل Hamto
▫️
طراحی مدرن، بادگیر و فوق‌العاده گرم
▫️
تن‌خور عالی و دوخت تمیز
▫️
رنگ مشکی مات همه‌پسند و مناسب استفاده روزمره و سفر
💳
شرایط خرید آسان و مطمئن:
•
خرید نقدی:
۲,۳۸۰,۰۰۰ تومان (
با قابلیت پرداخت درب منزل
)
•
خرید اقساطی:
۴ قسط ۶۶۰ هزار تومانی (بدون معطلی و بدون ضامن)
🚚
ارسال فوری به سراسر کشور
📥
جهت ثبت سفارش و کسب اطلاعات اقدام کنید.
https://memarket24.ir/product/fast/64834/180124/
خرید قسطی
👇
https://memarket24.ir/product/brief/64834/180124/</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/695875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اسرائیل هیوم: ایالات متحده به اسرائیل مجوز حمله به گروه‌های شبه‌نظامی مورد حمایت ایران در عراق را صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695874" target="_blank">📅 19:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
روایت کارشناس مسائل نظامی از ورود امارات در کنار موساد، برای کمک به گروهک‌های تروریستی در جنوب‌شرق کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695873" target="_blank">📅 19:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695872">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای
مقام آمریکایی: در حال تشدید محاصره ایران هستیم
یک مقام آمریکایی در گفتگو با الجزیره:
🔹
نیروهای ما از اواسط ماه ژوئیه، در چارچوب محاصره بنادر ایران، مسیر ۱۳۰ کشتی را تغییر داده‌اند.
🔹
ما در حال تشدید محاصره ایران هستیم که از نظر اقتصادی دچار مشکل شده است و سنگینی فشار ما را که ادامه خواهد داشت، احساس می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695872" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695871">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900a6d1b76.mp4?token=t3IetlMjaLJTp31wnz46W8oUswDv94gQLZutPLI6UzyKxlXjMZajEzbV0aaN1uKyXwI0jsSTOUvGh2a5yYGGzJL2Y7cQZnELTxN0jkzaEFhM5yeUUe5L8md5u2PivNc1_eCU1K-tfmcC3GBZcl9yuXrUqOvWrgD8vv6YX1w48rW3qhOrDec34rGUeAA3SbFspAJCL0HG-h-pyiENOuILyODlyN4EiEfqRVBe2zVelrGL5ebmTnqFBBYcKuePEdUFv_UWSxsA5hNrei18JQXxm_G1ttg2qm_R8juBZ4qwp6LJwPCkVawxovSK1X74JFrfHzS83m1YY8ZlXp-DFKGTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900a6d1b76.mp4?token=t3IetlMjaLJTp31wnz46W8oUswDv94gQLZutPLI6UzyKxlXjMZajEzbV0aaN1uKyXwI0jsSTOUvGh2a5yYGGzJL2Y7cQZnELTxN0jkzaEFhM5yeUUe5L8md5u2PivNc1_eCU1K-tfmcC3GBZcl9yuXrUqOvWrgD8vv6YX1w48rW3qhOrDec34rGUeAA3SbFspAJCL0HG-h-pyiENOuILyODlyN4EiEfqRVBe2zVelrGL5ebmTnqFBBYcKuePEdUFv_UWSxsA5hNrei18JQXxm_G1ttg2qm_R8juBZ4qwp6LJwPCkVawxovSK1X74JFrfHzS83m1YY8ZlXp-DFKGTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشت عفونت ناشناخته از آزمایشگاه طاعون روسیه/ ۲۰۰ نفر قرنطینه شدند
🔹
یک کارمند ۲۸ ساله آزمایشگاه ضدطاعون روسیه پس از شکستن تصادفی لوله آزمایش حاوی نمونه زیستی، به ذات‌الریه ناشناخته مبتلا شده و جان باخته است. حدود ۲۰۰ نفر قرنطینه شده‌اند و احتمال طاعون ریوی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695871" target="_blank">📅 19:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695870">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
یکی دیگر از افشاگران پرونده اپستین جان باخت؛ او نخستین مورد نیست
🔹
سایمون آندریس (Simon Andriesz) از مراودات تجاری میان هاوارد لاتنیک و جفری اپستین پرده برداشته بود. او نخستین فرد مرتبط با پرونده‌های اپستین نیست که از زمان علنی شدن این ماجرا جان خود را از دست می‌دهد و خبر مرگش با ادعای خودکشی منتشر می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/695870" target="_blank">📅 19:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695869">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYBaFnUcry70dUw3LfNk_8wu7euiZbHOVCPXBNQzV40cu43DkSNLGdyp-Av1nYnCULsYAyWDNl0GtUTiKZ6zZVjFVwhJOEGYPCM4ZSSzZaFccLkUj74B470MIKOMpz3yva6PgDb7FmM6CvDpY8uZkRLOjCGsOaSS5zT7pJmprWiaE9iH70pMO5IQVf2DAkq_ZckMCIPD1s5m67tlh0F1RpcysLmpEneHx8qQ_PNBdFfiwxVvPP-sxuh5-iElkrei2gFdT2tAc7VYtUfbKM8tZmx_uxvBejR411QP18YjYo1p3yAmv470HN6gKwNekJVVZiTGIO8PmuleRev2pi6ZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سوئدی: اطلاعیه تحریم‌های آمریکا نشان می‌دهد که ایران همچنان برای عبور از تنگه‌هرمز حق حفاظت (پول جهت حفاظت از کشتی‌ها) دریافت می‌کند؛ موضوعی که به نوبه خود می‌تواند نشان دهد یکی از دلایل افزایش جریان صادرات نفت از خلیج فارس این است که بخشی از انتقال‌ها و جابه‌جایی‌های نفتی با شرایط موردنظر ایران انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/695869" target="_blank">📅 19:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695867">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش و پرورش مجازی شدن مدارس از ۱۵ آبان را تکذیب کرد
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
درحال‌حاضر هیچ بحثی درباره تعطیلی یا مجازی‌شدن مدارس از تاریخ مشخصی مانند ۱۵ آبان مطرح نیست و برنامه‌های آموزش و پرورش بر آموزش حضوری در تمام طول سال تحصیلی متمرکز است.
🔹
در صورت ایجاد شرایطی که نیاز به تعطیلی یا تغییر شیوه آموزش داشته باشد، موضوع به‌صورت رسمی اطلاع‌رسانی خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/695867" target="_blank">📅 19:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695866">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزارت جنگ اسرائیل: ۱۳۰۰ نیروی نظامی و امنیتی اسرائیلی طی سه سال جنگ کشته شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/695866" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695865">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a06532b0.mp4?token=XROFzRmVSuIeOgEWKQE4k0MkXfKG12zUYPBKbokkZtGzQtF7URjW2MWDih6f641tn6mvIbnlhm7KTltkgcOyULqfLWcZ6SFAY6eex-vNjMmxVuN1B118wrIabr-K9tazEAkdES47QPqZhaHlWbB8oTP2lEr5rLYg9tu5LMRZegG0eiJDO_KxDGl1uV0RGCUlBqtwdM830ggiT5CVB73-7mVrkzNsKZu3mrvZlvjRPSBI5WGeCF3Kriv6E7S7rM5zmoaxZ_9MPyJO-MZQlRWMzb5axM_toxXnLcGqPU_Qo1JMoW0BZJ4JMS674-qHd8tHCroPJn53O-wzli9HK3okhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a06532b0.mp4?token=XROFzRmVSuIeOgEWKQE4k0MkXfKG12zUYPBKbokkZtGzQtF7URjW2MWDih6f641tn6mvIbnlhm7KTltkgcOyULqfLWcZ6SFAY6eex-vNjMmxVuN1B118wrIabr-K9tazEAkdES47QPqZhaHlWbB8oTP2lEr5rLYg9tu5LMRZegG0eiJDO_KxDGl1uV0RGCUlBqtwdM830ggiT5CVB73-7mVrkzNsKZu3mrvZlvjRPSBI5WGeCF3Kriv6E7S7rM5zmoaxZ_9MPyJO-MZQlRWMzb5axM_toxXnLcGqPU_Qo1JMoW0BZJ4JMS674-qHd8tHCroPJn53O-wzli9HK3okhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه ترفند کاربردی برای کاربران گوشی‌های شیائومی
🤳🏻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695865" target="_blank">📅 19:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695864">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اعلام قیمت خودرو در بازار متوقف شد
🔹
پلتفرم‌های خودرویی در اطلاعیه مشترک اعلام کردند با توجه به شرایط هیجانی و نوسانات فعلی بازار، موقتاً امکان به‌روزرسانی قیمت خودروها وجود ندارد. به‌محض ایجاد ثبات در بازار و روند کاهشی قیمت‌ها یا رسیدن به یک تعادل نسبی، قیمت‌ها مجدداً به‌روزرسانی خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695864" target="_blank">📅 19:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695863">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwjpQf7qVKGt12Hb5Hv2ipAQcWHmqiu1gzddrgkE92VRNZxq7vNbSC0TbvIZ0nkEKaM2khRk8vY6glFV0DWq2s96pMu5FSX3PMxlhnc12k2K31txyBiTFX7WJbjeP6LCyEl9s8oLc5QCLYXNjV3W4IEic9dUQ12dBbz6eF6GfDJHB4zxyy2PqJ7dCM64HQozeG3K7kZoDywGnRv0gTKp6Asa4TfMLtwhHCSnlrI5-fFoA1nHCwNhC_XJLy9KNofyOg6IPNSsK_KO0tgWO7VZqZijB7TdsC32W_k7sdVn-RBrvoLuGFFJboDjqQy1cWQC2iy3jK5yTcUEs3JDEfN1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجری: آیا این یک دیدگاه یهودی است که بخواهیم کل غزه را نابود کنیم و کرانه باختری را به اسرائیل ضمیمه کنیم؟
موشه فیگلین، سیاستمدار راست‌گرای افراطی اسرائیلی و رهبر پیشین حزب زیهوت:
🔹
صددرصد. تمام عرب‌های ساکن غزه، حتی نوزادان، دشمن محسوب می‌شوند و دشمن فقط حماس نیست.
🔹
هر کودک، هر نوزاد در غزه دشمن است؛ دشمن حماس نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695863" target="_blank">📅 19:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695862">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCs_YhvjrAYwPY6tiH8g_d59SBZLRnj2f7sCero6p9VPzeIQ2EIdijBUVtK7t2MAMvK12CAoXklodmwj-HyWU1Jmfnca8N2LW8JOH2bOomgRInt-9DW-ehWLhFhElMuwddM2IpMbuEYIc_Lquc8lMa127awp9WiXQr5lzvwgIFn3N0b9ZE1UHtdM-Ln7EMwDvasoq8A74QPRDyTxz1vBzR7Ft09g1Uaq71n0Kw1R_Qg-BECujC2LETKW62Pxpw6x9PD0ouNUi4LrNIhVFWvbr2mdKDcUZQPhtoybpwgjuUQG82VlJEi5CBndsLiwcB9kK_VdZTqa8eAnkBEgpdxQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خوب برای حقوق‌بگیران: اضافه‌ برداشتِ مالیاتی، عودت داده می‌شود
🔹
رئیس کل سازمان امور مالیاتی نحوه استرداد اضافه برداشت مالیات بر حقوق را به ادارات کل امور مالیاتی ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695862" target="_blank">📅 19:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695861">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eb7e86ae.mp4?token=Jdy-FQrR5IW4c0I_aF_fCO4vMmVyEzqUcqFjVKXFVyxGsuDcS4Wesn1__-l5JCeEBbH_V1CQ5VYe78rWrI9wyxhVzIaRsOnnzHa3cw54ktfnSkkIBuK9WXjZxTxMhzl2MI89v0MOZ3R59yfXkw-nwofppojJ6iHuEj5EXYTClSfLlO7Dg_0MMiQVYxYbHtRDY5ktGC30ACtJIgXIwF61kaFe18WQx523Fts2H5QtmvbJHVbnincMoBdsaY_ILvt-YbmWB135TQuGSaHj4jbpUjh-pnc9I53QEYs9Lg4U_4xqpd6EV9yjxiiaCFqRPUsfUuOgP9WH0opstExbYX7mLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eb7e86ae.mp4?token=Jdy-FQrR5IW4c0I_aF_fCO4vMmVyEzqUcqFjVKXFVyxGsuDcS4Wesn1__-l5JCeEBbH_V1CQ5VYe78rWrI9wyxhVzIaRsOnnzHa3cw54ktfnSkkIBuK9WXjZxTxMhzl2MI89v0MOZ3R59yfXkw-nwofppojJ6iHuEj5EXYTClSfLlO7Dg_0MMiQVYxYbHtRDY5ktGC30ACtJIgXIwF61kaFe18WQx523Fts2H5QtmvbJHVbnincMoBdsaY_ILvt-YbmWB135TQuGSaHj4jbpUjh-pnc9I53QEYs9Lg4U_4xqpd6EV9yjxiiaCFqRPUsfUuOgP9WH0opstExbYX7mLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ونس: ما با اطمینان نسبی معتقدیم که ایران در تلاش است تا همان کاری را انجام دهد که دولت ایران در طول ۴۹ سال گذشته انجام داده است، یعنی اقدام به اعمال تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر. ما بسیار محتاطانه عمل می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/695861" target="_blank">📅 19:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695860">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa41670cd.mp4?token=B5X73SarV1whl5ETtIK0ODG4Kheodcw750KqyEf4aKBYYV63UxBvfvIuRnIlyqPms70S2vB7P4icXDt-n78wHVkxAD615IJJDxlXHoqe1spbpzYuLKTdLoCGCiit54M6Nfd3V4cVzdevMx3pBQp1vqKKT7QayJW_x5LIIByBqAx7brVu3iDOCOeckVQ1n6bRQb5ZW9-XMJU8bzTVMAxrZUmGbfEYZ0fQNBoWLtronj1_LNhbBKYePN4AFIsGPbt0GiVLNS6H8nMJCO01JYCqiXcCYQmoVuXXeZhMsN-u4vKfXsuQFUg3RGneiR-oRZv6oNo16cK-EoCr3MxNhomRbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa41670cd.mp4?token=B5X73SarV1whl5ETtIK0ODG4Kheodcw750KqyEf4aKBYYV63UxBvfvIuRnIlyqPms70S2vB7P4icXDt-n78wHVkxAD615IJJDxlXHoqe1spbpzYuLKTdLoCGCiit54M6Nfd3V4cVzdevMx3pBQp1vqKKT7QayJW_x5LIIByBqAx7brVu3iDOCOeckVQ1n6bRQb5ZW9-XMJU8bzTVMAxrZUmGbfEYZ0fQNBoWLtronj1_LNhbBKYePN4AFIsGPbt0GiVLNS6H8nMJCO01JYCqiXcCYQmoVuXXeZhMsN-u4vKfXsuQFUg3RGneiR-oRZv6oNo16cK-EoCr3MxNhomRbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین از نمونه‌هایی از «سلاح گوشه‌زن» برای استفاده نیروهای پلیس و یگان‌های ویژه رونمایی کرد. این سامانه امکان درگیری مسلحانه از پشت گوشه دیوار را فراهم می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695860" target="_blank">📅 19:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695859">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ناو هواپیمابر جورج بوش پس از ۶ ماه حضور در خاورمیانه در تایلند پهلو گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/695859" target="_blank">📅 19:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695857">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c2d0ed10.mp4?token=MQeC0xds2f0FU4FyO7D6mV95MSRMDhx1elz-NboVIC3IfVonTpYwiFgck64fNtoi9bBz4TrvnDc7gVHrgYtyNOJjIRL_8Se7XPApbKCurgIj6jLfw7UADYn6jzvU2e1tpHLlGpUUPr2CO8ewmtJGAnoqh_hTgqBFLgBhNcvh3IaMlcQ9SEeT7Fdzb2Y9LStZoz19806BZEYJEj-Lchdni4ZD7rXq1VXH5jLNgit51gge3xki0Cu5UiclzqPP1ra3liYTPEqlN09ah-0WWKqsmQp941HjQWxQ0XMUQbUsp6Io-6vpf6io-PnH_xO0AR16m3_342PWRFzmtfqOzedARG3vONwHdSb87V0IbsukVaEmGhiowK61yo4luaGY2Q7U06DDmnIboEKPodzMu3B7r7wBj9vuWGJLCeKcA0lsxpJKGt_3Eyq47MMikzha6FV_ulJZbRIuKSUnlURg8pQsNCNrjMXuWawolWa5Clo80fqsk6RmEMlnWWeYCOSsKJSYzop-dJGuedHQS_JKz5_SMGONAZbvUXc4Yow1Nf5M0iCZneDeOQtf9kMnTQ1qY9-yXbGwht_LVqaN9b90stgE5_9z4MKDVqlMrMBbuMS6PAVSwV5KyQLZMK0G3nz48kDWtJfqk4jRP_MasKINTeh2hU3DJc3yB4_PnRCSxwQdq9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c2d0ed10.mp4?token=MQeC0xds2f0FU4FyO7D6mV95MSRMDhx1elz-NboVIC3IfVonTpYwiFgck64fNtoi9bBz4TrvnDc7gVHrgYtyNOJjIRL_8Se7XPApbKCurgIj6jLfw7UADYn6jzvU2e1tpHLlGpUUPr2CO8ewmtJGAnoqh_hTgqBFLgBhNcvh3IaMlcQ9SEeT7Fdzb2Y9LStZoz19806BZEYJEj-Lchdni4ZD7rXq1VXH5jLNgit51gge3xki0Cu5UiclzqPP1ra3liYTPEqlN09ah-0WWKqsmQp941HjQWxQ0XMUQbUsp6Io-6vpf6io-PnH_xO0AR16m3_342PWRFzmtfqOzedARG3vONwHdSb87V0IbsukVaEmGhiowK61yo4luaGY2Q7U06DDmnIboEKPodzMu3B7r7wBj9vuWGJLCeKcA0lsxpJKGt_3Eyq47MMikzha6FV_ulJZbRIuKSUnlURg8pQsNCNrjMXuWawolWa5Clo80fqsk6RmEMlnWWeYCOSsKJSYzop-dJGuedHQS_JKz5_SMGONAZbvUXc4Yow1Nf5M0iCZneDeOQtf9kMnTQ1qY9-yXbGwht_LVqaN9b90stgE5_9z4MKDVqlMrMBbuMS6PAVSwV5KyQLZMK0G3nz48kDWtJfqk4jRP_MasKINTeh2hU3DJc3yB4_PnRCSxwQdq9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت انتخابات اسرائیل؛ نتانیاهو دوباره با ایران می‌جنگد؟
🔹
خیلی‌ها می‌گن تنش بعدی ایران و اسرائیل، فقط به تصمیم تهران و تل‌آویو بستگی نداره و یک عامل مهم دیگه هم وسطه و اون، انتخابات اسرائیله. حتی بعضی‌ها یک ادعای جنجالی‌تر دارن و می‌گن نتانیاهو برای اینکه دوباره رأی بیاره، به یک حمله دیگه به ایران نیاز داره، اما واقعاً همین‌طوره؟
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/695857" target="_blank">📅 18:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695856">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b30fdb18.mp4?token=NeZGfoe8q9Bpj4m0PT-p1DXAhDPvgA30Z4TYnrQcANiObD0dUZdF-h8uRlB0Uxl9F8JlRn-StHPuhVkC2y-vdzdAt3Ff1VMSI-Ooe797Jr_nyXcHTNwQtjgvpbkZ6J216_8Qc5Rt33vNZBgdc6GQSBfLH39LuOr2Twyoc_urs8MF2QRHZ61z8cWdJtuEODmltxfyhPYwO4UlZnPhMmIkltjSdmr1_Y0s3A9crHI5lWVQ95py-pWwmG9PwRcbwWTO_Tmecunt0UKtXgQJS4OupfMx6gH-_Ah0EqVCS73gd-dvIrkmXRnqUFz5uJ2tmpxvGgx5VPl99sMwqxnctS8kOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b30fdb18.mp4?token=NeZGfoe8q9Bpj4m0PT-p1DXAhDPvgA30Z4TYnrQcANiObD0dUZdF-h8uRlB0Uxl9F8JlRn-StHPuhVkC2y-vdzdAt3Ff1VMSI-Ooe797Jr_nyXcHTNwQtjgvpbkZ6J216_8Qc5Rt33vNZBgdc6GQSBfLH39LuOr2Twyoc_urs8MF2QRHZ61z8cWdJtuEODmltxfyhPYwO4UlZnPhMmIkltjSdmr1_Y0s3A9crHI5lWVQ95py-pWwmG9PwRcbwWTO_Tmecunt0UKtXgQJS4OupfMx6gH-_Ah0EqVCS73gd-dvIrkmXRnqUFz5uJ2tmpxvGgx5VPl99sMwqxnctS8kOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظر توریست چینی در مورد جشنواره فیلم‌های کودکان و نوجوانان اصفهان در خیابان چهارباغ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695856" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695855">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd0de3f83.mp4?token=CIKSAQbtcjrDk1SzbwlIMf7z04JOqS5TQikCQ3LUMa7MhA3QIhDD8PM0mRqbUSzLTavtPCzr5wDtFt3Z4doq4L3pf5my6NKY4U6EhSaw-GO2UBnZfEV3XdJmcSuPNCDA6a2Li83LF4y0ORvs6YLS_DYuzhLJfNJDzLlaOqc3SBNQvyznv0LvxlFBEnWPRRBe3xCih3moaMZARYznZLhoxQ0CHFvqWTq-ARdYxA06Nkbvq6vPL5x63ZsF8SKOT1N1V5xkGf6vksvd-r1EkZ5cpNI16Gq6n60H_lRuIKZcSN5qGXEkVdECiwb_8_-hXOjc3dxrsVhq03UDRyuj5vPakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd0de3f83.mp4?token=CIKSAQbtcjrDk1SzbwlIMf7z04JOqS5TQikCQ3LUMa7MhA3QIhDD8PM0mRqbUSzLTavtPCzr5wDtFt3Z4doq4L3pf5my6NKY4U6EhSaw-GO2UBnZfEV3XdJmcSuPNCDA6a2Li83LF4y0ORvs6YLS_DYuzhLJfNJDzLlaOqc3SBNQvyznv0LvxlFBEnWPRRBe3xCih3moaMZARYznZLhoxQ0CHFvqWTq-ARdYxA06Nkbvq6vPL5x63ZsF8SKOT1N1V5xkGf6vksvd-r1EkZ5cpNI16Gq6n60H_lRuIKZcSN5qGXEkVdECiwb_8_-hXOjc3dxrsVhq03UDRyuj5vPakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای مسلح یمن (انصارالله) کنترل مناطقی در نزدیکی باب‌المندب را مجدداً به دست گرفته‌اند
🔹
در تصاویر فوق، خودروهای رها شده متعلق به عربستان سعودی قابل مشاهده است. پیشروی نیروهای مزدور سعودی از صبح امروز متوقف شده‌است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695855" target="_blank">📅 18:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyzjqwOKhGeRmsYQ2PNaS1miL05-UbIw1yeIigiVotvHtWL0XmUKTJ3sKMA16Lx-6WCbysCE-eP4r81ReuiYQAcpUFmPpRRg66tmfxkosQj0rNPVZKSL0SJlrugAdROYiJJBx5kS4tER-XxX4LYblTawtiCLJx03vGcJN45HjHVBpq_gPd8UrhF7zg5vJeDpa7E6LoD6T6XE2PHoDOaXQe18qSeEBs1mhKCH2Vw8E0lN313ApqTZEo8pIxRAiy1p_gwn5kqRpwUs9-dYWwdiI_0rhZgbCMN3tbvgPsqc77D9OAi-PjTY7WrflHkWWyl43Vn4eMA2D3eeV_LAlQy6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA1Wrkh87wFjwkY0QxQLBdpzwI25o6Gi5lPJTH_wIs5OAOC3DQjHiI4XoOaxDsRkpNil0BrkxjTkp5r9LY8GFHD1cK2cZXs8s1Vs7IIqOYmNwcFGughVeEal5PcvL7w70dCS2_wNDnwH3R6VGFKSQqP94tbJX335Ra9SLTQiFTzizqCJxI6OQL44alY0qWmoEyvLhomZ5XzWO4aBuWBC2Mh_uT2VUzpCmHJCrffVPM9tB8MnHCZmuQ6Xy_3pU2WgiXT853zkQr9RVQGLmfDLaSMsoetzAwKtGvYzt-E9q6FneeYb4DysOSpZSDJWdffbWDGk4Yc64wWAYo346WzCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTK7IpgXi5JmuONgZvzd3yCogZxT4cIDt9KJxXo7YOdjRY0Ci2qcQNfi2HtAnkxCeTz4PIQraxVjvMm5eOwu-nMrD2RJ0xwW8LlL7DFjgjR-HxTsaEduWk-cMlqdOvUAIsLIDkRBDg423Ha4slMO3q_HlA1PpGH9GuwoEBk7PJePUQ6gBBAFlTNNW6Kx36o1C770t_LUwNGXy9EAC-xJbEF3EAMKpI1gLoXH1XIgbjj55HknEzfL11kpTtqbBrfn3qdYYGZZinOn0YkHNqeFLgpX3IgZ3zLdCQPix0AsH98eh6JwJzuW-DH4FPTr-2A1Aq88NRJc-VjFv3r-F1rwYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc30bd640.mp4?token=jvY-t2Ac3qqYL9MJonV5zEwFF_0jTikqIu3hlcIovMyCRqqAS4B2P9eeAIm9tbr5vyxQZ2SG3rtAujkQox50OszOMZ1ndnZqSXs4TEAc6G4WqwwGzj53PYRqvLq_vn-oIWzSrdoZXnYsr0b9NZkf83y7obWlEuUORG2f5DEXtGNfK-ONN4QKVZzmtnIwx5e5Vj9w3UJ-P__22Ag9hwKTKN2tYfxfO_d_uzpzb2nXVUzRRivBPiVbnd0DSnZ2mqftKqQJhnCPLxbgt7PRxWkqc76O8ASxbF8V46ot6VnW7Obh94CieVk1tsvzt7R5Mo4SwqJPh92DgxCgsao_CwHV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc30bd640.mp4?token=jvY-t2Ac3qqYL9MJonV5zEwFF_0jTikqIu3hlcIovMyCRqqAS4B2P9eeAIm9tbr5vyxQZ2SG3rtAujkQox50OszOMZ1ndnZqSXs4TEAc6G4WqwwGzj53PYRqvLq_vn-oIWzSrdoZXnYsr0b9NZkf83y7obWlEuUORG2f5DEXtGNfK-ONN4QKVZzmtnIwx5e5Vj9w3UJ-P__22Ag9hwKTKN2tYfxfO_d_uzpzb2nXVUzRRivBPiVbnd0DSnZ2mqftKqQJhnCPLxbgt7PRxWkqc76O8ASxbF8V46ot6VnW7Obh94CieVk1tsvzt7R5Mo4SwqJPh92DgxCgsao_CwHV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طاعون، بیماریی که اروپا رو نصف کرد!
🔹
طاعون باکتریایی Yersinia pestis است که در مرگ سیاه حدود ۷۵ تا ۲۰۰ میلیون نفر را کشت و یک‌سوم تا نیمی از جمعیت اروپا را از بین برد؛ قرنطینه و کنترل جوندگان به مهار آن کمک کرد و امروزه با آنتی‌بیوتیک و تشخیص سریع قابل درمان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695850" target="_blank">📅 18:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت بهداشت: هیچ منبع رسمی خطر ویروس روسیه را تایید نکرده است
قباد مرادی، رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس مقررات بین‌المللی دنیا، تمامی کشورها موظف هستند که بیماری‌های واگیردار که امکان گسترش آن به سایر نقاط دنیا وجود دارد، به سازمان بهداشت جهانی گزارش کنند.
🔹
سازمان بهداشت جهانی نیز بعد از دریافت گزارش کشورها، آن را بررسی و در صورت تایید، میزان اضطرار را به کشورهای عضو اعلام می‌کند.
🔹
اگر خطر ویروس جدید روسیه به اثبات برسد و جدی شود، توسط سازمان بهداشت جهانی اعلام شده و میزان اضطرار آن اعلام می‌شود.
🔹
تاکنون هیچ منبع رسمی و یا خبر تایید شده و رسمی از سوی سازمان بهداشت جهانی و سایر ارگان‌های رسمی در خصوص تایید، میزان خطر و اضطرار اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/695849" target="_blank">📅 18:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SykQ8MBP-jxeKCx7DChphoJAIUPPV1mJTGYIJDL2a77X-N2NQ_mCP6GzY_GaGprd4eahkftTwYtvQvT_0--du2F1IJbRq7hKxwMd_4yK2Dtm2_sjj8813CB_hHDD5JyNRkH3H9h57juxclaFBAMdWXU7gn5rMWndZ_fUL2cVPtPEVRzhC2DtcDd-R4yVQ9CW33FFD5_lfMgU29_6G8LWnt8MjsERh6dho0hpC-V48YPah0HBmtZsluB0n9YN04Na5ebsq6vnYdMflwezl4QfpZSXgaX4orb6ZGhEayM2hkByxsUBtQZScLypmQ9LrM3rq0ozjbrVY_3jqmxDd9kp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سنگین آذری جهرمی به کوچک‌زاده که به طرح فروش دلار با کارت ملی حمله کرده بود
وزیر سابق ارتباطات نوشت:
🔹
دلار را که نباید بر اساس کدملی و از مسیر رسمی بانک‌ها به مردم عرضه کرد؛ این کار که شفاف است و قابل نظارت!
🔹
راه درست و اصولی این است که ارز را بدهیم به نورچشمی‌ها تا در سبزه‌میدان عرضه کنند؛ آن‌وقت دیگر کسی نمی‌فهمد کدام مؤسسه مالی، ارز را زیر قیمت از کدام نورچشمی می‌خرد و بعد با نرخ بالاتر به مردم می‌فروشد!
🔹
چرا بازی را بر هم می‌زنید، آقای «راننده رفسنجانی»؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695848" target="_blank">📅 18:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
یمن آسمان عربستان را منطقه پرواز ممنوع اعلام کرد
🔹
صنعاء به شرکت‌های هواپیمایی هشدار داد که حریم هوایی عربستان به‌جز مکه و مدینه «ناامن» است و صحنه عملیات نیروهای مسلح یمن خواهد بود؛ پس از این هشدار مسئولیتی در قبال پروازهای انجام‌شده در این حریم نخواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/695846" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اخطار ایران به یک نفتکش متخلف در ورودی تنگه هرمز و اطاعت آن از دستورات
🔹
بر اساس گزارش ارسالی، یک نفتکش در حال ورود به تنگه هرمز، در فاصله ۱۱ مایلی شمال خصب عمان، از سپاه پاسداران اخطار دریافت کرد.
🔹
به شناور دستور داده شد تغییر مسیر دهد و بازگردد؛ در غیر…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/695845" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdEnfvYfN44Q9hLrIUfsnBRC7fyqoZXsgo9cEEwD1A5jnoF71wXjQWea4R4h9F-D-klwc1SfI4c6or4ZtYg6VSE0g5IFCMv4kM7gNl6FmXZuzS808KnIiUYZsKtsaofi1IWESEZ3wQeopB-2AdKkSPTbWb81QftO3Hm-WKS3VXeD1YemPL4na_R85pk9QhYjW6mPQ3QMG7BdA72CiebyGfmf0vBbJ0Cv8pmANNxuaa12Nwew7XDLVn1aClXjeCUorOe8eh8ZlmSoqTkAvOBTZMf09MQ5pcAJEqltGB0-F_y6iFepbp7RMseY1jXi7zzMkG81pdR4dxunTUaO3UOnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: خطای بعدی دشمن، «جبهه‌های تازه» و «غافلگیری‌های بزرگ‌تر» را درپی خواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/695844" target="_blank">📅 18:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa04eab51.mp4?token=PFghuAZTKSqKO3TDfDI56zABVm4did4GGAU5bKIMhMCYTqlSvCsdt_t6C-uOtjKdkc_yWlGFMl1IhrzAw_9o0h628_PLkK1k5EtsnWvhsij3srHzhLD-pRKitbzR5BCMjLhD5Suc-cIQ2Nrkv214gxHDpvaSL_BaUnJnzezYhE2DP43fmrNCXnASoG6gOYobBIq1G2posvDQazjjnGxB9gr0WYe4NtXqyxjzpnED0mzriw_QbIsyFWeHPoilo2VyyUTQOUwZ4jbGCSIzBKkYFq2HEDbs6-mTSNGFopp17tVg0A311PWpqzb9fKxnHe4_yHWzHZMbj0JQ8VcRzacmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa04eab51.mp4?token=PFghuAZTKSqKO3TDfDI56zABVm4did4GGAU5bKIMhMCYTqlSvCsdt_t6C-uOtjKdkc_yWlGFMl1IhrzAw_9o0h628_PLkK1k5EtsnWvhsij3srHzhLD-pRKitbzR5BCMjLhD5Suc-cIQ2Nrkv214gxHDpvaSL_BaUnJnzezYhE2DP43fmrNCXnASoG6gOYobBIq1G2posvDQazjjnGxB9gr0WYe4NtXqyxjzpnED0mzriw_QbIsyFWeHPoilo2VyyUTQOUwZ4jbGCSIzBKkYFq2HEDbs6-mTSNGFopp17tVg0A311PWpqzb9fKxnHe4_yHWzHZMbj0JQ8VcRzacmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزدوران عربستانی زخمی‌های انصارلله را با خودرو زیر میگیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/695843" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695842">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdjtlYQ-PFSNGxcCDkbwMly8LpBT_wBmuM5c9GCuYmQvljs6yXIO2OquXEzVEtBphV4ICKaES4bswnq_R0Ys2tEXuYy0tmeGTsq67BudwynzHSReUTww46ad0ulW-W-GMOBvNaUjE55AFI3FRmQNspmeykB_wMueVjsRWs9lNqbCdSf05fEVcFPcLAhN-fywYFUOh_3ginYNKvTjAJhJ2JLHY0xY1Mp2kI5FlhQVUMo_DRxSs8KL__Qsvl0LznDWHBosdP8l7JkQkBncXkYSrzQZe5ckln_NVKqW7WRC85NK92youGBA6k56oe_zLQbGUl0PxoRwfSPFeYJGtOC_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران: ترامپ مشکل سوخت در جهان را حل کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/695842" target="_blank">📅 18:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695841">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پرونده دارویی کشور در آستانه ارجاع به صحن علنی
روح‌الله لک علی آبادی، عضو کمیسیون بهداشت و درمان مجلس:
🔹
متاسفانه قیمت دارو در برخی از اقلام خیلی بالا است و برخی از اقلام دارویی کمبود داریم که بخشی از آن متوجه عدم ورود مواد اولیه به خاطر محاصره‌ای است که در آن قرار گرفتیم.
🔹
در برخی موارد مخصوصا بیماری‌های خاص قیمت‌ها آنقدر بالاست که برخی از افراد ترجیح می‌دهند درمان را رها کنند.
🔹
هفته گذشته در کمیسیون بهداشت از وزیر بهداشت و رییس سازمان غذاودارو سوالات پرسیده شد و پیش‌بینی من این است که اعضای کمیسیون قانع نشوند و این تحقیق و تفحص به صحن ارجاع داده شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/695841" target="_blank">📅 18:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_Apqf1sVGpR7zJ_NlTdfltTrxVRQ_qJBMijreATXV-5VEYCtSGNtua8SOPKWIf9NtH9UDIweLa-pIyDb93gjg9SAE4joaIDejwBe-WJ7uFOtihJIebnPwnH95U764yt0pXq4AXx3_cvkz0dmcN8wwPjeM_oQhc_FkiDJdN6hHKSFbypoCTshkFzVwaryOrcNEAzxjmnkWDlHRqK6VMb46SUrvLzlb4wpx5ZvwRnLeeL-buyVU5vL8xzw4Tx_6aFYO-XBzJolY-owGXK-2cJnDReD6kdoAfoDh3opV_wfgH6Y_PiOgDgjsMamThvyZMH_J3d7Wv60_bLid2mALtnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPd-8o1vwCsLwjKICktsd_-21iyV5GBsn5dz85D7Wzvr9Lq4dpLRuff0BHYJTnNThRHfGVXa5lz_hGkEnSXGWNSsdD6DxLm9qpGDtZFMMYAyDZ-68BKuW9xVBVe0DWYN0gDJlenoClEg0ktVSHaIIfKMpxyopg4B41fdSQQ7v9eF8jVke1SBfE5GynvpvsiygqxTCV-L-YqZI8MZNPT25TdZjXkJaEQZ-0z_1Ml9XomKs9ZmnfDRRKC5tRhaK-8y8pIdgKdVb11f3KnZT_1XK4-AtdgjE0qMy0g2sqe5aDIL5Zg4m4yphJD6c6SmImdp0PS3U_JMvrfFC58cXjGQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJXYE4MM-nNtUU3kP6Ns5l4SCEg1pNPt7ajuSq9Q7nG1fWJK2X-4PIRyJcVvYsqZa9w9OCgQHX8g4dxJju1USLNqZKznX8ExWp-bqVSzAfEmzrjgEiDeS_myp4cnkMTqr1QK3ffFWhVM_Ufh3Jcysywi4Abm1y0UOtRmFqLjnGfgeOb3S2bA---Ad-xhKDD8_UMpPbi_Op2Qs4VP8yCb-gd4ty_RCjVtqLEWugmKiEYdrDMrvXJkMjvn38cvEjNXr1Cfd9ageKweZ8BQ5H1nYamec_XZ5zYJNyEuFPtQi-9IJwjk6jq_Mz0pxr9bMIHuJyNy5T5PLpwV5vU77_OiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJi7kGaLg_YtMCFBwAIu9-mA4S-L55-6toRIeSNBXiO5NuhQRDov8MF-E28ncLnIiC8uSIPl25kep9SQsm19oZImTRe-EX1InwEHpFftQpwoiV-Yv2RbHpI6AZNuwqZHowRgWjZpK9tUF3h8Z0oSqQCvTpBpjpnLBmXLeo6V4XnKWtRtNsLfDDLtgOpFHee4uzLXQbPfahAZGQ7RWXSlftHKL04o2Krm6vmkLhLXK8yquxv9RF41xtKOxAWNj1682VA0OUA5oFWZ9nAt4RnVRR-qROB7bfXFVfllxTkzviQ43QrPARg70noXrNhS5fXO17yVyA-QgRdhrD4hf62LtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ویدئو همه حرف اضافه مربوط به مکان رو همراه با تلفظ‌هاشون یاد می‌گیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/695837" target="_blank">📅 18:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
نشست محرمانه تیم امنیتی ترامپ درباره ایران و یمن
اکسیوس:
🔹
مقام‌های ارشد امنیتی و نظامی دولت ترامپ به ریاست جی‌دی ونس در کمپ دیوید درباره بحران ایران و درگیری عربستان و انصارالله یمن گفت‌وگو کردند.
🔹
احتمال ازسرگیری عملیات نظامی گسترده علیه ایران و مشارکت آمریکا در حملات احتمالی عربستان به انصارالله بررسی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695836" target="_blank">📅 18:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69b62aed.mp4?token=H_5rW_92pg8eiRnAN9bne9w1iVeN3zEFjuJs7IaHKSk8oF0i375PcFpE1t2mJKFNQN4XJ8xe7n4uQGQQiS_uriEPkWvhKEOws4JBuNnHk79DcOQzJhrOP2jpoU4gknBg6kxtlUVBw6rBAVCVP8xgscxMMccnJYLeeYPhQQV3-UQxM97EOi_IcHhrnCe_sDFklgDhl5Jyso-ePwRNjY-MwnKLQfZJhcdE0kKjQa1tNs_HMffUUGo_VBO1ZLpTtrX507XBPwkwgYam1bGDX4Fm-3Ch7yd-DiF-CFSYVW64foBmXPVfEYn5C7Nf11LHJqQqr-sM-leZ-M0nlxfg3Wrn9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69b62aed.mp4?token=H_5rW_92pg8eiRnAN9bne9w1iVeN3zEFjuJs7IaHKSk8oF0i375PcFpE1t2mJKFNQN4XJ8xe7n4uQGQQiS_uriEPkWvhKEOws4JBuNnHk79DcOQzJhrOP2jpoU4gknBg6kxtlUVBw6rBAVCVP8xgscxMMccnJYLeeYPhQQV3-UQxM97EOi_IcHhrnCe_sDFklgDhl5Jyso-ePwRNjY-MwnKLQfZJhcdE0kKjQa1tNs_HMffUUGo_VBO1ZLpTtrX507XBPwkwgYam1bGDX4Fm-3Ch7yd-DiF-CFSYVW64foBmXPVfEYn5C7Nf11LHJqQqr-sM-leZ-M0nlxfg3Wrn9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غروب خورشید فوق‌العاده در جزیره آنا ماریا، فلوریدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695835" target="_blank">📅 18:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6NGA5gxj6zxm7QhvWBEF5rp_DKSDBWqQULJylGnqy-ZhWBx-669TCKbPc8RpkaC11bnSXnIbPTyqpBzvLQ9HBs247pmKHnycv3rWCeNsXdy-z7aqSxYxiPn1DrQ1-DOecoQ3Fsac6kJbXNdPULcSuyw3ei1C-OZulbblWHcQy8gH30Uci1Bos6jJovL-E401RfLHItrgEH6gKfsF96u8ykX6N8hxSOKlKDHdGM6qYKEa9NTP3LrhGH0wefP42iXdUL9XInVb_M17wVxsaQfionkFxr2wwosD3JlUhrpGswwHwoSsepFkHx_h2ZtRLSP2kd3L472SNnyuFbTvKZeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت دفاع عربستان: ۱۰۰ فروند جنگنده نیروی هوایی این کشور در عملیات امروز در جبهه باب‌المندب شرکت داشته‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695834" target="_blank">📅 18:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای الجزیره: مذاکرات ایران و آمریکا با تحرک دیپلماتیک فزاینده‌ای همراه شده است و میانجی قطری مجموعه‌ای از پیشنهادها را برای نزدیک کردن دیدگاه‌های دو طرف مطرح کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695833" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اخطار ایران به یک نفتکش متخلف در ورودی تنگه هرمز و اطاعت آن از دستورات
🔹
بر اساس گزارش ارسالی، یک نفتکش در حال ورود به تنگه هرمز، در فاصله ۱۱ مایلی شمال خصب عمان، از سپاه پاسداران اخطار دریافت کرد.
🔹
به شناور دستور داده شد تغییر مسیر دهد و بازگردد؛ در غیر این صورت هدف قرار خواهد گرفت؛ کاپیتان نفتکش پس از دریافت اخطار، دستور را اجرا کرد و از منطقه دور شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695832" target="_blank">📅 17:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CojhwYx_yttpkeZyEAoO1xhePYGNSyeaIuFFOYRrG7U2GjmTccuJ3KLH-MtpEJ1dCH4i64O4Ya8oRFhDGwZ_XJDhr_-Pe068B6-oYJfbdxMod7NBg_wGhPcb6m-Aqc38F-ekeng6S4v0lqPsMYBptyuLKYPqKSZceGlV199yIBSLaLF9CyFTVeiOuxxHvJdYpnSY3EwL1Ebn_HmiLB4e9Vk4YY3UxrxPhKYRdpV-q0kmGFuqnpdbsSLJt1OV2ldFIrs8XVRX1zwi7AMGbdo4l6kNGXtIGKJ7rU-6ewz4HfmoqX9bVhXt3VS-Ijea4JyuE81yf53d6udFulP0TrTn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکه‌ای از شهرستان ناغان در استان چهارمحال و بختیاری که بی‌اندازه زیباست...
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/695831" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695829">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqbLprXnFI1Fdx1uaRJ3BiGPouH4Ad4Kdra3hO1QTKCbXQP7WNfV-nmjtwrTlNZe0wkn4B61bNCmOSf15T5sEc6iDMXZ8SkbSgJ8M1ZngJ4oN2xumdtevNO0jcdmBpg5lslgu_ohI1oNgrg80pOM5_kmmE-PYx9hMBzTKLAldpoxL7-ZGvgSfl_OEL4B4ayQVYc9oAxnujkN6jm9rNiy7_eYSqh7CQ6fCb0hCcxxDNSIwDHk2j6uVMGLXaSLdmF7d8k6HBYes2J1xxBdpdVS3OCYen0e0T7i9VqlIFDlWnySPrCB0y3jjUiuoWFMzAc3-1QTXKCcfAzIetDsM60NGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
طی شش ماهه نخست سال ۱۴۰۵ صورت گرفت؛
رشد ۶۳ درصدی پرداخت تسهیلات بانک کشاورزی / تزریق بیش از ۱۴۶ همت به بخش‌های مولد
🔻
بانک کشاورزی در نیمه نخست سال ۱۴۰۵ با پرداخت بالغ بر یک میلیون و ۴۶۰ هزار و ۹۵۴ میلیارد ریال تسهیلات به متقاضیان واجد شرایط به ویژه فعالان بخش کشاورزی و صنایع وابسته، رشد ۶۳ درصدی را نسبت به مقطع مشابه سال گذشته به ثبت رساند.
🔻
شعب این بانک از آغاز سال ۱۴۰۵ تا پایان شهریورماه، در مجموع ۳۱۷ هزار و ۱۰۳ فقره تسهیلات به متقاضیان پرداخت کرده‌اند؛ رقمی که در مقایسه با عملکرد شش ماهه نخست سال ۱۴۰۴ ، از نظر ارزش کل پرداخت‌ها ۵۶۴ هزار و ۹۰۱ میلیارد ریال و از نظر تعداد تسهیلات پرداختی، ۵۴ هزار و ۲۶۵ فقره افزایش یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/695829" target="_blank">📅 17:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695828">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed37b9187.mp4?token=SvVC0HKlbMg78EIUBtYNWXhwC0Bwrww_Ubk5_pDTcijLoK4acXEHSbrWg7sg-6mxakjDN0fuVPjcOskCczLOnjOMbtmQ8XvKfPZQDNjB5CX0L8SSvYTxhjSv5-pQqbqpqgNmb7dgFQVvDsKW0ePhFE9Rs6N5MJbfyZr8ZWOpwO6cbv3gjtI3nN9DxjpSancgIqLcpFJGXiBWf9_xz99oHSA7-88F-tPcWnpEt-uPFAE4zK9LFU3ypgdeNM4PUt3YrVXDCVkw-y6ebVjtcIA6FJ_J5PZUMDQrFfEsiVGQVneC_6tnAx7-urpM7F2074MuyFn52SN68amKTYnRrzO9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed37b9187.mp4?token=SvVC0HKlbMg78EIUBtYNWXhwC0Bwrww_Ubk5_pDTcijLoK4acXEHSbrWg7sg-6mxakjDN0fuVPjcOskCczLOnjOMbtmQ8XvKfPZQDNjB5CX0L8SSvYTxhjSv5-pQqbqpqgNmb7dgFQVvDsKW0ePhFE9Rs6N5MJbfyZr8ZWOpwO6cbv3gjtI3nN9DxjpSancgIqLcpFJGXiBWf9_xz99oHSA7-88F-tPcWnpEt-uPFAE4zK9LFU3ypgdeNM4PUt3YrVXDCVkw-y6ebVjtcIA6FJ_J5PZUMDQrFfEsiVGQVneC_6tnAx7-urpM7F2074MuyFn52SN68amKTYnRrzO9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از شدت بمباران دقایقی قبل صنعا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695828" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2255239737.mp4?token=VrPQjyL4kNrPa2Mq4QiOswZBJRo-RTGWr-abOH8X4mOE7rxk2Cdaa9dgaX59zhHl5Qm2D3XeMHnlLadWGipQsPtTWZ9isp5JHm2ZEcHBka2BVrIF94oHxhyLS9Ie2muFWRIxBC22tWMdz3bXR2y9mdcQOMgfHUXfWRuMOIfRIC0I9HvO8-24nq15kvkErofydcG8lrkUpm4W7EMEkGMfcOLvg6bij58qkN9u0HHuDksJp4GyBV3rS9bXmdwX5qiB9eKTsolJuqo7brpdYW6TSxvvA6WPLfrFnHRA6nH_h33mgtm2hjBD421G2VN6Z8zZ9GbL_gjTW8UByZm1tMQLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2255239737.mp4?token=VrPQjyL4kNrPa2Mq4QiOswZBJRo-RTGWr-abOH8X4mOE7rxk2Cdaa9dgaX59zhHl5Qm2D3XeMHnlLadWGipQsPtTWZ9isp5JHm2ZEcHBka2BVrIF94oHxhyLS9Ie2muFWRIxBC22tWMdz3bXR2y9mdcQOMgfHUXfWRuMOIfRIC0I9HvO8-24nq15kvkErofydcG8lrkUpm4W7EMEkGMfcOLvg6bij58qkN9u0HHuDksJp4GyBV3rS9bXmdwX5qiB9eKTsolJuqo7brpdYW6TSxvvA6WPLfrFnHRA6nH_h33mgtm2hjBD421G2VN6Z8zZ9GbL_gjTW8UByZm1tMQLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش پارک دوبل؛ حرفه‌ای ماشینت رو پارک کن
🚗
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695825" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476d8900bd.mp4?token=pibj6IuGp_-Uw9zxUy-Lu4w-YXZMcJusg9ea4sCzMx72gwpsN85-iUgCaLRZTbuvsdHIV_-FH01XEp50aho2I_2v5_rwslHpDs56AqRyvIBBo74xnXxsTssP09GesvUUxGjDcWHtPa7UakNiQC5PxaGdrPbcixkbDkVr6poL97-Ol3wGCqJxOegsTQJ8KQfZ9dyylQYr_2fl3ilm8MptjBXYjPyVleAJl8ajEz5Yd_rAE5Ji1N64r4-eHlzjjwZb7GujPWjXiTfCwaDyCcivz2HJmLfZGz0xFFvAFbuxeFqitLiSnR17c-vdTGmQ56GSfRYGrXw0ea-2-impIepprw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476d8900bd.mp4?token=pibj6IuGp_-Uw9zxUy-Lu4w-YXZMcJusg9ea4sCzMx72gwpsN85-iUgCaLRZTbuvsdHIV_-FH01XEp50aho2I_2v5_rwslHpDs56AqRyvIBBo74xnXxsTssP09GesvUUxGjDcWHtPa7UakNiQC5PxaGdrPbcixkbDkVr6poL97-Ol3wGCqJxOegsTQJ8KQfZ9dyylQYr_2fl3ilm8MptjBXYjPyVleAJl8ajEz5Yd_rAE5Ji1N64r4-eHlzjjwZb7GujPWjXiTfCwaDyCcivz2HJmLfZGz0xFFvAFbuxeFqitLiSnR17c-vdTGmQ56GSfRYGrXw0ea-2-impIepprw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبر عجیب و زیبای‌ صادق‌ هدایت‌ در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695824" target="_blank">📅 17:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
قیس قریشی: تراستی‌ها قاتل رهبر شهید و دانش‌آموزان میناب هستند
🔹
باید برخورد با اینها درس عبرتی شود تا تکرار نشود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/695823" target="_blank">📅 17:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEGM_a_CIC778Dy4KnO12Cr5Dy5yaRXWT8NCI9n0napXO0x_uHyD054LJ4c0oIfHND7HIK35U1OTcBT-b61cT97mbikUDnDiMXekjv0ESHNWZQx2qWahfs_Mbwl9Ky9ranOAgFwRz0q5IJMA8H8eBMxGs-9ITg_YwR73rJVnWR8M3il3k_BXpERDzXzGuf0d3d3-ND2wBi9Fv6rT7JWFYq0qjLqVZSUaRyHGEpfgSsJtFrEj0y0kt9OfYNDeDni1ymwK7AGQGs974_0ZndekRXgeGedCav1Hu0-7Wou7Wo6LvQSHWAcxZSYDe1dtrH80L_jlHuyVDvx9O6oHCZ92bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با نیمه پنهان ابزار‌های هوش مصنوعی آشنا شوید
🤖
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/695822" target="_blank">📅 17:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L837ZfXUDIGue7SqzjgrVl95zh5ym8YyMxTa7VJQwUH_RYGYhVtriWEm4rg4I3MuMWObc2JSu2cXOzVl245276hBT3IxfmfhUvtHs7hvScqEz0ZOtE-AGWdymh4SnzgLkAKAiEMLumYRL6t68U_oKJoZYlLxpWDrr5UBDdzrZHPPCrDE9X72abbWytILg29nolRGr9Z007_jXQSxlm68oSzOsWGNERd4HhkNezZxQOdbp8CBZGx6_G1mfiUk-JOODE1M-JS1mu8GmiKXwVbVZANrM6iZ7rtcdc7kebBkmbnTVl4luwSFeYWB2-8kahLgbQO_C-XF9OQP4wABN-EqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش استاد شفیعی‌کدکنی به تصویرش در دیوارنگاره میدان جهاد/ مرحمت کردند
🔹
استاد محمدرضا شفیعی‌کدکنی در واکنش به نصب تصویرش بر دیوارنگاره میدان جهاد، به مناسبت روز شعر و ادب فارسی، گفت: «کاش این کار را نمی‌کردند؛ خوب نیست.» او در ادامه افزود: «ولی به هر حال مرحمت کردند، لطف کردند که این کار را انجام دادند.»/ فرهیختگان
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/695821" target="_blank">📅 17:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
انتشار جزئیاتی از برنامه بازگشت نخبگان به کشور؛ از مسکن و استخدام تا واردات خودرو!
🔹
بر اساس اطلاعات منتشرشده از سوی سایت رسمی بنیاد ملی نخبگان، برای تسهیل بازگشت ایرانیان متخصص جزئیات تازه‌ای از بسته حمایت از ایرانیان نخبه خارج از کشور منتشر شده که بعضی از بندهای آن در فضای رسانه ای کشور مورد توجه گرفته است؛ از
تسهیل جذب در دانشگاه‌ها و مراکز علمی، تسریع ارزشیابی مدارک و امکان همکاری همزمان با داخل و خارج کشور
تا حمایت‌های مربوط به زندگی و استقرار.
🔹
در این بسته،
بیمه، تسهیلات خرید و ساخت مسکن، خدمات غیرحضوری دولت و حتی امکان واردات یک دستگاه خودرو
هم دیده شده است.
🔹
حمایت از
شرکت‌های دانش‌بنیان، تجاری‌سازی فناوری، ثبت اختراع و ورود تجهیزات علمی و پژوهشی
هم بخش دیگری از این برنامه است.
🔹
نکته قابل توجه این بسته، گستردگی دامنه مشوق‌هاست؛ بگونه ای که بازگشت نخبگان فقط از زاویه شغل علمی دیده نشده و موضوعاتی مثل مسکن، بیمه، خانواده، خودرو و ادامه ارتباط حرفه‌ای با خارج هم وارد بسته شده‌اند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/695820" target="_blank">📅 17:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695819">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پزشکیان در نامه‌ای به رئیس‌ مجلس، مهرداد اخلاقی را برای تصدی وزارت‌ دفاع به مجلس معرفی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/695819" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695818">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان در نامه‌ای به رئیس‌ مجلس، مهرداد اخلاقی را برای تصدی وزارت‌ دفاع به مجلس معرفی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695818" target="_blank">📅 16:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkHlf82Ad-zJawFV1ECwqlgwy3kjwwS_qrQpiAsoxCkL6xW0iJhTl7Bfm0Syg1NVZYiAIS-13MKqmJMhUwfnIabs_WQS0RRBMCxU-DQ7kNVB6_yAJGZCIXbi6viq6XbmQU0E7DO-rwFkehfgzVI4BpBZTl6e21kTrf-DRoQerodt-8oChJQAbzfhDJdk7bhhvWkN6pscTEmD4t4aqhJ7jtv3soaghtca5IaWByhU7VmRITewP-Q24G5RHrW0TIFg9v7Rm7Ss7aL9CiFfsCfhKdr5mN9aJWHQD9sBC15lDQ7ThXROnalt29ZvgKsV_xi8hfiFGXwBoUTFNRpw3AO-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2sDA-knvYV28zqObKYx13GvLHcTITJj2vJiSOpwJqv3fhCpgwZ9bUPdE9MGHaH6mHwe44NhS-izXtm06wIUocNeyDizzID7Ss1jvdb85fULxO_1_LH9bITAB-RcR41VHePE6eY9WhzxMhqng-hE-zEmebwYVgWkSpMJV88nSYL2U6Ok10QEiReboUXzRCn16STBN6nfVqjYkqE06TFamMOqziCqqB45Jf-qqkkUur-WgXmorUOGu4EhKVzdIKo-8ENN6R7mHN6_1wz-FzM1QwoJVd0WDRFTeR9vJZoGv5ZC_7GnF5Uf1uMmM4Wv8IzcD1ZbM3PRkdBZp1DvsHmeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peFYcTqyhABsTVTnYmsjeUURjSTi-iEvX401sR5i9ueUjL2J3G_tNXHz6dp1LEUkXdwVdJTNgk-hclsWuXR1oLx0pScrOLhGxkxpRzYK_m7VRgaHsek2-MdfOCqmkQiYbQCmOqQnf3Ggb0umuCekX2afkuf2-jGw1Ez-bPDqhI5ruPpDJzjubgwC_J-ovdLMb3LW-JvzQCIdrC5D3VBlfgVZylkdT-Eq5Ak6wKMoQ__oEDACZz1tRcFc4oUXsuaCJAiSUf6nYPd8YQVpTHzdWvwjj-Fxtycfc4EZgXkwk5VGg26aAGei-Esm2zpU_qiC8b2NStKFaJUlj4SKHJlORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BD6lv-zKNf6NjtGTeMNZ3YvvNgIu7nZcPHGGc1a1DuiyL-s4hcJVQ5WWFNIH05ihgGAOaJQVk1LuT8MdvMvYzSGfaNh7S5x469Qbv6kyfhh8JA4zADfGd55a2gloD_5i4-VjDw8B2XuhEfGsjyZ7eOIcK7n9P9seXAnms0TNv7SURLxhZTZVt_BwpLrlVXPDRbTH4U-_bcYHt3hVE7X3q_pulESLcNOUpKWfDBTf3XAXbqzi-kh5htRc5f8oOdWxIij08VWoZmt5VQfwv369rZETG6YayqpKjSIUHZGmdS_f5NxGReeFH4Jknib9g-McLNa-K-Q8-wSo79M9WZMlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9BZRqnO9w8e8p_EHEd-kbsHaKYGkkL5CdY6gADuvzgdAKeQzdNisFlbbh0jVTdSKmaRId7gMJXV1AdEkGuKMnPMxTjxM1p3ZzoeIs48uMvPAH5uKoT_ASB0Az0E_-AMn5QEwQww8QyAposwZuiJyIRi2oL2gvaGHzvYuDXeF1XZx5njAXKd00gOTm-5JMzHtbkgbLc5tSx3zp5nyDC30Z_CCe4ReuLfFiiR5m9rMpAnrtRr_rEb-GfhmEveXFKZlEitMxhzwEL2ZCwfNMfJrTXXyp2a0RpgmctOP6ltiraLQWH3LMsmVzyekwBc4BR9f5H2Fqxwpyk6Us0HsCL36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eipO4uGQySPrJDIBMS006TwuiulyoUuqJmDPkOqgyXfoI7cn-2UCmnAvhJ83jHZzTrj6sdhRYjVctIG6qwNbwaWfIaBoN0kDOXBgb_JkKvuSp-8H1SHGKc6mkGtC-dVqZAUnY4k5M6UrnSQJKK9Kz9X-1oRL0c0qEIrHwBW__3mVdYu6dtHXq4ehDMRwcyJ5frsDqRjJuTU47tPh1eIG5L9H_KnXE0NjoCQQuHafQOqlX4as9MKpUsxJ4PYlw5-LCya8yeuEIaX61ieC5TvZh9NztU6II_2gW2k_XBwxFr5HQNtvBo2oN8gug5KU13Z2b6KqtFYbjhAbY6dYN-N0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSTLC0fFyRHO7iDgwCL01BRmTifwR-2NMy9Yq_yaGMBn9HWHmjyWBR1_tgBQnaTdGCZFmo0UnGRLHQAlP5eP2zbUU8ZTh6J4wcLPS6ui56BpHH_klAtdEFHKbE6DWihGxg9tgSqEqZ4GEsXNLDhprgSLBu_GBfp1InPLpPcUAFOBOIYiOhyqvX1LILwmCWQm97L87XPbPITVmgYFZpTYOCMUG5s1waXpqss0M_4L-fd4805d4EbdWJFOAv69wvAEnCfusXYOS8tbQEHv8VEZQiYrnXtRU_4nFiYJRgcpGyDzS7uj3LmBvGVap8n43VsJXAqBnhQTRYeZyTexn34U1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7G9gkOYmn6875x6trNTFDfInH0bru2G7RdPnrFfJGscSXyxB1tvsqs5KY9nHr4SilL3WYTXWSaq49bvx5b1Ln7quEVGMY2ZfcBw9QMNc0qpQ8zAM2oB1pzy02oac_1ys4RPmyrLzD_Sm1zRvy_e-HG2yHKdVsqnZa5X3d6vPOgpAXoqK4jsQtpc9Mj4bnFVDl04wNDN8cne5NWBQKf3O6dtLpkSJJVviWtJrWsK8GszfUxS382fDJzLfyXP17ejyIEqswmMiAuk0VknwWwqbj1Da78AUGN04ZQ3kqaNKTqbHo0lKFLWuY36E9gmrp1zXval6ePRW3PzKR1IvM54ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZgKamko__VC4M-TZlxkLT4lUTUq9pDWjvUvhN85qvXWc_QNDW_7-DYf5QtOS7rDFNBsXV6WrMKkWcEbyPFFVxF1UAJWGlD8x1qihjBI-gNqudCS7uOX605ag58b5seKZlWX5KQbLOO9BPbZrsrnrnz4CQYTZXU-EK0GIa96nb6TQVM7TdkdxggjdCIzmP-GhMG3nTWWQqO6ZL9veG3E2rIS8M1sjI3beTkDcX_RjbUC2h6xe7FjJFN9sfBYht6eQKYFqd1QZeaADq-75izVPZ8olxm4MDZd-l6grVxBVdUWWcj5cg5XcwokjzPCcgAStmu7yQWNV4Sbl_8E-DFQjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۹ کاری که بدنت انجام می‌ده و حتی نمی‌دونی چرا؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/695809" target="_blank">📅 16:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مرکز آمار: از هر ۵ بیکار، تقریبا ۲ نفر فارغ‌التحصیل دانشگاه‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/695808" target="_blank">📅 16:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7nU0xbccbk3pDSgb49FQIHLYqksMFDBvyrir1aOwnwEkmOLeNfPi2u7eZkbL1h5GZ02cBhvdV7lBTQDAt1k4AfckUU_w30Mf1Q-fwJGZFsnJGyNmavswXbb2XHmJiHVPEI6zNfIE2xUyPWcC_rnYWJqFyxwR5rTQf32vlBwAKs-KctUGgUIhj0l-FiMxr8KXStsgjVWPAfKhLwkQkILmiCxZQHn6cYUM9-4mZ3YX3017fg7a-XpTTesfgz7JxN9QrMv2Wf2esHI7ZRtmQJ6MSg3AmD3yIpY7a_pmFBIUtPBY8acy-9YFTvNhErCuJCL8zzp3ycUwFoDnCy8-vZ9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همایون شجریان با «هرجا که تویی» برای حمایت از آموزش دانش‌آموزان روی صحنه می‌رود
🔹
همایون شجریان با همراهی گروه سیاوش، مجموعه کنسرت‌های «هرجا که تویی» را از چهارشنبه ۱۵ مهر ۱۴۰۵ در شیراز آغاز می‌کند. فروش بلیت از دوشنبه ۱۳ مهر آغاز شده و اجراها در دیگر شهرهای ایران نیز ادامه خواهد یافت.
🔹
بخشی از عواید این کنسرت‌ها، با حمایت دیجی‌کالا، به کمپین «هرجا که تویی» دیجی‌کالا مهر برای تأمین لپ‌تاپ و آموزش دیجیتال دانش‌آموزان مستعد کم‌برخوردار اختصاص می‌یابد. مخاطبان همچنین می‌توانند در جریان کنسرت، لپ‌تاپ اهدا کنند یا مشارکت مالی داشته باشند.
🔹
این کمپین با هدف تأمین هزار لپ‌تاپ در یک سال، دانش‌آموزان را وارد مسیر آموزش دیجیتال، مهارت‌آموزی و منتورینگ می‌کند. همراهی شجریان با این طرح پیش‌تر با اهدای لپ‌تاپ شخصی و بازنشر قطعه «می‌تراود مهتاب» آغاز شده بود.
https://mehr.digikala.com/madrese-besaz/#map
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695807" target="_blank">📅 16:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آیا دزدها جیب ماموران را هم می‌زنند؟
🔹
سراغ مجریان قانون رفتیم و از اون‌ها پرسیدیم آیا شما هم مورد سرقت و موبایل قاپی قرار گرفتید؟ پاسخ‌های جالبی شنیدیم.
🔹
پاسخ‌ها را در این ویدئو ببینید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/695805" target="_blank">📅 16:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aeafcd985.mp4?token=b6jkDhjlJspd9c3ypvx1dfT85C49CbNcmQpnn-9x5Zb2_m3cKHTf1XQx4RzsNKcUSrcedCM76siNXzO6ko6LSM8iiUEgPDBeKwHezV8by050PHtJXgwGuQbBNMhIJ6AP3htZV4hElvQCtSyUtLS9yaLFKbEjSZEMuO6I45g3LkSCvpWonQt4MsQLZ67ki8JpauwqQcTLkwsgoCGx9z-rIwtxlk2uD84-NobNYW2QqYenSTM6iehdOoO3jKAGpmgJCc3icytxUlkd6j3k8yx0bYeRqPdeUtEoVqenXjetX1h4hdD3-N1BjR55QVV_RSath1kvRKBn5kqT1d-PS4PlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aeafcd985.mp4?token=b6jkDhjlJspd9c3ypvx1dfT85C49CbNcmQpnn-9x5Zb2_m3cKHTf1XQx4RzsNKcUSrcedCM76siNXzO6ko6LSM8iiUEgPDBeKwHezV8by050PHtJXgwGuQbBNMhIJ6AP3htZV4hElvQCtSyUtLS9yaLFKbEjSZEMuO6I45g3LkSCvpWonQt4MsQLZ67ki8JpauwqQcTLkwsgoCGx9z-rIwtxlk2uD84-NobNYW2QqYenSTM6iehdOoO3jKAGpmgJCc3icytxUlkd6j3k8yx0bYeRqPdeUtEoVqenXjetX1h4hdD3-N1BjR55QVV_RSath1kvRKBn5kqT1d-PS4PlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه‌طوری هم دانشجو موفقی باشیم هم پول دربیاریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/695804" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXbpD_0MQ0Y0_pg2vbTVJHjKc3d3hYK3YzmwoM6AbZ6JFCNQTjrQEInkMkEbu_7Aku2ofPdJcbZr_I2WKDCRuZH8sTPlKxTMS27tZzW3E8_fOc3Wh5v762Ee9vUri7X4dFA1YAnqSo4cEgWBm1i40mCCFpGdahbB2ysWIrLP9-NrsUYym_NM4Z3FcDkYK-J8lZc6nyp46clh5Kn2xKnRyPva18eyEfM_fM1VOHPp5vZJv9e0oc9ajvDB5DbmLvreNWeFO6t1a_oexCa77x6V002GdC6UlEo8zoPVqqzrUiabfXp1DJLo9__P4Xd1ZWqKyX5ivsg9Wfj3Xm1j4efSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرید زکریا، روزنامه‌نگار آمریکایی : جنگ ایران تا چه زمانی ممکن است ادامه پیدا کند؟
🔹
مشاور سابق جو بایدن:تا پایان دوره ریاست‌جمهوری ترامپ.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/695803" target="_blank">📅 16:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
گزارش میلی از عبور موفقیت آمیز از بحران/
۶۵ هزار و ۸۸۰ میلیارد ریال به حساب کاربران میلی واریز شد /
۲۴۷ هزار کاربر از خروج سرمایه پشیمان شدند
🔹
۶۵ هزار و ۸۸۰ میلیارد ریال به حساب کاربران میلی واریز شد
🔹
تا ۱۲ مهرماه،
۴۵۳ هزار درخواست برداشت
کاربران میلی به ارزش ۶۵ هزار و ۸۸۰ میلیارد ریال با موفقیت تسویه شده است.
🔹
همزمان
۲۴۷ هزار درخواست برداشت توسط کاربران لغو شده
و مبلغ آن به کیف پول میلی آنها بازگشته است.
🔹
در حال حاضر
۱۶۷ هزار درخواست
دیگر در صف تسویه قرار دارد و روند پرداخت درخواست‌های باقی‌مانده ادامه دارد.
🔹
در مجموع تاکنون
۷۰۰ هزار درخواست برداشت از طریق تسویه یا لغو تعیین تکلیف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695801" target="_blank">📅 16:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2Y5c7UYCiWymTOxjS6Hno8Sp_zB9XOVHbTSe-Jdvb8wkn-qsyVoLjElubNJROqyzTqgCr7ZVdntqwr3gguuoRFREXDIq55vNPMgU2YMKYCPHS6V1QiYNQxli6oKpMaKu4qGfspaEi_W1n6tGfas5Rey5x8j7LT4QHE3VCIix5tbBkCag9umtux2QTrjxcx1c6n_wmoW5va6r_fklUL-RKmobcWRvKFE09LX9P5N5ct4TRE57wOy3Ob0hhKqpcSlr89kov7FU1o2xvkxmBibIWwpJwNG35fsEqSSJ60tRZk0cYJ4ISwttccQDX0jsXzCYBr_qDlsrZnL-tVRedCz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والا: نتانیاهو نگران وضعیت انتخاباتی لیکود است
🔹
طبق نظرسنجی‌های این هفته، لیکود به رهبری نتانیاهو ۲۰ تا ۲۱ کرسی به دست می‌آورد و نتانیاهو از افزایش مخالفت‌ها و درخواست‌ها برای برکناری خود نگران است.
🔹
کنست مجموعا ۱۲۰ کرسی دارد که بین احزاب چپی،عربی و راست‌گرا…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/695799" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEfrSu5y70bIUgsSo8g0s-V3yd5ElU2FEhRZZbM1oU0yhEPXweJUjwfGaHkRygIG-xRrMuBFiXLoBQR3w_N456bk5V0tI1-bOgtDXPMUosRpbiTKeJNcbx8HXXPRvaekZ2HcPEv_4UsxuZ9BUjUePlntzLI4KrTlspQ7lDOUZqY5oGPzXgv0AHYSkv9AqdCl9V5Yy8oIcvoNql52R3wsfTRoP1ZlLQI6HculsZTvv0WcqAiVvcwiBxA5HAchATyBP1strST5cNFiPX7Y6BSFZNdDayKUo12GjOPfXvMh78qxVeXHrqgegLWF0wacQEMkWERw6fzizmac0YWtHJxe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ خودروساز ژاپنی برای رقابت با چین متحد شدند
🔹
تویوتا، هوندا، مزدا، سوزوکی و میتسوبیشی با اجرای طرح SSA به‌دنبال کاهش هزینه‌های تولید، حذف الزامات و قطعات غیرضروری و افزایش کیفیت و قدرت رقابت با خودروسازان چینی هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695798" target="_blank">📅 16:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
روحانی: بسیاری نظامی‌ها می‌گفتند آمریکا یک سال پشت دیوار بغداد می‌ماند، شهید سلیمانی معتقد بود بغداد در ۳ هفته سقوط می‌کند
؛
قدرت سیاسی باید در تصمیم‌گیری‌های جنگ وارد عمل شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/695797" target="_blank">📅 16:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxv-NtcqTKyV5-0dBHfaXnEVETpAw2lay3jsm30uBurnyibrSSDLNQueJwtb_acj7FzrmKi72K02bXWNOqgJlnTAXg7BRyYXYB_b8iV_Z_1SCiv0--3vjBebFADAg48Hld0nHx-QbGC_nUVmNeony_5SeTfM8k2bA1IT5IsekhXVFTadTCXTV5b58WwrCMDwCxEiqJkzw8KZIwhTKqcfzWuOLldc1VQrwRr3EKoNTTfkcXXVkVovWkZnjML0O-Qoa2vx2f07cjD5hOZqO5m_malSapFIB_vMXAn_uNJUGlRT1IOAFEidX22GQp17d7ShRd-7kqYXBVjQnLhNJPTv8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر آرامکو عربستان هشدار داد: ذخایر نفت جهان «به‌طرز نگران‌کننده‌ای کم است»
🔹
پر کردن دوباره ذخایر و همزمان تامین تقاضای جهانی نفت ۲ سال زمان می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695796" target="_blank">📅 16:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGzLwUPaKau81lydM_RVFC96VaWWZo3xIecOP3U2X7lGN3TobKbWU94tECKd7krMe5HTLoCeTi1tQl0hpTSptElpk70ZKgkgUjr976pVogoiqS0Dr8_-79pES5qFueRGbyOB5-q_VLf-6zGbjw2l8mBxQn9e7nSmUMZ7U1BjXmvNLpK0v2A5KM23Y2PAxemWEUQ4qL4nGusk2bzgkHN1ZUUT0d7Bemgqo4hCBSijxz7OgeAXIbg7rGRD6ihhlVHrJ_ZiG--dylHdJZoiRzxjQzep5p6ZMSJ736jGEYfJcPCSZKBfLcUVJucwax1EU2kjIl6fztzpt-ZkY9ZgbAmjjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز دوشنبه ۱۳ مهر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695794" target="_blank">📅 16:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695793">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7f0a82ae.mp4?token=E0ngr5wZDZvYFdzTJR7yvOfKJbGLNE3zh2zi1SxI9I4HKg3b9bWdwlJvGnrnrNBS7tioUoKwEXCP6UNRGNLwli5VvIze-4_3bX5XM6jZdI89PdirPy7Fd_Sg0csL98-jjigrcl_BeDW2lt5ZB6Subnu3ck7WXhL26M2Go_gHYr0sCimg_20znFwAcFf20gMF4-RyR0a0a9J2tSMTEC8nyXhqVkUP3IOxliWAqywvL6AKkqJR_LvYSfSEQB-1c43_DbkYkrdftMUWWTFbZoeeI1si-z5DyMNBLTflw-WBOLrghOgaBmO9gf0yz-a12kC9PAeLefYUwzMFrei4X_BJbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7f0a82ae.mp4?token=E0ngr5wZDZvYFdzTJR7yvOfKJbGLNE3zh2zi1SxI9I4HKg3b9bWdwlJvGnrnrNBS7tioUoKwEXCP6UNRGNLwli5VvIze-4_3bX5XM6jZdI89PdirPy7Fd_Sg0csL98-jjigrcl_BeDW2lt5ZB6Subnu3ck7WXhL26M2Go_gHYr0sCimg_20znFwAcFf20gMF4-RyR0a0a9J2tSMTEC8nyXhqVkUP3IOxliWAqywvL6AKkqJR_LvYSfSEQB-1c43_DbkYkrdftMUWWTFbZoeeI1si-z5DyMNBLTflw-WBOLrghOgaBmO9gf0yz-a12kC9PAeLefYUwzMFrei4X_BJbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپا؛ همراه خرید بدون کارمزد بازنشستگان فراجا
کیپا (شرکت توسعه تبادلات پایا) ارائه‌دهنده امکان خرید اقساطی بدون کارمزد است که با انعقاد قرارداد با کانون بازنشستگان فراجا، ۳ هزار میلیارد تومان اعتبار خرید قسطی را برای بازنشستگان در نظر گرفته است.
بازنشستگان مشمول می‌توانند از این اعتبار برای خرید از فروشگاه‌ها و هایپرمارکت‌های طرف قرارداد در سراسر کشور استفاده کنند؛ بدون کارمزد و با پرداخت در دو قسط مساوی.
برای مشاهده فهرست کامل فروشگاه های حضوری و آنلاین طرف قرارداد کافی است به نشانی ذیل مراجعه کنید.
https://B2n.ir/nm1615
#کیپا
#فراجا
#بازنشستگان
#خرید_قسطی
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/695793" target="_blank">📅 16:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
جولان شپش در مدارس؛ تهران رکورددار ابتلا
🪳
🔹
در سال ۱۴۰۴ بیش از ۳۵۵ هزار مورد آلودگی به شپش سر در کشور ثبت شد که ۷۸ درصد آن مربوط به گروه سنی ۶ تا ۱۸ سال بود؛ تهران نیز بالاترین آمار را داشته است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/695792" target="_blank">📅 15:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba778d5187.mp4?token=IK4jAArmpkDP118hV8UfHv_imTjeZxaIM14W5umueWlgoruS7sTb7A-16O-dEiIQ3KH6mO1b-0JPhVSB4DVLSlvImlD4wab1amFwQYj7uNruQbzAtEDUTEmaCZ7UmpMagB63BodDbj1yYv6OeLNKH93P9MLago8Z5csl0of4t51DXxCFJO9pBAyLEGtoDZZwR3LJgqXaBHhnC6C4oFLV758EdDTJGbWCOkSA1mOP5HfTg12eS2JvcJm0xGbkab8-vjh8McVd7JCbRipk14jgdwADkJkZVE353Hy4sT7mNzKWkt4I92OCXs5RqoXHkinmdE7HcSOInpav3nBCeAan0yPwsmbKZ4PuPn3jfAsVPfC722226aMzsvV01ltBZD3SFBKcL2WrExfsZpaeKtvDzNTHik11XRWgrPSNQGN6i_5EmLDHc82nvAPcg09d0pwNUke74yysjvvspU9bhrO5NYNkfwv-pVB4zwHxgcE5gmONPKne1G66M3KpfXLrV6isVmR1guArJCUWJzaCdlGSA368AbF0c5AT1Eo76CKtgIe77xbs_GG_5_yFs3YkkOaxABruT6OjgryCU4jpGp5q5LfPvqh4ihjWH7Fcax9BjXHd4J1NAUZFf8bx2YLkdD1-cIABBxpi_pNxmxWgUBkSnB3bthLriM_f7wSKTJALo3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba778d5187.mp4?token=IK4jAArmpkDP118hV8UfHv_imTjeZxaIM14W5umueWlgoruS7sTb7A-16O-dEiIQ3KH6mO1b-0JPhVSB4DVLSlvImlD4wab1amFwQYj7uNruQbzAtEDUTEmaCZ7UmpMagB63BodDbj1yYv6OeLNKH93P9MLago8Z5csl0of4t51DXxCFJO9pBAyLEGtoDZZwR3LJgqXaBHhnC6C4oFLV758EdDTJGbWCOkSA1mOP5HfTg12eS2JvcJm0xGbkab8-vjh8McVd7JCbRipk14jgdwADkJkZVE353Hy4sT7mNzKWkt4I92OCXs5RqoXHkinmdE7HcSOInpav3nBCeAan0yPwsmbKZ4PuPn3jfAsVPfC722226aMzsvV01ltBZD3SFBKcL2WrExfsZpaeKtvDzNTHik11XRWgrPSNQGN6i_5EmLDHc82nvAPcg09d0pwNUke74yysjvvspU9bhrO5NYNkfwv-pVB4zwHxgcE5gmONPKne1G66M3KpfXLrV6isVmR1guArJCUWJzaCdlGSA368AbF0c5AT1Eo76CKtgIe77xbs_GG_5_yFs3YkkOaxABruT6OjgryCU4jpGp5q5LfPvqh4ihjWH7Fcax9BjXHd4J1NAUZFf8bx2YLkdD1-cIABBxpi_pNxmxWgUBkSnB3bthLriM_f7wSKTJALo3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف چند کیلومتری در یک پمپ بنزین در دبی مورد توجه کاربران قرار گرفته‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/695791" target="_blank">📅 15:51 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
