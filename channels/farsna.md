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
<img src="https://cdn4.telesco.pe/file/JnpM3YVN64uN6jPkbTswR9taA5G22TE8y8I3sAfvxEdY6j_c1uaoaU22rPRc1lOE2MZudya2H31X3V639shbgttLARl0clpa-YAHxYnqmSR3NSTKAH3ocM6WQgkZ2ViVd1mHZ1Kfxq0nGU_qumRrQ9shkixIMNjU_y-q2lqyKngGmyQ-rhsIPV_gTZexlhMmrodpd2ffcIpu9ZMN_ONxOfZxlQF7JLHVWUIlIakRDt6RI9wmx4fywRS9daTdvbDUvDKtcIaWDK4ipXqLFdJSDLe3gaqaOd7lnZ_Lw1aqqhpxL-MjQBMREYBHA5wKbrkZCdO2UtQUgP4Gs8wIbX80xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-464242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8hZvUX5wS5u_jgOXR3BWujSrCseS8ZHJcV6k9AIMS2cdGO4Y58X67k6JE_tLuiaH8J2pn6zxEHWYmLOvidKWOI38LeJtWrQOSgzzQm73l67CMzB4LMvCNRjNgamrBtK2izfZCzZONiQrVwenSNIh6ZsQdjbM7QzKbgdEpx9UEMQAWhinsDBy3Sfc4sZ3o9KUXkEyL-3HMxtDjJmU8LMaVXGc6RrD90-gM2lSzCN56f3z_xLvCn6PGAAkPBvonBIKh4Kja66QqsTMZLUtsJ_uTlbPNv-sphEnzl7GOU8HlA_I_VCv5w3b6BSf_a2dbNjPElJNQIQrmwXwL_yBnk2PB4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8hZvUX5wS5u_jgOXR3BWujSrCseS8ZHJcV6k9AIMS2cdGO4Y58X67k6JE_tLuiaH8J2pn6zxEHWYmLOvidKWOI38LeJtWrQOSgzzQm73l67CMzB4LMvCNRjNgamrBtK2izfZCzZONiQrVwenSNIh6ZsQdjbM7QzKbgdEpx9UEMQAWhinsDBy3Sfc4sZ3o9KUXkEyL-3HMxtDjJmU8LMaVXGc6RrD90-gM2lSzCN56f3z_xLvCn6PGAAkPBvonBIKh4Kja66QqsTMZLUtsJ_uTlbPNv-sphEnzl7GOU8HlA_I_VCv5w3b6BSf_a2dbNjPElJNQIQrmwXwL_yBnk2PB4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رستاخیز وطن در شب ۲۰۸؛ روایت اقتدار و مقاومت کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/farsna/464242" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpGbleDLXPi2COZx1JPkzbnq9vKvQdcEh2t-DJQLk6ReoMzwceu0vY1Gl2m-iLZyaqpEFA07mTvp0o40iTlUaSF6QX1TbJHae1uLGIhJFHeTjvNDrUDStVYQsQ0GYQZ7ylI4t1Y2Iuugd2mA-atAwSCKSRf31F0abBr1alkToNQMvhBsX3HC8811q7me35iT7CdWes1Pa1dc4nlK6Y6iYEzdnqXJ2hwIYaX_JzGh8IGUrFuyl7wztSRuVjEC-5o2dIqSs3tiSLlRqbm_8vrlAKHS1XccfnOt7xCPQj1Ewu91O2l6j-dLamUA8Lh3WJ_s-l0oOA4GEskgz995NDdYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امور زنان رئیس جمهور: پیگیر وصل شدن کالابرگ و یارانهٔ زنانی که به تنهایی مسئولیت فرزندان را برعهده دارند، هستیم
.
@Farsna</div>
<div class="tg-footer">👁️ 346 · <a href="https://t.me/farsna/464241" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمدی مقدم، رئیس دانشگاه عالی دفاع ملی:  صدام هم فکر می کرد ایران را یک هفته ای از پای درمیاورد، اما ۸ سال در این باتلاق ماند
@Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/464240" target="_blank">📅 22:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQhzIEzDVGT6Wcm_6tF0qPjKRTOFuK_gCX2LqmXwHyJR7z0dDiXUt9SwoXr1fz3B05Fc3vX9gXNP2z5ZkI2Owi9q7TSQM_uRd5RyyYTLtYvo06Z3owutWVxAXZ95-OHVxpyDokESXI_Yu4PaB8bEIWIE6DmwW4TpHGNPprGPXZnr2KNs0drl4gAnwyBy_ig57uSzL98ZE6CGLS5vtV7OD0uPuQb9aHwwiwl1qaPJVwK-b2lQu_p2tS4nZBULPc_prraOHj9dLqwKdc7ThIa9HAzuPPhROOhAiR8RPCeRzbyZujFdxo9rKW3i4s8tjd_BpKzCk30nquJiXqdlUN8EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: مشارکت اروپا در تجاوز به ایران بی‌پاسخ نمی‌ماند
🔹
اعتراف دبیرکل ناتو به انجام ۵۰۰۰ سورتی پرواز از پایگاه‌های اروپایی در حمایت از تجاوز نظامی آمریکا علیه ایران، نشان داد اروپا بخشی از زیرساخت تجاوز بوده است.
🔹
دولت‌هایی که قلمرو خود را در اختیار آمریکا قرار دادند نمی‌توانند از مسئولیت شانه خالی کنند. این مشارکت بی‌پاسخ نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/464239" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
عکس حاج قاسم جلوی چشم نتانیاهو در سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/464238" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsppmZWc5uL7nM7etlR5uRuztL2GwXDubuYkbV5r-37IVkgiV6LxIXY_HLC-DzHmPc3UT-NPrNuw5bTcKW7gjxcVsPx2fYhYCqbO3aBr_a2wQQQUmAACon7FB8VUyhwi69Z1KGb41mXViSz2nhp03Xy_UV6Mj7E3n6u3UZGDUU-vdw3YzdC4QWNgKlZ4hdW_QPjMqelSzdnVdt4V5xILkKuyWRmnn46S2msjHbdF5raEMK7--25bIsdL1gk_-_aIju7AsTyfHCVj64zN0Rmd-iA-c11spkfVu0EehExxqDpx6htmD1RZu0bUxMVJrwR_0p5qVyT1k8fjkzFipsoaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش یمن به عمق عربستان سعودی
🔹
سخنگوی نیروهای مسلح یمن شامگاه امروز از ۲ عملیات نظامی در خاک عربستان سعودی خبر داد.
🔹
یحیی سریع گفت در این عملیات‌ها، یک مقر بسیار مهم در ریاض و تأسیسات نفتی آرامکو هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/464237" target="_blank">📅 22:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستاورد جدید محققان جوان ایرانی در حوزهٔ سلامت؛ داروی درمان کبد چرب التهابی
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/464236" target="_blank">📅 22:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464235">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران هم‌زمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.  @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464235" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/464234" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDqMl8tv5LH1t29Tuc0S7RTsJ2baRsY6GpBTua0877w4wrwbQjzxFnt1LPQpWX7LtnhyG16RSu_8PTfDGA6969FKQEeON3_SxSM25LzkwfqODSp2X5vZykKrUARyYg4KLRp6YM9Doci7xpa2GkTcaqrD1S6SFFQn9SbuQdQVEDJcaTEQtQTwUFdHXzcLV8ouzM-9rQTMQ7NHHow4GipgA81wSk4Z8m-i925m1KqpqbI9I_UJ8vHNR9fgEuC-q-2psazegwDR7ixnJUGZDYFhge_bWnuAvDL5IcO5MJIFvxNgtwuqFhAVruKjqORn1ARGPeLAgQ6qIaB9UVTZZoJ1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنا بار دیگر از جنگ علیه ایران حمایت کرد
🔹
سنای آمریکا امروز قطعنامه محدودیت اختیارات ترامپ در جنگ علیه ایران را رد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/464233" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاتل ۷۳ هزار زن و کودک اهل غزه: اسرائیل مرتکب نسل‌کشی نشده بلکه از نسل‌کشی جلوگیری کرده است!  @Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464232" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر رژیم کود‌کش: ارتش اسرائیل، اخلاقی‌ترین ارتش جهان است!  @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/464231" target="_blank">📅 22:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njIXv_T8mmGpMfFpD4upJp4NH4xOw9W6nAg3XyUAVRapwqRVcYcoR0tP3xLUtmNfFxJm87bWsIeL-n_r79pW0UcX8-9B3bmy3ZsTD3hZQlznXwXzlrUJsbVDPWgDjIA21GoVflNK-6qXfb3V-abkRjsehxpVdTOvNd3TMEHIoqCHW4nMbOZnsMyQCMqwoG-xfg7dEdNdS0C_E-rGvKo-wTm58m44dD_RDaGoPf8s33nDOQfXa_LiDMekDanG39IsW-sfFvc834sPtsSbYZf67u0xzzeB5T9OpeI4yowqXVipzPAD4KAwoefEvaFMzEgrU9AuLltHSBEpE2_YVZ_n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که هیأت‌های نمایندگی بسیاری از کشورها در حین سخنرانی نخست‌وزیر رژیم صهیونیستی در اجلاس مجمع عمومی سازمان ملل، سالن را ترک کرده‌اند، نمایندهٔ امارات عربی متحده همچنان پای سخنان نتانیاهو نشسته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/464230" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a10092a8.mp4?token=HA2bGCakrGkRn9Yc9HH5kf_HlxFude3G1rmzClFbR64OAjjUb1DO2pCud7QO8SLhbyw_GaIO1K1H3MloNDUGp9aHnOGYjHsEosDa1dBdSQcBhoYl9aFsfa62VdgrTChqDcM6syUgDF6_TBTE8M4zIShIV4jFztskX7jQaa5lfUJj-l9Par34WUb6OUUWgxVf3-WBc2kUBiRzFj7cm10DkSCQowtr4L7QEgnPNU8N6CVqJiWF3ozc-u-r4N1yWGzBxE4ioywKcAOITzFj4mhvcop91atsJs3QMJVgHafuNZvaxll7PBRNTjSuKZ-HNaxekICLF8CMXPzfZWanIMonDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a10092a8.mp4?token=HA2bGCakrGkRn9Yc9HH5kf_HlxFude3G1rmzClFbR64OAjjUb1DO2pCud7QO8SLhbyw_GaIO1K1H3MloNDUGp9aHnOGYjHsEosDa1dBdSQcBhoYl9aFsfa62VdgrTChqDcM6syUgDF6_TBTE8M4zIShIV4jFztskX7jQaa5lfUJj-l9Par34WUb6OUUWgxVf3-WBc2kUBiRzFj7cm10DkSCQowtr4L7QEgnPNU8N6CVqJiWF3ozc-u-r4N1yWGzBxE4ioywKcAOITzFj4mhvcop91atsJs3QMJVgHafuNZvaxll7PBRNTjSuKZ-HNaxekICLF8CMXPzfZWanIMonDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو با نمایش پیجر در سازمان ملل به اقدام تروریستی خود در لبنان افتخار کرد
🔹
نخست‌وزیر رژیم صهیونیستی: پیجرها را به یاد دارید؟  خب، این را می‌توانم به شما بگویم که حزب‌الله حتما آن‌ها را به یاد دارد!  @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/464229" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoarZbpeJvndBgwTAOD538LTC3hon4sIIdyp6nb-LN91lqrzDTtzoo0vj83q5FGU0rsFAyLkjMdAhU4YRDYo0WFcQqln8Frc2mIzYSo3R2r6VDRVHzxTjCLPvzheqFqVuJX6xIiENnpBjcVyiU83kEUW40MtduxZR5EMj77KoyIWzNkB-ZgBCM05p-0JnNXOZg2S3JfxoT2q_ZYlaIG5Qo0Uxc3iLPkBCb-BQ9-NHvl_PZ2Mwxj0mtf5xM9c9v2txlE_mE6P7VnR4kXuKA2Ge0nXLk55N7RAk-sRUEmLmRNrFHoGi9JppNKrSY86d_Pa16GNVqIn5cjcGrNwnNPySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران هم‌زمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/464228" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84ce924d3.mp4?token=FwO8oqxWx5ODGy_VuYPUbmU_Hr5IOOcElawB62F_EvKT1Pk4GC0R7Kdi8llWGZ3qz3p3pzZulbJ9S0Tk9lUM-l6ygKaZwzkcRV4zqfdzjWH8CkTIm5xNt1RPU0XlnRB9lOiqQyZRSc2mLlskz48lUQJfWrhmsptfksEJegK1SKWyqZhQhkHexa5Xaxyw88I_Xe7UZrqN2KVz2XVE70boOEOxqe58epXEppzyyk0IOlFAeRF1Qrg4W5AXI7Dher6lOanacVnxfty36Dmqw3ey_0_KuX2Mcxh1sh7mBr39XlJ70juPBy8tNK3uX1mqB1QqfNsQ4DahkyEbxdWg1L7MvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84ce924d3.mp4?token=FwO8oqxWx5ODGy_VuYPUbmU_Hr5IOOcElawB62F_EvKT1Pk4GC0R7Kdi8llWGZ3qz3p3pzZulbJ9S0Tk9lUM-l6ygKaZwzkcRV4zqfdzjWH8CkTIm5xNt1RPU0XlnRB9lOiqQyZRSc2mLlskz48lUQJfWrhmsptfksEJegK1SKWyqZhQhkHexa5Xaxyw88I_Xe7UZrqN2KVz2XVE70boOEOxqe58epXEppzyyk0IOlFAeRF1Qrg4W5AXI7Dher6lOanacVnxfty36Dmqw3ey_0_KuX2Mcxh1sh7mBr39XlJ70juPBy8tNK3uX1mqB1QqfNsQ4DahkyEbxdWg1L7MvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توجیه نتانیاهو برای اشغالگری اسرائیل: یهودیان از زمان حضرت موسی در بلندی‌های جولان بوده‌اند!  @Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/464227" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
خانوادۀ ما هیچ‌گاه نتوانست برای سهام عدالت ثبت‌نام کند.
همسرم از کودکی در خانواده‌ای روستایی با کار کشاورزی بزرگ شده و بعدها به خیاطی روی آورده است. با وجود ۲۲ سال کار در یک شرکت، در ۵۱ سالگی فقط ۱۲ سال سابقه بیمه دارد و پس از تعطیلی شرکت دوباره به خیاطی مشغول شده است. سؤال ما این است که چرا فردی با چنین شرایطی که نه بیمه و بازنشستگی مناسبی دارد و نه وسیله نقلیه،
از سهام عدالت محروم مانده
است؟
🔹
بیش از سه ماه است از
آسیاتک
خط فیبر نوری، بسته یک‌ساله اینترنت و مودم خریداری کرده‌ام و قرار بود حداکثر طی دو هفته نصب و راه‌اندازی شود اما هنوز این کار انجام نشده است. هر بار هم با
پشتیبانی
تماس می‌گیریم، می‌گویند درخواست ثبت شده و تا دو روز دیگر وصل می‌شود، اما همچنان
خبری نیست
.
🔸
چرا با وجود اعلام مصوبات دولت دربارۀ
سقف افزایش اجاره‌بها و تمدید قراردادها
، در برخی موارد دادگاه‌ها
حکم تخلیه
صادر می‌کنند؟ این تناقض باعث بلاتکلیفی و نگرانی بسیاری از مستأجران شده است.
🔹
مدتی است
سایت جست‌وجوی متوفیان بهشت زهرا(س) قطع شده
و امکان استفاده از آن برای مردم وجود ندارد. خواهشمندیم شهرداری تهران و مسئولان مربوطه برای رفع مشکل سایت اقدام کنند.
🔸
دربارۀ وضعیت
بیماران اعصاب و روان
، به‌ویژه افراد مبتلا به اختلال دوقطبی، گزارش و برنامه خبری تهیه شود. بسیاری از این افراد، به‌خصوص جوانان
از داشتن شغل و بیمه
مناسب محروم هستند و افزایش هزینه دارو نیز فشار زیادی به خانواده‌هایشان وارد کرده است.
🔹
ما حدود
۳ هزار دانشجوی سال آخر
هستیم که در
آزمون مهارت‌آموزی آموزش‌وپرورش
شرکت کرده‌ایم. از بهمن ۱۴۰۴ آزمون دادیم و خرداد امسال نیز مصاحبه تخصصی انجام شد اما حدود
چهار ماه است برای اعلام نتایج در بلاتکلیفی هستیم
. آموزش و پرورش می‌گوید نتایج را به سازمان سنجش ارسال کرده، اما سازمان سنجش اعلام می‌کند چیزی دریافت نکرده است. بسیاری از داوطلبان نیز به‌دلیل وضعیت سربازی، قبولی در مقطع ارشد و برنامه‌ریزی برای آینده، با مشکل مواجه شده‌اند. خواهشمندیم اگر می‌توانید این موضوع را پیگیری کنید تا تکلیف ما روشن شود. ما فقط یک تاریخ دقیق یا یک اطلاعیه ساده می‌خواهیم.
🔸
لطفا در مورد
خودروهای ثبت‌نامی سایپا
پیگیری ویژه‌ای انجام شود. ما در تیرماه ۱۴۰۴ ثبت‌نام و در بهمن‌ماه همان سال تکمیل وجه کرده‌ایم، اما با گذشت حدود هشت ماه هنوز خودرو فاکتور نشده و هیچ پاسخ روشنی نیز دریافت نمی‌کنیم. برای پیگیری به
تعزیرات
هم شکایت کرده‌ایم، اما اعلام شده این موضوع در حوزه مسئولیت آن‌ها نیست. ما یک سال پیش برای خرید خودرو طلاهای خود را فروختیم، اما اکنون
نه خودرو تحویل گرفته‌ایم و نه کسی پاسخگوی ماست
.
🔹
از
پیمانکار شهرداری منطقه ۱۰
خواهشمندیم به ایجاد
جوی غیراصولی در کوچه دلخواسته
، نبش سلیمانی رسیدگی کند؛ چراکه این جوی باعث تجمع لجن و ایجاد بوی نامطبوع شده است. همچنین از شهردار منطقه ۱۰ درخواست داریم با حضور در کوچه دلخواسته، مشکل تردد خودروها را بررسی کنند. با نصب پل، تردد خودروها در این کوچه افزایش یافته و آسایش ساکنان سلب شده است.
🔸
کالابرگ ماه گذشته برای برخی اعضای خانواده ما واریز نشد
و متأسفانه کالابرگ این ماه نیز برای آن‌ها واریز نشده است. با توجه به شرایط مالی خانواده، این موضوع برای ما مشکل‌ساز شده است. لطفا پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/464226" target="_blank">📅 22:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b138f38651.mp4?token=Zu7V9SHXeyayW3dJPM-AGmbqs7SfdPOsEJfJYpWZlQS775N846Xh51ZeweAzA8YsSXsLvJ2onewmnF6ii2L7iKfbTJAZZgzLpKCMo5hQ5YoZcD8SyjyhaOV3viT9LX6hnLLE9ZI5cxHW7AgLr4NY2z-tG_idwXSunTfS1JGQ5gWR_zxuknyKEi4Kr-7jcS5UUqsORrJ-KxBIYIauCbVHMvgwPIRu9iYzoclZuyTxaYiCa1wcZ46vyR5IVoHZm2Gop0fISV_m9FbFR5yzSm7bl9odk6kXVbHgkmPFdy2cdJNhpimnB4Ln3n0Ob0i8pY0u-AdNbdxJqVp7EmhwbzrVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b138f38651.mp4?token=Zu7V9SHXeyayW3dJPM-AGmbqs7SfdPOsEJfJYpWZlQS775N846Xh51ZeweAzA8YsSXsLvJ2onewmnF6ii2L7iKfbTJAZZgzLpKCMo5hQ5YoZcD8SyjyhaOV3viT9LX6hnLLE9ZI5cxHW7AgLr4NY2z-tG_idwXSunTfS1JGQ5gWR_zxuknyKEi4Kr-7jcS5UUqsORrJ-KxBIYIauCbVHMvgwPIRu9iYzoclZuyTxaYiCa1wcZ46vyR5IVoHZm2Gop0fISV_m9FbFR5yzSm7bl9odk6kXVbHgkmPFdy2cdJNhpimnB4Ln3n0Ob0i8pY0u-AdNbdxJqVp7EmhwbzrVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌زمان با آغاز سخنرانی نتانیاهو، سران کشورهای مختلف سالن سازمان ملل را ترک کردند  @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/464225" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464224">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
هم‌زمان با آغاز سخنرانی نتانیاهو، سران کشورهای مختلف سالن سازمان ملل را ترک کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/464224" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoM-yKo4iENm-8ChIoE67gBK1iRPEUqcIkWZHnrxoiZrISoUYl75BmHUu3KvMYGcrx-6pGHSGNeq0bZ8zQHxY-akI-n4-rli_afHokqJgCN3MIfb923dCdpXqDNQFc1r3_C3GHAppG4SWoaWVSR2Ksl9J9_zYQYSQ3RibEj4jgf3ANHWAk35oK0BLf4oearFLmvI6D-daW4kHldj7SZCcgeuLaz8KQslpYP60in2K1O-9kOfFeztxQ3KvNXEQFElmApBYUmNslxch0-ptZz1L493Cd_itV3O_W_eW8xkhKE4u81Ha9mg3PayKLthxhrJo1YZ4dpH2sM_-oFxwXP0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار یمن: مرحله بعد، برای عربستان دردناک‌تر خواهد بود
🔹
وزارت خارجه یمن تأکید کرد که افزایش شدت جنایات روزانه عربستان سعودی در یمن و هدف قرار دادن مراکز غیرنظامی و منازل شهروندان، ایجاب می‌کند «با این رژیم با زبانی که می‌فهمد سخن گفته شود».
🔹
این نهاد یمنی هشدار داد اگر عربستان تصور میکند که می‌تواند از مجازات فرار کند، در توهم و سراب به سر می‌برد.
🔹
صنعا می‌گوید به خاطر تداوم فعالیت‌های خصمانه و اقدامات جنایتکارانه روزانه عربستان علیه ملت یمن، مرحله بعدی برای رژیم سعودی دردناک‌تر خواهد بود.
🔹
وزارت خارجهٔ یمن از هرگونه تلاش برای صلح که منجر به رفع محاصره این کشور شود و به اشغالگری عربستان پایان دهد، استقبال کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/464223" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جدال بابک زنجانی و وزیر صمت بر سر سایپا
🔹
وزیر صنعت می‌گوید در واگذاری سایپا حفظ اشتغال موجود باید توسط خریدار تعهد داده شود اما بابک زنجانی می‌گوید مسئولان باید از شعارهای پوپولیستی برای تعهد بخش خصوصی عبور کنند.
🔹
فرآیند واگذاری سایپا به بخش خصوصی از حدود یک‌ونیم سال پیش آغاز شده است و نام بابک زنجانی نیز در فهرست متقاضیان خرید این خودروساز مطرح بود و پیش‌تر مدعی شده بود با پیشنهاد ۲ میلیارد دلاری قصد خرید سهام سایپا را داشته اما منصرف شده است.
🔹
حالا زنجانی در واکنش به شروط وزیر صمت مبنی بر ممنوعیت تعدیل نیروی انسانی و تعهد به عمق ساخت داخل، این مطالبات را «شعارهایی تاریخ‌مصرف‌گذشته» عنوان می کند و می‌گوید خصوصی‌سازی نباید فقط به انتقال مالکیت محدود شود و باید با محوریت توسعه فناوری و افزایش بهره‌وری همراه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/464222" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cac0ac8f6.mp4?token=C8_F3-h9dyBq-vBSP7KIOrl2aGZNy50O-zkBBmzphAehA6SwkDAHMY-bbOLcODymSvneef5CKolcWGLc8wCSMgOkkaMjhDz5AQJ8bUHzWtMdeuW2e-0oXvDagixx36dZpjIN2pyVPkQEQG0TS2xIfWiGSeeS8f6bbFHHpzxLtRVgxS4PwtT2bgvbWbnAc-MA6ojuh2f8noVqZmu5HGP2TU2kUy1JOH9PgqQT6xM9IKUGyCaOGVAKUL2wZfs7xod0PXsEcbQVLawKW2yMV9E6HuEZCieplLt5VLsTpFsfDHOenoN8gOD4uAYwZv_7J9LGXCm7gaWJWMgMKyJdA67WuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cac0ac8f6.mp4?token=C8_F3-h9dyBq-vBSP7KIOrl2aGZNy50O-zkBBmzphAehA6SwkDAHMY-bbOLcODymSvneef5CKolcWGLc8wCSMgOkkaMjhDz5AQJ8bUHzWtMdeuW2e-0oXvDagixx36dZpjIN2pyVPkQEQG0TS2xIfWiGSeeS8f6bbFHHpzxLtRVgxS4PwtT2bgvbWbnAc-MA6ojuh2f8noVqZmu5HGP2TU2kUy1JOH9PgqQT6xM9IKUGyCaOGVAKUL2wZfs7xod0PXsEcbQVLawKW2yMV9E6HuEZCieplLt5VLsTpFsfDHOenoN8gOD4uAYwZv_7J9LGXCm7gaWJWMgMKyJdA67WuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدایانِ کوارِ فارس حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/464221" target="_blank">📅 21:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464220">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10289f5082.mp4?token=M4-bKNLfAd4c_PxT_dZKGWSQRUo0l5-gfTULcj0IYL7qQ7wegmQ1zFHtPVG8oI7pTQxZQpux91toLwQBLPDzCdOhYt3Yp1CYDWJNXbMOm9d1njZ8sGCbcT5zQQDZODT2J4CwOyptCteQInZSgKEZ0BPvAcfLLo-eH6cI_ATI75w7bAAUIG-IxwvKb7wyZy8kN8bRKFMMZcTQ7g6YAoYjR6mZI363eLA4bY1FVj854Gpl52lpdETwNP_wpvPGXXbHvM-2rdTP3_OQGaJ3UUq6MRM317EPyNipt3UK9MH8fTXHrlRFgYtxUN36djzMG5ZqTpW6a6Y3H2dbzhhfUkPFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10289f5082.mp4?token=M4-bKNLfAd4c_PxT_dZKGWSQRUo0l5-gfTULcj0IYL7qQ7wegmQ1zFHtPVG8oI7pTQxZQpux91toLwQBLPDzCdOhYt3Yp1CYDWJNXbMOm9d1njZ8sGCbcT5zQQDZODT2J4CwOyptCteQInZSgKEZ0BPvAcfLLo-eH6cI_ATI75w7bAAUIG-IxwvKb7wyZy8kN8bRKFMMZcTQ7g6YAoYjR6mZI363eLA4bY1FVj854Gpl52lpdETwNP_wpvPGXXbHvM-2rdTP3_OQGaJ3UUq6MRM317EPyNipt3UK9MH8fTXHrlRFgYtxUN36djzMG5ZqTpW6a6Y3H2dbzhhfUkPFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و گفتگوی عراقچی و ژینبک کولوبایف وزیر امورخارجهٔ قرقیزستان  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/464220" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سازمان اطلاعات سپاه: ابتکارهای نیروهای مسلح جمهوری اسلامی ایران، معادلهأ میدان را تغییر داده است
🔹
حساب مجازی سازمان اطلاعات سپاه: مقاومت و شجاعت ایرانیان و استفاده هوشمندانه از جغرافیا، الگوهای پر هزینه و کم خاصیت رزم ارتش آمریکا را از طرفی با بن‌بست مواجه ساخته است؛ و از طرف دیگر، تخلیه و غیرفعال‌شدن پایگاه‌های سنتکام، انتقال نیرو به اردن با تصور «عقبه امن» و تحمیل تلفات، عقب‌کشیدن تجهیزات اطلاعاتی و نظامی به نقاط دورتر و حرکت به‌سوی استقرارهای پنهان و زیرزمینی، هزینه سنگین حفظ حضور کم خاصیت آمریکا در پیرامون ایران عاری از تهدید را برای مردم امریکا به همراه داشته است.
🔹
ابتکارهای نیروهای مسلح جمهوری اسلامی ایران، معادله میدان را تغییر داده است؛ پایگاه، باند، آشیانه، هواگرد و هر چیز روی زمین و آب را از جمله ناو های آمریکایی را در معرض ضربه مستمر و مداوم قرار داده است؛ در مقابل، تداوم قدرت آتش ایران و راهبرد شلیک مضاعف، منطق افزایش نیرو و تجهیزات آمریکا را با یک تناقض مواجه کرده است:"افزایش حضور،اهداف بیشتر و تلفات بالاتری ایجاد میکند." و کاهش حضور توام با اصرار به ادامه زورگویی، مردم را علیه آنها بسیج می‌کند.
🔹
همچنین، دستاورد راهبردی را باید در کاهش آزادی عمل آمریکا سنجید؛ اصابت ها به نیروی دریایی آمریکا، تحمیل تلفات در اردن، از هم گسیختگی شناورها پس از پاسخ‌های کوبنده، آسیب‌پذیری، انهدام و به‌ غنیمت‌گرفتن تجهیزات بدون‌سرنشین و افزایش اهداف در دسترس ایران، آمریکا را به سمت پراکندگی، اختفا و «حضور حداقلی» سوق داده است. معیار اصلی تغییر موازنه، صرفاً میزان خسارت نیست؛ میزان آزادی عملی است که از دشمن سلب شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/464219" target="_blank">📅 21:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a8d6c21a.mp4?token=th7sc5SWt2fp_P8u7iQu-GMDrSfb2ObS-H7ySHN00iu3_cqO1IWKMnjikk3F40qV83wCrfUsQ203lRrPBFAx4VqdJK3wnBDLTNubZdFzPoZbL--sEUj6knQA_rymcH7YVol4vQAbON9GpRyLa1SgvrV9H3k0TG3BbVFHRV0efiZiB4xlrnMzwztHHlcu4wdAv_qDKyzPTsw5pXj5NPUXRlt3FQ1o4q3FoNexyhI2MJ6C1SqLmulrxx0zjL99Lq9-UfY6ik4H_i9N9-FMfwcHuq9JyVhEanYNhx53Qc-c3lYI6Bte7ksHo1DSSC3yvc5nLzj-WREISZ7CtSr-HmwQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a8d6c21a.mp4?token=th7sc5SWt2fp_P8u7iQu-GMDrSfb2ObS-H7ySHN00iu3_cqO1IWKMnjikk3F40qV83wCrfUsQ203lRrPBFAx4VqdJK3wnBDLTNubZdFzPoZbL--sEUj6knQA_rymcH7YVol4vQAbON9GpRyLa1SgvrV9H3k0TG3BbVFHRV0efiZiB4xlrnMzwztHHlcu4wdAv_qDKyzPTsw5pXj5NPUXRlt3FQ1o4q3FoNexyhI2MJ6C1SqLmulrxx0zjL99Lq9-UfY6ik4H_i9N9-FMfwcHuq9JyVhEanYNhx53Qc-c3lYI6Bte7ksHo1DSSC3yvc5nLzj-WREISZ7CtSr-HmwQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عددهایی که این روزها از آمریکا تا اروپا شوکه‌کننده شده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/464218" target="_blank">📅 21:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a681fb1c.mp4?token=P8aa0n43dopyZqHfkoEIDgLl30xjS07Kk-PlhxZr1_JsMMmdzE9rDRT0weTDXHVLOKeW_zhcmbrJe07-bxsi88R0dPpj7RuX5Nsa95ruccdbdZ6vQS33ZlO5Jj9Vvvbkt5aaYtcpBiclF7exl1M2sahekVB6iyG-9woHBOABOepxzHjo6o-debDAfvPRTZXWwZl3fl_9Ij21xt618Y6-5CR3oMchojOpnD3wBi7067KCN63kFlV14wERRfse_MxTI4cDSEkSc1I9nY6o6MpnZt54rPZqovWpmQcw0pY5IivvQgdlndKOWQcVORW6YkmcZGfp6lvaifUWWZwlPkvvJZWpVtoYdxoJsouVDuqEwdmWYeiqohBoI2ZStDXQcarWPg8w0u52AemjagN2g0fy-OJCWHgI3HQvnEZlKBsN777mm24jpSmES2yhnaeVhd-mTC9ZE3_6edcP8FGUKtW_MuUMwkKbhX3V35WG_3qnu5tfQzp1hoUOOAC81g6aMdHZmHa-P4Hzgx6Jyqo7Qca4nF8AL09RI791d0g2MuXzhULrJX-NC2eiCVnOp7uPZ5rO7_N8SLIOVYjInoaaUmTWO-rkddRdpafejZgRSHA9UBIFVDRTgEvhoUklgBhZLJ_E7uMyRO9xioAnGGNfFQwtJ005siYqJtxBZzAvXASTIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a681fb1c.mp4?token=P8aa0n43dopyZqHfkoEIDgLl30xjS07Kk-PlhxZr1_JsMMmdzE9rDRT0weTDXHVLOKeW_zhcmbrJe07-bxsi88R0dPpj7RuX5Nsa95ruccdbdZ6vQS33ZlO5Jj9Vvvbkt5aaYtcpBiclF7exl1M2sahekVB6iyG-9woHBOABOepxzHjo6o-debDAfvPRTZXWwZl3fl_9Ij21xt618Y6-5CR3oMchojOpnD3wBi7067KCN63kFlV14wERRfse_MxTI4cDSEkSc1I9nY6o6MpnZt54rPZqovWpmQcw0pY5IivvQgdlndKOWQcVORW6YkmcZGfp6lvaifUWWZwlPkvvJZWpVtoYdxoJsouVDuqEwdmWYeiqohBoI2ZStDXQcarWPg8w0u52AemjagN2g0fy-OJCWHgI3HQvnEZlKBsN777mm24jpSmES2yhnaeVhd-mTC9ZE3_6edcP8FGUKtW_MuUMwkKbhX3V35WG_3qnu5tfQzp1hoUOOAC81g6aMdHZmHa-P4Hzgx6Jyqo7Qca4nF8AL09RI791d0g2MuXzhULrJX-NC2eiCVnOp7uPZ5rO7_N8SLIOVYjInoaaUmTWO-rkddRdpafejZgRSHA9UBIFVDRTgEvhoUklgBhZLJ_E7uMyRO9xioAnGGNfFQwtJ005siYqJtxBZzAvXASTIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتهٔ دفاع مقدس امسال آمد؛ اما جای او میان این همه خاطره خالی‌ست
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/464217" target="_blank">📅 20:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea3a76081.mp4?token=C74JpNKRl547hK9EqbbVcZ4b3o-ft63qVVXDIBnRcbYUEpB1rTbjoCgz9Ya3qgPKgmVwWKuIuNLoYZS8pvR2QILiVqZSiOR1iT_zj7YDJEXN5jfIHLdU-SsqgAqize9CFWRj9nch-yweIN-8Y753a9v6hDJA3Igs8lA7_2w58XMmkwP7tWSN48AqFODiZxbQOSR5Fte9N_WLICuIYO6NWGJl9eYv0HM7CpU9NhPK7m9W82bhVwPdcWbq6SdEU7PYfdAyunvgVbIsnvZviN-B0yo3dH_nZiyqq2YfIeadMUHj201rnOQuX4rG04B_Y0LIbeDLk3-Os09-uNDjEBcy2YgqsPDn4nXrZ1h33xVNXCIwN-G2iCFDKg6G4Cf2On6GxP1mMI3KAWPNfp06wURmLBC29yRpg_-YgB2o1dgdc3tkrUbLbeQ4qwuMwGivnqmlTYhO008uYkxZ2JEMXdd9-XGBb5W0X07KCGlS0dE2gmKNBIQWqWodpJLZtESwo4FzJILPtlPYxERRA3G7hHkXQfmosPiixXBLSXo36nGFtkh0Bfg7pDh5guZpw4W87K-TFlZW3Mhp0QJ2Zm6RgjsD3x97gSlucM9BnESebXPI-L4DMEH5g7cCQ83_xYJ1Nhf9-LL_SOsnyhnbvpTMNI7G0uBFTxPExBML4PnGdcPkI-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea3a76081.mp4?token=C74JpNKRl547hK9EqbbVcZ4b3o-ft63qVVXDIBnRcbYUEpB1rTbjoCgz9Ya3qgPKgmVwWKuIuNLoYZS8pvR2QILiVqZSiOR1iT_zj7YDJEXN5jfIHLdU-SsqgAqize9CFWRj9nch-yweIN-8Y753a9v6hDJA3Igs8lA7_2w58XMmkwP7tWSN48AqFODiZxbQOSR5Fte9N_WLICuIYO6NWGJl9eYv0HM7CpU9NhPK7m9W82bhVwPdcWbq6SdEU7PYfdAyunvgVbIsnvZviN-B0yo3dH_nZiyqq2YfIeadMUHj201rnOQuX4rG04B_Y0LIbeDLk3-Os09-uNDjEBcy2YgqsPDn4nXrZ1h33xVNXCIwN-G2iCFDKg6G4Cf2On6GxP1mMI3KAWPNfp06wURmLBC29yRpg_-YgB2o1dgdc3tkrUbLbeQ4qwuMwGivnqmlTYhO008uYkxZ2JEMXdd9-XGBb5W0X07KCGlS0dE2gmKNBIQWqWodpJLZtESwo4FzJILPtlPYxERRA3G7hHkXQfmosPiixXBLSXo36nGFtkh0Bfg7pDh5guZpw4W87K-TFlZW3Mhp0QJ2Zm6RgjsD3x97gSlucM9BnESebXPI-L4DMEH5g7cCQ83_xYJ1Nhf9-LL_SOsnyhnbvpTMNI7G0uBFTxPExBML4PnGdcPkI-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم به سخنرانی رئیس‌جمهور در سازمان ملل چه نمره‌ای دادند؟
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/464216" target="_blank">📅 20:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1585d33210.mp4?token=qZvA_RSpOLoinTBvP31_44zkjCczfMD2bOIKq8lhmjlRu5T8xu8CyWbaXgZXM4l9vAECCQBNS6d9xvHpNNgLuEfR8k9-cqxmPTN_GpUlnPd7OkfzXOC4FL6Zku5fCB-ICoFo7L4O1_GyORFIzdBIRBXQ0Tcppa8yK6_dHGxq2kiTo7I2Z4Rn6abyyBWT0h1__vgWqCaE8xJJfS_FR8D6umsjV64iN8iC3y102pGoLUDODmO3ykU3A0q8r0x7OSxF9EbR6uZNNIM5EZAw-h8TkyKWUmqyg8dkdqjf9nSXHRfZhbfPxpo6okTYeTRQgGz-Q7IXi1DN8vp50bHgsTOdr2LYfjGyocN2kKVnw6ZjqSa4hGl4nZWUyp1LZP3nmOp-0sGcdW46EoDMOigdlWxILRx-JidMxb7OCDwLGvbCukW7qIGAb2BIuRmz-6aCtS2OsE5wnL_fyJv6n_Wdr5vBHgo74w_lmUvDiDrgz7T2fmFAKg210_HxpAyjyKgtCXJPfs0X2XI_ZewH4bsIs-R0ItwdjDDETKcMIeTNZFQwQj3qVspV_cj1CX6rOKRM5WZVv6KEQtWdnj_RU66mUE7f5uDMV2CL9P0Xxcr4M03rdCBZRnC_u-xnqeGqvou7WvCmHeclLzHMohGgQOfLfCJIf6LAuWXhLrtA4SLnOvNNgC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1585d33210.mp4?token=qZvA_RSpOLoinTBvP31_44zkjCczfMD2bOIKq8lhmjlRu5T8xu8CyWbaXgZXM4l9vAECCQBNS6d9xvHpNNgLuEfR8k9-cqxmPTN_GpUlnPd7OkfzXOC4FL6Zku5fCB-ICoFo7L4O1_GyORFIzdBIRBXQ0Tcppa8yK6_dHGxq2kiTo7I2Z4Rn6abyyBWT0h1__vgWqCaE8xJJfS_FR8D6umsjV64iN8iC3y102pGoLUDODmO3ykU3A0q8r0x7OSxF9EbR6uZNNIM5EZAw-h8TkyKWUmqyg8dkdqjf9nSXHRfZhbfPxpo6okTYeTRQgGz-Q7IXi1DN8vp50bHgsTOdr2LYfjGyocN2kKVnw6ZjqSa4hGl4nZWUyp1LZP3nmOp-0sGcdW46EoDMOigdlWxILRx-JidMxb7OCDwLGvbCukW7qIGAb2BIuRmz-6aCtS2OsE5wnL_fyJv6n_Wdr5vBHgo74w_lmUvDiDrgz7T2fmFAKg210_HxpAyjyKgtCXJPfs0X2XI_ZewH4bsIs-R0ItwdjDDETKcMIeTNZFQwQj3qVspV_cj1CX6rOKRM5WZVv6KEQtWdnj_RU66mUE7f5uDMV2CL9P0Xxcr4M03rdCBZRnC_u-xnqeGqvou7WvCmHeclLzHMohGgQOfLfCJIf6LAuWXhLrtA4SLnOvNNgC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالای غیرضروری جای کالای اساسی را در واردات گرفت  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/464215" target="_blank">📅 20:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482f2ca9fb.mp4?token=XysJtAzInpxU8qDyCl7trOH6zhThgeOjlu3ED2r4plQeOzwUBZ_jmKv-5Pq2orfoEJlw76Ola52Ri27yY_wRSfoW436AIH-BCw2J3FzCZswgmmuRlhkTrYhnL-0j5pxR5x-QpEKkbCyuNJ879OvtpSA0aLYoW-5OlDqDU2wM6VbL_wU9lPzAsZXD0AkYsZWEybL3dGbI5YJASGCKmYpV04Es8_iNfZVo-FHhPwAqZYaj2kjB0jmzw5HirjKwwC7IHnPl0Oqeto_Z_Mdoc5fxme8Tk_a6tS4wI-ggOHBtBsC6dHInWjrA_9ybMqZlqdFTs4K0Zwc1mttuh46MpkGxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482f2ca9fb.mp4?token=XysJtAzInpxU8qDyCl7trOH6zhThgeOjlu3ED2r4plQeOzwUBZ_jmKv-5Pq2orfoEJlw76Ola52Ri27yY_wRSfoW436AIH-BCw2J3FzCZswgmmuRlhkTrYhnL-0j5pxR5x-QpEKkbCyuNJ879OvtpSA0aLYoW-5OlDqDU2wM6VbL_wU9lPzAsZXD0AkYsZWEybL3dGbI5YJASGCKmYpV04Es8_iNfZVo-FHhPwAqZYaj2kjB0jmzw5HirjKwwC7IHnPl0Oqeto_Z_Mdoc5fxme8Tk_a6tS4wI-ggOHBtBsC6dHInWjrA_9ybMqZlqdFTs4K0Zwc1mttuh46MpkGxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر خارجهٔ اردن در حاشیهٔ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/464214" target="_blank">📅 20:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEzEOKfxPMOAayS8GglezOXT1MjP_85HJisprBP7aZKx2BuElkmQc-L5raanmKw68vdVqgYuIXuy9ntB1vsIa7Rlr9338ov6r8_me0i2ccXqi9gkKRAQY4CXFa2LAZo5a6_VGlbdkh2vAyzXcx-I31On9PtS26awsXBhBUIPnE6lfGyv_-rurt0Lb-DA9nH1SZy5uS9YRT9X1Ldh41XBb0eLAzxOCK7MelX7HhjIYAuuolQUbkVhVDKHeKvv_fbu6zD_cttq1YGiK5JnmUXG9iFjcascvCRVeTT6skr1C2YJpSp3nYree70EbK3oNKFH53opDeP7BtV0ybLqa2AxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پروازهای ایران به این کشورها برقرار است
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/464213" target="_blank">📅 20:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmQs0aOijiymgRlmJmO8oIzmWRtSw-BK--Y8_BElGjvYRwBhp9j1tkuhWMh-yeIjoabofp3NIqZPUb3-TkhhNwrtz7xbaoMgMP__C2n1FbyO7g8DN2W9VifNohlYELDy6r4L-nUUUWaeXHRm6A7iTHk0c3XgbbmJE3WtBXncmw32y9-sAbMBqPMZ69m3ZbL3uJ4b0-RZmof0pwj65kUbiCX6Qc7UjhJCin6RvNLauCLztFgt7axb-45NovtoEOyaJ8kRqywa7hpBYVs8Uj_VmZKNHx-APuVk5OCFCh--yctqnZyniSM2J2DInxDoDlxKaRlCJdfqJixwNoFRC0CJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف یقهٔ بسنت را رها نمی‌کند: رکورد زدن بازدهٔ اوراق قرضه مبارک!
🔹
قالیباف در واکنش به رکوردشکنی نرخ بازده اوراق قرضهٔ آمریکا در حساب کاربری خود نوشت: «آمریکا! سود ۵.۱ درصدی اوراق قرضه ۱۰ ساله‌ات مبارک! ماشاءالله.
تازه باید جشن هم بگیرید، چون برای ۲ سال آینده، اوضاع از این هم بدتر خواهد شد.
🔹
دلتان می‌خواست ایران را به عقب و به دههٔ ۱۹۷۰ میلادی برگردانید؟ کسی به شما نگفته بود که درافتادن با ایران، کار آماتورها نیست؟
🔹
حالا ما خود شما را به وضعیت دههٔ ۱۹۷۰ برمی‌گردانیم؛ با همان نرخ‌های بهره‌ی بالا، قیمت‌های سرسام‌آور بنزین، کمبود گازوئیل و البته شلوارهای دمپاگشاد! از این نوستالژی حسابی لذت ببرید!»
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/464212" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZpvIaE4rvQLtPR1HOoL2NXRE9uaMF9LAn4-G1w4a_01Kb5V_Un9INZVDlr81MkGRlY6U89wJNuHzUk_zyQ_zFWSw2V0YWzGSqnp-oGj5f-0gVAqvH7xSrAkiRQBhmixo5F1MAZD2im-q2z7B7rk1_LfFRZb-e796HTcdSDbyAmCHs8zUAxP8SXe7WFROMrt8UzLMCIbKhcLKaopALQ9Oble9RcS7EYAQJRX3LdAla-t2a9nlD95hS7yLJ55osWourLl3GfPlRmHZz1_-b_cVQgwRYcsWPJf2jHHRNHBVlwaT8ki6-jbYs_69LigDD6CT8fXQMqgZPQUVceq7DLVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Gd173Gg2lMBIx1_wI0Yn5PG5gHhfQF00nc811PHFmDgN23Ii-hIfWGdtVPL-YE9cZtUyk4H6eJ5ycXzgTEdg-fnJnz-NlJBM_rXtiaBWc6ggIZG2eT3Ei4Vne647DLeDxAoo_5m-l_LPY3flpSaI4HD8sKVurBqfPGZbqLgsVS3cp-FyPdbgpM05EUk4dLWCiOH0NXxox7Bvzxuv2hC9LmTHJ9cOZrntPGtK1jjG-4imgqBmB8fZVJlr0QiCtxy3XLKmJMwkzMFsTuEwtpPJeM6tIrLpfIpkV1X4vphtPbqUD7IsCCIWhiP2d5q-f_OTDT3Plmk9HxWDUC6_C8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5ZQu8Duolu2CSbCXcqDYwng_tzEs2mait92hLWIZW8urnCQ8D3ImtzpCy0kEPPLoCaohOp65lXr4_KqeJEf69VBSwO9ANgpdrbI-bCUgKux64Db7eZSGQElVouwJJ8604KkkMB7cgXfbfNJQA9JmHSfRkuh8j3gDfeFtc_1aCS-XoNwKX4QBbS8Aa67Lq0wkQibBt28U6Gq1lC7pC7KXg1jNKhaasl-EHtJtNF1uLRyl8U_5zgCzoALjuZckb3miC-oYJRbWI5Gl0VSSHfdC05jJyxB86q7V9oICEWI_wQQ-9M3d9lzqxBjq08t2pfvASABP6Fhz3q3QiFgKWAikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcYmAdp7EApUFaHTuFQGmFkFLPv34DvSEvTk-z0H9sCNk4KBv4F6U4Y8CHccTAO9H0GUazEYCbAQk5okRcfKpaHH7uzxYJRyafLIWIhEeu9BB_q9UcCJAAxLtU0h4n8FZ_3hBL_e1UMYYwVd75fKkFuER-k7ZZsXXUen6L9hiU7hx3jojqQHR7oz2-X7TIHXHPefniJtXF5cCDV9P16vTm91W_eJ_0xt_S8bvCRYGv_u76CaJfnaRS9JbVlSqxz-TcOD34D1QTd7Cb1bTb1NgYN9fiPhmXDGgi74feSUiYe23Qz8nWB2YdtP05NJWQCjXLkCq_O8bxV8pYEwdVcCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBX315nTjkYsqLjf9mkqpcoPEN29_x9ubTi9okbi7_ZbPSFMc_b18Gb4UPfI5AQvTETHUUo0A0QXekiX4tjks22kaM-R3dr_4S5A0yEVM9FTT9vA0htkZiIybH5tXuKiOX1wqV2t1uslxkzi0_fgfKZ0cM5md2nPIUr3bwEVDQh_rELpYYqrEI17BdmXug4lfzPTDygTK2n6jY85GS3JNTN2klIRQH7Z1JG5BQriCpFDUZeYltWmI5eYNochujKGuaXVcpsSm8OssoAEUqGosam0Y1Fe6K8wtZtANV0excSqcgAVtWBuD6fVI_6UsUPkib44LNVK1oVa1tQ0uT7z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awiSqefUG_gfEXxgS37KVsF-hWOZuY1oUYLqdFOM6mfCgGOJJF40lC6SENA4GKrsxQr_P2Do5yV2hrK-24za4P4rcoWyN5nW8I6rCvey_gCe_KjhpV4fO-svLuxytV5SPxSkofrmjQGtE9I_MFm5CFZu3PL0SAJN-Ky4m70IGNsnQiruwvQPuTaP2I6AYKNEga3UBABELfNfv7fPXj3IpbJTijcaqu44POwGPyF8O1W5aj0oBQUj-4ZSC0SekaiL-90TeLCEWR4oh91QpVYilCtMD0VtUyvCEYY0hZqFXbFBVbFvZMlVJtDfSSTdIw9UScnHKYN1NRWPRqHvyxuW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAo7A62C2cFQwjGASYy7qq4B7Ve5r356VAlRr2VTLAWP5DV5U-yzw5Xc-9oAH2Y__Ynr-70L4MjlsoQMsNkfHwF5-Y6MLdSX42DNO3WQep2lhh-kixRsWjqepishe0uVh265AHJ5m8JaRM_w9xNWyfrR89j7OdYpFklIZnSx9xHPvuOQqRqzhaJWTC9cooVYrjrheqJYyfGJHCCCDWiKDTKHb6ne0dwpz9gvPCodQAcjp_JflAnZSSMYcP_Bmq62BFwV5H40MAEDyJ9_SHsMfmu9wD0iYxA36_fZ6xrUs-W2cGWO9ktW2hTtOtMZvHpHZD4XWVTJtGTtJpAdlZx1Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غبارروبی مزار شهدای دفاع مقدس در اهواز
عکس:
محمد‌ آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/464205" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464204">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f1971f1.mp4?token=UNW7sQFoF0ZYFK2BTJ_9gymzAGalzx62cRHy37uVpexfN_pAShHzuWWQZeqhK-li1kRw6-nfHoJhyzllrzAoYNMf-wvJsu7xYZz_CR3L6ayDr7jk-w0oeCu-ZbY4qSUBJHz3Be40k_lLUOb9_kS8LeTSaqYbDMeBP5lFN6jgF0airMxTLsBIybHQQw4be3RI6qCf8_YCCuKtYCIRO4sXxB3IE-TaTvcV4SRRIq0qEhAK-s-R3_Qe4oX0An3Yjz5b4SM_4mjiSWKriOlfP91HRj1guuDxS_ZRk_wl8V17FYFdRxLdI8SsF7L_zAyf2czI9SxglAMQMAMxoIlsPag5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f1971f1.mp4?token=UNW7sQFoF0ZYFK2BTJ_9gymzAGalzx62cRHy37uVpexfN_pAShHzuWWQZeqhK-li1kRw6-nfHoJhyzllrzAoYNMf-wvJsu7xYZz_CR3L6ayDr7jk-w0oeCu-ZbY4qSUBJHz3Be40k_lLUOb9_kS8LeTSaqYbDMeBP5lFN6jgF0airMxTLsBIybHQQw4be3RI6qCf8_YCCuKtYCIRO4sXxB3IE-TaTvcV4SRRIq0qEhAK-s-R3_Qe4oX0An3Yjz5b4SM_4mjiSWKriOlfP91HRj1guuDxS_ZRk_wl8V17FYFdRxLdI8SsF7L_zAyf2czI9SxglAMQMAMxoIlsPag5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر خارجهٔ اردن در حاشیهٔ نشست سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/464204" target="_blank">📅 19:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhucCpZ7AkgoN2FtGcGYJnk5i05PML8qhwrl_5GYSyUyubIwVyWUmRtX3n4KHez5KHypTOmR5oLNybLvRv0gNi9laVv1S2UkanF6EBopCQdBjbyxdWKR2adedxoX_GzESpigub7PYOB8d--imKvdva0P1OpxIqCWArBipADFfrTtR9iGyeb50XIudg3ljTVqmFkfaRAOdYTtgaTW9RVWjRn1W8uTZBMKpDsb0FBb8u5UvWCMp8immk17FpxMhzBiX40LAjYGRSY7Hq2FFc1QGCxlpv1WUQgNUvGmaM-_mKoA862SbDG5tdDuxm7hXXWlvfkA0yn8mmcvB3JSoVPSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfryDbfqhFZoz48TzJTbxVoC-oA0Ma_at9yBMXCBwL34ar_RFJG7e5i0c5kBdLul9i9_ivtMSl2mZb4wjmxcG0Jxb29lSScaunqPUs-l47Ztm514BOefX8cisag7Tvt6v3T1Ky1fbE8fzPkep528-wyZ_Pm_K-UE4oVlUyAM2LfdaeyKU6xFlFpmyuObLLoT2Nn8CZh6S4wnvo_trdnIhBlVKHi_9XWSgTuggyAzc68LD8VuI3Eb44tLM-3TrktTKd_9jPokv6U-ln9zcQn7BS4JVc4TDW01cntffbjfBo_uCfTsYq61FcNMY_2Dzx9cOCu8xIOP-vvNO_G3yS4RkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2WXZyFRWnJYvrrQiNoqDAn39eJ4ImPQDIqBuQMHPiPiA2cbx0U-Gnph2z7pmLNlZYTQaOJJXlyCmS6Ao-exb7ZZVi4u27Sdfe3qKWsyo50Hzs_wUo1RrthTZXOGp1L6B9hMMM03eoiVRxyCNUC0LEP7rU1tZUfV0wRjRJCmSIm0LTwIgKRYQnyWSDpqUe0Jv_dGicI2iRAqEmlt5lsWPbt8ycwzT1IVV-eN5W4ecDBKS-z5cNf6TuvjBmSMjU0gK-DnY7HYIQL0zhS_0POO0BBePm0dzSfGonO26r27qNXMWy_PyMzhw844lZn536hOno44xggjqv0Kl3sycuWLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm3irtmvbAbl5PE5ILMm1gMU7CZvw39bODmoER4gAyZIkbmwJdqYCRC4GjT25IdcMA7Q162F0vRZc362EokYGkMNrjeIo5G5u2Z8luLoIIApMk0HlESXYbOTpkoD_aUazrRonka5Y0cBz01959_yfdLqOf-D8nLoww4smMAij2uqZNd_o25nnb_4c1XI_6Cw0wSWs3RbNqDxfEDLrcU2wXQrrEDdP2ZzUcUWS6vfkZJsL-XEdQNfy4FSeKGEoK4oOYdHxZZDRInc8q73zdczZr0MKL952bRR0yvvxwEi2Q3vm9WgkVURN9sP6chOnasC0vqQwrh_kFtbccKmGNdfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/464200" target="_blank">📅 19:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdbJU26H4zKzITXruD5-Kg5dRqyp6FJGMOYEZYu9r_zhmoBoJ0kAqXX5vecrKVnkpDXsYgBXZ6MJmsXoYTP7Ca7b4_mkdf5aFpYvI_iNrtI9pJYd_Hlun40sme4DTbDKWyzbn41efnu3faZwybh-hJc99qrDJ4Ij8Z1rCAsSb1e8t4RrRvXW1Sb-kRjwlaJoeEtGU9--FrxsjgzRkyGHfjMoK391mZ3sijXO916G6EEDEemOO5DFiyq-3IaRE7RC8WNyWUOF89mkt5kdeGAl02RkTO4m7jRt0MoJFImTLHLYSIgXQmJt5kopKcBLpJ2QN-_z1UhSYgQq9aIqCXCqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باز هم مغلوب گربه سیاهش شد
⚽️
ازبکستان ۳ - ۱ ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/464199" target="_blank">📅 19:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sxj8lM1DqOxrfcXL5zBCWUfsHmE0LXZkusI8D8hYK790osSXFx5EOiTEEf1GoHVVt9N9j0tj_5DgbJX_Jems57kLJZZ9T8KB5qi9Cpn8D6964TeyD67bIdTi-J22cfGA22U5McCBEZhilGz6FBcP477Uou7VR_PSOoc039nPwzziUESDmQGhOJ7nCdU6_G3cy5KyXyikUhWVT6ZryNLao9Iso68LfVGV7iaLmrkxXh2Rl-vL9DDYaqMJXIhHukmZ64oTmNOUrbiveI2W3ZaWmlTvua37CGpu3Jgl_S8SEVuX8hbTb9ZNpb6UN7W76JUuST0MwNiacjFKrly-RUYi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با همتای پاکستانی: نقض تفاهم اسلام‌آباد از سوی آمریکا سبب تشدید ناامنی و تنش در منطقه شد و آمریکا مسئول تداوم پیامدهای این وضعیت است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/464198" target="_blank">📅 19:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=c6Z06_I11WzfdGoh1MBVpjzLy-LaMZCmSINzTgB3LlR0ayI9lXfxHX1aRYOUjx9YtuJ4-Pd3WZUbte-EUyBQUDDLieVKfyCNxnBX049b-fxPRSABse87Kh5-zdKKpC3NClDGxKSgzbikUtiSede20q33HQIo_1Be5jLSGGMCdIctpxrMazFLoe2RtNC6andiWJc5C15TjH_6hnpYd1lXHePP_RfMvORFoQvnrkUGLI4wPKYPFyKhu2Q5ZoopTNeawuNME-eXp88HQ_he_M8xsWgAnqoxUJQ639h4jJaIrnOmZ24JWa06pfITkgas1kVau605YTvGcD1dZPpIQB4Ouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=c6Z06_I11WzfdGoh1MBVpjzLy-LaMZCmSINzTgB3LlR0ayI9lXfxHX1aRYOUjx9YtuJ4-Pd3WZUbte-EUyBQUDDLieVKfyCNxnBX049b-fxPRSABse87Kh5-zdKKpC3NClDGxKSgzbikUtiSede20q33HQIo_1Be5jLSGGMCdIctpxrMazFLoe2RtNC6andiWJc5C15TjH_6hnpYd1lXHePP_RfMvORFoQvnrkUGLI4wPKYPFyKhu2Q5ZoopTNeawuNME-eXp88HQ_he_M8xsWgAnqoxUJQ639h4jJaIrnOmZ24JWa06pfITkgas1kVau605YTvGcD1dZPpIQB4Ouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و گفتگوی پزشکیان با نخست وزیر پاکستان  @Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/464197" target="_blank">📅 19:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2-bijeb5NXyCrEZK_6expdgMSE7VwCN7PQslYmrcmatJ2OACkb4S_l6uE6nBqIXWSnvwHpsuh78jzKtL_mws07dpCJqHnlRKIICH7FeAIeiJqZ1CSCnSB14k_L3kxG_u6vKto_wcxteB80NRsMxwinS3nPbvuvvbLPxAmzLiNA__MHhHfJe1gWb9BTHd8JKB_PZ8Gdd-KBMHqSpet2ZLm4k2AHsLiQX68UT4IppDt56tgAg50YJfuqg4rGC68eZzpHM8NlWc0_OGjm8wpRuLuAXvaOnucLZ6qOcNOyiYHeomk82oaH0eSo_I8jqobmjWJ8Pp8LBPN3_kKnM1c_pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو منزوی‌تر از همیشه در سازمان ملل
🔹
فضای سخنرانی‌های انجام‌شده در مجمع عمومی سازمان ملل متحد نشان می‌دهد که استقبالی سردتر از همیشه در انتظار نتانیاهو خواهد بود.
🔹
رهبران جهان در سخنرانی‌های خودشان در مجمع عمومی سازمان ملل حتی پیش از آن‌که هواپیمای نتانیاهو به زمین بنشیند انتقادهای علنی تندی را نثار رژیم صهیونیستی کرده‌اند.
🔹
شهردار نیویورک نیز پیش‌تر او را به بازداشت تهدید کرده بود. علاوه بر این نتایج نظرسنجی‌ها نشان می‌دهد نتانیاهو اکنون دوستان کمتری در هر دو حزب سیاسی در واشنگتن دارد.
🔹
۲ مقام آمریکایی که خواستند نامشان فاش نشود به وال‌استریت‌ژورنال گفته‌اند ترامپ و دوست دیرینه نتانیاهو هم هیچ برنامه‌ای برای دیدار با او ندارد.
🔹
حتی اگر نتانیاهو بخواهد این سفر را رویدادی عادی نشان دهد، صرفِ حضور او در این نشست، تنوع و گستردگی مخالفانش را در کشوری که اسرائیل بیشترین حساب را روی آن باز کرده است، برملا می‌سازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/464196" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119444cb53.mp4?token=EBAhBwoe7L6kttz2CdXp98OWj18DQeHw-zqvo3qXSXWm5iC_kfpDR_3wyRzidUdr4ct9_SawDIv-IQaroLC8nguYUo1M_O7FWiQWgd1vHmGGXz-fEt801sodI3y04A13kmMNQVwxEUy3K-E63qVHj1cZk0IbMW7gEbpF6vythpaLJfaUUYVOrLx6v3v0ORv8F4ToTemEZftes7bH0LnB4M4nzZx1X-HUd89EsloBw95LSm1rj-MQtPA7eKYOTUBWQEh01yOAE8KhDp-FDLmG9AkDi-E75RMQR8hl_9eyTKZTeJzCCrebx_N5fnWaR9fKoJvm_HQxdXqy_wjjDcmxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119444cb53.mp4?token=EBAhBwoe7L6kttz2CdXp98OWj18DQeHw-zqvo3qXSXWm5iC_kfpDR_3wyRzidUdr4ct9_SawDIv-IQaroLC8nguYUo1M_O7FWiQWgd1vHmGGXz-fEt801sodI3y04A13kmMNQVwxEUy3K-E63qVHj1cZk0IbMW7gEbpF6vythpaLJfaUUYVOrLx6v3v0ORv8F4ToTemEZftes7bH0LnB4M4nzZx1X-HUd89EsloBw95LSm1rj-MQtPA7eKYOTUBWQEh01yOAE8KhDp-FDLmG9AkDi-E75RMQR8hl_9eyTKZTeJzCCrebx_N5fnWaR9fKoJvm_HQxdXqy_wjjDcmxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم برای ازبکستان از روی نقطهٔ پنالتی
⚽️
ازبکستان ۲ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464195" target="_blank">📅 19:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464194">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ مجمع عمومی سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/464194" target="_blank">📅 19:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید  @Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/464192" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ycwu1R5x-c0G8WuLJIRDrQUkZ2RN9VDd5zeIpbEbtPviU-Sqi5iWz4675O84n2sVgXjm0Sl-IerwWqJq2LMIvtjaKXpxwAlGTXh6EOzdsR0byicXTELYH2ilm2BbOAB5JklxyLeBbOd_gtsaTkRJK81R30vZf5FhMig39q3cdbTxenhRWkVGxeP-6ABdYjF1e9bFvCjr0HcVMtPAAxeRAzn9NJWKibdewlrxTM-RRnVhL3-rP8P-xWw_5UkLNJj5LlBdL6_pMf-TaQZBjZ8NILzvzbMn0aB18Ep1KrWjNaMY6CUIehZna3Eej7eqRlMM060kWrg_BGcWlmf75_RXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-zSXD5MsbwmWp2qU-p5GYgvLbuCY3YqWE4bh4x4Jbzwwllz3GF1zG-2k5kAFUILISEec5DKvAQiNtGv-IbxxLJYjaZ6JEQpHV2wjdUIjUCfTzPzmMizQuddYyW6JCbCLtQ1DuI3QuwiGAVUrgYH9hTcQj9TVFJRVQLDQXL05WT9Al4J2E91JTbdiVFr7h5vQ-8A-PjhxgMEiRW3GifjDiA8dVwGni9xm3vB6N6slI2vb7XE7mpKzeNCpR162wON194prDaNIS90kx6N1NGECmN50JK7OeGOp2wBUKtJYyvjUpMfgKxSHfL7-4HLceAjXUKYV3n9Q85D52QmW0dMAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور قالیباف در منزل شهیدان خادمی و نصیرزاده
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/464190" target="_blank">📅 18:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی توسط رامین رضائیان در دقیقه ۴۹
⚽️
ازبکستان ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/464189" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464188" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG1bUlHgOtl_W0iTrtESf6U9SbT7UFPDgfNEn-QzeXjgLsgLL1ZKp4LLTOzGsIiE11VvwnY8_WtNvh1EGzYtsW0_oxsm4mWKFTz8JA1CKOL7BtAzppLIMh7B9zjzybX6L-8_3_N48csVqFOpWAqfhcSagyBNRQEl-a1AdEgI-TW3cT01o9lfmJLVrI4XF0Q3zTu0VBO9azPMfQhbOtx99tfI-43Rwff7f6t51ecLIOmmqGfG8EPuUpw2GIKCYrOK4lReuG-A7j6krwwUBUyJSjaDR1Or3DPmOuR8iV5DZQsI3P6odKnDchjwDtpNeZD34texgMeCn2B5CAycdkICTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464187" target="_blank">📅 18:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU0nN_e8X-RNpSawdI9M-PGwuynAFNM8jM7mxnl-a3nIRqWO97YulfG25GJMeBn561RZKFWg9woOEhdNoAGuLctGwpsqZflK6OlZei6SFp04OTaBgabK9xzgnVo7SCtA8r-yQD-hzIF36Q3CPhYGt9c_PhPuNy8vugiqhwgYebVHxBb1kBSCub0jDl6weFdAklVKn6uxcWKDPIVIV3qIAGbd96yDa1HTEOjhj8LYo2NMR7MyGOI5eKdYYRQcLvUF4mLSp_qCbavJ3V14nTNUZsz08FsF7QwplEQrJQbnS6IccZrWWZ6rbeWiPWg893TSQ8Mc1NECoIRLJjb5ZHk7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این عملیات، اتاق‌های عملیات، مراکز فرماندهی و کنترل، انبارهای سلاح و مواضع مهم دیگری را هدف قرار داد.
🔹
مواضع و سکوهای پرتاب موشک در اردوگاه «الدغاغیر» در جیزان را هدف قرار دادیم.
🔹
در این عملیات همچنین چندین پایگاه متعلق به عربستان در منطقه جیزان را هدف قرار دادیم و اصابت‌ها دقیق و مستقیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/464186" target="_blank">📅 18:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3Bj7eZyyEh7cOrkrtpRJF96aIJF8OniWpmeLKRCftKLdSnwS4PZG8H4Pc3fy-no7pGx4r8FCo6KGtXbL6_ScaQB3npDKBc2o3onCPsCVbaHFaa0Z1W77gZC8vy5NS84Yxqe0D4FNt8In7lHBQZAUcuun3YSMf__phEd51osQWtDMQeQQKBA_D95jKLo5J9ghJkVzuez22X8NOpj01zjPfavaMCunV0ybvdIWDsTzMhsufln4tmW2fUQWOBG_9JQh07Pw7abCbSZcv0s34xfnZLH7I9-DZnkUdnLpcJ4V2NrFoJEhyfUMp0p0oc5CUzw7itX53jqYlLiNYN8vk6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان برنامه‌وبودجه: منابع ارزی موردنیاز برای تامین دارو از همان ابتدا توسط بانک مرکزی کنار گذاشته شده و ارز دارو همچنان ترجیحی است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/464185" target="_blank">📅 18:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464184" target="_blank">📅 18:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXdBMoL-g7roi1jAmmYwCoQQb5eTTtMmERGgtmbOlFg0xinTcFmt1uBMLqGn0ZEOyobXf4JXsSirCboP-Ai0QPWPUNw2IadnZEyXKEfmOAGC31-P3582TLJG-fwy1cRzSJIS63dqXrCymXeQxc1aYacco2fKyYjwm4m0BX2U2ekQyQ5ajAIXi9sfomE6fNqP-TobpprHVz4mOB8a2Oo48XItm650DH8Ant1TR9P_vGMuSbAqXedCewKeKAfXtXksqb11YAhf99-cP7rmTWqHg4PiFLGGya6JzcURuCLxxOtJDtMjGWf9gZZfRoCq9_l3Xou7UX5Ef8OuOxSItbX9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TG04C4cEtf72cVcIjDgi9lrx0hZFSlvVuvulIk7EYZU_DnDjGGtd6oPnZa75UlmyXFE5fIt6xgrtSIoDJv1qih-v-er1NPa1l1_M-r-RzjrAZBckmckO6dvdhIAOUrDO5N4HJ48FK3SU35L8UVNtnkHfJCXLU1jVQPv5kM4ocQ5-EvFtUyQKWimDIMNpTgxEs-oHCl6vdyoJu5_gLOx2pu3JK6nJ1_lftJBxolX1ldM-b64SAqp2IHOBGZ7CrfaAMhLICrc5qR-3To1vbi9EqvNHP_bGmlw6VqoY9c_Fl1qiqIu90I1kA1yPy4QxP7PMkHFv6AUj-BVBI5haLQxVlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ مجمع عمومی سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/464182" target="_blank">📅 18:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۸.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/464181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۷.pdf</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/464181" target="_blank">📅 18:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ذخایر نیروگاهی در وضعیت خوبی است
.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/464180" target="_blank">📅 17:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الحشد الشعبی یک طرح تروریستی را در غرب عراق خنثی کرد
🔹
سازمان الحشد الشعبی امروز از خنثی‌سازی یک طرح تروریستی برای حمله به مواضع نظامی در استان الانبار خبر داد.
🔹
این سازمان در بیانیه‌ای خبر داد که یک گروه از تیپ ۵۵، یک مأموریت امنیتی و بازرسی را در محدوده مسئولیت خود در استان الانبار انجام داد؛ این عملیات شامل مناطق بیابانی در جنوب بزرگراه بین‌المللی بود.
🔹
به گفته الحشد، در جریان اجرای این مأموریت و با استفاده از دستگاه‌های کشف مواد به‌جای‌مانده از جنگ، تعدادی گلوله خمپاره و تجهیزات جانبی که برای حمله به پادگان‌ها و مواضع نظامی آماده شده بود، کشف و ضبط شد.
🔹
این سازمان خاطرنشان کرد که مواد ضبط‌شده توسط مراجع ذی‌صلاح مورد رسیدگی قرار گرفت و اقدامات قانونی لازم طبق روال و دستورالعمل‌های مصوب انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/464179" target="_blank">📅 17:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/464178" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDuB93sf_uU-xha5U26dOuVfF_Sm5haMqMrcUCf6Lty4SxoPZeGym4dpfWEORHIXZzUFPW0RXj1VNM3EWhRgK7B---AfC2u49BxQv33ep2vjcnbKpCYgXaJsRYA65peQfKas8cqYzb3rigtnpIh9Y3hMgpRWN3SfpmfDpgKACEUToD-tac-cuBhl3IpURwBs_a4gKcnS1vlXg_wQvaZVieqtXdbQ3KZTOLSP7DGQ46qPtQTgGJOKjkniit_da_xhZfaCf7nOzR9HsTrrHmR4ohRsUjkCpSEuIAsOlDHxtPguk9MfV7Klb7LNZhIchGI6e0tppJzsA1qVv9CfG_kn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXPBeyhQrlol4m4QNYbVnOxCe49DezhBUJmM-n7rn-mCEJNvqdmKbWD58HIgeMEsPwzAIg1hT577Sh7Ys0yyDcwhIM1s5QlEqhqh6gpzqT-bWogkuMzDuA5Vs42LRwRy_IlLC0ia7iv5ciTkancnQ-pm0-CZA8MLeO_0S5jI4uTyJ2tf-1t8zwx-2XlOCnsUiyhgqwaatdTRv_POlTNt_lgHlmATP3png3gBpYjWx-k8VZ9JOLMwiqrd757Toof7z8-tEbgrGc_Xp8fu_D3oOw_Q6F9OH4ONG2SaJaZ26woewggAakINVhXTemHnKRGa3SlU2sZCuOHALZUJWBGG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG9c0IAQg6-3sMOq3WQTd9lSgZEZQrEojwYc_z-w5K4Nzlm5s-ZI0q4hx5tl47uIhfMwetm9LM67Yy6MENPNelwpNuksYgDUnu6voqui8r06P03r-0-c8jDaql-z1qnzlFb_OysbAIL7DVT_6Rve5rCzPMnBsxcUsYhQ_8Gy3k8BM5rAIrL3FAxjoW5xW1h1HNYZCw07wquQ2ONCdk1oK0e56No4k3VGYemFSx6d6U4f03papwcYaQRsvHwMLyWi1AlKhF8rHWEyj2A6yP7MwmQnu3v9Z0exw3RL5uGcCmYOx2DVA88p4URGD9WQs6Unyf5iVXwqrZK1kC7zTpAeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqeOHrWGRIPJCw7KwyqzQBqmd7ITyUesDUKHqofzLqjj-E4SsW1cq3cixLl1i4hzpEPcFf1YWnPjSJROv7cM2yfFf3NW3a-8hObP8MwRoxniPWPWYQVJjzrIbHNxHDkJswIl5sLPeTvsoqQtj_gIm9wiRQFGP3UuDspKrA9JH3BdgN6L_qSPq2dcqQtX9vya2pou5FLdVBrrNDj2NEkEH9XG9YK-2kDwo8-t1fNMUq0_7vrOR5PMRVkYTN-kno7vGLn6TFuD7aDBhPWC0yNT4Ru_fWW347EZoXD6OuxakwiCBgmaf-8cZhBp-wds7I-kNUH04zNiB0rQkkDP7Yv65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_JTluAu0Piq3m2FIdSl7TxK3x6EQYKIasL610W39mkkuEsnAYSIvsoHYNdEphhfXYLiTwcRO1x59Ggsz4Ejfbc4KMqPfRnrxinj-4DCLwdwJcDn4jhG0LDgK9TsDYfce0uarbnwMz6E_SJdlrYyWUnMaJQVZ89n28VuCCVAfytvTdGxFCObpkMQEDpC8fyb4kZrZo1MgKCRYOXGWAvIXPR9v-7KjL0lTxSgfpStpsk5mbn4kjjpM3YM4rrTs3dM_KmgiGj59ujIrePAKRfM4rZYP_4-RKED3TwNsOZ3xLMxPeGwMbF9f2JyNjfNL39WhVCKBKyuVlSYda9f-PT_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tG_sHeyR63R_VQwjLNt234PYYsuRaFfAxvriN3BS4_CAKSIoGJG25ZsGEPjsdK0hZZqIiEEfo5FEjt08hC-bgCa6QdzPqk-CiYdQfU6Kjz8OBY_3iGUw_cIuR1T-z2AjfS4jSXEAUpcN-FdUNKOWFilov0tc_mFQZXXRHS9NZ8QOvlm7DJx0kZ9iFu2syvfaJX_VJ3CVZe1kyhMQvSibU396BEREqQpNd5WotJ9W_G-XAK-kxr_Bv2VItxKsd23aP5ERJ64i8TQvxaJQayxbFGCxY3S_F6YhrjwaKewOP6NJGkdhbhXsR3M_AbLv1gNobQkDp5aauE3QOcf0fDUdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKGs_SHGDa8Ol3p2XeoRLK26DOkBcSLBRy-1O_BguUBYNJSjLljJvZMa0KVAKnUp30doySu10B3Av5kK9qr_EGhcAVvxEBDqXtobLbP8JSonfJp508S4m2FQ7KkBwB2vOaSYwtfyRv3GnzFLSNxJBNK5YTc30rFMHPNwB8NNdgpY16JmdBJi7ZsAkcCLZw9AiJQ8S2Sah_vwKS8ED_dEeSZdVArcw6zPWlfohfp_FJZPszTTGEWbYYdiKQgQL_PzIwbiXdZNdsu0SrPt0t-TI9SBTl8_TB8f-ACuulC-Qw2tZFJn0DuZAlzW9QDlITqgG7h6VxbG8MdUXF1omH4Vzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات کشتی آزاد خردسالان در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464171" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh8D6DwtWbbFayzZrJvpVTghqtU23cScwOjb_KCwd2j0Xa-Kn06vvj9EFdGEskGOYdl-1c00pEWfmgUPNq9dhwd8MC_GLXu7N20-qpO3h0EDbOdA4IJYuETfErDs0tYQSmvmMMljh6xEsJ5FDbMU4lxeWXYS4YV3bQXseagjH_-v2MMc6urdiwJQJDwWWPkVDlhoCatPIY5FxqIkz_jGgMktBr0Z0YOwoxMhGwaHyPuaftWJlyd8Gh2Md9vDTHgFcG9XQ3_ZKfT7-pN-P87Zd2aZIao0f91P03RkCyS_Mu2rgtjB0F0msN_09P6GimqMcYB-z9k1jaRc8RlhWexPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کوله‌ات را کامل بچین»؛ پیشنهادهای ویژه همراه اول برای شروع سال تحصیلی
🔹
همراه اول همزمان با آغاز سال تحصیلی ۱۴۰۵، کمپین «کوله‌ات را کامل بچین» را با مجموعه‌ای از خدمات ارتباطی، آموزشی و دیجیتال برای دانش‌آموزان، دانشجویان، والدین، معلمان و اساتید اجرا کرده است.
🔹
این پیشنهادها در سه مسیر «وصل شو»، «مجهز شو» و «مسیرت رو بساز» ارائه می‌شوند، از سیم‌کارت‌ها و بسته‌های ویژه اینترنت و مکالمه گرفته تا تخفیف خرید مودم 5G و 4G، گوشی‌های به‌صرفه و فضای ذخیره‌سازی ابری.
🔹
در بخش آموزشی نیز تخفیف‌هایی برای «آکادمی همراه»، «فیدی پلاس»، «آی‌نو»، «چی‌بخونم»، رویداد «کی‌بُرد» و پلتفرم «کدیکا» در نظر گرفته شده است.
🔹
در پایان کمپین نیز از میان خریداران قرعه‌کشی می‌شود و ۱۰ نفر هر کدام کمک‌هزینه خرید لپ‌تاپ دریافت می‌کنند؛ هر ۱۰ هزار تومان خرید نیز یک امتیاز قرعه‌کشی دارد.
http://mci.ir/-GHNE9B
@mcinews</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/464170" target="_blank">📅 17:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udLAj9uw1xAOvJWgThMsAfKlTz0nzcb4PCCZUX2e50iPj9NXo7aUe-MdK5tYu6hTs0GphXHN5cgA_0QNWg1UHJka30Kh3LlyaJS5NG5biTXMiU439wEoEectP2tVsIzz9fzP7KqWwNth_Y-DjfzreYVozntEmJvfY4NhpKxqXa2U5v03zg1w5SLjXTwyB_HQ_-y1Uab6LUaxIlEOJNSwqbf0cV9zJ35uL8LjUxEsbzHB9RnO7JZmkQKreMmqCVdhwtjtBhwaMVMJGASaROFM4Qk0ZHcacn5RAjYARhvBiuByAfjBZ8uzZxr-nIyt3J244NfV2zbltBMmiCWGSznoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1XJopN10jgS-x0KYN2E5kGhMJU5SlPhWnEZVAv8AggdoDEEdqvPd0DjCZqI6wI3XepuG-Hyjb4P--Zh1HvFfQxk8vq9oS24WBhQvvJS92aQuZxZIZh_Av5jxgZZ5l8VVFKn0e5Qq51KPCuJsUUdyzh5DujFPQKI-O6T7P6j0pxPLA1rczDuyFoS1YNZlz0FuC-51CnSAogAx0czkxkdA2DDCO5f4RTmfwisdVG0_vltPERBGMEIjSTDaxBCLONA7RBgfVzw3FpJq8PllodmT0eLBqX61MrqTW3M0dZlmCFYgcA6tFuE7iw7aodJzS34OKWMEWHm4RGsqnVIxkAQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh6M6qBdo08ggHbBGYiSCp6hXSqXDmtDunc1K7Nqu3HIMc86tqcyz1sG88S8x043lWckk5Ox6UAqRufz0RNj7b5hU-62oeggNeM6JSyiBRxpxlHaOkywh8jvURFZezjiGO31_VaDwu8fXoNHJVVMVAfYjceC8ySfqgkJNoyUMW6tw0Tde7_hLzIQEOqfJrK07GErEEdgNWJgKBnq3uskYK-MLiUvWa4kDn2Buf2-neBFppzlzZ90RY2Bs5izyefdGK-MsgDDNCC5J3Rn0Z8Kc_4m1N1Pl47XMWi1V6qRlPT_LFxqr6nZ-iSzHe04zIxX8ue98hlM8BBBf8q2ADoI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-TH02axlFNOanvoH5g_90qRfExaRM-jdb6wj9vwbNcwdEbrm5CZPbot9NwiVoTEmcofd08EIlMUOjGleFyVvMz1r6dLYoDFUjtLEgZTJdk9gvkEtocoV-EriWOdIVdl--0K3_27un5XtCn4PDIHXo7UfRjs9qRzb3IwE4siZrhEDU7kcrznV-fbQxUG6Y9ES9oiqlW8Lk1e8qP1_hqtUH4bySzKyhz622s4LEHsxZYK8G-wYAul-Osa5nUH9XvKrbMN-yjHG6S_vOkP-AsyC00Wdtq6ZzEegPYwbzUvAnGwI8HSbkpJmTIUAc9a4SaWPI7zBtO5FUISkzeri3Hq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUd_9xdrFyi45DN3jIZEjyneGWDH1NY7VxfjWptSqBConrxpD2f1ZHJ2G6S9_OHBNYLtSlDIUTY9xsyuvYnHzR-L6CnZvS481t24PT4Ihiw2T-HWld5Wavq77Pk-sSmWeD-JZOITZ7daeLDHmUqizYCZocCjCjkzr-I2WNSzUWctnmZ1h2xkA2oJMHS2_4NSkqrkI-FlqWdBrRqWT5awTbyE0liwkMks9ymj4tDFFtZrKxlbgujhurb0C44uAtAG47Myp2la66ck0vQ3yvt07UmxDIuQOJ7YBiq9vpgZuMv195joxUnUGG7kGNWzktMHwv88MZHZn7mMWrGhEWbgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oym_pbplSDeDip9mVjBARbemtzp2s5WNEFoCYg8YqEJas73TkXoueGU0LXjnaFD42yyOChA4qek5RNY1jDfCsX6tjmZyJ-s74B5uG3xnP7AGzfllbCdRoxmHzsRT24Z9baVC7X0lROQ8-rkmGt7J2OalKoTgmDCOsC5wtAaqm9f7S7qUkw8aSepa6D492DvVH0JD6qiRQdM4I0ald2qx51T_n0lMQaJ6A2rgwnl7Bp1g4Bm0ZvI4Zfo6Vl19ZZ-uZ7Hb7wHJQHF8xQhTRS9cUkIFLJxiMUACGKPRYZ2pBlA20NKqoErydhQU1nbgX90egLpzrniRGPsrpm3ndIjWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nicfMOM-mYdcFTedsF9wdM3qc1-JeoTLwPLWpB92AHTN8shRKWh9ZXIHM0ldPEB_DyBac0eul3p2ySa1SNf6A6UCUhzpTT-xgJuVYcH93XJkHvb8qRSLPp3w3ts36ONgYvPlW-ierbpmpyBOcixLV54ot0niXJ_g0bV392ObNIRqXnpZDMhA9Rz0VCbcbZjt3qub47FfmgO50Oj4q_lwaCSShCfGq-FKDOeHhin0hFTLEwinoO0dXaa2V8rHkIMRZ29Cl0GQFfXkOYF367ePsFApkdghv-fyTeSeIffutxgy0Xx9D2BfLqfpu0AVjfRy2dbUzoGrU-hBWoEadJ787g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHNNdxJLKvOU4cDopMR1UCgA96W4x_uOIIQi7fobKU58AIo-uiDbTK5-3hVGM6huWeta_dOMzivuvceTU7kdOH5mfRKuNe_lStRJkXm8HXJTSA1gW7DlMQWGIbnMc3fuhiWXeAbRK0P862t4rp_1LRfsUPAmYDgo5y1gHNVunQY56RASVg-8UjT7MSdTqh3g1_32i8oXxtow96QuO073tAAJZHBXm8pxkQ2YfqwdozX8io2C538TXVJsmIZfzPnD4Y50x7BIZ8etrgQfgEvRBI5rdskfD9CeUZ0S4autQS9cekhnMlQ3E0OQwCuwYQe1vIyJs854wpoNTy5Wm1PzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔰
فرش قرمز مترو برای دانش‌آموزان
🔻
به یاد دانش‌آموزان شهید مدرسه میناب
➕
@metro_farhang</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/464162" target="_blank">📅 17:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/464161" target="_blank">📅 17:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464160">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b9af8605.mp4?token=Em6rq8ceRPtUBS3fQCr6Xb2CZtRa55rrmBn374Iu36cCi-k9SeBb8LeUFizI9TylTUX7Zcb-WTYVftrRDec-GJ1ntdadAuC1nwTzQpmlGRiJgBVuM7KU0CEsqKpqVXYvjx2ky9UAQBXJaQKDO6fcSHKwI26Ryh46NZ-zHCXCm7Hlj1aBUztitGXZF5if236R4_36e8bE1TJ5SCD-MRt1L2cMySwhWclkRxBjeVFmdHnWx6MndohRhLEXy-AmcLc1DSEC7jUxY3Xr-dK4rCsBCaRtq9a6v4LuOaY-FNlrN3yCijn2o6YRjZyOqUzAclLeFdvegudsr993CB_REC1Ilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b9af8605.mp4?token=Em6rq8ceRPtUBS3fQCr6Xb2CZtRa55rrmBn374Iu36cCi-k9SeBb8LeUFizI9TylTUX7Zcb-WTYVftrRDec-GJ1ntdadAuC1nwTzQpmlGRiJgBVuM7KU0CEsqKpqVXYvjx2ky9UAQBXJaQKDO6fcSHKwI26Ryh46NZ-zHCXCm7Hlj1aBUztitGXZF5if236R4_36e8bE1TJ5SCD-MRt1L2cMySwhWclkRxBjeVFmdHnWx6MndohRhLEXy-AmcLc1DSEC7jUxY3Xr-dK4rCsBCaRtq9a6v4LuOaY-FNlrN3yCijn2o6YRjZyOqUzAclLeFdvegudsr993CB_REC1Ilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین حضور فیکس درگاهی ترکیب تیم ملی ایران مقابل ازبکستان
⚽️
بازی تدارکاتی
⏰
ساعت ۱۷:۳۰  @Sportfars</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/464160" target="_blank">📅 17:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blyspS5RvVS28FfBn19hf9EwlxMJ9Hl91kp1kAGbLsXXBelSjFWfi_5MlYsHaNm9UyhWLAQYaoLwEVEhiuTC180QaBwr4WNnyCpwUJE10RrBmcawSQgPP3IODd9NiRnjbCFcPVMGb1WO7KBI7C5P61g0tX4C_HwV6uFof9ZgGmCR6pASQ0znpc2TXXWoWDXv9uSkTkweDQL26Y_LWigPLkHSRzgi2Ry3hURVoD85qGrnyt2xk7PY5zyhTSwq_c4UPdp7HY29-NCj2ybklWUzr7dR8qOvRESw1WfwRWHAR342UKGLVE_Iym_jSDJ0dcefEYQGQCG9ZModibcKP07iZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIY-JBQV_kViLM6YPuBu2uWp1l9gXorTol9yPSyftNFwo7Ne2U_rFUZbDlJHxT5pzPNTzBzL7CyGbafz3Ywzx5MjtoPWoyBTtBz52G3wu5D4mr18d-7F_ubvLUTStKFw3a-l85Vao0mcMJZbYjHUZ0Sxn9E2nWuWbo_2QKWVhOrWR6GmRgbhqpMlMux9ZTQaYlNyAAAfuTloB1KISrX_3-1h2BHBVQZhpfOgu4Z0CFc9C-KZkE11078wPl53SWpIte84KRuf7oAkzaqRJwKc36CdBAMmJYlYruNA6sVBtNwsnpMezZJmw7aN3_jFq1c1s71AI-4HucxcE1cDoPH_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR_YbSUR0x4Qq3uC26q-7cncZjxSDRTCFZdmthp9iQqapKS6kTYPwp08DBdoUVlxtyI2CMthsJfX0e_Yee47dnFYOtph9Qnw7E6okH126oVvU9z-dmXLgM-VkIyQtjMmdVkoZJ8pDr6nbNOeJWpR-twHzg-RgRhKlQ3i5B6w7wSljPHB1wKzyEHDzriI4Qb235VsX5WBFYz3Y9mLnaNvHV1PRTDbep2FEbsPHcsDSE7HsVcIZ931SvYKqBJ8h1FtEE9gpBQ76xLwPJn7Pn6pC5_jBECJY-ZRAbmHPhNGBJP4x1GWS18VPhCZ8a-hOlmIYPfR0w8kA9Q1dGnRkZbzsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار مدیران ارشد رسانه‌های آمریکایی با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/464157" target="_blank">📅 17:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1520ab7287.mp4?token=X-8fEOtO8r1q8xmQOMIcFnvPDXydnL4aGC-Iokt3Y5c9LTHxtzWwNUXBMcTQjHjWDzKdPHx3q5EpHa5rip1sEzsqlcbmzsFr1e6I-VQmLSqOjXa8_sbE31Z2QQLG2vCjqoT8_xnOg7e2NI2UJu7R3IU8g4w6KvjHNi2dFg2g9NXTNhXCp54RFluMdBwE3G_13WwdiJyEO5Pn0dFKGlb5ImeV4PK6N0rx7RiU5cmTZBi2IQDByKkho44qGOL50vSaRIDGvg31kLspvGjFX3y1llZT-B7NY_2661Pun0ARluR2AkKmtQJXHhML-lbmnnuT94JYtBMIKU8_FyechnC8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1520ab7287.mp4?token=X-8fEOtO8r1q8xmQOMIcFnvPDXydnL4aGC-Iokt3Y5c9LTHxtzWwNUXBMcTQjHjWDzKdPHx3q5EpHa5rip1sEzsqlcbmzsFr1e6I-VQmLSqOjXa8_sbE31Z2QQLG2vCjqoT8_xnOg7e2NI2UJu7R3IU8g4w6KvjHNi2dFg2g9NXTNhXCp54RFluMdBwE3G_13WwdiJyEO5Pn0dFKGlb5ImeV4PK6N0rx7RiU5cmTZBi2IQDByKkho44qGOL50vSaRIDGvg31kLspvGjFX3y1llZT-B7NY_2661Pun0ARluR2AkKmtQJXHhML-lbmnnuT94JYtBMIKU8_FyechnC8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی رئیس‌جمهور: پیگیر پروندهٔ دانش‌آموزان میناب در مجامع بین‌المللی هستیم
.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/464156" target="_blank">📅 17:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
۲۵ هزار بستهٔ تحصیلی به دانش‌آموزان مناطق ساحلی جنوب کشور اهدا شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/464155" target="_blank">📅 17:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b4f1e70.mp4?token=PJNGVpwvEYzaqXnlYK6h-hPMcZav-H76zjY06T55MlJklYtMXt0ildItPup9vvVF1ndxVPrQi8lBJQmycKkG1F_U36_c2b-I8RU2k_onm8bw9JCxY3TQ-eB6LCqPMz3mL8lhIj7b3c6BUwFRKxUCK15fL-5JwZoD5vEdUoS1bVFTtAVUY30SPowADCyTURisXCH0o58WfeWvr6CZZxIFPJzW4jThzVLSJ3A_Bfc71laFqX_EdF3nb-CKcalyJDMMo-HNsfxnmQjV2_CDJW7hTOzmX2Z9Y4e8CkYqLA2-pXYvD7uYqF0gWd4Pb0sk6r7sVfEOjEpM9ew7f-UxX7lwUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b4f1e70.mp4?token=PJNGVpwvEYzaqXnlYK6h-hPMcZav-H76zjY06T55MlJklYtMXt0ildItPup9vvVF1ndxVPrQi8lBJQmycKkG1F_U36_c2b-I8RU2k_onm8bw9JCxY3TQ-eB6LCqPMz3mL8lhIj7b3c6BUwFRKxUCK15fL-5JwZoD5vEdUoS1bVFTtAVUY30SPowADCyTURisXCH0o58WfeWvr6CZZxIFPJzW4jThzVLSJ3A_Bfc71laFqX_EdF3nb-CKcalyJDMMo-HNsfxnmQjV2_CDJW7hTOzmX2Z9Y4e8CkYqLA2-pXYvD7uYqF0gWd4Pb0sk6r7sVfEOjEpM9ew7f-UxX7lwUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر خارجهٔ لهستان در حاشیهٔ نشست سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/464154" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba0NqpydoXxurPUAiXPmRH5Ei0RX-BWjZtxn-ouHeXzisFgcBCAhwJ5S7Ejh4nSic-wSuuOJ5hjn3w5K-zm6USBBETXcr5kvOZThfUvzgu_O3Chn24I3ZgF3hGGetTuY-zPRjRPxPXx1uRTmAU6V3TK6BhNY2RYfiWnpM_lHBrqU7AlI_I4ednf5BOa2_WO7TdnIaHf6JXLFUcF_aBXnpFCE-2gjBrjSgOB_NJjER7YW1jwP0xHs4G6G7YPBQF41c75y6TONRkt24iTRYwJWrAg9CSvEVhrWxD_FlrsHPIGmEb85hEo_-Bgd3Jj2A84SiosOSbvp5WKqhSJAjeM9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: پیوند تنگۀ هرمز و باب‌المندب صحنۀ جنگ را تغییر می‌دهد
🔹
دستیار و مشاور عالی فرمانده معظم کل قوا: جنبش انصارالله، خود دارای اهداف و استراتژی است و خودشان در زمینه تولید سلاح به پیشرفت‌های بسیار خوبی دست یافته‌اند.
🔹
من فکر می‌کنم که پیوند خلیج فارس و دریای سرخ، تنگۀ هرمز و تنگۀ باب‌المندب صحنه جنگ را تغییر خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/464153" target="_blank">📅 16:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgQflT7Q1M4ZMTRXwgnjZZ7v8_6e5oBi8n_LkU9V-Vti3t96Izb1EaLkQ-mWC938txwLha8qknt40QKsY3ulEyPzz8iK8SFgOUyicp2o_w-3TuTeTX6kG2VYgTrUENZqojHYo06vBXyFI297_IBMfQEJLWTe9KxBgg-pi3Mw1rWz-iROIorqy1VL0Eoq6crpSBciUur4EkUx_ZyZWJ0SavTjpDKBLJUIZJ03cReqSnWKT5XorBAOZGtJ5HVBO6kmNIF-loJxgjIn2W77CJn4c2S8tcwgd9cIgDX5QCoBbTFe5l01Tlt9hlCUVEeJwQ_Qsof8dfHtaI9ZLxPyRjwKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: مواضع صریح و انقلابی رئیس‌جمهور فریاد ملت مظلوم و مقتدر ایران بود. @Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/464152" target="_blank">📅 16:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaab1592a.mp4?token=s_OW94wVxFHPEQAwGWAU07hUv2pfb2EGE_vrYvkLDPgZ_pbyjxbplNEsQ1TMFdecES6g3RXlmhghr-XLb2-p6rP6cH76_QqrXma6OGzC_VH9Z_M98nkDLpYOHQdCGBMKHEnVyIfnTNM08l81oosv-yGhwKzTQ_JNS94PGOQmhECm-THgGKW1VezWzMeIDRBNu6PpcXRiPJYfEfBMIteA7P_-Ao0PzDMls5hFfLGtN3AiQYWGnufG0wNFyIZPsRxCVtWKQUCH8IWpX4orGV7JMSNE5_Q5v7MEB4_jqfuTWNIaOFCKkvmu-1JILD1u0PWKpHxj8dtKZLETxIqxmFqapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaab1592a.mp4?token=s_OW94wVxFHPEQAwGWAU07hUv2pfb2EGE_vrYvkLDPgZ_pbyjxbplNEsQ1TMFdecES6g3RXlmhghr-XLb2-p6rP6cH76_QqrXma6OGzC_VH9Z_M98nkDLpYOHQdCGBMKHEnVyIfnTNM08l81oosv-yGhwKzTQ_JNS94PGOQmhECm-THgGKW1VezWzMeIDRBNu6PpcXRiPJYfEfBMIteA7P_-Ao0PzDMls5hFfLGtN3AiQYWGnufG0wNFyIZPsRxCVtWKQUCH8IWpX4orGV7JMSNE5_Q5v7MEB4_jqfuTWNIaOFCKkvmu-1JILD1u0PWKpHxj8dtKZLETxIqxmFqapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیسک صمیمی برنزی شد
🔹
در رقابت‌های پرتاب دیسک بازی‌های آسیایی ناگویا، صادق صمیمی با قرار گرفتن در جایگاه سوم، مدال برنز این ماده را از آن خود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464151" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVvBgZ7B9b5SIqsXnGU4Z4cV5XwKMtuPK9qBpkOunPPLSUd3unD94nd4wpOcwrTXancUJg-prv1JLbMeTt593XwwQyJz7bxe4Kex50a5pXTaNzzXjGksn0rDU8qrqLTKhR59T_8lDMTv_8IyuD0B0_5rf-BQmFn9GdXJ7bEfmgqEArgX5PRWbxNA4iRYnQQ0mRe9y2auYzaa7PVVuRZyY-b7n-UZ6Dy6hJUkgyTL8aW9pQkv1guNe2JPIxDxHallCghZ3LE1rBSp12F40_-8IY5LnBiXKJjnkjc6_i-vvs0kWcLEMYLE3fudxI5clMjBoK2VktanRqYv6ai9cYRRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین حضور فیکس درگاهی
ترکیب تیم ملی ایران مقابل ازبکستان
⚽️
بازی تدارکاتی
⏰
ساعت ۱۷:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/464150" target="_blank">📅 16:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eceb316f61.mp4?token=ISJzBotqNxWVsVU5iFw0XLY96Doz7IuPJ-GPUDRxX2utPxNFOVLn3EEhT_GNgUxERVDH-3WWj_27PWnaH2-Lo1X2zeeBJ1ThoGEBeninzk5uEiAU28Xr-PaDRRyhFeYcZAwh2s_fnLuAjqYIDzbXYiTi3xwOscCy_vPjb3uF8H6tGj3KaDB7O4A1G6UOanpk104QZFYn9P7eJhoSLCKnJRGX-LOfkTAb1nI0uEqaSUoW4q375h8uYbzwN65kBwftiwu4hMi5Q-ft3Wl_-WIyylcUz0SsqAmsCxsaGfTe9HazEtNPu9_mFgH4h2--Qp6s8-9QBKSSp4IFK7fkshZyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eceb316f61.mp4?token=ISJzBotqNxWVsVU5iFw0XLY96Doz7IuPJ-GPUDRxX2utPxNFOVLn3EEhT_GNgUxERVDH-3WWj_27PWnaH2-Lo1X2zeeBJ1ThoGEBeninzk5uEiAU28Xr-PaDRRyhFeYcZAwh2s_fnLuAjqYIDzbXYiTi3xwOscCy_vPjb3uF8H6tGj3KaDB7O4A1G6UOanpk104QZFYn9P7eJhoSLCKnJRGX-LOfkTAb1nI0uEqaSUoW4q375h8uYbzwN65kBwftiwu4hMi5Q-ft3Wl_-WIyylcUz0SsqAmsCxsaGfTe9HazEtNPu9_mFgH4h2--Qp6s8-9QBKSSp4IFK7fkshZyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی پرشور آهنگران در جوار مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464149" target="_blank">📅 16:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e579a8978.mp4?token=C5S-rUPgT-wSGWdnxL9m-VtDMH1dRWHt1P44G_1gm6OxL_UkiXMFUITR0RnuepjI4BowpHMye3Rf_k5m3JQkx_A817jDXhrLy5UEsMvR5ePNvVPJVWZ3lCk9vOVTHhGayGPquVStzB-QArp0zkxNTNWgMCPWrmPchD25xLxVqXQOTYrpLl8UvMzEpydGbYlBt1ZFuDPR2fgYwi-Sd1SMbFdeDAPxMgs5ch7-jbk9evaLNFhx5MLKNT_PQUMWZe_FVMpJRU-WD5A2sPKfHgSvrP_2gTdMtAgOKGJn9GmGKZnGsyw-rmr3YfV9yS_wTBOr0ABLbO6nOf41FCrKjStNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e579a8978.mp4?token=C5S-rUPgT-wSGWdnxL9m-VtDMH1dRWHt1P44G_1gm6OxL_UkiXMFUITR0RnuepjI4BowpHMye3Rf_k5m3JQkx_A817jDXhrLy5UEsMvR5ePNvVPJVWZ3lCk9vOVTHhGayGPquVStzB-QArp0zkxNTNWgMCPWrmPchD25xLxVqXQOTYrpLl8UvMzEpydGbYlBt1ZFuDPR2fgYwi-Sd1SMbFdeDAPxMgs5ch7-jbk9evaLNFhx5MLKNT_PQUMWZe_FVMpJRU-WD5A2sPKfHgSvrP_2gTdMtAgOKGJn9GmGKZnGsyw-rmr3YfV9yS_wTBOr0ABLbO6nOf41FCrKjStNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ورزش: وام ازدواج برای سال آینده افزایش پیدا می‌کند
.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/464148" target="_blank">📅 16:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7lGga5MK-Eot6tFbrYDbBkAF0Zs_w-jss95R6oxyDl2ti2j4bIqrzWNzqOlsozz1r44IVtbrZZBnL5vOKLPQBFGqOvvj8W1Y9gZ95dsxr2mLYUzcItNuC9oz9tPQCarafq_EpIZjybWj_iExlZSjpAs1omClRrQHvurVqLJ0jB9itlxmA9XhNE0RENZvXzIH6gRYlwD24bvIQ7p8W4hksRzbMPAP4I3_dzGKTTVwA6Dgsh0rkvP3RmXV02ReIBSM6uqiTeRhcOdDIfKPnERxDSZOdvdpYX7zteUSMx8kspoxEKP7WvtBcXIPfVc34Dl6PJpzVt7P9NA5jESGM-Qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نگاه دنیا به یک سخنرانی
🔹
سخنرانی دیشب رئیس‌جمهور در سازمان ملل بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت. @Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/464147" target="_blank">📅 16:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5f6d18f4.mp4?token=Ygn_OFds4zmGq2ZvGRt7hq0MyCJc_qa73e_vPb_AVz2HwgGtJyPUFU_Zr1qjFrGkZsSxQ9TamuwM4PyV9x0BYaQ4QzLdoSNWHAD3HCMPsOqk1IvP6GOO2xrcFffSNtTMewHmrKl_QVhUe7fnozYzzyh1-kgzoRhPgwbNpTyg0X3EqqN91_IyJsXvgkAG1ajc9mdvtybwa88sZR63o_k99UR6Xa6eNmEiP1f-tUDvgLBbbex9NfheU5WUSKVZXsG3wuVcymbC7mDlc1JrBvUlycbEPuazDnDXSJxanVGYII8yr_Xp6LjNe8vF0IqTPWHTHAQzyLkk0pgw46qvLBFfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5f6d18f4.mp4?token=Ygn_OFds4zmGq2ZvGRt7hq0MyCJc_qa73e_vPb_AVz2HwgGtJyPUFU_Zr1qjFrGkZsSxQ9TamuwM4PyV9x0BYaQ4QzLdoSNWHAD3HCMPsOqk1IvP6GOO2xrcFffSNtTMewHmrKl_QVhUe7fnozYzzyh1-kgzoRhPgwbNpTyg0X3EqqN91_IyJsXvgkAG1ajc9mdvtybwa88sZR63o_k99UR6Xa6eNmEiP1f-tUDvgLBbbex9NfheU5WUSKVZXsG3wuVcymbC7mDlc1JrBvUlycbEPuazDnDXSJxanVGYII8yr_Xp6LjNe8vF0IqTPWHTHAQzyLkk0pgw46qvLBFfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای: تعیین تکلیف فساد تراستی‌ها و غیرتراستی‌ها اولویت جدی قوه‌قضاییه است
🔹
یکی از گلوگاه‌های فساد، می‌تواند موضوع ارزهای حاصل از صادرات باشد؛ ما طی مدت اخیر بر این مقوله متمرکز شده‌ایم؛ اعم از تراستی‌ها و غیرتراستی‌ها. تعیین تکلیف این موضوع یک اولویت جدی…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/464146" target="_blank">📅 16:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a160901.mp4?token=oGB8ylEmaL2bCvm2D_PXmzCMHH10NTq3JYUqFSxbfzpFfMpiQAohlHapdhoVdaE38th51UZHLXiaCJZL0VDMI1dgnODfajOtAHBYRqo1XZxJZxxcV_ZUfG-d2ForxfzeIGdpJSyZnafGRA7RauL0NnaVE92Fj5b_xPVMsbSxWJ7ysQ_pJxQx3nOOguHXUUW880ZfNSv-I3bBWrQWs4YhIv-knB8z7OS2AVZUpshccgNA0NTU3mqDvhw_CKhVT92oKOROt2hnag7CngdXSB4XO_XNq_PHFEcw4i-HitxGGuwz5PSlegVlrpfrozVmi-PUpIlPZUZ77PlBu_pcmHywEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a160901.mp4?token=oGB8ylEmaL2bCvm2D_PXmzCMHH10NTq3JYUqFSxbfzpFfMpiQAohlHapdhoVdaE38th51UZHLXiaCJZL0VDMI1dgnODfajOtAHBYRqo1XZxJZxxcV_ZUfG-d2ForxfzeIGdpJSyZnafGRA7RauL0NnaVE92Fj5b_xPVMsbSxWJ7ysQ_pJxQx3nOOguHXUUW880ZfNSv-I3bBWrQWs4YhIv-knB8z7OS2AVZUpshccgNA0NTU3mqDvhw_CKhVT92oKOROt2hnag7CngdXSB4XO_XNq_PHFEcw4i-HitxGGuwz5PSlegVlrpfrozVmi-PUpIlPZUZ77PlBu_pcmHywEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار ایرانیان در خلیج فارس؛ از شهید مهدی تا تنگسیری
🔹
نظم و ترتیبات ایرانی در خلیج فارس و تنگۀ هرمز نشان از اقتدار ایرانیان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/464145" target="_blank">📅 15:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a88122ab7.mp4?token=olBKPKq5KOLKvBbvYfkCWY3p3eRJqb_PHbC5A79ofIJQIPCIkGQovlBmSNRjXVZbgAynEoe499ADtpOxIUeQdKUM-0r_9ndSqGW3q3TeBG-MJZknaTqAwyl4bV-80V3NLxcJ2e0fnRMMJ7VKuC0btPA9xffGtVSWUOqgDfHsVgNw4Aj9_wx5zvqH6taBSYtrR2QCh2uHvEU_Ep_hfIEn-MBtp8qyKEjr4pzpgHCEsLlHZWzjBxOO-kccgF5SBOqWefdXfrJwkvp8ZdRPRyosJqWQlrqwetQj1aPulPw2Wqn8-Ce_K83njVMF0dAoFwzlLFE7WcLlgfBDg5t5KSS2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a88122ab7.mp4?token=olBKPKq5KOLKvBbvYfkCWY3p3eRJqb_PHbC5A79ofIJQIPCIkGQovlBmSNRjXVZbgAynEoe499ADtpOxIUeQdKUM-0r_9ndSqGW3q3TeBG-MJZknaTqAwyl4bV-80V3NLxcJ2e0fnRMMJ7VKuC0btPA9xffGtVSWUOqgDfHsVgNw4Aj9_wx5zvqH6taBSYtrR2QCh2uHvEU_Ep_hfIEn-MBtp8qyKEjr4pzpgHCEsLlHZWzjBxOO-kccgF5SBOqWefdXfrJwkvp8ZdRPRyosJqWQlrqwetQj1aPulPw2Wqn8-Ce_K83njVMF0dAoFwzlLFE7WcLlgfBDg5t5KSS2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ افتتاح پادگان آموزش نظامی جان‌فدا با شلیک حجت‌الاسلام طائب، فرماندۀ سازمان بسیج مستضعفین   @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/464144" target="_blank">📅 15:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkcXXTe4NtyAbEWgx0rxY4yysntDnU29NoN0XiJ2xwUYrRvInoXm8WXPr003KA6A42rDl6wIPAn90zhOVUVjnZPsXypoJ7if-om8Cg6V2TVaM-6XkX6ps8bwqT4ZrnBGpXNsqFKLCxUtPWXgtuuAXfsjrf3xwBC6nu3e7BSoMx5c1vrGxLu9xfUvO9oDatHgzNbsoLDME52Rppx3ZtEGc57glzef-dRRjfooCDK14ZxlOHOsgZjRacwYv9N0awndZFaoTM8LEg8c0GvVS9eeQT68IpucTdGZ1O3bQ6ePTmFHAuR2dXg1xUwMwhRabqzHrzauwSKJbf-a3JnMx9tB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی با وزیر خارجۀ اوکراین دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/464143" target="_blank">📅 15:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3faed9dc.mp4?token=lkhcrJX0hPDrczwZHzcPV9M7dXhPTtOwL3_1I_1qGqIudWR5JNZddLdiqInx2VJkBvHqPTPZwSE0n3IWBLmVVIigxtBbhhUVyQpz8jeFEkuPLC7PEUloIJc1uN06OCVAeSV3fKgdsxOqhkt80Lg4tq5I6SbBgDVV1FmX1UXDCBgCrBs-u7af7FoRdnCmd0MxcgXkQirTIF0f9pH4FzvSm485mJQDcJDhSlUCBFp8IYtenU5EhS0hrw5w0CksQ2wdxQbTGowlW9VHXZWJbJDF0iAgASkRJefX4SiyFn0IsT070qsX59ac4ye_R64ePVlTe-LLFDvdgX3WCsBE_BcXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3faed9dc.mp4?token=lkhcrJX0hPDrczwZHzcPV9M7dXhPTtOwL3_1I_1qGqIudWR5JNZddLdiqInx2VJkBvHqPTPZwSE0n3IWBLmVVIigxtBbhhUVyQpz8jeFEkuPLC7PEUloIJc1uN06OCVAeSV3fKgdsxOqhkt80Lg4tq5I6SbBgDVV1FmX1UXDCBgCrBs-u7af7FoRdnCmd0MxcgXkQirTIF0f9pH4FzvSm485mJQDcJDhSlUCBFp8IYtenU5EhS0hrw5w0CksQ2wdxQbTGowlW9VHXZWJbJDF0iAgASkRJefX4SiyFn0IsT070qsX59ac4ye_R64ePVlTe-LLFDvdgX3WCsBE_BcXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صورت‌حساب تابستان ترامپ برای زمستان آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/464142" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15262db003.mp4?token=Coms1cTIoW6zRvcBylf2e76O48lcHNA6pKWtDcBDwzMbzk0m92UgwVvQ7svntrjvFYtxCHVSZPeeTi0PzcyW2aUoJnwzOD1qKJFMe8FF0Wm7xU1NB_aPwu5kjBx9kfyZE4rm1JuZnYsz0H_JyV2PB0SIq7l9_f_L5WAgurw-0mY__dVFURVXaiJEjgDnlbVcfV9cTDdthW8GQQqrIN3rToPw9cYbkTwGoFk22EkGF49Eh-ODh1Ph0b3onI-Tf8EiJB2A4orX-Dc040oDu8KJGISiVrg1nmqXeILLBRYfZzlp3LWPRzEvHarXN1pyrCQlLSTSzXR17V1fDm1IRbwZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15262db003.mp4?token=Coms1cTIoW6zRvcBylf2e76O48lcHNA6pKWtDcBDwzMbzk0m92UgwVvQ7svntrjvFYtxCHVSZPeeTi0PzcyW2aUoJnwzOD1qKJFMe8FF0Wm7xU1NB_aPwu5kjBx9kfyZE4rm1JuZnYsz0H_JyV2PB0SIq7l9_f_L5WAgurw-0mY__dVFURVXaiJEjgDnlbVcfV9cTDdthW8GQQqrIN3rToPw9cYbkTwGoFk22EkGF49Eh-ODh1Ph0b3onI-Tf8EiJB2A4orX-Dc040oDu8KJGISiVrg1nmqXeILLBRYfZzlp3LWPRzEvHarXN1pyrCQlLSTSzXR17V1fDm1IRbwZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگاه دنیا به یک سخنرانی
🔹
سخنرانی دیشب رئیس‌جمهور در سازمان ملل بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/464141" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI3kDkQCWunbTFKs4Yc7sBHxmlrOfoBjqgsZ-r2RENTPmr9obInSrUZAvRYDI6PEdqtT5-xiyaZnd__kxXREhxjXNZFSHG7vmsUAdG2PLMqrZG05umH8-OukLyvkdO0SWhBxJWGjb_sFNccUlUoYhfoDVPhZaEWDqqTmAM7qfaborR2Ud2LckbM3WkJ98OTwPGzsyoR6tr3bS4qjzQmIJFz69GQbtH3DMvenojbIxax0Ly_WYc0c8P3j92TVg9lcQW934j4v0Z0hAi5W1LJzTIDYcg7ATd0Oq4m6gQsglm_ch1rVZtbN5dApMEcR43B0At9p4wLyEgt-JYeup_bPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سازمان بسیج در تقدیر از مواضع عزتمندانۀ پزشکیان در سازمان ملل
🔹
سخنان  رئیس‌جمهور و به نمایش گذاشتن تصویر رهبر شهید و تصاویر شهدای مظلوم میناب و لامرد، توانست صدای حق‌طلبی ملت ایران و مظلومان جهان را به گوش دنیا برساند و هیمنه پوشالی قدرت‌های سلطه‌گر…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/464140" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3c1f9bf0.mp4?token=mQyP0qZCLyBgpitaxi_NhWfSccnCDMlTBF-3RjFVxRtMjVY3tdOjhBZwAfb-_luj3JLKL6zJAbJc94o7Ia2Oox685CQ1hxWtJwXsfO0fFjGjKKy1NEd0Y6CroAsbK1vydMetbx37ZRYbmsko8pf2oCPHrrxIg7J0YkwtPQr3NSmPFuzdIOHzxAB31XDOBIFuxK0fsBQsEbM7NjBMkt4A4JgjoYVnu3NXR6bEUeE3chJGbJPqUC3mFFFUYd7ZUA2-96M1O0DCHivvIlikrEMhlwA_nHtt-Lwep59vGXBPVO6Ddu_ppdISXNbjPZCyFuED3x9l7lgzznABN0J0_-J9Up5QT6jBJH2HYVJ3jdRM8zbY3UnXqNSU4YrmUm7mICp2T-3swRKcAHcFkK5EBYZcsBPxwn5o0hcyCHVeyt4uBiVi3NjYkTa6c4Fox8xkb3IzRyaLmdbT32OuTAjJUI50KYRHzAvir09VsfklabX0WIeLBSW0a8BO3A-zCvb7DuitCdmWAuMUiUqTHGApXBm4INZ7dUJLoYWNtsYT-gAXkZbeQZguENd6uC_BsgHOqyPYXWts_x_qKo6KwSbbKzf11UZ-CQH9FLBguFJaE2fMy4tYxm76EMcAjeHmLX5m7Q39DhWfX91HZ7fuoJk70zopkQO-gzfkfO4SQo5sqQVIIsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3c1f9bf0.mp4?token=mQyP0qZCLyBgpitaxi_NhWfSccnCDMlTBF-3RjFVxRtMjVY3tdOjhBZwAfb-_luj3JLKL6zJAbJc94o7Ia2Oox685CQ1hxWtJwXsfO0fFjGjKKy1NEd0Y6CroAsbK1vydMetbx37ZRYbmsko8pf2oCPHrrxIg7J0YkwtPQr3NSmPFuzdIOHzxAB31XDOBIFuxK0fsBQsEbM7NjBMkt4A4JgjoYVnu3NXR6bEUeE3chJGbJPqUC3mFFFUYd7ZUA2-96M1O0DCHivvIlikrEMhlwA_nHtt-Lwep59vGXBPVO6Ddu_ppdISXNbjPZCyFuED3x9l7lgzznABN0J0_-J9Up5QT6jBJH2HYVJ3jdRM8zbY3UnXqNSU4YrmUm7mICp2T-3swRKcAHcFkK5EBYZcsBPxwn5o0hcyCHVeyt4uBiVi3NjYkTa6c4Fox8xkb3IzRyaLmdbT32OuTAjJUI50KYRHzAvir09VsfklabX0WIeLBSW0a8BO3A-zCvb7DuitCdmWAuMUiUqTHGApXBm4INZ7dUJLoYWNtsYT-gAXkZbeQZguENd6uC_BsgHOqyPYXWts_x_qKo6KwSbbKzf11UZ-CQH9FLBguFJaE2fMy4tYxm76EMcAjeHmLX5m7Q39DhWfX91HZ7fuoJk70zopkQO-gzfkfO4SQo5sqQVIIsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
شیرازی‌ها لشکر جان‌فدای ایران  عکس: احمدرضا مداح @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/464139" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca987a407.mp4?token=t9H1YsBIsWengKpb-FQjtD-niiWJJUaMyXGVJ4aXSkOJxJrkleXvn6PfIP2E5k2xKzQo0YHAtz6RclOojMJbzvw52dT9qZAXoXJoouraZgFuF_qiw9JqZ_hZKxv6vUk_IZ0FhOFLDayqgIFwEbcSQu8Ju6Q7I0MtQFlskFcUnvupl_85Jln548tsgphdVDSwMoMQPjaCCwu9nG3-Nm8sP4OLnjvTTBUqg03B-BcFcJ7qQIPnoGdbeTNTlz-N1XaN3C6wHZsLpHJwed75a0LWHK9mlU2FBAaiB6Q4u6_iaAzeoXu6t0DegtfVyhJ-3lfy7RhU_MultCfHKe_7BCSuqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca987a407.mp4?token=t9H1YsBIsWengKpb-FQjtD-niiWJJUaMyXGVJ4aXSkOJxJrkleXvn6PfIP2E5k2xKzQo0YHAtz6RclOojMJbzvw52dT9qZAXoXJoouraZgFuF_qiw9JqZ_hZKxv6vUk_IZ0FhOFLDayqgIFwEbcSQu8Ju6Q7I0MtQFlskFcUnvupl_85Jln548tsgphdVDSwMoMQPjaCCwu9nG3-Nm8sP4OLnjvTTBUqg03B-BcFcJ7qQIPnoGdbeTNTlz-N1XaN3C6wHZsLpHJwed75a0LWHK9mlU2FBAaiB6Q4u6_iaAzeoXu6t0DegtfVyhJ-3lfy7RhU_MultCfHKe_7BCSuqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه‌وبودجه: منابع ارزی تامین دارو همچنان ترجیحی و ۲۸.۵۰۰ تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/464138" target="_blank">📅 14:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88677e22e.mp4?token=f1T1Az3sVHp9ZVaokWj2Kydn6vh1pjJ7ZNdJfizMkW_jJ952Nic8s0Sw_UFW1mL-bMUR0NRd_AXPgUH4kv7e7U0QAmoceJh0ku10q20b4dGpTTgOpEHEFshhVPi5DpdyDgKYDdlqW54LuKIUmr0rYRvLUZzQMfdMPzAbkCaSB4JMnRp18v7OM8LvQHFyYBpU9NBBSF7fA_gax0IBvIetj0Rx27KDFXfLBPkyjZ3SCX8l8_m0wi01Gi-RAF460LSsbhH1-O3hnccNQ3pUsoUv4x6HAolou7R_hXkv7pFXoEK-2CPhVZ52C2DHjZnsv9ucRH7sgHYvBsfTtBUDjr7uDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88677e22e.mp4?token=f1T1Az3sVHp9ZVaokWj2Kydn6vh1pjJ7ZNdJfizMkW_jJ952Nic8s0Sw_UFW1mL-bMUR0NRd_AXPgUH4kv7e7U0QAmoceJh0ku10q20b4dGpTTgOpEHEFshhVPi5DpdyDgKYDdlqW54LuKIUmr0rYRvLUZzQMfdMPzAbkCaSB4JMnRp18v7OM8LvQHFyYBpU9NBBSF7fA_gax0IBvIetj0Rx27KDFXfLBPkyjZ3SCX8l8_m0wi01Gi-RAF460LSsbhH1-O3hnccNQ3pUsoUv4x6HAolou7R_hXkv7pFXoEK-2CPhVZ52C2DHjZnsv9ucRH7sgHYvBsfTtBUDjr7uDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه‌وبودجه: بخش عمده‌ای از مطالبات گندم‌کاران این ماه پرداخت می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/464137" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgCKBZc2BP13nHDlKq2vdhEBe14_UfAPFOhjeHwEXeHo2UraFyjAxNQTnOmP4Dh3qCkI1J6OXvJF8gJifDUI3JUubJ7IoUrRwD2iJtxnH5hpTyF8awtZr5dTSrC5-GBAff2OYmcOLdLB4cy5SWHntZ3GlEgPylMerfuwP01pPxJqpibIq64RoMQGRAHII44JumzYD_l2lFdWLNzQ_ofg6QgWywAR9kmczbC2RNHm4LPs1XcOf3VQuNz33RwVWlY_e0Fc1YOC10moZmCkF9-CECg2KDXHR0zFPN3HKhCwzoNiDq_jUokHzNfjrEQ699G7vXmyuoXYg7R4SmN9z_u88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: ایران نیروهای آمریکایی را از دریای مدیترانه تا دریای سرخ و اقیانوس هند رصد می‌کند و از موقعیت ناوها، هواپیماها و نیروهای آنها اطلاع دارد.  عکس: مقداد مددی @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/464136" target="_blank">📅 14:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4414df7320.mp4?token=GVcuJMl05pqSvedRa1dLLnJWLTCXL_fwuLHF4zkE7056O_QYPkZ-9TxDY33n1HDBudP9rOL5Rp0XdpcntlZ8Fe9sgVWvGvrmFQOVCbapfNLSlUoV2bq5un5qJLORe8s-sif3oFIip8pBpV67HqT6qJmR_iPeFjYqgrup0KS7PdSavo3PGkmDgJdYMdSKOTII8uzZ6LIq1-8HYlCNptERkHjdl6E78FfSmmSb8HHrWAF7sLWSKBOAcVrE9GIDQsD9PQ2BQUg98NPvTbG8Ic-uppZ6jPEbltnVqnVsOPLyMlPLSxojeIdswQ-Vqo_zsUGVCrBPs5I37xMK40RCYZJ-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4414df7320.mp4?token=GVcuJMl05pqSvedRa1dLLnJWLTCXL_fwuLHF4zkE7056O_QYPkZ-9TxDY33n1HDBudP9rOL5Rp0XdpcntlZ8Fe9sgVWvGvrmFQOVCbapfNLSlUoV2bq5un5qJLORe8s-sif3oFIip8pBpV67HqT6qJmR_iPeFjYqgrup0KS7PdSavo3PGkmDgJdYMdSKOTII8uzZ6LIq1-8HYlCNptERkHjdl6E78FfSmmSb8HHrWAF7sLWSKBOAcVrE9GIDQsD9PQ2BQUg98NPvTbG8Ic-uppZ6jPEbltnVqnVsOPLyMlPLSxojeIdswQ-Vqo_zsUGVCrBPs5I37xMK40RCYZJ-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال تاریخی آرمان در پرش خرک
🔹
مدال نقرۀ آرمان خدایی در ناگویا، نخستین مدال تاریخ ژیمناستیک ایران در بازی‌های آسیایی در وسیلۀ خرک حلقه محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/464135" target="_blank">📅 14:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464134">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978621abd9.mp4?token=NBcBPUwI-bKiBfW_gcXGF2iug42PjloBjhFPc8UoCa4uYqtLgI9OVUrtDhjVMA8Eo4IVblmuslajclUf7X1edr5GiKH0yp0R9JKppQxueuL5GnpVTdTxl4q5QrCTSUCXF8dtLuRNjA7NitFyDXDPXPnzKLO6E1h9jJV0G4fxl9Ownn47svAuXTI-Wc1gdwBpRNNf5torqZqABvivl1Q4nYfpblgutgWyMMOLzlgKWtRDCx0hoFIEgSas1m_JBfBgnCfCJvp3i6d7Y2uT-GqRsEfNFf9vLJbkXPKzX0DHsWhIn9aapSWR2q7wo3p4tvz3QZeQF2yFyqnfT_D-25tF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978621abd9.mp4?token=NBcBPUwI-bKiBfW_gcXGF2iug42PjloBjhFPc8UoCa4uYqtLgI9OVUrtDhjVMA8Eo4IVblmuslajclUf7X1edr5GiKH0yp0R9JKppQxueuL5GnpVTdTxl4q5QrCTSUCXF8dtLuRNjA7NitFyDXDPXPnzKLO6E1h9jJV0G4fxl9Ownn47svAuXTI-Wc1gdwBpRNNf5torqZqABvivl1Q4nYfpblgutgWyMMOLzlgKWtRDCx0hoFIEgSas1m_JBfBgnCfCJvp3i6d7Y2uT-GqRsEfNFf9vLJbkXPKzX0DHsWhIn9aapSWR2q7wo3p4tvz3QZeQF2yFyqnfT_D-25tF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بعد از شنیدن سخنرانی رئیس‌جمهور آمریکا، متن آماده شده را تغییر دادیم
🔹
در مجمع عمومی سازمان‌ملل از حقانیت ملت ایران دفاع کردم. ملت ریشه‌دار و متمدن ایران نابود شدنی نیست.
🔹
ایران را نمی‌توانند نابود کنند؛ ایران کشوری است که ریشه در تاریخ دارد و…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/464134" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9eee73cef.mp4?token=pifUKBxR-wrXGqBS8yCJO-M6OG3hAzoA1TDuiY8TsMEMGXlxQ4-CG0bDvV0RKMCcIKsKVl3WoHFvUOHIeXd3kAsvu4xyv7kj3KG6NArBEWuoOqwU6SzZLz17d8yeLFwlhZZ0jaJcW-1uh3USFzzWPhfyvLbc-yS6mjtixtR-OXm9gGWLe74i9o5T-ZfObPHpAg3cMy-ysq52KAUrAsMDnDU1AKCHSA_ZUvObsfodiqPVxU5ZabLwvAzTvoRfUGjMnrDRdcjbgyNn_NL1fqnmrLxYyqvNLzQESkvaGzDXu_IZ5RdknjvrEtbw04aCzHmkvfXsX83igkXVpHNsyhXpmCylo3vvB5bsTnfBZ7306pYnIskClFfdGLd0I2y05o4yOajxPD8KPdo_CO_-_L1MWZ78LI-4Fa101UvwMM7eD4Wrc937DcpkjqRy4iL0DsCcdRmbWT6qpj26-hVB-ivoMO17Bx8GZKWpCySt5B4GLYeNERoJ5cJVuO899gDAk3OLZhfMVbKCSqRK9ZnbFJ3qiHPjhfZoMCjOGuzLdwRUnc6gVnS4gHNUHYInM53XQErpBOUQ3KEY7Xe33e8iQyH-1qRQYDlcjz4vDJu5DENu20Yus6qDRxAA-YD24LwKS8Sxq8HXj1AsvOAAZNvqJtvuS7jG7SlwHrQR1CwOE2BjdHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9eee73cef.mp4?token=pifUKBxR-wrXGqBS8yCJO-M6OG3hAzoA1TDuiY8TsMEMGXlxQ4-CG0bDvV0RKMCcIKsKVl3WoHFvUOHIeXd3kAsvu4xyv7kj3KG6NArBEWuoOqwU6SzZLz17d8yeLFwlhZZ0jaJcW-1uh3USFzzWPhfyvLbc-yS6mjtixtR-OXm9gGWLe74i9o5T-ZfObPHpAg3cMy-ysq52KAUrAsMDnDU1AKCHSA_ZUvObsfodiqPVxU5ZabLwvAzTvoRfUGjMnrDRdcjbgyNn_NL1fqnmrLxYyqvNLzQESkvaGzDXu_IZ5RdknjvrEtbw04aCzHmkvfXsX83igkXVpHNsyhXpmCylo3vvB5bsTnfBZ7306pYnIskClFfdGLd0I2y05o4yOajxPD8KPdo_CO_-_L1MWZ78LI-4Fa101UvwMM7eD4Wrc937DcpkjqRy4iL0DsCcdRmbWT6qpj26-hVB-ivoMO17Bx8GZKWpCySt5B4GLYeNERoJ5cJVuO899gDAk3OLZhfMVbKCSqRK9ZnbFJ3qiHPjhfZoMCjOGuzLdwRUnc6gVnS4gHNUHYInM53XQErpBOUQ3KEY7Xe33e8iQyH-1qRQYDlcjz4vDJu5DENu20Yus6qDRxAA-YD24LwKS8Sxq8HXj1AsvOAAZNvqJtvuS7jG7SlwHrQR1CwOE2BjdHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متفاوت‌ترین جشن آغاز سال تحصیلی در‌ حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/464133" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464132">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قزوین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb4b65587.mp4?token=ZdQT0CEioY50t-L-Xa1cOqJostPXEuGWWAprVBUdWfO_1_JB3snF8evUgzjyFcT-HMOjWlRebAexHiYJaAJdIo7dx80CH0S5-ZCX8Azb1jE4DBbpHn_qYCCKVkpjsUozZQ0heQTDjyvhNQutjQdtkXpHbGcPnZ9FchQDELG_ERhzVjZfVB5f4ewi-RNcWYeyhW8P_0z9s8idZPmw8yTGBfqWUBywr8NstonTg-Of3QN5luNJe-7pC84fB6FTg99pmEvmjdSujiumv7IizL2Cou-wZvqrwttTC8-xQayL4fzw901dINGbHit1hJkYzpqBRLe1zXhLFbanO3NYrFke5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb4b65587.mp4?token=ZdQT0CEioY50t-L-Xa1cOqJostPXEuGWWAprVBUdWfO_1_JB3snF8evUgzjyFcT-HMOjWlRebAexHiYJaAJdIo7dx80CH0S5-ZCX8Azb1jE4DBbpHn_qYCCKVkpjsUozZQ0heQTDjyvhNQutjQdtkXpHbGcPnZ9FchQDELG_ERhzVjZfVB5f4ewi-RNcWYeyhW8P_0z9s8idZPmw8yTGBfqWUBywr8NstonTg-Of3QN5luNJe-7pC84fB6FTg99pmEvmjdSujiumv7IizL2Cou-wZvqrwttTC8-xQayL4fzw901dINGbHit1hJkYzpqBRLe1zXhLFbanO3NYrFke5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدر نبود اما فرمانده تا مدرسه همراهش شد
@QazvinFars
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/464132" target="_blank">📅 14:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464131">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibwlO1JwlL1fBAX6eVJxbtJxRLnAqSAFNp50Cid-0AKZkAJ6oexpbxLxNyaKLkduZv3cYfxAR8V76tjq679EMG55VmDlZwKaM7EE1Ux4rHEjwV9S4Ys4UTefTKreHlXn_xjUzsHr4L1fznt-GyS1NRRT11lw5c0teNJH3EZ3Gl0MEM8mZjBo4hMFAnKRVRfbznhdehxD_bV628Qcul2vN27PlrfAjtCewx68S78QlDSy_rJmO0gqAlyFsNQeNy2dAuCsnHsY9vruhp-orty6MW_E6PQrhjtsGEnvGSN5u27LZV9exF99lJuZ3lZCqUg18FXu3TPnJMiDL83kI9pjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرلشکر صفوی: پیوند تنگۀ هرمز و باب‌المندب صحنۀ جنگ را تغییر می‌دهد
🔹
بیش از ۱۰۰ سال است که یمنی‌ها در مقابل هر نیروی مهاجمی که می‌خواست به نوعی به تمامیت ارضی آن‌ها دست‌درازی کند، ایستادند.
🔹
جنبش انصارالله، خود دارای اهداف و استراتژی است و خودشان در زمینه…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/464131" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464130">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ممنوعیت صدور چک رمزدار از ۷ مهر
🔹
بانک‌مرکزی: در راستای حذف چک رمزدار و جایگزینی آن با چک­‌های تضمین شده، صدور چک‌های رمزدار از سه‌شنبه، ۷ مهر ممنوع و همچنین پذیرش (واگذاری) چک‌های رمزدار در سامانه چکاوک از اول دی‌ ممنوع می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/464130" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464129">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7b4a05c1.mp4?token=DaxyyKS-V0kUuDYlByXyAfuSOi0nxUTdqRBBVTZ4Ed4pouu6xRXB3yy4-ir05BZcZq2V38SKSAu6g0ff5SPns5NrjvvKSUjIasDWjaMLf99xFRbxhc_bfbH89zPmb_QqhN_ESzt-kjKbB4hTdfR1DqV3_8uEqZ1tJFS0YsbqtvFEqlwLqsgd6-IXOZhwN423tIkewJiXIRT4eerINIe_OUw4yFw-0w10ZxvxHtxGg2vrD7LGhFw9yPFxKGOXqBTRS6Y6uWUYfwHnwK9jNnREmOY-eFw0CaqITIv-7hW_yo1X2x4oWpsaAmdgn1NQsbikXlLVsxtK_cZx5-CyerKnKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7b4a05c1.mp4?token=DaxyyKS-V0kUuDYlByXyAfuSOi0nxUTdqRBBVTZ4Ed4pouu6xRXB3yy4-ir05BZcZq2V38SKSAu6g0ff5SPns5NrjvvKSUjIasDWjaMLf99xFRbxhc_bfbH89zPmb_QqhN_ESzt-kjKbB4hTdfR1DqV3_8uEqZ1tJFS0YsbqtvFEqlwLqsgd6-IXOZhwN423tIkewJiXIRT4eerINIe_OUw4yFw-0w10ZxvxHtxGg2vrD7LGhFw9yPFxKGOXqBTRS6Y6uWUYfwHnwK9jNnREmOY-eFw0CaqITIv-7hW_yo1X2x4oWpsaAmdgn1NQsbikXlLVsxtK_cZx5-CyerKnKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدس بزنید این‌ کارها کارِ کیه؟
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/464129" target="_blank">📅 14:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82dc15a2c3.mp4?token=XtRRCjpfFjwlP6ypUWVeLDxYZTcehXfB8O8A4Yw-2JQvu8zXdShb_ig4GuqlCIsb8bpzX3HEHsLXNg79L0Te1iEirW7zNy0LwyApvVzZBPbYPxYR6h4YmQQE71IXWBJltC2mXPm0cHpk0a4Cwt6037KYfo_Y5VkvDK3wfII9mJMigdQMWSRCe0QFmMl_TOaCVZW2-K8HSumqOXvVssHSRF1imnhFOaWuoXw1KN-kFB6yObgHXnHe1u_H03H_WohEbAnBFtz4r-xRdhECJnwyfm8ul84uYm39vFKUrZbA1mHWVDBA4RwbPpsZ5Y4oLLAp-dxZRPtNmjhcFzJ9eLZZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82dc15a2c3.mp4?token=XtRRCjpfFjwlP6ypUWVeLDxYZTcehXfB8O8A4Yw-2JQvu8zXdShb_ig4GuqlCIsb8bpzX3HEHsLXNg79L0Te1iEirW7zNy0LwyApvVzZBPbYPxYR6h4YmQQE71IXWBJltC2mXPm0cHpk0a4Cwt6037KYfo_Y5VkvDK3wfII9mJMigdQMWSRCe0QFmMl_TOaCVZW2-K8HSumqOXvVssHSRF1imnhFOaWuoXw1KN-kFB6yObgHXnHe1u_H03H_WohEbAnBFtz4r-xRdhECJnwyfm8ul84uYm39vFKUrZbA1mHWVDBA4RwbPpsZ5Y4oLLAp-dxZRPtNmjhcFzJ9eLZZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلنوشتۀ دانش‌آموزان اصفهانی برای هم‌شاگردیِ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/464128" target="_blank">📅 13:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFHvlwPkRaabdrEyC7BAkmUJZUo5VYaWDDvetV8PJnUIoC7bnXT40oY_BKnsRbYFsYxdVM7SIK46DZKZqqoniRyw-3Rq8LjGoyaUlxriYMkzlkPKY8mUAeqKObtthwCHOXMBmtiO9LWFkvb_LP1jfg8lr0WvSlkpAs9xn16A2vmVM_8jlAqrVSrA-3VLDHjSIOufZTzfRqlXYmQVF9cUHcw9NTEqcHYxUR_jOemPfQfzKU9DRtfqeMY9uVQEVIToyJhgRDQBSH_Ncf5Xy4fwTL3fyrkWuzjteeI9Bn9cBVBZ-TfRHdxOPHwapaWNFnTatQm-Yd4jsyFA5bbMeZtSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTQfMco5lwh0fFrxw3TJhj-u5LqcA7HrmkSQZbLdLIlHsChnFRuczVuJu5WdXSbK4HfJitqA1Y3ZTJmoIAOELPF_24oejr35nbga7hSksuV4XQABgdifVnSLGp2CgIaNQ0jsP5bksWLFXedVnvEKeYPUauGoiUT6oLOL_zvp97ClRhEcaEVENr5sj5HxXPb8OvWAMSrUz1uOkaxlmEh-9C4IxvXrbZGKDKDT9ldcWI00sntOqbpiCY7Oy8SJ3dam7TZOm9MkxtNR9vHEYTNC9z3YDuSRdOzgqgMbGso1YBzsa4-fA33qOhyxivrO9UMcQgOeapWFDcPIcfuGEakHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrZI89tuo-3fJnl_qf2OSqi93djCQnLqno6gmgJDVVG1jwwN_z15b7AKkZ8WPpKnvC3glMWgzkC8YefFnGqtkh5SsqOlrCyZ7nuBa8aLGQS0w2dtIlyUDQE7y4cMMKGKjduMGXwyCYKECc6GGbVIkI9QhGS46aR1oOGN-8hobQV_ZDEGCHowEjXAn7drsX_wq-tRPoTlinjrJbx7Co21xe_3JVOIsOlElu1QDpH6Y0PTJwC15-q6OmKN4tWqCMdnL_GT8YWe7V14zx0763sIaLew-09qHimkyaYXC3k5zzY5g31jq9KFuR7R81SnVQrY7cg0dLn641xsv4xItkQIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gvu3GUH9CJmQBL5aH0rSmPYV_bvtan1R8JGQEKTB0e_U_K8MOqHlpFSj44kFf88BLj7u-hb4OEXOnVK1IzhVMXm5JCZSt4Qu5zkU89LUslRS8ZkFLzoC0nm5S9MTOWNozkr0y-9pzKjI_0o8Z-q5Jfz-Tx4zgCoT6Pt35Y7RBASPOwiri-VlpOtwKjL6T63GZV_W_LNUMvcrM01UXSP6ugdssImu7ESyukRzWYE90KhK44bKSu-An5zZyH2QTbb2_vDQahnftVwRxRBAiKr40mMT4FGYnPd9_rhsL0fndrwLezF7lQR-zL-HAvqksVUlIJB7-ugOIqHdK5domLSPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COWw8PMWRxR8mXVWFNYyOHl5P-ZMWbLkrIbAP4qgRf8gN98VnXJ-cn2gv4Jts9vALIgBTFABrTE2snAP0JITz4tsSLVaHJu39XVLq_YHhQLuOf-InyiUP0DUkGPpSDh-Y1mCyNMYqv3Rq5yrrPviqKTJyRkxQj-LjJPmn-AvkP-T5E7WDWKMES5j2LnqWEvjD59c857vMjhy68yqehYg7L_kNHGy82le62RvobmSd0Vtt5STHec7GlwhxuTubEU3G9W63K9weW4c6_crxvLsqer6IABb9-BqBmkvyzXX82FCA793yNkpnTZd_YeMjr9elJMMW0pyQ34M0xpwB7b-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Upgogs8FHxfe4EfTpGQ9NR9a3Lfli6s9WQg1523jGNYGr8iS_ZrPx_96lHz023BAI-wRR7YENIVVQFbLpLfLpw9J-EagUxluH0NDTKv67JO4wgsFKng19edV-E5t4guPjSWtbX4fZhQs97QUr076qv5rJtK_C6cHn050VJrM6woMZzmlcxytZdbwnqOw-1SechxoFE-pZinX7TZ9c_tMB48q2uWX_vUu4E9Cef6Vp7i3THLab4htD01x-JP97ziuMTC2j3B4mO8qlwRO0xA9cM71DzILPt55xNZPDPycRHB-thzZoTk01ZXkD3__-takO9X2uBgenc2nqbwHR4JFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIpKmohFpLbODOlJKTtjJbdHDPgZbPOcIuptHrjjvrrh2tvRdyf7gewRpDzo7FsPB29Wl7erK-m1QxxDhXgMDbcg53ko00jYc65nqRFwKPb8I2VpaU3jwHuhT6Jpf3k6Z4h6lNslyStgCYPDpkatTZ1NFgQauabbsg5c3Yde8VEzufylHRA5CmmuWGqiIob0-0TdmRU92RNzQBfInnClGRnCGfrhpMzCJFjIzlERPrVUwIhI41lMWzzYHwNB07N7B3OCmgudLAtnv80R1ZN02kKaGKpbOLsadt7M08C_R-CwMI16PDMhsXjIYn9BgFHdImUqqkiNSQML6GBZhPS5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTGYEmbJCqBCflAfx_QDuyYcGKLgN4sNhU2wdnXtzdaQq8SG29AIGivRjuqteJxz3OP4nD6kFZ87JkiAySqpG5y26AyGLUfm03PR_YUzTh6HpXI5OAahSRpryiHg1Dv7JBKEDMXYWQ7YxfCFpqVHnNFfaxDq3zAr20-6AvJDzBAd7RMOWQtQdu0eikZJq8C4swyet_KvMho3KzAWJccO5yAaUh0AC0sn2YiHCKQ50p0OTx_ukbi_PHNoF9UA-Y-JdqGbTykorsHNqlXaSrSP2kKST1MJP--IA0cwBv10PGXN_q3-ZSCwGWXq0LH7DQNWPrCPQcKeqVqlA91tpOhVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxP8Z6kR7jG1iSfQquMv5YMLiC5ZVShndGmUpFp2fooJDchRX3qfL4Jb0kxdcP9huxVJO1vVXx1AGAEQePmoXiRfNubciSay0T1a--LkOULJjkLY4v1XhfObfkehnM-BSVWP4_IkZ48TDSHexgzgeVGdA3VwKiR7sVSvP_1x4yFaOQ1rACiQ-X9BZW_Put07L3UwuyTeNHnsMBpccSxx18NxPTUVOKJf1u181sbQtw__tmAxPDLrSd1fL2UlnU0EK30Pa0wvDtwtBl9RZ5wHPvS6Qfng1E7sZkEf7SyQ5T8xTUAk140md3ktWaw2AZmUDyI6KZ2c5SxxZ9Niz65ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUgAnfXJiZlNnFTUCNviZQVDbAs4PzdqYR1g3BA0SI0xYHfINlSAchWnWD1PKjl-BGxNL62_HPnpqhOh2bXxDlwMNX8PIwU3iFVqV8HF4GMnJbOLOs5peqJiNrKEKhAKzP2967jJtAZk9cVcc8x4VvVgn85-0kRvlxSW6JQ0ra8nxIqfU9mM8gUYfYg5zLf3BvjIjLFmfSM4bFrRcdN6UMLJdV8q2K4W4ZS_tDlnMOc8baN6ZAqUiS9VCPqpmMVDCn1XWhqtkvzpD-J3aRaBa5otW-XZgNv8mQjcIjEZkgKmf_5RSgrmbxJw-ay6k2isox3G58NxiWxbe8Xbs6GKXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان در اهواز  عکس : محمد‌آهنگر @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/464118" target="_blank">📅 13:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8jM4-2VshwbRySeJcxtlZBGC0alX3Og7pTRfciz_HQUhmF7D86qI4OLqVNOJdnntRuwkDgZL25oUtX_N3r-Vga5gfmJ_eKgRWi_rL3vZeXsKgbEQ7jLdQgwphIjr2ssK1cJkDoXmbKaBJkroPNLItFkSP4o4XkFvqxNxZQSOcg4YUiXB12_55rJie-K87J-pH8mPW-qjvWwF4VZLggscWbAgC_FuPRAgJMQ7i7XrE5CeSACdxgW5CmWUu-fXAvT5MZ7VgJMxpAUoEm1gpfqZM9al_S6kxN8hvYgJkzzZfJIPlecv3vN8GE_RI162-A8GT8SSxA28YbFNaNRpAQ79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: انگلیس روغن ریخته را نذر امام‌زاده کرد
🔹
رئیس بانک مرکزی در خصوص اقدام دولت انگلیس برای تشدید محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور، در همراهی با سیاست اقتصادی آمریکا، گفت: این همان مصداق روغن ریخته نذر امام‌زاده کردن خودمان است.
🔹
به نظر می‌رسد خزانه‌داری آمریکا در فشار اقتصادی به ایران به آخر خط رسیده باشد و کشورهای مختلف نیز برای نشان دادن همراهی و تبعیت خود از آمریکا، فعالیت بانک‌هایی را که بعضاً سال‌هاست در چارچوب تحریم آمریکا هیچ‌گونه عملیات بانکی در ارتباط با ایران ندارند، برای خوش‌آمد آمریکا مجدداً محدود کرده‌اند.
🔹
البته خود ما نیز برنامه داشتیم که برای کاهش هزینه بانک‌های غیرفعال در خارج از کشور، محدودیت‌هایی را بر آنها اعمال کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/464117" target="_blank">📅 13:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpYT4iZETOLWf8aHrWOs87TS_8rUCWXgUZQasZ5KnFRQt4DBEm-xMocbDKyxOSRMioRm26KvjhoHMAmwdAOo7TXGpAR9OgH9rWzpO5fTjjqXCCdx5R9IY1lVL-AJwGZpS6l51-vpZXOSbtdRCn_8mflaft3MCSE0pcCBq0CFK6lcwihu6ObTReiyNHX-_3PP9oVEYld6-gFXLGNmZ8bGM6d-w9_nldSKJx_ij-il-CHovdbTGuAm-vOtuaVZldePbwW9bD220dCQk5iZsMT1pj8x7j97hSD2ugZb5YQUQA1-hZkPkGiKbJ1_YtO9APJdjze-FV2WFrWwBimsMR2PHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سازمان بسیج در تقدیر از مواضع عزتمندانۀ پزشکیان در سازمان ملل
🔹
سخنان  رئیس‌جمهور و به نمایش گذاشتن تصویر رهبر شهید و تصاویر شهدای مظلوم میناب و لامرد، توانست صدای حق‌طلبی ملت ایران و مظلومان جهان را به گوش دنیا برساند و هیمنه پوشالی قدرت‌های سلطه‌گر را به چالش بکشد.
🔹
بی‌تردید تبیین مواضع ایران با تکیه بر منطق، عزت و صراحت، بخشی از صیانت از منافع ملی در عرصه بین‌المللی است؛ از این رو، سازمان بسیج مستضعفین، ضمن قدردانی از این موضع‌گیری انقلابی و شجاعانه، بر این باور است که چنین رویکردی نشان‌دهنده مسیر روشن و استوار نظام اسلامی در دفاع از استقلال، امنیت و پیشرفت کشور است.
🔹
بسیجیان و آحاد ملت همیشه در صحنه ایران، با حمایت از این سیاست‌های عزت‌مدارانه، آمادگی خود را برای پاسداری از دستاوردهای نظام و ایستادگی در برابر هرگونه زیاده‌خواهی دشمنان اعلام می‌دارند و معتقدند که ادامه این مسیر، ضامن سرافرازی ایران اسلامی در معادلات جهانی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/464116" target="_blank">📅 13:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmGpfJTe_RC_cemekOFy7Fl_vGs8gGBeZdGnFMBksD_y5Bgm4jz_MKW51IRCBYBj0SxsKwVzs8vBsTPxumujhAmTKoFfPKyCmLryLZ9EFUUXFH8PMcrL9UI4_662pVGfYFHmasb0LIjWkB16nh0w7KRKa0fxjn7MlH5oeEB6iMHt3a7yzC4cDzWE4yfLxT3z4b4ovb9RzzUFXDuy0129is_A_g71P2iIMdBG-1ennJtRPFKPYL7PBxbnDY3oBOf95PhjrKtnYcxfFEagFROMKZljnhPRR5KtTS6rQ9SLGHcubDMkZ947PwBq9cSzH8bVHK-IuWw8NkYDvkuIz4GCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8J03sx4lhYFyfa0JhI1n6DCTVUxe8EZ0BxbRIYSYOweqiSCg4O8tkRYVPtyQu4xRqzKfbBuem1f_vW13rZAhFhtcCUP11cppxMqnOlx2AYzWCFUPLGIbALCY40slxw68tNPzP_GwNxqzD6LstiaWCh-cs1qau7JAXllkGwTWplriWu7G7p79lqCj4oF9OVKerw7QHKOj6mPd89Q_d9WOCwtzCxJTAKk3x8VE5R7OI9nOkP5MY9h-SQYpusI9wCALUa7QhOLWlea5ahXWrProeJh6wmqBbuT4OoZNnNhopc0bvfRuIAWhwTqaRpxaFDgCB3JUn0G8v57slqsLdDBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGewW7h2VuCfwqj9UKQkhv1UoK_MkYdbUml7ZW-JtAX8m7GygWCKoT4W9rCYa_jy5Au6qS_AspDuyANb9KYaljTIj4TdSGncCCYACSz2oyKD_Gzl3YuAHUwD3W6NnqPI3tlV24pEgyis-juNA_Q7DTxki3jYF9s8jWfqNifPWt3WzUDWinWcz8pmGoZNbBmRxGyehTK49pcQqFR_PhBUuuhvT8-d10XWaZjatGH9pBVfbMVyM3XI9D25Mf3wV6YeNiNS6kpvyrIcIRAKuu0ri-ct1uUNTUUXlXzfN2nBLX9G_rIa-EE5U1e6voP7Diflg-DW0USbnmOtKHMT8VbwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6jyWmUguFcmR71MysNi8lP-0WHMkTvmfdh1meL5-FMxn-YFNl65hvL7LT7_xImiQIw9O28XXpo6F776gRuPoutX0LjFjsQDioaUchuENjcDKhvkKY_iAI-d3RE0A5OFJQ_YkL4ci3kWNJ-wLTbTeG0qseVW8-FoSw2pGJPnydoXepSdzvn267ZtTS8asAgPOjPLFWSyEfDLQcDwqtWC2eBNIlEA1mbVx2HlWAS0uRciRl5irZVTjuaEheD1xN5tmSLMBQblNjUoyVE12PROdx1sVyTMjlL3SWwBs9n7nkh3A69NIar0DcVQ1sRzfJss_dcuYw8-ejTYNZFa_U5gPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPfAWlWkB_v5wlbj5UP9sAPJ1IeiGcIFLamyG3zevQLT1eDgUIIXFFiOfQop33GSdeDadwyiyKpxqaKqIH-fgHmAM_LSPANZR4CfgrrpsweN9165aJRkD3jnskB1aLmKnVSLTh88T2nBPK4wtr0RnZR39oUzv8Yeysd3bsuFt73omrpbfkWzfKHjKqE5G7bC5VNJ4nIPh0voc6dlDl3Y3ahGvF8wTNEEejQzSCB_eaNECXabOThw4HS_iIp1kx_Mws73Czvi-p5STg4J-F-zGkUWgA_vf7usq5Xhy2oKXkFqkxt92x9zy_qXJYLzYlcWW0_Sv427OzSAjcJmXFCThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f41tkvtT0NyVBPbfN1NlryJ1APLf945CJMG4tw8gTimKxOQknL3vVq7VO25FaFObhVQRScotBNCB83TVK96PvVtZKLwit10OJvAfVWIElBNH6lamQbHf_t3i2H1WZouc6-tOrrgDj73n2-zCv4hg7U-yIWT1XcjKci4pjkh-lr6sbIadDd1PBvJ7s7-FnQTZw_V949Vf2WsVj7t8i4ajcpCWTiU1Cxifoj2UHCGdHJ650OrYldaL3AUe-uRChwSi3TAXcQ8j0rZ2Yi4m0Nd3Obiu_XCMAg3hIzuxuMW5JRJKChX4Hct6hvJYS-QENYvWFfT7342iUGzMy5Lp8y8wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCm_JSLou10kGHkLm2t3pT8O6aCJedzOwlribUooBJbENQfuEP-ZtQBAA0tVG4QPdc3CxcF2mACP5FXBtItrmsTZomA6z0I975bVlr466uIh6NRDeonHvQ6s-8bo8k10nwxsVnKHCwycseIIcDzVkvq5t5kv9O4aq1MkdCsMCKlfo5_uato8poE9NLm4FJy45D8sV5ai6WU3dK3fdFlKhYBwtaVqCkOBmv_HFzq5L3eUjo_ZOZXQkL_IVTDmBG7zyx8vAcJubALLZv24mbGVoYifSoVkW8j1ZHeZxu06AMCQnIXCbXqKvgqYBJyRHJ0YwTgmtNO22DgjRoGuR5Ci0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان در اهواز
عکس :
محمد‌آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464109" target="_blank">📅 13:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیشروی ترکیه در شمال عراق برای تصاحب اردوگاه‌های پ.ک.ک
🔹
منابع رسانه‌ای از حرکت یگان‌هایی از ارتش ترکیه در داخل استان دهوک در شمال عراق به سمت کوه‌های کاره و متین خبر دادند.
🔹
طبق گزارش‌ها، دلیل این تحرک تحویل‌گرفتن مقرها و اردوگاه‌های پ.ک.ک پس از خلع سلاح و عقب‌نشینی نیروهای آن است.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464108" target="_blank">📅 12:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d1f5367e.mp4?token=ogLKlVGaQbXlE2thFKOHhBJF5LRhgTecmS0vxXdILGNjRbtgKLKqIiGVwJ-Ei1s_CUUzJOPFyAdHsv2I-bbeDCQHqDmUmx2p86LDk2-LcV8eDt2ut5y8Sr0WQUuIgwpl29aafiixgF1tf-C-QtFEiMBNRld_sen3AtSntWx8S65YZZ7XxijFyv6uGIpqvSUE6QEX8PHVX9ENCV2SWyGFlXKXJNwZhIyTuV5ZgWisiJY7kelmBUFmqfNbP4yCtDzV_2eUOpC7g8eW1fQG0v_0TBGbrdmP_OZhwyVtbSI2di4fNgXpWZM6v0lOA3Idn3MRMZLtm4DyV5NvNiv9Ms0FQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d1f5367e.mp4?token=ogLKlVGaQbXlE2thFKOHhBJF5LRhgTecmS0vxXdILGNjRbtgKLKqIiGVwJ-Ei1s_CUUzJOPFyAdHsv2I-bbeDCQHqDmUmx2p86LDk2-LcV8eDt2ut5y8Sr0WQUuIgwpl29aafiixgF1tf-C-QtFEiMBNRld_sen3AtSntWx8S65YZZ7XxijFyv6uGIpqvSUE6QEX8PHVX9ENCV2SWyGFlXKXJNwZhIyTuV5ZgWisiJY7kelmBUFmqfNbP4yCtDzV_2eUOpC7g8eW1fQG0v_0TBGbrdmP_OZhwyVtbSI2di4fNgXpWZM6v0lOA3Idn3MRMZLtm4DyV5NvNiv9Ms0FQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: رئیس‌جمهور تصویر رهبر شهید را در مجمع سازمان ملل نشان دهد
🔹
نایب‌رئیس اول مجلس: رئیس‌جمهور حتما باید به نیویورک برود و تصویر «رهبر شهید» را در مجمع نشان دهد که چرای آقای ما را به شهادت رساندند؟ گناه او و خانواده‌اش چه بود؟   @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464107" target="_blank">📅 12:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1589e559.mp4?token=ECIsEBbHoJnF6V6yU602VaxeABZikH1WLm7ueOEOb9bMAqs6441rpzQcseO1YwV06kbKQFVa0VjtLNST96Ec9UDwLp9QoOE42L_sQ06RPR0t1fWOyzRgBoeDPFOdZOdcWPL5NWFxWzhFsJoYWs6Q1EYpbMTf42EF0WHvqh77VUUSfKRv1oedvO7GWYZXv9oSAKPacD22ICXhQZTUOOHIoBRrnfOnKkWUGAkqAjZJAA-6goCUuZ7xTklzkbGbMKXEKQHngWTZjmi5KTQ5NLQp_BO2MrcFREv3pHohE63cSoaaBy18yguYbujvMPNF7juISbIZ7pNYNlc_v-wNhRWBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1589e559.mp4?token=ECIsEBbHoJnF6V6yU602VaxeABZikH1WLm7ueOEOb9bMAqs6441rpzQcseO1YwV06kbKQFVa0VjtLNST96Ec9UDwLp9QoOE42L_sQ06RPR0t1fWOyzRgBoeDPFOdZOdcWPL5NWFxWzhFsJoYWs6Q1EYpbMTf42EF0WHvqh77VUUSfKRv1oedvO7GWYZXv9oSAKPacD22ICXhQZTUOOHIoBRrnfOnKkWUGAkqAjZJAA-6goCUuZ7xTklzkbGbMKXEKQHngWTZjmi5KTQ5NLQp_BO2MrcFREv3pHohE63cSoaaBy18yguYbujvMPNF7juISbIZ7pNYNlc_v-wNhRWBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات جدید پاکستان به افغانستان
🔹
در ادامۀ تنش‌ها در روابط اسلام‌آباد و کابل، ارتش پاکستان خبر داد که «۱۰ نقطه در افغانستان» هدف حملات هوایی قرار گرفت.
🔸
بامداد دوشنبه ۳۰ شهریور بود که پاکستان به افغانستان حملۀ هوایی کرد. طبق گزارش رسانه‌های افغانستان، ۳ غیرنظامی در این حمله جان دادند اما منابع امنیتی پاکستانی گفتند ۲۸ شبه‌نظامی کشته شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464106" target="_blank">📅 12:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwTvXFz77Wlw9AMKqEj6JTGu-lesLANfLJwlotKXTh-M--zvolTfYvaV_He2dikZHPLQgD0Jq4fVh3K8e6VpPZiRGU740ICQIQKv3gQ1U9GoVBxTMI5Mu-DrVjJsSDyt0wCdiOvGRjS7i4-uR9is966Y50JewaqE2v0RlQx2bG-P5JzTDLYPGMAcD-YFY6oQEAjMHZSmDLB8F3M4RYyKnIT7t_T0ZV3duPg_rgachxQ9yBHIgMbK_DvadJa6ve3wdP-ErcdoKqFuSb5y--3S2TCNCIpEClzI_HeI0oLuJ9UJC-ORaC93qWAXnvmDJK6nKgL9RwdNJ_JzboqtHiKaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: علم‌آموزی، ادامۀ راه شهیدان است
🔹
پیام رئیس ستاد کل نیروهای مسلح به فرزندان شهدا همزمان با آغاز سال تحصیلی جدید: امروز تلاش خستگی‌ناپذیر در سنگر علم و دانش و دستیابی به قله‌های علم، مهمترین نیاز ایران سربلند می‌باشد که فقط از طریق تلاش شما دانش‌آموزان عزیز به‌دست می‌آید و در این راه وظیفه دانش‌آموزان خانواده معظم شهداء که یادگار شهدای گران‌قدر هستند از اهمیت بیشتر و بالاتری برخوردار است.
🔹
یقین دارم در شرایط کنونی پیمودن موفق مسیر علم و دانش توسط شما دانش‌آموزان عزیز، ادامۀ راه شهدای گران‌قدر بوده و علاوه‌بر رضایت پدر شهید شما، رضایت خداوند متعال را به‌دنبال خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464105" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeR9DafyDWOoMRtS1Zp6DEy2Wzdb7KypUMKBHdLCWCkqrGZ781Pm20nlL22C93yIbkjU_jVgKdee0mxrhMcuNadCqmY0LgJ4ZLhWcQSt17kUB67nZFd-fR41iwAi9OPJTh1Pa3CHgnqhJjeXWMatRfM4jfoFVAmBhF--olhr8INKIHIb8hiIeRqcz3OwULORLuezq4A6wjdI7CQ7eVIdxv-xibgvPm22ArvHlr4FOLFkurgsPIs9RU3IEOPBD7dbF3Wc9D52bTArMnZWW5KBKE_Mf9PIha_NTRHxyaMyaAVhAt2vBZUQ9gy_Zt3eu-EmMIMyvrxxybTJs3sftRcDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس قوه‌قضائیه: پزشکیان در سازمان ملل جانیان آمریکایی و صهیونیستی را رسوا کرد
🔹
پزشکیان با استظهار به میراث معنوی امام خامنه‌ای شهید، با صلابت و استوار از حقوق حقه مردم ایران دفاع کرد و جانیان آمریکایی و صهیونیستی را رسوا ساخت؛ اکنون صدای عدالت‌خواهی ملت ایران در گوش آزادگان جهان طنین‌انداز است.
🔹
حقیقت امر آن است که ما از جامعه بین‌الملل و مجامع بین‌المللی، مطالبه‌گر و طلبکار هستیم؛ آنان در واکنش به جنایات جنگی عدیده آمریکا و رژیم صهیونیستی در قبال مردم ایران، سکوت و انفعال همراه با تأیید را پیشه کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464104" target="_blank">📅 11:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ7JWAmKj8q8LdhIoemuirX18pyVq3pyIvf4T1sUkHtRSnely17YtPc06ATROoJIiZuFanrcysjcI8SBDb_T5jVGwP6TJDHr55B79vh5JcBcEBG-4V9a0rcgfBJSdNsjAnA-x2ofMTFblAklZTJX8hdIPTrBZYo9PTLwj8KYf2pGMzP_dxzpnM21sUCReIsfB7pHDlg_nzNAfPYztRMTFRcwQXxffP76ALd0ix8q8lQ15RNRhhvdCo270eMorBCV0_r20fUP83seZ9U7KzmTWaiPkROrj0WoA2ugTN8IZPRXbwAmWVhPXzGYs8qCMPtkKh4sApEArXUKFWzaarHWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: پیام ایران از تریبون سازمان ملل روشن بود: دکترین دفاعی ایران تغییر کرده است.
🔹
سردار ابن‌الرضا: تولید قدرت دفاعی متناسب با این دکترین، با شتاب ادامه دارد و سبدی از ابتکارات و قابلیت های شالوده‌شکن و اقتدار آفرین در اختیار داریم. با ملت ایران نمی‌توان با زبان زور و تهدید سخن گفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/464103" target="_blank">📅 11:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5yClgt7ombtWe_p4OxdgYe4l94aJ2eez-Y8DPy1_RgNC8ont7QVfS5oQo5YSvkLoEx3HzPLNYR3Bs6wl5cMZx9rUO54oYrVXanW7-SnrkNcDyqcv2ldwPVA4zZ84lYuFplVe7sA-qG50HgJMUQApH2VDZ-wDWMZYRG72POJpwmAjNwxvKXYXzGW9isMUM-MppTlLfSeXhtz83lREUZDsRjU2yReXkS_1y4AS0tXhP8mFL2s67lwg2bNslvvJRB7xOIpJjMX1Cm5Le7DDysNp7dLt6yHX6Q8igCO2cySETe9tOs2y0id8lULI5eLrjRqx66op6dLIx9XoxvbaWAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دانشگاهیان، دانشگاه را به محیطی برای حل مسائل کشور تبدیل کنند
🔹
پیام رئیس‌جمهور به‌مناسبت آغاز سال تحصیلی دانشگاه‌ها: در این سال تحصیلی انتظار می‌رود دانشگاهیان با حفظ چراغ علم و پژوهش، اخلاق، گفت‌وگو و نقد مسئولانه، دانشگاه را به محیطی برای پیشرفت علمی، کرامت انسانی، نوآوری و حل مسائل کشور تبدیل کنند.
🔹
دانشگاه باید فضایی باشد که در آن دیدگاه‌های گوناگون در چارچوب قانون و اخلاق علمی مطرح شوند و اختلاف‌نظرها از مسیر گفت‌وگو و استدلال به فهم و راه‌حل مشترک تبدیل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464102" target="_blank">📅 11:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ae3f81b.mp4?token=Bv8N7WUtXZX4QBad28IhS6p8BeETmhcwanVlWsHckQyMXJG6qvdj3dH8GiMQZy5K3lXwgOxhrHx6fJ8dbuvdOdH5qzNDiI8tgqVDD-1XKKLVcu374tB08iHyTM38ImxCVoNxKX5v9-5vIk9noCgthOAY12B0b8ol-coXH5CEG48oAyWzeTUhFZReJsFfQ1CSNY5WTi-n_7_rwTflCxLM_ox7lOutZCRVrFqvg4r_mWaL04JKCHK2xpqEkAvqFlPy4F5eRa5by3kgt9c-W-a7mgAq3O8oe56jwjzt0jRgzCiSnWk14ob5BurrLxpQ1SqNr_-_gI_1VIK-qm7TgWcYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ae3f81b.mp4?token=Bv8N7WUtXZX4QBad28IhS6p8BeETmhcwanVlWsHckQyMXJG6qvdj3dH8GiMQZy5K3lXwgOxhrHx6fJ8dbuvdOdH5qzNDiI8tgqVDD-1XKKLVcu374tB08iHyTM38ImxCVoNxKX5v9-5vIk9noCgthOAY12B0b8ol-coXH5CEG48oAyWzeTUhFZReJsFfQ1CSNY5WTi-n_7_rwTflCxLM_ox7lOutZCRVrFqvg4r_mWaL04JKCHK2xpqEkAvqFlPy4F5eRa5by3kgt9c-W-a7mgAq3O8oe56jwjzt0jRgzCiSnWk14ob5BurrLxpQ1SqNr_-_gI_1VIK-qm7TgWcYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر ارمنستان در حاشیۀ اجلاس مجمع عمومی سازمان ملل
🔹
پزشکیان در این نشست گفت: سیاست قطعی جمهوری اسلامی گسترش همکاری‌ها با کشورهای منطقه و همسایه است، و در این خصوص دولت همۀ تلاش خود را برای اجرای توافقات به‌کار می‌گیرد.   @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464101" target="_blank">📅 11:18 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
