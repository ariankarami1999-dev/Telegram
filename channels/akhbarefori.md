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
<img src="https://cdn4.telesco.pe/file/FgUkLoYSNrrEMpnQmIh38a6wND7OXXNxnBcjHY1ff0ky9HFvZ3y6dXyrlKCI3Tcq5GX0KRumJZ1lpZcszQM9LrmfxJV23b4Q5Gp71IgGFhEFIDkx9Gv8FU7yqsOY5aUk0xgGP4mWhCUoMNwI4ex0GWowMTmEWPkmA3_-hTB0RyJDqD2jUAAHDkhxBhT7Zjyx8aNDhaVeq2UU54mMqSOWKg4_NF0o_v_2cD3otR4vU2bWR7guo1766zGr0iIg3Sxe5kwuf_VvAUeLvW1K2XBjGIRtoAPFWXAkaCANW6YlcesESPIz9WWJN3LRq-x5sJCoUpcNshNJtkFLARfacFnL9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-691840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u26CPuFqhvoJhDxg5KN3U8zDDlJtFlTRo23s7mCOgH_Ca7c6A8Re0gLKjODeaZDOVpv2S2rnrOA2UqIBZfFOuIIYAi775BTQK_7rScZd0Waj3N5340MOAaR01pyymefp2zfUuUZ7YXiEokmPBLsZJydERH-bTiRDW9fwq-2b4kPt3KtdTrQoqELZQnz8BNHZWC90G81H9jN9vSIsS8KXiE1BQzBUNhVvl_6_i1kM0n_n7hmY-bxxJSmcU60JAoEiJ5MuCjRKrPMBClwD8Mdzmk7Pwc9ouT0HXFHXkuBYEyaff-fqRV-tueaKca06ZUsQMr3m0r6KRAx2_ntUMoYgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b1ea7144.mp4?token=Yyv00Cr4eZFd2FRavOZ7J1imvQu3fPF_3q1PFlK4CIOsW_fMXNiNJtasq8CPkLrIElOq6hEFl6sAyKKZLOULewrxIFjKTjKIcRg8Zy0SKQTuYeSyLKY7rVqJ4UmBu2dQz41VFqKThwqa6acupeSrjyrRM3VTwggeylyOcjBcpkAdB5Sw508RsblVuQvkAut7m7iRPj425Vd4wFiYPSGw6q8zNk49pgCivOZ-wTmYgVPm9cVGODALjEBRn04Tmojgm4MNAYjiErIGS9dpGkWHw_WZUlUK0IWu9JziiW0QNoEAmhSli3O_g4W7D94HJjfbAk0QyyFIfFRMieC--pjJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b1ea7144.mp4?token=Yyv00Cr4eZFd2FRavOZ7J1imvQu3fPF_3q1PFlK4CIOsW_fMXNiNJtasq8CPkLrIElOq6hEFl6sAyKKZLOULewrxIFjKTjKIcRg8Zy0SKQTuYeSyLKY7rVqJ4UmBu2dQz41VFqKThwqa6acupeSrjyrRM3VTwggeylyOcjBcpkAdB5Sw508RsblVuQvkAut7m7iRPj425Vd4wFiYPSGw6q8zNk49pgCivOZ-wTmYgVPm9cVGODALjEBRn04Tmojgm4MNAYjiErIGS9dpGkWHw_WZUlUK0IWu9JziiW0QNoEAmhSli3O_g4W7D94HJjfbAk0QyyFIfFRMieC--pjJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماساژور تفنگی 4کاره
خستگی و گرفتگی عضلات رو با ماساژور تفنگی ۴کاره از خودت دور کن
💆‍♂️
✨
۴ سری کاربردی، طراحی سبک و قابل‌حمل؛ مناسب استفاده در خانه، باشگاه و سفر.
🛒
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63579/180124/</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/691840" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCwcXAYfZ2PbZaSVPl08z1l9b7LjRHoPZEnEiDIfIhN3rorLDxjU3TFvCqH6pL-ehQayAjZMYuuMoHmAvpGu1OqMP-5WYuMeQijUO2PyciJR22xkCdZNzg-plSQkS3cpjwrONhdZAlCiOv0YW4bwJZkuGye2GpGUBE7jXH8SekFtmnAt8xqo-7CTGnWUk3di4Uvn5NDAAutvmmupdMHEHvZHiGpc3V6iKE5BypgL33cdt4I3C3cuvF4MVebDIPFlbFuQ1iBIbxvY0f_5-Em60LN-ouxHFNpw1pPP-2xPMDsMUfCPPtA5juNFOFC4BnnbqGkDzWl6-yZgw0N5mvyjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ائتلاف سعودی: ریاض هدف حمله موشکی نیروهای مسلح یمن قرار گرفته است
🔹
ائتلاف سعودی در ادامه مدعی رهگیری و انهدام این موشک شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/691839" target="_blank">📅 00:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq5LhXYHrXbpO5H4kQ0qW3Uf44OsQDmZ9SuvwPyTh0mv03BBOTCyRCThT5TG66sesUcI8x2RHkNlOJdGTkDhFkNQhX6sh9L7OoDAh5SDtj7S8OuCY13QmFCEWDHsVOhvrNqod6ONLB3H4iE322D8ayFe_FVXfxnsCKgoITDQz8p5tjSyF9m5aNAX6DX8KMCxjBNQ8H2Z9Datd3zEmFmssqbJyLtuS2IFVbeGUOoY-Gn4thKDzwB0OZpFjxBX77ZRVFVbeSaVk43qYW9ZDrxAhTDLkAuYl4V_9u1rGMChNjkNINIeZQtSDTV5RTUNdA1iRD21mo8K901yN6DbpqaLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادویه درمانی
🔹
ادویه‌ها فقط برای خوشمزه کردن غذا بکار نمیان، ببینید هرکدوم چه خواص درمانی دارن و چطوری میتونن به سلامت بدن کمک کنن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/691838" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691836">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وزیر اقتصاد فرانسه در واکنش به انتقادها بابت افزایش قیمت سوخت در این کشور: «من نه دونالد ترامپ هستم و نه فرمانده سپاه پاسداران ایران»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/691836" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691835">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نخست‌وزیر عراق: گروه‌های مسلح عراقی، تحویل سلاح‌های خود را آغاز خواهند کرد و انتظار می‌رود این روند تا ۳۰ ژوئن ۲۰۲۷ به پایان برسد
🔹
به دلیل جنگ، ۶۰ درصد از درآمدهای ماهانه نفت خود را از دست دادیم
🔹
اگر گروه‌های مسلح پس از پایان مهلت تعیین شده به فعالیت‌های خود ادامه دهند، آنها را «یاغی» تلقی خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691835" target="_blank">📅 00:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691834">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران از ۱۶ تا ۲۶ آبان در تورنمنت چهارجانبه عراق با حضور عراق، لبنان و فیلیپین شرکت می‌کند؛ ابتدا با لبنان و سپس با برنده عراق-فیلیپین بازی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691834" target="_blank">📅 00:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691833">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9_2SiPDAhLRIGni5PxOj_1iI_3aJvUx01AgavRl8sYAzPV_VC6HUwM4arS0QW-7FXxwaX1MK3E4iUfYh7SYrrVkBY36mURCZtUORxuWPSwq12e85LwkFCvNQhHTFIzWXQXmr41mQiVgD34NyM6rTYcbELS3NFRybYRTpX1hMoP3WV0RZxIP3WI2HUWAn2OBXYiu51kOHlxc2zdZpy0tD5BrDR-iKo2kroxvG-YgkUTxQAMIwoVrrw7f36toB2Z_qCGPSbQXPpLM8l1YVTmQy4IgwbqA0J7tTdMw8g7iAuY3wgNoOD4XQU_Lzyl-t4FjKWnslBD1oEcs9gbONvrYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/691833" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691832">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_E9C8qY_GLFBbX0ovs-dOvS_p8JcIMWf5ezTYt9H84kVBt0HyY1eL8Fpl9Dwk230tJKP8yPcg2D_5lVwSNFkaZ6POqBUZokBnu3VVyUfyWHf0ZUlTr_Z1D5IrkoFYOiu737BAvzSPDzrOLL3axF2CNS56LyVjgNcSYKd2dvV7w1L87ZOgFefu9CVjvQNp_8ckJDDNWVxy0t6oMBb0wcdcQdHif_Oi4qQCiw41Rhn2Gt1RlL3Wx5MrfssgsFN5awK7Jo5JqpukEMG3_AizvaL9kcH1g65VHVKOLvcJHxf9a099JFx8EP8HLgByOFh6J7ACRMu8qv0kDhzcapg0_9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواص انواع گیاه هایی دارویی و عرقیات رو بدونید
🔹
هرگز در مصرف گیاهان دارویی و عرقیات سنتی زیاده روی نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691832" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691831">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: احتمال دارد آمریکا جنگی تمام‌عیار مشابه جنگ ۴۰ روزه با همکاری متحدانش علیه ایران شروع کند اما آنچه می‌دانیم، این است که روحیه سربازان آنها خوب نیست و ذخایر تسلیحاتی‌شان هم در وضعیت مناسبی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691831" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691830">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/274b445379.mp4?token=AoH_-GVDDX9fNng87_DjjYiv74rzfspMuiDk6JhK-bUyT-e1mKKMFvhn9aPGGykzLG6s3VoRIxCk3RFl1CdJnUaOO2sDScaCm8oa48VSCzkgjW49GKRFIZqgo90Ifmcp79KEE-ED7-GYMWzQIAUMDVwSmDkaraOySmeDmdYRRIkaLKrJdIcm3C9W_p9pApt7ivvN9yO3SZQt6SIIsnqQx3bDtPG_Lz8Z2s59bimwckGryFR31D9YZb3znHmBR2CWA2FujxCu9nJ97a2ew_9zQMV3w_4-_agQRR65rwNuU0wh_EiDQ2Zs2zw0U-PNBNOBBsiUx-5DXulxFbZLzPDtU2l6FvWe9xwwGHa6_OfYN_rbfGCBMXYmarcu3MdcGzqhjpHP_cc-Rjpd9v_WFLKWIJHed_Ytl-xgzpASw9SnafnEvTuJCRCVGHbJpWT9I1j3SU1fJjTw6TkLmMfLRFHyEh4R0QyGfaIcit8AXZQZp0vYwGiXO_EkUVRE6Rd8t_LIvT6pR2jBLimy4bsQD9rYH5Ik9lfFJNQDsLrSVbKfGQVTWItKp-9WNo3j155GoIRsWfpBPNaYE6AV8WYAAih3RhDxjBg6KjSATHzt6xpX_lYlkmy3KfPflMYkjfEhnwVdbWqtTbjac_n8tbYWahUobrj6xvaAolPUY5cqrS1X3n4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/274b445379.mp4?token=AoH_-GVDDX9fNng87_DjjYiv74rzfspMuiDk6JhK-bUyT-e1mKKMFvhn9aPGGykzLG6s3VoRIxCk3RFl1CdJnUaOO2sDScaCm8oa48VSCzkgjW49GKRFIZqgo90Ifmcp79KEE-ED7-GYMWzQIAUMDVwSmDkaraOySmeDmdYRRIkaLKrJdIcm3C9W_p9pApt7ivvN9yO3SZQt6SIIsnqQx3bDtPG_Lz8Z2s59bimwckGryFR31D9YZb3znHmBR2CWA2FujxCu9nJ97a2ew_9zQMV3w_4-_agQRR65rwNuU0wh_EiDQ2Zs2zw0U-PNBNOBBsiUx-5DXulxFbZLzPDtU2l6FvWe9xwwGHa6_OfYN_rbfGCBMXYmarcu3MdcGzqhjpHP_cc-Rjpd9v_WFLKWIJHed_Ytl-xgzpASw9SnafnEvTuJCRCVGHbJpWT9I1j3SU1fJjTw6TkLmMfLRFHyEh4R0QyGfaIcit8AXZQZp0vYwGiXO_EkUVRE6Rd8t_LIvT6pR2jBLimy4bsQD9rYH5Ik9lfFJNQDsLrSVbKfGQVTWItKp-9WNo3j155GoIRsWfpBPNaYE6AV8WYAAih3RhDxjBg6KjSATHzt6xpX_lYlkmy3KfPflMYkjfEhnwVdbWqtTbjac_n8tbYWahUobrj6xvaAolPUY5cqrS1X3n4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر: احمدی‌نژاد و روحانی نفوذی نیستند/ ادعای ارتباط احمدی‌نژاد با موساد، توطئه دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691830" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691829">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
عراقچی پس از توقف کوتاهی در قطر برای شرکت در نشست سازمان ملل عازم نیویورک شد/ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/691829" target="_blank">📅 23:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af441ab91b.mp4?token=iqULHrz-wNluKsb2-khCX2pgwfQH0CKRZheJ8FMo3VVt0AsQNWTWhs8piYa0jIUQm1n4gK9buNz51M34LmiaU3gRoyxdRDTe3U4TrB5F9QyRxW7oSTZaO6a_AFjzNUREtjxtPBY73L1W_RXl9dIGEtFP7IErPVydjocoAI8EexfVRldqZzDdS9zwDj9DuD6eZFTarTqDIzfTW-nYauzLCnXa024xAhHn8Io75jtJf91P8JUzfJ7N458kqU3jRajH3oE4P7jUgpnSRSDnzZznS_C7T4ycBr7L0SHeCJ49JeyE-NL5hFsC4faN53yl7sZYVHgs03FYLBMGIQj6opa2Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af441ab91b.mp4?token=iqULHrz-wNluKsb2-khCX2pgwfQH0CKRZheJ8FMo3VVt0AsQNWTWhs8piYa0jIUQm1n4gK9buNz51M34LmiaU3gRoyxdRDTe3U4TrB5F9QyRxW7oSTZaO6a_AFjzNUREtjxtPBY73L1W_RXl9dIGEtFP7IErPVydjocoAI8EexfVRldqZzDdS9zwDj9DuD6eZFTarTqDIzfTW-nYauzLCnXa024xAhHn8Io75jtJf91P8JUzfJ7N458kqU3jRajH3oE4P7jUgpnSRSDnzZznS_C7T4ycBr7L0SHeCJ49JeyE-NL5hFsC4faN53yl7sZYVHgs03FYLBMGIQj6opa2Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای ویدئوی جنجالی آناهیتا افشار چه بود؟
🔹
این ویدئو بخشی از یک کمپین تبلیغاتی برای یک فیلم سینمایی بوده و ماجرای انتشار فیلم خصوصی واقعی نبوده است
🔹
این شیوه تبلیغاتی واکنش‌هایی نیز به همراه داشت و برخی کاربران از اینکه ویدئو در ابتدا به شکلی منتشر شده که می‌توانسته مخاطب را درباره افشای واقعی یک فیلم خصوصی به اشتباه بیندازد، انتقاد کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691828" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M80r0WMn74vvYg0LP_Qbr45rTQ4b7Myvp7wrIm9KsfXs6k6jBeulIKjuDhrqfGn5qe7BOuLHBSKBUERrh5OH38wIJBJXXgou5qJAPhQuGB-rM5NDUAjQNFH77ftsWX9EiszwTbBPtlvicqE-CizjyFxG5binoV_1G2OwZKGmINvqFXBevCATAMBDG7F-AUUBsF4boVwOiqb9igj4ThtWfMR3Lwve9G9M5WtgwlubTGvrkgLI3iPAgKypQCwCO_kSCHQa25oPAtW8-HVRaexVe4hmxvPg5UoeHQl6PpmDV9XODtdvDoT93RzOHLDinaGGGvkB47HkRwbhYcrHSCKSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس از آینده ریال؛ روایت یک سیاست کم‌اثر | چرا دلار دولتی نتوانست ترمز بازار آزاد را بکشد؟
🔹
دلار در بازار آزاد در محدوده ۲۲۷ هزار و ۵۷۵ تومان معامله شد؛ رقمی که نشان می‌دهد عرضه ارز دولتی تاکنون نتوانسته مسیر صعودی بازار غیررسمی را متوقف کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246934</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691827" target="_blank">📅 23:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nez8DDD-FYSa0LNUTa6Bdd_9QJC2Pu8z7m0pMX-vi5OAhROh3QJEhYrs5ZlhT3NP7Ki2f62QxPH3qvqSiwI61S8lfpaIqPH7WZQ3o_qe0-g5Xoxhobvxvo186_DeviAnX31Rv70d-jby1QEb8hwey-BiMs3AKMJdjIHlV8CKMFwYbY4CC9xRGxa5OjNPADPp3SGU-eGz9u3LNAAutXBdb3DEqCqVjbsS0Mj8PlWGeVYHzUSXEmYs7zaIa-94uYbgJPrAYzgyKEOY3SC5YIYNbmw9VulpUXY-gYTNxLEbvNNbUce0MgrtIMQTpfGz8XayLDzO2FrbuRXQbJ9GysGGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از روز اول مدرسه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/691826" target="_blank">📅 23:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ویدئوی عجیبی کاخ سفید منتشر کرده؛ ترامپ سکوی جدید فرود هلی‌کوپترش را افتتاح کرد!
🔹
ترامپ مراسم بریدن روبان برای سکوی جدید فرود هلی کوپتر جدید کاخ سفید برگزار کرد، اما اظهارات او به‌طور کامل به دلیل سر و صدای بالگرد که بر مراسم غلبه کرده بود، شنیده نمی‌شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/691825" target="_blank">📅 23:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK936RPUJxudcvCQhxg_fe85V5Y-xPswJYtnzTWjGQHS_EUbrvGKu1TWINYdNUU9xt0g4Tg5hMbvBoV0YC77buMUqIdbWVSR70GbG7o7xX9_Eb3gTh-Gx-YqZ3vkw9GoLuSDWmEkJCq_IGsdX9HPHtbvhxoqAvW3A51RJMe0liQcDHAPQR6RuOXd_KS_QLi7O8drkujXg24Zi0dARvLPRVxECkMPToCJ9X5jUUZ1AJkRJw3XwKn5RdhazLxQt5D4to6fFoqvjkFgP6G-lH3_Jt9kgtkYW5QSBmWshMmqYnD7EKcyah5EaefO1ANrMCC5_DwnFkTbSPLrLBc0YL_WMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیماهای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691824" target="_blank">📅 23:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
خبرهای منتخب را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
شی نورانی ناشناس مشاهده شده در آسمان تهران، بشقاب پرنده بود؟! | شما نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3246809
🔹
جنگ نزدیک‌تر از همیشه | منطقه در آستانه یک رویارویی تازه | آیا نیویورک آخرین فرصت دیپلماسی است؟
👇
khabarfoori.com/fa/tiny/news-3246818
🔹
محمدباقر خرازی آزاد شد؟
👇
khabarfoori.com/fa/tiny/news-3246774
🔹
داستان ملکه عرب که با بشار اسد درافتاد، تبعید شد و به دمشق بازگشت | اصاله نصری کیست؟
👇
khabarfoori.com/fa/tiny/news-3246666
🔹
بازیگر مشهور بازداشت شد
👇
khabarfoori.com/fa/tiny/news-3246931
🔹
صفحه ویژه اخبار پربازدید خبرفوری را از دست ندهید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/691823" target="_blank">📅 23:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0155b55335.mp4?token=HNOp6hxH-VZY6kV1I_Vr4v4-0w7D10mE_Sn8RfXKezzr9IIccvBKJEZ4iOKB9RotLcq_1ssQ8SNw5AAiuImPMVz4rlTb5mg-M4itYwjNe1Mgz-ZPTjg1sudJ5ggaUglveop8sfOESGARXDF5lytX1y5OrAbiuYkL9xiWop6nz9cEIBRHZtipcn4h3oR9ziUqOb9SEOrlqhMm8lSMdk4QNgjRA2RUK-J1QKdzBleBmTVqxyy_cdTE2h0VF3G8-kL3naI6KIJWbC0w2vVPhN4IA2YKqUQsw34w86M7sOeixNPBMjwx5cFAaIVZiRIWtGvfDEzg1JOAgebGd9cCmGZeVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0155b55335.mp4?token=HNOp6hxH-VZY6kV1I_Vr4v4-0w7D10mE_Sn8RfXKezzr9IIccvBKJEZ4iOKB9RotLcq_1ssQ8SNw5AAiuImPMVz4rlTb5mg-M4itYwjNe1Mgz-ZPTjg1sudJ5ggaUglveop8sfOESGARXDF5lytX1y5OrAbiuYkL9xiWop6nz9cEIBRHZtipcn4h3oR9ziUqOb9SEOrlqhMm8lSMdk4QNgjRA2RUK-J1QKdzBleBmTVqxyy_cdTE2h0VF3G8-kL3naI6KIJWbC0w2vVPhN4IA2YKqUQsw34w86M7sOeixNPBMjwx5cFAaIVZiRIWtGvfDEzg1JOAgebGd9cCmGZeVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی مدعی شدند:عربستان در مرز با عراق بالون جاسوسی مستقر کرد
🔹
گارد مرزی عربستان اقدام به نصب و به پرواز درآوردن یک بالون ویژه رصد و جاسوسی در نزدیکی مرزهای عراق کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/691822" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
نتایج آخرین نظرسنجی ان‌بی‌سی‌نیوز: ۶۲ درصد مردم آمریکا جنگ با ایران را «بی‌ارزش» دانستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691821" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8df78991.mp4?token=t3oZ1wbsObck3Zx1s13mXCEsGfv47WH3-bgS9o9LEWqQ98p4b1uXK44yfp_F-Yv2QnSD6wOFTng5aw8iIpKgvmBJchQr7Ygcr9LDrB37UESsYnrKGkzxnBrxRZcumwDGQKgNYdjLvQzvuf3pNNRJdRjDj8dOWv33_UorTS_sd7CjlUpPFSRmcuqICw7CO-eY4NfuLXVO-FibeiyHOPSq0xfIRMZNAke7JhxbYMqbr3VVfKZYbcXhSk8rdrfm3QNIYfraF9ZGvCdfLta3ywZ8FWKcEVoktp26X35J5bhG42q5FkqnqAdDgJnTW47i50QKgRL2FvhRuA8B4pZnVamY-gXrua2MtplU6DsteQrCmu-Lp9hcyw0XaAhszKVUkYVsd4HRvGzxdFoxhKr5WSZxBsN5unAu8jdkkzZB9-Z2u9ytbytqLH80BE5AFjC6X6ubpgejaeZiIrEzE3sp1Dql2dG0cl_1qj7Jab69cNEBAOs6NyUmTuE5qZ2bIkiHS25uZYmSEiTA2T7TuXL4DtsRyq8qpIJRDkcSl-4Avb9rT3nRFTjyL6EUQbRqH1jCjTF5I-wA5d22AKQeegBKmCXj3p0oWFXGc9sT5vtIx0p8WXxioL4qPtCpXU2LG9uN7Jx9ZebsjlxoKdXgEpfqdkQA6NXXvGf6sVyE5bNJlApfw2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8df78991.mp4?token=t3oZ1wbsObck3Zx1s13mXCEsGfv47WH3-bgS9o9LEWqQ98p4b1uXK44yfp_F-Yv2QnSD6wOFTng5aw8iIpKgvmBJchQr7Ygcr9LDrB37UESsYnrKGkzxnBrxRZcumwDGQKgNYdjLvQzvuf3pNNRJdRjDj8dOWv33_UorTS_sd7CjlUpPFSRmcuqICw7CO-eY4NfuLXVO-FibeiyHOPSq0xfIRMZNAke7JhxbYMqbr3VVfKZYbcXhSk8rdrfm3QNIYfraF9ZGvCdfLta3ywZ8FWKcEVoktp26X35J5bhG42q5FkqnqAdDgJnTW47i50QKgRL2FvhRuA8B4pZnVamY-gXrua2MtplU6DsteQrCmu-Lp9hcyw0XaAhszKVUkYVsd4HRvGzxdFoxhKr5WSZxBsN5unAu8jdkkzZB9-Z2u9ytbytqLH80BE5AFjC6X6ubpgejaeZiIrEzE3sp1Dql2dG0cl_1qj7Jab69cNEBAOs6NyUmTuE5qZ2bIkiHS25uZYmSEiTA2T7TuXL4DtsRyq8qpIJRDkcSl-4Avb9rT3nRFTjyL6EUQbRqH1jCjTF5I-wA5d22AKQeegBKmCXj3p0oWFXGc9sT5vtIx0p8WXxioL4qPtCpXU2LG9uN7Jx9ZebsjlxoKdXgEpfqdkQA6NXXvGf6sVyE5bNJlApfw2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه زوم گوشی‌های Galaxy S26 Ultra و iPhone 18 Pro
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691820" target="_blank">📅 23:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZsb-WTU60oX2fVXnwu6uxrNjMndbkvsANgezNCLtID68nBEGgE4DZ4D1rpjamNt3g95KA8RMET8uQgopM2M2ThE9xryMtDl0bMCy3Z913F0kUbYrUUaST_x7N-T-7EODLZNwCiyS3v6iFfhlq7fSO0x3-2igqmZS2ohTUHNHNuAOeuwiyWyyzqaz5-k4OlNyOwMMMbDEbkgregW0ztVdDURXRx3Q3hyDCLoWilCgdAnQbaonflYQ2jaM2PuTFJ0TDX_YPPpSy_Jh812jjUv2Ws-4xavPb_VM1HqSBAs7ChY1x8VPY1bPgu0S5IIkweawkguo2JjyTbcSjY5i6tX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K83MdvSSISpXN8i0z8TOM3UXxJE-2Ol7prRS6K5AaBeDYZ-amcskvudx8DFmpwPNk0wsVOlhVyfFMC-IMW26zJ4SppxEH1xhfNaOBKkgzylKoDQtWQvdY9Noz9qUVv-0aSB4Ewqr5wMEzAV9msvBPD-5vOutEDJGx3B3vIkqCe-huOeN5oddgAAA1tUErLuVzZeQj-f3IWqCQpCqRyAeXQx6HYheNBG_hTC4Dd-P6nSFlUdiSOZidLZCw4aKTmCs1ucFV20Q_Ac-Kp8-3mEMYDyMJIwkVmCDqHbNe4iWcCgnUdalJPsRYLqEYxwu5sK2zSFGOmMBp9j4S08moghr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i628xhg-703gIBw7A6IaeLxJFsIYr4_ga--qJRuDaNdziVEf_XJdx8-G5TU3DkJ8SDZr4OwUn4PbJx9OtqGzhVYYHkmnn2F-pRkjWXC7McI_kUdKQNNrnKnYdZIJW4bwBaJbCP1ri9_UvptvxO8j-xQSCdnqEoXNAudM61aCKfpVmCISa0-R6--XzfNmw7aoZVzFjFhhqAAI_Fa927sNdST0ZlDpF_HvUiWFhz4Esiy--Zu_2IkZiOm95s3_vueMQAO3vzcMA-PT0F85IDbnBvMFl9Ul3sgrAIYfl4aSEC8ySv2W2wvsg_SpilDwVZdPQdVKTZSLkpERKbks7QlIQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وزیر ارشاد: کتابخانه‌های سیار تا پایان سال دو برابر می‌شوند
🔹
سیدعباس صالحی، وزیر فرهنگ و ارشاد اسلامی، از برنامه‌ریزی برای دو برابر شدن نقاط استقرار کتابخانه‌های سیار تا پایان سال خبر داد.
🔹
او در آیین بهره‌برداری از ۴ دستگاه کتابخانه عمومی سیار گفت: در ابتدای دولت چهاردهم ۵۷ کتابخانه سیار فعال بود که با راه‌اندازی ۴ دستگاه جدید، تعداد آنها به ۸۲ مورد رسیده است. همچنین حدود ۴۵ خودروی دیگر آماده تجهیز است و امیدواریم تا پایان سال تعداد نقاط استقرار کتابخانه‌های سیار به حدود دو برابر برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/691817" target="_blank">📅 23:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428d5f3794.mp4?token=G0zCPzwhSOq-Rv-rjV84rmVHMpuNC_ssm4T4iAIbMXZrzjV2GyB_15cXMm97eVMnTKHweq2dLYveNejI_hCJYJutqFCEWOnyPuAn2m7br8Al0ilKtUcuY4_dC3oatGxnZvAkrEUvGd2HyiS9PSqFqKlKgSCn8RzSBSUjme8rSjxChb7QilBDopDPFg2x1F-3EecLcJ1yuTLyrMut71THsNue9yWqhAHL_ppGFLkB-BBip2hsBC2M540gxQdZhqz5--ZX3kOOf0Dufo8q4dVzBdwljr3f58cCKcZzefEu2j449nu86z48kV6hxcy8-iBI21M4G-e6FyVRGS50qCjvmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428d5f3794.mp4?token=G0zCPzwhSOq-Rv-rjV84rmVHMpuNC_ssm4T4iAIbMXZrzjV2GyB_15cXMm97eVMnTKHweq2dLYveNejI_hCJYJutqFCEWOnyPuAn2m7br8Al0ilKtUcuY4_dC3oatGxnZvAkrEUvGd2HyiS9PSqFqKlKgSCn8RzSBSUjme8rSjxChb7QilBDopDPFg2x1F-3EecLcJ1yuTLyrMut71THsNue9yWqhAHL_ppGFLkB-BBip2hsBC2M540gxQdZhqz5--ZX3kOOf0Dufo8q4dVzBdwljr3f58cCKcZzefEu2j449nu86z48kV6hxcy8-iBI21M4G-e6FyVRGS50qCjvmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: «از جنگ ۴۰ روزه تا امروزبرداشتی از ذخایر راهبردی نداشته ایم»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/691816" target="_blank">📅 23:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgZZ2OTAX_J4J7EaFQgtyAMzl6MXrSi0vs9AcryWiMJotBq7-4JyTjpky-givHpNX9hHhbxZHhgkA3DfS6Hbu8Q74Akgtuy3qe5HfLsMqMyr9A_8Fj0NP0TannDNko5nhC5JsYmZuX2yod6vUHQVxHYItx2SX4VBdLuVe3HX8xF1tOEjW3wasc4voP0tYOKmu8lFwj9Zy5YX5uvWT5Na5XG7J5lSeeT3n6NvS5_zGFUZWNZI0H9ppQZbmQR4yrcuRL77G0FibvneHdUYxHLwTH9Lwz4N77g7XRCL_wz5V3bhrdytpMJwOBejoC2V9kyeGcd67XEH51wB2Cq_byScJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی از طواف پیکر پاک رهبر شهید انقلاب، بر گرد حرم مطهر کریمه اهل بیت حضرت فاطمه معصومه سلام‌الله‌علیها در آسمان قم.
۱۴۰۵/۴/۱۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/691815" target="_blank">📅 23:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNSyQh3pWnUD5V8Uzm_eGDezACsBvo7ACNVh8TbZ5NkFVC5yTo5mFRQw_U5fAUcZLhjO-R6WvNdh5JyemWlP4zHgz-1H_qaWemo17JSfqc_hrl8zohuIW1IpQbxcAn6ToZ6XcYRrgGMBN76Vzyj8SkvnAJgFvFZ2Vu5upMiu1uo6Wv6J6zl8B-R8BpR7z5oTC46oiBcx9m-Af42TORi6lrrCquq3rTn0HyqxLgn1y_Du8whEy8ljnLdYQspLUWX_DpxIoKhY-gM5D5ND6RB-DOB_1H70Pic9p121cYcpyv0Ahvjf0B7hSysMKqslKB_qxDx-WvajXMxFwCMV4btmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جشن فرشتگان
🔹
زنگ مدرسه دوباره به صدا درمی‌آید و دانش‌آموزان راهی کلاس‌های درس خواهند شد اماچند صندلی برای همیشه خالی می‌ماند، صندلی‌هایی که در میناب و در مدرسه شجره طیبه صاحبانشان باید با کیف‌های کوچک و لبخندهای کودکانه وارد کلاس می‌شدند، اما در پی حمله آمریکا معصومانه به شهادت رسیدند. امسال نخستین روز مدرسه با یاد شهدای دانش‌آموز مدرسه میناب آغاز می‌شود؛ کودکانی که از کلاس رفتند، اما از خاطره مدرسه مردم ایران هرگز نخواهند رفت.
🔹
هشتصدوشصت‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/691811" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c09d73eb4.mp4?token=dIqr-RdT1SUvcWsFTtgFS_8gKpRG3ajN8NQVDLKSY-LUy7CJDODf1C305k4KiSsHyYrnKtZxfJndBLveBIX8BaPKoyp3XqDsDWnXcSdvG30m3H0l0YNM8PsrLXWf25jFvXNZr0Gz3GcYSEVgJ78JJJmw4GNlHjaNaQErtSNnx8rwQ0j4-hogDjpT9x64C8Prace90aadN7SXuB0_qfPkS4XBM71iX4LEh1AJTVEr3V3im1SbAftNtbEEQU6UUdfUn-Sc0gbXwPtmj202T_QzXZBJbhgWP3ouZn5o88fCJ_RIgnTs7ky1Biazku7kiGS0QvyP1BI2hS8R4a5NN1t7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c09d73eb4.mp4?token=dIqr-RdT1SUvcWsFTtgFS_8gKpRG3ajN8NQVDLKSY-LUy7CJDODf1C305k4KiSsHyYrnKtZxfJndBLveBIX8BaPKoyp3XqDsDWnXcSdvG30m3H0l0YNM8PsrLXWf25jFvXNZr0Gz3GcYSEVgJ78JJJmw4GNlHjaNaQErtSNnx8rwQ0j4-hogDjpT9x64C8Prace90aadN7SXuB0_qfPkS4XBM71iX4LEh1AJTVEr3V3im1SbAftNtbEEQU6UUdfUn-Sc0gbXwPtmj202T_QzXZBJbhgWP3ouZn5o88fCJ_RIgnTs7ky1Biazku7kiGS0QvyP1BI2hS8R4a5NN1t7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه بیست متری حفر شده در خانه خانوادگی دو برادری که اعضای خانواده خود را به قتل رسانده و جسد آنها را دو سال در آن دفن کرده بودند   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/691810" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb9ZSnIqy9TiEWypUHf4sB3KQVJH8dTmzdgIHdRlYfeK14ivkZI7ITLOpirCGNBH7evlCQ-VsVfwsUdRv6YBqQgAKbIHWqC88ac-uAdgCiDJV7G7MT-ZLkIXBOFqICCOSjwWwjJUEzbwFAi6WpdWIj6sXKuervWzKMrObbCZAIZrJYIFvUs49dvtzbnMCXgP6slCQ7UTjNhc8xAxZANqu7GT8fa4XWFJ4o3xjnFsK1IXSwHup8iagGn1W1ZFnKIiGHoKecnjOk_w9ui1kVCKjlAMo8hQOmy-ENug_y423tjYb0kRN17CQgWlgm7Qlqwx4J3suWblrcyo8S-tO-2OcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوک به چین؛ ذخایر نفتی ریخت
🔹
ذخایر نفت خام شاندونگ چین در ژوئیه ۳۵ میلیون بشکه کاهش یافت (بزرگ‌ترین افت ماهانه از ۲۰۱۶)
🔹
شاندونگ محل پالایشگاه‌های مستقلی است که نفت تحریمی ایران را می‌خرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691809" target="_blank">📅 23:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه دوم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ی دوم:
تفسیر دعای توسل
🔹
انسان باید از توجه به منفی‌ها، نقص‌ها، غیبت، اخبار بد و عیب‌جویی دور شود و توجه خود را به خدا، اولیای الهی و نعمت‌ها معطوف کند.
🔹
توسل در حقیقت نزدیک شدن به خداوند به وسیله و از طریق اولیای الهی است، نه شریک قرار دادن برای حضرت حق.
🔹
در دعای توسل، دو مفهوم کلیدی، «اعراض» به معنای رویگردانی از امور منفی، و «توجه» به معنای روی آوردن به پروردگار و خیر و نیکی مطرح شده است.
🔹
غیبت و عیب‌جویی خطرناک‌اند، از آنجا که توجه انسان را روی نواقص دیگران قفل می‌کنند.
🔹
دعای توسل در حقیقت، دعایی برای ایجاد اشتیاق، رغبت و اتصال قلبی به خداست.
🔹
بهتر است انسان در دعاها بیشتر به آخرت، عاقبت‌به‌خیری و نزدیکی به خدا فکر کند.
🔹
نجات انسان در آخرالزمان از مسیر توجه قلبی، دوری از منفی‌نگری، توسل درست به اهل‌بیت، و آخرت‌محوری می‌گذرد.
🔹
ایران خاستگاه اصلی یاران امام زمان (عج) است و سختی‌های فعلی نوعی صیقل دادن برای رسیدن به آن نور عظیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691808" target="_blank">📅 23:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ju06uZ7axtwE5pi3ETsQ_GE45EXsdbDDmrx1GTDWtgCe08oX82RCSumBD3RRtDrXMdQOLcs1HuyJCX5vCpeSVTy0nJIslFD22fw7Ifj5Cf4ExdglAmJadc8GNwA79eDlo8r8cONH_igkbkh0E199S4g-NV84-ZytZ6mW8OCc_7dlRFzsQ9GVWxAlIQZjc2-G60YVVvMc2ZpxI2sNjRg3M7ZQTXrejHehyKAhwHV2ofqKxxzoRB4Pbk6Dp9nZa3OnwdoQio0pFVLlCxQ5o2eXtbjiELn6O3CTXURKTOS9fkw5yJ56BSaxuwuClkZq2FL7CYZoc_8VdIxH5GgI_s3YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6WYSoMS5CD6oG06Z6h3_AAQOUtkwFL9BkIcEsqZWUkUe14G9ojdGrL4nMkVKL11CY5tGvKAqRaKgIxutIXLzTsSC0rlKWWe67MhaWZdgXSC1Fd71SuwltH8H7YXty5xyPCHf7W3yVFhlszoVsli_lQ7-xen7ZxRTxNGzQsumUGBGCkrGZ8iEaL4YhPfT-5s14e3PbgwBHi-aLxV-0sYKbUijFueFxJFFrL3D9aIcPkadfD0StW-xPbgUR87PyEMmzfMWaiVFf5bWA1rZb6CyT9oFHxy8aZqbuDDxwPa0-XJkdxHeILxh_eGtFWvzTEacdA7BLhh5L9xvA1HzcLJUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61b8869c.mp4?token=pyfsGS6GRuvKeOLKKiQ_07A_bjv4WS-3-pk8_DOLQliF7hUrqHwMi5MnaubleXVpDbyTqqpFNL3QxD0FIUiIKQVmsRiyO1sb_PV8QoN9H-ihIN48IOnM94n3ZmFKbvgh6RUzrhoQLMoEfriGU1TUhsvdt8QONzJlBYTXuzeSLubayz7UvAFpptCni3YkcyzG54XbTT3OOD7MO2XdTDBuXVfDGRkqJW_6lWl3PSxi8L0Tb8w75BwjcpmkAvFv1qb9bk9I0fUc3LIO15liQ-eH850k4Ib9lE3JtkfnDzOpIP91grcMaU6LI4plg4KFJSyW4E57ZtUWa9DtX-_B4MywAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61b8869c.mp4?token=pyfsGS6GRuvKeOLKKiQ_07A_bjv4WS-3-pk8_DOLQliF7hUrqHwMi5MnaubleXVpDbyTqqpFNL3QxD0FIUiIKQVmsRiyO1sb_PV8QoN9H-ihIN48IOnM94n3ZmFKbvgh6RUzrhoQLMoEfriGU1TUhsvdt8QONzJlBYTXuzeSLubayz7UvAFpptCni3YkcyzG54XbTT3OOD7MO2XdTDBuXVfDGRkqJW_6lWl3PSxi8L0Tb8w75BwjcpmkAvFv1qb9bk9I0fUc3LIO15liQ-eH850k4Ib9lE3JtkfnDzOpIP91grcMaU6LI4plg4KFJSyW4E57ZtUWa9DtX-_B4MywAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمن: با موشک‌های بالستیک و کروز و پهپاد به اهداف حساسی در ریاض و شرکت آرامکو در ینبع حمله کردیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691805" target="_blank">📅 22:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa4pj7UyCPfFUNm_j02_3cgyUGs-VKkBfdEVt50pOu_Uddm59y-cTtidRLkXfBWMJIEI1erdjl3kGiy1eZ8Tf90hfc2s-oCw0SqZNy5tnvFA4DHeQAV_H53AzWy2wTH6Q40Wxh6loUHW7itfGYxfURER3xHVMD3C_riGO8gN9MoHLjYUTgeYUr7zmcnLGUBMAFvaa22cBqUKLryG2g_LMw2hHRJRi98qxPB5aC6nzMIWdtfPO-TXQSLL5cpMK2gEyBaV2NcL9-rQIeS3SRG2OmjmlCr3Rdtsk0h_EdnNChQilDbE5Mc45X2cMDQoOdZO9duCLk4g_fZKjUm2f6aa4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ پهپادی ایران و آمریکا چگونه خواهد بود؟/ این پرنده‌ها سرنوشت جنگ بزرگ را تعیین می‌کنند
🔹
روزنامه نیویورک تایمز گزارش داده که پهپادهای ارزان‌قیمت ایرانی با تحمیل هزینه‌های سنگین به سیستم‌های دفاع هوایی، «معادلات اقتصادی جنگ مدرن را تغییر داده‌اند». تحلیلگران نظامی این تاکتیک را «جنگ فرسایشی اقتصادی» توصیف می‌کنند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246936</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/691804" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691803">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
استاندارد دوگانه رسانه‌های بین‌المللی در نسخه فارسی و انگلیسی در قبال رزمایش جانفدایان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/691803" target="_blank">📅 22:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
جلوه‌ای ناب از طبیعت مازندران
#اخبارفوری_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691802" target="_blank">📅 22:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691801">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN6FfgAAFa1oLsn9NZ21XUgQddGD49_NtzQaIrlNq_jkic8Ps-y0niOmuv0j1Pb2jwgxX_czlzM7tEyqep1UQBur5eiSdGi5NsSN5U71L0Rf7Zp7MJOfjnyjk0inWOUGTWfj8p2a7XeM3vwUujVjNwyAbNuRTj9ybdUEb7m7nRQ24ek-_hZb4zufcrqFpKSIZGaMd7bxoTQzAtiZoWJ7eeykitiFefUy2kc-cxWycWp12F8SgGn0Z1LbYgLsA2Z2GjQ3l8iMUfSt_sfDJz7LbV_4h42bEJTgssRKDZ8fl0PeCRvri1TJi2Fp9pDXKbMvxYrUeQOzI5OjTW2lu_QaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: باید حماسه‌ شگفت‌آور هشت سال دفاع مقدس برای نسل جوان کنونی و نسلهای آینده شناسانده شود
. ۱۳۸۴/۰۶/۳۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/691801" target="_blank">📅 22:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ابلاغیه ستاد امربه‌معروف و نهی‌ازمنکر تهران به‌تمامی برگزارکنندگان، سالن‌ها و نهادهای نظارتی!
🔹
نصب دوربین در سالن‌ها و دسترسی پلیس به تصاویر
🔹
درج مشخصات و شماره همراه روی بلیت‌ها
🔹
تشکیل شورای امر به معروف و تعیین مسئول در هر مراسم
🔹
ممنوعیت ورود مایعات و کنترل بوفه‌ها
🔹
معرفی متخلفان به دادسرای ناحیه ۳۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/691800" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egR87imUCV-mqRBp6tc0FUMu84u0iSl7_jLatwVxxaHGgbw6Hpo6AC4MbAT2BaYCzKah_XTeyyFE3mxaSktNK4bG8uFAc44-LRRige_00zE77ApCUytPu7WCHtnreBAZz-uks0j5G0eh1dTINsp80v-fa-l4v9Ubu-51i5E5z1JrGgZw5oazGPg6ZnjhsXqkrBJa3L8t5NWLzaPrAxuPJef6K86iYqLtKyTe3HmIzx_a4XOGQNAVcfLicBFQfZ9wbw2dJPCogyneSKtsU9VgEXuXzTfQXWDEj8ZA8RZsneWRfAEA9HZM943Ir7FIQqfeWEFR5BxTMC6lSZnGnXbzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیج فارس و بزرگ‌ترین فشار عرضه نفت
🔹
بر اساس آمار آژانس بین‌المللی انرژی (IEA)، صادرات نفت خام خلیج فارس با کاهش ۴۵ درصدی به ۱۳ میلیون بشکه در روز رسیده و صادرات فرآورده‌های پالایشی و LPG از این حوزه نیز ۶۰ درصد افت داشته است.
🔹
این بحران موجب بسته شدن ۱۰ میلیون بشکه در روز از ظرفیت تولید خلیج فارس و افت ۵.۷ میلیون بشکه‌ای عرضه جهانی نفت شده که جهش ۹۴ درصدی قیمت دیزل در آمریکا نسبت به پیش از جنگ را به همراه داشته است.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/691799" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Z7PskPiXqSYFLY7gndiMZutcyVcJsTLH2HUr3g_8FuS-F8D8e1fUjVpkloMtcMPbDl9a_6NIWiafdo8gVTnEEvuDIBWwKc_K2dvPrwddmHke7b1CnTR_nN3AvvV4NN1L76I_v-YaSLR7qvaaiG7qOrVbmL4Jz5499LbqVoGwDDCWSfcm7dnFGztPOpSijhR30_xLtxzig1mO_Pwp4unxm4SCJjQT5NdztCxCwlVX0FltelKZkNibIM1Mz4RwRhwrTWYDl8KYavKplcA9PZfDLdj5QmhTxSfjTPeX7GTC-Q6qfpRc-8hxA4LGOA0uT1lt6NQqefNTzGF2bZi8Ta3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید کاخ سفید: اتفاقی در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691798" target="_blank">📅 22:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691797">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد
🔹
بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور لغو می‌شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/691797" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWU5v19n7vmOB9VcDqwgyy708HsagVHOUkoJHIkGraklocYC4v1ozygon7RHq-U7hzS6aKZdgPuosvSleHK-lZfkoWMKGy4fl4yyJ_sm7RJ9HGCSQMGmuEAq-drlXEXIhT_m3jLRGjHKKp8b57BczxDfEtOZkFWS-8PhssritqhqwoldNKN1l7Ip7n7VmRMdOL3rpAdm_Nsn44i2kWb1r2lT7IPDycgapbCw1thUPfcwPTN8O4XfYsxpoyQmQiCGOO--maJgAgs7EkeqLVWDdefXx29IqtCg4A8_pUxEZJzZ1YGeObSmr2HrPdGk-7FjoY_n3LzHzvZFCVFsxPhnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgLI7K74VkSDOEiwU16L8DRmXOnwqqUmUMvAa9eevX4CyGmHW_oFNEksR7ncbfGuOHNU_fl7-4JraUhxGoFGt-hd38stTNdlj-E5ck_CoY7la39GzIoXFunl5YnWeURx4pol4SB5PaHUiqcjIbC3D6-Ouv_fIYGZmyH3rSNiFLUwsAfGwfnbND5V8MjmLDrlBJsLv3B47svYA7LaO5-t8zbIvbDH_SyVs3ltjV83OJkY5NpdWzX-3-WYyAKbS-hnvMJqIbdRPSEAWQuugmhiLJt1Iv4uzJpWJyxJQm8sxhxhlw0p_FUE2qtu-iTpsZRzVE0C6jdLv66G_dWKikptHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igVepsvyBB2rcKENp47RK0psb2kYCa-S4P7PNUht4R11qXG90qL1hrbcje-jWT2GEFeYDVArlZluyAdcnJXjyHt-UOpcnKVIUbvecJK0veyWXZVgPhtncI0z9YAEent7Ibry25By6zdoJhcaopY60AFzvrmDGk6zb6Kj3bz_jVtZ3oXpmfESO6yAAg2DrnMIfb4iCCwOe-lJwWBkRD34JRW3xeusIw6hoUN5pVXrCrlYqe633wmU0yiiX_-sIVDnNrPfAxdTGpB_bqsLPxmt2bfOf2xOcGQHhT9lKtty6Ijfdw499j6n-M560EFQr6tsd4yM4SEjrMzw4-V59TifoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHZo17coREhilAkssvRLW8b0Gky9ySqpZp54rYs0pV9x0OCGn1GhRPgzNiUK4aCLiKzp6PudmwffNyh0am291yngzVrT2FKjIQIc_PhLTQk9Ur0C0dHS9OigabfGFhh_RSIg60CvK6c3HCPfzaGkl9FBCXHPpyX6xAWkILLq8uL0u3mlYEqRQtR6QwQWrZydtKtDHw_RgSC98QjIMmB_dySzytxyUbMK6KEjCyCO1c3c2s33v021xVM8YXwW5cvFx2wmkYfZwqq-JxBLOnRkX4qa_JxxUSNQRWKebmDMqSc8G1DUqhTWdOs8149VSSfqMNHVQh2Ij5egpHpRvM6BUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر پیجت رو از صفر زدی این هوش‌مصنوعی‌ها به دادت می‌رسن #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691793" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691792">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اجتماع بزرگ «امام زمانی‌ها»
🔹
همزمان با فرارسیدن میلاد باسعادت حضرت امام حسن عسکری(ع)، اجتماع بزرگ «امام زمانی‌ها» شامگاه یکشنبه ۲۹ شهریور ماه ۱۴۰۵ با حضور اقشار مختلف مردم، خانواده‌ها، عاشقان و منتظران حضرت ولی‌عصر(عج) در میدان راه‌آهن شهردارى منطقه ١١ برگزار شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/691792" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691791">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آینده پتروشیمی از دل ناترازی انرژی می‌گذرد؛ «ارزش بیشتر با انرژی کمتر»
🔹
حسام خوشبین‌فر مدیرعامل شرکت پتروشیمی امیرکبیر، در یادداشتی منتشرشده در روزنامه «جام‌جم» با اشاره به محدودیت‌های تأمین گاز، برق، خوراک و سرویس‌های جانبی، تأکید کرد که صنعت پتروشیمی ایران در آستانه یک تغییر رویکرد قرار دارد؛ تغییری از «حداکثرسازی تولید» به سمت «حداکثرسازی ارزش به ازای انرژی و خوراک».
🔹
به گفته وی، در شرایط جدید، تعداد تن محصول تولیدشده به‌تنهایی معیار کافی برای سنجش عملکرد نیست و باید پرسید از هر واحد انرژی و خوراک، چه میزان ارزش اقتصادی برای کشور ایجاد می‌شود.
🔹
خوشبین‌فر همچنین تکمیل زنجیره ارزش را ضروری دانست و بر حرکت از «فروش محصول» به سمت «فروش ارزش» از طریق توسعه صنایع پایین‌دستی، محصولات با ارزش افزوده بالاتر و پیوند مجتمع‌های بزرگ با شرکت‌های دانش‌بنیان و سرمایه‌گذاران تأکید کرد.
🔹
مدیرعامل پتروشیمی امیرکبیر در ادامه، تاب‌آوری را بخشی از مفهوم تولید دانست و پایداری خوراک و انرژی، آمادگی نیروی انسانی، تأمین قطعات حیاتی، قابلیت اطمینان تجهیزات و توان بازگشت سریع به مدار تولید را از الزامات صنعت آینده برشمرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691791" target="_blank">📅 22:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691790">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
فراموشی نماینده دائم آمریکا در سازمان ملل: درها برای بازگشت ایران به مذاکرات باز است!
🔹
نماینده دائم آمریکا در سازمان ملل بدون یادآوری خروج ترامپ از تفاهم‌نامه، در حاشیه مجمع عمومی سازمان ملل گفت که درها برای بازگشت ایران به میز مذاکره باز است و ابراز امیدواری کرد که این موضوع به‌صورت مسالمت‌آمیز و دیپلماتیک محقق شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/691790" target="_blank">📅 22:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfhjwNbaqOWaWmDLiwr9etDyofEBqE7leNFJRTC817yc0LW1GmgN4Id2HTJBqGpuI0H2CGOT55NT2tr37Zl1Tw4fiCloxkvPNg7dn24mnPPn7oB3cKTXq0KdKCB3lwPcxPjp3zhz1ZrNhN-sPT7iZMPAE8bO1_-jJdUbHQxkk0__mmqipwjHGOu8Vk4TIqjdurlRrGViRRAwFSqIa3-JW7evHu-22lp13RvI7I3cVdBIYUgR0NjF53_f7j_HUifxnk11JgR9z5v47zMOf8wt17JrrrliSx8Eo-yEIIFlNHHsliwM9e7S5gA51A1hZtb1eq-Isc_tT-IGPF6R1EZ4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی نخستین Googlebookهای گوگل با قیمت ۸۹۹ دلار
💻
🔹
گوگل نخستین نسل Googlebookها را با همکاری دل، ایسوس، ایسر، لنوو و اچ‌پی معرفی کرد؛ این لپ‌تاپ‌ها با قیمت ۸۹۹ تا ۱۲۹۹ دلار عرضه می‌شوند و گوگل وعده ۱۰ سال به‌روزرسانی برای آن‌ها داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691788" target="_blank">📅 21:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بلومبرگ: اندی برنهام، نخست‌وزیر بریتانیا، با اعزام مشاوران نظامی این کشور به عربستان موافقت کرده است؛ اما هنوز درباره سایر درخواست‌های ریاض، از جمله حمایت از زیرساخت‌های نفتی و مقابله با پیشروی حوثی‌ها به سمت باب‌المندب، تصمیمی نگرفته است
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/691787" target="_blank">📅 21:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e232785d48.mp4?token=I59j_53DA2z5dnnqY0eZl1dITK0o4X8871HMX_xfedFmTthiiMWTMq6wiaBZcrTBBjMgcVyOsryUPj5XsQvnNLR_25uwmqKe0nOj3R1OvidL17hHd3tsI33FjDU81kTwHNo7uawCWVR1P6ZAD_Igfz7Z5lkT94EJpAYbx4LCOLtrl8SGaZMI9fBjZNWPUNNyjQPnFxI2Zj7lgwM8AUZTRT5Y0OnbqanV-lAHtVs78MLwa4z5B96jKJR_yM6QK3dQfL454SKfe67bFeOECE18Xso2EQgSNQJu5s0obwMpvjw8JMHyNvQ92umjOujppIcX_SPkrPn51xlXoNd2rp7MDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e232785d48.mp4?token=I59j_53DA2z5dnnqY0eZl1dITK0o4X8871HMX_xfedFmTthiiMWTMq6wiaBZcrTBBjMgcVyOsryUPj5XsQvnNLR_25uwmqKe0nOj3R1OvidL17hHd3tsI33FjDU81kTwHNo7uawCWVR1P6ZAD_Igfz7Z5lkT94EJpAYbx4LCOLtrl8SGaZMI9fBjZNWPUNNyjQPnFxI2Zj7lgwM8AUZTRT5Y0OnbqanV-lAHtVs78MLwa4z5B96jKJR_yM6QK3dQfL454SKfe67bFeOECE18Xso2EQgSNQJu5s0obwMpvjw8JMHyNvQ92umjOujppIcX_SPkrPn51xlXoNd2rp7MDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زهرمار چگونه گرفته می‌شود!
🐍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/691785" target="_blank">📅 21:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khDxcWkhaooR8ZUMW6nlDQncEu3ES1DqAjt7jOmo8i5_0tQopc3G0ZVypGjnVvpMuKfXBH5VLZXzjAAvDM4AgaPe32Kvwe2f_L6v9Hu75RllH4-bphM3ZHNYf9YjYHyY2tLoxttJPzCH4LReS7sRf1YmXFDvc2nE64SBFKvSbB290vck41U_w3vW4bmrqSDfPXWLCqEBekYmlE50SfpIm0iKFBLP3DFpSVg4Zlp85ss2ceEKhH0zw7I9ddGMidqnWKDC3qIt4HnDRh6Pyd7x4FI_cT67TtHLNgEnzBulggrL3Z4yhQIyzYuC1sHYElm0JcFlHzEYD2LI4ZIxHAwscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☎️
کوتاه‌تر بگو، راحت‌تر به یاد بمان!
شماره‌های ۴ و ۵ رقمی مخابرات، برای ارتباط آسان‌تر کسب‌وکار شما.
اطلاعات بیشتر:
www.tci.ir</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/691784" target="_blank">📅 21:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=cTDPhtg7uKi3wY_mFpDaD1z2GUVEjLtuvhMmQuaQw1uxFX8PWMOLgT499hkQ-Ig_1qg-FkFJCjsgqZ46IPCQagkzwrJlPn0AXYu2l1QjOy31kmTy8uzLN7RnxoDGJKmfpfbIB-3XQKZnpuLNllIRulSvyol1Jy-tx4bTdzId09mJTD3uHY-LOKkv_CKYA1kOuI_uISaXqr5w02mBB96TJyn6NTuYTL75TXZ9KKlNYvbNSBkx2ZKikogwiup-8zAoP8XbmUtHSgWn95eDCpLconHvMfb8uwq9xYUKOhkPzK083InOBmt6CnUwymfmAVJrlZnahQEkfqw9DjaGOcW-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=cTDPhtg7uKi3wY_mFpDaD1z2GUVEjLtuvhMmQuaQw1uxFX8PWMOLgT499hkQ-Ig_1qg-FkFJCjsgqZ46IPCQagkzwrJlPn0AXYu2l1QjOy31kmTy8uzLN7RnxoDGJKmfpfbIB-3XQKZnpuLNllIRulSvyol1Jy-tx4bTdzId09mJTD3uHY-LOKkv_CKYA1kOuI_uISaXqr5w02mBB96TJyn6NTuYTL75TXZ9KKlNYvbNSBkx2ZKikogwiup-8zAoP8XbmUtHSgWn95eDCpLconHvMfb8uwq9xYUKOhkPzK083InOBmt6CnUwymfmAVJrlZnahQEkfqw9DjaGOcW-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چراغ‌قوه اضطراری چندکاره؛ فقط چراغ‌قوه نیست!
✅
نور LED پرقدرت |
🔋
شارژ USB + پاوربانک |
🧲
مگنت قوی
🔨
چکش شیشه‌شکن |
🔪
تیغ برش کمربند |
🚨
چراغ هشدار
🔥
قیمت ویژه: فقط 1,198,000 تومان!
👇
برای خرید کلیک کنید:
https://memarket24.ir/product/brief/30291/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/691783" target="_blank">📅 21:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
اشتباه گرفتن بادبادک‌های نورانی با سفینه فضایی
🔹
تصاویری که دیشب در آسمان تهران دیده شد و برخی آن را سفینه فضایی تصور کردند، مربوط به بادبادک‌های چراغ‌دار بوده است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/691782" target="_blank">📅 21:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2378c22128.mp4?token=S84vjPlyrE-N6WQMysV5eaN6MLyaavca-4gDoB_2atsg0sM2lBVCi60yZ3sLOlw5QEh80yuFq6TvHrCb99pha7xGM-gBvfJKPTqSAP-nQeLDSEiDC4B8Mr5a5puxRRRxwUxJjIZNsGi2L1gc6r5686_N-_xoLz5-9hWHyjHj37tfRoj92f0brveowMCKDIJJnXOk68quwQfluNeBVt_GuKwUAr1WxRqi2Gi5dbZ1UX7Gt4rEh2y_ZblWJzGo-KUNhTaNGZsEhTlq3afZPoUZ_68Sr-xSn1btuXSdhZyL8XbP6FsmxVSYxDvX6cMSJ8rAFF4l9Apl16hfuFgHk-jVOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2378c22128.mp4?token=S84vjPlyrE-N6WQMysV5eaN6MLyaavca-4gDoB_2atsg0sM2lBVCi60yZ3sLOlw5QEh80yuFq6TvHrCb99pha7xGM-gBvfJKPTqSAP-nQeLDSEiDC4B8Mr5a5puxRRRxwUxJjIZNsGi2L1gc6r5686_N-_xoLz5-9hWHyjHj37tfRoj92f0brveowMCKDIJJnXOk68quwQfluNeBVt_GuKwUAr1WxRqi2Gi5dbZ1UX7Gt4rEh2y_ZblWJzGo-KUNhTaNGZsEhTlq3afZPoUZ_68Sr-xSn1btuXSdhZyL8XbP6FsmxVSYxDvX6cMSJ8rAFF4l9Apl16hfuFgHk-jVOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
حرم حضرت فاطمه‌ی معصومه سلام‌الله‌علیها، حرم تمام ۱۴ معصوم علیهم‌السلام است!
🎙
استاد
#شجاعی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691781" target="_blank">📅 21:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1292afd051.mp4?token=fgxBHlbGkxoCW-qU-nBgboW7XZCxozp_8dmI-Hxv4SVvazvtIBYKNpk6B0ju9Wpkl15PSWfqWd9YgS96U80WlhpTbYMyoYm2L_GgETqco4e9t_AOpRGsIy3t-JkCyQv4XM1v7tcHa0t3-02X4uDZJ1ZQQ3NLYgL8fkRmujn-OzvWMHVKEjvBlM3utJBNepNiiex-X1kq4lHC9UjiUU2Y8h9FljqzfxIWMNNWYwZhGyk7l1QjvkROJtpXxbhLmV47P7ZPhyHNZH0KaKftZOD-LuFnv3oUey1bKCHY-azNAggt60fpHFuplTwIPQf_Xg2EhoJ5MUzlva7_YU-z3ylbPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1292afd051.mp4?token=fgxBHlbGkxoCW-qU-nBgboW7XZCxozp_8dmI-Hxv4SVvazvtIBYKNpk6B0ju9Wpkl15PSWfqWd9YgS96U80WlhpTbYMyoYm2L_GgETqco4e9t_AOpRGsIy3t-JkCyQv4XM1v7tcHa0t3-02X4uDZJ1ZQQ3NLYgL8fkRmujn-OzvWMHVKEjvBlM3utJBNepNiiex-X1kq4lHC9UjiUU2Y8h9FljqzfxIWMNNWYwZhGyk7l1QjvkROJtpXxbhLmV47P7ZPhyHNZH0KaKftZOD-LuFnv3oUey1bKCHY-azNAggt60fpHFuplTwIPQf_Xg2EhoJ5MUzlva7_YU-z3ylbPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشم؛ تکه‌ای از بهشت در جنوب ایران
🌊
🔹
علیرضا وهاب‌زاده
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/691780" target="_blank">📅 20:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a39522b48.mp4?token=UPcgZu0-5i4TxSS8wb5w3uKhaQjwigOAKZA_if8E3STF2CiO7Mf62HnZnvVMDx51Py_GAYWKD8GkMWYY4sRQpWVO1M3No2AyLYTvGD03WJwV4VnbNNJWLsrsqOvg3sOYKegYC835fekwM1ZHzvTCZHONj2o4CPqXoeb-NFmhfeLorVKYd65fnX3QJS4-2V9EI5n9-XY52eRcewqRFS3wvF146J3Nm6ysrFlgbjN45Cu_G305XqUSBuA18IxP5e9Ahiw805aihhcrI4dcnQcmGfPK-JZQ6EE6PYAYVptJmrP78YQ3i1OYVYu4EVsZKQOL4RnCvDpYbk88mreavmtXClzEsTPVkmVkwRHP89vt-ktieIiRzTzIkuyKfUPO6ZPMfCZ7zxVqykgPxGwunYG-jJ4_230uGb2DBtiu_g0kTQ1DaEGzSbLR5VDKZn6CN7xF81p5s3DHTnGVUInbpU83uS2fSJmXzn0mvElP_DVDe2yyGQ09an-oOiFcKtbjk8PrSuiSsYmi1-D0BTRQe1NaK_upGcglfx6zrstaR0XNBmDhkz3vGPW7Ft4bSCGeGgGvlQuz4Xb5svjmr17GQPW331Y6maUOJqPYAJMESR_6I5lKKvi3fYVvrjpjU6jHwbc4wH5OSPGYdfwSg-t7z34rw0dVLbpWhCCmHfgC8j_DzEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a39522b48.mp4?token=UPcgZu0-5i4TxSS8wb5w3uKhaQjwigOAKZA_if8E3STF2CiO7Mf62HnZnvVMDx51Py_GAYWKD8GkMWYY4sRQpWVO1M3No2AyLYTvGD03WJwV4VnbNNJWLsrsqOvg3sOYKegYC835fekwM1ZHzvTCZHONj2o4CPqXoeb-NFmhfeLorVKYd65fnX3QJS4-2V9EI5n9-XY52eRcewqRFS3wvF146J3Nm6ysrFlgbjN45Cu_G305XqUSBuA18IxP5e9Ahiw805aihhcrI4dcnQcmGfPK-JZQ6EE6PYAYVptJmrP78YQ3i1OYVYu4EVsZKQOL4RnCvDpYbk88mreavmtXClzEsTPVkmVkwRHP89vt-ktieIiRzTzIkuyKfUPO6ZPMfCZ7zxVqykgPxGwunYG-jJ4_230uGb2DBtiu_g0kTQ1DaEGzSbLR5VDKZn6CN7xF81p5s3DHTnGVUInbpU83uS2fSJmXzn0mvElP_DVDe2yyGQ09an-oOiFcKtbjk8PrSuiSsYmi1-D0BTRQe1NaK_upGcglfx6zrstaR0XNBmDhkz3vGPW7Ft4bSCGeGgGvlQuz4Xb5svjmr17GQPW331Y6maUOJqPYAJMESR_6I5lKKvi3fYVvrjpjU6jHwbc4wH5OSPGYdfwSg-t7z34rw0dVLbpWhCCmHfgC8j_DzEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فؤاد ایزدی: هرگونه کمک، ترامپ را برای تشدید محاصره ایران گستاخ‌تر می‌کند
کارشناس مسائل آمریکا:
🔹
ایجاد مسیر خروج یا ساخت پل طلایی برای ترامپ تفکری کاملاً اشتباه است؛ چرا که تلاش برای کمک به طرف مقابل جهت خروج از بحران، تنها به گستاخی بیشتر و محاصره افزون‌تر ایران منجر می‌شود.
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/yRIXrUwC5Xc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691779" target="_blank">📅 20:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a49f5f07b.mp4?token=EF7sR5m9_WKwrWSdB9vFL-UvrMuDGe7CGwsAim-O5TbK1DVrU5XxymqnZ1sfseQ01ZwU7BLvkAZBVe395b-DFnalODM7uxfuH9WCP0OJl69PabRiy0NYtLuYAxEdHHsbt_0weJHdQcckKDwTYCxFd67194egrcbs0CC83D7rf-vnRCySbH-7m_CNg4IW3jx4i2g-xO_herLq0GrjCHkemHC64OjiHMZ7_n35DUjgI6bmf6hDliHnGydZjxFTe2xIaZE2-kdP1Qm1-YOmSKnCbOBYiEXN3oYkXopXsExgvYzR1tEfHaXtefCNxea1NlQ44Fi-GCupY2k2q4ATMq_ttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a49f5f07b.mp4?token=EF7sR5m9_WKwrWSdB9vFL-UvrMuDGe7CGwsAim-O5TbK1DVrU5XxymqnZ1sfseQ01ZwU7BLvkAZBVe395b-DFnalODM7uxfuH9WCP0OJl69PabRiy0NYtLuYAxEdHHsbt_0weJHdQcckKDwTYCxFd67194egrcbs0CC83D7rf-vnRCySbH-7m_CNg4IW3jx4i2g-xO_herLq0GrjCHkemHC64OjiHMZ7_n35DUjgI6bmf6hDliHnGydZjxFTe2xIaZE2-kdP1Qm1-YOmSKnCbOBYiEXN3oYkXopXsExgvYzR1tEfHaXtefCNxea1NlQ44Fi-GCupY2k2q4ATMq_ttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری خیره‌کننده از حرکت یخ‌شکن هسته‌ای در قطب شمال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/691778" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مشاور عالی و جانشین وزیر بهداشت: مشکلات تامین دارو درپی توقف پرواز مستقیم بین ایران و هند تشدید شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691777" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc4b1140c.mp4?token=stu7E3uJcZZRU8Uc0gC332Bx-xDirsyj6RY5hmL2JiGks9CSzROc_zJqkyYE7HzZ6mZM7qrzPojd12KhZCp3YaFU_NaUo1S2i4GuXs4uXhFhJ2k976BpeASPgTTbjMxuH9rbJbI-Pn0fPrmPepYlJQ64d6en52Dw9vhltlGndmGIPI8wqVM8DNr8WWBhqjAEUeRFP23GCsurMESWV2ghVDCdb0T8z4Y6sbY-Ud8-fPprggmdruZEflFOlOIRasGisIQtDKa68-m-P204emlo-90OVo4A88PDGc6iwKZ-Wgay2IUllcYxJiwzwE0fge1lKzvD6QK68lLzsAI1UFwSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc4b1140c.mp4?token=stu7E3uJcZZRU8Uc0gC332Bx-xDirsyj6RY5hmL2JiGks9CSzROc_zJqkyYE7HzZ6mZM7qrzPojd12KhZCp3YaFU_NaUo1S2i4GuXs4uXhFhJ2k976BpeASPgTTbjMxuH9rbJbI-Pn0fPrmPepYlJQ64d6en52Dw9vhltlGndmGIPI8wqVM8DNr8WWBhqjAEUeRFP23GCsurMESWV2ghVDCdb0T8z4Y6sbY-Ud8-fPprggmdruZEflFOlOIRasGisIQtDKa68-m-P204emlo-90OVo4A88PDGc6iwKZ-Wgay2IUllcYxJiwzwE0fge1lKzvD6QK68lLzsAI1UFwSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای محکومیت بهاره رهنما به ۸۰ ضربه شلاق به خاطر شکایت سیروان خسروی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/691774" target="_blank">📅 20:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHH6C9YOwpUkfjCKn2RgTcUgS1JsXp_ne5EjZx_GSnlMv_PdnrRV_Fzzc0EXpCY-N72S_PSVbLw0MmDKectN3pvJt9IA-sKJVVV7cu93OJEO39c3RVmTVobw5v04rjBWOzeY3-vwzT7_K1fx1UmWZgiQbrR2-mBcNng6L7ZhoNvOI2DRqJT_0YMcNTsXZXzihq2Seoqu4Ky6RP32itPBKhvEaxqAhSAM9pSvRV2Lx-vTsGNRBq7ICfjHYqXwxTCaoM0Mj2agsLA8GojTOdTPrP5an6EAWsCFZLoBmh0SPxa67vBlhgld0z6YQSDzXV0m8IbH6lGhnpso2AP43tOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اینفو_تیتر
|بازدهی یکساله شرکت های فولادی، از ۱۶۹ تا بیش از ۵۷۰ درصد!
@Titretejarat</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691773" target="_blank">📅 20:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">17-1 Ane Manaee (1404-02-02)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
ساختار اعجازآمیز سوره مبارکه "محمد" در تبیین دوگانه‌ها از قله حق تا ورطه باطل [01:06]
🔹
"خوش نیامدن از حق"، همان تبعیت ناخواسته از باطل است و آغاز ضلالت [09:54]
🔹
تماثیل قرآنی در توصیف تبعات سبک زندگی حیوانی و زندگی الهی [15:08]
🔹
فروپاشی طواغیت تاریخ و قدرت‌های پوشالی امروز براساس سنت‌های الهی [19:03]
🔹
در تقابل "تبعیت از حق" و "دنباله‌روی از هوای نفس"، معیارِ شناخت، قرآن است [21:32]
🔹
بیان قرآن در تفاوت بهشتیان و دوزخیان.. و توصیف بهشتی که پاداش متقین و تابعین از حق است [28:10]
🔹
مقایسه علم الهی که موجب تعالی وجودیست با دانش ظاهری و دانسته‌های سطحی [38:00]
🔹
درک واقعی از دین و حقیقت، یعنی قدرت تمایز میان هوی و هدی! [43:33]
🔹
روایت هشداردهنده؛ تحولات فکری از پایبندی به اصول انقلابی تا انحطاطات اخلاقی و تایید همجنس‌گرایی [48:57]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691772" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691771">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGh3FB_xEH1nXJywU27xe9GSpUoFi-zxiQidIn7DhbF_u1H7VUQ8NqlpYxaPNK3owo1KUP2vDbpbtUzUbjIl7KX06diF9UPNDu1M-rKFDaaL2_i_WNAM2wWZUsiSXOTPKzb6fdBkU8COQMSuuKc5FK4m58SFqijMBBwUuSvpHIE1PI4qCwE6UjWFuJLyT71sSfyDT7AsjknpKtTApqILoUjKEf2YwfsfeFuPvpLuye4ELe8qyPno59q9i51VNyXm45UBDT3ZlHJQiuQRJ7cOjOyjp6V2vyw1MOSTlGKvV0pHnrZ46HxUWrXeSXnqX6W8qwKye1x_LgLU9Y3eV_zeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیروس ابراهیم زاده درگذشت
🔹
«سیروس ابراهیم زاده» بازیگر پیشکسوت سینما و تئاتر پس از تحمل یک دوره بیماری دور از وطن درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/691771" target="_blank">📅 20:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691770">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7df9eb7ef.mp4?token=onhyBcCaVxwlitAHdsVlK8VRRty8V6VQiIRkr0QPA4AT8cUhkeRNDBoPrUm9LntdvikxIyNfLJFLWkBUmZ6s712vkxQyYga0mkek1681dPj6syEYlOg0mN8W3MBVuSVJg8RBhqiSK-86PcJh1_dqS3c3VnSo1yDavV0sYarDnkACVTga5rksAyK3vBojE7BY_D4z1uugx0SW8FI5LFuxB0239RH_7B1SduK092amcrmk1Sx6I1x0k_u0BGlSahRqV5N1-tJm9lIAzMPlFdmx-o09bFwjzXiYIZ-WOXKLY3rt--GhykBVjro93e4VnqpGQideMDXrmluVpWSKdpPdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7df9eb7ef.mp4?token=onhyBcCaVxwlitAHdsVlK8VRRty8V6VQiIRkr0QPA4AT8cUhkeRNDBoPrUm9LntdvikxIyNfLJFLWkBUmZ6s712vkxQyYga0mkek1681dPj6syEYlOg0mN8W3MBVuSVJg8RBhqiSK-86PcJh1_dqS3c3VnSo1yDavV0sYarDnkACVTga5rksAyK3vBojE7BY_D4z1uugx0SW8FI5LFuxB0239RH_7B1SduK092amcrmk1Sx6I1x0k_u0BGlSahRqV5N1-tJm9lIAzMPlFdmx-o09bFwjzXiYIZ-WOXKLY3rt--GhykBVjro93e4VnqpGQideMDXrmluVpWSKdpPdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای ساده برای تمیز و براق کردن ماشینت
🚗
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691770" target="_blank">📅 20:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691769">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آمریکا از صدور ویزا برای گروه رسانه‌ای همراه مسعود پزشکیان در سفر به نیویورک خودداری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/691769" target="_blank">📅 20:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691768">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7cb34dd6.mp4?token=k50WGqZwNKU5gVukO9OuoTNxSx4NY_dLyJeqs2_QAuNk2QOQ5Et5muiyRg9KSRlgSv_FHyKsgwmvKX2_3o9u3ELqke6VdpMKrK6b6plXovAWfOLohejhe5C_dGthIW8qUQZBy3mU7bmrM6HO2d275AFfdF3jPfpVSQ5wpVETilmxkgyMILkDV1UO76Ruml0cJxbT-AgbMf2wFTTHTOAhM8f4QR1pfQbs6oYbMXX4l5WdmdT-mb662LKTHZNLX_s9GevJ22oCTrQCa-fuBkThpn3VwM0Kn1qUjFeyiYLd4hutw3Tu_tqphjMueSTecoZc3_sWYU352Emj08QKM2h5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7cb34dd6.mp4?token=k50WGqZwNKU5gVukO9OuoTNxSx4NY_dLyJeqs2_QAuNk2QOQ5Et5muiyRg9KSRlgSv_FHyKsgwmvKX2_3o9u3ELqke6VdpMKrK6b6plXovAWfOLohejhe5C_dGthIW8qUQZBy3mU7bmrM6HO2d275AFfdF3jPfpVSQ5wpVETilmxkgyMILkDV1UO76Ruml0cJxbT-AgbMf2wFTTHTOAhM8f4QR1pfQbs6oYbMXX4l5WdmdT-mb662LKTHZNLX_s9GevJ22oCTrQCa-fuBkThpn3VwM0Kn1qUjFeyiYLd4hutw3Tu_tqphjMueSTecoZc3_sWYU352Emj08QKM2h5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚛
اگه درآمدت به ماشینت بستگی داره، این فرصت رو از دست نده!
🔥
فروش عادی و فوری نقدی  زامیادEX تک‌سوز و دوگانه‌سوز مدل ۱۴۰۵
✅
یک انتخاب اقتصادی با سوخت دوگانه
✅
خودرویی که هنوز هم یکی از پرکاربردترین انتخاب‌ها برای:
✅
باربری شهری و بین شهری
✅
پخش کالا
✅
حمل مصالح
✅
کسب‌وکارهای میدانی
و... محسوب می‌شود.
📌
طرح فروش:
📌
مدل ۱۴۰۵
📌
رنگ خاکستری
📌
زمان تحویل طرح عادی(نقدی):هفته چهارم دی‌ماه ۱۴۰۵
📌
زمان تحویل طرح فوری (نقدی): ۳۰ روز پس از پذیرش
⏰
شروع ثبت‌نام: سه‌شنبه ۳۱ شهریور ۱۴۰۵ - از ساعت ۱۰ صبح
⚠️
ثبت‌نام فقط از طریق
سایت فروش محصولات گروه سایپا:
https://saipa.iranecar.com
اگر در حوزه
باربری، پخش کالا یا حمل‌ونقل
فعالیت دارید، ما را در دنبال کنید:
🌐
www.zamyad.ir
📲
t.me/zamyadir
📲
instagram.com/zamyad.ir</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691768" target="_blank">📅 20:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691767">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niOv9nhW1WxkCa6NQbf8kXeOuz4EZ_VZ_dKEqxpLcFboJJ9_gfaGVXAOceXZ7Nfnt57THeh27PDNNT-S-cgvrqpchYRIbrIKStcowjwzKN9Z4DS-bBJ6_j8zjAt9lPDuyWfzBwKpn4yZwkhzE6b66GKCUGeJUmji9-NIVAPngLrn8OnIf4b64JzxDU33pG_aWPNekEOgOFj3E-jW7utfwT-U0_Nah8jiAyofRMLQfjoP57hE8GoiiwUnBPmdghXQGyMLG2xgmZnzARztggKqTn431XJ5yaHMU8NNGdANJdhG3UwzyPPGLa_QiFCiC3sMb_AZ2q65LVY4xiksjq3Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه‌های تلویزیونی بزرگ ABC، CBS، Fox News و NBC توافق کردند، پوشش جمعی خود از در برنامه‌های ترامپ را متوقف کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691767" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691766">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054bdb2c4.mp4?token=lg52Xvr_JV-kbmecfvio5lXNlLfnpVdvAC9YzDbSqav7ygk2JLfFZ2nTVYzW6lARG8msawzR1R0CBZezwTgmeYLR72_D8djlegT4moHDRLsDPcmpaXtp0mj51XOzSKN0VQPbj4VdVbcEt3w8WyuHPDc8caaHcDcKkVYfmbwr58OdJgacsXAAbtz7AGV_G5viQ3h43u7AodtmgMQx7HTYPOM2ksnRQ9IDTldza3QeFcRHOEqC-nCUIrfYwVTdwJWDXR_Dw6vSqunPEbJp1Ww0H93v26B7xwi-9J9ynWN5xRAy60iEGxG0sfbAvd_8B-O2f4XligVggokElKIGSk0t-Sp32U-GJOme7JxJBQjxn0jcWvKm2PPRq8b5YXfgS1e5fEqTZ0nKWK-Mg6mFvGCPrQvhPYsEJLUIVM-zTt57k7dnrmigt51av5VaARw9XdnZItW-OyZHzubk6zdPysROGHhQdLYhdHiblGFdqqD2k8SwkkXdS4jbK5jdXX275kYpaQ3o7ImvjUJesmvEZ2-_WRtxsjfg2WfxiSbj0VKMmYwiDuHBgDpocSH77pL4AFtH6C_p5ylxV-iQMlNbX43IWWetwN1MbJUa8usDVJDdv-h84r7dbjyGgxBqlt7RXVWK3nHEvBM0ZURawa-p3QPjL3v5AajLz4DW0CksdfT2It8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054bdb2c4.mp4?token=lg52Xvr_JV-kbmecfvio5lXNlLfnpVdvAC9YzDbSqav7ygk2JLfFZ2nTVYzW6lARG8msawzR1R0CBZezwTgmeYLR72_D8djlegT4moHDRLsDPcmpaXtp0mj51XOzSKN0VQPbj4VdVbcEt3w8WyuHPDc8caaHcDcKkVYfmbwr58OdJgacsXAAbtz7AGV_G5viQ3h43u7AodtmgMQx7HTYPOM2ksnRQ9IDTldza3QeFcRHOEqC-nCUIrfYwVTdwJWDXR_Dw6vSqunPEbJp1Ww0H93v26B7xwi-9J9ynWN5xRAy60iEGxG0sfbAvd_8B-O2f4XligVggokElKIGSk0t-Sp32U-GJOme7JxJBQjxn0jcWvKm2PPRq8b5YXfgS1e5fEqTZ0nKWK-Mg6mFvGCPrQvhPYsEJLUIVM-zTt57k7dnrmigt51av5VaARw9XdnZItW-OyZHzubk6zdPysROGHhQdLYhdHiblGFdqqD2k8SwkkXdS4jbK5jdXX275kYpaQ3o7ImvjUJesmvEZ2-_WRtxsjfg2WfxiSbj0VKMmYwiDuHBgDpocSH77pL4AFtH6C_p5ylxV-iQMlNbX43IWWetwN1MbJUa8usDVJDdv-h84r7dbjyGgxBqlt7RXVWK3nHEvBM0ZURawa-p3QPjL3v5AajLz4DW0CksdfT2It8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از پیرزنی که با واکر خودش را به رژه جانفدا رساند تا مردی که با خالکوبی اصرار به اعزام به جنوب برای مبارزه با آمریکا داشت
🔹
دو روایت جالب سخنگوی جانفدا از تنوع و تکثر مردم ایران برای دفاع از میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/691766" target="_blank">📅 19:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691765">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24930f261.mp4?token=pIniFqm0EQTVe8xqDc4oDPg-DlMjBRd0qbRAkL1hkdAorDMZEheo-kLLHvOkqbZJS-vkqx5NgHxnSq84I5jpQhHRKEOob3K-bnHu1gDK9PCIqjzRG-toCdBp-VyzYEiLejhdCquIEAOV9CLArmQ27Ozy7EpXtQtVZtX9hN7g0KJYSuCiQDVdEN-ij_FQDp5HyyyzWC49MRI-OTHFaFWIXruAaHHNpVsnBWalBiG3x8QrnACAL0KRtgeJCPn2AvhWphvMSKpKl1_p4EcYS007wvvR4xhkOXeCqzRfRK-CrA4tIjGq6_C5dzTQXQVqSsMpaRUVMqzujwmNw0ojs7umig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24930f261.mp4?token=pIniFqm0EQTVe8xqDc4oDPg-DlMjBRd0qbRAkL1hkdAorDMZEheo-kLLHvOkqbZJS-vkqx5NgHxnSq84I5jpQhHRKEOob3K-bnHu1gDK9PCIqjzRG-toCdBp-VyzYEiLejhdCquIEAOV9CLArmQ27Ozy7EpXtQtVZtX9hN7g0KJYSuCiQDVdEN-ij_FQDp5HyyyzWC49MRI-OTHFaFWIXruAaHHNpVsnBWalBiG3x8QrnACAL0KRtgeJCPn2AvhWphvMSKpKl1_p4EcYS007wvvR4xhkOXeCqzRfRK-CrA4tIjGq6_C5dzTQXQVqSsMpaRUVMqzujwmNw0ojs7umig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنگام کار در اطراف دستگاه‌های سنگین، فاصله ایمن را رعایت کنید؛ یک لحظه بی‌احتیاطی می‌تواند جان افراد را به خطر بیندازد
⚠️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691765" target="_blank">📅 19:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691764">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین دلیل شما برای ترجیح «طلای فیزیکی» به صندوق‌ها و پلتفرم‌های آنلاین طلا چیست؟</h4>
<ul>
<li>✓ عدم اعتماد به سامانه‌ها</li>
<li>✓ احساس امنیت و مالکیت</li>
<li>✓ عدم آشنایی با فرآیند</li>
<li>✓ کارمزد و هزینه‌های پنهان</li>
<li>✓ از پلتفرم‌ها استفاده می‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/691764" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691763">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fc1181d5.mp4?token=WpuysjGG_hLJZqsFqu0Ne2fy8XSvPP0GlcXdJUZA4ULM8AU4broCn-3UYvPn8mKkQ93XU9jflgWR3PE3cxLx5GirMBzvxgjpAyjItJYl7Ym81rswfcL22wGvQow3PlYSxmfy--GYmlTwvcavEWANDIadXKc1Q0NnCUuY38E6E1Cn4VTOwNXfDImYcb4y70C76Chi915RpxQVIN6gIFF0jZGN_FTIpUhH1mpi2X5t_871xYxYupa_W8r3N6w58StTYBI3BmxUAybaL2ixaQcLV4tETGyDudDYWrZsuZIy7ZAWaqML6NyeG_hLU6V6eCoNJZ8vqMQtgXwG8MLt35inCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fc1181d5.mp4?token=WpuysjGG_hLJZqsFqu0Ne2fy8XSvPP0GlcXdJUZA4ULM8AU4broCn-3UYvPn8mKkQ93XU9jflgWR3PE3cxLx5GirMBzvxgjpAyjItJYl7Ym81rswfcL22wGvQow3PlYSxmfy--GYmlTwvcavEWANDIadXKc1Q0NnCUuY38E6E1Cn4VTOwNXfDImYcb4y70C76Chi915RpxQVIN6gIFF0jZGN_FTIpUhH1mpi2X5t_871xYxYupa_W8r3N6w58StTYBI3BmxUAybaL2ixaQcLV4tETGyDudDYWrZsuZIy7ZAWaqML6NyeG_hLU6V6eCoNJZ8vqMQtgXwG8MLt35inCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به معاون ترامپ: تا کی قرار است آمریکایی‌ها این قیمت‌ های بالا برای سوخت را بپردازند؟
ونس:
🔹
تا زمانی که ایران صلاح بداند. ایرانی‌ها عامل گرانی سوخت در آمریکا هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691763" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691762">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای رسانه بریتانیایی امواج در مورد جزئیات شروط هفتگانه ایران برای مذاکره با آمریکا
دست‌کم ۵ شرط از ۷ شرط در تفاهم‌نامه اسلام‌آباد هم مطرح شده بود:
🔹
آزادسازی دارایی‌های بلوکه‌شده ایران
🔹
پایان جنگ در همه جبهه‌ها
🔹
عدم مداخله در امور داخلی ایران
🔹
توقف حملات به خاک ایران
🔹
رفع محاصره آمریکا علیه ایران
🔹
یک منبع سیاسی ارشد: این ابتکار جدید است و هیچ‌کدام مستقیماً هسته‌ای نیستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/691762" target="_blank">📅 19:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691761">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مصرف برق فیلترشکن‌ها ۷۸۹مگاوات است
مسائلی، دبیر سندیکای صنعت برق ایران:
🔹
در حالی که مزارع و شهرک‌های رسمی استخراج رمزارز نیز وجود دارند، بخش قابل‌توجهی از موارد کشف‌شده مربوط به فعالیت‌های غیرمجاز است.
🔹
بر اساس برآوردها، مصرف برق ماینرها حدود ۳هزار و ۷۵۰ مگاوات عنوان شده، رقمی که تقریباً معادل ۱/۵ برابر ظرفیت نیروگاه رامین اهواز است و همچنین فیلترشکن‌ها نیز روزانه ۷۸۹ مگاوات برق مصرف می‌کنند./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691761" target="_blank">📅 19:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691760">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
هشدار وزارت بهداشت درباره واکسن آنفلوآنزا   رئیس مرکز روابط عمومی وزارت بهداشت:
🔹
تاکنون واکسن آنفلوآنزای معتبری در شبکه رسمی سلامت توزیع نشده و از مردم میخواهیم به واکسن‌های خارج از شبکه رسمی اعتماد نکنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691760" target="_blank">📅 19:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691759">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e691b28e36.mp4?token=VNz9EZlkytS8xhHP48MOcaRm54esK_p1oMnggEud9la5F7m1d31bFWFsacykuy6Rrt0xiZQLnFcQFMdHKauRqOFqjv97k5y1h1v1JXwF0bnoEgQuu8np2RggBI05radkP9FRspnXERRzoVo6f-XwkG8A_xzIfaJU7dnmXmHcPeRRnX502PqFqdVOJB0zYI_jAeKLOHTqiF8QFGG89CXvO2EkuUXEE4-kx5V0z0dwdWIQ4acan1gA_dhLTqTmd7c4thXGFkVgES5-YyUtB_Gny1px8Yo_bH43ej_fppdi3oTfWWOzwfmx9yz2apR5-vOtqUZCbLdUKFlL_fSacThouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e691b28e36.mp4?token=VNz9EZlkytS8xhHP48MOcaRm54esK_p1oMnggEud9la5F7m1d31bFWFsacykuy6Rrt0xiZQLnFcQFMdHKauRqOFqjv97k5y1h1v1JXwF0bnoEgQuu8np2RggBI05radkP9FRspnXERRzoVo6f-XwkG8A_xzIfaJU7dnmXmHcPeRRnX502PqFqdVOJB0zYI_jAeKLOHTqiF8QFGG89CXvO2EkuUXEE4-kx5V0z0dwdWIQ4acan1gA_dhLTqTmd7c4thXGFkVgES5-YyUtB_Gny1px8Yo_bH43ej_fppdi3oTfWWOzwfmx9yz2apR5-vOtqUZCbLdUKFlL_fSacThouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در اعماق حلقه‌های زحل، قمر کوچکی به نام پن (Pan) قرار دارد؛ قمری چوپان که به‌خاطر برآمدگی عجیب استوایی و ظاهر شبیه بشقاب‌پرنده‌اش مشهور است
🪐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691759" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691758">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr0k222hJNktCY3r2OtX9BAEVIjpiL3xc4umYTkQleSxBI5hHpRE-4YxcxeXUxbr-WyPTjyaiH8aYN9f1UiCYlq769eBdIXfAC9TlZpj4Z2ULmtHg_TE_RK0xYfMmrfuWGgvGSzoduAByeuw9wp3M0uZHYQydiYq47oLDrERB3_eAC8jsi3yVVGIqu0CiH09QwaBelu1wcr-vcTvK8hbRCfZYfoennyE8CTqN_fK1jDEPeqn2NbFVH3By0-l9_mJYlb2D051wTIxZt9WlNbKc_YUo40ZxjxcORpr05V7NHRHtBpx65rs4k0fuqKIucUcNZZpW9Sw_6pM9qKeBn3-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه فرانسه: ما تصمیم مقامات ایران برای تعطیلی مرکز زبان وابسته به خود در تهران را محکوم می‌کنیم
🔹
سفیر ایران را احضار خواهیم کرد و اقدامات مقتضی را اتخاذ می‌کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691758" target="_blank">📅 19:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691757">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای مضحکانه نخست وزیر قطر: ایران صلح طلب نیست!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/691757" target="_blank">📅 19:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691756">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df374921dc.mp4?token=XSIK3JNBQqO-ZJzIoVfefL6yqeIbuyUDdUv-4X_z0BM7CQCrHQMTZ0cg4xkM5LAf8a2i-LFSoH4m5Vrd6aDs8DsfgLnvTgEiSPtFKDYbZ2Ao_YXf2hmXin99mXn273ljVuabjBlTy98wpPY2Lr9YU0r2wxucLRL5SpRVwOd4-RB3J6ACRIGYwtew3FNz9-QlBZpwlguHmClPSlH2PM6DSagUg7MyDVnI2jy9C7p6fypBy260WAJkahPV3OdWJLXSLxY4-GXQV8BAJ2Ms1b3UBttMjP1hMxern_Ko07qRtkIJXOnRMnzRswdKXVJAqvdpbVPJ-WSrWuGW1J7g2KHHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df374921dc.mp4?token=XSIK3JNBQqO-ZJzIoVfefL6yqeIbuyUDdUv-4X_z0BM7CQCrHQMTZ0cg4xkM5LAf8a2i-LFSoH4m5Vrd6aDs8DsfgLnvTgEiSPtFKDYbZ2Ao_YXf2hmXin99mXn273ljVuabjBlTy98wpPY2Lr9YU0r2wxucLRL5SpRVwOd4-RB3J6ACRIGYwtew3FNz9-QlBZpwlguHmClPSlH2PM6DSagUg7MyDVnI2jy9C7p6fypBy260WAJkahPV3OdWJLXSLxY4-GXQV8BAJ2Ms1b3UBttMjP1hMxern_Ko07qRtkIJXOnRMnzRswdKXVJAqvdpbVPJ-WSrWuGW1J7g2KHHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند بامزه گربه پالاس برای گرم نگه داشتن پنجه‌ها در سرمای شدید
🐈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691756" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np6dGwePE9kbXDVeOb2HgcYkKdh3sDl0T-vhgI8T_g8EPaQklpwAewfLpKN7MiGab6qP6May93wl4LieCwmaXt2Jr1In0fCnHBQ5ErEcwm9YA9UU8oPCAAfwZLDMS8KLTXAjPZGqZxLiIizmiHyaFmuhHTzHsySOne4T84l23sZsY960gTrN23r9TQ9aFJFmxpe-Tu7fa9OWxkjF0q_EqaD2KZSdwEUgm_6rEL-XP8K6cPHwyuUZfD02o5Rbl5vX4zIvDl73B9oR9gs0ErSyJi9DH1Ugu6fm6pmeXxWbGCytA4zUM3lJoq31koHFIO3VHnYcXrEtAxjHZa3BNMctlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpN0K156AKa1L_kknZY0iKh8udTthOODNIcjFb6vIR61P9VPqmgfg0C0fvEHHT0AgD8OBqpCe_BAwznyAh1WaogcLdSn0ml35yBfrEbHhSQV7_Iz02HakEU3sPxTdD2i7AAAta0o8g0oYqKLTyw2F1rpyRU2b9TkjtaCuA6eh-CZTJrP1Lg3CHakpFLEXOhlVPd18ccwKpT7ZFjO_WbuVAca1EyV7Z71IqUT-wAqQXG-Vezi44Ccug9fRnmQ1PckfXK9zWyHESsgb-7SGLBtdAAxdhxHfyo1yD8U2UpcmOoAoKHdE2V5OdxgnWd6gGVbkxRQ_sX6b-P2kaQIWr3X_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گلایه شهروندان از نبود شبکه فاضلاب شهری و خطرات چاه روباز در کرج
🔹
باسلام، حدود ۲۵ سال است ساکن کرج، انتهای گلزار غربی، خیابان چمران، خیابان قائم، کوچه محمد هستیم و متأسفانه همچنان از شبکه فاضلاب شهری محرومیم. با وجود بیش از ۵ سال پیگیری مداوم، پاسخ مسئولان این است که فعلاً پیمانکار نداریم. در حال حاضر فاضلاب در چاهی ریخته می‌شود که دهانه حدوداً ۵ متری آن باز است و هر لحظه خطر سقوط اطفال وجود دارد؛ ضمن اینکه این وضعیت باعث تجمع انواع موش و حشرات موذی شده و مشکلات بهداشتی جدی ایجاد کرده است.
(محمد شاهی)
📍
استان البرز، شهرستان کرج
🔸
ما در  الو فوری همراه و صدای شما هستیم؛ چالش‌ها و مشکلات محله‌تان را با ما در میان بگذارید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/691754" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e9f43c61.mp4?token=U12PRbcyJEoQZHVem2q1RCg342jt0q7j7Us2XFQXYwhqIKYzxQChzdPQRQzh9TQx9i1qVoEj4C6-tQi2lwU-czpnznefnHQBZm4EK413tsf7GmrpscfrjnurHyeZXfuGUOedMoKoJUnIqCe9fWhwP9crSHISqMFfk9BM6NzSdRs1go7AyxJcMFX3-WrOhKN-JBiMJUZE4ZE1X3fxaItD_I7OP94b15_u43mpyvdm3cS2RbrJSdFj5TU9E-_d8KJKJw7s5gGPbsYmfuRkH0iSe2Oho8S1yNJwJToauCu-2U2yOl0GA4rFboWgo4xo7wPubnUX053ArWEmCg8Mnw104A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e9f43c61.mp4?token=U12PRbcyJEoQZHVem2q1RCg342jt0q7j7Us2XFQXYwhqIKYzxQChzdPQRQzh9TQx9i1qVoEj4C6-tQi2lwU-czpnznefnHQBZm4EK413tsf7GmrpscfrjnurHyeZXfuGUOedMoKoJUnIqCe9fWhwP9crSHISqMFfk9BM6NzSdRs1go7AyxJcMFX3-WrOhKN-JBiMJUZE4ZE1X3fxaItD_I7OP94b15_u43mpyvdm3cS2RbrJSdFj5TU9E-_d8KJKJw7s5gGPbsYmfuRkH0iSe2Oho8S1yNJwJToauCu-2U2yOl0GA4rFboWgo4xo7wPubnUX053ArWEmCg8Mnw104A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اراجیف معاون ترامپ درباره تنگه هرمز
جی‌دی ونس:
🔹
با وجود وحشت‌آفرینی روزانه ایرانی‌ها علیه کشتی‌ها، ما همچنان شاهد عبور حجم قابل توجهی از نفت و گاز، از تنگه هرمز هستیم.
🔹
این در حالی است که بر اساس گزارش منابع معتبر دریانوردی، تردد کشتی‌های حامل گاز در تنگه هرمز به شدت پایین آمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/691753" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0083ab04f.mp4?token=YWpVOdVH3fSDwkVPW_IO2yNahgFXPCzkWJ387PmrpVy6X6IrEFONzc4zXuuSv4ZqZ9SoDs79MJEx_PStnCqOqdizEB3mZV1PE2Z4Igm2PR4fzFSE4JCKKliBXf5us4oZT3TsDhuP15RYaSiSjdWwg6gRAsWnVMnexz3bSaauv5E58NTTTOkHYvlp_LDAuza0rwqoQxJ0YIaBBy8BZHrF7Kt5ux9NZlnC5nQDtzE9ppkyXeLDFQRtURT3IXBXw6nyumLHQOsmWUZhRVEHhtzYcN1etxl-xAYBfylB0LLkcEHkZBxPs94JXIzUSJqJ3Sq9pa-aVcgKTS2c6EY0iA420w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0083ab04f.mp4?token=YWpVOdVH3fSDwkVPW_IO2yNahgFXPCzkWJ387PmrpVy6X6IrEFONzc4zXuuSv4ZqZ9SoDs79MJEx_PStnCqOqdizEB3mZV1PE2Z4Igm2PR4fzFSE4JCKKliBXf5us4oZT3TsDhuP15RYaSiSjdWwg6gRAsWnVMnexz3bSaauv5E58NTTTOkHYvlp_LDAuza0rwqoQxJ0YIaBBy8BZHrF7Kt5ux9NZlnC5nQDtzE9ppkyXeLDFQRtURT3IXBXw6nyumLHQOsmWUZhRVEHhtzYcN1etxl-xAYBfylB0LLkcEHkZBxPs94JXIzUSJqJ3Sq9pa-aVcgKTS2c6EY0iA420w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کندر را بهتر بشناسید؛ از خواص این صمغ قدیمی چه می‌دانیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/691752" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmtEWdRrmQXbX4HH2QUqwdkXo8h11DnjcU5PgEI-aGDuUboEZzDRvQL93ICZ5prng8qMF1zDOB6VJ79RMZOEnU7_tHZT9EKochXXpY0NGP9w-yDgGeao3MrmJwU6G6tyEw0a67ISKxkzBo3yh8X9J97xrduIeGDBGnxGFlcxK165L1D-tZUGdwouKQFRG2izTAXFEAMgb2vncmIhlkSTik1Y_90yYqP0UHi19xEealOQZGoYsWn-7OUDXiZfWrJ_awNmiCuAxKcKb-0r0upu9L0ROcLwga6gnPE9I_9eVkrtcxaCvVWGs1HM08aKRqRqUt4BBoc_kvKS0z4F4LPxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به مطلب نشریه اسرائیل هیوم؛ وقت آن رسیده که واشنگتن خود را از این غل و زنجیر رها کند
🔹
لابی اسرائیل دیگر ابایی ندارد از اینکه نقش و نفوذ خود را در سیاست آمریکا در قبال ایران آشکار کند. در نشریه متعلق به میریام ادلسون، که بلندگوی این لابی است، صراحتاً  گفته شده سیاست آمریکا باید به‌گونه‌ای باشد که در قبال هرگونه بی‌احترامی یا تعرض به اسرائیل، آمریکا نیز هزینه‌ای بپردازد!
🔹
وقت آن رسیده که واشنگتن خود را از این غل و زنجیر رها کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/691751" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691750">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عربستان به دنبال حذف ایران از جام ملت‌ها
🔹
گفته می‌شود برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانه جام ملت‌های آسیا تعلیق کنند. این یعنی احتمال حذف تیم ملی از جام ملت‌های آسیا وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/691750" target="_blank">📅 18:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691749">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
هواپیمایی جمهوری اسلامی اعلام کرد پروازهای تهران، مشهد و اصفهان به مقصد فرودگاه نجف طبق برنامه پروازی در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/691749" target="_blank">📅 18:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCUlxHUuI-DTuytNMWejMyHe5UbOr8a_RbpioT6uXwZt6ciALL6lN3Jtgro2EPpkfNl2PulI_PqbFHqEF9RRzs9OriZsD7S45R-tbXOUyQ9z0eVKiD-5AaW6dG8wUAn8qOdLBaoey-lEIfYqS1fObuILdeg0CVm4na5nYSBKz-z6UFqk35aZ1F82xxjjxV9XU47fYYIs6FHZD7D-fuqq1WyEZ6Cn4cjbmNp3bUxd7xyPZc2ewvwVEt1rBJ-Q1Hgwnx0dtN9z7MMs2aqv5A38Wqqq_2JzsGwUVO9ps-lssfp9kwPnr7Gw33OCjgfp4YKRT4fiYNpP3vbgSlZVMGHyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت جدید برای کاربران | خرید طلا و نقره با کارمزد صفر میسر شد!
🔹
به تازگی متوجه شده‌ایم کارمزد خرید طلا و نقره در وال‌گلد برای مدتی محدود صفر شده. کاربران برای خرید این فلزات گران‌بها دیگر هزینه‌ای بابت کارمزد پرداخت نمی‌کنند.
🔹
به این ترتیب، هزینه کارمزد از فرآیند خرید حذف شده و مبلغ پرداختی کاربر مستقیماً صرف خرید طلا یا نقره می‌شود؛ تغییری که می‌تواند برای خریداران این بازار قابل توجه باشد.
🔹
بررسی‌ها همچنین نشان می‌دهد وال‌گلد به‌تازگی همکاری خود را با بانک کارآفرین آغاز کرده است؛ همکاری‌ای که در کنار صفر شدن کارمزد خرید، این پلتفرم را به گزینه‌ای قابل توجه برای افرادی تبدیل می‌کند که به دنبال سرمایه گذاری در یک پلتفرم امن هستند.
خرید بدون کارمزد طلا و نقره!
خرید بدون کارمزد طلا و نقره!</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/691748" target="_blank">📅 18:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
رهبر انصارالله: تمام تلاش رژیم سعودی در این برهه، وارد‌کردن ترکیه و پاکستان به جنگ و آوردن تکفیری‌ها از سوريه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/691746" target="_blank">📅 18:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: رژیم سعودی، فرودگاه‌ها و پایگاه‌های خود را برای پرواز هواپیماهای جاسوسی اسرائیل به سمت خاک یمن در اختیار صهیونیست‌ها قرار داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/691745" target="_blank">📅 18:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
فایننشال تایمز: آمریکا و چین بر سر تمدید آتش‌بس تجاری به توافق نرسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/691744" target="_blank">📅 18:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cucza4pX6RVosXAQVlbaoZ9PHYN4j9OF1UniAVR4-deO0J0DKgjc5by8BwATPxeVcS0PUm2tqQuSXkbEuz_7Puh-GRzQPzsYc1wtV3G14hAV9Vt-PJI53vT0YGdff7EVUNIi2xrZ2oZ8DOOy_9fLbQJNuw7nNu-Bpt5PaE9_uxRNBvhRWbKblZSFVOHUOM82vqsE3JfStA-Ak_4xDEB9uqmHn-psn-dupx4xA_WWPZP6unbOWUh-ICp5PQ1Dihsp8tJ2u8pmrxzd3P87hpO0Ha-QBw1PscAf7YUx104XfmikdU_rAumRrAqobmdWBPw028c9NREQuzCcSLapf9RgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوتمیل تیرامیسو؛ یک عصرانه یا صبحانه متفاوت و خیلی خوشمزه
😋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/691743" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf82d6f38c.mp4?token=b8KsLFDspjqUDEi1AST7E8eAU8lZKFOSmVYFU-A7CL1j9aAtkoX67VzmWW9Ykl8mhERlF8CTZSI0oM5roeXmwWXRFhYEQ4c82760EZJc8UH6pP9qEbCpsaSU_YgcPI9_RU__NKfGJqDj0cTSuSOaoN1sny3-IFkZ_vg1xiJMr1J8wS6KCcJ_D3bnR9O8QPp_ktkVmUiPConpBXJk4kInDoIu_8xwSG5rbTW6LylAHP7-kmHDJGprIckkKAkCyvl0Dj_83d4iu39xEfS6HFb8Sk9ADyaI5fY-1D5bdauAyb33Peipz6IfP0oqX2Cb8WX8LzgU0XzG9IskVrWAfw4kpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf82d6f38c.mp4?token=b8KsLFDspjqUDEi1AST7E8eAU8lZKFOSmVYFU-A7CL1j9aAtkoX67VzmWW9Ykl8mhERlF8CTZSI0oM5roeXmwWXRFhYEQ4c82760EZJc8UH6pP9qEbCpsaSU_YgcPI9_RU__NKfGJqDj0cTSuSOaoN1sny3-IFkZ_vg1xiJMr1J8wS6KCcJ_D3bnR9O8QPp_ktkVmUiPConpBXJk4kInDoIu_8xwSG5rbTW6LylAHP7-kmHDJGprIckkKAkCyvl0Dj_83d4iu39xEfS6HFb8Sk9ADyaI5fY-1D5bdauAyb33Peipz6IfP0oqX2Cb8WX8LzgU0XzG9IskVrWAfw4kpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله وحشیانه عربستان سعودی به یک بازار محلی در تعز یمن
🔹
«ضیف‌الله الشامی» عضو دفتر سیاسی انصارالله یمن اعلام کرد که هواپیماهای متجاوز سعودی، بازاری محلی را در بخش «ذوباب» استان تعز هدف حمله قرار داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/691741" target="_blank">📅 17:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: با چین درباره ایران مذاکرات پشت‌پرده داشته‌ایم؛ نمی‌توانم به شما بگویم این درگیری چه مدت ادامه خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/691740" target="_blank">📅 17:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
شهادت یک مامور فراجا در ایرانشهر
🔹
بنابر اعلام منابع آگاه، یکی از نیروهای جان‌برکف فراجا در حین ماموریت بر اثر حمله تروریستی در ایرانشهر به شهادت رسید.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/691739" target="_blank">📅 17:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان با چراغ سبز و مشارکت مستقیم آمریکا و صهیونیست‌ها، در یمن جنایت جنگی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/691737" target="_blank">📅 17:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhPRdICAH8ScH8BGhOQ0V4PhhebiedeIb1Gs1iB-3LX6F7vTvd-g6idCt29kGC7hS0aQw17VjbH5S273xJy-hfppfNr5oAtZsWiMPaIC3e0sWGqWfQyg0x-nuJ55DYAq3Njtb2xuz-IeJoSAUs2IEhxnH-BlqtS9aaOVA5etfqZE7DOJk7y4LAkeZ66BkncAvLa7h02p7J4O7yESO7_-YvP53jJLZpEFDOA9FfHVSoWi_oyEVLDNTM4Kv_WeWD-ZL20XALckuFPDYKk05AeNiPHCzKgOJx2OpN_Y14XPjMGcMnTaIotvts9_L7CWgZ1RiTZxvlJKn0-gJ7GFgfxFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های پنهان در «پا» که نباید نادیده بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/691736" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان با چراغ سبز و مشارکت مستقیم آمریکا و صهیونیست‌ها، در یمن جنایت جنگی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/691735" target="_blank">📅 17:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین دلیل شما برای ترجیح «طلای فیزیکی» به صندوق‌ها و پلتفرم‌های آنلاین طلا چیست؟</h4>
<ul>
<li>✓ عدم اعتماد به سامانه‌ها</li>
<li>✓ احساس امنیت و مالکیت</li>
<li>✓ عدم آشنایی با فرآیند</li>
<li>✓ کارمزد و هزینه‌های پنهان</li>
<li>✓ از پلتفرم‌ها استفاده می‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/691734" target="_blank">📅 17:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyHOaLNlWWurACaLW4aEqhXAqT_OnAnql3SObNwRy7FyUtFmHeCBVldiKQ8ehs_YVGbfqWG3m89Xo3pWIrC3hp7_jaTYp0ELVjOEP_Ial6ZGC2knfeAFBFNkn1AnwG4O8DE7-6sNYo0xrOCxm00tXzKH4XR2ReJguB2-8Bbl7qchjwVc7eElRk8yAcmi6Zp51z94837vBed7WoRxSEybdwRXTLBM0b5Wbp6SdGcawSHl_oQzNiMpaC8XO2CoDIW-ImpdvmoLy4xTYP_sMxD2Kwjx9r3rGY2v_ZpWrh0Ywgxug6V8fPmCmre28xKLRMmJtm89n7qTQU-gTgYYQrrzSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواشناسی: موج بارش‌های پاییزی از روز پنجشنبه وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/691733" target="_blank">📅 17:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2tl_C_U25tgIez29LGb8xdx1KcUi9HSfJEFneTROi6qiymuBHfSu_eyuK1WZuPZZ9gztZ8d7UKiBvtp75A-5AUHbNQimHVgjUT7GEKIF8Z_CHBLT8ec-l3dOvY-fDrobJW75rD20PIlo3bF4f2KhEmm_6J8ExaiAkZHJIap3xqWwXX-Ycu1O_V4rtbp9mkGY-unuVRMTPGWorQAsNgdNoeO1a6S1HlhfyzcWT2eaHwRmQ97UQbs2_WaqhnadSU--S6LLXij_Adbrc5hskLb3y4rQ-TRnOGz2r3eLUb6ZLjoSwN4l_nZch5boedoaS8khf7Vr7NbL8-mJBCESnHQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش قیمت نفت به ۳ درصد رسید
🔹
نفت برنت ۱۰۰ دلار
🔹
نفت آمریکا ۹۷ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/691732" target="_blank">📅 17:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شهادت یک مامور فراجا در ایرانشهر
🔹
بنابر اعلام منابع آگاه، یکی از نیروهای جان‌برکف فراجا در حین ماموریت بر اثر حمله تروریستی در ایرانشهر به شهادت رسید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/691731" target="_blank">📅 17:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a79612931.mp4?token=PTrZhKD8YvTbsyMpRfbnVWtpk63l_iKOig2NeceS6SeB3sqh69douRz46o2FqtZS3xW7iRgxi3SPOuKnXaZBZIPivNCzc_GQ9E4DYONAFfGMtP01xuU1a_vq7-N7ccGJezS_9a3cBUK1UegMrPa3jOImLtCH2DpA-8Z2udfbApK7JlCx7SV678ICNAnjRFidMeRuxZ8gJuCJyn-j6GaaG9QIlefkO6UbZlSaTEaPM2154D87SmC-Lzt7pSAuV1NL9ThcvhPyeUKB7a9jPUZKm7iz6X__uwqDnaQr3iEAneHDu6gRYfyMtGUE4Sxn5S3ABAAbeq-TR6thO9lsepskfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a79612931.mp4?token=PTrZhKD8YvTbsyMpRfbnVWtpk63l_iKOig2NeceS6SeB3sqh69douRz46o2FqtZS3xW7iRgxi3SPOuKnXaZBZIPivNCzc_GQ9E4DYONAFfGMtP01xuU1a_vq7-N7ccGJezS_9a3cBUK1UegMrPa3jOImLtCH2DpA-8Z2udfbApK7JlCx7SV678ICNAnjRFidMeRuxZ8gJuCJyn-j6GaaG9QIlefkO6UbZlSaTEaPM2154D87SmC-Lzt7pSAuV1NL9ThcvhPyeUKB7a9jPUZKm7iz6X__uwqDnaQr3iEAneHDu6gRYfyMtGUE4Sxn5S3ABAAbeq-TR6thO9lsepskfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691730" target="_blank">📅 17:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c109d1fe1f.mp4?token=e7FX9jsLt0MjyqaAmWdUOajXsAneJWXKUoiHgzCo6gyLAPqfcmtfj4KxDp2y0QE7cbRkNa8BpGOID4LLk9IppHxyLGtZfo1jK8Ui5KJKyCm9xIfi_YGgKnzaY2u039qWUfQFCjXxFwjfFbI-jrz8kSxyJnJ6TqOAOxq1RTHYvEZSDNetKZomCaZjDuXRCVpmjVumkr9cAcRWZd3MjfnakwtdQs3PYdry_nHVX-34nh1wqCfViWM5nxv_QJAELSLjCVjBg9VFKVeHTwkcusTubUK8AeY7x8dWtQUPGspXFd93cpdDt8xUZmHpf2fVFky92kGE3dz96BcUFVkEgnrHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c109d1fe1f.mp4?token=e7FX9jsLt0MjyqaAmWdUOajXsAneJWXKUoiHgzCo6gyLAPqfcmtfj4KxDp2y0QE7cbRkNa8BpGOID4LLk9IppHxyLGtZfo1jK8Ui5KJKyCm9xIfi_YGgKnzaY2u039qWUfQFCjXxFwjfFbI-jrz8kSxyJnJ6TqOAOxq1RTHYvEZSDNetKZomCaZjDuXRCVpmjVumkr9cAcRWZd3MjfnakwtdQs3PYdry_nHVX-34nh1wqCfViWM5nxv_QJAELSLjCVjBg9VFKVeHTwkcusTubUK8AeY7x8dWtQUPGspXFd93cpdDt8xUZmHpf2fVFky92kGE3dz96BcUFVkEgnrHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دستور انتشار اسناد موجودات فضایی را صادر کرد
🔹
در پی اظهارات جنجالی اخیر باراک اوباما درباره وجود موجودات فضایی، دونالد ترامپ به نهادهای فدرال دستور داده روند شناسایی و انتشار اسناد دولتی مرتبط با یوفوها و حیات فرازمینی را آغاز کنند.
🔹
ترامپ در این…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/691729" target="_blank">📅 16:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان فردا سه‌شنبه عازم نیویورک می‌شود
🔹
مدیرکل روابط عمومی دفتر رئیس‌جمهور از سفر فردا (سه‌شنبه) پزشکیان به منظور شرکت در مجمع عمومی سازمان ملل خبر داد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691728" target="_blank">📅 16:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691723">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17217aebf0.mp4?token=FMy_KoJl7uxgUU5EqHua5BMPjTI0sFPgfdZuMC1VHkisDar2aB5_wHyC0liKJm88FS_tHNgv6ePdFzze48zGSZyI4nFM6pUH4dYFLswLRa4wpXXDn1gGUeLcM18BgMqODPlclQgLN0Vcm2_2gInHdnlRNXJcS2cS4zrGwBbXtv0MCuZFCuKjLtElEJlYchWxbWMe-MKEiszrYh8Dib9_dvBJWcwiCqWdMQI2SVLmY8XVkP5e96_B3vjYCHP0WwrRvlBlAI_jg4QvWmCtNOxG1e3rk6INvDuDgvpFwQr_7rO1_ytxaT6ayPlQ9oT2xKXMZxpK7tkfJHElpjjC6Fgb04emmHNpT6d6rMc1gPVf4aBcDt431d4eovW2Srl1yS2ihRsHf7vjZexmizcgJSx9mopYNmjy-yNBTHpxchqrZyRJU2zu7rERJnqjJbik7a2tfLiIRwMmpm32JzYK-saPWyLITC0iYxc7LTiqgSwBgetIB36D2l-cOQmn-nr7e2EnZ9F2_GFzLC5Sd98mt40Ox6gJkvO6bKctXMOIVcyAI9yfcgOBLbzU3SAGBUTmsUlX22BqXEvhsDOA3s66lxwh7sHqv4OhgmZwYtxD8ji4py9L_tEYeiwRg6XPAO6VFiiJSGpqSsj6PWRlUd5jpdgwlpAPNVBrFRvD0Yzv4pk7iiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17217aebf0.mp4?token=FMy_KoJl7uxgUU5EqHua5BMPjTI0sFPgfdZuMC1VHkisDar2aB5_wHyC0liKJm88FS_tHNgv6ePdFzze48zGSZyI4nFM6pUH4dYFLswLRa4wpXXDn1gGUeLcM18BgMqODPlclQgLN0Vcm2_2gInHdnlRNXJcS2cS4zrGwBbXtv0MCuZFCuKjLtElEJlYchWxbWMe-MKEiszrYh8Dib9_dvBJWcwiCqWdMQI2SVLmY8XVkP5e96_B3vjYCHP0WwrRvlBlAI_jg4QvWmCtNOxG1e3rk6INvDuDgvpFwQr_7rO1_ytxaT6ayPlQ9oT2xKXMZxpK7tkfJHElpjjC6Fgb04emmHNpT6d6rMc1gPVf4aBcDt431d4eovW2Srl1yS2ihRsHf7vjZexmizcgJSx9mopYNmjy-yNBTHpxchqrZyRJU2zu7rERJnqjJbik7a2tfLiIRwMmpm32JzYK-saPWyLITC0iYxc7LTiqgSwBgetIB36D2l-cOQmn-nr7e2EnZ9F2_GFzLC5Sd98mt40Ox6gJkvO6bKctXMOIVcyAI9yfcgOBLbzU3SAGBUTmsUlX22BqXEvhsDOA3s66lxwh7sHqv4OhgmZwYtxD8ji4py9L_tEYeiwRg6XPAO6VFiiJSGpqSsj6PWRlUd5jpdgwlpAPNVBrFRvD0Yzv4pk7iiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«این همان آینده‌ای است که می‌سازیم»؛ واکنش ایلان ماسک به ویدیوی هوش مصنوعی از آینده فضایی بشر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/691723" target="_blank">📅 16:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691722">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
قطر: تعمیر راس‌لفان شاید ۳ سال زمان می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/691722" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691721">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مومنی، بعد از دیدار با وزیر کشور پاکستان: مرزهای ایران و پاکستان شبانه‌روزی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/691721" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691714">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNXUJP96CsMZAldOmdDG97rlbmj34-u5M0G6WRFPMc9cD0PhGyWEeyRcRarZVLYo6ksP0LQ6nJQX_NuAdDQvVZ7rW0iLmQkRnVMJdnw6B2YVK_4iZFt4CeTo3QGpjBfHBXlH6LExRapFJew2_uGTosCwTe2qY3Hc6nprz2CW3AAqGsC3F4Yb6r7GmOISK2p4SpF7Umxp0jFk8MGYPtGPDvpxz0mPrHp00pZtH3ITzqLzMnIT7EUzJgG1xeLTuNxNZxk0uIwzwH24_FZXG4o8Yb4CgNPZj5VR2gNQt3SQ1iL9oj_SGoeRI2OBJsc9U0ELHPuXsqPzLevlml2PM2Y08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNfZ3549_NsioQh24ncIsqwQQfQpuE3RlnaNn4FWS2zlQLHLSx-izHbswVxX_cKjC7Vhm8FN89KWHtSynsFf076ROrIS86JtMuOpn4E30lbX1MVapM7XmRVLwtnHeFLchXwRTJWwCidSzmloQrGOr_wHuf5tJCqFck_Zo05qzySlDMCdzrP_VtMm1uZaNe7EdJNll4EAGPdCXxNBJEXkMfumfWF1j3QQXZxd5O-mXcPldM9G3Wsww7Qm2uZms7K-WlzSxIHHf2Vh-Vz8C1dM__0TYS-b6f3FDDgVvoH1x347axsv_vqxFKBN-E5L9VRD_T2UAihSTSH9xHKU9gT-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQAMwk6EyCVBxLgd_sNwRBF3dkX4zlbGw_T2G0YeCgOCjZj10JRFA-JSzexVIkhDAOiu3_WQvB66O8MhjXqP4J6cjJ89JXMnq3YWz890lUDdNQRQ1HyYiODUGMGaYzXB_6Njm0Ztb5EjgD4iKYGMbZbJquMRbMUhQsIckkJrophQnrryl_J7kv2NHPhjQmlU7qfPZ_a3AGCiVyyuf2ClFLK6jhM5CMtQzHyoHFU7vkr4L4xWYoXsZH1ocmErnNLQZl3DAoBhY1A5u2jH7ysgWXI-B3K3BUxWd_navje1V9FrkLebMI-sSU0zqv0A1DsSfGtd8M--LDJk3gS1Xw01TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uum92rN1G4552ZsyEIDV4_RBnZUXL8MRere6GeAmU-zTqOyC_Zwet8hHvpaNqPdF0OzEysrIVplksBGbMDWi2jxTqvfHELrqRb9CjOUj7UDRo1eUibp5ctrNb6jtqoqRICqJr81o4ICc097ju7qoMqzjZGUUMIa5Yn-PNtbkWgjnw6QeLED9VO252MAqXsQPHBZnU-vTFNgss5e5Xz_xEb8ITzA0iCRp1p-kEfodzVaRtC6C-eLs4agl7eIqTOi_rawQcZmuBN7eoYoZ2f8w0W6Rak_dmoJS67xcrrGz4GCVuRSr8TqarEEUZ9AjldqvPGt6lb5fYlvzKPv6vLAs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgfkxgwEIcYh8kena3vE9gMXTg9ebBOnQGkEgGJVkYvbaCMKq5oms0hO0MVzQ15Her3bvR6iomzrnCd01GSXugA8bYhYvItdLHjd2H5gMmoLQvXAIXPKB_iEyOdkqHIDqF40mGh_w431QLYFJHHLv7b_u-do_HVg_FGJ5rhTUdKFblw67aVsFLRl5-1V14mvivHaWHnTdVXkOD69a9DyiGvMDV7brzGBYN97zv6ynbT7ugswjbOp867rLlne9Jo1Q87BJ0lkcj1y-qOHfjZFG2AXwll2f1Hbev-nbC6wui10wXkqTINsryqN2w4bNyJ09eQEQkLjskZ5uq3znSAhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMDop64hurt6lckt4oWaObngXnM39F-ysYqnF0ho__7XwFw6NSS60ylQmsP7qkqcnxsjf103vp49BR21jssjTqOSTVr0IXVp0vosPE4MHab8Z85zlwyTgeQS9_YQTNFUc0TXNpkzVRgPHPDhFayFvVjIpGz-TPWCV2OnseXlHDUfkOAuDNiyeSXsI7w4WEJEmcwtr-E2jfXRPxPG05EOH9K1PVxe3Ia71balTH7rVozw1V_ck0kgkzYLFj_g8BOAoW1ONWMpOgMXlwnvgtvwPeuKIe0pGsGr9cJYCRwLSx8Totqk-0rDHVoG9026FV34EnZJVzW4Dwf_zBTz_vdHEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی هفته
🔹
این هفته بازارها چه مسیری را در پیش دارند؟
🔹
از بورس و سهام تا طلا، دلار و دیگر بازارهای سرمایه‌ای؛ کارشناسان، روند بازارها را بررسی کرده‌ و از چشم‌انداز روزهای پیش‌رو می‌گویند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/691714" target="_blank">📅 16:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/528f1dabec.mp4?token=p4DAlbykxuft2dJB3YlN2TV1k2V6s_hArWVZBgoFYRSmFhF3PcWoklrBD65mR5ZPNcxCaS4W-xIDPMfXh_d9QDJEOsUgnoOkeTj1BAplSXSRU7cOkIaAod-LsUyJMRAqOrCHeJMQFAZs6j9e7M1SsxATtUuQ1IGYWJjOZVgHD5Y-GHuaiLkB47AOqu2v9HUwLl0jUjMyLp6fnjdAgjISY8NnaWRlUx-hH1iEEyrpAwMEwl2TFU0bTvKHeqI6WscEKB91m4rgzaZmX-Wbov5i60mo89NpwpBH-bFJULqoBi-JfceOZrbzOmSb9dj7h-7glBuLbwPTqvHbH8M0mVpYcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/528f1dabec.mp4?token=p4DAlbykxuft2dJB3YlN2TV1k2V6s_hArWVZBgoFYRSmFhF3PcWoklrBD65mR5ZPNcxCaS4W-xIDPMfXh_d9QDJEOsUgnoOkeTj1BAplSXSRU7cOkIaAod-LsUyJMRAqOrCHeJMQFAZs6j9e7M1SsxATtUuQ1IGYWJjOZVgHD5Y-GHuaiLkB47AOqu2v9HUwLl0jUjMyLp6fnjdAgjISY8NnaWRlUx-hH1iEEyrpAwMEwl2TFU0bTvKHeqI6WscEKB91m4rgzaZmX-Wbov5i60mo89NpwpBH-bFJULqoBi-JfceOZrbzOmSb9dj7h-7glBuLbwPTqvHbH8M0mVpYcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز   سپاه:
🔹
لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔹
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691713" target="_blank">📅 16:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
گواهینامه رانندگی ۹ برابر گران شد
🔹
هزینه دریافت گواهینامه رانندگی که در سال ۱۴۰۰ حدود یک میلیون و ۷۵۰ هزار تومان بود، در سال ۱۴۰۵ به حدود ۱۶ میلیون تومان رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/691712" target="_blank">📅 16:15 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
