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
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_SCRTXIZ3SnESPG_wvKLm7eAk5tTQrH-orNFDMkurHTpU_u1G3kin7aokjf8YmViDpBkhlO2bC_HPKmoWgv4kJ53PYBF8krzyLKhP2EtlSagyLyRIg_cb7RBWrL0Y1JsXJIzxYRyuSVy6RgGOFbf-6PBxw2dd6rFBgtQ0BgSxwscMp7mYbscfO0K-sfmdD5PeZS1xw3Rs3bGXYIS0VpaKW9pj6roKFBMNCRhJufaMlOihs36iTzJiEt4kd9OV4BuvRc5ZcsvYrrFMInNiJVo5TUTivMECtYrDOOrvJbzjghHxpvbSfcE7_DQ3_7yLRYe83pWfmjX6I9euk324Rv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjEFofRyaqinnTPAYE_vo6TWPvN4TIy6wuLFCgWDgEnbwMkya8aSpDIAbH-QuexISsrNl7R9gUbLRdDJxc99j39sJm2mZrbDrVXsCELDhFhBV3CXpG2Qxeu7Cme5380fsjAB5NCmpuzDeFSKXHyDmsRAmjvc3m1NPY7CC05XAEK3xC-1e4WW1w9IabxK7MPzhFlBRmsShwpzGG5dZbVS5AJcamy5-0fC4vf8ZFLSbWz41E_d-KqyFQ8B9MqJDctIzsIjU6icovdJgNUxShV5BBNDfPDnjlRngGyUywkxOyLB9NAtj3dMKk8Tz0c9MdIggRuGT1maadokqnwtB6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEK68BX4eNB5pxr7MKeKZ6h1UZyTZDu2qFLQbNM2l8NNPzwIhrsrcB9oRTYKKBDu6PMejC9MpqoRAA6pgxDKlIpgyBDchZjjKNquY2qdYn9KJoGHo5XFFYDcoM1fE6SPJOjeAbrnF4NdhDj1KiKWDBRxnCjP5DjFvagyJv63o9Y6E-UFBa8rRiI5zW3sZUVkl9qmCPAUxRClsB9lD5t7xjkYaR-teTyE1vEQcX86elXamiTWbF5YpfRQXwNke9r-eeaz8Pm95SwqizPPjGMPdlAf6g_0OxC8z_H6FuaaKEkOHzQS_-J4q0p2WzjGYC5FkOPmQG0J5NbDlShTGctk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ63as7Tp4L4Kyiy5_A4wbvqQhlHHia2GdLokuamDQCiV8uyoUTTf92zJXIiuPK4kVEkl3E55dzln8A4iWTio3eZW5jFQnUj6cdfHELhknehROcBuuFW0rQP9d_MQFRfWwvcuH-6ZU57T0RpReMg7vA0VsUmoMt71vb14yLWoKbvS9Ds3M700Pze0Vk8E670fdB6oLdkTtwiEy-qdxTGxOP9JFcueDautwuaJeZ7DRBEPjMEDGZguaRDOTYeY17UE8pZoO5mCNRBF0JE3YJPjm7vpoeEstvvwrawYwZ6u75E8ho6YfAPpA2A7fH-Pe5K24PAsv_Upsu7VVYHDzslww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCILebHerj1h59p4R76BI7xSKvhl1nhH8UIK5tOeC0LuTED18SQj7xiRNFO2__7YUO3PpEZW7x8_uiiwCJ-NYVYsjOPrXEY0rpBbNpwbT0nfMfRnlPEYPzuAUscASwUv0e8RjqQh3OkASF0NG02VWqVAtl1_SXgFTHbeCo26NI9svf7-db927vLk4bDYdaXQexz_V5QwCb8DHg5HWHbHFoarvIJOKvxOkMOzTUk3hCxLsFnGNxAUv8vD2pwjgSnmQVQFg54EZrt46_ZLKMKCnGkU680oZBetWbWUQYAc3SgyGEnzve4S3oMXpSL1R9MPCVDof2PRrGGfbwu_wVy5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n54U4kvSGnD44oT_8WJI3xSaDZ9RTSnlKmASqCH7dGKRMpeYh7BVKnMtRsY0utBsZtO2r_rdl7zXi4aOlQbPOdvGDD4UylQ8LOZpxXp_YGqBT5yF8eTdYkKGgfTOCVhigMVFhdosmOR94j3HL5i3o3KdqdksBmgkIuCpOi9imaEuAEsL89iSsM0KxB25CIyIi1XzDPLUyI32wVVHea3_PSXbjNif4hDL6p--WZOGmNXaxdWoqvJKFxP0oxbhXTZGsBVy1zwiFTIkQ1zSxRpJM1sM4tJJMyyXh-i_PlccZbEtjr1O9bn_bBCVBe4PULafpcYsda_mgaHO_Kq1aZoiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=h9NIorOBvtSvADUVGNjMbNkDBJ2wexYFodANaCJ-XiXFC0ZoFX1740ZU4EigWFKdWyla0q3oAbbuH1Rs0v_B0LotDcyMUI61eissu2qoOFU_Us2PKKPa6wAulRSFqzCBMmHLP2UvdSR67TTlnq5Lr7se7PtIS5aXSHmgKQDz4tlVOcDjmugHSD-GA-IOkEO0b_8PNbn1my6IqIaUQyP-tkPuT8TFn_6mOTv6jsxNo6ZlStwHLvmi1VIQnQPqYEXbUBIy6CvZlIOKVQZt6sy9pVHcBY7fwLLjOuLhsp3YuDlsvb4tPkBoaLQNHwEcBs-Ket5-ZlZRq8JZ3SGJ-A5Hkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=h9NIorOBvtSvADUVGNjMbNkDBJ2wexYFodANaCJ-XiXFC0ZoFX1740ZU4EigWFKdWyla0q3oAbbuH1Rs0v_B0LotDcyMUI61eissu2qoOFU_Us2PKKPa6wAulRSFqzCBMmHLP2UvdSR67TTlnq5Lr7se7PtIS5aXSHmgKQDz4tlVOcDjmugHSD-GA-IOkEO0b_8PNbn1my6IqIaUQyP-tkPuT8TFn_6mOTv6jsxNo6ZlStwHLvmi1VIQnQPqYEXbUBIy6CvZlIOKVQZt6sy9pVHcBY7fwLLjOuLhsp3YuDlsvb4tPkBoaLQNHwEcBs-Ket5-ZlZRq8JZ3SGJ-A5Hkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ahlwRXjHNyHg7hP6hH8hH3L89irXhGMWMVxL2W2qOmxJeQaFoMcuImDByej4euQ5zg2HSi76FfYN250sAUNbKIGLu4pt-6sADbONLdckmlW5pSn2DmM_VWBsNEqrq1pplkmhfFluZP7g6kfoxcWRA8_aXopUEAqxxOZN0W8NTe20z4uNlRjIOB8NaY0rvQ_aKOo4EjqpX9gTISTb-ek6uThKSHeTNZhbMGk4NZJxlJvGSnn4db13RH8r02DlH9wxs3lxrKHwXpf7NynHDcOp6p0w44sRFwkM3pCnLjmxWaVp30i3IY-WZJxyHHYlgrcJHClhA2r-k0BtnJf8f4Xw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ahlwRXjHNyHg7hP6hH8hH3L89irXhGMWMVxL2W2qOmxJeQaFoMcuImDByej4euQ5zg2HSi76FfYN250sAUNbKIGLu4pt-6sADbONLdckmlW5pSn2DmM_VWBsNEqrq1pplkmhfFluZP7g6kfoxcWRA8_aXopUEAqxxOZN0W8NTe20z4uNlRjIOB8NaY0rvQ_aKOo4EjqpX9gTISTb-ek6uThKSHeTNZhbMGk4NZJxlJvGSnn4db13RH8r02DlH9wxs3lxrKHwXpf7NynHDcOp6p0w44sRFwkM3pCnLjmxWaVp30i3IY-WZJxyHHYlgrcJHClhA2r-k0BtnJf8f4Xw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=KRc0NEh3d1pX8rJPqJCzDcF3TQViMeIQ2L8nmWD3iLcMLcQspUHmLUYBVcJq1XGlkDNxz38MH-QrE0F3HK620UvkyV3f1weRl2cF64vmqcsbPJJb9wUtha2fAyk0K8h625SX9m2NEcMmeRSoLkVHbdv4KVC4vXdolClVnSXkTPPgEJQqso8IiCSE0cnv5ly0LyNKdRbIUOrqtWuic1YMC20YqZgfyD8U7oneCZztHJNoGD-knVvO7Gl3t6sYfIz7WYCNgD5YRsyGeMu__fa53ZPuYjeXUXOBdcHWwIqAsvUHwp135AuQsHVULS8olvACocuuF-IYqzjytFpEyrL1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=KRc0NEh3d1pX8rJPqJCzDcF3TQViMeIQ2L8nmWD3iLcMLcQspUHmLUYBVcJq1XGlkDNxz38MH-QrE0F3HK620UvkyV3f1weRl2cF64vmqcsbPJJb9wUtha2fAyk0K8h625SX9m2NEcMmeRSoLkVHbdv4KVC4vXdolClVnSXkTPPgEJQqso8IiCSE0cnv5ly0LyNKdRbIUOrqtWuic1YMC20YqZgfyD8U7oneCZztHJNoGD-knVvO7Gl3t6sYfIz7WYCNgD5YRsyGeMu__fa53ZPuYjeXUXOBdcHWwIqAsvUHwp135AuQsHVULS8olvACocuuF-IYqzjytFpEyrL1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpQhk8SE0LRkYNjPWpDn6-aPBp0D4zJ85ewuyWDtan8-gmxGNxnO2ZaTHcmr8gI2w5SL16XN7uModYKpyNHadI_wGu98PZfioN3-fwDXNnJHrpP_8GZOkzcNVJ8UT9rBVDRoJUUnSOFsOhB1Gz13pKuGB4wdAFdqC5HwAq2NGxRpcWJfNj9Ha5lNTOb9GVpc7bSRfi_hZZLK31gG9ui_5zEyGVOalqaDFXF30bMc8HRzxojM749jGzbqw4m9ol4XxmOZPYEXTopvrBwLWYhk_r-mqt_-h9_-gragmZYqhTN_x_C-U9HzamIWOpHiya1koCZuNTkwwFNui7bME0V7Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xo9Qo-DlSkjw5YWT1Q_uqtfgx-JP4L2PaynI761I7qr7134PNsGHdwIdWS7lgNrjJS23r7WqyTEKdi6vECtaBQwDDDXoxXR9BxD2lcbhvT_j3NFZrpB51IKe3jDmJHzP95Gke5IM2kXwIYL5mbiWmLzZHDSHtZRDmYEcabYi4oHu-Iv1vxe9GuZPBwJoiJLlCt4AVx1vjRSb2PVJ_5T55Q06xKaL0oo-Vk2T0lOT4pczMhCTofKq4wo7KdyIT8s4KPCyYLe6Q4X0YFPg556PnBszKR-dJssLJ2F0TmtGV4usHDYZrQD5Ao6JJC96S5LQd7uVo7ANqJICIqhS9Vg8og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=PDejegVRyTgEr9UdWi6y34eoRVxmG7tMR60YpLfa7l1X7-HQNOfXahp4VjO2e16it78DQWlzPJXD4B2Vebwmh3pYyOeNH_VCckVxDkFPOz2dvA842y6gaGJY0W9eI7BFDAGMc6rlUP5GutqfVtSoXZr9MwtI6vIFkASoNNTC07xgkdMKBiMxfDruqDr7Gf9K-OGKc2AkCgt0ogYaMBFDC23U_G9jKljZw1GLa3sAl_ERWgGw2AVLfUycrzSYmuvcILQnTCnYJUAI7WeMCtnv5yGkTop-fVvYMkS70Emta8uDiMWDF69QGfg6JbAFd9Gefah-hODQUzFAsxKgVFbD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=PDejegVRyTgEr9UdWi6y34eoRVxmG7tMR60YpLfa7l1X7-HQNOfXahp4VjO2e16it78DQWlzPJXD4B2Vebwmh3pYyOeNH_VCckVxDkFPOz2dvA842y6gaGJY0W9eI7BFDAGMc6rlUP5GutqfVtSoXZr9MwtI6vIFkASoNNTC07xgkdMKBiMxfDruqDr7Gf9K-OGKc2AkCgt0ogYaMBFDC23U_G9jKljZw1GLa3sAl_ERWgGw2AVLfUycrzSYmuvcILQnTCnYJUAI7WeMCtnv5yGkTop-fVvYMkS70Emta8uDiMWDF69QGfg6JbAFd9Gefah-hODQUzFAsxKgVFbD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=WprPy4fepgIum8rZp-G474Yj8KkqJw4gkZsFg8afKXfnR3emi9LScUURkdaZHIXmrjsfSiQR2HL8N3RkCYviAeBh4YUO6MU9YdrvRIGjZbHtYWhuwBC0BCv8ZM3f2V2VxC772NRwB18O7BsbLFntQG1xExbg9K3Ib5b5bCk-2F8Atvc9jUhNxNMJubtKWeFqY_K1vLd7pElhrcuEO_4tYls3k4JWEOLD8DhIxL7Oua5QOkychjTe_6jjDPv3gmHTUaL5W3FhOJSO64oygcKfPxUYX2uEN0XXXmQYGgdigePk9GdtLB6J6o73Gn8jPOpk93bfOLvU8z_W6BeHv-8Ekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=WprPy4fepgIum8rZp-G474Yj8KkqJw4gkZsFg8afKXfnR3emi9LScUURkdaZHIXmrjsfSiQR2HL8N3RkCYviAeBh4YUO6MU9YdrvRIGjZbHtYWhuwBC0BCv8ZM3f2V2VxC772NRwB18O7BsbLFntQG1xExbg9K3Ib5b5bCk-2F8Atvc9jUhNxNMJubtKWeFqY_K1vLd7pElhrcuEO_4tYls3k4JWEOLD8DhIxL7Oua5QOkychjTe_6jjDPv3gmHTUaL5W3FhOJSO64oygcKfPxUYX2uEN0XXXmQYGgdigePk9GdtLB6J6o73Gn8jPOpk93bfOLvU8z_W6BeHv-8Ekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rsi-VPg3eRvRS3ygVhxsT6tmhwAKTH-s-8_qYrsH5JWMH52TwCIRyTJ30dwNE7GG36ls02GIUXRxMRxLeiQuNYuujdaybeRHag7is633Rt34YGjJTq2LrlRp8h4UM2USvVr71x-uL_NnIWuEkmfoeRJER_e5njoU-6AUqwZcN4RCaQ1uSnm-w0flox2c3ogxExS4PDl9K9RnYv_JVkMaaBg2JGL0zsaRm48wDsZ5a1Gkn00AIS6-LaCieFJvvpXJbO8w9QgAFwvxnVehid-c9f3ZHlPGy2bqJZxd8h92zBVKtZLLTb_K9EoM-bb32HkLfnnCnQ6yGpZOGxipN3eMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjDhH9m7BAZEEARqSRcmj8gQIxYOAMvZOUQrsgboctfahuTJTPHVA0zQwm0juO3wYljEr1j084zjeu_66mqN6ZGEP6mAZsjifICMGO32jydL1T6piLBX5CL5FjFbPzPKBkXUYCTP5vHm6APM33P7ycTqO7N4ydvOFaiWhiRvA4-A2xj5kwwVXjp8LiqHkLZ5xUo6NwafbYlCFe8M5pBc79Ki0aPmoXL1YepLHu1Pfq9_lTDICBtW_2feRcMjCG2bCyZW_pwjtjfMVACRId3blPj816NtSYUFRNBS_mYlsBornmCzDCM2suweanhIuwqA6vcKBhqiXhe9x0cFMrIlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boY0HO39qVqEoqcornmyl2CvFyHcF2Fg5Ikp-FVvkWbJ5G2Dr-phZ_PIs4gmvPu0NR_OFkp2Y-phXX98iLwOSSWivKn4I6gOyr80Bb_2j6FqmEhw6_3BCO8G193YWaCvLldNVvqB0uvlgxV8diawrKQ1wjzGRII9ap4kVI_H6SbeRcChywDPobKBlr5tyB7SpXyup62zf117nufWPHatWhSrlYRupD24m0x5q3jnrcmpLfeVA5SPfrCgSJi1nTYNWHwjW1ztcQFj4JTSU5C1x9GSIg2PqQW55jy_LCWgqgN06bvYW4uYmYvK-pzHmhsVjkttvp49laxEaY4gmB_JLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=ZqL0XLIxH0tkR7xCby1LxtHSCDfdnxQvHD85iMevMTEOAzpA6E3vpTv1PKRSt1YEYXwzUHZevhk6nE6QE0Cb5Nsrn65wbfb6t6i8GY37560G99amqt0s--7dkApm_3zHjfMpJUA4P-3J3tt9aYJAIieYO33SH2ClKspc66UetrU1XEG6j8OnUyC9sqG5JNlSS-ql8vSCRjzalOvzrAysEmawS-dMGByL7ZnLOgvDbOewtALdJ0PlBwfsbYoiGGHqAVfgroa3yqJDTaSGk4o7QaNOsEf0Ly7n3Vm_GbcW2PoagFQpwva3fV126AJBwTdgrdx2LuXtJp4F9A-2hU_AyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=ZqL0XLIxH0tkR7xCby1LxtHSCDfdnxQvHD85iMevMTEOAzpA6E3vpTv1PKRSt1YEYXwzUHZevhk6nE6QE0Cb5Nsrn65wbfb6t6i8GY37560G99amqt0s--7dkApm_3zHjfMpJUA4P-3J3tt9aYJAIieYO33SH2ClKspc66UetrU1XEG6j8OnUyC9sqG5JNlSS-ql8vSCRjzalOvzrAysEmawS-dMGByL7ZnLOgvDbOewtALdJ0PlBwfsbYoiGGHqAVfgroa3yqJDTaSGk4o7QaNOsEf0Ly7n3Vm_GbcW2PoagFQpwva3fV126AJBwTdgrdx2LuXtJp4F9A-2hU_AyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=sPhiepbbgGWuurtMh0K0rONFrcXOZxxFxTxE5S8w1aFh0_vwGjGXSL4Ia7-jEIJPCqJc5oNhkBMBu3qnEvaBxtaW2JAo75QXTWYe-cU0BG24_mRy8V_tTMvPusuy3cIxGTB7pw37N0tL-lYKkTDw-zC626pJSykgYvyufCmjDWgfkGvb-ClctxvuqAcil8_HBS_Pu7VWSOCQsoIBCK7OlQ2qzy-xlmU1ayfmFEY-kK1lxV8Drn25DngynPo6uRU2fPlSt2d3HsdQAsleMmJjFHPF2SfUvWD86kX7fLWqDYSHy0t6-yxr2vKcUvB-8aaIfPAPH4sqGy7Q1GAnlXFnng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=sPhiepbbgGWuurtMh0K0rONFrcXOZxxFxTxE5S8w1aFh0_vwGjGXSL4Ia7-jEIJPCqJc5oNhkBMBu3qnEvaBxtaW2JAo75QXTWYe-cU0BG24_mRy8V_tTMvPusuy3cIxGTB7pw37N0tL-lYKkTDw-zC626pJSykgYvyufCmjDWgfkGvb-ClctxvuqAcil8_HBS_Pu7VWSOCQsoIBCK7OlQ2qzy-xlmU1ayfmFEY-kK1lxV8Drn25DngynPo6uRU2fPlSt2d3HsdQAsleMmJjFHPF2SfUvWD86kX7fLWqDYSHy0t6-yxr2vKcUvB-8aaIfPAPH4sqGy7Q1GAnlXFnng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-mx0CBAtWu7U-iA6i2cedtYHeU96UlklwdiRr5QEkY5580s-93DUhgzzLQg30PwIArXciqhQ7UTm4fZi-YixpC2DmopfU2zzIHnHtMubMmR9wWOcwevhfdEqbWQ2N_BiXQh-0iqJ3g-iw4SwxdFE5UHroFPLt9ngotGENAxR5GaszqMCmIbdqmL__6ykrHNCkPAqKVWtyeEv_qGpYcuBil34WUbiexX1eVD10y2i30_kdyrumnaf1HHwlvNFgUOX0l8hR0UN3qyvDJwF-RD_yxuCA8AAtA4VYQPqHri-DQVhfrbUB0BOzGODSmCyuQSj2ylBDHfPqU-jMnLylZ0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=DbxUbTUIJ6kZ0Htw5E9sF3DwDc7pqL8uOT-QZkg4gfgtmULJR05brz5G0hYa7zM7TFD4cKEqYe86oSCswDKYGebZkryNdSqrLDXG3B0tINW6SYj95Eyejp7DrX44im2AM1klP_o6U6EqWPXTa_IUpHksh7yNuEuCslrOlWk0NWsoTJ5khliO-Z65_Rd3ozGiA5Gtd0dlSCuBkK_2y0GhF8dam_wgcvnGWe_IpUhl4KF6XiQFzyUDLZKlNxMljd-68QVDsoyM9bN1OOyOHgKerwvQdJU1VwCTEqWWBExelpCMn24ythnpBJM5A5iPocYuxkXO1rOteWa1kJQAaLRKcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=DbxUbTUIJ6kZ0Htw5E9sF3DwDc7pqL8uOT-QZkg4gfgtmULJR05brz5G0hYa7zM7TFD4cKEqYe86oSCswDKYGebZkryNdSqrLDXG3B0tINW6SYj95Eyejp7DrX44im2AM1klP_o6U6EqWPXTa_IUpHksh7yNuEuCslrOlWk0NWsoTJ5khliO-Z65_Rd3ozGiA5Gtd0dlSCuBkK_2y0GhF8dam_wgcvnGWe_IpUhl4KF6XiQFzyUDLZKlNxMljd-68QVDsoyM9bN1OOyOHgKerwvQdJU1VwCTEqWWBExelpCMn24ythnpBJM5A5iPocYuxkXO1rOteWa1kJQAaLRKcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXbNjvn81l29_EDj7Je3uwjRYVQys0akToNrMRMoL2T21r-Y_e-rXV5ntwjrOqn8lETrQ5RRFUXdHJ6Cn-cO2A_1Wqw_DapISACDQQS7-2BXX3oy-YHz9dxzHjO8bWljVk8e-HFd6c2c3q0U2P_SZN_HQLQ8l2hkKQZOKmPFYQMnIemNsM7zJSE2gZS4sqJrZqQbN7wkAsnKkrUCCbgIRtNwQdTN4ScKGHUSgeK1y_6iemBva2QYZ2s2jt-xHSZ4QvU-FpGaP6tBFw3KFlOBU_bTmAwx4VF6I6xAFMRzQ7lw8sHk5RApjljFAVSdwiVxmyfbQK-R3BHIsBnUWzsFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOlN254S9fV3j5q768P2GDNz4QutnYpkXnQEM8trZXvZzaHzYhCdKcdspRKWzQ-mdRLJI1uEIJHDGOReWKvfTEbsEV-eBjGcjHHuGsxMurap2_V4oSmHdCnAo7LjQjuagiQJm8_8lmcC3aQeazj_xgYCdtNEGedsiIyjt8o0o67sDeMG7pDq-lLoKgD7ZK_KxOgTiJc_pvTglTvFnCKSOrwOWQ0jZmlUUARDL3pqDFdfE8ji6e2Nw5yUxmzH1KBPJHHsUJfvnwIBzpRCa-2CrAsx_VcprTUg_4yrzzfQ-w8WX-6auPpycJghYVPhC80c15Tzov-wdqKITPrJzO9ltQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A05l1KpAyAoBOyGuzUQH-tG9hnY_QBDJv81yBgTspr6zlnZ8wgIXFfTwhyR0qE0WWpYhCLLI5UoYbZxsetIGM7a1dxuF9QIqpOhJbf9mT1B_mxgT97UZwHgGD6_KuRO1uKRMDGsniRTtdqQ3jumrgIu6P0qCikz0dIbFAuKJv5rQr6tPuhGZ9Ld8nGv2o6x69RG3uWpVdwaCnhG-_hIwWgZONVqnOEp_e8exQCPu_or4Pyr-7djKlJhboSMY23lxwJTUJyfSsq4cuIs-viivR-0CE5fg9AEQEyqiNAnGd31yipEULCa9DbqVjvRmQKuml_vbm5JaM3tM5HvId2rABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWHH8ggHV8R8761ZDuFiQ6xQG49Y6CFwWh91gNgXMh1a_uzws0Dl1I8I9nGc2TVIkE-Rh0xpkhvCK9wRFy8OBMA6fuA4QzsSdNOL_ks9ss15uNP_TgU0qkShYaNGciTXNRI3eh04vVsARY_aygqBxieEtNMmQMNpqOGJv3eMKIPIgYyed4XbpY7mQv6ChGg17zm3NhwtLWxQYFaGrtHirhFyGn4L6H7bQBsrMlL_ZHr93VNhrAsWdfRI-hFJgL-PnBavSZ5DX_0-3OWAdEKdxG2XHdPYAqavjyssObjcwdBhsl1KnAduN8Ua-mJ8ibo569hkM_-MlOjXPAkYRM1Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=haU7b9JmVmfhnKTmteWXl6pkz_lY-H4kUzJLs2k7t6nrkrcaqJ1wwikpA_0ke5Jv4T9RlgmJEGe4dGoVQceTRPpiC7Ix5zk-jiQtBmklZLiUhKJ8BaqiEIcP9BHyp_oSFk3jGv14KRQCtLSw-GlvokMDvuk1gpu430cIKmW2HC9cYax4xoOtlyHx8m9dRlG5qFdsVKksCjoVKIJTQR8B1gR7tR6adhwJPPSh04ktnWd_M8pwgX5PK0eZpK4Cj_XZet6Yi_jQ_hPcz2SdH4UpPSP60wgCWKkxve6c3fWK9D-NWoDzBIyT7jhU4p6WMJj5AFmiXANaz2oSxGhwy73Spw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=haU7b9JmVmfhnKTmteWXl6pkz_lY-H4kUzJLs2k7t6nrkrcaqJ1wwikpA_0ke5Jv4T9RlgmJEGe4dGoVQceTRPpiC7Ix5zk-jiQtBmklZLiUhKJ8BaqiEIcP9BHyp_oSFk3jGv14KRQCtLSw-GlvokMDvuk1gpu430cIKmW2HC9cYax4xoOtlyHx8m9dRlG5qFdsVKksCjoVKIJTQR8B1gR7tR6adhwJPPSh04ktnWd_M8pwgX5PK0eZpK4Cj_XZet6Yi_jQ_hPcz2SdH4UpPSP60wgCWKkxve6c3fWK9D-NWoDzBIyT7jhU4p6WMJj5AFmiXANaz2oSxGhwy73Spw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=bzhU74QNhi8YLvHTnRLP23HsLZBRIiv88TjNUha4pKbBVWO4_tZXDhE_lM5Zbtb9nskbyKiM3bOmGprgRhwkj4IDygV7NbctuLF2K8_-RnX1AxCY6F_VJ4iyP5QBswEnJymyTEFKFqvWeXXmTZ4aM0wn4ImQJqZNlrsblvP56QbtBHMAd7AKnbgSako3XQ5hVvOo7PlhmDek3HJ0bo_IRX_tKr8fU9kuxOR4Z1wS0S4SowpDqdW0Glhc7UTxuN3NllFjJahx_ZlC6TJm_znYSkDr4LSW8kP_rPx0e2pz5WJbl_ANi0MqBcSCYO1j2q6mJYrNrZ2E8Feof7qRqdwjHhUzwKbCbR0Q6oi8ZoAkrdhpLUIM7KbyvudMYlM5XGS9i-St36DXKCAjlp1PPMrU5cI9xbxTgyygz74EkOtBV-D7sCr8M9MQd68PU1foiRsgiSGATzD-YsmngIjBWZ7oOEP_nMLtbp56IxJvd9IyvskvFOrBXEMGHiyx7Ov93WH5DTzhtV8y0DU7H-ZVyr2tq7EbTjtPJBDsOvdh_06VyzROcByKeNwOrdk7POrsEZrMHnOBUWPHb5_q-9nbJ7wEzgU11WsOKjprpxC76whQWlTJHR7u9iN136-QBlkxn9kXbU55swt_DJYqfzkaD1gR321mZVwCH60JBozxJDGRgt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=bzhU74QNhi8YLvHTnRLP23HsLZBRIiv88TjNUha4pKbBVWO4_tZXDhE_lM5Zbtb9nskbyKiM3bOmGprgRhwkj4IDygV7NbctuLF2K8_-RnX1AxCY6F_VJ4iyP5QBswEnJymyTEFKFqvWeXXmTZ4aM0wn4ImQJqZNlrsblvP56QbtBHMAd7AKnbgSako3XQ5hVvOo7PlhmDek3HJ0bo_IRX_tKr8fU9kuxOR4Z1wS0S4SowpDqdW0Glhc7UTxuN3NllFjJahx_ZlC6TJm_znYSkDr4LSW8kP_rPx0e2pz5WJbl_ANi0MqBcSCYO1j2q6mJYrNrZ2E8Feof7qRqdwjHhUzwKbCbR0Q6oi8ZoAkrdhpLUIM7KbyvudMYlM5XGS9i-St36DXKCAjlp1PPMrU5cI9xbxTgyygz74EkOtBV-D7sCr8M9MQd68PU1foiRsgiSGATzD-YsmngIjBWZ7oOEP_nMLtbp56IxJvd9IyvskvFOrBXEMGHiyx7Ov93WH5DTzhtV8y0DU7H-ZVyr2tq7EbTjtPJBDsOvdh_06VyzROcByKeNwOrdk7POrsEZrMHnOBUWPHb5_q-9nbJ7wEzgU11WsOKjprpxC76whQWlTJHR7u9iN136-QBlkxn9kXbU55swt_DJYqfzkaD1gR321mZVwCH60JBozxJDGRgt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=fokxvMU7ha1_m5eCLGZh7kvzNQQ7OV-mB6ihv1yCXjAJ_wkhXXAkydY9WhP5qMT82tWEK4SR4Czty0IvNFpoE6WdRCqNotV-9r7tydnJFoz8_zMIn182zTDJN_CE5Z8a1A0Ik8CvRdQdJ8VP2GbTLQVcBc84bVWubzgfS2qAzma6W5HlnfLcefx5p6pRbKa1xOqvAGPNjX6gQuJn0cfY33ea9WHQN-WWfqAJRPuEdsTsVk4fK91xTDIR_JIuc6XFCjVH1_kg3PFBh1VZlQ2raWFKUq5aHwtnF52ziYFZpExTNBIs2hGWVw1ShURYzHY15KxCjCmj74tgF_3PGHRUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=fokxvMU7ha1_m5eCLGZh7kvzNQQ7OV-mB6ihv1yCXjAJ_wkhXXAkydY9WhP5qMT82tWEK4SR4Czty0IvNFpoE6WdRCqNotV-9r7tydnJFoz8_zMIn182zTDJN_CE5Z8a1A0Ik8CvRdQdJ8VP2GbTLQVcBc84bVWubzgfS2qAzma6W5HlnfLcefx5p6pRbKa1xOqvAGPNjX6gQuJn0cfY33ea9WHQN-WWfqAJRPuEdsTsVk4fK91xTDIR_JIuc6XFCjVH1_kg3PFBh1VZlQ2raWFKUq5aHwtnF52ziYFZpExTNBIs2hGWVw1ShURYzHY15KxCjCmj74tgF_3PGHRUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=qIEYNjkYfHh_WonMIej0kSZ4i02tmzHkyalQL0L0qFYmvrAWkjNt2kZJ9620eKzCbD0srGfkO7082ENn04hKjnuJne91kCY5OjWArrPLZsSSUvEQ8csuIC1W_jaPmfgEcICuQYIo31ptwVU-AGJxcFeoC2b5NMQHdKwO40fXWAADmUIqHo2UCSY5nOI9JyZ78jXS0p622ONViEnJITbJI9_1nLe-NEt30qdFN6whzhvmPBccHKgSiHQZcbGVoRLtMY7FBbZ6M8kKYlMKHRtU-qfAiLCkA7i4sEF7ZyO9UZOJJN4tKgXNx-gt9zCaFpITGP62g7uTQGw414y6ndk0DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=qIEYNjkYfHh_WonMIej0kSZ4i02tmzHkyalQL0L0qFYmvrAWkjNt2kZJ9620eKzCbD0srGfkO7082ENn04hKjnuJne91kCY5OjWArrPLZsSSUvEQ8csuIC1W_jaPmfgEcICuQYIo31ptwVU-AGJxcFeoC2b5NMQHdKwO40fXWAADmUIqHo2UCSY5nOI9JyZ78jXS0p622ONViEnJITbJI9_1nLe-NEt30qdFN6whzhvmPBccHKgSiHQZcbGVoRLtMY7FBbZ6M8kKYlMKHRtU-qfAiLCkA7i4sEF7ZyO9UZOJJN4tKgXNx-gt9zCaFpITGP62g7uTQGw414y6ndk0DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYYc2dOZZbnHK3VqtZEb3FBYdpV3D7ZsJkqv1nkBpKHJSaJCN0cHdC85-_2fr3wc1zs_LPJKnX-7qgd72L5iJ9JBLm2FgUHOX1JM7KNfYoBh5ZgtOLwaRZB7_-5TMCLYqrElCQ5OgofKq-jOSaadhok-ZHJp0xK80BsNeOxZN81LmEaBz4Q2x7uMSG_s7t88kyQt2IbH1PTT5A45w7PPxXZPhThvz78RDiSZ8IBnqy4GqI0GetWoOiyEQ5C3XozGK_AI8S7GcCHNYMh5u24REQs37SgBYv74Q5hjI-slJxu5zTmDLTfalDZbjRydKH7JvyKAeE9CKedIBRRYOLy31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tySx41pnTP-WoilXLeFlBiDrhx74pyMJnJMBLaSyzzzFwB3RCK9oSNMeAZJfQ8WmKh50eqopBYtkD4r5r33ZgdhoEWvr6AndpSsIMIRGPWCCU9rbfnHdtF0Zu7Jue-szWWH22I1D9Cpl-suqdcMtb2yiDMQV18RgDMDHcazfillYvsHa9Zg9CYk31hYHT98pnyL_hIEOoJdMSeXGs72vq5je4XHmSo_oFm9hsLxP3RMllFXgDUgkhI0mk5lkC9Koflt8bz0_Z0jZUiorvGwQUokZUYmr_VCDQEv4poD3QrD4NaGQFHGfjqMTJuFELLJ9Lpt_xitHduA7YUGRkaX_5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwu9oYunAW6BDdth_JIGlzWqZVHnHP5pS7NOIKS01eT-Gw59ACLeMaEhUbjsSH3GDMcSEoqCAb5bhlQGhk6kThzk7AVgvJ5RGaQS3-j_BYLLct1NsM_whVXTzvVj9nDMgwhjXDPyo3YiaVaZxix1qQOfele6O5lIDmPOesrQlbR4b_aycl3YQtpdMCuB2d6TCA7m1NZT5jqLux3ZCfagZ3LK6xxqWeYQlR2NyBlM3TJXqnumeUsHt-E0sI37XzTGLQnhD0N36W9QqE7AZ8xqHgWsnQ_zWgPXrvlPje9invgVPCk8fePLVojNIoKxv93V6HiOi1cKbsvxlvCKC8v9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbYp0uhK2hu7YNZITueHcfGcr5bO7Agmf1kdUqfO8x0Na6Un8wNaHoL2--c5Njd-y64MLVpiOK0w0BfUX72tZJBqKUUIV97UuqFL62pnZSL4ps1yq99_BHkCignVkAf3ulTnOWpvPNe4p6UQ_mqvNZtoqmKPh1EpuDWIeUhzh_YXNbvjFymYnpJmHB_0IrTG4V4j5YkxDFIcfGSDyhqP8rGV2grJz7vstPa40H1N3F6IAUBc-lr6uOMaNKJfWk9kyXrUwD3pO0FxhYT-k1l9mTgr24uRAde3Zfu-r2wN6DpEsW15NxTh8b3fuvPJyQ9JHGE4JGPPKHqHJvrY8tQGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdy-M7HxEmc0oiHym8j-aE62mlw7NRWtDk9RlDTLXV3blQJHNVuVtFlEcht5-8gg5QVK4W1mCqRHWJ5v1C4M2X0bgbg5DShfI2YV_PVeCKsrUCgF87TKJzDeau858nWlroikRDteB5xnWzoCc91A_GFHmsmy9EAfDohYkOeqi5U7TtbrpMt2y8qJFzXzvlq_J5zbUFzuCtwF3ekNysZ4BTJCtNiMtDA2NqbiWYZhHH4QVoq4d71EdF6Q9qqFIbSdThATG9jImddg-ZMKbWi3EGiRTwjwld0AOGtfEYEHUkdZKHfX8wbqbbKkkZlPxi5WWQk0d0iA3O0j1HlL4Sa_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lL5eK3E1e1hls0qCL4Eqp8Qxi52pSS-mM9-78Q4ejQ1DSfjG_nzzJ_gChnd4lxl4Vp7kHyjnu-LEwLOixpGDnd0J7azsH9eBUWyKcUk-TR9Ps2wf2QVmjyZ7xOaJ0lz0SK7rYi3MvpkIUzcLUOnBOcZdrICecctaJtLWChbTcaHYTCZ6qUvWuoNHUhHKvFMr4wtlugvVfecot3g4ln2Vp4EcijYmDgHTiQW8eqNUWI_yIli3KSjCQhJH55jaRr86OCJw11LIKN8wNLNA4cUEhWwgfSZobDfyONeW8TE94UHhJOzXlC1nQqa6PwdWQvOkr4n4p7eXdEsoCugnLWXKSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfjxkwB9Xyo8Lf__cuFD0fJrb_-0qCbKULT-0wzfkDNw7MFJxEzOMC3lCibD15dtd_DdIq5RjpfoaX2wcp1soLr-NbCMezCupCpSBHwrlaXPWoLnKZ9JzaAxPT4EZ8nXFA6WhXisI33RqSMhtBZq8JpCwYgnnHvXj0SONq0bquesZ1Hx8T7emBR3iThyvBGFDRvXCd0tcBomkbeCxkOUKWOjHi4-tMm_jiJ9_T4dddxqgV2EAB92KAsyJqF5KBfBLJr09qVM9mpkNtXLUnUAznapWRENSKERr89Eu74kNKKUxfoJcZCF_Wmxlze0WAFh17AZmpzLudF0oO_iF92piA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olHekUVa8mE5dHvb1w18APPBgHeY-LT2A31jFmLkvNx70b3qBNhMHSpk6mwq_wUjjlIdVi6Z5LMF1MQUpIEBrG9DDfd7_PPRur-7dHjh2cW25oxrIWnR3yJQgOutPYNPbiqftUe8WU7Ugu-pueT5RycLEPF3BIhPjdq8jlCdzli0kTqMS7jmb-RPebTFc_J5sCTHANQAPp4nqKjvOfHbkcJcvQQB7goW6AS4-BQRaOOXloZBWSumszpdR143BZDL_gZqZH5azJmQA3LkJifgk5x5Ry8gnQXPz1YFSYwoer_QPqLZYk5CyVqyTs3S513RnyrsDEtpa6113VUCathg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=IqZg886TnyjCVw2uIxDB1S_GemZRNdT4N_MDM94W7LancNTBoHl7X27sBSqoP6v0fY8mHm7IY8vAut-_nahFNA061tR6i4WgFagzSsaODaXG609n-bnZfN0q3bfeRyyL9gfKuQbY0HH2b8uCTI-Qqu3Zo_tyZXC8-4krt-hQGUSGmfwcgBUACwN33tyQtt1eH8IotPNt36U93Y1UcsVZYog-2txz3va0N6Hlye2qJ2AX0KiWmSOlISZUA5l8uTySq1CI9LK4QTV0XQ856kCsrVSd-QRKVz_8759A8KLk47GSP-9bMZMEdpjDDqO1YLA2trbAfUN9rLW2erMpaIGJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=IqZg886TnyjCVw2uIxDB1S_GemZRNdT4N_MDM94W7LancNTBoHl7X27sBSqoP6v0fY8mHm7IY8vAut-_nahFNA061tR6i4WgFagzSsaODaXG609n-bnZfN0q3bfeRyyL9gfKuQbY0HH2b8uCTI-Qqu3Zo_tyZXC8-4krt-hQGUSGmfwcgBUACwN33tyQtt1eH8IotPNt36U93Y1UcsVZYog-2txz3va0N6Hlye2qJ2AX0KiWmSOlISZUA5l8uTySq1CI9LK4QTV0XQ856kCsrVSd-QRKVz_8759A8KLk47GSP-9bMZMEdpjDDqO1YLA2trbAfUN9rLW2erMpaIGJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=Fxua6Jz5o2f97g3Ddz5GCveX0OfcgQ7V6oYq7hPCpIY2Ifkumy_ojI7GQTfxf8rRTSHnQI_x3qQ4q4kIeMIsDHvuYhaSSfiK23E8wb-ieJMJ8bc5fWJSngrLdp5WCCHmSOK5hCHZ7Ybi3XjCt3M9XJaqe1_0gCQ37Pv4bpg2lMQwFvBUMh9PJbX7u0aIuhGC_hs97S7wGrlkX2ydit5TgG278O4LCVY5otQ9iFxeJi2FxQvyuOZ0d049p_XrR1OiWhIkWI8dSYTdJBgRKdxIpa9FlCAVuxyf3FxNrwEC3QjVW6HrAdRvyNog9d5gXEosdkHRGtOVU8MkhIxV4yHJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=Fxua6Jz5o2f97g3Ddz5GCveX0OfcgQ7V6oYq7hPCpIY2Ifkumy_ojI7GQTfxf8rRTSHnQI_x3qQ4q4kIeMIsDHvuYhaSSfiK23E8wb-ieJMJ8bc5fWJSngrLdp5WCCHmSOK5hCHZ7Ybi3XjCt3M9XJaqe1_0gCQ37Pv4bpg2lMQwFvBUMh9PJbX7u0aIuhGC_hs97S7wGrlkX2ydit5TgG278O4LCVY5otQ9iFxeJi2FxQvyuOZ0d049p_XrR1OiWhIkWI8dSYTdJBgRKdxIpa9FlCAVuxyf3FxNrwEC3QjVW6HrAdRvyNog9d5gXEosdkHRGtOVU8MkhIxV4yHJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhJa0-ipJs-X_jJPxj0j0qYGoJyXylt-Y2glK2wS1aQb2JvQTeFE5IOVXZYPorm3apqn5dRTq8RbN_AFgJBTSjU_t9DqHfdldWuVENsuoo0rZsjj22YFIZWFsrWrM4bwNIjBQ3CZEmk_b2jWZwZjNLPfhT6-E_gt5PSdAwtye-e2JbBvwC9K8JfyKexSDH2UAQlSsS6WueElIEtJ112PQkPFnDkBjuwvFc4k9Q3utDEbMnu7FmX9gq3M9s5gWAUCCm5rv5ZTDnGGTW7Vq8pn8J60BzS9rUQgGjnDfwhoZfa8ymjuGBmBJ8Tk-tmaOCzh8VDlAjVbOBH-iESkFlglXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=JKTCPb-b3CivncH3Oa696qsBul4-RtZJ5nn0HeWrDKO56j68_h8QNWXaoX8yrhl1u4qUCwSOruewKrsdH7-tQJG12j2QKI_HBIyUHXRRy02P39uEOfbuFvRXCpRfAjIumG5YoOUOFP2b381JtMXeZ9PBuXQM_gEK37TM9l4hY_R0JQjntPXNTBkZi59eVzr-mW3Md0Vf5jVSAwiUXP5t742h5EEOqgPudJI93qU3LcAAMGDV5eopxeffNTBHeOW6-pv9BS3aH94E5yt0g-YV3DLDEqNkrtSkp5dzFdEms-ZjLvfLF4RXlrcpRHejiEGU8NilgJ3aemSdLKiP3S5Oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=JKTCPb-b3CivncH3Oa696qsBul4-RtZJ5nn0HeWrDKO56j68_h8QNWXaoX8yrhl1u4qUCwSOruewKrsdH7-tQJG12j2QKI_HBIyUHXRRy02P39uEOfbuFvRXCpRfAjIumG5YoOUOFP2b381JtMXeZ9PBuXQM_gEK37TM9l4hY_R0JQjntPXNTBkZi59eVzr-mW3Md0Vf5jVSAwiUXP5t742h5EEOqgPudJI93qU3LcAAMGDV5eopxeffNTBHeOW6-pv9BS3aH94E5yt0g-YV3DLDEqNkrtSkp5dzFdEms-ZjLvfLF4RXlrcpRHejiEGU8NilgJ3aemSdLKiP3S5Oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=a0bVMRrmAzKLki0nRIeKZ6F76SijdzjFy9pGN_63qCvfboifk7wceKNkn809t9bSIrpTBzrH9z4xyNo1XCZkHR2OwjfSPNHYxTVA1m42Sn1OQJZ8dtxFTpJwDgdichWlI6IwjJGe8iQrjShdPteW5tRxuNjMHTbfF9-ekSHQcrqEOdskzgKpF6ThFI4FHWkYDaQ2fNVEGBqUxYqgXQiwwEOvikP8ZnbRLfLEw-_3N2rIAs_c9K-CyhKf9XDyJQtmEIFZvwuunO4eL-K4y_fX8o1yhWMkidFtIBLY7TVJoNyXrNSnIhOosgpqN4QMgc2SfLJW_vknGhQ06thqvp-2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=a0bVMRrmAzKLki0nRIeKZ6F76SijdzjFy9pGN_63qCvfboifk7wceKNkn809t9bSIrpTBzrH9z4xyNo1XCZkHR2OwjfSPNHYxTVA1m42Sn1OQJZ8dtxFTpJwDgdichWlI6IwjJGe8iQrjShdPteW5tRxuNjMHTbfF9-ekSHQcrqEOdskzgKpF6ThFI4FHWkYDaQ2fNVEGBqUxYqgXQiwwEOvikP8ZnbRLfLEw-_3N2rIAs_c9K-CyhKf9XDyJQtmEIFZvwuunO4eL-K4y_fX8o1yhWMkidFtIBLY7TVJoNyXrNSnIhOosgpqN4QMgc2SfLJW_vknGhQ06thqvp-2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFugYpmakUmur-ggiNB2g6t7MoTCnEmoPyZtIHooZv9bXk1Vj7yRxQ-wDtrDURT4h6QbaUqO4yf8MdZCHg5DF4RXGaP8kuVXtFCuuLkAuxdidq9YiiyK1YeJVmLZjfe0sAKc_lTawQaqYE-a_aLHjmpi6TCk318aammGfOR718dLVMkN1c-zBUzsxCwrvB8kKeSCHuCDlHYm1fKcL0ctklrpRm3vEEfCDt52uP536ylz720jmsChBiZWa_YtMLZI22flNuUdWmIqTtM_2FUxJYdboRCO1-7ZDCj4aFtmka2S1V89ik62sullHJfCI7vk3BwT_Lgs2gMHDpqrm-EvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVHnt7mmBh9RtaAlnErO142feiRzTSeq__ByoT9z4D16nD-xk_0B32d_Vv2lE8w5JSAM3zkB8nY4ahP1-gX-abneBVOchqYyYQTSoATBdoVgXJeMbhipUwyF30cczO_b3heLM7_ALQiq4_yMePTCTWAX8q5oHjqp9VGBTmO1kPG2JlbI4u8mlEx5OT6B3ECuVghSbscDvFUCaxD-OyNiFPDpxaACNCTG-ykXnSczys-_H87QfYe3w2P_SpXDL5NXfmz-CWKEDanaPLr_YIv6a0OrKP2cWVGh06hZ_PUO7DZrVRYw1SDxGPWGq1e_N-N6-3uvjm-APl9cHK3dvCnAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2m5-0XyJ8qESyWFskjloYBMTKWG6qQnvw86kAtEUuf0guwxwOeSrYdGUy2_jsrvsj0nWxejdIaNiKcV5Wf-i0L1812rOXQT7cu7ulPCCaXfpIHRpukUTy8zGDH-2ZaoKLMrdAbJYcqqKildSWtFhMIugHWeCr6WoFbQDwJyaM1o1U4_e_J6Kkmzna1Z8wvUnoDosKiKquBWMqezkM3eWE1meE4txdnChbP7D0xRe-PnKRXDzFSPQ9l_PEHYHu5RY6qCnF8vGIPfYQLAAr-N4aR9auSKw428AtjfB3w5N-Tk_CCBei6AX7pu-qyN81kNTOPTL2WPOuwX14sUc95K4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=A0Z866D-DkiByUO6XEH_GITcvqS_qHi3mrjADdAE9NvxIzi38uNlC7ncQDiAAsrBciRhj1TcOGpcuVMp3R8kjvlGKEYYJvdlV7of6xjpTl_BQDK8SLI2SBRoQr0SuallGc4SMAIoos1rUWN6q7jpzmvWlDusjexpvCx27aVGqCEzB1JisFmbXIqNLeOtBCAlJJtf1cmK5B01G3WRjveccSA0b-_JlSpV233ycTQCkuaebZ-CPtFf5q1OOijaZhb1xAHigojZOdXCxoeqilNrAOqStQpwPVr1M_TmFQJigusAkZgVbeqs3esH_LioVBO1YpXO1XAN-JBnKeOUArZnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=A0Z866D-DkiByUO6XEH_GITcvqS_qHi3mrjADdAE9NvxIzi38uNlC7ncQDiAAsrBciRhj1TcOGpcuVMp3R8kjvlGKEYYJvdlV7of6xjpTl_BQDK8SLI2SBRoQr0SuallGc4SMAIoos1rUWN6q7jpzmvWlDusjexpvCx27aVGqCEzB1JisFmbXIqNLeOtBCAlJJtf1cmK5B01G3WRjveccSA0b-_JlSpV233ycTQCkuaebZ-CPtFf5q1OOijaZhb1xAHigojZOdXCxoeqilNrAOqStQpwPVr1M_TmFQJigusAkZgVbeqs3esH_LioVBO1YpXO1XAN-JBnKeOUArZnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nY4QDwD9OHPJGKP3WtMsTy7VEUg9InuWnrV7bVCOt6DBP5djYYvKPzivR4nqOzsyj7X4dqLWbLrDb2beIS34fYAnkBQvxEeRirfFpWHUM_gJbq7GHj-qc--RogqcqGWBb4sqGmX4LD9irh9pXkkA0QEPbiPHgpmH3P7Sw2znfSYex87eMYPbBXFTjTueS6pct6VdSfMFCqhhFYun1y7qOcKA3Y0Aw3URnhu_kL69xj4sjXRnj-QYdPahuE4MQEZk6F-owMvT8TIgkGQlbGgGTXwm57SD4UxW9eP63sGEOf39v0udRJnsNQKUsHVaSIeE6A8KWT726YaVe_9ckR5pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VntZbANI9BnP_PlUKVJKcjgAxU9RgjTngbnyKNQMlbwI8nbqBHzI1w7sHzKocmAE05ZdYX0NPaFM9lwWJsW82eNRHwQpGmKGmR5xv-Foh7LaHy7j1emd4eaa2WE-ecWNXc8TrE46ghebKsWbz7mDAXgXkertw4_51MJw9OfnChNEP5OIEg2AIIqLWNOFhWY0GHmRCotTs2KmZ5OsUfUdOXisXB9Wl3EmwmkSeHE16P5LYn3o7n60X7vbLh1ruC5Ya5O67wlxRRjJTkm5zc6cGAbKnc6IChCYJkfCe25yizephh3i4NiGhVoNjN_eobCXSlGkuww7XaSRBPNWOjkhwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0PDWsezw5IELv8B_58oCYyNa5-Nv0jy11yYKoMLuGMWrIb8UsABjkRF2Kzuwm6bN_rQhAu9Z554pgkCWmEw8pPIyEcljzQmiSUiILMS15iLcIs3G4s96MND6YxDkxkbHZSixUggIb_5y5_IvjsY2-bQpqtvuF3Bk7Um0TZTF4_w1UP_OJyQ_s8Cjz5EsMetnQzgyiIBy0Obe6vzMpRsRlvVTGt-tP8roMvXVIs-I8FEuM4UDxXNFk26AQy9uTVXucw5FFwh-gRw6SUzgf814GJYWUFPOPBI9O9Wj0llHWPTltE2QMkyt13yimHh-U4-TVeUyqQHQfKks3hopBzAEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=JyR-4x8nhwlFGrYfRIjjS6oMX70MMjKPcJ84rZVvlP04AbtyNQOEF_HO4JVZ5prorqtKTDRt6c1HChU-EI6A18HwxLSXxJSXbAQwyjpNWUVOR6WyjkPVDdJpX3UVTcW2XcvscJAs8l0AOrnPxzqrDkePzX6XF5R-M_QfeMnMQCpqmosAknIAmi29-TTXka3YMsC44mU_xz7AMsLNcOLI-g467cWt6u-ktgb9Br0QQb8JYRTP5AXsowTilBGiq1bck6K5CCV90QCgPMTke_-skDiE9HbRHAJN-qkrjBlF-bDlcg2CY8joObINJ0-VKcqV8XjjolUP6LWasp2ip1QY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=JyR-4x8nhwlFGrYfRIjjS6oMX70MMjKPcJ84rZVvlP04AbtyNQOEF_HO4JVZ5prorqtKTDRt6c1HChU-EI6A18HwxLSXxJSXbAQwyjpNWUVOR6WyjkPVDdJpX3UVTcW2XcvscJAs8l0AOrnPxzqrDkePzX6XF5R-M_QfeMnMQCpqmosAknIAmi29-TTXka3YMsC44mU_xz7AMsLNcOLI-g467cWt6u-ktgb9Br0QQb8JYRTP5AXsowTilBGiq1bck6K5CCV90QCgPMTke_-skDiE9HbRHAJN-qkrjBlF-bDlcg2CY8joObINJ0-VKcqV8XjjolUP6LWasp2ip1QY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=WNmQQqJbMa2O4StbsWtMytotrSBK7VtbH9l1IrOM0Ck3oxdcgQVncaf8FbjZjSAukKP_WFFpu2DdcPTxXe3VKm4UoqtOAq_r29jyPgOn033p_QloB1MkBj-WW5Nx_rI0iMpx7o9udJoYQIYrt7LKZ6ARnOjSAyeMptJjb4c_6s9Vjqyv9Sqjzw4wykkrSNouwECY89NiFgAqjoILCOzlegDCnB1LoGqRne2oV8DGoUl3vn0QWJRGZD4uaTm671BUzAwhOIpHAftoOnH5YcdXPWE-wovjqo33KOeM_jz3kStti_eDSg-L25mgOFTEQb5D8cmDp5IyIZpkq4lnyRmDnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=WNmQQqJbMa2O4StbsWtMytotrSBK7VtbH9l1IrOM0Ck3oxdcgQVncaf8FbjZjSAukKP_WFFpu2DdcPTxXe3VKm4UoqtOAq_r29jyPgOn033p_QloB1MkBj-WW5Nx_rI0iMpx7o9udJoYQIYrt7LKZ6ARnOjSAyeMptJjb4c_6s9Vjqyv9Sqjzw4wykkrSNouwECY89NiFgAqjoILCOzlegDCnB1LoGqRne2oV8DGoUl3vn0QWJRGZD4uaTm671BUzAwhOIpHAftoOnH5YcdXPWE-wovjqo33KOeM_jz3kStti_eDSg-L25mgOFTEQb5D8cmDp5IyIZpkq4lnyRmDnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=jKNZs_CkG-q8cyqS4dUTNLLS9F1oFHKvLZM-7TOsxjBrLSuELTXRrhr1nGK57Z0oyOIZWAGdBwgT-AMsYmC_TrUxeQAayFqAjMxV8LE9ZNAWuDcuhQSprx0kyRwp4miIhPwfj0BmYWsnpw6jXVgihGDWMF2kcGr_2_a9gYAw5FqmY0x5uVrAzAUMHd0dShisug5A235jlx8PQNgrMbWqUNmVCVPaI3p9GXdp4e65kVpJmN7Ee39bTCzsLK6CPuAceeL8Y7MzasLqujdJYiGKEdgPzKb3y4tECMgcuZZIw6_voWIyhF00TDQ_vSSjTEsAykO2-EDZ4Z1h1KkKOIcbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=jKNZs_CkG-q8cyqS4dUTNLLS9F1oFHKvLZM-7TOsxjBrLSuELTXRrhr1nGK57Z0oyOIZWAGdBwgT-AMsYmC_TrUxeQAayFqAjMxV8LE9ZNAWuDcuhQSprx0kyRwp4miIhPwfj0BmYWsnpw6jXVgihGDWMF2kcGr_2_a9gYAw5FqmY0x5uVrAzAUMHd0dShisug5A235jlx8PQNgrMbWqUNmVCVPaI3p9GXdp4e65kVpJmN7Ee39bTCzsLK6CPuAceeL8Y7MzasLqujdJYiGKEdgPzKb3y4tECMgcuZZIw6_voWIyhF00TDQ_vSSjTEsAykO2-EDZ4Z1h1KkKOIcbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=X3oYMCtEste_w_APRqqRJVgaKhCgG3Y2ZfP6SJDxZb-M83p54x4MA2VSNufNsU_tvtYBtA7oPEnC-u9jwJnh-j4WXVIDYB28LQjkI6vyHlRhgYZ2gpkjg9-oW9FZmUq79lM9kuVGmQ7ZpWASV4tZvCY-5I3iigKRa8noDxRYxF2DDO0dzSabrYpnmS-n8HP950A5XhbUB7Gn_evW9rUO2VhL8auHydoJSf8tuXgkuDgggG0l2WNBr4_qj-eZBA_NbnY9zdBJGsMpy9GYFLrlG2ulcOQ6aEO6bg0dyk7PrZxrYX4HJMiX-1wVREAElegw4PG5szAKYr33AvFcIXGMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=X3oYMCtEste_w_APRqqRJVgaKhCgG3Y2ZfP6SJDxZb-M83p54x4MA2VSNufNsU_tvtYBtA7oPEnC-u9jwJnh-j4WXVIDYB28LQjkI6vyHlRhgYZ2gpkjg9-oW9FZmUq79lM9kuVGmQ7ZpWASV4tZvCY-5I3iigKRa8noDxRYxF2DDO0dzSabrYpnmS-n8HP950A5XhbUB7Gn_evW9rUO2VhL8auHydoJSf8tuXgkuDgggG0l2WNBr4_qj-eZBA_NbnY9zdBJGsMpy9GYFLrlG2ulcOQ6aEO6bg0dyk7PrZxrYX4HJMiX-1wVREAElegw4PG5szAKYr33AvFcIXGMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=EVWPVB5omMvIBqZmT0FQKEqjoO4t9D4KYI6SXKcCbaUcJJAtH-4qT0puYyx5DQUgRNsFQKr7ejxILOV8ye76zVeWzF0fdsjRnATqdnDzmphKnUo5Wy5w56siyEqeUEmxlwrlGa6r1Fg3shlzmfJdXG7rKjRbkrmZMhf7cC9ECdniLoH9CcNNaXh2mYWjZQnPlQhaJ0KLHVHv-XOKVSBQ3Rk2Haj9HSEqft0M-a1WZ3CgYw-3-eC1OrvTxoZ8pY5EQkROOZsowCc-zZcIZmpZugVwxDHR1PTt2D3Q4xJzf8t7iGBx2suB4Bn2Yh3RqJmdIsuVAbHaaOSLWVCyPdZ9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=EVWPVB5omMvIBqZmT0FQKEqjoO4t9D4KYI6SXKcCbaUcJJAtH-4qT0puYyx5DQUgRNsFQKr7ejxILOV8ye76zVeWzF0fdsjRnATqdnDzmphKnUo5Wy5w56siyEqeUEmxlwrlGa6r1Fg3shlzmfJdXG7rKjRbkrmZMhf7cC9ECdniLoH9CcNNaXh2mYWjZQnPlQhaJ0KLHVHv-XOKVSBQ3Rk2Haj9HSEqft0M-a1WZ3CgYw-3-eC1OrvTxoZ8pY5EQkROOZsowCc-zZcIZmpZugVwxDHR1PTt2D3Q4xJzf8t7iGBx2suB4Bn2Yh3RqJmdIsuVAbHaaOSLWVCyPdZ9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUX_MqU0ycjdDi5UDVLry_KNqa_ovRCYPy9JA4Jh5PH2S0-sHB6Vvl0upd3PZgZQr32tUGEfcA43OvI7iERILPXzb3Xw4BItJbIGzcdqNW6Yh5nOYYQ7xm3X_wj-HMij-hOpBfVXD8S9gZx0wHNkRTx-igypJ3yoszeJG9i0VFY-PSoWR0RCVO2NymF7MJuX7F9Su6LUMlWxHT6eQ6-p770qksxtSufJdqs0QN8XTiVRf9Jmahc-JFCmup7VIsiWjBVAQPmVi6asPvaAie72fvpNkPUYuMrZZXyUOm4M0u5SoiVqSs3qiUBxa90Aei8yPRwXVF1yvsT9LaaVIanA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOi2OttT41aAYys918w_FlWGk5ZPM404rddQ6G1WEa4-8zzRQdIWMaS80ii5ljIYjekwOLOs3h9zOpvHuxqhwQyMbXpFwKYAOwzl-3uvOLnhlRBq4N42abpEZGzRsDO3qeuiRKcx6C-4iL_Puqc2QhHz2fj27xvlVGXjhrhLaifuxnbCwu0yFTFfFJUEIKkbE-demH1Xc0Yf_va2r-ZRlZpg98BeMnQvfhmNq9su5Zi_ECgmFq10IfeNTLBLbDPQR1eG5at3_Z4ulaBN5hoZMeQsVN9y7HbN2L9sml4ih61xVOqawIN4Av4ewGLTB-LDMnDqIjKt2RRgIaSDXpCBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=D6DPs3kCJEKFT354_sEOWQwXpCSwpGGQVRqRMcUeNrC9Fad8CviQFrRkDmrJKlwWdpmeVI41yt1jQTUkJu3N51Bo4XmZBwIo_YGWcn6PQXTIdr_SDnhoIIArHaOswiJ2EIY-ouwkzatqzFwcXS31cPf8KP7uYzQhQW3hs-K1GeYklqAe9glWPWpnz48mBOOmoobKDRNMTOXyA0pTJxh8ftbU-SdPVxhpDEm9_AkWNOvvesnTrZPWQUe2UWgY4L4mtW5yMdfVrhmsTsnxdU29FGzyKn7tywZAkGyIntV-O60rW220DN4D3cvaZp4wArF754tOUtnP-srGxjdT5Nhtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=D6DPs3kCJEKFT354_sEOWQwXpCSwpGGQVRqRMcUeNrC9Fad8CviQFrRkDmrJKlwWdpmeVI41yt1jQTUkJu3N51Bo4XmZBwIo_YGWcn6PQXTIdr_SDnhoIIArHaOswiJ2EIY-ouwkzatqzFwcXS31cPf8KP7uYzQhQW3hs-K1GeYklqAe9glWPWpnz48mBOOmoobKDRNMTOXyA0pTJxh8ftbU-SdPVxhpDEm9_AkWNOvvesnTrZPWQUe2UWgY4L4mtW5yMdfVrhmsTsnxdU29FGzyKn7tywZAkGyIntV-O60rW220DN4D3cvaZp4wArF754tOUtnP-srGxjdT5Nhtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R89s25ap7i1ArJNxqiF8BlE8fQA0hS2I2du7PPNyJJP4ODmJEsl4DgfYUJMhaVNsxSirMC1heS-qFy-QvWDV2YxncIJMHcy6wwmOyYqsTw7McoyeZyU0CHEQGtweAu_lCw1cXRSKpQU8CdhKIkVf5T3mfvlBL41LiZbe4YN5fEn9EFmD1_ELfsQBdb7vvTPSj-YeVHWeG1QQ3o7oyfplcdGto3en91Zkgmpl4IOooVEpRd6_E4NvU33sH8KvmtAGRl3hDPYWlAFoQbYil86P_Ikd797EZ8y9UEnIHFjf8hB1La9pylZOlO5MypkX6kSQIzKVinHatMmg5g0ZKpYEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzMwIRsBOqDXM4t6NtKrw6zgw5UBnGyjLCHqcf2oW6th9FDTHqTZ-0VjitXQEWYFv3InwVN5ESRDUbG1fi5vO2AVCZshZWPJ6UzX6X40mKiT5f4tnTOGWE8laoMTnnUSHLjWjDv1A1TEs5JC6hfj0xH553zJpW_wgCMicxRzhnJbclnSzMzE5cj3vYi2BTrIGBnpBDrqM8J5V_t0ibrgyj5nf1qdKe-IgICbcUTDn1t-hy-G6oYxK_r7-QKTjCqQsonFbqxhx_F7-AYxuRCEVUkel4MFfgbzkUc_Hp0-ZcpZLA8hyyDF4iZKmck8SjOv3QPCFg97Y559ksB_cQK7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxPk8w97JLeW0BZncA8cSYPcdjJCh78Oi_bgUQJ-qOLCKddjas0O6ChVnkTm-mEPAyacDp_s2j-ALmsQEU_ss47JsYLdoWoTVOY2JoElZ4H8oahvfMFIgSA7yoschUKEr38ILFsy8uAoZD_4n4A2vYvAZpXy_5vI6Bpsiqke7LkXtgAakE5xI7ECPCrtnWOVFGsWVYjJFjyS0dP15oFDJxY_PeGSZ_L9vSis9mztKbF3z1Kug7lOwjlyzMTyoChaV9QKqJEpYKAiXAPGpDDyUZl3txxdauFKJz724hBOuWeVPPPKjBr6uxwOOni3ECx4q1XA9DeMq-wUqI4CjaFr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-n5wzBO1vFUZC_ULxp4oaeuD_o_MGnOnCkkzVNYuTAR3kcCUxvnP2ufFKEIhtz5h5rH1DXcw6ntAbrYr49YwsewBBATsma_fcVrJ6dJno3EeTGFv-HHTs7aXB__ThuFCLnipZf11ZF-2pxggqPF4cu62GJfQ6ICTgC2sNLQ8uck7HhwP7fSuvx4m12DR4mGEuuyx8ueasuQlkOClGJO-I2bdQd7H3hy4mocg2DwqiwlRYSMTRqTV4sCW2Ak27m4OpWLlqDw6ID9w80y5zz0TqcXjY0gnsKj4tTqatn_xLcorYJDxamVEdM_Ki8VvZ5gYuiEb9ULkzVlAPpqAZ6Ltw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=FG4q4f19XXEBM2_Lg2i6MJV1CatjIjojn1x5TJI9tJB8kWgLn_t9Idm-bw-Ki5J0-6yRUYThOIaXs4PGixFPkO3wExogmMJOZQsuJl6Z1Ww1jc8aFLp-WwJkgv6ajOdjHpteWq7KfQmUJvozGqfaNlsfUVcQvPYiB2saah3Oh3mYDEjzdzybnoEMjNstkUxYfPHqUdoJFNY7PTnOXNrw1-wy4SAOMUADs0_lMso7HZ-5Ih3NmVq5eVd53b6pWfnW4nWDn4eqannjuKisUMlri_F2MnM5BQ-nsvWxbyjQc-50PCZbs888B2VVb-vQgfDtRaSSPlISLFG4y0UssOzjWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=FG4q4f19XXEBM2_Lg2i6MJV1CatjIjojn1x5TJI9tJB8kWgLn_t9Idm-bw-Ki5J0-6yRUYThOIaXs4PGixFPkO3wExogmMJOZQsuJl6Z1Ww1jc8aFLp-WwJkgv6ajOdjHpteWq7KfQmUJvozGqfaNlsfUVcQvPYiB2saah3Oh3mYDEjzdzybnoEMjNstkUxYfPHqUdoJFNY7PTnOXNrw1-wy4SAOMUADs0_lMso7HZ-5Ih3NmVq5eVd53b6pWfnW4nWDn4eqannjuKisUMlri_F2MnM5BQ-nsvWxbyjQc-50PCZbs888B2VVb-vQgfDtRaSSPlISLFG4y0UssOzjWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQBt4gEE5qV0arsPEqcPueAdEFl1IcWSy0-ugNcbRANqSTcd0k1YlyTr4Xp0YA03V_Rfx58cQAmsu2GVa9a5lGaZ2Xpzz-IYQh_2IwinhtqywFHb9MPVFhLbYAHGOnztancqkScnQ-W4MlNSeOWG5cCV_5mh36sqzloFwA507eOFJzjxKDl2hQdpncpfNam9Qxk-I4zg-UG8S1YH9QzceckX7it3m8WSVM4V0-f0G6kknStBQdqsLIJIX17ULKe7kKAlE2c76iBDFHkeSN3HpqW7ihmbWbHJY-ZiJo73s9vduychZGX_IbIZaxAG6ZUv_ASO8CHtjwqXksIXe1lj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIQQfCAYVA73OxuxRrQshM9AoMzMib5TntVtuIRuqkmFFe9Ex199SCJmJNm58BqZjkFE7UrD2P55UZKyctKpO0FqnnU0rWZs6goIfAq2ozzgE9NT8pxNBk18xswguqXVYYehhj1vm0GVlCZC038GawylSbUHHf95L7PU8XL98PISU1OJZxA0lbEAwmemXWQ6MvE1kK696395EjeVhbu2oTwq5tdAzAcrRnTFg5xE561kKbXM2goM0ZfOqyPtT0VtOcvhaV_ltTvzc0IvMxyQpohb57o9TjF4khdHqgxdGzvRgyqNztqRZ0HvC3blIuM8OIx4lj7PVv0gJsGAeLALDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
