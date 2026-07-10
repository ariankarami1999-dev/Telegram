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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 188K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 10:29:07</div>
<hr>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_SCRTXIZ3SnESPG_wvKLm7eAk5tTQrH-orNFDMkurHTpU_u1G3kin7aokjf8YmViDpBkhlO2bC_HPKmoWgv4kJ53PYBF8krzyLKhP2EtlSagyLyRIg_cb7RBWrL0Y1JsXJIzxYRyuSVy6RgGOFbf-6PBxw2dd6rFBgtQ0BgSxwscMp7mYbscfO0K-sfmdD5PeZS1xw3Rs3bGXYIS0VpaKW9pj6roKFBMNCRhJufaMlOihs36iTzJiEt4kd9OV4BuvRc5ZcsvYrrFMInNiJVo5TUTivMECtYrDOOrvJbzjghHxpvbSfcE7_DQ3_7yLRYe83pWfmjX6I9euk324Rv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjEFofRyaqinnTPAYE_vo6TWPvN4TIy6wuLFCgWDgEnbwMkya8aSpDIAbH-QuexISsrNl7R9gUbLRdDJxc99j39sJm2mZrbDrVXsCELDhFhBV3CXpG2Qxeu7Cme5380fsjAB5NCmpuzDeFSKXHyDmsRAmjvc3m1NPY7CC05XAEK3xC-1e4WW1w9IabxK7MPzhFlBRmsShwpzGG5dZbVS5AJcamy5-0fC4vf8ZFLSbWz41E_d-KqyFQ8B9MqJDctIzsIjU6icovdJgNUxShV5BBNDfPDnjlRngGyUywkxOyLB9NAtj3dMKk8Tz0c9MdIggRuGT1maadokqnwtB6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEK68BX4eNB5pxr7MKeKZ6h1UZyTZDu2qFLQbNM2l8NNPzwIhrsrcB9oRTYKKBDu6PMejC9MpqoRAA6pgxDKlIpgyBDchZjjKNquY2qdYn9KJoGHo5XFFYDcoM1fE6SPJOjeAbrnF4NdhDj1KiKWDBRxnCjP5DjFvagyJv63o9Y6E-UFBa8rRiI5zW3sZUVkl9qmCPAUxRClsB9lD5t7xjkYaR-teTyE1vEQcX86elXamiTWbF5YpfRQXwNke9r-eeaz8Pm95SwqizPPjGMPdlAf6g_0OxC8z_H6FuaaKEkOHzQS_-J4q0p2WzjGYC5FkOPmQG0J5NbDlShTGctk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ63as7Tp4L4Kyiy5_A4wbvqQhlHHia2GdLokuamDQCiV8uyoUTTf92zJXIiuPK4kVEkl3E55dzln8A4iWTio3eZW5jFQnUj6cdfHELhknehROcBuuFW0rQP9d_MQFRfWwvcuH-6ZU57T0RpReMg7vA0VsUmoMt71vb14yLWoKbvS9Ds3M700Pze0Vk8E670fdB6oLdkTtwiEy-qdxTGxOP9JFcueDautwuaJeZ7DRBEPjMEDGZguaRDOTYeY17UE8pZoO5mCNRBF0JE3YJPjm7vpoeEstvvwrawYwZ6u75E8ho6YfAPpA2A7fH-Pe5K24PAsv_Upsu7VVYHDzslww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCILebHerj1h59p4R76BI7xSKvhl1nhH8UIK5tOeC0LuTED18SQj7xiRNFO2__7YUO3PpEZW7x8_uiiwCJ-NYVYsjOPrXEY0rpBbNpwbT0nfMfRnlPEYPzuAUscASwUv0e8RjqQh3OkASF0NG02VWqVAtl1_SXgFTHbeCo26NI9svf7-db927vLk4bDYdaXQexz_V5QwCb8DHg5HWHbHFoarvIJOKvxOkMOzTUk3hCxLsFnGNxAUv8vD2pwjgSnmQVQFg54EZrt46_ZLKMKCnGkU680oZBetWbWUQYAc3SgyGEnzve4S3oMXpSL1R9MPCVDof2PRrGGfbwu_wVy5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrvL7D_gRkdiJESuyHe8X3GB8dYep8YxLLYKajaMyWnwmHKxKX1rxMrXNzG85byAvRPL1fzy0w17sm2ByWhtUzrAZ-KcgtbaKxN0OeOaFyXmEmk7edEwmfJFPtCXPs_4WxTTDBr7JGm6cm-HxgQE3EkgA9zRnif-NcUAIe28sS03WJAMQMiJbpbkAWLbiKqBbmL-QVuqqlM3lEuPD5gJ4gSOAP3jqTEmUT7qkrTmXv9H9bgZ5MPw1g-q74-AelJUIv3hH5hAIrYNuoMR3jX4wxQ2_uMehTURtHO2WGySyNHZKh8ZRZrDBPl5FHXi4JYn6DG2KhCweORmC9NCvC3kBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=usAR0scwI4LV_boIPzMSaGRSSnyZ5kejwTpD_PDZMFnMUE1ThH0f0erJmUv5zDMOrvlcKpqjjN9c8AO4uNJl_r8y0WDpDwuHC_FkLEXCmKTCVWaytbRmmpWNtJH-J69M5ZKgEfR3cvkx0nQg5VMWqa9XoGDqg98AtPS3Zn1qcte_u76GSavLFmswhuy89BtVdNTOxTBxegot84TGsogGV2Ca5vdQpmooel9YKA4QDmlvOYzMujMXQFotl01fdiULmnXzDoXLQR0dlTGi438z8TPJpTLrOVTMZuIKRKgwKDwgVEfVCdAj6QYrmtD7MayaNy-FRiLMhEZOyDyKhGqGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=usAR0scwI4LV_boIPzMSaGRSSnyZ5kejwTpD_PDZMFnMUE1ThH0f0erJmUv5zDMOrvlcKpqjjN9c8AO4uNJl_r8y0WDpDwuHC_FkLEXCmKTCVWaytbRmmpWNtJH-J69M5ZKgEfR3cvkx0nQg5VMWqa9XoGDqg98AtPS3Zn1qcte_u76GSavLFmswhuy89BtVdNTOxTBxegot84TGsogGV2Ca5vdQpmooel9YKA4QDmlvOYzMujMXQFotl01fdiULmnXzDoXLQR0dlTGi438z8TPJpTLrOVTMZuIKRKgwKDwgVEfVCdAj6QYrmtD7MayaNy-FRiLMhEZOyDyKhGqGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=FQXx-450qEUmUzmFligzt6A4nm_WxZlBazXM1GlctDPN7c6u6gB1yzWsPCcGXwaWEM7u8WHjlLSVH1GsjPznxEiMnC0p6LT6R59UJUDdb1WozuMcfL9bNcpY2CX4Lg-Jc3u3wZO5Jdh5tt_o07OcgyUC_EXG5uT1GM_lEeRdI4zT2j6GYNpR3R3qo76IXwQY0AL_DXeLLPssVMJI3f8FCa4ik_E-TAFIWSgiLlT1C33X7QLPm8DG5AGx_v_g_H-Jwktcafe-Gr3UuKAKs7ZHC6QB6x5klkLerciOj3xH8muIEy0VfhDKmSUgq7UWySUtqpYXOFWx0xplrNyDeYvXRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=FQXx-450qEUmUzmFligzt6A4nm_WxZlBazXM1GlctDPN7c6u6gB1yzWsPCcGXwaWEM7u8WHjlLSVH1GsjPznxEiMnC0p6LT6R59UJUDdb1WozuMcfL9bNcpY2CX4Lg-Jc3u3wZO5Jdh5tt_o07OcgyUC_EXG5uT1GM_lEeRdI4zT2j6GYNpR3R3qo76IXwQY0AL_DXeLLPssVMJI3f8FCa4ik_E-TAFIWSgiLlT1C33X7QLPm8DG5AGx_v_g_H-Jwktcafe-Gr3UuKAKs7ZHC6QB6x5klkLerciOj3xH8muIEy0VfhDKmSUgq7UWySUtqpYXOFWx0xplrNyDeYvXRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=Rj0r9c0j6Kxo9d1Wb3MptfZY_o93h2SRe3R5iFz45Y8vx6KKuHo9c4t_oKDoPXuKEWZ-fuLgdTPh3f0m9O3nGo2-Rm8BgnOEC1Lb5Qpv5KLREPYN54ODIlOgSyEd23s8jEkCol6U9YCa_kAALSFbihHl004TBGx5WXZFKhBgBQHhdZEuqf9XzqiqjpDUZLMY6jQ6DEb6sVbjjrM3tz4pN-_rpGui1tv_DWg2L_sbaQ5JFhV6xQbVDNmpKR5Nj7sDCSG-jUMrjZicBr3Mv_L4M5c4k8SaUTgWiE-YDhItdtdpesJfmPeAj84gvu8XeEvQ38mMRvkSJKzyc-MY25KVPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=Rj0r9c0j6Kxo9d1Wb3MptfZY_o93h2SRe3R5iFz45Y8vx6KKuHo9c4t_oKDoPXuKEWZ-fuLgdTPh3f0m9O3nGo2-Rm8BgnOEC1Lb5Qpv5KLREPYN54ODIlOgSyEd23s8jEkCol6U9YCa_kAALSFbihHl004TBGx5WXZFKhBgBQHhdZEuqf9XzqiqjpDUZLMY6jQ6DEb6sVbjjrM3tz4pN-_rpGui1tv_DWg2L_sbaQ5JFhV6xQbVDNmpKR5Nj7sDCSG-jUMrjZicBr3Mv_L4M5c4k8SaUTgWiE-YDhItdtdpesJfmPeAj84gvu8XeEvQ38mMRvkSJKzyc-MY25KVPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocvD4CRJ_jfNLTmAjqg1ahzZa8gABz68zSHWZ26sdlfH6Ax89sBfFY57bpjryq3l_QZfWrv25OVD4_FkM_lkZjfJlb-A-an01gARC94LmtONKTcfQok6JhxPblesYMtVJfUYxrHsxp_RTxt0tT5BG9SP13n9BczP3Fe75DZoiYA19LYMB2I3fmEX28gZArxaA8QyCt4vpbgCjyRiL1Yy8ZZl6P1XhheQ625ojxbZfjhKstpgd_wXdyJr4Os2CV19kQynohUX07Tm3nrPxja-vC1z9LXitaqVlm1Lx0QJR4w_9ZEIHygPiaVXEskkCj4B5zBUKzKQdQQIlV7HRWktYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTk7XQ18RYQLtEtYOiGFwibrmPRr8QlVFosEsDnHTP1vPXBZ713NQxpoJHVA9EHgQugKxIjO5_lbgLg7Q5KKnnji1iVeRcjlPclr75aYEDvCmCPQ0R7T4Ce9bcSZOJbzYs4WswhYUI3ITSFzAmyOeZzhU1iAE0toQ2Yw0DhOOMlnKhr2zks4asen_Uu-17SsCkDyhPWgsmYJ46abl0HjS4ixbkeMXUmQHKKe7gxOmQceWQ7oRyNykug2Ld2jGa0GZBUkYZ6lOK_hSTxpmYVjnOrujDlJpPklqUHU-Ghk94AJBoWrVT-0G1e2a35EGStJzVx46rmTqv2Vp0JpJcw0Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=h-6RrCNqarW7Isiy67E7yU5-oQQKHiiqKZ0us1NktU8y3rfYZyhXEsJSMrSXqad0TQEttGebJWbATfFUbB5wTGWyr1Q706TPU6cNQcw6M2Aavi5cREp2S5oAURUWQidUNcJPxTh7Armn6RWQJmgI6HHRpkLOuRBCT4iQypOc50BfkEw397tnzDt5JkhijptuA8krOToqSavwOI7vNtWhAMaePaSijtVCmAdstZwZ03UjxnzKFw8JSb87A9KciED4cP6mbNRa7aMNboqJYIDVSns4ICVMRtXDarNnUKVlOdu4uOamyZxcNhiypb5xONNKGIJVGAgl-MdJOocpxJo4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=h-6RrCNqarW7Isiy67E7yU5-oQQKHiiqKZ0us1NktU8y3rfYZyhXEsJSMrSXqad0TQEttGebJWbATfFUbB5wTGWyr1Q706TPU6cNQcw6M2Aavi5cREp2S5oAURUWQidUNcJPxTh7Armn6RWQJmgI6HHRpkLOuRBCT4iQypOc50BfkEw397tnzDt5JkhijptuA8krOToqSavwOI7vNtWhAMaePaSijtVCmAdstZwZ03UjxnzKFw8JSb87A9KciED4cP6mbNRa7aMNboqJYIDVSns4ICVMRtXDarNnUKVlOdu4uOamyZxcNhiypb5xONNKGIJVGAgl-MdJOocpxJo4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=s02446IgfOQ0yfiU6tjt3xzIDA0FqdB4OXEGxbEcdyHEl66RkTjg9CfDjotKLSeVYAtybvovc_Gtqx9PU94oVHXQrq3hRfLH8H3rVMSZCcGO6nYhWqzyxeGaI9H7BeJpBrLkfW6f1QIBdtOZw2qaapEzcx_zdEWsV3Om_twOLoefWLDTWpRPrVTcGPS07fK5kVbbRlhVO0El9r36VbvD3GArNBnJHb_ULY29fU-3Wx7qF3bPNyTBSC0iB6UuhkfbR7CVvtd5f71Rf2ma_aIBRtjSIg9QBMsxEj5aG2HVSeuKsUlKK08Ew7GT9qX8NSAVONsA8LslXo2zfT8VVffKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=s02446IgfOQ0yfiU6tjt3xzIDA0FqdB4OXEGxbEcdyHEl66RkTjg9CfDjotKLSeVYAtybvovc_Gtqx9PU94oVHXQrq3hRfLH8H3rVMSZCcGO6nYhWqzyxeGaI9H7BeJpBrLkfW6f1QIBdtOZw2qaapEzcx_zdEWsV3Om_twOLoefWLDTWpRPrVTcGPS07fK5kVbbRlhVO0El9r36VbvD3GArNBnJHb_ULY29fU-3Wx7qF3bPNyTBSC0iB6UuhkfbR7CVvtd5f71Rf2ma_aIBRtjSIg9QBMsxEj5aG2HVSeuKsUlKK08Ew7GT9qX8NSAVONsA8LslXo2zfT8VVffKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rsi-VPg3eRvRS3ygVhxsT6tmhwAKTH-s-8_qYrsH5JWMH52TwCIRyTJ30dwNE7GG36ls02GIUXRxMRxLeiQuNYuujdaybeRHag7is633Rt34YGjJTq2LrlRp8h4UM2USvVr71x-uL_NnIWuEkmfoeRJER_e5njoU-6AUqwZcN4RCaQ1uSnm-w0flox2c3ogxExS4PDl9K9RnYv_JVkMaaBg2JGL0zsaRm48wDsZ5a1Gkn00AIS6-LaCieFJvvpXJbO8w9QgAFwvxnVehid-c9f3ZHlPGy2bqJZxd8h92zBVKtZLLTb_K9EoM-bb32HkLfnnCnQ6yGpZOGxipN3eMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK2lUo1L-8MHBjNIHp5GjMvIZlaCjY3GAmNFs6ZPXPBvlTq39bGEw1ZHFwb_q_XLFGYdz5LIy4qGQ5eMWqYLNT6Nk25jxamZyEbhexpEGGcW2EpoI3wGJS9HgnAXbtHEt8XYsg7uuXEFCg4fZJjOVjVZ012BKaMNAixPVfWIrW94ONWyh89MkuFW_uhSldAjwCuJRhjr6CfJIJpuRBwvgMziCKg00uOVXQddrLLCWgAY0jP4MWyJlNTGG-1owfQ-aaUmkWF_I07bvEOfXU57Ybhuwi6mBoVf46Zjlr9BD4o2DzgbBDGuVk1GtIE4xU808ah6ElOuYxNILpSV4Xfgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP_wA1p-HgCSDAAOPOadmTRVVvf4FAM-6quXuO8Z7H3LTWSIBJ2QGyNtvkTq6zu_blDnd7XlotlJMR_xPWEYfQFNHeAqtPTq2IoNpHmkeCn3AI8L2CziHQ7Pj1mzym9I2N3eQJpctdxI5LY0MC-KD1U1fiKvcVSGw8ptxWWiO6fPG0PqKNZl77bmFOA2bfvWf6SZ5UhAFx0UngcXC2-TxShUeOTEQUpaVIASXu7bTzRKtJV9ciVyLuUk0wD5zJUu3BjrELwbe_Va9BA801RYQQ_BQ0pqXHOWQJQYDCFVJ5vVNl5X3Z94qcT1xiGMwxDUG4WIx6cgWNFU3iRg0kxP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=PmvKy7MhGlXnz0c7HV3qZpTZ2ZFdeiwV0W4eKcLgRvx8by3hxWaF5BA2pNNiKlHYI0_8tER0ZtM3-IjUv5Dt5sPKB8b-BqBTosRqueko38Sr6f9XdRBIh4sqfW7PragN9bd1bNpo9Rqhtmwd0EyjklMGKOL_krUCmWwb1picINv9X6FEcLrxLq_WVW_KtseXT1tY4Gb1T6SoMRa3thrWL-sphdK_lmuTGhmYjNlO_BoyXx3FGArk4v4iunN0F5RwCUNZNacdZO3ywP_cZeLsSFc8vvkTadX3DVczUtbjicTyvzoM6MCmuE8v4dQNM__QtzCd2aUjm6UJMCMvnyUBGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=PmvKy7MhGlXnz0c7HV3qZpTZ2ZFdeiwV0W4eKcLgRvx8by3hxWaF5BA2pNNiKlHYI0_8tER0ZtM3-IjUv5Dt5sPKB8b-BqBTosRqueko38Sr6f9XdRBIh4sqfW7PragN9bd1bNpo9Rqhtmwd0EyjklMGKOL_krUCmWwb1picINv9X6FEcLrxLq_WVW_KtseXT1tY4Gb1T6SoMRa3thrWL-sphdK_lmuTGhmYjNlO_BoyXx3FGArk4v4iunN0F5RwCUNZNacdZO3ywP_cZeLsSFc8vvkTadX3DVczUtbjicTyvzoM6MCmuE8v4dQNM__QtzCd2aUjm6UJMCMvnyUBGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Corgbs4nHFjbSJwG5Ge7e2-1OcjGAgo4P_72xMynY65Pxn2WlzFS4BXVGMeuRYHPH0vJOBmOGgmqerXJvBJG066B6CA4Q5jQaY-HUhVIHeUo1K4pCRlhVFNWE-So2FIDwtgxZIwCvulS_MotdI7DlCHxX3udIY_2ufG64cd_-M3RzspV8jHN2WAePdBUWxw7ns2mwoW7J1BDE-9KpXPJoXr8x-swAv0EUbqw9rL-aFnhxPXxhrmXu12JPOds-b-3lbVA8WPPrrBwRRZX7BUj6YPetCL3mpQ12jtW3roG7ys5uN3jC68j2YX8QX9teSpK1pUJBMJZGo-c7gAyuytRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=Corgbs4nHFjbSJwG5Ge7e2-1OcjGAgo4P_72xMynY65Pxn2WlzFS4BXVGMeuRYHPH0vJOBmOGgmqerXJvBJG066B6CA4Q5jQaY-HUhVIHeUo1K4pCRlhVFNWE-So2FIDwtgxZIwCvulS_MotdI7DlCHxX3udIY_2ufG64cd_-M3RzspV8jHN2WAePdBUWxw7ns2mwoW7J1BDE-9KpXPJoXr8x-swAv0EUbqw9rL-aFnhxPXxhrmXu12JPOds-b-3lbVA8WPPrrBwRRZX7BUj6YPetCL3mpQ12jtW3roG7ys5uN3jC68j2YX8QX9teSpK1pUJBMJZGo-c7gAyuytRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=CO7NxlIHJz8QiNRUvb1GzLvYbk0kQ3rWrVlFB_BqRze1afQO1_3FeeC2V8pAkpJSlD77_yqzbOFF4zrTkiWEHwTqpK3NiaLzYQx6Dpy09Y60-kMPuc1CEYQcewjVlPl9VcIKtF5IFGv7feAzN-dZRXwuukQMbTMIKCnOBRI7Y41-Xu5QFiil3vmaBLoRl0RiigCocWtFhV_tjO1W9Mxo8JtF-LZQl3emDsIhr8e9Z_H3qqGEdYFwmkKiY1wKGcJMLKYv0IYYE7xt8G5TmFiU8YiKCIeDoymL7N0ffTyNb0WM8PtTsXaqMTqXHj9N8_3qRlQkfAwnCsvamZ5OYR15wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=CO7NxlIHJz8QiNRUvb1GzLvYbk0kQ3rWrVlFB_BqRze1afQO1_3FeeC2V8pAkpJSlD77_yqzbOFF4zrTkiWEHwTqpK3NiaLzYQx6Dpy09Y60-kMPuc1CEYQcewjVlPl9VcIKtF5IFGv7feAzN-dZRXwuukQMbTMIKCnOBRI7Y41-Xu5QFiil3vmaBLoRl0RiigCocWtFhV_tjO1W9Mxo8JtF-LZQl3emDsIhr8e9Z_H3qqGEdYFwmkKiY1wKGcJMLKYv0IYYE7xt8G5TmFiU8YiKCIeDoymL7N0ffTyNb0WM8PtTsXaqMTqXHj9N8_3qRlQkfAwnCsvamZ5OYR15wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSbrBGUPdKXg5ASPBjNmaGT68aoZoXhuI1x9uqsuEGQSOwdV6VDW-7PNPrRow53G8fDL0GlPpXiKxvO5Xwkp9ecvuSXQ3FxAu8vBb4ALucPluiNZYKggNlzuvM07tZErAKvmcGgYe9JsuGGNUSTb5YBd5oDmVAAbJFKqjzZ0ooPhADOgkGb607EoAb_RVjQSMbPz7JW1AoZ7QZ878AmUWR2pU7VQO0TBofaaYXximGZAS3HPcomQEu6S5YhVwuU1rsZ2cBLB3ygkSaO-Ljr9VDbjhNETDJz1Pn3hj6Tt4JFswSPbO72bVbAjUX-uJLWlYU3C1sVCOmxN0E_jBo3-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=b8eecYdpdU5fb7ECM2pLU3XVnnNUJ42XK76WPmHX6Z6CmpjmHy5a6VTlU0Yk6u28gq-XPcGF1IFlmBdos-F-iOBlbNcB9Gb6rVDV2xFyKvu2fpptLxy-6Yhs90zCnZ2j6cuTW2Ze1PNhUZIFVxXy8rDsH_r5FLEPP4QdXRb89cuVAsaqy-kutzbej6sJ05pK0w4sppkCqfi9FsEJxTGGCvqDNzfvDigCXTviTDWmkeHT6lfk_PbAFB_HDCLDjsgLUNb8dwi3rHv0a0IGnCw0FN3bwUqrXouzoXgSFmIw7ZWb_p_PWFVYZop1I3qvuk-okpYGIOsKwbM6hp1gHRYgwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=b8eecYdpdU5fb7ECM2pLU3XVnnNUJ42XK76WPmHX6Z6CmpjmHy5a6VTlU0Yk6u28gq-XPcGF1IFlmBdos-F-iOBlbNcB9Gb6rVDV2xFyKvu2fpptLxy-6Yhs90zCnZ2j6cuTW2Ze1PNhUZIFVxXy8rDsH_r5FLEPP4QdXRb89cuVAsaqy-kutzbej6sJ05pK0w4sppkCqfi9FsEJxTGGCvqDNzfvDigCXTviTDWmkeHT6lfk_PbAFB_HDCLDjsgLUNb8dwi3rHv0a0IGnCw0FN3bwUqrXouzoXgSFmIw7ZWb_p_PWFVYZop1I3qvuk-okpYGIOsKwbM6hp1gHRYgwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbmEmS63c8CUQFIynTJy9ePWeQvDqfhYMC7GUItcAdwFgSVEmplWRbw3Lm9nPkVOYe0pAOaEuMmm5WID4onqUKNgmEC5M16PRo7ijHZMhfmJSLYRW-9IcIgztD4mRrlYxmT39vaO0wAAtf63n3jjBJ3Rd_pTeCUA-ZCKGmKZZceIFSRSZo7faBSJXjOqujcAsv-gFmcDHKOMNRAEouKOrnF_Lh_T_OGMlQ1LrMKmxS8WXXqRBTTwt2xn49SvZGGs1cdpnfz-7Wzxbo1E0C4Vf8yAndACCV2DRx9viPYEb_yOMDf4lDSxjTN41JDWGr-gvTxULryg2gbTEBPmDGPrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTAZttzx9uOQu9qIPX38QaMEyInSPDoF0keoo9fZlB6tN1LRwTi37D4ZEAj9fnqYv7Bu_Ie3X3BK_7IlZ97lru3gJZIDrV98ytKWrmNduy7VwSHt2FBtnmfI_jZ1W0nOz3jovMi_1avFJY2WxTjV5qFJmDifxYYQbEtIyyo-DoIB_Ka5VkHIRh83EwBH7bA8Y5Qh5-pCMmw-tH9miVxz9-9-1ApSg5Xbqd83rgldnpQVRdSlI1X1bOuZtuCwmxzrwO4neA5KajlGsXKd9whOx9PJDiBUCBNGvHwhY4QaLPFoWHYfVaaIyf8-W8K3PTc0i_yAOkpLo44knJzLdx-NRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQLqjazNXxnFWx3tEp7_zurZEWayD8Zbg2-wbE4eW567JXCdHLBGB-0qVrdx0lzuVc4fjoGZCnW79eoUDC1EThftP9fMmWfTDg7Xi4i194UclT7Ai9frTYPHtUWX8g777Id93_dFdX8ASWEsT4yIQxP5C5i9J0XYs_FH-ieuQ6OfWP_fjfDdA8TAPZ14g6hcAso65ODua_jXX-VuhIrxzOsX6ly8CGn8MZCh12jD6NltwbBNkPpm65P0_cWK9dkdiuCy_4CDNR8y3rHiMGKLRprChKQmf3LHUiK_xj8ZZFC5E7WSHoUpYvdp0KahdY6iTu9SlRj8H2cHHDXUF1Emxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVKP1HxnFuzIWBT3Lq0Y6ELulI0Vi1Bsqfb2WjEeKUzdsxyheZ5uPvoXxQVsX6Gng3_dW3O-rqQsfEIaxHy1TFGuK9pfVBhdc56eLinrEDyovvmlsr3Ncjvls6c96igQa2JGQgzpWG3HJqvnclSGF08mxs4H11r61JbaB2wpaY1FjN65kPGLa4uozG_iID6YQ6HRsyKRWQ-NxIWfpmJyC4s1js9JPgNZcKkZOAbteVCRszIpRzHXbgdvZxj8uJAI5T0yYlzvxHLlQyK9mN7W7N5H10_OfCIO2HuDTYtD6r-2vflxAftyVq328P0V7HSReAumdX3mLZjr2iRmgR-fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=mfdny6qR5Wjlw1K71ikuze-DSUvNcbBuhzxpmKo_18iDlD-FBln6UcmMJIBAMY8Z9rlEDZr3DNT3UzTepycxM95979jEfAtKjKG3KjIob8cXxk04VAN3fplR1Z5TyalMRQLyfJJXXQy80YTT1RpAz4m7NAI4zqsYK5S4TrtA7BR29v8JmXSrpEYdEPZien88ZX3bQDjmbcfkgeJhCiegMkO0MyicQwIpmDYBzPEn-Kr5ffFD0giT5AEWknvjkz3zwEU0xx4kZFyUVh_wOVMhdzGellC8Vn9x_yUWr0ieeHHvgIY1l9wtBJ6yu3nefgKBf-3TH-Ucpz5BjhQPI6Jy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=mfdny6qR5Wjlw1K71ikuze-DSUvNcbBuhzxpmKo_18iDlD-FBln6UcmMJIBAMY8Z9rlEDZr3DNT3UzTepycxM95979jEfAtKjKG3KjIob8cXxk04VAN3fplR1Z5TyalMRQLyfJJXXQy80YTT1RpAz4m7NAI4zqsYK5S4TrtA7BR29v8JmXSrpEYdEPZien88ZX3bQDjmbcfkgeJhCiegMkO0MyicQwIpmDYBzPEn-Kr5ffFD0giT5AEWknvjkz3zwEU0xx4kZFyUVh_wOVMhdzGellC8Vn9x_yUWr0ieeHHvgIY1l9wtBJ6yu3nefgKBf-3TH-Ucpz5BjhQPI6Jy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=X95KWIqigr49MhtXUMSagzfJm2HWuTuHdg9E1J8QdZqF5vFGCcR3uHltQu-uiWeNg0h02b8YO39DZr3agMsYRiLQ4H73RUFvks9YAnJTmDKvjOib9JeUpUWXFc6HakbuTzvSwxRqDT0OXDFS2sYCrT14NvD_podm-kTGJWizuyM33GnqKK3JbwvT3wmmmm-DCvcvuHiCTW1gC8yTNJ0jFg_dFHXiQOa0xRufrYX3ggN4BJLgTygKaKtdK9qzAQ6E8PgS3h3fVtCtZcuzaCVxgTyDVUoY9YF_s1XJ-vWLQopw8dHlAUQc2DwdejuVm2DCBk8w5JJM12g_NkXs_lUt8hYgq4pH74LGizoAi45fb2RXoJ1qFXA0jRZMIVSo_FlpXUXXNKSmjfioBWiPSq6LAnTRY1Z0CfnZgHWNBWIMBT-seTaGVpPbheHLd3o02IOoovsA6jDYVYhEuGf4p-5HMUNDKI3cvGA1PRuGbmf2tz4u5S7KHEWdFAK9b7cgEH_4FvkdVWeLZ3l04XXo77-ejgJZY3zvOe9Sd67LQJQhbwHjhZtkUKQu4uz81Sn7gLpTlRu9uqr8XfxPvleCBOU66jhlGtkctaV-rFHZa96mZpAijrbXdkWY2ejG6efXeClGGZS1AIPFCuOprJRK7KKV9tUnuEWs1yFRD44E-N6rQEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=X95KWIqigr49MhtXUMSagzfJm2HWuTuHdg9E1J8QdZqF5vFGCcR3uHltQu-uiWeNg0h02b8YO39DZr3agMsYRiLQ4H73RUFvks9YAnJTmDKvjOib9JeUpUWXFc6HakbuTzvSwxRqDT0OXDFS2sYCrT14NvD_podm-kTGJWizuyM33GnqKK3JbwvT3wmmmm-DCvcvuHiCTW1gC8yTNJ0jFg_dFHXiQOa0xRufrYX3ggN4BJLgTygKaKtdK9qzAQ6E8PgS3h3fVtCtZcuzaCVxgTyDVUoY9YF_s1XJ-vWLQopw8dHlAUQc2DwdejuVm2DCBk8w5JJM12g_NkXs_lUt8hYgq4pH74LGizoAi45fb2RXoJ1qFXA0jRZMIVSo_FlpXUXXNKSmjfioBWiPSq6LAnTRY1Z0CfnZgHWNBWIMBT-seTaGVpPbheHLd3o02IOoovsA6jDYVYhEuGf4p-5HMUNDKI3cvGA1PRuGbmf2tz4u5S7KHEWdFAK9b7cgEH_4FvkdVWeLZ3l04XXo77-ejgJZY3zvOe9Sd67LQJQhbwHjhZtkUKQu4uz81Sn7gLpTlRu9uqr8XfxPvleCBOU66jhlGtkctaV-rFHZa96mZpAijrbXdkWY2ejG6efXeClGGZS1AIPFCuOprJRK7KKV9tUnuEWs1yFRD44E-N6rQEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=f8TlcyQrO3RIoR1GMJEcRORbI5-oCVX8FteiNMn70TpxrhgtznmRU39hb4HCqm7qrN_TrE_gpTxaArR8dzX95mF9seGTLFmp4EggJbngPAwqKbou6C4VNJ2E95SHbULId7ZHjTmVoEnMbp1jEbLQidzddbzAUSF4LZ9NeexnwkqEidSs9r43BASS4V2on_-7QFGFPN0pb4jo3DnF6myEOpPSrgvXWPaRmFp0IlDGTwBRbS0hBkAFMBUXNjTN9-yhPYEYQ_Guz6GlewaXU5TAMZY2tQNQdB_s8jrF_j_BSdwnk5TEfRKyQn6tnRKRJvpfYsLjeeOEomYK5phwTShGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=f8TlcyQrO3RIoR1GMJEcRORbI5-oCVX8FteiNMn70TpxrhgtznmRU39hb4HCqm7qrN_TrE_gpTxaArR8dzX95mF9seGTLFmp4EggJbngPAwqKbou6C4VNJ2E95SHbULId7ZHjTmVoEnMbp1jEbLQidzddbzAUSF4LZ9NeexnwkqEidSs9r43BASS4V2on_-7QFGFPN0pb4jo3DnF6myEOpPSrgvXWPaRmFp0IlDGTwBRbS0hBkAFMBUXNjTN9-yhPYEYQ_Guz6GlewaXU5TAMZY2tQNQdB_s8jrF_j_BSdwnk5TEfRKyQn6tnRKRJvpfYsLjeeOEomYK5phwTShGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=fjgeKGlu5cMoRbXmUQDXMgC5O-wNTdgXttnxEupZC2880OL85g-1HoV39rPX2el9tgtaa1mVAlkKeBcVeojyWp08Y09N2arDHG9mL8kU1ZuVp35i72ayJhB5jD_HkfScbe44FLKchiJ1FJP0Jn67pfpN9XCZ40SfAwkFyq4Sc_WlGiYEi5JjZ0DuDBlujqXARuihvBQxRtKvTRYJgga3gz7EvKWf-kmtX9i0B1jDYuQT6lWhSZTz9YM6W3vrqwJLhYZxHZLTRy3akz3Lu_m7Bu3ZXvCm2mbl7BzNB-Pqmz45g8-04Vlw6xJsOQVckjvK15RL4-9vChaGYKWIEBP5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=fjgeKGlu5cMoRbXmUQDXMgC5O-wNTdgXttnxEupZC2880OL85g-1HoV39rPX2el9tgtaa1mVAlkKeBcVeojyWp08Y09N2arDHG9mL8kU1ZuVp35i72ayJhB5jD_HkfScbe44FLKchiJ1FJP0Jn67pfpN9XCZ40SfAwkFyq4Sc_WlGiYEi5JjZ0DuDBlujqXARuihvBQxRtKvTRYJgga3gz7EvKWf-kmtX9i0B1jDYuQT6lWhSZTz9YM6W3vrqwJLhYZxHZLTRy3akz3Lu_m7Bu3ZXvCm2mbl7BzNB-Pqmz45g8-04Vlw6xJsOQVckjvK15RL4-9vChaGYKWIEBP5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSgtoQQykFAq8ygghY9Roh5JGxSkIZ92jpkb0itGc9E4dcAzB-xL1dQmjQeWyBmGGO4DoFoTddweE4rC6Wa6Lh96_kZ-pX41GCVpbZu7H9zNgNpoCqvVHQWCFzrD3HTSQvS-vcI-JL_nhjQrExYdRugbz-WqBVrLSyqlsXAQcCajNr4SOjgItGEE-t8gEhSf56gNsQBoe9AlJpGj6uli6zE6sG1ugfaZl7tL__Q3mVXEn5Vk3m2Dle7UbI18ixlQNIJdKw9T4I4bVc6wNRkJgC-BsG_8g-UwpYHdkl3pXgJz5xiBmU3CRuO2kOocUCFjl_cZCkVS78Rl2CHKWfXggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8akbrztSHZgS68-AIq35UlfH5Nmd-l93yjI5r8OQQk3jfEt6fotp8Fsjm9TylbMPkV_yJTMbqW9XWWe3lmwN15LD5wZHGYpaYWFic2VHQntqT6l0DO-Zp83tY6WNh3aCWah4HiCoBA7QdsXTvA2EdUzYK0cKM6T8lGkj2JqNgpiiYqD6Ms6BVXY6YcI-7Pi8M6qE1MHp4dDaHswD944XNzF9HbcMJ3bctNKMk_K14wq4SR9a5NN3Q5kYvlB2t87ZW3DMytIzTKotn9sAN1ZTGY8BoMeVRvPsTUWb_kybF2JC9XwdpGY8clavy8XkZ25LDKa_VhBJqqYKyQZzcL9Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT616TJgt5xd-717suSTB-ssALqOL9UUFktQ5U1kT8EDmjw-0Y-KMGgflKzYjUZB6e4HbfV65dO3p612CjjPuRlHEz_2GG3V8k3vNXzZiZU8KuElu361hDwuWYDWoxPvxWt5rox3FvT8ltUiCmNpH_TYj5B-NWAHXPAOhRpXBRit2NJ5CF03xKbO3JqbQ6sSjmx90eUJhX3PNgS1bxdp9uFRuLssW9XKP5l_2xjzHyu_1Sk6w4eBHA6NiDlQ7ZMN9VbwoHdFa0ANZJv1TtIjymTiQLp9BEf4aPHHcnrukf8PQMhop3_Et_FVOw_ESTgbtziYGkRVx2Aq0XfiDXOPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXz2ddFEAt-6kLb4d7JHiIC_gCaey3TtYATYcxzZgyguJIOWTna6R95NQm8nVJfMaJYGRCFljfWIkzrQbRIWEXxtcUL9Dq4i11zRugVFFJEOA2ojdv6dkN-33ctekErTZIQJPxv6-qTWxPcAgyHf18dHsVxqLMUXQ_nJ2GVr5qvvWg4vRikFmfecV8QBqCqwt6WKfb_ZkY0gCp_Vx46QS88FpmwjGawdZkMUhSHxcyekATpWibTEc8fyHACG66-euLqb8Bo_-DXYsS_FwQ6NjJOpflIGvYQ8hiJBxE_V2YEn352Rt6Kqr1v5XzWs_WEh6EyAKbFCfSIi-WEsmlUgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAp5KirH7M3D-Ws98-DBKljfR3r1O7vkukLBwM7zgTvG0KKaT8MAWejgdqgouGyv11Twxtr1SbK7v9LdEQ-If1-kbEYK-Y1YdNFygkcL3mJXoflmwr-H3ltfKicor1j_-olkO-yCZhz5km3PjLK_EuPps1QfM2340zcRfuOSjj1z9xsvKik_bc8EXkWTNB0MXl-HQKhGapa4Os4Tgya0OkuNOb0YARU4fpDhjGyEfuduq1Zc_9M5nFqO6QDMkoT5pbRTRuTElJ2aFTjPXqL1pW2zRGzP88AYNrgTrmAIeNvLKIppAN6_gaQSCSrYMX9kjtHnvuCHRKRN4hzH-cFsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg2B9UjDgwemCL-yD-dDFtW1_s0BTRboeVDd7P10UriHsU0jSxwrOQ1nen4EOJ0TxWQtSFoGLGmKgV-38oyZDMykz4PQZlKIsRCTI9bybTNJv7y3gToSzpPA5zhcmaVHmMqkk5bvzqPP-ZQQ-WBhw1UvvZVt_YBXceAUcqeb_CrUJcY7lyzlHdBem0qc8Zt-wbvJXkBVZbhp22ER1KFYnWGYRmdWbRp427UKShycwa2CRRtT3M59I13r1zuJ73VEPDygiBvDyUaElHWYSA9YMWQINkm-rOrlqU1s3rgUXj9dE21XFtSxYuGjxSBviuj7_nO8V8mtDLhus2t5Cq-A3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVC09NNb1rrMDljSKsxN8tYbgXRrcUJ-BagIr8QJP92D-nZnujJTZQjKJp4AXyQNqfLqoMFR3qBqxvqlsdKCt8Hz7X1OZIOC6Z051DaD-uHT-13v_nhAee4MvxBCIDQsePdTU_wh_7F_EY4_3MxBZgFtTJmAnahiblnh4G8KQ9i3XdVomfmGhXi1wqA5fOVPzislx22eL0-cj6S6uocI6zZnScVfT4ox5dJuVDiGURgO6a1I_L-zzCW_UUIeQa2457QOPf7yGgNCCdUml6qxPXKP703uzaO_6i1fX6OECgcXgGtI546CShTgP8FEoz1K92IrbBuWQfDbAzLV5QE1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1ZJrqj9xYqWafl8BuaLj9GG9MTkL9EUVpLEcQXibGGIJ5EzxWqcsFwhjkNS9Ogca-aE44MkQA3aHXiG4hP9KNubbISYKD3R6HHa1diMWlnKQF2aHzTZNbK--B6tt4MVP3RjOrVSxwZdsnLUoR7xmA1euInc9m4-RntV__S8iwbU5HH8cc7c9ZXfJQdzyKxmd0VYE8Kit4dwyLZXGqW-6XimyP_yg4AkBnubSHN3LFXjGXRGBkklkXNxh2PFYtNAS3IK4YVqe_8nXc5fvDzxSLqY2uwwsPZiYDKp3SQy4JK-Pbow7NKyDoymHbVqworyJO0gB3eHfkBUhOJRAu_iQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=WfsQTwqT54gp1xFkgpGc7jEWycusJFXF4bH9yk9geP11T23DTalHl4u_LqEeOv87P-sqQtVBuMRhU02lNJAsgMRKwJieWT-rrfCAJrwZCEHJ1NQAxcjaxkmyorBo1Sr1Z65aZThO6I1Rz8WOT87tUhOoZSMTysj8oA5Kc7_Bi9ea-oLJ9XAAVgK9GXd6CARhsAjveFmeAtrvvkYvF-66wqtUplFcOxN7JO_SfC-tXqNhGAPwuZgBRRsefTCcHaM7EQUCWuIumhyXqoH3UtoMCXoobXxz-KO4U7mODt8txzHQ69z7zozkToMwq66r1w2PxO1cz4JyE6D8R6qyickIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=WfsQTwqT54gp1xFkgpGc7jEWycusJFXF4bH9yk9geP11T23DTalHl4u_LqEeOv87P-sqQtVBuMRhU02lNJAsgMRKwJieWT-rrfCAJrwZCEHJ1NQAxcjaxkmyorBo1Sr1Z65aZThO6I1Rz8WOT87tUhOoZSMTysj8oA5Kc7_Bi9ea-oLJ9XAAVgK9GXd6CARhsAjveFmeAtrvvkYvF-66wqtUplFcOxN7JO_SfC-tXqNhGAPwuZgBRRsefTCcHaM7EQUCWuIumhyXqoH3UtoMCXoobXxz-KO4U7mODt8txzHQ69z7zozkToMwq66r1w2PxO1cz4JyE6D8R6qyickIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=Yjl3W4K8nvqKKlQGYYth3_1SNG-bBay6s04AvV1a-JL_4_Y-spEaK42HAh4jtUc2S4-qnBQfi6T0Eg_MGcyv-M2tDTZjenW7Um8zqLAZROzTb8-SMsCcb_F8LFP3g8YcM7XJgQsbZ2baBarmq1-aCL4lMq-vSOPbDF9QGZ5UA_6vniYe_uj4Hd8rKPSg-SBTjKu-Pke8mtn6esAgohExyAtFwtSp9xiPzXNX1h-puIasgaJUQ5n4yHEOPJoTF2qGhyiYspfPH1uIRSekuugwTLcPMhuAI_5xGqEM97tIrNXVC1lVR931a9MMW7crUHcJSPlo6qPQx_K1t96vkXAjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=Yjl3W4K8nvqKKlQGYYth3_1SNG-bBay6s04AvV1a-JL_4_Y-spEaK42HAh4jtUc2S4-qnBQfi6T0Eg_MGcyv-M2tDTZjenW7Um8zqLAZROzTb8-SMsCcb_F8LFP3g8YcM7XJgQsbZ2baBarmq1-aCL4lMq-vSOPbDF9QGZ5UA_6vniYe_uj4Hd8rKPSg-SBTjKu-Pke8mtn6esAgohExyAtFwtSp9xiPzXNX1h-puIasgaJUQ5n4yHEOPJoTF2qGhyiYspfPH1uIRSekuugwTLcPMhuAI_5xGqEM97tIrNXVC1lVR931a9MMW7crUHcJSPlo6qPQx_K1t96vkXAjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsJUlMVmtYZ9amKYBQ1FpI-Rkm_qKQ6C2fJc7RwJ4pI36rt-GvuXsKGtjYFmW-iszXYFju8KHh-uO0LxFQ-RpuklJES77A-K1xDwam0BpVTHrf4burihyZH25qIpDbP8OBEIGw1AF26Wlw_9ztdDALWM4HYs-eiiVSZvN8pWZUXgalURnstPqjNkcTp6ZsBUHWh-hPw6T_vHFU3MDiLyiN9lME03RtIKwmTf5dkGXE-PvaYLJovbZrUNGYunBo5CjhfglWVXxF8VMpfnD8LVi69y2xgaokMteE3E9wt21I1lZKXD6Q-omDCPcZ0LKxyqI13blVvqJOybuptIYL2csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=PHiGf5ZExSXrjQFGAwRjmmSmXt_k7tTvXlBPprVV_7ZPPdV-Io2DtN1v4DgElazZT9CVMzfg_RSTolujxb4GW1qiNIAPR7uW7b80NFQ0hl1F5IISp7CGVwQgTT0OxdL53yzFRmFwz5abWlPW3HnC-CWiLBVOJJbmFv289V-EyJ0qhaziZz4MwUyE2M-ZEkGjVbpZjRFT8gPC6OQrQyYv5ULbkUV8B5-vAcpqWyhbBBISSwp20YTeNvf6rXIQwAr0dKuheAtR1ju8Geq6Ovb7Moe1t8BJCEDLRrHecDTJ0Jqe6LTJdhqKaRfDUNQF0OLaNZcX3cPEuH_Qmi_0WxYK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=PHiGf5ZExSXrjQFGAwRjmmSmXt_k7tTvXlBPprVV_7ZPPdV-Io2DtN1v4DgElazZT9CVMzfg_RSTolujxb4GW1qiNIAPR7uW7b80NFQ0hl1F5IISp7CGVwQgTT0OxdL53yzFRmFwz5abWlPW3HnC-CWiLBVOJJbmFv289V-EyJ0qhaziZz4MwUyE2M-ZEkGjVbpZjRFT8gPC6OQrQyYv5ULbkUV8B5-vAcpqWyhbBBISSwp20YTeNvf6rXIQwAr0dKuheAtR1ju8Geq6Ovb7Moe1t8BJCEDLRrHecDTJ0Jqe6LTJdhqKaRfDUNQF0OLaNZcX3cPEuH_Qmi_0WxYK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=Eu7CJPxCFdIRW40awwIOLOhZ9WLo01V2f4Nd2T-74XLz2Yl67dKmjAmyeahxHI0X78xfuNtnzHZhpqxSe4iQCaxKVYeZkknxBYXYunFT-WguBo1qrhcvXFalRbgPnPMNG9QRydzW1scfaZ_riZ_VNqoQNMMOWPqMYKDKeZN2SQnmu3R9l1vp6dgez8uclhuqO7G5h-PbeCDpHE4ssJPiyNncvefPJAktQkDe1mLJFAoUOK1fBrv_wbBE0wB6T5mbeKjrzOPWaGG40SP5sBy81ddk4dxWhQoV_q7Nm2E7ifkbMGP0jJ-QnwHcrwJh2w0YeKVZhk9tmY4TmuH8F40OPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=Eu7CJPxCFdIRW40awwIOLOhZ9WLo01V2f4Nd2T-74XLz2Yl67dKmjAmyeahxHI0X78xfuNtnzHZhpqxSe4iQCaxKVYeZkknxBYXYunFT-WguBo1qrhcvXFalRbgPnPMNG9QRydzW1scfaZ_riZ_VNqoQNMMOWPqMYKDKeZN2SQnmu3R9l1vp6dgez8uclhuqO7G5h-PbeCDpHE4ssJPiyNncvefPJAktQkDe1mLJFAoUOK1fBrv_wbBE0wB6T5mbeKjrzOPWaGG40SP5sBy81ddk4dxWhQoV_q7Nm2E7ifkbMGP0jJ-QnwHcrwJh2w0YeKVZhk9tmY4TmuH8F40OPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqiiX2X3CEuiEtrS0xUQfpGHnYOjdEdnkSYXF83rWF_aLfAFjH29vh7oJWaYeW_xeXDuUGKGd8WJVeeALB3hbpXWKhDUbvlf4nmvYxqnxh4b-7_9jgNUKKs3I2sKnZe5jj_jjcZ0R4Y-2gI1jLyejkEkuqIdsaCObU9_Mk1uLn10BflM_G5pF1O9RT6CkulrXkW4WsGN1xuVpMwbgqgsI_xEClbwKWi3CpyQMQ8BKhv8S7AQ-Fxc7fKrJkPczH6zxQYsuHh2I2ggmTlPqoFX_gbwIDsgb6HON-fuKgs4NYzi9naHY_k1o5Qoz_LQDWoG1CXWuv7mmqAUT9nMO3nT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQx7nxvf64PdhjzG29FBaId1YbYTiMvwtgRjcwupaZhnyptXxHKED85Qtzm1D8eBih6s27XOZWBTxttXeVxM4FGiu_MpzuqmYeyA2tFTv0hQ2rqRRSDpbNNJKPBzGvI9mGQMnTVVxL5MrOqP9HvPbSin3ualddEuVGI8HxaGXU4oBWSX_R0-qipjXBFOHiE0G4O9ECrL0NyB0TdlBQ8DeXdX1ArT_pFvoQrJesR3b3Xpa7UjiUXv725RaoSG5vIiixC5aYxXbsW43wiy_ZIlwvF0NfjaL_qj9lWMLM3MpyO35PHe2gzxm5NfhYXSgClSFbuzL5YiPI9a7sz8lGm_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRMR2UgETrrM2EboarqOcbTjZVIg-w1mAv8_3HTX8pZengOrLMF8Ug0GIAXSpOVT896Vajrsn2WkZrUu7HTPRcgJ0abUuBSVCETwg5FGuYlOLCF77GIdfjV2U6Ivepxmd3BcsTgCCxBoTcDQ6RjwMtQzqPMhbG6-mqauHcoqjHinkLd3guYvUMSOUGO9rBUMLs5f9wWpIT0u9AVG6X1VPlOV_eCEPDNytn10-6saNlEOeyLp4eODWb7sQJxtiDmwFPuqBDzHki3Oki4FqYgWDVoBfoDN8NPXrBzJq4ehs5S6bINSdZT5EkgBc91MaLn_g_m3ONgy4w4G5cvv7wreBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=goKPeYPkuO5goYRzmSv8mXDXYz_uqdfGTCkuEaRddzdGpK6iFbpN2kmA3Umoeh_J8NAKpjkVN_TjCdKlmW4Ahu-R2f-etiS1x1gg96OCGJsmeNFd6O2daUqOIblGHEKxaSfAkpN2_dyZ1JyRbSciZijI9xE9e4uccAzFZF2jemfyEmC_jQrur-FmDs1idA0hpHK-g2JPPBCmPLBrdyOQLhcwkpIoGlOrnn0d1hDwx2ML_xSfSbJyD4226yrqjtRAXQCQTwPToy9KHdvxRb-T1KCfuxgNfKtU8-xqLO5dGu4p1vJKs-CbZDl785Hn6ed1cei8TfSeFFWiNJaXfCurnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=goKPeYPkuO5goYRzmSv8mXDXYz_uqdfGTCkuEaRddzdGpK6iFbpN2kmA3Umoeh_J8NAKpjkVN_TjCdKlmW4Ahu-R2f-etiS1x1gg96OCGJsmeNFd6O2daUqOIblGHEKxaSfAkpN2_dyZ1JyRbSciZijI9xE9e4uccAzFZF2jemfyEmC_jQrur-FmDs1idA0hpHK-g2JPPBCmPLBrdyOQLhcwkpIoGlOrnn0d1hDwx2ML_xSfSbJyD4226yrqjtRAXQCQTwPToy9KHdvxRb-T1KCfuxgNfKtU8-xqLO5dGu4p1vJKs-CbZDl785Hn6ed1cei8TfSeFFWiNJaXfCurnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gw-wrD5ngg66qRLTPp6XEm_8M8Qr3lTKqRUTcmZdJjVTjhuLFG3KzZL6mhAWzUHnHo9UBsPBVgUwXqe757a2wtEW8L7IzyAS2aQph3WkmNcKXsGLBlFdW5i4J8hEMZFPMK970EHx2dcC1EcyKgs65Z0FqjdjBCh0ra1rdddaof2ybK7LCDv9lH_c056qe4YxZzynjjPLTBFuBregT2fPaLumyP4PZ4jvxRLiur01uuAEqaerVrrEdZtxKKoIeVrwpnadnIctiwN7lwT4ZZXeU_7UvK4ZggLzeELMWK0GXrP9Uf4a40ih6WApQXFV_FqCtS1ddmpqt6yPiVhi1Jb6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSfTZKNmiXc0K0ctdoxPYeYKSFknzX717s8AaghkKiHVHHRMj3c-pB8MsO5SXt2cClGMy7MRLwg5YndUzOpI1_CzceUy5MUCf9RsSmtV3m_P53--pqCMASxxzKKzyfNoPSS1EXWXCxZeomG6fU7NZPRMVhS2AnEdlzNkG2QE3ZGfDm4j3tjX6feMSbKQqm0mKk1eMbWGvm-eo7MsglsQzh7BpRf4akWQWkzAq9DqXrx4WgTeWzcJBhRKmwHK3_UGRCyZlpSc_HdNsWjQSXaZm0tzMonaYEcguhJ3Bnecv450YxNw7dzScL86keidlYGlTYmq2rI4e2m2163bPELNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXFS_JZY0FEM5wbQhqhoa2BMBExwHSGV4kxn_-gWwKP85w8PAtHSltGpXeN_wT703jXbHzYskxq_xYGkVYn1vfGurPTYH_GCcvCv61H4esJL1wU--8aq3qA-aUxm1avvLKFl4kTK6H1qHdUoJjh-82WRIxCIQc1MjKEFi8bWZpFsILNFig1ZerNsdYHdv42iKtJfdSSRqW5eG4iM2OLZ_NINUX8AmYSZsioP6a5PsDPxgV7p4Yqbs-whhH2wkuQKDqZPmUdKpO3Gsx3ftEc6FbnBfOgWw1adFeU4Ux4dc9Zm5g78tVVAjlFY1vrS_dyC_6rWYq_NKc3nN0hr8ZL3ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=BVemzgtBNHrzkC2JW0JC5AjgPjlISf3FtVO1CM6KiB4LkQcTYo5dPA9I-PXDMF-OjEr7ROWnN4TUQj3kpyj1FK3pG1Xswqf4yg5xm1-oLRd_NJjW2WGrIFTdH50IgXGkwV-vtAZl8t8HxF8TqLrjGLBZbIUlbF61iGlVs7AobbRkiSksFny6H_Io-RVHFgUwqQJ89k1ojHdr9iCIprthGuxrewLYZA1Ib8MFwLxWUNoYw-AZn-X__M58eqUoRQMdJXIFBM-gyGTs6mIXE-jCSm3YeKc9ACKnNq_NwprV1Hab8wtPyQrSrsFnsgNFrFkqQv5p2nK9EjO8wjDaco3l3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=BVemzgtBNHrzkC2JW0JC5AjgPjlISf3FtVO1CM6KiB4LkQcTYo5dPA9I-PXDMF-OjEr7ROWnN4TUQj3kpyj1FK3pG1Xswqf4yg5xm1-oLRd_NJjW2WGrIFTdH50IgXGkwV-vtAZl8t8HxF8TqLrjGLBZbIUlbF61iGlVs7AobbRkiSksFny6H_Io-RVHFgUwqQJ89k1ojHdr9iCIprthGuxrewLYZA1Ib8MFwLxWUNoYw-AZn-X__M58eqUoRQMdJXIFBM-gyGTs6mIXE-jCSm3YeKc9ACKnNq_NwprV1Hab8wtPyQrSrsFnsgNFrFkqQv5p2nK9EjO8wjDaco3l3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=oH5EQTHCREoV2i9-Ib81I5Z9rUrdkN5IimfiDfcB42WtuGkRGy2EBd6ggcBGpISvYb6Nsbi1-Z_FVcaOq-e13GArDESs5ns6-zHLb2gizgZbNfRvanpGnV68Tqbk-SawRGIkEFvzYaTL5gBRwPt68mk9fHm-wzPikxKVSpSWXwYj9taMzct3pH4uwBPSI8LftxkOOhble94UDLPP7B_tg_Xx_mDz0a4pRGIrDiFzgLzoJF8nRhQVW7xVjP8aVMKFondOmEREp7dDBIOtAkYeBUM-_JhrRkGt-dXX-QEyS_1Pgn6CGW0WxaE89qTyhsN3PrCf_-17FUfR0ki_tYXBSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=oH5EQTHCREoV2i9-Ib81I5Z9rUrdkN5IimfiDfcB42WtuGkRGy2EBd6ggcBGpISvYb6Nsbi1-Z_FVcaOq-e13GArDESs5ns6-zHLb2gizgZbNfRvanpGnV68Tqbk-SawRGIkEFvzYaTL5gBRwPt68mk9fHm-wzPikxKVSpSWXwYj9taMzct3pH4uwBPSI8LftxkOOhble94UDLPP7B_tg_Xx_mDz0a4pRGIrDiFzgLzoJF8nRhQVW7xVjP8aVMKFondOmEREp7dDBIOtAkYeBUM-_JhrRkGt-dXX-QEyS_1Pgn6CGW0WxaE89qTyhsN3PrCf_-17FUfR0ki_tYXBSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=a91heeypcyn1yaZeQkhY5V4vNo9cq_nA8KJNu6jX_mfIPLUAk7eT8WCtc9SOHCE4mjFV9c6P3fkpoZ6bXXhCgjKc-JVH9I_SeESnVGZK801Rs7n9p1jWyuozgwwIHDVujqrCyT39SNi_RhlAgRVkTedfA_aAT7uelAfnHTIsQgu1BR9tFKar__R6iqc0T2vdC57DNqcgttWC1wlJVhVnxh-pQGyCZsZlOW1uyeuCcqPI4WMrwwGKo3ua4Z8NR38L__drH__8oIqSCuBFadyXcwBo4RdPGHwiWoabADTOq30ZsBmUV_36AG8SZxkYK10xoRR0QcNY59sLpFr2F0pFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=a91heeypcyn1yaZeQkhY5V4vNo9cq_nA8KJNu6jX_mfIPLUAk7eT8WCtc9SOHCE4mjFV9c6P3fkpoZ6bXXhCgjKc-JVH9I_SeESnVGZK801Rs7n9p1jWyuozgwwIHDVujqrCyT39SNi_RhlAgRVkTedfA_aAT7uelAfnHTIsQgu1BR9tFKar__R6iqc0T2vdC57DNqcgttWC1wlJVhVnxh-pQGyCZsZlOW1uyeuCcqPI4WMrwwGKo3ua4Z8NR38L__drH__8oIqSCuBFadyXcwBo4RdPGHwiWoabADTOq30ZsBmUV_36AG8SZxkYK10xoRR0QcNY59sLpFr2F0pFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=AYLJktSIcMzrMgGrk8SU-YHvEGSpG3ypGZAYRctAZwtOWeMTa8fV_DkwHxNB2TAa7iEQrH7YacJxRZg3LIs_-5SQHcYAUu65UBgnKG0xk3IWsCnWrzEw9r7_dMldj5xTMMvPazNZr7VbGC7DBerop4tW-fCYe0rdWNfNiqdl424gdVrrvBYy9Z_emBVdDlI3hLiDZnQLOjCMi1Iul7JPdFpDnaGo03zJLiwGp0rz8RKpOrMkyn8K_oxD4jjyVS_KziET72JFT0Yjbwc2_pthDhKg9AzSerhqSiFT--claDY55y0eJzB2uh2Cni8y3hsex_FVZy0weLiVEmMPQLgUvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=AYLJktSIcMzrMgGrk8SU-YHvEGSpG3ypGZAYRctAZwtOWeMTa8fV_DkwHxNB2TAa7iEQrH7YacJxRZg3LIs_-5SQHcYAUu65UBgnKG0xk3IWsCnWrzEw9r7_dMldj5xTMMvPazNZr7VbGC7DBerop4tW-fCYe0rdWNfNiqdl424gdVrrvBYy9Z_emBVdDlI3hLiDZnQLOjCMi1Iul7JPdFpDnaGo03zJLiwGp0rz8RKpOrMkyn8K_oxD4jjyVS_KziET72JFT0Yjbwc2_pthDhKg9AzSerhqSiFT--claDY55y0eJzB2uh2Cni8y3hsex_FVZy0weLiVEmMPQLgUvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=oDgfoRH7r_I9AM2Ify9kjo700XyKk_cbUvL_0ZIpLD79pyhJ8aoebmB6UvBZlGHAT5YDkGDLL7aGhbuGmTvzyLU_1lf4irIl0bgItEGPYB0BI4BbtOuZW2E2XEwBJQ9nsTH5gnqpBRvWfo5LezzcrAaw2XmUnSH88L1GcVfQRb0WLdo1kSB9eLs9IVLmN8ODdhAiPb4FNvBa1xVk6S3y169nybMBK3gjgIOXMiGrI0-SyIde1mIBonkds1pQ0t_OMB4BmvQ6LUuTUskUxZqgQLliRlIiYrYvcBgZenkkFrD2LVyUv1y67xZzetCBY3WJjA8CPK2dSUOxDflEaV1sng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=oDgfoRH7r_I9AM2Ify9kjo700XyKk_cbUvL_0ZIpLD79pyhJ8aoebmB6UvBZlGHAT5YDkGDLL7aGhbuGmTvzyLU_1lf4irIl0bgItEGPYB0BI4BbtOuZW2E2XEwBJQ9nsTH5gnqpBRvWfo5LezzcrAaw2XmUnSH88L1GcVfQRb0WLdo1kSB9eLs9IVLmN8ODdhAiPb4FNvBa1xVk6S3y169nybMBK3gjgIOXMiGrI0-SyIde1mIBonkds1pQ0t_OMB4BmvQ6LUuTUskUxZqgQLliRlIiYrYvcBgZenkkFrD2LVyUv1y67xZzetCBY3WJjA8CPK2dSUOxDflEaV1sng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmzdBNIWWKhbiG6oJAIRqI3g_1jy5ZMWQHDhZ8e5hQddYtX_VmbVcfxYdNe-U7M5vL9ndJgv6cp32cJcId7EG32s8T53VIwnwk-PGm9KKTgB9Mii75eakR5ec7R8HSmiETBo2V-Hvj1TMILaNYwjZ4gtslAFu1PD1HIfGuOfrcKIrAbD0jGCKf70otwI3MUA_Q2iu2NqySh1Ck4WBlh7OL8g_6qUWqFXmMq9iarNyIheg-_9_IRpFSZQvzUO9eEcE-oQuiFrn_2QCLBHuwWAiPfWEBbYLChyIqz7GejbwQ-tSNprHMEQ1pS7PjX0huZTslAosfvjmCMi4zzCJCyTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-nb3tuG9ak4hjqzG1YMkXLb0C_lCi49u5d0VgLnY1VsUOd06IMlBsH5vZLVj5fEQaafeiZJdxwUiC-OOUOTOfQnhlvpxzC81NEJJrVWxbAd8p2sJn-q2ZdS8AeHKE_k20IdN_2qL63Fk4HCZ90yqN1Kb7_z8WjPcnTxaodISnza15DOh1PUrQ1_aaFVnWokXtTLJDRerNi9nDM6MJ6JxCUM5KDHxy8ELTp0mClsLGgl8ztg7jlRpEVDT5TLuxY-ZHST65BIKfFYh_YfxlVGagv061LAwmVEvNDmNU2D8p--Xj1XXGETkkGh10LxoksmGbzScQCv4ZCvLk--9DoD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=bSmE2ZNlQHlTxZQplMHjV8nfyqOBys7MmNNeskiR5oqtwilHfZ3xuZMaHZ4IuRm4YYSMEUW2DR6sb7W-LE35nYO_uh7TEyGfJtJTpYHixbe-jhBjiXmtCYjFMzh_IAUS_1V7nuPODQw3Z8BVwQ_eF6sfHN9mrOmw0hMG1bJc29BMYxq_Elb4WlPh9zYy285ZLo1yNkQ2H5UVWNdvZWNXH5uq4iBBHnHVNyK0Y7UWHWaS8-Qd-Mkph_OEgWB18K7m6Gvf4Y_FwZfja70ZkMj8CZKZ23pfzStHyG4UVPYRr4jxHR0CoqJY4gMr0z-2r-xxOuyRlmmVHUPqKrm4FOwHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=bSmE2ZNlQHlTxZQplMHjV8nfyqOBys7MmNNeskiR5oqtwilHfZ3xuZMaHZ4IuRm4YYSMEUW2DR6sb7W-LE35nYO_uh7TEyGfJtJTpYHixbe-jhBjiXmtCYjFMzh_IAUS_1V7nuPODQw3Z8BVwQ_eF6sfHN9mrOmw0hMG1bJc29BMYxq_Elb4WlPh9zYy285ZLo1yNkQ2H5UVWNdvZWNXH5uq4iBBHnHVNyK0Y7UWHWaS8-Qd-Mkph_OEgWB18K7m6Gvf4Y_FwZfja70ZkMj8CZKZ23pfzStHyG4UVPYRr4jxHR0CoqJY4gMr0z-2r-xxOuyRlmmVHUPqKrm4FOwHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdqc4UyBDgAOKJTQZFS6ZJwGtteh-lI0dXKSLShKwWTbOwEJvKmC3lXG4CE4KYT_ZtESf9j_nOt8NpHcDF1HbuPhtuOBal6s1qm9vXGi9uctj9PF8qBonsgw0a5p1sNMe4Ug9-h9HOTK8HB95XTaI90YTIovYj6PtZnIEFU1a8FjoV7GokbCjtzd_7MP-mP5wlXdbwV5xqklfyI8VKcYbC2GNRL76wGeabTb7HwkFRsdGghNA_XYoTJJFZzDf7b1BdSTAvEO8V5qhN9GNx9wWJ72vgHka65VLgp_4wX4sXy6XSw3s8KFMQtDvglAHKLOMuBLQtgCXJ4s6jA4Rh29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIRGbJ-SNfVTWvK09I8qxX6SDv5MB2MVyhtXZeKgH2C6Vs--V2oktW9g1NC81m3poZ5sZT3-TAVD8DiKvZgONGtVu-NepEJBPfS-9lf4uODFz6-_swhrfEyz6nbafH9PcegnE0hhPUWQGptTWFnasgxtGBYlwy3cMWunROP62C843zGBiPV1_IsnbyB7jTSXJ7fwyXR8zbF0-uQn8TlDTvEyCyUOmJRelryVGYkk1uIQNa_Ym0X7bFrjzP8TR3SWvljcDzIP8Yr39U2Omh1CBPz49YmfQKOBg_Q2aLTSJ3hECxzh-P6dpSMC6WjNpaOac-QUIBEFDgw5ahOa_Bo4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJMPRXXTFu7dAXZet7Y0j_VM_NTvk2QLz-gqlhGvsQk_VzfSEkVbFpVsp9uSpjXN2-wHeX1ekP9LMK8r6nuKiXXH6GET8tUX5i4Npu6S53_WOVA-6u1BzaUOexJQZOx8MSoWPHPqqfGd5JwnC2tlWwITbLLBFFR-oUmm7rIJcO0j-8Ogrj8v9dzoHpJ7bO8y1gxtWFUTOfFN0i2HWUbkB-xItezUXAaNBBg7id1fhj3SRrnhMtysfnvczIQ9RSmxRP1Nyn9HSDdlXlkZGaO_j51lbxT1o8czPzmuDZXeJWOTO5GAIei-UltFimQuoX55m3pLYJfStdE3geoJALF0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uw2oeTqVQQgTrtxghpfwqHcuDEICZSOILZA0TDG66BFzm8DPd3NmbAZgV04cRqRWxgXp0f1iXt4C3DSGuzfqH-0A4jrGKit2DuTqBog2RXoUf0UPociK6o382_04ylJAf6lA9_Uqrc5FvBR7xeUVA86fOcbB7YJpRGS4GxeHikgKP4jEkHvRbjg9eO7wOVjUySdsygXeds-gE5jg5-4TR4gY_4QjgyldWLY9iTOWQGD00Fp26XoF87bcfVMIUvRWfsJi1PRYj0pCWbZ6DcsGTP7YHCNY-uwvFY2j7Q64K1I5NF470yLR-1LQyUNOSiT7NOrdQcLbfLvfvNan7WHpDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=Q8EjKg1gzET66MOAaYhMcD_Z4Mt6mOEDaQsCWWQ-ZxAWeI20nHf2nXeLvsMiL00KFKNG6vvll3HsBaVtQiAgdVQ7jOFkSPQ_bX0EAPLdAzRq7RCmXY2XJgvDaIggxeWvpS_2iqWNqIYrOJSyQf1SiHxRCAIs6sU5nVXxEIQLlf9RA4JF4mE4Y4xzCbEFkPIdR-RnK-nxSl0859vOBIm1JP4J1hdrp2uCt9n5RwSFG4sWfZuSBa8THbXrccuG7yP4xA7Sb7N2UFlJ936tGP7BfY_W6J4BRwYclV2Mj5jmmuz1ddR58xiZMSMf-9Pl0WJi8BARjzTIT3xyfjRoG62Eyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=Q8EjKg1gzET66MOAaYhMcD_Z4Mt6mOEDaQsCWWQ-ZxAWeI20nHf2nXeLvsMiL00KFKNG6vvll3HsBaVtQiAgdVQ7jOFkSPQ_bX0EAPLdAzRq7RCmXY2XJgvDaIggxeWvpS_2iqWNqIYrOJSyQf1SiHxRCAIs6sU5nVXxEIQLlf9RA4JF4mE4Y4xzCbEFkPIdR-RnK-nxSl0859vOBIm1JP4J1hdrp2uCt9n5RwSFG4sWfZuSBa8THbXrccuG7yP4xA7Sb7N2UFlJ936tGP7BfY_W6J4BRwYclV2Mj5jmmuz1ddR58xiZMSMf-9Pl0WJi8BARjzTIT3xyfjRoG62Eyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
