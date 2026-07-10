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
<p>@news_hut • 👥 189K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 06:50:05</div>
<hr>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjEFofRyaqinnTPAYE_vo6TWPvN4TIy6wuLFCgWDgEnbwMkya8aSpDIAbH-QuexISsrNl7R9gUbLRdDJxc99j39sJm2mZrbDrVXsCELDhFhBV3CXpG2Qxeu7Cme5380fsjAB5NCmpuzDeFSKXHyDmsRAmjvc3m1NPY7CC05XAEK3xC-1e4WW1w9IabxK7MPzhFlBRmsShwpzGG5dZbVS5AJcamy5-0fC4vf8ZFLSbWz41E_d-KqyFQ8B9MqJDctIzsIjU6icovdJgNUxShV5BBNDfPDnjlRngGyUywkxOyLB9NAtj3dMKk8Tz0c9MdIggRuGT1maadokqnwtB6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEK68BX4eNB5pxr7MKeKZ6h1UZyTZDu2qFLQbNM2l8NNPzwIhrsrcB9oRTYKKBDu6PMejC9MpqoRAA6pgxDKlIpgyBDchZjjKNquY2qdYn9KJoGHo5XFFYDcoM1fE6SPJOjeAbrnF4NdhDj1KiKWDBRxnCjP5DjFvagyJv63o9Y6E-UFBa8rRiI5zW3sZUVkl9qmCPAUxRClsB9lD5t7xjkYaR-teTyE1vEQcX86elXamiTWbF5YpfRQXwNke9r-eeaz8Pm95SwqizPPjGMPdlAf6g_0OxC8z_H6FuaaKEkOHzQS_-J4q0p2WzjGYC5FkOPmQG0J5NbDlShTGctk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ63as7Tp4L4Kyiy5_A4wbvqQhlHHia2GdLokuamDQCiV8uyoUTTf92zJXIiuPK4kVEkl3E55dzln8A4iWTio3eZW5jFQnUj6cdfHELhknehROcBuuFW0rQP9d_MQFRfWwvcuH-6ZU57T0RpReMg7vA0VsUmoMt71vb14yLWoKbvS9Ds3M700Pze0Vk8E670fdB6oLdkTtwiEy-qdxTGxOP9JFcueDautwuaJeZ7DRBEPjMEDGZguaRDOTYeY17UE8pZoO5mCNRBF0JE3YJPjm7vpoeEstvvwrawYwZ6u75E8ho6YfAPpA2A7fH-Pe5K24PAsv_Upsu7VVYHDzslww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCILebHerj1h59p4R76BI7xSKvhl1nhH8UIK5tOeC0LuTED18SQj7xiRNFO2__7YUO3PpEZW7x8_uiiwCJ-NYVYsjOPrXEY0rpBbNpwbT0nfMfRnlPEYPzuAUscASwUv0e8RjqQh3OkASF0NG02VWqVAtl1_SXgFTHbeCo26NI9svf7-db927vLk4bDYdaXQexz_V5QwCb8DHg5HWHbHFoarvIJOKvxOkMOzTUk3hCxLsFnGNxAUv8vD2pwjgSnmQVQFg54EZrt46_ZLKMKCnGkU680oZBetWbWUQYAc3SgyGEnzve4S3oMXpSL1R9MPCVDof2PRrGGfbwu_wVy5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n54U4kvSGnD44oT_8WJI3xSaDZ9RTSnlKmASqCH7dGKRMpeYh7BVKnMtRsY0utBsZtO2r_rdl7zXi4aOlQbPOdvGDD4UylQ8LOZpxXp_YGqBT5yF8eTdYkKGgfTOCVhigMVFhdosmOR94j3HL5i3o3KdqdksBmgkIuCpOi9imaEuAEsL89iSsM0KxB25CIyIi1XzDPLUyI32wVVHea3_PSXbjNif4hDL6p--WZOGmNXaxdWoqvJKFxP0oxbhXTZGsBVy1zwiFTIkQ1zSxRpJM1sM4tJJMyyXh-i_PlccZbEtjr1O9bn_bBCVBe4PULafpcYsda_mgaHO_Kq1aZoiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=ctTif47CggUlyWu8DSke0EXjWRbCSTg4CyiKqhgecxS9UlDDJk4R82zzhlPicXZljsFmJvoI3Ikqh8ApHkfuRcxle-iFWSpidPqWGVe4vAYLA9AZ22-EUNgYjnk1SF8ONSA5zdAQNGWLEp_PopSVzJhJ_I00KxIWqEpFj7lXJsJZem56wNqo9JR1c_r8MaYny3w6wyogWTkAe_xJn6lO8loGBNt_CYGZBX3250NJg8VppLyFXZf3nN5_XQm4ROfXUemvK_pRVhHZbTW4mLFOVc-lrMBGPU48gAqQ0bAlFMfrQuM2bBBhKdClY_HqD0ds5ufQE9nhtTP5Ag39bUM7cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=ctTif47CggUlyWu8DSke0EXjWRbCSTg4CyiKqhgecxS9UlDDJk4R82zzhlPicXZljsFmJvoI3Ikqh8ApHkfuRcxle-iFWSpidPqWGVe4vAYLA9AZ22-EUNgYjnk1SF8ONSA5zdAQNGWLEp_PopSVzJhJ_I00KxIWqEpFj7lXJsJZem56wNqo9JR1c_r8MaYny3w6wyogWTkAe_xJn6lO8loGBNt_CYGZBX3250NJg8VppLyFXZf3nN5_XQm4ROfXUemvK_pRVhHZbTW4mLFOVc-lrMBGPU48gAqQ0bAlFMfrQuM2bBBhKdClY_HqD0ds5ufQE9nhtTP5Ag39bUM7cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjDhH9m7BAZEEARqSRcmj8gQIxYOAMvZOUQrsgboctfahuTJTPHVA0zQwm0juO3wYljEr1j084zjeu_66mqN6ZGEP6mAZsjifICMGO32jydL1T6piLBX5CL5FjFbPzPKBkXUYCTP5vHm6APM33P7ycTqO7N4ydvOFaiWhiRvA4-A2xj5kwwVXjp8LiqHkLZ5xUo6NwafbYlCFe8M5pBc79Ki0aPmoXL1YepLHu1Pfq9_lTDICBtW_2feRcMjCG2bCyZW_pwjtjfMVACRId3blPj816NtSYUFRNBS_mYlsBornmCzDCM2suweanhIuwqA6vcKBhqiXhe9x0cFMrIlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF0No2u_Uy9CCJdeQeNKMKWt_F7p4b29Wsf1zI5dbj3WmQbKhSL6XHT-dTVjZ8c0DgShCtI0aBQ6KhItplTgbI-F9l8fATV_K4bDcbZzp0aynBQp6vAI7Ev0UPTAciiPt2j1lzQlh4YMuEw1Ew9uqMklygnwSnYy47QbebKM3ENS20RcpZBMBaoIR4OpQLjaBye2J92wTZRqc4gGUAl6sGVjaLfBaHetuTDKZ7xZu5Z_0T3Nk8ALNgOTi3CwtXLtisvV532kzJ5akuGXpqL84DxAPxhfYhHfcLFOWT_4AS7fU92Sf78SJ-hqCk1W6JEKUnL1ncDqg15VFLwJhPGBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=B_JqqsN68iufrWvydukBvalI2NW1b5rdJ4QlDytr59pkjkSb2xWLdxe9hqy9DOBj0IK7y8yAzK9G2GMyQtnpKHTsv8yOHzRTPRCNc5_blJap1ebVkx5YAq8SN7J1VUELsJGtZ7hfxopTrvLiSYtz_1bN5Y1ChWpAcw6hp6RulJ2a7qx2caw75x3-cr_Z5xxWBvvl_FJc3ZSIhT32Obv5zCX6Zv2tbH3dXQBxTuBIe3hTrqWYvvD2nS8rmHYHZ5wJqB94Ynay0AxpapbdsLKuyTLD30WAT-pVFORtvAxVOJD7rZmTOc2ExqMCZTzjDwhiejdn6ku604uEZEu2z5gUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=B_JqqsN68iufrWvydukBvalI2NW1b5rdJ4QlDytr59pkjkSb2xWLdxe9hqy9DOBj0IK7y8yAzK9G2GMyQtnpKHTsv8yOHzRTPRCNc5_blJap1ebVkx5YAq8SN7J1VUELsJGtZ7hfxopTrvLiSYtz_1bN5Y1ChWpAcw6hp6RulJ2a7qx2caw75x3-cr_Z5xxWBvvl_FJc3ZSIhT32Obv5zCX6Zv2tbH3dXQBxTuBIe3hTrqWYvvD2nS8rmHYHZ5wJqB94Ynay0AxpapbdsLKuyTLD30WAT-pVFORtvAxVOJD7rZmTOc2ExqMCZTzjDwhiejdn6ku604uEZEu2z5gUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=lNS0Dnuvf3cf6wE1XWHkxWpTyV0PLQOw6kX8Zb8Bsh5uR92JRVkBLI1PZthEcE5E4s9Q3nZxN8m9YrVUDeald8D4UtLam4sY4Jp-0zO7RRrwYA9CcDKAV6yn8NpAJSIVJdrd0Ngg87a0e0m8Wfkjp3TiM2q_oiIdZcBro8-BiV_7nJ0eln7xALA8vsd_0wXoQ_12Bf98A3EiOD4aUULUcTWE7D0ls60_FQWiOnxrl3l4gqUnQ8JLPULUHinroYZMmNOfNFNmQxDnLKQGtYLvv_szRkSOrvcjnefQuhffGAr4beGH979xRgasTCboji9j1yKaFl6pZAvhmtRKcqNHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=lNS0Dnuvf3cf6wE1XWHkxWpTyV0PLQOw6kX8Zb8Bsh5uR92JRVkBLI1PZthEcE5E4s9Q3nZxN8m9YrVUDeald8D4UtLam4sY4Jp-0zO7RRrwYA9CcDKAV6yn8NpAJSIVJdrd0Ngg87a0e0m8Wfkjp3TiM2q_oiIdZcBro8-BiV_7nJ0eln7xALA8vsd_0wXoQ_12Bf98A3EiOD4aUULUcTWE7D0ls60_FQWiOnxrl3l4gqUnQ8JLPULUHinroYZMmNOfNFNmQxDnLKQGtYLvv_szRkSOrvcjnefQuhffGAr4beGH979xRgasTCboji9j1yKaFl6pZAvhmtRKcqNHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh0rkf_cTVd1QqAN8eufUSBkMoW_W-ebWKHivUQrFlX4KmUy_-Cctgl2JW83SeL5WLmJ1bES1dbq4n_vdPfQDqoR8hXfrM0HiHEw-7I9GWJDz-lSG0StEn46EmLS6v4B6aU4hO0xukINLyBkEDwFItHzo9lhB_yk1lAEjSw65N04u1-Jq3EFkGFENJtWs4NlsRCmZTCqUqYXCNOlJqwQ0QedLz7K-7hvAqgN4P6aoSt8rBTfyEgJxU3H0dEU73TCXjhBKcGMPFGnG4KUMXDGDDaoR6MyHwt185v4VST8awoVedIYJvDmU0isVaVfZNzfcmnwBSOojSoOLRLpItQG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=TKvpJA3xak_t9zZy8ueG-1gFoVRIPnEUfBGeeZU2v7YnZPn5CitWhIyzu1wayXWAHeTEinGPwbVBkOWhMeFPNOIaYZ071VnevhZGmDSfxzCpoWZdUY1ukapYmpAx7IIbGqRJM3N3u90_v1G1IGvlJ9djy240bQ1GkHz4eEanrlbA-6qIRJZs9fHr7ca1FuGCg9K2YMq7LRWuXOcKO8R2kojpR_IGkOD889xO2i4MLKYtMX0EMOeDGUbmCUFfAOZ2JzrM__IkBLU951Ap-3u6v4qJLSFnaSf_ZmfD-TfMYgrDA8yDnY9kF4ULwc0bymiRYDvN_MxcpArp8yNZxkvgLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=TKvpJA3xak_t9zZy8ueG-1gFoVRIPnEUfBGeeZU2v7YnZPn5CitWhIyzu1wayXWAHeTEinGPwbVBkOWhMeFPNOIaYZ071VnevhZGmDSfxzCpoWZdUY1ukapYmpAx7IIbGqRJM3N3u90_v1G1IGvlJ9djy240bQ1GkHz4eEanrlbA-6qIRJZs9fHr7ca1FuGCg9K2YMq7LRWuXOcKO8R2kojpR_IGkOD889xO2i4MLKYtMX0EMOeDGUbmCUFfAOZ2JzrM__IkBLU951Ap-3u6v4qJLSFnaSf_ZmfD-TfMYgrDA8yDnY9kF4ULwc0bymiRYDvN_MxcpArp8yNZxkvgLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lhzvf49OcUDdZbNsyqVylFqGAfgSsICjtIBnv6MgYWsogA7hK99YxedfMiFu4vgEaRs9xYgvhQKeZi9e0wBg9wa1r_CL1dTC0c2FRWnvUAOyXwGkN3NM1WyDYIanSbOjiUvMijAQt5Rmc3zGByAEFdPvI7FFm3_XdnbooweIzsAfTn3PLRoOg5cNqdvicJAkJLIYVJ1I5nzwU6vYp6YT-Ol9T6BShvraod2gAwkLgDjneJJFnhnjr_hAp5enmSj9cRmi4qtRjHY-jTucUw0-s0i7FqXWh3pLjXnmmZnwya5W9-VHdI2iX6hymkPYTi6kNhL1E9JlWSH6GmhYQl8ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHQBniURDZ-3G5lUZQgiz35mnHtpT9MgS6mZhTei5tuLsr1g0VqAcGP4GQ84SE-reNVgm-NmCwR03IH9WJXgl7eWXxmtifLLRq0T7QyAs8WinDBJTCd0qkcCKGptsjkyrjEhZ_pXqDJGbaq8lCT76RpNkcLcsBpesJx9Kjd0Xe8keAc_oFujO1mT89jczM30q98sljMspvdQXqNM_yCzDDnd3577cxkwKg35PEUdMtPbJWRCypPfX-Tp7ojXEXG7956D-zwmfkgbyWYOcnfwMs0zv5qcNqs6xCQjW8e_zATpU3rugT9Dxcwp9rsqOfro-VcOr7igAXAbKnY3twN_4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVWhoz9hdFdq42ZgnDX-Ernzgim9qHYJmNL2eCqtXHmC8SEb1hZGEuSdCV-e8HYs3hEmij_TkWUDx0eqhPPz0x0My67vz5BQBw3jhB23b1aiUnK51X_Wu5sgITU8gmWerYu5m-_A4NrFMNSaPJ3rPJLF_vUY4zsaJ_EBlnYVfOt4SD0vDiLM16cVJn3fPQpet-bics4vuZajq3d4C4UEYDZo5OtrKCNxyvDynJ1h6-KLcbiMSORbSU-UXfuUW4UU4ljPVECMV-RTYsOOURByNCx2VEVEEYSWcMp4z6x6sgOQOazg-E7G-drbA4fGNcELEtZeE4ifRzRBAy0Ov0RWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPsdUpN2qWnc24oQKQ9JwrWmpyPYc4Uccsxg5dHqzyRzcl0jqwj7ekvuwTrzw-XIqadEOqPwfIlTUN8rDEMWoyHTpew1qpMxMZ84b7TG-EdmXbIEiOdMA0kne2xiNaYmkJ8ZxuEZ1y-oL84wvYUU9WW612EwMcYbs8AUpm1nNcjmUMhGWszWWEqMwBqG5Zr2y_rUQXwM_jl3IqvcyO4lqP5w_PUXqxX8Nv0W7uIrT0lAQNrUJu0IFwDPnCKQOvspj1o0MfWq9H0bm_Fv4ZTSH31ALmNYQRxd-H7LZTUvDBSSHgRMPPU_GhNbckjMPCfkxzvCiZGxIno1eqgul4A3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=gIZyndlQIfbUgYWyeZgg9jO-Y-lBchiuS2O7d1hUYjuSQa1G928Rdf2AM9fEB3L97wxQi9FcpnZacni3WUaiRONeh7aG8RZcVIY7O2y4REycmd6cNFjn5JJQz2GKA40kCJod7hM5I7S2SZ2PrqDn-sgflhUK_LSy5AG0W_783WUY4SVG7388Rh7Hvu5itTM9pRHUPp7nWJfqLiSfZ6jdBPfOaDmkRHKFi3WfjhlpMXnIbWilcImx_ZfkiBZVMuFowlKThSqiV0Or2khZRSwCt2AseoB9oDcXYUyQJgjkIy3DuEd2u1ooN-TeLC5GJ1AzXU4Vc6jb4qK_Gv1DFTiKOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=gIZyndlQIfbUgYWyeZgg9jO-Y-lBchiuS2O7d1hUYjuSQa1G928Rdf2AM9fEB3L97wxQi9FcpnZacni3WUaiRONeh7aG8RZcVIY7O2y4REycmd6cNFjn5JJQz2GKA40kCJod7hM5I7S2SZ2PrqDn-sgflhUK_LSy5AG0W_783WUY4SVG7388Rh7Hvu5itTM9pRHUPp7nWJfqLiSfZ6jdBPfOaDmkRHKFi3WfjhlpMXnIbWilcImx_ZfkiBZVMuFowlKThSqiV0Or2khZRSwCt2AseoB9oDcXYUyQJgjkIy3DuEd2u1ooN-TeLC5GJ1AzXU4Vc6jb4qK_Gv1DFTiKOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=Aez1V7OJJD0ov4GpMQU_pUSoGsgvFTbtWyDMK2S4hAmYD_Oa14-r7H3ZimeBc_5mAWRnUF2lJasfBXTjLyaCJlkvl5ppKhRI6zDKd__zmAFsgJvj5IjFuuvyuy8ju_vdljN8XM5GfZNqzu3Jmu-RIPXHW-8YSi_vbs3JXWl75m4lLdHlM-MKwiCJlAaeT3bU3Y9goB6I5skCC-pbE5HvUm9h9hfgmz5IXoifhB3pRxCpUkBP_bXn9gNqRHZfF0yF4U8IA3ZODvrFluwUVQolKP0JJz2xRhiEc2R5q8rhOw8eVmkGmZQpW8kfamuljhEetSxCcRxZpTT6yQwJuZibsGzksBFHQ14e4OlZMC5GgS8Tgsv7a3Qo6JSnP362jWMNHdNwFBim5UxySLa_U6QM90SqAHURfjTsA1dReC3KfvbQujvr9lpm9Bsxh2tIfF3t7a3zFuIajhR56MKmNjCU8IzZmrzjfJJ3Ibh8FUBJS3zR7MwalH8e2B9zsyuHbl7PmM6cB3oY6-Xpj2iL1lko8UAKQuSN1_sriKbgwWnzqKNGWSeWA1yNdi23vW3oi5IG8zZzHR2bO3NntTf859TGOyJOgwnWvk7aj_Qn_4c88wk26esZI3aeN4g8lQ2w2suOrlXPqfwpceyPyVcQGtThuCPmHgFiZ_ZLuzJXGW-bOQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=Aez1V7OJJD0ov4GpMQU_pUSoGsgvFTbtWyDMK2S4hAmYD_Oa14-r7H3ZimeBc_5mAWRnUF2lJasfBXTjLyaCJlkvl5ppKhRI6zDKd__zmAFsgJvj5IjFuuvyuy8ju_vdljN8XM5GfZNqzu3Jmu-RIPXHW-8YSi_vbs3JXWl75m4lLdHlM-MKwiCJlAaeT3bU3Y9goB6I5skCC-pbE5HvUm9h9hfgmz5IXoifhB3pRxCpUkBP_bXn9gNqRHZfF0yF4U8IA3ZODvrFluwUVQolKP0JJz2xRhiEc2R5q8rhOw8eVmkGmZQpW8kfamuljhEetSxCcRxZpTT6yQwJuZibsGzksBFHQ14e4OlZMC5GgS8Tgsv7a3Qo6JSnP362jWMNHdNwFBim5UxySLa_U6QM90SqAHURfjTsA1dReC3KfvbQujvr9lpm9Bsxh2tIfF3t7a3zFuIajhR56MKmNjCU8IzZmrzjfJJ3Ibh8FUBJS3zR7MwalH8e2B9zsyuHbl7PmM6cB3oY6-Xpj2iL1lko8UAKQuSN1_sriKbgwWnzqKNGWSeWA1yNdi23vW3oi5IG8zZzHR2bO3NntTf859TGOyJOgwnWvk7aj_Qn_4c88wk26esZI3aeN4g8lQ2w2suOrlXPqfwpceyPyVcQGtThuCPmHgFiZ_ZLuzJXGW-bOQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=TzReF1lTXwxFoSals25pbO5Uoji5g1h183dqjUg17YOBbxx5TKLTFdCY7eHHU1gQas2MM83ML36kv7XKcxLw7SFm7usxkU581QB2XFBD0rtiEL1aR6IzprljZPXYuoagdDvewq6sY-TMsPicIT1zmYKoFNDBhCsrcJo5WombGD945LfwIKILT-NkjojYHseUaM8BNeqpVbAkBQcxxyFXMmbl8IRV160YNRh6bOBSM1lyKPWHfXm0PBmpYXvzkx_uB2K3lSteTJnIo5cj99IPTrS1Kh9JgFXIxM8va6EvEJrIt_3pabaj-zIx8Rssyy4VYs0yoZ9D-P053IvsskQMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=TzReF1lTXwxFoSals25pbO5Uoji5g1h183dqjUg17YOBbxx5TKLTFdCY7eHHU1gQas2MM83ML36kv7XKcxLw7SFm7usxkU581QB2XFBD0rtiEL1aR6IzprljZPXYuoagdDvewq6sY-TMsPicIT1zmYKoFNDBhCsrcJo5WombGD945LfwIKILT-NkjojYHseUaM8BNeqpVbAkBQcxxyFXMmbl8IRV160YNRh6bOBSM1lyKPWHfXm0PBmpYXvzkx_uB2K3lSteTJnIo5cj99IPTrS1Kh9JgFXIxM8va6EvEJrIt_3pabaj-zIx8Rssyy4VYs0yoZ9D-P053IvsskQMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=IWtcL_D2DwAUE8OxvvIdKiW-uAedCP6SysDmQHDSc-FcH6ay2DdNc9Kk7d45a1owbBIMS777-p2lU450Q5wsbFvInR8gO5b_7cHKxVTLGlL_QhIoXap2uTt_jPklZRUWe2XHrFFeHO_OF2y9hDRvNjN3p8P5fU1ONz0xduofsmz1DniP9pHcR39PnzTWTwlk3Tdcwd1dXT7MHc4lf10SVFIWZN7SNZEEb887uw58I4Xob7a6FfH6F7S0K8InrYDLH81aAFtIjcA_GsMY2rqkKEQxrJWNwS6VhIustiyA8t9D4gEgWZ-fq9amm8Qe-NIWwHB-IQS5qoJePWkJ4qkL9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=IWtcL_D2DwAUE8OxvvIdKiW-uAedCP6SysDmQHDSc-FcH6ay2DdNc9Kk7d45a1owbBIMS777-p2lU450Q5wsbFvInR8gO5b_7cHKxVTLGlL_QhIoXap2uTt_jPklZRUWe2XHrFFeHO_OF2y9hDRvNjN3p8P5fU1ONz0xduofsmz1DniP9pHcR39PnzTWTwlk3Tdcwd1dXT7MHc4lf10SVFIWZN7SNZEEb887uw58I4Xob7a6FfH6F7S0K8InrYDLH81aAFtIjcA_GsMY2rqkKEQxrJWNwS6VhIustiyA8t9D4gEgWZ-fq9amm8Qe-NIWwHB-IQS5qoJePWkJ4qkL9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dv0aupqhEZz7HGWxFIpSmMFO0dcm-TvPe0HjF_vCj5-d-G6LozakZvqILBW0K56FNHJRzMgu4sItIQTpYzoTNLhCfJZ3d2MAQvTpjfKOJrLDIzxPCkmxPp_X6ScVyFOQRs_dcs--cPxDK5vd32nndI2e5nOXai7qiKUsChyQEGn7FrxTuXpNWWE1kJgJWElfXdO3RMtQ9NV5oDdm11UunhQ8LPd6QtDjlhC0W-bcjF6-BKFDSAxMfE5yxCu3jA-GT6zqGmDed3_xLSZpXWYH86CtcYj95RYDjy_LH0KWDRwQo1Uju3yguaRtSjUvbdBIfGm4CNWiSy5E5-5h-3RBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyHdIlyAsPcwFF3HGg4qJ-CtY96lHoPyz64W1qQiEeH7HFd4-bEDPEWjDrjgojFj8cviCaA-LbJqabNGwWESxn1V4PZ-f8utUPpsdb0Zf4L_LBp-Zf8muetrNAA8_mN63dLm6izqQ8zNywz5T4kOEHezreqigWmj9C4Nz3HFfoEpnhiXE7fkYbWEuEUpmREGgOhRD5kQA374QWqxpgaGLRdSdZEYHc6DiODXZ1CPNuPPjEtQulAN0MgI7eVjPLjcosJMM1LEO-v_mCtuTx0oCs9bEFnJafihB-x1kMrc653jBi5S307L519slNUZvXhCBxLngm2wghEgO7fs82O06Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRDNUOAKDYFGdN2GtG1Lo7J9qLhgkujLxNr_edF7SYLEDZhSnNHPNcKLQ9RZ3nHt9gWEB0J0Dd-tFmwNfGsTIQelv2hBpe7GBFaE1sVeELsDcE_T6Aid_IlRsz4n1j_JktwjVd-27XNy0pce8LqLMPe03dvnIhPExJFI9OnoUQnJ1EujLYTRE0hn5whO1QyZcG21zU7bySpKUthCl3MAk4IuBd4wTl_qGCQnSWK9PL8Xf8UQNVbjTQ68ShSIEGspx2of7Zwk89H1dDQSQJb1-KlBWlq4B9jpmVQI4ZfK5tsZ5_ZCBf7POtBVqWvvD-JDwrmhv1DExcGrSRzwXhIAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOuW1uXdiaPP6jYqZzGVNqrJWcXmGoDjIEUjNO5YCaIrXXiZFZfmkCw0cmjMI7p_gxz2F1JOphgcQeB7KcpihXtuX8EZdFxforFRGzJCDsp7syt_Edt8qRv63W9JaWWskjl_Kp2sNK4v-w5nn_2e1WK2YnT6Jml9UKjQqtHNPsKW7RbhRAZbayIwtZ_mbWSjdAgNOa9R-p5dwB4zwESuvOv21UEeBMe_FFpzl3Jj9CZ6pwF7VUt7y4TDkLJACJeeaDNpePtQvyHZ0O6PG2_nD_Vidi1yx9EC3cvdHJyKEAO2xu_TFbIChVM5Gjpr30VSgMHjfONwpANgmEYlwPxdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiHY5ji4KqYxU9gFjYzmlkQYagwdYN7uOeVvfrqID6oheVcxS4TstAvuUljmYOQWlxoPz-KTpXFRlE8LYXS4xwIzp7DQGPbbWFqlQJeGi0E8rU7JAENrD2bu9gcZa6UwIFS4uujs8fH5pQOm4Yd60uKKySX3-5tS5afLWNs5ccywRp4CPNu3bX8SSvE1qi43uYoPsF2p7WO4B1dh-59PVRmv8xmtvX9RKM1Va3k2MwQwruYl9OCNSSnLtguXazjA3JQzJeMr4-XbVapr-pZv5vILtsHHShkkWy88j2QyzFnZFEfmJbPFDM_3C9tPwowsxuSudoAJWzYsvqAV6ZmVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZigWy_46OIPAtHZ4JSDww1ecnVQ0sXYefbMbwunDMUWU4fvPglG94fnKDLmb_Xn3Ao2RhIoV0T6JgzWLLY598I5lkLnqHYdERNBRLdShYrn-eWo41r2z232niVpJYYExMphWYmtKZqoR8figZ6mVQ9WuQbftiR7Zax2Eep56YgdyrF-qxcBo3VxpFBqq0twsGSqglzEslxm9zLqdY12MvpF_IGuOoegs0IJaGrYWIStc5xb0VHh0BYaadFnxkKmNdmyNFliHzFI4K5UXXcNVBj7iW-SaJmxYk6e02XXk5rreGuhRIZYNNtPk6kjCDrMdWZ9KqvLhcQpDFj8J9Xw21A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI4kjO6m9LloA924Ra3xLoHOjxAwP1CvSfh7JqefBQsMRNXgnwPmgr_COup8h3m3wwD1VzC9IR_ewzdK2vUBBBIg6aOE3I92ts9zmCchuZLxe_Yhga1Zr5FDe8GrSt5GAZz9NKwU-xBfR2YnRNgsS7ty7xdeXhqS0YKi_pL-ZS4ByRiU9gzi2STnwEvOMxI3fzi297cH7wbyG4qppyQGVHMJNcZsCODuFK356VGBzUCbk-DhqFA083ujwVqYzDbPQxM6nhRb2eoPtzIXiNasGmnoXdL7b6LTYgWKIiRxYGWzRsjGOp7IR-wAdBpm7gHS9Y4bxreFCKMp-4yBoSrk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL9KFbWESdxs4jc6Fi8snbjCK3-mQ-83un7rT1vtzWwvKxSD1BT6XOHXydC0k6D6dGOPc-wI1-3Q2O6J0dgp9Ci7LO-kDzUTyoq9j2p6xmtzxb9ewX6KXLzC2i34n1S2pDQzCmvfbvBfqLIYS6aSU1V4UGkaSydzbf0ZLP9ZIlt-1pp2gYhP_37Yi5ij9HoKOr23KkOuQHEA2uYjgmmB9HTRVtRJgapJLg36s4yQu1wYtOccSIH_flb8_M2WPegNmDI1slRmOlYgLjRPI5QWEmEFC99wbCevPwUMtBtZDNjuSJoM1IM4j3IQiqonIJ-wQXqZl6padSu4qC-vM_8xng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Md26zSlYkvzXAc9Swa9Ff2ylQ15MRuDoEOz8zMQwRb11dlD88_0S7ll30biMjvEdEhmmK6xj-6is-HIQXlHi6VQAICWgjcL42CCVVcgqif0NnyYIDxNcA86f4lNcvkQEYdMiwlrmlzAs4z8yYLLMzlrrUu5qxu1G-qQLzJzjKPujts5b2kx26tnTNnvUx8wV7F8TvIFyf4O3e2gQ0YMYaqJSq5dmlAbiXFpkQT8u-a7fhY9ok678IhHPeiJQNGyGvs9LNr_kppCCdG7jdyKYJFYEy2cVc2zl4-40swUza7KDgc72CQZEhd3sCO80sA32wC_QtKfh9mvKeg3roqRqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Md26zSlYkvzXAc9Swa9Ff2ylQ15MRuDoEOz8zMQwRb11dlD88_0S7ll30biMjvEdEhmmK6xj-6is-HIQXlHi6VQAICWgjcL42CCVVcgqif0NnyYIDxNcA86f4lNcvkQEYdMiwlrmlzAs4z8yYLLMzlrrUu5qxu1G-qQLzJzjKPujts5b2kx26tnTNnvUx8wV7F8TvIFyf4O3e2gQ0YMYaqJSq5dmlAbiXFpkQT8u-a7fhY9ok678IhHPeiJQNGyGvs9LNr_kppCCdG7jdyKYJFYEy2cVc2zl4-40swUza7KDgc72CQZEhd3sCO80sA32wC_QtKfh9mvKeg3roqRqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=T3PISWCKNt5CPdWoDJxXHxJncJsTrJtoTaIdE-6Pm64Z3PKh2k0HULZT1tBgff_8-uB73w2oU2TVWb3ItUwnoyBCqFH1MmnhdDiwvdvAsrqtAP-icjtFCyxexkobfA7SecWy2We9pPKfmYoM33-ngdH4qXaq-iZHigJJDidP3sDFQwK3TUz-FoyaM7tveHFEbQ0bRwL-yxVl7GvhwEStkc7TWv4tdOIzvGMJZjSDCjc7ZL7nm2DPr6Crb70dsA--wb-Z9oBtJdJogdZWDlRXGdHZBQL_tYcfmEo98sprQeQ2mxcGgUEu8OOga9DXDogvvgPjDEK36TrLllGM11IshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=T3PISWCKNt5CPdWoDJxXHxJncJsTrJtoTaIdE-6Pm64Z3PKh2k0HULZT1tBgff_8-uB73w2oU2TVWb3ItUwnoyBCqFH1MmnhdDiwvdvAsrqtAP-icjtFCyxexkobfA7SecWy2We9pPKfmYoM33-ngdH4qXaq-iZHigJJDidP3sDFQwK3TUz-FoyaM7tveHFEbQ0bRwL-yxVl7GvhwEStkc7TWv4tdOIzvGMJZjSDCjc7ZL7nm2DPr6Crb70dsA--wb-Z9oBtJdJogdZWDlRXGdHZBQL_tYcfmEo98sprQeQ2mxcGgUEu8OOga9DXDogvvgPjDEK36TrLllGM11IshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFleBccliM-nLZSp3P4bYG75JOFFoSU_AQv6n1gnEQyzC7LoqcDmJphR_-76faIUeHU7MsjMeqU4dj9vXKjjnCc9A9aiwue7TWzjUzxfXuejmnGeWmpVpICXImjtZ3rRfXX3qWXO429Z2si-m0EbRo1oT0v6trdJhPMPMhhDhwUimezdQHEVFThs2BS0qwPRHqC-8EIunjwD95XJ2oiWISw6DS9pji5rImN9bH7teq9ZXRK-MvVhi9WnXVcLdy6I4voazDodwGfMiEwMk9KzoTTwVyR2QIW7Rztg51UTZksmu_kMxc_cLtGwDchFmfAAbp6Au9iwFXBMjaLT_NUBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=M1V56vgGl7Kb9RmDq0jaMI1kE-LuDUI34hZaOQAd3t32R9TUXrCKD9CCSlZN6N8idilFXdwozEihS7jfetBlSMWhxyGUwj0H91EYbm54ru9cYGo1i9lomOULlrgz7t5ro6IOJAlYU5v3IHnXI_vS-OAYd4zIuqNDpPJp6GY5P90l_UHXUhyuE_MJZJ08GAaTCckb68f7Nq6-EdA7ZfVm9x26QsI1Vo-bIJlnOeRDy410rELC19vhowCY3nxT0e0w4a6xjZbSunq66ig0-Mn_dCtqGMiQ0PbiiAOfIXCI99a1UkWV8T6lC4G5md1dC37TBHppReabZdXOR4__FjnP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=M1V56vgGl7Kb9RmDq0jaMI1kE-LuDUI34hZaOQAd3t32R9TUXrCKD9CCSlZN6N8idilFXdwozEihS7jfetBlSMWhxyGUwj0H91EYbm54ru9cYGo1i9lomOULlrgz7t5ro6IOJAlYU5v3IHnXI_vS-OAYd4zIuqNDpPJp6GY5P90l_UHXUhyuE_MJZJ08GAaTCckb68f7Nq6-EdA7ZfVm9x26QsI1Vo-bIJlnOeRDy410rELC19vhowCY3nxT0e0w4a6xjZbSunq66ig0-Mn_dCtqGMiQ0PbiiAOfIXCI99a1UkWV8T6lC4G5md1dC37TBHppReabZdXOR4__FjnP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=AHXRlDFkTI27-YixSwEbZ3jDKFHJCCFh_U_hLC7IoC5OgFSea_x3BSK50UJO2hec8IaKZF_yE1z2doEOn7ndwc2xYv1szqIHJGj0nFCDMstKZrEGwFXeDeGJYsSHywsD-0iZ7kJI4Yd29qEpxdHa14blQ-aymczFjjqwpHTSr-LX2CIFuQ-cifYTyDW9cd3RTxMPuomFm20KdXwBR9hRcS1W3J5CgM2v7sM_d4JTryJOLm0tDaFs1AwAnXFesUhg2vuHB0Vd1kyktorwNQMlNvZ0NruMQvvWhMrXcyY2gK2igR5Mfb8rREM6MCfN6YNRj3Ni-tyY3IdceGAKMPfNBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=AHXRlDFkTI27-YixSwEbZ3jDKFHJCCFh_U_hLC7IoC5OgFSea_x3BSK50UJO2hec8IaKZF_yE1z2doEOn7ndwc2xYv1szqIHJGj0nFCDMstKZrEGwFXeDeGJYsSHywsD-0iZ7kJI4Yd29qEpxdHa14blQ-aymczFjjqwpHTSr-LX2CIFuQ-cifYTyDW9cd3RTxMPuomFm20KdXwBR9hRcS1W3J5CgM2v7sM_d4JTryJOLm0tDaFs1AwAnXFesUhg2vuHB0Vd1kyktorwNQMlNvZ0NruMQvvWhMrXcyY2gK2igR5Mfb8rREM6MCfN6YNRj3Ni-tyY3IdceGAKMPfNBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLhs7W_uiKWzwMtlr1sAMfyHh4GNPG1RsINMM6_w_D95AJFI-dyWN_33BruWxfdCa9YXal0Pel6IQ0QtatYR9rfTxD-zrVV6_zUmBwL0OK9PqeA-1-jaVzoVEAZso5I35drIA3rwnvB1N_xHrxG3AEWhVleHpzA7amuft4G14vYfg--8_fd15NtluX3K7anH0sUGIS4obVAQTrSMOY9xD2Yeewo3fpPW74fxjROxRfAhMga_zZou0lsyBLhhpmthwrWY5GytVP8G2pM1NYNaTkBZOLPMgR8jcEx6BsEjeevOS5V60v2npjk87UZKO2t4WT5mxK7ocJp3N61yATdImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAm_Ikvgjx3pa0KzSJvWmHgPr9k1iW_TLMGdcZC9Pj_g1fQeB0Ponkm88X1epJGW8YRPiGiClrQ3I13NOBAGJIyYrQ8ErHp1lyd7m_mL11W4mWzscpRVDdDAtwvZAZyVpZtQxuD_gIvawxw9of4GDwFbVC8V8xIdNXcnxhcWdq4RsjJHmzifQU0yj--scRhqqcu4cMKpKVtPZExWhs-JCG4NDqG8IwtwrumtSXlHZI1dbFhbfLijRedic9lvQEqJ6jg_XKeiGb93GvepI7oTbc9cz0RMjZaB03b086hx1Sm_oegGYMW5YzpCSrionN8qnAikqo_CiMpr_osmz9m87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbTWUsMBqmQyJZx3VyHt4wqce_PO6pwAqqj9Mm64U1AXzTGVZcqk8fUHk7dxr_7B7jgqY8834uCpK_k7WL8PCKjnIAPbygcmDs-1TYMi38qp-z5LTI8sBSKZtVS_5LA5u33kbKs5GE7mNeFTZmA3flUPgNh5XiRZ6UCI3IZ1JZfBsc4Sd-JKUNwuzTGKwIt6OWe785KNUlRDpmDwPHcLg6TvOenXKt8Fx5XeZTEyqF8QY31hBT5zHGKaLUZPGDzApha_0z3oUwYKm-b-4DMF3t1NI5qTvxPp2P99ij9Am_HxLP1y9TpPpPsvcByMGTf6Bk71vLduXvXK2Y-iU4Jf0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=u07RNDHyR1nGN30jC42qQFtjzI9tFQB3BeGykw1rdVLx_Wa5ApVz3BQTdeBio-1WKRpq74SvIVg30qFcvrieK93it_eqnxQcSyToxnKn3ADEfO9rhTm7JuqJcF1P3nT7mYnnyhaFT9Dcv9OYywxt_lpwRPjDB8kv7CKn3GDnL5JtpZ9x4oCZRPTt7enGmbbEbY8DV6ZkkF_6OyfBmZ7eGbWZW0ZjrPJgpOAon0P6UIYB7F9axt-ftNY5vnPTYTIvKkZ4zjDMPDXA2VUyWpxEXwzwfhkBKa23WyXAIH7zGiXwgP0rChkjzmKpYJ4GeGDTjmPnsdD9DEseulc4dU0buw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=u07RNDHyR1nGN30jC42qQFtjzI9tFQB3BeGykw1rdVLx_Wa5ApVz3BQTdeBio-1WKRpq74SvIVg30qFcvrieK93it_eqnxQcSyToxnKn3ADEfO9rhTm7JuqJcF1P3nT7mYnnyhaFT9Dcv9OYywxt_lpwRPjDB8kv7CKn3GDnL5JtpZ9x4oCZRPTt7enGmbbEbY8DV6ZkkF_6OyfBmZ7eGbWZW0ZjrPJgpOAon0P6UIYB7F9axt-ftNY5vnPTYTIvKkZ4zjDMPDXA2VUyWpxEXwzwfhkBKa23WyXAIH7zGiXwgP0rChkjzmKpYJ4GeGDTjmPnsdD9DEseulc4dU0buw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eG_gTBl_U3nrWOS0nX2XvDxgQtz_1hYsLjq-f9bUpe4CuJ0WQs4Js_8e-N1mHKeZsPq-pINaAKPZd8EEbm1Faj4jP0eSlrzPkzxwiUrDFM4J5OTZc_dLlD97H1IeTQUoNGoSGiIyH6_RhN8D3wzX6UBdVIwEbYq9bgac4LmPZjVtQdWGihzSs5xvJLakJW6GpH4ov79wFHZnbwU81YkzA_PYTuex_uNJhmebZrJuZjhWBqpiLrHMMl8jhLK8KjcyfKZvxiwcLFUAQIUkayfwaYfig8Njr-mrrL3iBby0RL9Z8m3KsWOesk3iqRklarp7rc6meI7543Mh7rfmAbAMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ukf4vIxgxaT40qSshc3Vv2j8W0WW4AvONCUwJ6dgk5XK-2boSHTF1uqnDDx98_z7bIEQU2-TM3EpM6K8XkcT-kNQAb8JbSu5ayuvy7tGduKkr0NG3AZ-7zMAjmolFnlLbB7ZuVs79rZ_xQim3SbgIN1usrCTy4QrVqCuTiM5IGkLFddfMGqWNRzd0IZssAc2ZwHSOa8HbWQqXX2POBy0DQsNEEwxR3qTj-edsRepLBykxzqFCfgSczs453H6F4Zz0qBtS5L6df1rCcU6wRoKLf_TbGR5Uo7wwT475UQrYyPTwSLiT4Z2aGjrkdCyZ0TO_6fuL5uyzfIr7qxS9N2qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWFQxR48b6W5aefICTL_jE_7X81S_uc3xDvnkN7ujX00oTizhY5vdZ8xb1eAYL0iWe11nneO-WQ6s0mUbFM7ZW-g_bq8vZ9wDWItJxnxNSyjAEssHSE57LipCDKM6dOBHzFfGrSA3ZYrwYz_ysnr1quztPn3h6aL8JAnrcdpcXHGFhtdYjywtsaCO3dbij9zKr_g_POsrjtuL3azUg73jDeh0z7JsWuiyqiFDp5N3FuZsU0cNhkGHrC3eMqrWvAlZk0wzUBF7Ov4euk8N7UYy_Fr9ct3CpY0ZKX_dwE3p_XHDDxjkAO4o-NCzDaP0Pzjz6e2X9o77SVO7qLE5WzGbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=H2javKTqsTQlMZyUjzEWJlc6RWvqBRObf90NWJ10hdQzeTTOFPDZVoVFPoVrXo_edu8xH_-GhJao1EVNc_vo0PUrZKGXNOe-TyW2cdWOnWTSJD5nRcioeFCSacMFrTK8dGeB_gSjytJI4YrgrwAEHpzWFS-Oo-Esegjz-OuCM0wrQFYDTtJ9ROSOWQyHsWDp57ClCdh6A1M0f5N7R-KTifcYkQFa0R3STk07zPkNfmQ1atOH0FgEXNm0jNeNBOy_PtEM7dM3qitfLzQ83EMgil0bI1Tcd3EDzAb-dr_-LUJwldrp4wnF9KJiVeRML1tXlx6bOT5gUauEkh9b3Y_45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=H2javKTqsTQlMZyUjzEWJlc6RWvqBRObf90NWJ10hdQzeTTOFPDZVoVFPoVrXo_edu8xH_-GhJao1EVNc_vo0PUrZKGXNOe-TyW2cdWOnWTSJD5nRcioeFCSacMFrTK8dGeB_gSjytJI4YrgrwAEHpzWFS-Oo-Esegjz-OuCM0wrQFYDTtJ9ROSOWQyHsWDp57ClCdh6A1M0f5N7R-KTifcYkQFa0R3STk07zPkNfmQ1atOH0FgEXNm0jNeNBOy_PtEM7dM3qitfLzQ83EMgil0bI1Tcd3EDzAb-dr_-LUJwldrp4wnF9KJiVeRML1tXlx6bOT5gUauEkh9b3Y_45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=L4sjg5zaZOodae4obScl-3z1kBLEDwvqyN1Zo-fO6hpCFxkpcwsvaQvJ9VHpULYPZZKBApxyaOxqDZtK0MoiFtYNzyNozuvXz4r4nnpeS8n3Vyco7NUrDFEIJJYiAD5h_b54zE40oNm1prDcgWDtwSiYN1Z5OD56GpeFRXmettem7PWCWhiv1Jqo7KpNSAK6IZV8lW_XE67ZhetsUB5I7ubWZz8_bUzoUIzMLahzUcist6MtKoduDsVzugp_gtfGCW4aI7OzqyNC__HB6Fg3cqi45PSbSiBqsBwrjTlemI_joBuvUGkHoKwv6InA_yHgZvAd0VLPXNCyA2SiuGkSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=L4sjg5zaZOodae4obScl-3z1kBLEDwvqyN1Zo-fO6hpCFxkpcwsvaQvJ9VHpULYPZZKBApxyaOxqDZtK0MoiFtYNzyNozuvXz4r4nnpeS8n3Vyco7NUrDFEIJJYiAD5h_b54zE40oNm1prDcgWDtwSiYN1Z5OD56GpeFRXmettem7PWCWhiv1Jqo7KpNSAK6IZV8lW_XE67ZhetsUB5I7ubWZz8_bUzoUIzMLahzUcist6MtKoduDsVzugp_gtfGCW4aI7OzqyNC__HB6Fg3cqi45PSbSiBqsBwrjTlemI_joBuvUGkHoKwv6InA_yHgZvAd0VLPXNCyA2SiuGkSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=ZGTqxvgCBrlCZELnRunuTyts0B1EndtSDuJS2EYMS5wG-RKTnA6SUcjmLTC4mDrsQB3cf5YZFdLVOeGl7SVn0tXf669125EresKCEnL5dPhH3gXW20K2zYT-qgyVpeBmb20A3BNBG7_Qi76fafIh1pjzLcJRN_nBz_1LA85cfX_BJIKHJgIE2R7vMwlQ_zd5w2C3-uhIp9aL31Sxerio76qcf-aUyWkpKw2-3zlw60lRIwtG-uFfnDyYCWCWZUh71Jl-8Hie9zad4B3xs-ZPzLx7if1cbZvwl03Z7bs2nhMxsDdM_9WJIP2NC550wGXQL9jxCoIMPSVspn2tKLq8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=ZGTqxvgCBrlCZELnRunuTyts0B1EndtSDuJS2EYMS5wG-RKTnA6SUcjmLTC4mDrsQB3cf5YZFdLVOeGl7SVn0tXf669125EresKCEnL5dPhH3gXW20K2zYT-qgyVpeBmb20A3BNBG7_Qi76fafIh1pjzLcJRN_nBz_1LA85cfX_BJIKHJgIE2R7vMwlQ_zd5w2C3-uhIp9aL31Sxerio76qcf-aUyWkpKw2-3zlw60lRIwtG-uFfnDyYCWCWZUh71Jl-8Hie9zad4B3xs-ZPzLx7if1cbZvwl03Z7bs2nhMxsDdM_9WJIP2NC550wGXQL9jxCoIMPSVspn2tKLq8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=Ib9ADgwdQaLDvWg6DhLzaaSaqoguHB7ArQOdOdlGic4ka9ipbGU6mniCpUeSLn2KgamGO4B6JH2dzcTpV6OtkvKQRcSy9tYUab1in3HgJoWo5a8GYDUGPX_uQX3Of40Yx1TT55XQTyYOmZ0skDWWmVyQ2riutLgcDpLi25ih_W6aArjaJaQ8a3fMKnZ80S_c6FRpv5fZK41enGgp1OKMpHe_9wUigKrSchAhTLnczLtswf6LZ9dx3Uiq1v3wXOsk5vnjghn0nXERrrynZuwbyO0HxeNcKs4IhffogU_s8AFcBm3BW2YHGqXbV6qLahE36drLzL9lqzOPMXaRoRveBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=Ib9ADgwdQaLDvWg6DhLzaaSaqoguHB7ArQOdOdlGic4ka9ipbGU6mniCpUeSLn2KgamGO4B6JH2dzcTpV6OtkvKQRcSy9tYUab1in3HgJoWo5a8GYDUGPX_uQX3Of40Yx1TT55XQTyYOmZ0skDWWmVyQ2riutLgcDpLi25ih_W6aArjaJaQ8a3fMKnZ80S_c6FRpv5fZK41enGgp1OKMpHe_9wUigKrSchAhTLnczLtswf6LZ9dx3Uiq1v3wXOsk5vnjghn0nXERrrynZuwbyO0HxeNcKs4IhffogU_s8AFcBm3BW2YHGqXbV6qLahE36drLzL9lqzOPMXaRoRveBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=pBLdRKzeD604QM8uLxro81xRXn1bnIL_Rjr-NSDi5YYC8595lMJTV7nOPrbJ0WCze2RBnmCS8SctoJ4NUuJ7UTnlitNsAlVRPWqNBrtDQdNge3MFRyecznUJWDuAmo9l2SfxT_k-iEjHUq4DYG7k1TPIpcI22CZyMTkWugGv9mVkdiw-XuKWtxYaMCe3hDpAfbv5L9uwDLASOLbdSVVgX8DOM8cPwhl3-geO1J8sdKiTq_D_qu2J0U1xGpIZC6b2IKbJiAeWLkGi6Ug8DcRPhbg89HDgOhBLe0f5z0gzx4Tg24LTIhbIu9vdwEarUKMg6esWT_Urqo86L2t20dSdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=pBLdRKzeD604QM8uLxro81xRXn1bnIL_Rjr-NSDi5YYC8595lMJTV7nOPrbJ0WCze2RBnmCS8SctoJ4NUuJ7UTnlitNsAlVRPWqNBrtDQdNge3MFRyecznUJWDuAmo9l2SfxT_k-iEjHUq4DYG7k1TPIpcI22CZyMTkWugGv9mVkdiw-XuKWtxYaMCe3hDpAfbv5L9uwDLASOLbdSVVgX8DOM8cPwhl3-geO1J8sdKiTq_D_qu2J0U1xGpIZC6b2IKbJiAeWLkGi6Ug8DcRPhbg89HDgOhBLe0f5z0gzx4Tg24LTIhbIu9vdwEarUKMg6esWT_Urqo86L2t20dSdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npzCpXJAPZtzBqzn8o0R9M1EqJlA6o_xTYqxjMzM_IvS79mtfGqy2OuR8OMYIPGzxcj4TG6pvwG3b4GXKaramtWXygtVKjtkaX7wEmfsF-Dy0q1gy77jzKDMZqzaZ5F8BPgXi8520bBExQ7xOJB6zjd8b3WpsiPfVoUSqM4dKqov6iqD0cnagjxZKUpIqrPjsmXD9F1EVFd5phjMgjjbau0X5bskpnDTG-wGLUmf4sg11z1wSH9ucJvOUpg1sCEi_-pVu1nNEQ93BN4qW1C3CJwCsVQXNklWNTzaXw0Kmg7uV2JljiX0FWrA1wnhiwlwH8HoBGj3hla7MPEYGB_I4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oABbBUezhS6MRNWAQV7CjBuSLjlRy_VolRB8bubIa7HRwDGHcWz3IUarFKLqH3VaD5ntiPgcTKdks5pUeZPFVFPaWsu1-DgSRTWZiNX85hUmqAYFru5WHmE53x_U31tJp_1NaI-vUnU9DhxvufeG07K0dNjtrwvSq_DcLeGi6R6hmnwMGj3yUd3bHgu1vFFc6cMZ0i2ZYAMi6BASv_YPe_J3M4qdCa-_8wwS5p6eWMm-Drcf7vjVELkInr9ciLoOoCEU8Jggg00uj3JlBZfG0IXJk8rVSNyOC8v5S_ZIbeXCDf42zFLccT2ugYrS4g9muTCkpQ4AxRi-MmOy-ULotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=MTZA9IeOcm3cAFP1hAG_27LRHkBDTYa48N4V2NseyTwidyqf_PQW6kb6FI-oPzDfY7nvCqw9BuN8PG3m5YcuyaGO3Jz-jexpg_-SfH1DO3R_csFU2RfoStk0DAOZ1TZe6Z254zFh1Fi3UYdkHXSJMKRO_XuzlOPZn4izbH397aBQC7NQG39EUUdjCYg0eNKq33FPD5sqRFLk0j0ULn53FuNd9urR62JpuMrJXrmU1Q0ozpAHZ96vIRv73dwjc0OAwWr1YaMsUYZDc3WNJnHpSEXSDO0HB43NY1KE-_QK10XzRqKcHHDX2UzYGKZw8tcfhO8y_npv9kUzn423CC6efg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=MTZA9IeOcm3cAFP1hAG_27LRHkBDTYa48N4V2NseyTwidyqf_PQW6kb6FI-oPzDfY7nvCqw9BuN8PG3m5YcuyaGO3Jz-jexpg_-SfH1DO3R_csFU2RfoStk0DAOZ1TZe6Z254zFh1Fi3UYdkHXSJMKRO_XuzlOPZn4izbH397aBQC7NQG39EUUdjCYg0eNKq33FPD5sqRFLk0j0ULn53FuNd9urR62JpuMrJXrmU1Q0ozpAHZ96vIRv73dwjc0OAwWr1YaMsUYZDc3WNJnHpSEXSDO0HB43NY1KE-_QK10XzRqKcHHDX2UzYGKZw8tcfhO8y_npv9kUzn423CC6efg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amuwtEL0CuAOkGuG5iRvB9u_FOEHCy86D5X-SHYTluRvE7k6ShfPoaeCuOTCVNyOdQz7-3U1vVdkLeiQi5EeKOwqM5KGc737qfxF62vCMEEl6C4jy4zksgzt6tF3AIX91HVFo4jcuh21l0sP-8J_Xm6r253NThEOK-NnFJ0ATU0KbOd9wNMDFH-Os73runDN35zUn-FU5bVEdLwcbAR5cVIYzEfZ9u8bT3uNPtPUS0HHxUovuBE8e6gOSH-obMiFbEWMKsXIw1NQuxC0UPoEraZ62M-jo_2_9Rn8L656TFNJHpQzZFNpN6xWMrqafjTSHLKVl1E-XbUnwIkw8ocgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_gu635I7_IDaVhw2Ww5m0Wehqh7pmvys3Sj4m8Dw7bjkJIGhAaioEN_NAk6OQY1jG2gQxY1_uAadHAIK_5vNMJOK-7bjRh8bSe2xzS3Qw65QglYWNxVH8q8dRrpQ-2EJcYkm5_htoe115y6x2sV7a9r1GrvtRTTkaLcO1pDY1yB9m67ESdrHfAFJchIUQ5xprY5BlUffY3prZxXr1cPoEUH3AUoYOgGUEupvW2EtJPmAYf16JsHIP554pbDVXsWTR48S05K4siwwcGo1ZxRjOXPOHaCb3uKvTohJcf2awpsbDAQAHZO1peC2kk4geAEzt0dob00ppiq0XeYoVneEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNaAj1oluz6tL_RSdZ-AFq3iaB_RC8_vrPN7MfDRbshjBuXesE7_YD0dtGXIstciL41uOUTEuN7dBamF2msdga0W-14dvY_MKw2czMCUd7eVhGG5h0cTsah0BMBVfsNxQOGGMP4J3IxZqrdzItGAkJXaVjq-3uu15Y8SUFzWiDItA3H1PKqUiXyjnKt3f6wGw3ueSyG_u-JwHTffByUNGq0t33u1OmO0rplEMklPb1gbbAuIv0s4AJlnYpOMdQxkwMIo31atsus4Fa5v0SF1HDOok0T3HlnZtEI35L8929x31Se0MW70WHRkWAcJp-qMIzQLkakqiUol8j7IW95tXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTNqhXibxohfR_4cR3iuWeLRMX8_7K66zvvhZHj_QO7LgtRNLpZ1O2OPmTSR4qAkcHSjWahYIQhulmpaYJwM8QSt4sZOfjaSXhw2cEhdZu5ZGc_Li5h2puZdnSrDaqbrQER9orgmC4V8wrGM06f2TzvRpSYDuXVxfub9lPzaF1jKLf54Z3vAGlXBFshoiKmI_a0rO1UZjZPT7FP8p8W053mBlzkFyswqyhi9PVH45_tej4-4tfTzxiDsCI02DkRB8WIa0pnXLuxAbxi4wxwFb1_jkUNSpuVD3XrcIqfRybCHAdTAsmVgnTBWonzX5ZzR2v1FV9BWkXpnLE_6rni4oQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=YEl1mPRMKueUHLmZvqVn4ayiDZe2RzJcYJD0KXlXNUZeAuK4BtZmm_IjFCCDM4MEuWGtllDnv7Zzfkag6klmTeby5xN1MxePEl4wYio0TnO8mv3Y8S9s8s1ZMaIlSY83pP_k2UWA5mCkCsWFz3OADj2r_r9QhnJHSrOID-2wbxEVEJSnQgQ4OJbgJpfDlC704xnZS6ZPNo_X_KTy1-LgaRGsSOUnBgryM6CmOkQZsGb8fYB4tucveOd93QgLbqUa3Zkd5LdJYkIQkaAJNTyq1w2PnRhXTg_KxZGub16HgLN02C0S9vi7dwDVHlTTRMwrX9QjOtHNH5O7zv1Yhwc1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=YEl1mPRMKueUHLmZvqVn4ayiDZe2RzJcYJD0KXlXNUZeAuK4BtZmm_IjFCCDM4MEuWGtllDnv7Zzfkag6klmTeby5xN1MxePEl4wYio0TnO8mv3Y8S9s8s1ZMaIlSY83pP_k2UWA5mCkCsWFz3OADj2r_r9QhnJHSrOID-2wbxEVEJSnQgQ4OJbgJpfDlC704xnZS6ZPNo_X_KTy1-LgaRGsSOUnBgryM6CmOkQZsGb8fYB4tucveOd93QgLbqUa3Zkd5LdJYkIQkaAJNTyq1w2PnRhXTg_KxZGub16HgLN02C0S9vi7dwDVHlTTRMwrX9QjOtHNH5O7zv1Yhwc1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDyXmEuonr_sp_c2oijmbInp1AoHHIIMGXUCJRdC-1LneJSiGV9ORdLPAGw-9dOM9DHQD8lmn2l0R9WLtXrq2tOYP4uytNZtQ-UqOPo8z51fdaSWK-A_6QgSIg3a3Z3YZdrztkZhfL9Ei-JMA2qvOzLTq2lvSi__NKSwq6siUagrkKPBY7Q0RSV4p3Agzr7gdO0S8KHYAIsr1Hd5s2_ysDrIiwP9GafeisFKZpgDst4Bs9CgpEpi2rLXNJvMhbmDKZ6rwJhBzNMnLJGkXdgF_TVPRHUvfG4ca7QmUcBP5iEH4AI-KY8QN_kmTwGuI-j4F55J2yRM8aTeC2NDBlDSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxTeWdzEkaWpe_oao3GAj-F3jFgT4BxgC94UyoeUmMl2VSV81MXR9agZvOZ1hdZelQxdu70F0P8W18I6hFIhZUK5QQjWlRZNKozDoNBy5iMuQhYsSD2VGt-hsf6mvQd4XqHbRA-EBT_Qvjl8jrnN0IkD0TYcj6OyVBcJwJFyRA5ztc2PFJWNs0cnD9k5EjouVRwjIbU6JN-cikDYLdma6vfjrgEgVgvPXmvMiPtyO7uA5lKONJ8Qwa0HrFK8M2pjQCASQRS4QY4vSXB1G33vQBz_0Wcy5GiRBHhOLWgc4i6we-8Z7mBJvIE6qD4OJonU_nkevJZs8wB8P5Z0Xd5Xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
