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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 188K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwga0J5qoQpDy7fdgNWSFyD6jtgsob4p1o6RLRVe_bbKM2Yv986DG5qn9jPz61nvjgCrHM93CyIQx2qqrhFeA3kHuDdkVgCzoq6W_P4PoIdkr3IDxS2oEf9C1_Qvtl04ut-OvLpHEztSWGRp5B4Z-aGQ1nO_GOh8VSWOARsj-j-qQ4m3YKHAX-w4x56IOvL4Z32lxOjEuWvW5y4SlGng_3C52VGaUc2oNK7pmtaqkiRFqNGTKUfGL6o8bZ1U9WEcXUYlgJReQgjS_RNNMcz0OnVd7i8tF-3dtDgT-glPY03ouPHyzYp-dYH0JNPHU-vDfGBpsOsNnj_BKk5DW-GtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kq3T_2CavGcuAVoxUfplfubHnE7OTK24HASaEC8iwpuFC_esIer8aLaXW_7jmxjo5JKMrUz4phhOGo53KOwJUj_wcJVJYwrHnE1hEyokspFho86RoYZRXSv7y6vdMDI_oMj4D6t9-nl9JfXl9u-wyl_e3sVcsGMdAuvmGKwZHA2_uLNzUBTDy0530nxB493NfUxN4I4eP24UmRQhj6y-hdUNnnIfJMA6XsmMwsZOeZCOG2daM0FRde-Dc35HVZQBwe_5r4SOvQytdlO-RdwZ2hO2KWECNYPp66U1ypJmhI9VkAmUf8t9AAxKeEMizMfH3BSeGDQll1J1ZwROVEYF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_SCRTXIZ3SnESPG_wvKLm7eAk5tTQrH-orNFDMkurHTpU_u1G3kin7aokjf8YmViDpBkhlO2bC_HPKmoWgv4kJ53PYBF8krzyLKhP2EtlSagyLyRIg_cb7RBWrL0Y1JsXJIzxYRyuSVy6RgGOFbf-6PBxw2dd6rFBgtQ0BgSxwscMp7mYbscfO0K-sfmdD5PeZS1xw3Rs3bGXYIS0VpaKW9pj6roKFBMNCRhJufaMlOihs36iTzJiEt4kd9OV4BuvRc5ZcsvYrrFMInNiJVo5TUTivMECtYrDOOrvJbzjghHxpvbSfcE7_DQ3_7yLRYe83pWfmjX6I9euk324Rv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjEFofRyaqinnTPAYE_vo6TWPvN4TIy6wuLFCgWDgEnbwMkya8aSpDIAbH-QuexISsrNl7R9gUbLRdDJxc99j39sJm2mZrbDrVXsCELDhFhBV3CXpG2Qxeu7Cme5380fsjAB5NCmpuzDeFSKXHyDmsRAmjvc3m1NPY7CC05XAEK3xC-1e4WW1w9IabxK7MPzhFlBRmsShwpzGG5dZbVS5AJcamy5-0fC4vf8ZFLSbWz41E_d-KqyFQ8B9MqJDctIzsIjU6icovdJgNUxShV5BBNDfPDnjlRngGyUywkxOyLB9NAtj3dMKk8Tz0c9MdIggRuGT1maadokqnwtB6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEK68BX4eNB5pxr7MKeKZ6h1UZyTZDu2qFLQbNM2l8NNPzwIhrsrcB9oRTYKKBDu6PMejC9MpqoRAA6pgxDKlIpgyBDchZjjKNquY2qdYn9KJoGHo5XFFYDcoM1fE6SPJOjeAbrnF4NdhDj1KiKWDBRxnCjP5DjFvagyJv63o9Y6E-UFBa8rRiI5zW3sZUVkl9qmCPAUxRClsB9lD5t7xjkYaR-teTyE1vEQcX86elXamiTWbF5YpfRQXwNke9r-eeaz8Pm95SwqizPPjGMPdlAf6g_0OxC8z_H6FuaaKEkOHzQS_-J4q0p2WzjGYC5FkOPmQG0J5NbDlShTGctk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=qg3NzoZhJdF6arKEgIEIaC5RMkDQqq5q3i_ezhMWk6qWudeMUburY3ngPOyzNwPW3bXujWQ7PtlY7Ze-TYgpRhgH4XkPb8yJXgoPDZlJjlKFr9UlyQYGosGiZQ6jduSDoL8yHJ7tPA9fK1jEybakeK7dJ7nkrd5AGS18ShmiaTGcBde3s-E9P-o1w5SoctJxkMbp5YXazXg6MdCJNs0bgLwf9pxaSriyOTQnFMVIGrmMP1PgT2joAVx1lSHSKzVaXO6ej2tVNH6LpDFsHw3VnkT5JjUbPVg4zclpqDG0PPOPBJe5ll_uNiJAfkaWms7R7ryuNb0tZPKCtkv8ihhMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=qg3NzoZhJdF6arKEgIEIaC5RMkDQqq5q3i_ezhMWk6qWudeMUburY3ngPOyzNwPW3bXujWQ7PtlY7Ze-TYgpRhgH4XkPb8yJXgoPDZlJjlKFr9UlyQYGosGiZQ6jduSDoL8yHJ7tPA9fK1jEybakeK7dJ7nkrd5AGS18ShmiaTGcBde3s-E9P-o1w5SoctJxkMbp5YXazXg6MdCJNs0bgLwf9pxaSriyOTQnFMVIGrmMP1PgT2joAVx1lSHSKzVaXO6ej2tVNH6LpDFsHw3VnkT5JjUbPVg4zclpqDG0PPOPBJe5ll_uNiJAfkaWms7R7ryuNb0tZPKCtkv8ihhMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1yZxVZAVjFUCJzLHkGpUOPYrOUgi0v1GF5HL4d3EgAMglV4yLhTZGMG1Z4bFSje8Nt0gmjvzgK4G1HBnSkBhBjYefodJjJxSuIAlNcJ7sLtYGrbXGLWIlEh2N3IbUSGJRJMY_ABqszaTtyJK_K9rzhbVYfh6ws3KYb6l3a60U8-AebvXWxCVGoxGBmXcCwx65QQY99a6GCMjNFPjBTCLY74_dwiA3-E6U93uQF7AgY1taeqfrWUTW0xBg8Gx_-ohouDLC2mF4mBzpFq4_-NtjK2XD2hbgSEr0Q3--2dmrwOoABWU05RDWhBy-2DFuSUmXBnz7dttq9aTg1M4RfO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpNvlrwal5onobwpa00AVDt3jGHgSXQ07N1uSVFfO86OYqSbd2Z-HNCJiA2MjQ7-hxs79Xs1TPOcICM0gHceytzwmP5VXBiMISCqrlXAjwg-p0MGmZS8B6CK9BMgyfMc-kJNda-KtcOloItWp9EBCc5oUuT5HI40bTeRwQOuSt04B30mHH09LCwTDwNEP6UtTfEjW63zw1Sk21tT53hYb__4bsowM6LvMFEUxPMabzVLcvdY0Pytjrb8mzza_tw5ZsTjKxZGLpSdZ0a--x8hPy1AcLsDd24a2osBZKqwNJruAi_2KzFhw5h_bpJ3ITT2XyOsdrq2Ns_XtdbcgYNYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc26XP4FHTfmUXORlGemxynOZdoiXDZK_LJ3YFOXzPYdabk-iic2wtI5vMJfpXQFcmmTz3JBlmTyIYlO4zEulFv4znN8bYQcjlIvYhdD_EzMj6y3kBIHTYvhNzqIJLbtF05a2Y5WV9aURasfuKrYWotv-iQy8Z1GGIA2f5Dexxp3Q-WwXN5xpsrBZj-_ugu1KLy7CkP5OMJ7pbGPrw8OAXJHLNaBpzi4Nhve8F1Hng4VqN1gHZmk94aZmeU-K1lU9S9yKnL4ac2stxZoDQsJ-zcJ2Ozx_IctFzLdSxGL9oqYovKvEM3VBmKMguQ2TkfAjxoCUJsIZkHF_7UcHx4IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuZYBnVhww_fH6x1CUKrSE7eU3_Q0j7mh7durpNcJPZJFOJI8SLvkOU400n8K4GkOqk_sQ0ERrxikDBYZ3lUzO4aTotynjf3mNbMqeZZK0RfM50B9t5WLc_-1MFBC3ACQb0Wv92NQxgT9DGEqOXVPi3BbQ_7c21tV3urIi5aM2teYlsx8tToLyiw12Z5ptL2DiH0wrfdYn210UsC6_iBsOXbMOz3RvS9FX8YnPFcIotDRM-CVDGj0hRfDJmqxj3Bakequ_TkWrbsG8c3b8bNvDu_-JLceJyT-wo0nEHtWR4g6MGovm5vdx7sK-ZANyPKOINMjALnnRZEKQinQfnKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=oGYmXpMgE4aJR1cM4r_P8FkSI4QkJDu7ffs95G2eyoaQF8nBxivznDLsksjpc8JoRkV3FG6P132PjXuWEtY8nzm9x-xWwLTqIBX-2GGcVrg3vaWVO581nQkeEPqucYCMHtcNxRx74086O_zuv1NDnVEnJsil4g6Yl3imCMkDivogP7R7IFo5K_2a-bs8e8Nb1hbpzvxz-PloJ5kYJqXiQWUOxbBs9Id6fPpzAoBJfc8u6avuXQdR1E-tAvS1FUCCW5IitOywrGTMsvcXSNNHJYXVsKyZ7rO9pCsLEB2zaoExRETGxk2Jfe17fGDGfhsh-bjlata2XdQjRMcPIw1-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=oGYmXpMgE4aJR1cM4r_P8FkSI4QkJDu7ffs95G2eyoaQF8nBxivznDLsksjpc8JoRkV3FG6P132PjXuWEtY8nzm9x-xWwLTqIBX-2GGcVrg3vaWVO581nQkeEPqucYCMHtcNxRx74086O_zuv1NDnVEnJsil4g6Yl3imCMkDivogP7R7IFo5K_2a-bs8e8Nb1hbpzvxz-PloJ5kYJqXiQWUOxbBs9Id6fPpzAoBJfc8u6avuXQdR1E-tAvS1FUCCW5IitOywrGTMsvcXSNNHJYXVsKyZ7rO9pCsLEB2zaoExRETGxk2Jfe17fGDGfhsh-bjlata2XdQjRMcPIw1-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=mRlvbL94bkcf-rRz1IvucBX5N0NL-BHRAw9_QhbYEdM2PEzBgvp4bxOKAmKnHjCjD85Xik9C13MJSq46hObaadiUDsrIuS0SLP0IYTWhgYkjyuliHOYWB1aK3koLsIdX8yVMNzd7kbz6j6kG82vb0GGQo5qGyJmYfXCcc4EK-4bIKpbjAkdW5_GQOgLukdnx1ZRyY70hOe1QFR5fYQOjgY_67uHaMF47FnbiJxXeAZRObetmC4mVa08Tkcxv1-6pkar71hjYl3wWq4SBGLyFp9oWgTxnTVqYoyfiXbqx6DZxqfHo3jWWhy3Ube0AjqyLcVVrwJw5zH41KDULuTU_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=mRlvbL94bkcf-rRz1IvucBX5N0NL-BHRAw9_QhbYEdM2PEzBgvp4bxOKAmKnHjCjD85Xik9C13MJSq46hObaadiUDsrIuS0SLP0IYTWhgYkjyuliHOYWB1aK3koLsIdX8yVMNzd7kbz6j6kG82vb0GGQo5qGyJmYfXCcc4EK-4bIKpbjAkdW5_GQOgLukdnx1ZRyY70hOe1QFR5fYQOjgY_67uHaMF47FnbiJxXeAZRObetmC4mVa08Tkcxv1-6pkar71hjYl3wWq4SBGLyFp9oWgTxnTVqYoyfiXbqx6DZxqfHo3jWWhy3Ube0AjqyLcVVrwJw5zH41KDULuTU_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=pSEqR_fq28eC3Ve4O2zw6wHsjG-SEeU8q7A3PBb2lQ1i9MhRp4SQKAv6ob63Gf-eo4J8Dd2sIIiRbMtC01Q-VNjqd90aaV5KCvmoLgaXPcWnOS-tRzNKRMgoY_7EmIzh_eq8CIqFkpsbV5iP8SoVAmlBBhXykVuqFoyL_l_FE802Fdxgr4QD5oy976yyDEh_Kcg0qScSFBp7ND-_y58Nj-78gPODenEEn_KtNgmiFCEwwroRAgfROE8BowNC-qKDfu7FZU4cBqpc9fEmMwCFrZBsJc83SaO9refA3S3pfjSchqsVtCUWzoyQEUnpslGzCl0Sahyo_5aRVx0aPzfuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=pSEqR_fq28eC3Ve4O2zw6wHsjG-SEeU8q7A3PBb2lQ1i9MhRp4SQKAv6ob63Gf-eo4J8Dd2sIIiRbMtC01Q-VNjqd90aaV5KCvmoLgaXPcWnOS-tRzNKRMgoY_7EmIzh_eq8CIqFkpsbV5iP8SoVAmlBBhXykVuqFoyL_l_FE802Fdxgr4QD5oy976yyDEh_Kcg0qScSFBp7ND-_y58Nj-78gPODenEEn_KtNgmiFCEwwroRAgfROE8BowNC-qKDfu7FZU4cBqpc9fEmMwCFrZBsJc83SaO9refA3S3pfjSchqsVtCUWzoyQEUnpslGzCl0Sahyo_5aRVx0aPzfuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URjw9chg6bovtx1KaXeklwhBmHhWPiD1MROTcPcgGgHn5pxHRM-_dXcHwTDQT15iYnPu0oWK0RJSOmKg3xWnCzWKKF1-hQuNr4rCmwcZsmBi6FuTT9x_chyzwRnj4occ_1TEGl5zFMA0FlrfoBFgcVgffrS880Vm2tHvXqGIglNODkFfRIQ60x4GfLqqcGorGc8q0uwqo9235mVYmJWqYNcqL4Y6BHbYICVJSnoQcX2BES1Ii4LKIszO17CtwI4JrAwClUo1IR5aB1G7ju9gj00O-oeBqepW46dda3alY_eC8PkLTFVWsDdWxTLOhsIwIlBdSXIxhdfd1sQ9mjjzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAsor_9r6Xusezntag036dRlZkIQiy8O3ZkUS2Zo0FiIfzBhRUXSlTUOJrZvaWriw6p3W3Sz3JJsV18jTpPSGud-aOsBdBVxlESFP9e1Jm0Geuxwj8hEsLerZOWVdkWlsxZsBputRZWNjBQZ0aQD4vH302wotUUwHDZniHTOeETfgiBBs9FvVH2V_WybcoZMG_AvRbvQ-jL-zgSWjsS7icHzZ1qlUzt2BsJlDTEQN0YyqHCQtCbY67cb4RkUhzZ-Q_rqPeRBpZFKo5Yrf3E4CvF6nDz37_ngmi_Q4jcGNpgI_Kvab7Qhu7yNDG626m4MYw-ZM9peKjlXYvyioky8Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=q0Sib7hFZ_fu1MXx2-XgOS5p5WyOH460LSfkEZS6k3jk6h9J2N10bCbtEkozr-msW_Riz422nAsZrX5XSRIuXaeEUxD_Zag2BSv2WnLi31tu45dcSFAbK_fHFMOkrT6h5nm9c3Z5__JE3sRkSa3CcWFYmTYHCRuHXhL0gk3e1EQKoNqDjO4QcgdipMAb3opplsciJ0HRvLrNrIQd53K1ar4X-srD_ufh-9yrHXkKpQhXdy4xHFugE4LlxeR6yiZIOOnWeZ3YE1jE6uv-VMU5ntl6-eHmH6iXGiMbb8fTgtR-qv5ARNo6X0lpxS70zYYXO0G3DGkXQST63bxApaYrIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=q0Sib7hFZ_fu1MXx2-XgOS5p5WyOH460LSfkEZS6k3jk6h9J2N10bCbtEkozr-msW_Riz422nAsZrX5XSRIuXaeEUxD_Zag2BSv2WnLi31tu45dcSFAbK_fHFMOkrT6h5nm9c3Z5__JE3sRkSa3CcWFYmTYHCRuHXhL0gk3e1EQKoNqDjO4QcgdipMAb3opplsciJ0HRvLrNrIQd53K1ar4X-srD_ufh-9yrHXkKpQhXdy4xHFugE4LlxeR6yiZIOOnWeZ3YE1jE6uv-VMU5ntl6-eHmH6iXGiMbb8fTgtR-qv5ARNo6X0lpxS70zYYXO0G3DGkXQST63bxApaYrIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=OqHwlm37ljFum_baSExyp26Ob-AX55s9eXuoHkf2aKhqeiwZweD2195-k33_vnFCIjup__j4OuGbuoy3vfiYH1e4T_kuxUM5Sh4k8tjkzYLfMhqq7uYJXuTMn10p3UA5WF5Ooy_-Uo_xOoVpBGw3OHnQ0RVgPaixQ8ZagVqmyafJIepPSrRsBh7v1VhawM9k1n5magkU9jaRFNji8yAYWo_xiOiiY5-h5xzuA4ZfBtI6-CIESl8szJJLT9o6MxeC9AxCL6VGruNanJWOlCROytmkC8rmL4MB_6klMipD8C0t3El3feAMrZFWiduLn75wg08se1Yfr3cjbmFhWjIhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=OqHwlm37ljFum_baSExyp26Ob-AX55s9eXuoHkf2aKhqeiwZweD2195-k33_vnFCIjup__j4OuGbuoy3vfiYH1e4T_kuxUM5Sh4k8tjkzYLfMhqq7uYJXuTMn10p3UA5WF5Ooy_-Uo_xOoVpBGw3OHnQ0RVgPaixQ8ZagVqmyafJIepPSrRsBh7v1VhawM9k1n5magkU9jaRFNji8yAYWo_xiOiiY5-h5xzuA4ZfBtI6-CIESl8szJJLT9o6MxeC9AxCL6VGruNanJWOlCROytmkC8rmL4MB_6klMipD8C0t3El3feAMrZFWiduLn75wg08se1Yfr3cjbmFhWjIhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHkWEUrIIut7pkxSvC2XXjJJliOpkJPRehUxW-aEyFD7qTF7ijF9QMfLLp00mLjL15iVzxYaSAgacpGQdpSg2HGiHB0b4aZWCjKh6nh1HbRODORDVIst4NzacJv4EuG3rKJhg-4OU83jL6OVspCcLWpbR44imaXkJgBpH4mWfENI2Z7hiuAJo3TrRvvS773k84ELBvVIokVQq01CfoVfwbIVaYWozBSWCoF9kiHJXUmFLnZyJzdMzRJh4_CKgkSiB1F4X6tHicyT95vHSZmY5Kk54WMQOo71ergOjZrbODmAd6ejyZW0AuxfM-db8qaVQUglBwUpVfyccjdd4vIREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYDFF6J4JN64fXN-hdf-rSWOE4mcfbC7vwFg1Uc_l6YMpad12cCLYIQ-5V-vGc13ct0DkMIu5aTFhtCvPxxs5r0lcV0eCvY-PDHV6dE4DLq0tGEoI8tx11eD1mlb3fmB9UhqZu_qsHf29Jxa-8AgULqkicDbzqlVGp_3YYAxcom6zyJMlm-sefmHNmcFFuNOSi_DzJrs3uUtj9EXAnphz-6vVrHCJIxmzr2L5kdwG8CrxY22Y4qrggw7gZcNnZvKCFWc2iBY0NOVy1-MGZJdTafWvk2gDkguztfoe-ZEppMNMgozYKl5eufWEdzyWXyrc6gedXiKKFVCUMmb_n9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0KCh5OVMPy_2XQ96jqezDe37c-kemwOxLtjl8arXH6nXq7btpjdPT5zHlfb8eB5Mq8Ny6Mub5fFzcHqxJciHBk4OEEy4m8YdMGEtW3GG8Nj-2odx_RWIqD7FHdQR4_1wkaiqzB6nNFfOROlrtbHLjhv2xB6ZHazfZDgJnmHc6JHOL9ER5Jid7D8j9Q6IiPEyc8FpzUgddYbfXX7oY3_TVnhndSQ-YlvNp1FE7dhlJY5scjTzj35c9AM5thFkXslsCo724jx_ZjTjwWAKqc2VCI7xgaJ0Q8G8rX_7RU_1YCRm3SwvFX8wO6yr-x3guy5bZhLxQrA3jwM_HrMV8PIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XEJnZcIZpvTDz05vs69jLdmK_XdrwPSYCpT1Tn5PN43ypsAOtsf-eM8pWcFy_bQwXAopcgKhqoFQ5Ebd26A3NRWnj6OyT5xZRbQla1YlvgCucpHm93Vyg1vzRFY_5A9uFkMwfzCng1_3Inub_bNkiUjfXzUSF4FyM1GNHa_X980YxGVhcZKqfhL6GsQsxQkSsshBKqikplICKg3FrVszNKtYPVFEplQ-4LlYv0qyTGnPvIe2E6MuGSU7_oSWT80Z9YqQbMjdSs_diGDDm7ofihFhHIxym-wacQtai7s77ns4MJwAzPg6FHrkb6pSsC75_431t3a_GUeSXFe24Z8iTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=XEJnZcIZpvTDz05vs69jLdmK_XdrwPSYCpT1Tn5PN43ypsAOtsf-eM8pWcFy_bQwXAopcgKhqoFQ5Ebd26A3NRWnj6OyT5xZRbQla1YlvgCucpHm93Vyg1vzRFY_5A9uFkMwfzCng1_3Inub_bNkiUjfXzUSF4FyM1GNHa_X980YxGVhcZKqfhL6GsQsxQkSsshBKqikplICKg3FrVszNKtYPVFEplQ-4LlYv0qyTGnPvIe2E6MuGSU7_oSWT80Z9YqQbMjdSs_diGDDm7ofihFhHIxym-wacQtai7s77ns4MJwAzPg6FHrkb6pSsC75_431t3a_GUeSXFe24Z8iTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=ppeImXVU4v2WzLuS6RMz2UNuDoHm5aaw3rVOppy7ZGCR-qhQkByHCRLdAkDFNncdoBQ7WC9TnBIUlELn9ZOXP6ofIMlgZKl5SOZ2bVNZKLk4ZRVGx3UiLdkx3aiSE1-3KDUR24M9_2MdNzHlidrN3aIYvDvDIK6HjwWzqzIzR6WFZA_FzFiJiA7mIqDYlSidqpFQsmijvOOnVi8NSRfI2FKuutX7ywML-FAUqtD5hSl700QNqBnNykXDegWMhLQSGaxpc5rI3KLzCoVZK9F-l6JGP-jLXXL9Qc6LovqwuSk8Nij5pwWR2pCnV8pCQOacQiAU7SLyXb4OiQng_WBJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=ppeImXVU4v2WzLuS6RMz2UNuDoHm5aaw3rVOppy7ZGCR-qhQkByHCRLdAkDFNncdoBQ7WC9TnBIUlELn9ZOXP6ofIMlgZKl5SOZ2bVNZKLk4ZRVGx3UiLdkx3aiSE1-3KDUR24M9_2MdNzHlidrN3aIYvDvDIK6HjwWzqzIzR6WFZA_FzFiJiA7mIqDYlSidqpFQsmijvOOnVi8NSRfI2FKuutX7ywML-FAUqtD5hSl700QNqBnNykXDegWMhLQSGaxpc5rI3KLzCoVZK9F-l6JGP-jLXXL9Qc6LovqwuSk8Nij5pwWR2pCnV8pCQOacQiAU7SLyXb4OiQng_WBJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Bduw2RANCL4XTlXe-LGGYfvS1WxURbP41tKpMr3tPZh7chHBPh8q79ChGwAmdmalBRxV8tGGfOsHmrsgAFqdxxU3M-QNWoBk6SsxQLz-kdk4jyHovM6k-pu4laVPX4Emx5bWxZXqiACRydwvNc_NdtuRytyszici3OX9GFa2HB5KU9rwAzHEPx_RL2mjMEgxi3pYOkFiTJulH5peH29RD0ogOcGl_cj0kbOZXnG4cyTLHGI3moY9FUPrWjq0BlRpVjcGw7vhkVD9s0MWyCgwS48LNpNcwP713j9ulr8iNfXxkg6uk-NSWvbkNoz44VIu__rBhgNqfVK1GWMIfmZ8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Bduw2RANCL4XTlXe-LGGYfvS1WxURbP41tKpMr3tPZh7chHBPh8q79ChGwAmdmalBRxV8tGGfOsHmrsgAFqdxxU3M-QNWoBk6SsxQLz-kdk4jyHovM6k-pu4laVPX4Emx5bWxZXqiACRydwvNc_NdtuRytyszici3OX9GFa2HB5KU9rwAzHEPx_RL2mjMEgxi3pYOkFiTJulH5peH29RD0ogOcGl_cj0kbOZXnG4cyTLHGI3moY9FUPrWjq0BlRpVjcGw7vhkVD9s0MWyCgwS48LNpNcwP713j9ulr8iNfXxkg6uk-NSWvbkNoz44VIu__rBhgNqfVK1GWMIfmZ8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=H3UiG_3zI4bnPEsTPQJ3BDwWcSgq6q2w9Q50Z0UPT-tcX7QibwL-sMiYvt5ZvIBBlVEwYIZrOsalvNIN7sD1UagRDhrNvOAGZUu2tGYpT3znwUwBoMsByM--x9wc0D3hWJ4TwgiyAlhTpJM0-iIm3HigL227tT_xdDyZdBD9MdAXKmaE-WXS72uBl8db8mMTtOS3OlPI5IxuawfjF7L4K9YkY65iBZJYXd-5jONIvWRm1QO5NE375aahJrFZIh-eQeX9dSSgM4NXgHGwO5HTTP9D9rYmLaH8RAFIBncnV7PbH78eB0Chpf-ag0vvaP7SEZbrlQoqV9qjNHXlkZrJwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=H3UiG_3zI4bnPEsTPQJ3BDwWcSgq6q2w9Q50Z0UPT-tcX7QibwL-sMiYvt5ZvIBBlVEwYIZrOsalvNIN7sD1UagRDhrNvOAGZUu2tGYpT3znwUwBoMsByM--x9wc0D3hWJ4TwgiyAlhTpJM0-iIm3HigL227tT_xdDyZdBD9MdAXKmaE-WXS72uBl8db8mMTtOS3OlPI5IxuawfjF7L4K9YkY65iBZJYXd-5jONIvWRm1QO5NE375aahJrFZIh-eQeX9dSSgM4NXgHGwO5HTTP9D9rYmLaH8RAFIBncnV7PbH78eB0Chpf-ag0vvaP7SEZbrlQoqV9qjNHXlkZrJwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE0ZIwl56wnR80nfKMmZOdinca-NLZYsBgC75t8mZcIpRL1LNiyaSDLl3bhyJtowhol2l16vOrWAvLjN1HmizVp0WEVNVOiKAZgmdbvWFeVTR6qMr1XBGy1wUfY0dty9AIeFZ5PnU9rmmMEi4UqbAYEkoitzN0vD21NYH8ARCIYLqnJcoqlvizBP-7lF2UcJvL4NtZDnO0cvTbIgoONFCGQfPVnd3UzdIdLSH0EEmQcDOCyDS8GC9KaYs2cyUL2ihACb59zbn43wl5m03lFqCcp7FDixS_LM84FBzQ32iPLEjXBPMnhJ8avLUJeMnqTzlMYluFWK5h3kdCyqckG9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=c4iKn7CNdSuZQ08MQMQBovE_QtMvLDOhhdL4oN4icOmXwPYuFsAnw0WxQHUPweYk_DKfm88bC1-fSJLADZ3lH2VC-KYvtsREbTdN29vEG3NqtcYQyZEhqQAS-y35LdAPqCCit0DTjipUE0ht_fufvRHKxmTtDVQmWfhxBw359xJJ0x3QNF2nQ8E1-h12qKmBizqTTERynmWkqzdxsjrdyTa11aWAhhGC0AnZ_RL0SH1fz23fmOPzXwa0GGAnl0vPXobVcPFQWdpfqB68P6Qvaic5XUmjxvmJgCxQ8Bw-pEe3uas5wKSicREPgQ9qFBCHBLjcrHXLmg5TeIM_f_pyBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=c4iKn7CNdSuZQ08MQMQBovE_QtMvLDOhhdL4oN4icOmXwPYuFsAnw0WxQHUPweYk_DKfm88bC1-fSJLADZ3lH2VC-KYvtsREbTdN29vEG3NqtcYQyZEhqQAS-y35LdAPqCCit0DTjipUE0ht_fufvRHKxmTtDVQmWfhxBw359xJJ0x3QNF2nQ8E1-h12qKmBizqTTERynmWkqzdxsjrdyTa11aWAhhGC0AnZ_RL0SH1fz23fmOPzXwa0GGAnl0vPXobVcPFQWdpfqB68P6Qvaic5XUmjxvmJgCxQ8Bw-pEe3uas5wKSicREPgQ9qFBCHBLjcrHXLmg5TeIM_f_pyBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSgIW6Sk7ysw_5fyEkIkPuPFfaPvnCz8-8jv1eBkMDHeOhZdp-eOl6GDo2n_2D8k2yb_Vsj5cYK4Nig79z3Yf44SCji4xX29vIppezlu0cIqVixPGO2RAUXPsKlZ2ajtsy2tVIG4VIIX8QpazXFY7H_91o9Hy4PONpBseGRRb_QOcfWqAYoTj9nc6UcO5wUA7nJuc4F9tdatJuYTckJburT_Vtic2KUNo-mOZHdKRdqx3s8WTO6ZCo11gJlWeG3FzopvM2QAf_XvCDF-EU_vwZna2OsTnCPetZt9ezVY9BMtHNR8249ZaTXlFvdgMg-GQkPCFLxOCcRw7WqbEa5yVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmrADzDdWdvU_5ryvUmMSud8dVVv1jJFqt8iX9gVyxQqJtMSlYsuBZ4Y1_NSAAlLYw7PvXBjKbuSJbOiJoutQxA15wyrbVSdzZjBk6RKT6M6zX0ox3_DYZlyphosekIX_rDgbNc6mfaDceS5Qf5S6M_usb9zVSIDb87ziY3ibg4xFFGshSJAx-IYESH_vo16y1M5ijLvtnTHWlXs0yWcBVza7G7hQynEZFJNgDeBVD5JPUiJOo63rI3N5Kwr1VnpvMSxVN_6UFdNaUvoSReitFiwL8FcWaVllj1YyxC1Fu0nJNggPZhSewHTZrrkUorgQzvz578EEfWvLfRusq475w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQFNTwJWESV4HzQJeoxvTam3RdruPHqkGG5nIA7K4qP8PmkkwUBjuq1IIZ66_fpYXc11Ih03Ama3nG7-UCFi5ssVkwocYej2dvhVOqUsNTxRDsYuXNQ5agOpVSdr9Vt4YUkXHxNBAlyODptEWwlFK6DALWsdoSm3WsIynX6nZ2VpoGT4bOeIfw_BQA4gaO1FfsOKs9yYlXyZCOasLtteBClmh30BZBqQYu3MQP8fPAya-RuNESXmnKkGacM4uEsguRWHNCIQGhiVRs-hPPnwXcjwffP_H2K68f4YUZzZ8Cn-N9sgjewUwk1ERZG9215Qdoi4JQ0KRXIB2JyjmJhfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCzpLA6WCinkr5ObfYSRWbmQ4xdD5AO8J1yHJEZChKPOwTdIclE9DDNU32wXeHYsQwbJsLeED_95g3hBfmlqRydm-29mX5l3IfByE2fgjZPDCG3Sxmpit0q86HJHTFmSx_lyA1IXTgXh6rs85GY88ymxFD2llSaPjTzaMkisD2ksz9tmpEBpFXLHCDiIRm2ukFNJMglpI5LEG_oubvAToyWTWtDSXYHsybVJAhVmHO4uTh9gM89hR3X0egE8sp5XQgUTK9SGI2R4NLp6gLNcJyoh2P-uOb7FnpuO20A74_t3UEHv_JlIdSu2_1rX1jVWazkwiMgyzLo7oOx8OGxsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=JZAMyUM6zlNj9UBMoMM7G3l2nLi2oc9CbLDk9mfTokayzRw81z-xQ7k_6jVieGuC9rdf46jri--cYJXLYo6WkXxrsj4t4pnsYXNeM_uaVYhZKA9pdBdamEcnrGus2PVtus-k8EfJ_xOjTLKkl5nAkCIQAcHpoo2rUHkavWablnUJ-mxp8V8Ly4FnRrc1H0vXkBMHhHlZ1kzGopfHPG4DKt10RRSUyGWebG9hnSTPaQEm9nxHHEarS-J-GUtbbAHqieLF3HprXVptgm3XcfNv_kIpe9L-AkxMaLRy2t9BjfA5PEI_mQ0OYZxfU4sCsJlc-rbZna-QOyPP714SDihnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=JZAMyUM6zlNj9UBMoMM7G3l2nLi2oc9CbLDk9mfTokayzRw81z-xQ7k_6jVieGuC9rdf46jri--cYJXLYo6WkXxrsj4t4pnsYXNeM_uaVYhZKA9pdBdamEcnrGus2PVtus-k8EfJ_xOjTLKkl5nAkCIQAcHpoo2rUHkavWablnUJ-mxp8V8Ly4FnRrc1H0vXkBMHhHlZ1kzGopfHPG4DKt10RRSUyGWebG9hnSTPaQEm9nxHHEarS-J-GUtbbAHqieLF3HprXVptgm3XcfNv_kIpe9L-AkxMaLRy2t9BjfA5PEI_mQ0OYZxfU4sCsJlc-rbZna-QOyPP714SDihnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=eb9RblwmG6pktUKq1fT236RPKO8d-W_A1MMdjXcu-HgJ6btp1x_x3QVTYN_sKvm5v9ExqfnYuSOmoiZ3ExTHH_3WEkLbnk2Vq_SugU7y_q_4B3nxMpLgpVV-Yvqy6F8KBSCx5r59a4bjE7VlzT2EKpj-ZsMBLu5rWhw_-3Ds9txaOqtJnPv_hhl60I5-6ekZxfKqEHy7vhMwVPwPR5sJwyoQJ6tW7qXPaZewoQFRUyZhNMEwq-t1Tyi2rVIegDaO-iF4rJujMoupVae_AiXIGvj8hwoLECoF26NZwyoxHC6QLfRJJf8xt3QNIy70D7W0LOvG1mxFGVfE1i4vD7Ma-QLrZXBBmiOYA7aOdsJKMdM3_K_8VIzBiWcxeLlYLLCovJ0As_2NlgHbLUFGFOtuJ_Lt4Sb8z2OS-biFFQHp1HC7sbCjA6vI1F0YyWn3zEUP_qbYLhaosgmIlfCSfLv88N0RwOiN-66PZg4T6Nd0DPukRvXDRsmQu1nnQtscbJkq43LEJakc4L8YssFoL4dgEVYTqJ4K3lcvtRrwopw-S2QEqPqPQrjkSpu6WCuJdfnvdjjdkQUXi6d3V9jmX4_q93RC-TMytc6xDwdpTQvnD9IPsPZ-NshWuHetVT-Njltp9UUUW1eRE7fHFIzXZltgaZVLf3Mkfz-l4WLCjDEEkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=eb9RblwmG6pktUKq1fT236RPKO8d-W_A1MMdjXcu-HgJ6btp1x_x3QVTYN_sKvm5v9ExqfnYuSOmoiZ3ExTHH_3WEkLbnk2Vq_SugU7y_q_4B3nxMpLgpVV-Yvqy6F8KBSCx5r59a4bjE7VlzT2EKpj-ZsMBLu5rWhw_-3Ds9txaOqtJnPv_hhl60I5-6ekZxfKqEHy7vhMwVPwPR5sJwyoQJ6tW7qXPaZewoQFRUyZhNMEwq-t1Tyi2rVIegDaO-iF4rJujMoupVae_AiXIGvj8hwoLECoF26NZwyoxHC6QLfRJJf8xt3QNIy70D7W0LOvG1mxFGVfE1i4vD7Ma-QLrZXBBmiOYA7aOdsJKMdM3_K_8VIzBiWcxeLlYLLCovJ0As_2NlgHbLUFGFOtuJ_Lt4Sb8z2OS-biFFQHp1HC7sbCjA6vI1F0YyWn3zEUP_qbYLhaosgmIlfCSfLv88N0RwOiN-66PZg4T6Nd0DPukRvXDRsmQu1nnQtscbJkq43LEJakc4L8YssFoL4dgEVYTqJ4K3lcvtRrwopw-S2QEqPqPQrjkSpu6WCuJdfnvdjjdkQUXi6d3V9jmX4_q93RC-TMytc6xDwdpTQvnD9IPsPZ-NshWuHetVT-Njltp9UUUW1eRE7fHFIzXZltgaZVLf3Mkfz-l4WLCjDEEkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=Ld8AMg6B588i1ZqtCuiQfZoddGqe-OvKdrDkxMv4wCZITsbh3b9kEmeNURl5CNHoVzyZY-FkLB8KijAWQi4HRXHJXkk7J8cWcTHNb7tqrPdGqEMbMPND-JRLef8IO_F-0tyVSimfzrGHnQzTLI4P3-h459_V7N908bqGVDE2JCLyW2DLId92axSLOtcPtM0f2GkWW-XC-dURpqhYfgeqsXkjU3GmAZrTde_r8PTW-fL0rQp40vo9KRqApTlEiCd9yfi2RHMlFbuOgL2tmLyRkliTYHH4R3Kza9KeM8utMRpW25AqpENNdGB2anO7CrxHDHhuW08_RdZV0Lu2A1UrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=Ld8AMg6B588i1ZqtCuiQfZoddGqe-OvKdrDkxMv4wCZITsbh3b9kEmeNURl5CNHoVzyZY-FkLB8KijAWQi4HRXHJXkk7J8cWcTHNb7tqrPdGqEMbMPND-JRLef8IO_F-0tyVSimfzrGHnQzTLI4P3-h459_V7N908bqGVDE2JCLyW2DLId92axSLOtcPtM0f2GkWW-XC-dURpqhYfgeqsXkjU3GmAZrTde_r8PTW-fL0rQp40vo9KRqApTlEiCd9yfi2RHMlFbuOgL2tmLyRkliTYHH4R3Kza9KeM8utMRpW25AqpENNdGB2anO7CrxHDHhuW08_RdZV0Lu2A1UrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=kvV2SaDpMuQ80v8Prrq8ldxItJl-ja8ohmmAMJvDGBJy2-ZhNUHkbQOFZ63K7Ia2bbwInbk0bXoVlJcvd8Q4-P5Vkgl8Ax6E6Obr2jsv7ZZqEk0q8w-OHziPrpCebIpY1Fmx_x3so1BZp3i1FFEJlAexbRu85FoZBRkrqZxXU_lC1t-HCoYuWJimClqMybZ93dslrRSFJOXdmP0DjkXy7Zfy9SGwzMIjneu47XRwCumH8pWWHRZKTia4sshawKkKMKYNcgJAgGLaO1OrZ4krH1a38pvyhCTQ8S6Puh4591oPvjlSnjKfWPvKunE9rfp60LhaWTw-WikObl_cfet6Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=kvV2SaDpMuQ80v8Prrq8ldxItJl-ja8ohmmAMJvDGBJy2-ZhNUHkbQOFZ63K7Ia2bbwInbk0bXoVlJcvd8Q4-P5Vkgl8Ax6E6Obr2jsv7ZZqEk0q8w-OHziPrpCebIpY1Fmx_x3so1BZp3i1FFEJlAexbRu85FoZBRkrqZxXU_lC1t-HCoYuWJimClqMybZ93dslrRSFJOXdmP0DjkXy7Zfy9SGwzMIjneu47XRwCumH8pWWHRZKTia4sshawKkKMKYNcgJAgGLaO1OrZ4krH1a38pvyhCTQ8S6Puh4591oPvjlSnjKfWPvKunE9rfp60LhaWTw-WikObl_cfet6Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUIBJjYNmDiXDzRTRkRwyDpmbxXxsv6s1hcVBAjuDwF3MEoOixEySRmjRe2HccqcNTEff4Vm5pvzVznmStjkX0stkP6D5tTGJHvwjqPpWq87_w0ZmHGXC5sO6iGMqvDMNjjOD3udHfbWGRLpIZeFfXc_9rzE0NCAn6O7dMRfwYa8mtOyUDMBoLnK4JcXSyiyM_cAHM2JyfDF2vCBWivIkA5H0gvcvQIyG1V-vNbR5j9GsvQawO3-YNdBd04qNgOf3ho_vI0WK_-LE7sn9nRXFuwKAMhqIdQtyznM9oBRcAVVYmHs_BqqUshksvaZ1-vh84od1RiQiMlaQF3JQ-96wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbePc-GtaldWOcZxFwmLuuwxpJrccdgXjxJOtL_RSqctjhgwYwZ-uT6xfTlMAYtsOZMWhUB8qDi30WRfazeFJyY65FZgWPR2fyXgMXRgD-TtBlwfWaOj5QAFSVfIpf3qazO3yx7F8PuhINFyiIKIpNhHBG3LGJcjJ6CO6ISJlhORqveferPnkWGbV1K1zYzY7zz0NZDpaZcE-mbH0r564H4AnrQuCXNDop6QR4Wj_Ij4xjqvgB9dVFjhSbkK7ocWbKnu6DDs9gF2Bv8HPnJi4u5bsktKBe5JDMm20cULi3p93CoFWUtpq3knLDAE2l-RjqkQHmTdeRNCZjk3LxyiWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM2v6Pr0ePlrJWmbFRmZvpFhRdySwcpL9X69Mtb_4-b-3ZJMA9xVwFhpFgIyX_pf_oc7_2cfGgZKiRv2eyl0RqQ7fLl06bM5-4cELfJPvfDqlrRdo0oEvkp76fAcWkVA0WwpiSucmNkvuZvr9entGv3-2miYj2IdaDSxTHui7Y-QH02iDUc89R034JBUKkTUWTZqcvPVX4UR7oOWKxYlryGaDxvbwxbBz5YLStSdh_8aHOdcCtEEQiTjLJHo_recJXkD2OqT5BPQyH7CrUvA-w0KJn9dbUOCpG2sdhYFrfwb08oKAONUHF0hLa_tm53LuseVcGa00HcxVYlvL6IGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZHUNOusvlkeSHcHbyiif-6rhizFLP5B1qm7F8pleK8JMLhfBBLlWOI5fgGlojpwKhs9iPcMSAzIO8UnxH73RRq5mCRzvCHTFQ2U9CQD9hno1EPB-JTAIOiVlpQ7mbmaGuXkt8Qk1Ejd9XjO5zEGTNxjwrzVTvKJwb_koFBgMO8ywhvnmS9yhxIWC_vANAUDUQLb_kkggpatSO2IsXuCsXIZDpEAM-O5J_Ydd3xeTQKjXgdUQ53-ulLHGlhqFCPsRSzb6vUfFPTFpPt86a-TZeLMHXeKwWo8Lz_3KrVEB7BSxAGNdpyiGmjiRN29HnVsLji0j77J3bl_q2LY_xnfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8_S0EcAkJaRMNbYyAxG2aVLrGvZXta6Dlmv7V5vAg_crENjR1l8hb-5Dw11LHwWNvJQ-AYo7-aHzKWwGQbeMlI6xMPGEFyCOUVY8MbOzWGo1MUO5AcwayYOxs8Cu8tGf60vl93qKqzjvEgOsl3rPtSev0pgwAG_XXXJXG-VwxifSs3_QkhEcsTIAh8lb8os5ZhBHst_vsvxgJXhP0Bdl6XlUUWOUjhJgPVC-W6kAwwiiq0QdAfcOCHHuw5ke7f_yy6e6AzXMfKowUTY5869RavwQsWAW5hUbUsHjCW3jKPeCNkcTjAnNNLuNwXb1LeL-a0jchM53b6sYstRVFomBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0y1UtVIurAtszM9Ad8RCY0j5VG3pxw8BDHzgRTTocdLNTKGdvcOJF_-fvQnNkxf2KO0R3Sm_t-Brbrc4rPhayoh0gngwAdS6X_liXeYgo1F_ImCYIXYh2S-O8CjJhwRvRswl_Iu0lXpxgf0VgNkAdZHXbpPE8M-uOYF8b5blrNNHrQXZMePJQZJY2tv0E1HJHNsPsjlX0Dwbq5Fev0BUG7r8gif43wQhpNuyvo-VNdVMH2rYFsQXXsHLrAgiGR2tZhFuGUjSrc_lsnMNnZcPypC_bsOAgA6iR1-2rhbgiyJusm80ee8cdbTOAq6u5IlWQi3t_l3lyMh3-FeebACNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtGDHWS8-MldVLU3MIB2_ZlbwVUdvzYcT6U04NnT66m9NSqTlr6vCU0mn5TrykSWms3vr4774XqWGFvJIuRu_h2YlwNP33OZR5bMwKjBRx7liqvukSEb_2s6LBugVZgBVh1hcsJF4M43bahIBA56vnZxb7Xd3J4nhz9QXHUFtTXWRtxeLwXko8_5Ja7Gc45DRw7sKiSToiA96c1zyWiNJwEod9tC2Wk3JppK2vALN6rTvQ5BiqcySNJ1SgVpfg8S7DT3fFkYRz2IGIGpvw_XoBbZvYNY_u2eJKRGvTA0fsPzlbMuJlmuRdLWWZ_f9p2i65IcXURJdTdM42XkOIbqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo5VPLVp6yxsDuPChDaSShonbEOWevhc6-Jwje90WKRtvcCRpkLCmtxmd63CRHu0FHtIJ2LZCPv4ig11rBE2e3ACZI5tVDsbVjfadHVyVdVARoIeuN4S8f1SUk-nMEkvL1qUZetlLeOOZ90zDb9TwsEgpTfaV2qn1CbtJB_43wmtogqZiZcMTIKiaiRiQ50qipoqg3iv8FtoRliw_3xMalVfykbkSKTgbf9n8i3LbJNBDPjUp7gTRp2fP0TUJdM1uMCV6rHpge8TgW6ErPRj33rq6PHL25AzvEWb1Tme93pKeLsZ5I3X14L5dBypKEY44RFIKIHkwGf1gB6pG5-DVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=vnM3P1YNM0ewTt9RlSrAyVZ9nfcILy0AFsiVfHglZpFqmuR6G-g6mp5Bz0HK6nuYYAIDp47YPZv6IDuR2ll0-tC_M7ox8z9U3y1fXrRFNYetv22HvYkBbk9Pq7fo7I60vcgDpF-parLBCAJ158JZ2_wDieJHebHwet0gDAUg4De3XbkED3pDJbtG9GVUstd17jxJjKEmoYsiRgWlUjCXBPxDhLYdJwW5HT_WUBqDW2Dr6OyOr3CjmiibKNAg6XtxelfPlbgE3yB5vSayJMQH5MyVfoFkI1AN5_w4kekHktS906Dxpo0v8bITE-Aq2yeHO0X5rH6hVZWRe3WeDU3_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=vnM3P1YNM0ewTt9RlSrAyVZ9nfcILy0AFsiVfHglZpFqmuR6G-g6mp5Bz0HK6nuYYAIDp47YPZv6IDuR2ll0-tC_M7ox8z9U3y1fXrRFNYetv22HvYkBbk9Pq7fo7I60vcgDpF-parLBCAJ158JZ2_wDieJHebHwet0gDAUg4De3XbkED3pDJbtG9GVUstd17jxJjKEmoYsiRgWlUjCXBPxDhLYdJwW5HT_WUBqDW2Dr6OyOr3CjmiibKNAg6XtxelfPlbgE3yB5vSayJMQH5MyVfoFkI1AN5_w4kekHktS906Dxpo0v8bITE-Aq2yeHO0X5rH6hVZWRe3WeDU3_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=IN3nz5YGDWbsLF5F_2hkujFDCVlubYRbhKeUesvEUkcK1-Xc6UIcfnXxQQD-Mx6xykmaWL3ySfO5ndnqI4ebnZpNTGjYCyeltR_10PKViPBeGHdXT2qjUaWFt7sQv3zsqg3y3DqXvfvvK1GHJqwqVYYA7u8UgN2fP2vwtwEWC5a4GfOsdpE9ne90GkvUz1U0bBqD7Vt5XEbsUo5LOJU77cFZeBwZr7pZ7JIsm_reZZ2dtia2mPcSmvNL02u7hJf9EWf3QQ66S4cdCQtmzV75IuyvkF-CgyonmygAe1LHMfNn_4Ej7zUr3DpOeAMHp1OjXAXgUvpxE1s_vgckm4bZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=IN3nz5YGDWbsLF5F_2hkujFDCVlubYRbhKeUesvEUkcK1-Xc6UIcfnXxQQD-Mx6xykmaWL3ySfO5ndnqI4ebnZpNTGjYCyeltR_10PKViPBeGHdXT2qjUaWFt7sQv3zsqg3y3DqXvfvvK1GHJqwqVYYA7u8UgN2fP2vwtwEWC5a4GfOsdpE9ne90GkvUz1U0bBqD7Vt5XEbsUo5LOJU77cFZeBwZr7pZ7JIsm_reZZ2dtia2mPcSmvNL02u7hJf9EWf3QQ66S4cdCQtmzV75IuyvkF-CgyonmygAe1LHMfNn_4Ej7zUr3DpOeAMHp1OjXAXgUvpxE1s_vgckm4bZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkUPs2-_VFEH-j8NwOX9ZMwy7FgnP8uCH-HRkyQ6-aBsXrfKCQf-tvCiMIC8yhk13tKAqMWed2ZeNKjbqs2vGBiC9xj6g1pYFE7M5eLdfFdlfMKiQGD1kf8qV9tM4nOGXrmabm7OD913tc_i4Uqt__cHaZUj-1jkIVpqSuqD4b4vtd0Ss5dAuXrdTUAuRGrhLBIRufzZxbVCd_U77tcLXLHIehk04Xe0Kn-7U9wCOe09aOsi60By4cqwgWmt3nmagaVC2PPuEUsbc00s8bmH2JHmQtEWARLiKuLgFbRhE71YiYtqGp9BVHk4jYSqjUSss13aeJb6n6F_YrAhfqG2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=d9CZ29Je8RARvzUizf-c8SR2uM7cJ4hBuWzMLQZHugBOrGFxWZKCIyKVSypRcWdrHZuifw6tJ2OK5k09dvrWERXPoL-XWnI8ScB-vHcXED4tBogQb8jwFO45XCwngsKN7xA6CF-ZIRQGDSYcbJTfLUk9p0CBcsee2kagqAsPceAhE3qSJW0w433xZz4tQFAwyY6MgbfYdKOlAcbKGi7BnR9lKnE75nTqiE0lQqu6qzdgU9pTWTeL1Grw35PhkU2kr2jnXhMvva2r0pNsEIEeMr6f72EKOy1Q6I87d1T9GKZK6mxWUuYzRKKL56ZM5Kh1B1PXfnaB4tZpjKjHXw4cXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=d9CZ29Je8RARvzUizf-c8SR2uM7cJ4hBuWzMLQZHugBOrGFxWZKCIyKVSypRcWdrHZuifw6tJ2OK5k09dvrWERXPoL-XWnI8ScB-vHcXED4tBogQb8jwFO45XCwngsKN7xA6CF-ZIRQGDSYcbJTfLUk9p0CBcsee2kagqAsPceAhE3qSJW0w433xZz4tQFAwyY6MgbfYdKOlAcbKGi7BnR9lKnE75nTqiE0lQqu6qzdgU9pTWTeL1Grw35PhkU2kr2jnXhMvva2r0pNsEIEeMr6f72EKOy1Q6I87d1T9GKZK6mxWUuYzRKKL56ZM5Kh1B1PXfnaB4tZpjKjHXw4cXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=Ul15dgAm_RpsiwWoRs5IWNiWw_4GqLFLe34J6kGJkvKJwy9zDepGqiAeMfj5Ocj4dHh2A9CORuc6nGO2x3iVy0pWxE2NyrC3hOpeOOnGlHWuDfcQCCT_HKnHtaVt1TtTPn4brj9x99-4OXK4YIn7Ly4darUzwxUaKN8GMNqB1IZdo96kPXuO57JRgVQ-jTiM0P6QnLMMlN2DKE-3hX40vZIzep5CchFjRzwSLyOiGAb4l_UK3wWjHIpCRDXMMl_g4z8H7iizOnB4Q8a6Y5kc9e6TK21lYYbYJVpsk6aKN9JZ_Y4grKxD3ZBJC4waVMZfbJ7x9n90FM63u0WTxdjVtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=Ul15dgAm_RpsiwWoRs5IWNiWw_4GqLFLe34J6kGJkvKJwy9zDepGqiAeMfj5Ocj4dHh2A9CORuc6nGO2x3iVy0pWxE2NyrC3hOpeOOnGlHWuDfcQCCT_HKnHtaVt1TtTPn4brj9x99-4OXK4YIn7Ly4darUzwxUaKN8GMNqB1IZdo96kPXuO57JRgVQ-jTiM0P6QnLMMlN2DKE-3hX40vZIzep5CchFjRzwSLyOiGAb4l_UK3wWjHIpCRDXMMl_g4z8H7iizOnB4Q8a6Y5kc9e6TK21lYYbYJVpsk6aKN9JZ_Y4grKxD3ZBJC4waVMZfbJ7x9n90FM63u0WTxdjVtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGsD62cTLSMhFOHfi0g9OwsZ77Yi_Fdm5WR3Nc766x5BqVnS2ijn3Cj5qvy6pcpNJfTYWijqmCDP0R6q4aJ0iyB2SLsAT9FgZ92t8z_xiQlN5CeNzK6cKa48LQHgPtnsx9xPXO1Zem8ahiX9Gh7oI0LXzTeH_zYNwsmeceEOx00xJdWftjw2AKY_cBVQmJ2e72ESNFyOZFIe3JnDyVcF3ZN5QlYd7ltAYOzrXcSczmRX9e4sW30n0GANzHQza-p-5RCvxwUUoKZVDsf7KHRGOsXiwCE-pcFYIaCqxKa-Sn5N-x5Mt6OcRxuLQPilQvYx9XFruJFkih4rJqgEDwZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mx9ASVe7az675JEWh3Kvz3e5EjOUIzxPeax089-3PbWYVCr1mrmWJdHFQ9bEMqWzAeFgun4Bv_EBaXeIslGdt-kE78EFTM7wUQxz88JUF5FlYIAfzRv3f9fggz4HE4CD1caRPDAkyfChv-XV-XEaj2I6S5ejImMuKIjsBAOLm9gCMhm_K0SfaHzUgDZemVxPsGINMIWUtXMWrAhQPOJTkZ3_1z9lxsVLVMxwZjAJ_M-eXcEHLWrV69UTcgttEloXcq6ltBLjB1IIZE2mWHWBi-CXIgxj3pY1wgs-6f4ha1a382si_y-hmeO8eilkeQG5MEOXE7SrZL2EnYmAmpJ1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFDptK5O43t46QhOBHLOf9L_3Tcev_j3m7VSU-c0YuKEwJPGT4zQWz2WL7lwYbenO3DdSu-GoVdnQHZT-4D6T8dpUJGKXFzC6P_W09H8vszBHdK_CFkNcgExfclX4WWNQ3E0xT1DAfiuMRPA__2xdQ2WxlASczL_jdjWZ8mWiRZJMs3btr8rhtOMrCiEpH1g-3AmLUjIny0x8tPk1yMNw7lutwQUVyOxZf9Vsy8tx-2vYLgerWSbcqtzeFDbtSOswpsnOuVxLStI2R_iAmDqHVe-3ggbbgTFjzfpt5LASBONNCMJ1r5e6nqLsjAbT44cvuv5eSfABTX1aKAvcrzr7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=RSUThBlLaG4-JKOCWYNKM3Sb7TlGqbEUaFwR5LHF8BBHCNb-2jrStoBJv6fmffcmBPS_HT1ZNEkDmm-QRlggKQSFCCV_8Ts2ttsMBXeDP4GfxI4Vhh3t2RsivHeCLp7ItO4pURgpLqbKUpCGSxZiSNO6D54ov3EzDh8PEqGceLpNN16AbT7PSi5W9BQOOhG0wC0-qlhXbgqwx8dVs_q3bdT3X5M-RXv41ylhkyTwFZMgSjptOuqKGSbPCeEcaZSX0xknCn9e0pUyMa52YNS0DtmzZlIJMlvavSnnhl848IPBujjV8EHpNgEbhqUZsRCiEvtpk1BXty-KKDw-u22u9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=RSUThBlLaG4-JKOCWYNKM3Sb7TlGqbEUaFwR5LHF8BBHCNb-2jrStoBJv6fmffcmBPS_HT1ZNEkDmm-QRlggKQSFCCV_8Ts2ttsMBXeDP4GfxI4Vhh3t2RsivHeCLp7ItO4pURgpLqbKUpCGSxZiSNO6D54ov3EzDh8PEqGceLpNN16AbT7PSi5W9BQOOhG0wC0-qlhXbgqwx8dVs_q3bdT3X5M-RXv41ylhkyTwFZMgSjptOuqKGSbPCeEcaZSX0xknCn9e0pUyMa52YNS0DtmzZlIJMlvavSnnhl848IPBujjV8EHpNgEbhqUZsRCiEvtpk1BXty-KKDw-u22u9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6WSTuYHFmZuli77nL4tXmomYAhkUL3jOeI_oHxeYOpFwlfzgJ8y02aaE6o2j87Oa3PeJ8abIfpF4-_XHmmVj5MurgYirc2JeJIXQlxYuBiPtGWdeHi4x6eVEPdFOCG75eJZVgdj2fIEsPCKVbAczHaK3020DDdvMXjLsCkY3Rd-3oqgEggLlXefFrkW5bU-IzRKzPLM_dJgDntE6iFCyhdM1w4gD_fAmaXAKf1zdyu4kgqG_gw10Ia87aZ8Pcd9gnsXNYXJFqtFPFK4JrBAWiHfSu69fDnBIln0A7jeTVZbyXzMh7K5TOuV4bnzdC2V6rHiz2-7i7a0QSDc1OMizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZjx7-Em1ITfp8v9r2FRdTqVBHP0IJs9rShUhIasJvKEkRtX8x8ybldiJxhw7ufnxLPoUw24OfkR4y74gavPKQBNw4MTCvhJ4E1gsByvO3kd1yyR5rdXrmZR_xWk4lusoJLfeFINt5wggncHldbDH8ACwqR8j9be80y4w54qn9gYx6kEylCfCos0jFGCqAhMPMQc4jVRQ0LeCBz-lOXasQzA6t5TM5s-jrdCIhFRQo5uDU4n_MjjnEmbTerVECESws8NqEeJOV0AsPYVCeu3GJosMa0Q_b61y_4ytBsdK8sRA6ggP4hNA56gUPMeAjagkhSZRLY0aRflx3O4mEi28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3C80V32TBDgxDfKk741pbJOFp6Er7sJEbi2xVGwvDVpyZb__ioG9evs1WQvwVWlpv6_XdIOWgtRQ65K-Ca2kvSXoCZhj7ejM2riIuU0fxjdqqWzftlzLSWlgMOS30ANSxqGRVuwOlwu6NeFfNAKd3qY-o_CzY2oEEDnY0R7XA9QY6i5mCj_Zgs4Nz85CYNNLzXIof0RC_HqtS30yUpA4pyOemk8ZBFW8WAVcvFmGz9hKS4yIR1XB8SBF0pTJaWrL1rpnWB-C0Rp_6Aqv-RFQAVfZt2FBTz3lbyzKrK_sf4eBgssa-e9dHisywLYnDpFK4vy4rkt-pFmAYQ3_gAuCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=b6HS6Vzb6wJiC2A5hrkQm4x_ngWm1ZwNmDK-09zuyz9CoH6WqDQkInryUIEnOn1xoehtKXcQGxrIA1oFCiTFkbnx2sOPDUHTxIjwdOeLTXKuJfVdZIE9Zi8XEap-x3KnDzJbfxyaoyimPr81yF2fbFPw3HaC8SJUqs_NchCaw0UvLDdhpV23fWtGSN-9MfXjh-afK558AvSL9dB1DIlz3kamkkQPOkrYlg1L13mQybIa5KjRWfsqerHO1Lg6At1ihEPCmp39jx4iqKjQ4_4MZLPoluTY7Kk1UTiVESEQwkblCZPmCj7w0cEqaojA6ip3lCAOQj1FCIMmxFWeDh2tKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=b6HS6Vzb6wJiC2A5hrkQm4x_ngWm1ZwNmDK-09zuyz9CoH6WqDQkInryUIEnOn1xoehtKXcQGxrIA1oFCiTFkbnx2sOPDUHTxIjwdOeLTXKuJfVdZIE9Zi8XEap-x3KnDzJbfxyaoyimPr81yF2fbFPw3HaC8SJUqs_NchCaw0UvLDdhpV23fWtGSN-9MfXjh-afK558AvSL9dB1DIlz3kamkkQPOkrYlg1L13mQybIa5KjRWfsqerHO1Lg6At1ihEPCmp39jx4iqKjQ4_4MZLPoluTY7Kk1UTiVESEQwkblCZPmCj7w0cEqaojA6ip3lCAOQj1FCIMmxFWeDh2tKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=MN6SFs8gCuAWYCguNteYG9Hs2pz1ODIXo91MGtMi0NAljNHkfrPzzTUn1vmcclcejbvYwqMyiiCFbTk1KBClFDdJZEmoIZtt-mAA4OAgB89_TVJogtItAzy_x95me4gBNGi1f4Wl1o9TKr-oO79fsFZACib4qDn8BjXVozWIgmu00leIJ8XrXMt1ozemGc4A1KS_dm2rjkRTnIT7RY7cjzvMyJRhaFkbipJFxSE5Kldpbepkdbewfj-e4-0YRNnr2jqMihj1q8-R22Mp7U881ZS8CXVEjpIVlbWDhafoFcVsL3aiw4NSi9nJmEqhfK6QeeY7qwr60RHFcNDmLM05hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=MN6SFs8gCuAWYCguNteYG9Hs2pz1ODIXo91MGtMi0NAljNHkfrPzzTUn1vmcclcejbvYwqMyiiCFbTk1KBClFDdJZEmoIZtt-mAA4OAgB89_TVJogtItAzy_x95me4gBNGi1f4Wl1o9TKr-oO79fsFZACib4qDn8BjXVozWIgmu00leIJ8XrXMt1ozemGc4A1KS_dm2rjkRTnIT7RY7cjzvMyJRhaFkbipJFxSE5Kldpbepkdbewfj-e4-0YRNnr2jqMihj1q8-R22Mp7U881ZS8CXVEjpIVlbWDhafoFcVsL3aiw4NSi9nJmEqhfK6QeeY7qwr60RHFcNDmLM05hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=tPdHFHiWohMZk24G8EyJ4DI1C3svmsLVQXEfWQkvR-ZnwuYSWBY9OhQWIvXmyDFf6tX1j3iBDLA-tzq_QfHU0xyu7GMW6k6G4JvicrI5Foqd-S4eGVqP8x6csU4RfmhKmo29L_ARJjStupTMdwh3V8kHudwEyopU9nip0zYN59aRdv34c6--ySGRxtYTGf8JhGbvsrUIK1S3HywF-u4fRQb4shpSgm3FF7nbSxzZiNsVK3BaMWZJBtjn9nP784WfOtyxiStt1NgCUvQYAFmSVf9-sy2VclLHOtMT3BsIEp5ZuLtlq4D1l3S1O1Be739SF2JTWyEezIyCgLNMUv2uxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=tPdHFHiWohMZk24G8EyJ4DI1C3svmsLVQXEfWQkvR-ZnwuYSWBY9OhQWIvXmyDFf6tX1j3iBDLA-tzq_QfHU0xyu7GMW6k6G4JvicrI5Foqd-S4eGVqP8x6csU4RfmhKmo29L_ARJjStupTMdwh3V8kHudwEyopU9nip0zYN59aRdv34c6--ySGRxtYTGf8JhGbvsrUIK1S3HywF-u4fRQb4shpSgm3FF7nbSxzZiNsVK3BaMWZJBtjn9nP784WfOtyxiStt1NgCUvQYAFmSVf9-sy2VclLHOtMT3BsIEp5ZuLtlq4D1l3S1O1Be739SF2JTWyEezIyCgLNMUv2uxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=FI5xzGq-9EOPlJuThZ1F27NrWcKa_YiDPtQ_ynfun46qOK2BIfcPIqYp9QKkaRDK8AK63E3Id-CmkpoPPO_rWBgg0sdnHxsSh3D4rxNEGNa8ymRF12rx700iR3_8HEIiUgzN5XP0W18wDI0FJzjUwaKCah7KdurG63pJfns6ufIutflSGxIG-4U8PTD5tjpsc2GBnumOrQ95tuw3ST67Zt_YwtpIlVeCJTKpRepZZn3MpH10FjNVCpt_4UG1mqg8Kaei6HaxDB8eErsbC29IZRzHEn2vy1luCumUg6f3BKeP-WoeUj1iaXQAjaGJA4RMwBlvHnrwD2RI27cPlQK0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=FI5xzGq-9EOPlJuThZ1F27NrWcKa_YiDPtQ_ynfun46qOK2BIfcPIqYp9QKkaRDK8AK63E3Id-CmkpoPPO_rWBgg0sdnHxsSh3D4rxNEGNa8ymRF12rx700iR3_8HEIiUgzN5XP0W18wDI0FJzjUwaKCah7KdurG63pJfns6ufIutflSGxIG-4U8PTD5tjpsc2GBnumOrQ95tuw3ST67Zt_YwtpIlVeCJTKpRepZZn3MpH10FjNVCpt_4UG1mqg8Kaei6HaxDB8eErsbC29IZRzHEn2vy1luCumUg6f3BKeP-WoeUj1iaXQAjaGJA4RMwBlvHnrwD2RI27cPlQK0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=uISt-1K7wex5tfn_ncRVuXDGeIFc3ASnV83LjlbTVAbj3xFzMVSGSXJgts4NMv4u3095_MtipBDAvgDiR_NQcJ4qCkJOuFVGrZBo7uwRpJbFlpxIxpYKB6k-B6EFyOQHg-15tcDgTqyzszfYruFjcg4TXO_rc6nh-LGsWlO6AsAUxCcnsxUmc3VmwR_nBWROLhuBlFnHum4yTAFzDXPt1vIdDdcXrQo3QlNML9TkZun4rZKKz7kDq8ETsYrc-d738Sb7grX-l9TMH4UU5HKvbWQwef3gHWgJXAP1w6syJYOjhqAgcYTyI6_Qs60_iannNmKJfR6P3y9zm2Bf2Ddahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=uISt-1K7wex5tfn_ncRVuXDGeIFc3ASnV83LjlbTVAbj3xFzMVSGSXJgts4NMv4u3095_MtipBDAvgDiR_NQcJ4qCkJOuFVGrZBo7uwRpJbFlpxIxpYKB6k-B6EFyOQHg-15tcDgTqyzszfYruFjcg4TXO_rc6nh-LGsWlO6AsAUxCcnsxUmc3VmwR_nBWROLhuBlFnHum4yTAFzDXPt1vIdDdcXrQo3QlNML9TkZun4rZKKz7kDq8ETsYrc-d738Sb7grX-l9TMH4UU5HKvbWQwef3gHWgJXAP1w6syJYOjhqAgcYTyI6_Qs60_iannNmKJfR6P3y9zm2Bf2Ddahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQdq7ye_6iwNUPEHB-8MBy2M-GJZM-igWHbwVrolNRSJ58Zk0VFgGUoKeeAtX8eWsv_5I6EQoyLUSVkF9c-OFg4YPE-sMQ-Z-pyDOC1gvHcUKtIRJJRtWbtZqQr26lGe72BcB1u3-o4hN7ba6gTu-l5H8NpR8VTTGi3-Z_z_MFnXWE7aGu919mxOBCJbfaeiO6cK6R2nAwqdUuKAQeg7gj30oxsJFN95NvbeidRbO2tu5hPD0vMPFZ4mAstPoMruNtY3xOyWtmFR7yknVIq2A3qZIQYAF4dc65PySLkGzfahKJhSUNNMtm2Q5vxMfggdzzXDpRVng24E2SLakPdvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5UshAMFnA48q46hBfzh9TGeVJO01PrfZBgS-vOZa6OCqoJdNqY3XiG4jzvZKIiOM91-CNxvDov8pn84Zz3JNOFVMVSz-_HpAFZ93C_xgdI0OkG6o3-9eUxuxtD1r6P-VN3AbPLTLIZ13BFhpADDt2liK-srp3UTb91LLTYr0b-oMOhrC3sygJllaNU23TJ2aNxicWJrZW2iggbQjrT-VmbqYVsoOlvNXiRTPO05NP0d_dX54e8Q0KqCxhK3Iv40T62DzWfNrYqNkh1L27_96fgOoQQe00DpaxjQQMMP4VE8j-QkzCovZkVWpvdLHnBsmLLyW53GjEa6XUbDRkK46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=pwytPgztz4XtEX2ZCFDZtz9p3nhBxwisnXeF9nFIhwjC1gZYPuhcBySNN3jx7yNVoRYNLdgEeueE5Bo7fRnImk6Rq_-4zvEIYMdQGJEMFldyNbEYzMbbbSNnKOlQ7ma4Bj-I_GwByHDta7ZssWXkTesGbckIhVihH9pRFiF2pvMlGpyWme6VErp-e_SIGuynDjzK7Tb8GRKvUsz99D1iFt1qHiJD4Ul1xot6-jG-n766pPnH55EK9WW4GYgihQkLpNTHA3k8aqwBRyGql-FFd6iTH8oGrBsDVDyI-xP-lsQfdp3dpxi-2Kp4iG0hI1Wboy5CP_QvkCnJINamjkedMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=pwytPgztz4XtEX2ZCFDZtz9p3nhBxwisnXeF9nFIhwjC1gZYPuhcBySNN3jx7yNVoRYNLdgEeueE5Bo7fRnImk6Rq_-4zvEIYMdQGJEMFldyNbEYzMbbbSNnKOlQ7ma4Bj-I_GwByHDta7ZssWXkTesGbckIhVihH9pRFiF2pvMlGpyWme6VErp-e_SIGuynDjzK7Tb8GRKvUsz99D1iFt1qHiJD4Ul1xot6-jG-n766pPnH55EK9WW4GYgihQkLpNTHA3k8aqwBRyGql-FFd6iTH8oGrBsDVDyI-xP-lsQfdp3dpxi-2Kp4iG0hI1Wboy5CP_QvkCnJINamjkedMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfkvsdfBBt87uiVHYCVa9SGuOkL9M4GFWcgxtmAhlpMA1qtQIGjaTc_9jxP3Ii-4k3YMFWFSKvBYJ_hnCDHbzgD_xhNwM2LPuJ8AmH5RuoHmS7ZOjt5UrHec-yxw7GgnmfgtvvdKk_oxZ7LIVrE8o6wdat9oqSAZtt1WGDRn3et7RBC_DQRUsZ2oHCoFqTraQLBq0lwLPgWTTUvhn0HNb8aKmvWyMof4j5a7S7PGQY6jEBywdmH-QLsA3p3zFrXmKxUQcsJvfht8V9b0Sxo-xmpwNzAgvStpxMS0tRKlleqYTIfnrzSNV3vJAshfmfsEASJUZHtwfgI95CuPQwjmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qazPqMSCyTem5duyWiSkU87I4I8zKv6wUf_dR7ulXx3l3YsaEDJLOVPh8qVL0Ck3tPWW__jN_rBJRYyONtEYJSL2MMp8zoUGfRD8vYGlIkwg-UgjdPMTRf-HquuOJxr_9FhvjXoqES2Alot6-aegUNLreyfNRbpykMYwNR6852THDLLXHayWhLVJYr-RR3SLpQ4Pvuu9zrvj35XRRXXqI3uiBTTR3gku-MkWLD7ZAfgyzTXMdSne9J5dnefq55xAcVOG0eb0C9v8hLakQy_444Lfz3n5CKeQIL0Y32LhJoNqiLheug5KD-_8dvfmRzqHMAc8nc8T-W8pQWaJXM-ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhQO8lSPALVHPWCimYh6QsxgUAxMsO7oLLQAnlhGBY-xVuDYJMztWdZTG_Nx4-qxNm0XExRa4JpZ5aslEJ-eNE_fZxSmy73jO-hR-3R0nVgohyH3Z3etkqsbUp1nyAnLNMjaogTlIEINhUKQqnE5DL2G3r_Vkec-XUhLPHu2GdPoPp89SKJosAofawNC8i71EX9qoUogGpf7_VKDiV28BItk08emY9QMQQsZZbwZjYLJ2CLuZd18vItXbiq572tYHNX_Ubc__6yZ_yGrX5ZNn727mK09SzC4DhmRIE6f-9O7iihg_WaQN3tvJWdhhE3tXFNxTxhTj-iGGnXc81BaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIXfSzIczkkDA2GaHv9VhbcW17HY8ERmzHezqJgIvFUAP70TwAYhwzLKFO0dND0yflLJ9zTr0HGxRWPc03yaCYxT2ahy-y3w3U70JONmZSew8oos4ij_uC5VgSvBIxgL8Mki3Ai9wfNoqlO_s-43LCu_7KANLrpB4UxdHxa453vH14Rtux6AggBaX2Jw8TJ_3wDmSqCOFkikdC0Bw4AQT8BU_OPUJHOPCdvWnWN42XyO1EaMi44MliT0sD-mO0TwGj9RVKLq7KgYSJ6-eo0FzoO3f6bEh6cUQkMneRG_TGCa0DunvDM9HL8-kdPEGnTc3H0zVIq4km7spctdI3gkSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
