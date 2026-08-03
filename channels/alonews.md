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
<img src="https://cdn4.telesco.pe/file/DMbufwhNWVs3kY7FiJwsPL0X2BHS37_PSpRVEIegdQ4-vah5PTwd60Jo7BJUM3kOUUvZWwzEWfsehRi1krhM2UhcbM7YAvVuJPLNaXoiBA36D6J_GzTFJVkyKkxNpK-ECQnvBRMAxU9MbesR4Y6SjMUBebwVj7ADjPL12um68FQ3u0p6bpO3dcCfddelBo-MHKn_fea__-HMTgvbR5mTbauUwb3lgulNlcrFRxOehSqQdVshzhTI3gRlyvyYv079jyPZxdeYvw4nPI0EAdgEt9DMhv14Fq0iL1uMaan-xytx3QW56RiQxyi5cjJN3I5PsNge08GR41_1PksoyvtJ9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 989K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVcWO-geff3hHWWbExUEdkD7cRlIAsEFoFy9Fe9_DlNPcWUbYe4y2D9wA9-iv9Th5LNmymVPZYCwkKFRCY4ISRDX0z5bqtreVW9Sv1N5ey-nfIg5MtIu0QO-r9isWcX7bOJL8mKjebI-VtfIkpkCp2mG02r9ILyrg2y9gCAqdS_xpW5nbgXJmJ3LD7J1Rh2x-26Qgz364VMt-_v2QRH_fdNUcKP5PKUrMNTwRk55CcMNSfmypXQwmFiyscpqYQHX1IUWHYjalE9sq0GfaYhNxKnvXY1skUHN-LIYysw3rFMbybY46heG2ZVO41muPmwZpX2yn8rJkkQNdHqQL0Xq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/139607" target="_blank">📅 15:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3b661bd6.mp4?token=XvH_2RI_s7qAv_-TINP0k2Ad1fQNr5e9zrArXwunqyphlTNJ7icuwDaHJded4UXjBrkN8eZOWQ7_iisKdLWkTN1kW8CwsjIysgRXWDphIpkuu9AiWsc4D8_ikc2v9NPIFT20dNh9Mqyj_eMjFfjO7rd9tDeVOJhu5m2b9eHW_nHeyOXI-wj7_0jYtlkZ_8Mo7RiTqYieheOt1J9ZT7co-dFbRCPuI8BHy5qG0vaL3q9H-oACBcBYPOQLXQHrsd51vOKVdg7DWv3NKiWexsJenwXgiFMb_1oU5pJS7rKpXYIwz9d-UIHZIuYIzcUa2RImxWtulV9pAOFJxfFElov2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3b661bd6.mp4?token=XvH_2RI_s7qAv_-TINP0k2Ad1fQNr5e9zrArXwunqyphlTNJ7icuwDaHJded4UXjBrkN8eZOWQ7_iisKdLWkTN1kW8CwsjIysgRXWDphIpkuu9AiWsc4D8_ikc2v9NPIFT20dNh9Mqyj_eMjFfjO7rd9tDeVOJhu5m2b9eHW_nHeyOXI-wj7_0jYtlkZ_8Mo7RiTqYieheOt1J9ZT7co-dFbRCPuI8BHy5qG0vaL3q9H-oACBcBYPOQLXQHrsd51vOKVdg7DWv3NKiWexsJenwXgiFMb_1oU5pJS7rKpXYIwz9d-UIHZIuYIzcUa2RImxWtulV9pAOFJxfFElov2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طی سرکوب اغتشاش عده‌ای از طرفداران جمهوری اسلامی مقابل موکب آیت الله سید صادق شیرازی در عراق، 140 نفر بازداشت و 54 نفر مجروح شدن
🔴
حسین ستوده مداح حکومتی لیدر این جریان بوده و سعی داشته امام حسین رو هم سیاسی کنه اما کتک خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/139606" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362a14235f.mp4?token=ay8ok6kqUMJvT3uI82indeXeooKD2-r-qVVVHCyGqNUmA0bzlJphRjSKwiXrabuxpoyRkisbIW6JIbhfvs2zIT8XN8ZvkTYhrRxDy4Oo8D6PEzvxOmmKDB38x4jexEf7Rf88kb12HPkLHsLxt5dJbE-r8AcFk1lJ0ju_N-A2oP3J3RsAGNbV4jTfxMswR-TuPdI2gB9E3ewviqh6z7Paw5JOE91v-ducR4wIsVLGAnZ5SOSBbxrkdtfb3AsqjFlsX_-s0BUUZioceDkRlITOUUl1uFu_hnMgMI45HqSfBaqkuEdminRDbNf_uAb21TKLC4-EoEMYqOsA-JddxDihfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362a14235f.mp4?token=ay8ok6kqUMJvT3uI82indeXeooKD2-r-qVVVHCyGqNUmA0bzlJphRjSKwiXrabuxpoyRkisbIW6JIbhfvs2zIT8XN8ZvkTYhrRxDy4Oo8D6PEzvxOmmKDB38x4jexEf7Rf88kb12HPkLHsLxt5dJbE-r8AcFk1lJ0ju_N-A2oP3J3RsAGNbV4jTfxMswR-TuPdI2gB9E3ewviqh6z7Paw5JOE91v-ducR4wIsVLGAnZ5SOSBbxrkdtfb3AsqjFlsX_-s0BUUZioceDkRlITOUUl1uFu_hnMgMI45HqSfBaqkuEdminRDbNf_uAb21TKLC4-EoEMYqOsA-JddxDihfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی پر بازدید از زیارت کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/139605" target="_blank">📅 15:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olst-WB3XK3SKr_wtGWPtriLpbaegJ4pyFK1womdVFEapC3j9vYhAOeshepyUYPWtJhioeOa3A3kQZICP1lsDGLBGs08gn0hikN-0lo6rGmzzwFyluc9G7FWlPSwFxvhZncgzKv3R0BmGdH5_uFxQ2PCmBSdZfD5B0iSNHcmpSWWi6jojoImxpgfKZvFlcghHmwibgs_Llsij0a435MoMLzy9fg-86bnIZpeWti0ieqi21AyOlcX8KQoOzJlGVRMuTAVxI4VsXZEeuxcmb44NFXW-P0jbdwnnCeqz--MBYUO38svqtLyRMLWp_Lx4ONGw6naDRCnresF2bN3PqQYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی: اینکه میبینم یه عده تروریست اعدام میشن برام از خوردن عسل شیرین‌تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/139604" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز، با اعلامیه‌ای که در تلویزیون پخش شد، سردرگمی ایجاد کرد. او قصد داشت ژنرال آوی بلوت، فرمانده ستاد مرکزی نیروهای دفاعی اسرائیل (IDF)، را با ژنرال ددو بار کالیفا جایگزین کند و بلوت را به اتخاذ مواضع بیش از حد تند علیه شهروندان یهودی مهاجر و تضعیف سیاست‌های دولت متهم کرد.
🔴
نیروهای دفاعی اسرائیل (IDF) به سرعت به این خبر واکنش نشان دادند و اعلام کردند که این اقدام بدون هماهنگی با رئیس ستاد مشترک، ژنرال ایال زامیر، انجام شده است و بلوت در سمت خود باقی خواهد ماند، زیرا وزیر دفاع اختیار قانونی برای اخراج یک‌جانبه افسران ارشد ارتش را ندارد.
🔴
کاتز بعداً تلاش کرد تا از این رسوایی فرار کند و ادعا کرد که او درخواست اخراج بلوت را مطرح نکرده است و هر ادعایی مبنی بر خلاف این، "یک دروغ کامل" و "بخشی از یک کمپین سیاسی است که علیه دولت سازماندهی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139603" target="_blank">📅 15:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3b6f35fd.mp4?token=QbSFUVPvzXOUcFEtG-Kg2z8307XZ21kXw8erJGSFvPoWGQr8pMLuPg9pyaWho2mW0xci3wX8oaowsVdkV18Ic7FTUQ0e-jdtdPoVEhnNzUyRWiF3vV_ZQXeCmL0jIs6JwPbbSA_34_qoC_ySggn0AclUM5pnwcuG6sxkkxhvlZ_FLV4l1YaFamwWKy_uzeI_XVNkNg5mnt46pK2ctDBk92nQMyczfEcUU_C5pC3oTV0YdZsjgo0xNuN2WxMIwWff9Ly9O7JEwJXPKKz7LD3_Ab3pintdsJJ6wCGwjXcLWbreWc-_FvCtZXWJdoLcYz1KNA3GSAcwNjZNuEINcJysVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3b6f35fd.mp4?token=QbSFUVPvzXOUcFEtG-Kg2z8307XZ21kXw8erJGSFvPoWGQr8pMLuPg9pyaWho2mW0xci3wX8oaowsVdkV18Ic7FTUQ0e-jdtdPoVEhnNzUyRWiF3vV_ZQXeCmL0jIs6JwPbbSA_34_qoC_ySggn0AclUM5pnwcuG6sxkkxhvlZ_FLV4l1YaFamwWKy_uzeI_XVNkNg5mnt46pK2ctDBk92nQMyczfEcUU_C5pC3oTV0YdZsjgo0xNuN2WxMIwWff9Ly9O7JEwJXPKKz7LD3_Ab3pintdsJJ6wCGwjXcLWbreWc-_FvCtZXWJdoLcYz1KNA3GSAcwNjZNuEINcJysVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار بارزانی با الجولانی
🔴
نیچروان بارزانی رئیس منطقه کردستان عراق به دمشق سفر و رئیس شورشیان سوری ابو محمد الجولانی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139602" target="_blank">📅 14:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ادارات و بانک‌های قم چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/139601" target="_blank">📅 14:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3c9d3e6e.mp4?token=e_p9aGTZNckRWbPOWFwzMgO1v6EEwnv6P6wWrzWcsEBAGQpXBeaeY72n6dOAXbQoUJ8HP4Ms5EIEIpYFR2dJiZVIrM1DaI7FnMxu3DSXi6ljmoZ7LTXH2hFnPZG4WpnHtBTjbuYMuXDb0aeHMAg6tcrk5P8WCMCWJdKtRHoOiuwEh3FuMrmsE-592zOKKgP2f2kNw_ZUvn4ZtP5HSwbpmCjxJSKljkAfa8bH2eTVI0vcU8ZGgxBaDAQeXoAdcjQekAldgjRJrBFZzKEes6S5oj9C168NnKVm9J3SFFdpEYHzGXTnK8mbfz2Ix87IJoPm5oKlameAT69zhKe0_YFmdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3c9d3e6e.mp4?token=e_p9aGTZNckRWbPOWFwzMgO1v6EEwnv6P6wWrzWcsEBAGQpXBeaeY72n6dOAXbQoUJ8HP4Ms5EIEIpYFR2dJiZVIrM1DaI7FnMxu3DSXi6ljmoZ7LTXH2hFnPZG4WpnHtBTjbuYMuXDb0aeHMAg6tcrk5P8WCMCWJdKtRHoOiuwEh3FuMrmsE-592zOKKgP2f2kNw_ZUvn4ZtP5HSwbpmCjxJSKljkAfa8bH2eTVI0vcU8ZGgxBaDAQeXoAdcjQekAldgjRJrBFZzKEes6S5oj9C168NnKVm9J3SFFdpEYHzGXTnK8mbfz2Ix87IJoPm5oKlameAT69zhKe0_YFmdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین، اعلام کرد که رستم اومروف به عنوان رئیس سازمان اطلاعات خارجی اوکراین منصوب خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139600" target="_blank">📅 14:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
منابع العربیه: نیکولای ملادینوف، مدیر شورای صلح، برای بررسی اجرای توافق غزه وارد اسرائیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/139599" target="_blank">📅 14:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139598">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شبکه سراسری برق کوبا فروپاشید و برق در سراسر کوبا به دلیل نبود سوخت به صورت کامل قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/139598" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هلی‌برن نیروهای ایرانی در کردستان عراق
🔴
مشاور فرمانده کل ارتش ایران:
نیروهای ویژه ما، 14 عملیات زمینی در شهرهای سلیمانیه و اربیل علیه گروه‌های مسلح مخالف انجام دادند. در این عملیات، تعدادی از افراد این گروه‌ها کشته و تعدادی دیگر دستگیر شدند. تیپ 23 نیز بدون هیچ‌گونه تلفات به پایگاه خود بازگشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/139597" target="_blank">📅 14:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ظریف: امضای یادداشت تفاهم، پنجره‌ای استثنایی را برای دیپلماسی گشوده ‌است
🔴
این فرصت زمان‌دار است؛ اگر ایران در بازه‌های زمانی تعیین شده به توافق نهایی نرسد، بهبود اقتصادی دشوار خواهد بود؛ احتمال حمله مجدد هم پس از انتخابات آمریکا، منتفی نیست
🔴
بسته ماندن طولانی تنگه هرمز، اجماع جهانی را حتی با همراهی چین، علیه ایران خواهد ساخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/139596" target="_blank">📅 14:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVcMLaqe6kkIhRW3J-gbxBltptpOt1_OP84iPFKdToHo8kPGzvyo5MFt4c7A0A94VFzoy4t5Fx8UXnibYAK006CR9QqtVCdq2y6tGjMnRPUXzqPBanyqMk_2NHw3tGhNBgWVa2wexUicrcyfdR9mzy2fSYRo5HTKAgzfnp8QRhmtkdh57eK8MbQpel-gjK8siHvNm1VkZcGnm-BPVXTmQZkPqNiLQo2gEq-eZk5cyyRBAzLkMPeZNHCDxSFLFHT_pvJ8683x_iCETfR6NugU7vCj01iARW_XrE1YHX6BQ6FPhyqto61yX08SpbhxHXai4XEMXc03C2aeBmbmq1sPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بستنی هم قسطی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139595" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRCJcDpFj61WKM_31drKBc6PPfcDXgQyNYYsE_ussbaiGWGnoYAFt8XUxj_sR47zXA0dRyFW4GTO3MaD8MRytmOcmAdVNIf3EPFs9rjjt828gbG7k8t3HXDB0UwhPpI5Lyq5VZvKm6r3Tcy0YLs5EqEdu4AJ2bTNnSTNcnj8INYD6fzfoMIPUymhwjFOp5r14i83gT_c0tqc4BXDfrltyBxwsFlwwn7i5LYKkufv8JYJTqLTcgSDQ-oF3vYp-H2mLpQD__oFb9y9-WI0J8Dgaa3ui2p0VFUvIPPIm_zjqBxhMiFVRpx4YNnpclxSMX32xOxF2feRmsASoNekpH-6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CBS در گزارشی نوشت با وجود آنکه دولت دونالد ترامپ خود را «شفاف‌ترین دولت» معرفی می‌کند، تاکنون جزئیات بسیار محدودی درباره جنگ با ایران منتشر شده است
🔴
این گزارش می‌افزاید اطلاعات اندکی درباره روند تصمیم‌گیری، ابعاد عملیات و ارزیابی نتایج این جنگ در اختیار افکار عمومی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139594" target="_blank">📅 14:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diJs0Bz18J9PvJWjrAyuZ4qDf1HhzWP0fOq4eS-LiUU909whLuuovd3FbZNj36FYi2RHl8DiQszH_qvejbVGNpaQBMzNkzYcPG4_a7Cbp_w3SOyAheoR_mYJlSI724tyRCLjic8hrxI8J5Y3_htV0pjskgzBbAXlzELOu4tLtkf0Jf1EkNg9dyZ1EV-V1kTB6Rq4iG8J5mGU2fSSvJjtC7zIaX0hlMoH5KaJOlWZLe25o5RDR-H0nZ3MQU-VByWP6siEc3Jg8gErRVCcTz_N3cuAoahc9tpXSs3FmtA6-Ye4jIdbER6p8ci0sa9q9ocpPGg4KsIVh8CdQ3a8JuGxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکورت هوایی آمریکا در تنگۀ هرمز
🔴
پایش داده‌های ناوبری هوایی نشان می‌دهد که هواپیماهای پشتیبانی نظامی آمریکا در خلیج‌فارس فعال شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/139593" target="_blank">📅 14:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سفارت آمریکا در بیروت اعلام کرد هنوز کار فنی گسترده‌ای برای تضمین امنیت غیرنظامیان در جنوب لبنان باقی مانده است. میان تدوین توافق لبنان و اسرائیل و اجرای آن تفاوت اساسی وجود دارد و شتاب‌زدگی در اجرای توافق می‌تواند جان غیرنظامیان را به خطر بیندازد. این سفارت خواستار اختصاص زمان کافی برای اجرای مؤثرتر مراحل آزمایشی بعدی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/139592" target="_blank">📅 14:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e8b5aa10.mp4?token=ujMf0OHM0cbQU1WAdv3D-e97j1JcWV899C90-8VQ_0sl-xrLOuKnKnWp3IFjLInobmtmaYLlI1Qo7_Dl2grwnmHFJzGv1SmKjquiu0qT1HiHQ0hgeEbegrfOQY8IqMG2ECD2bdeVgbnzFHRPSz1sIND5QJx9Ssk0XLjqZWnkVam0bP69L8NmUARxoCitymAieYEzD9v7-RU1-za3Z1U3_I0-iUmLIJ83zTEUtFkUSDlZUessf0xjNqGOf319toLdfOuKyK-fQc3B7xeLy7aTJuwL5lUflhttDJpSI9M8azmADB-AUOEpfWz64aGBrFVtyOVHhscVXLTfe4Yvpm0MqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e8b5aa10.mp4?token=ujMf0OHM0cbQU1WAdv3D-e97j1JcWV899C90-8VQ_0sl-xrLOuKnKnWp3IFjLInobmtmaYLlI1Qo7_Dl2grwnmHFJzGv1SmKjquiu0qT1HiHQ0hgeEbegrfOQY8IqMG2ECD2bdeVgbnzFHRPSz1sIND5QJx9Ssk0XLjqZWnkVam0bP69L8NmUARxoCitymAieYEzD9v7-RU1-za3Z1U3_I0-iUmLIJ83zTEUtFkUSDlZUessf0xjNqGOf319toLdfOuKyK-fQc3B7xeLy7aTJuwL5lUflhttDJpSI9M8azmADB-AUOEpfWz64aGBrFVtyOVHhscVXLTfe4Yvpm0MqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری اوکراینی به ساحلی در شهر گِلِندژیک روسیه اصابت کرد و ۴ نفر کشته و ۱۳ نفر مجروح شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/139591" target="_blank">📅 14:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بقائی سخنگوی وزارت خارجه:
در روزهای آینده نه میزبان هیأتی خارجی خواهیم بود و نه برنامه‌ای برای سفر هیأتی از ایران وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/139590" target="_blank">📅 14:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1c6e9f40.mp4?token=ufezGQNI2LvZ3eTfg7v6CGherS9h2Z3XIRa5l4J7dHQ8h9Drr3B9t1uzykv2hiAedpUtY3G-EjKQQkNd8Jq2h_4HRf-TxMRsAED-BzQUlkvyDIK7Q-rrLZlllNyeBxGPhwZR1sMKEpwNHsyspHN8NtSnj821KwdCSc1BJlFBUOWGn4TQZHHB1Nc9uXGIz9Vd6xvIQLvvw2ymsGlSE2CE8OJJGqAgaTT3b4JKarGiE-hPwquAjd0TAj9YE8TBhF1EH-NpgXZxa0cqsMU5qhk_fYK2iFK56-V5f9C1iZqKfa0We9aoE0GdncveYRPM6cioWSJBtRPBcQin604M87QNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1c6e9f40.mp4?token=ufezGQNI2LvZ3eTfg7v6CGherS9h2Z3XIRa5l4J7dHQ8h9Drr3B9t1uzykv2hiAedpUtY3G-EjKQQkNd8Jq2h_4HRf-TxMRsAED-BzQUlkvyDIK7Q-rrLZlllNyeBxGPhwZR1sMKEpwNHsyspHN8NtSnj821KwdCSc1BJlFBUOWGn4TQZHHB1Nc9uXGIz9Vd6xvIQLvvw2ymsGlSE2CE8OJJGqAgaTT3b4JKarGiE-hPwquAjd0TAj9YE8TBhF1EH-NpgXZxa0cqsMU5qhk_fYK2iFK56-V5f9C1iZqKfa0We9aoE0GdncveYRPM6cioWSJBtRPBcQin604M87QNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین به یه مرکز لجستیکی دیگه تو روسیه
🔴
اوکراین با پهپادهای انتحاری یک مرکز لجستیکی تو منطقه ولادیمیر روسیه رو هدف قرار داد
🔴
این مرکز که حدود ۱۷۰ هزار متر مربع مساحت داره، کاملاً آتیش گرفته و خسارتش می‌تونه بسیار سنگین باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/139587" target="_blank">📅 13:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osiZMV1WEeq4Yl9lBXCKl33WPvjkrSRb6hrnIWv9Zmt0O90-DYooFO7GtlnVOOlyy72fwhRg7FuU5nCrX17JEk8Kv4wrXzmp4C8-cVm6ScWBXglKb643D_qxkWJx3h4gdeQCMJ4kUGYKafaHpESiqkCki3PK5BMK8fCWDIshEKj394UyIaEF8yskJeS-9OZpDxOSIo5nzit42K26xRkIYx4hP9294Zi-us_WBFrdhGFVt7e8-hwIlk0i2uXJzTgtXUALKV2Iz9JH6lnjaDNKkKVkCuqNlvTOKyyf9Wl4QxC0wSTQsGprg2knct-ewuVH6L9w9sucJgnIkTSG2UP5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رده بندی باهوش ترین کشور ها آپدیت شد و مردم ایران تو جایگاه چهارم باهوش ترین مردم دنیا قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139586" target="_blank">📅 13:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فرماندار خوسف:  صبح امروز یک کارگر ۳۶ ساله در تونل معدن قلعه‌زری بین مینی‌لودر و واگن حمل مواد معدنی گرفتار شد و جان باخت.
🔴
هیچ انفجاری در معدن رخ نداده و اخبار منتشرشده در این‌باره صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139585" target="_blank">📅 13:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxTHFmJf1mqOP9EbIDtcc1qxLfTCpNauKIF0pUB9eFJ3TdcDy2ljV0bDZwwojlSCITKOEmD3sWsvVIpxhCC_JvGsxEzinZelS7UVtyvhWpiXtdvd2ixwXaaC8gQQx-E17c3Xae3Yk14WaF80ry8HR9W-mXvFEv_V3A3taAlWpDL9USjM4TrqMGIwMXuMabbATVrFRSUlZiR6ne3NliWVk6qt7OyOqQk0lNwsJyylY9NrTB4Aj1N1phLy9WYKBQc1kQnqeaDScArnKT_RgkP_CfPNvwk119ypNChxsvVrWDhabYWCsX92DVdYMnaOTDi9fySUde66mHLyPdobUnX-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر استراتژیک نفت آمریکا (SPR) هفته گذشته ۳.۷ میلیون بشکه دیگر کاهش یافت.
🔴
اکنون حجم این ذخایر به ۳۰۷ میلیون بشکه رسیده که کمترین سطح در ۴۳ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139584" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی، وارد نجف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139583" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBZAuDnDzeDtVz47ISFANODaxjI-ua9EMqHw-HIZbK5i6w-dzTnjG8yWbPfJ6Z5MX-g18TTO-qs3q2ETFz3DVmorGmTG_Ei_gMBA0dBUSU1o_QfmSQsN-MOgppXUOQ_azm_qcwmRFCMQfmsO8aOlBPbY3XEDUjlAWMOVXVKJQGGriWiw9EbZRpJ-qlJWNr4KR8IP3lynJXjCWHAjnRlhW5lqIUulFMiFE9ZYjjvXYkhN-3HaK_enPDAnwas9ZPmdAt-wv81Q-eSZOH4bYisGHfRVq3cuJo7m6rxKYamzXcqRM4aT7MJgizeIe3EUG_VrMDfLmB04PlQ7qL7ksF4xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
چجوری به آیندگان بگیم سمت راستی درجهت بقای رژیم حکومت اسلامی تلاش می‌کرد و سمت چپی در جهت آزادی، دموکراسی و جدایی دین از سیاست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139582" target="_blank">📅 13:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی صنعت آب: قطعی برنامه‌ریزی شده آب در دستور کار نیست/ وضعیت منابع آبی کشور به حالت «نرمال» بازگشته
🔴
استان‌هایی مانند تهران و قم، همچنان با کم بارشی مواجه هستند.
🔴
وضعیت آبی مشهد بسیار بحرانی است، به طوری که سد «دوستی» به عنوان منبع اصلی تأمین آب این کلان شهر، تنها ۳ درصد ذخیره دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/139581" target="_blank">📅 13:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مقام‌های اوکراینی، مدیران صنعت پهپاد و کارشناسان امنیت ملی نسبت به فرا رسیدن زمستانی بسیار دشوار ابراز نگرانی کرده‌اند.
🔴
به گزارش CNBC، نگرانی اصلی این است که حملات روسیه به زیرساخت‌های انرژی اوکراین در ماه‌های آینده، سخت‌ترین چالش کی‌یف از زمان آغاز جنگ را رقم بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/139580" target="_blank">📅 13:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=Uiexov0t93YpheNjjMCaktggZdO0x3j0-aJDsizzpobAW57nbGZikbNG-5z78BCToaJf3BO3lAv2JkIvaqGtZioHCQ4zJ9RDu54qXaUTGwW7jBYuKsxWNoorU8fW0kNfkYt6IiUgu3XmJ8rj2ulPHtda_BAWWF7NGPfwko8IxSv2semgL9NI-HI2rsSl1phteGoj5txUQLVhuLpwhYFtKrkR84uh_RsBQU2IHjjzxXl7fJCssR2V07R81V1ylK8NutwKvRAhi-qEOkT838ODswHIdXtiWLcetg0YmULT-BE9BJ_t2LMtc0zav7v2yEhyozNayOuR3ihZ00r2Y9AWEyEk6FN5XyrN5kkBe8Wxr9lg9WrEYUZQp1PIowLm3ARaF_SSFmvJPhe3rwqyLFNGikLe93xEuGmyw2tcvH9NPCNgegFppvVvMqfGsx9mYAppAmzo5JyBQzP1VXrCfU3fpl7AhaUqhjM_mbCkSnW4Z4slosULjprWLbJEeql2VIOJ-1xuyf8OiEXIrfTkh2Q506vl7jg91dafRdKS2IcZn7rwFOCjiYypfZaURI0jP_gS85OYxDgIUJRxnz07hmPQuyjJ1EYi72YaxEyOCT6pwIs91-vs_XlVi-VOmIVvFgR7P0bqK7GQqFc_nfhuJ3_3GsgafAHuq7qsd_erAT0IFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=Uiexov0t93YpheNjjMCaktggZdO0x3j0-aJDsizzpobAW57nbGZikbNG-5z78BCToaJf3BO3lAv2JkIvaqGtZioHCQ4zJ9RDu54qXaUTGwW7jBYuKsxWNoorU8fW0kNfkYt6IiUgu3XmJ8rj2ulPHtda_BAWWF7NGPfwko8IxSv2semgL9NI-HI2rsSl1phteGoj5txUQLVhuLpwhYFtKrkR84uh_RsBQU2IHjjzxXl7fJCssR2V07R81V1ylK8NutwKvRAhi-qEOkT838ODswHIdXtiWLcetg0YmULT-BE9BJ_t2LMtc0zav7v2yEhyozNayOuR3ihZ00r2Y9AWEyEk6FN5XyrN5kkBe8Wxr9lg9WrEYUZQp1PIowLm3ARaF_SSFmvJPhe3rwqyLFNGikLe93xEuGmyw2tcvH9NPCNgegFppvVvMqfGsx9mYAppAmzo5JyBQzP1VXrCfU3fpl7AhaUqhjM_mbCkSnW4Z4slosULjprWLbJEeql2VIOJ-1xuyf8OiEXIrfTkh2Q506vl7jg91dafRdKS2IcZn7rwFOCjiYypfZaURI0jP_gS85OYxDgIUJRxnz07hmPQuyjJ1EYi72YaxEyOCT6pwIs91-vs_XlVi-VOmIVvFgR7P0bqK7GQqFc_nfhuJ3_3GsgafAHuq7qsd_erAT0IFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: همه ۸۰ میلیون ایرانی حزب‌اللهی نیستند/ خانمی(دختر شهید سلیمانی) در صداوسیما گفت مملکت متعلق به حزب‌اللهی‌هاست و هر کس ناراحت است برود، در پاسخ به او گفتم شاه هم همین حرف‌ها را زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139579" target="_blank">📅 13:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خارجه ترکیه: حملات مرگبار و مداوم اسرائیل به غزه نشان می‌دهد که نتانیاهو قصدی برای برقراری صلح ندارد
🔴
تنها هدف نخست‌وزیر اسرائیل، جلوگیری از صلح و ثبات در منطقه است
🔴
نتانیاهو اقداماتی انجام می‌دهد که توازن شکننده منطقه را تضعیف و تلاش‌های ایالات متحده را تخریب می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/139578" target="_blank">📅 13:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خاویر بلاس، ستون نویس بلومبرگ، مدعی شد عراق عملاً برای هر بشکه نفت بین ۲۵ تا ۲۹ دلار مشوق پرداخت می‌کند تا شرکت‌های کشتیرانی ریسک بارگیری نفت از بنادر این کشور در خلیج فارس و انتقال آن را بپذیرند
🔴
به گفته او، سود بالقوه یک نفتکش غول‌پیکر (VLCC) از چنین محموله‌ای می‌تواند به حدود ۵۰ تا ۵۸ میلیون دلار برسد؛ البته پس از کسر هزینه‌ها و با در نظر گرفتن ریسک‌های امنیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139577" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تعطیلی ادارات و بانک‌های کرمانشاه در روز چهارشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139576" target="_blank">📅 13:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جان کندی، سناتور جمهوری‌خواه: توافق بد با ایران را نمی‌پذیریم، باید فشار حداکثری را حفظ کنیم؛ تحریم‌ها، محاصره و بمباران کوه کلنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139575" target="_blank">📅 13:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شاخص کل بورس تهران با رشد ۱۲۳ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۲۷۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139574" target="_blank">📅 13:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مجلس خبرگان: با توجه به حوادث اخیر، امضای رئیس جمهور آمریکا فاقد اعتبار است و نمی توان به او اعتماد کرد و امید به توافق با آمریکا راه به جایی نمی برد.
🔴
برای استیفای حقوق ملت ایران فقط باید به نظرات آیت الله مجتبی خامنه‌ای عمل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139573" target="_blank">📅 12:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گزارش‌ها از شنیده شدن صدای دو انفجار در حومه حمص سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139572" target="_blank">📅 12:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139571" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36bbe7e0e4.mp4?token=G-NXrlQMRjtzPaF87ZO99sbycRnyKzzU10b3LAbR2fBv4XuFuKBl0xJlUdBeyrEFtJ4X8znR3VrD3x28Sb-HMNDzClwQ-9U_MBr89TkhGGlue5etIHd5l96pth8U98ds553jYsYTOI2XQw0FRjbm41rdp-3c6dvyzsbZNN88CX0smRF0pYIUC_re3w6xs0Gj6RWTM1HR6H8eBmpjxleRxIoZEUqJnOtQq97zfhrMRr_MZ6vtd62tPF6Z-LlBQB__MSKe1UL3Buh47052nVf9IvQOSG-Yw-a5i-NWzzj0qs_57M-GeS9EYl6bClvgd6jVlf2rfwOJTN46VV9TRXnyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36bbe7e0e4.mp4?token=G-NXrlQMRjtzPaF87ZO99sbycRnyKzzU10b3LAbR2fBv4XuFuKBl0xJlUdBeyrEFtJ4X8znR3VrD3x28Sb-HMNDzClwQ-9U_MBr89TkhGGlue5etIHd5l96pth8U98ds553jYsYTOI2XQw0FRjbm41rdp-3c6dvyzsbZNN88CX0smRF0pYIUC_re3w6xs0Gj6RWTM1HR6H8eBmpjxleRxIoZEUqJnOtQq97zfhrMRr_MZ6vtd62tPF6Z-LlBQB__MSKe1UL3Buh47052nVf9IvQOSG-Yw-a5i-NWzzj0qs_57M-GeS9EYl6bClvgd6jVlf2rfwOJTN46VV9TRXnyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراکشی هایی که وارد اسپانیا شده اند شعار لا اله الا الله و الله اکبر سر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139569" target="_blank">📅 12:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تسنیم : هم اکنون رهگیری پهپاد MQ9 بر فراز تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139568" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای و داده‌های ردیابی دریایی نشان می‌دهد که دست‌کم شش نفتکش حامل پرچم سعودی، مسیر خود را از تنگۀ باب‌المندب به‌سمت دماغۀ امید نیک در جنوب آفریقا تغییر داده‌اند تا از حملات نیروهای یمنی در امان بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139567" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
میرشایمر: اسرائیل یا باید خلع سلاح شود یا از بین برود، جهان توان تحمل این بار را ندارد
🔴
اگر اسرائیل در جنگ شکست بخورد، ممکن است به ایران حمله هسته‌ای کند مبادا در جهان هیچ دولت یاغی دیگری باقی بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139566" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1a662d9f.mp4?token=TUqVVqobv47uKk308-N_R6oc5M6-e5LGXn3o3v4zm-TCRSURtCcgOFlFYcVMWQcuAF_GB8UpM2LB8v7lXFjC7nNl93yR_tIOWIxTaiVjGXUttIiJVx-YVR1Fr6WRKUsF4z9WZQglYhTgYxGU_A4CNvFQ6kPuA9mPUl_xOKkalfdetfIrm9uaVqXg0j_3TaMUDGpAnDBcmoE2v_w-ifTEZVz2OJr7nBKVCcTZBWCpm94p0-jOhYPrrTrPednZ5unTHvKsC6t3Pg7vBrsMicX8m_uizIu6R0PMu4dw8nzIRW2B5Dj5QPQ2T_RjUkwbBq8KLCUp4bhUMO5vUX-P1xrpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1a662d9f.mp4?token=TUqVVqobv47uKk308-N_R6oc5M6-e5LGXn3o3v4zm-TCRSURtCcgOFlFYcVMWQcuAF_GB8UpM2LB8v7lXFjC7nNl93yR_tIOWIxTaiVjGXUttIiJVx-YVR1Fr6WRKUsF4z9WZQglYhTgYxGU_A4CNvFQ6kPuA9mPUl_xOKkalfdetfIrm9uaVqXg0j_3TaMUDGpAnDBcmoE2v_w-ifTEZVz2OJr7nBKVCcTZBWCpm94p0-jOhYPrrTrPednZ5unTHvKsC6t3Pg7vBrsMicX8m_uizIu6R0PMu4dw8nzIRW2B5Dj5QPQ2T_RjUkwbBq8KLCUp4bhUMO5vUX-P1xrpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز پهپادهای شناسایی اسرائیل بر فراز منطقه ای در کفررمان در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139565" target="_blank">📅 12:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xf8FpWs5IMxpCdLJAg_eQOwmDkc--0PrubjX3lVZfhA3bG8RK1VxowB5kGEWGWmkYLYs9c0ryjQqAKfckq_wIIvKfOb5q5-Ljwjw0mPldOy_IYjxblO2luzDd2bxAH4uvTda43bohax0Tpl0SGEW7ER4i29apLmxstQ72dzGhh2igI6YscqoUOe1PqOLjRrnLjhBO7Nhe_s915xJi8hs8B10eR-xi2XD-LKxw4XaY3syraPnCiISd1TM7U7DjLOVEXTL0aDf-Nuwd0uXryyZpWhxFTn8ZdAYCjNjRKmTmHhWf-4uO8PbuCPvbp2aFN9CGlq7rhuB41cHDAfMrneL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک کپیتال وان اعلام کرده است که در پی بررسی‌های مربوط به قوانین مبارزه با پول‌شویی(AML)، حساب‌های بانکی سازمان ترامپ را بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139564" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هرمزگان چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139563" target="_blank">📅 12:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک مقام ارشد سنتکام به استراتژیست های پنتاگون دستور داده تا دنبال یک راه حل خلاقانه و جدید برای فشار آوردن به ایران باشند، چون از نظر آنها، بمباران به عنوان اهرم فشار برای کشاندن ایران به میز مذاکره موفق نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139562" target="_blank">📅 12:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره ائتلاف دریایی عربستان برای باب المندب و پیوستن پاکستان به آن گفت: من نمی‌خواهم در مورد آنچه که تحت عنوان ائتلاف تشکیل شده و قبلا هم درست شده بود و ناکارآمد بود صحبت کنم. مسئله یمن با این چیزها قرار نیست حل شود. ما باید تلاش کنیم ائتلافی برای صلح درست کنیم نه ائتلاف برای آزار رساندن و ایجاد ناامنی در منطقه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139561" target="_blank">📅 12:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فارس: به خاطر بسته بودن تنگه هرمز قیمت گوشت گاو تو آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139560" target="_blank">📅 11:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما با کشورهای منطقه همواره در تماس هستیم.
🔴
از همان نخستین روزهای جنگ تحمیلی، به‌صورت منظم در تماس بوده‌ایم
🔴
دانایان منطقه به‌خوبی می‌دانند که امنیت در منطقه تجزیه‌ناپذیر است.
🔴
ناامنی علیه یک کشور منطقه، خواه‌ناخواه به سایر کشورهای منطقه نیز سرایت می‌کند.
🔴
همچنین به‌خوبی دریافته‌اند که حضور نظامی آمریکا ناامن‌ساز و ثبات‌زدا است.
🔴
طبیعتاً همه کسانی که واقعاً صادقانه به دنبال برقراری امنیت هستند، تلاش می‌کنند مانع از تشدید درگیری‌ها شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139559" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
👈
آیا ایران به حمله اوکراین به کشتی ایرانی پاسخ می‌دهد؟
‏
🔴
بقایی، سخنگوی وزارت خارجه: به گفته مقامات اوکراینی این اقدام غیرعمد بود اما شواهد نشان می‌دهد که این حمله عامدانه بوده است.
‏
🔴
هر اقدامی لازم باشد انجام می‌دهیم که هم اوکراین پاسخگو باشد و هم اینکه دیگر این اتفاق نیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139558" target="_blank">📅 11:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92447bf90.mp4?token=n36I5vANg78pBOiFUmDzstKKreoj3eW2Rf4ng4athkVS7_CA1fcJpOZ6xzoTOEYjkihs3gsHZuBbPz0vjLaSSdiC8g8Deel3Nudam9tC92D3EBpaK0b9Y3Fd7YYw0EJg3nh66ad1Ywg74hjZeuJNYoQ6rxO7P1RBpROAEAaeRRRSjmv_MAHV3LzoXhUXXq2FxavcXb_f7aC4SzKMYk4lR30g68RWxfVTKRduW0kdjRvXngoaMsQP-bIev_dFsX3avoVR1-YAcD0tcYeJuolWWyC28jWHv3coEW1xKTUlDGMg2VlxvkQoBHzBnIpg_NO7ber0CVNWjFkhm9LjtgKItzRbYIYOuw4x76FZ5B0sMu7jwKJDRrP23nVY_6TzvlxPyAoalShNmPV2LhKeOIyNOeYNPFKCCatzA4sQOTrZ6ANFVseI15qJQEelBANBKpRMFFKRjuusmEBB8Xovy2GZzKc-aHLPQxDuzt-e_28o14CHSkI4ds8AFUSX0XzIcaJqzGZ1vqBk-A-DK6d0awVuNzF1cODIKDgPEfnlOjilksw1lqZELziHpR05pgTEDrFS7yQYnGCDeco8MquaIMWUoASPahqq8pQQDsCMrWtG2VK438qFAw6PbRX4vmGwjApZK_VT0WwGKYONExCuXbM1JdARZBbuf87oh0cEIELVX10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میانجی‌گر جدیدی به میانجیگران موجود اضافه نکرده‌ایم
🔴
بقایی: پاکستان میانجی‌گر ایران و آمریکا است، میانجی‌گر جدیدی از جمله چین اضافه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139557" target="_blank">📅 11:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139556" target="_blank">📅 11:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بقایی: ما الان مذاکره با آمریکا نداریم/ مادامی که نقض عهد آمریکا ادامه دارد وضعیت تنگه هرمز تغییری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/139555" target="_blank">📅 11:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139554" target="_blank">📅 11:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfCC51gmvTe_FAv2McM5Z48Dnr8Je3oNvo1TSRiyjA0QzUBdtkjrJ2eLmQdN-mC5NWL-lDVWzS_GJzKuwhayptKeP0JWmeXfbuKIOEHVoqBUXsFPrKebTo_BsgNfHCNJB0LkQG056ayEetA1Vsi0uleraog3WeBk9Vh-zASvgJXkRqVwH91xnZ30E4iNmyMGxtdJQRV4RL18kyO3hNhiLGcz1KRSDZH987YNi1zWBVbvj3IavwpzD7LxQbewK0U2tZj184Xt9iiR3BrHs7GiyXZrRxLDLV4MSPcHv_c7xxlbHH80kg4muwl7w1ErGt8lJjXSBayA3-vjj4g2MMWQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139553" target="_blank">📅 11:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcXIEu6j1vvwLrAmijD4Hf9v1pP3zyUkQcYYn3pxLlGZLChF9WEbSLEqqecxmnT15foMRZRFjhPiRehnJffKWFRPQeSPi3zmNMzgfLMYCjBYYsgw-o_RmUqVLFZJGpp9dla-tZHZ-XReuGpkHAHJgpHEA3bII0kV4aAkjrpBkFgOKkcFkBocW5Fv70n2W-ay9QNlJliuX_fhSgoTDL18hG04MH7l7IFqWAd3gXqQEfm7smGGL1NNNXVuykOQA8jcZDjFV61svV-x5K9BeQaIR5kIbZ5ReOOnJXh5ZJJlcHEf13EtRpYGmm3qSxjst7kgigu9aUoVGLk12c2HnOU2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSSfPdcj0UTsNKyAIWXweAS5P_H6nv2VjI-MJzY6EdDgBdJ4VOd3gHl0PSoV9YII0DwdRgCrGHiP8MKJNW1B50WlXNGbUauuHNYCwarZYRXIhFEDfUThBgHjiKysaZ28UUt_WGugpf8myW4A-YS7qsvCc2M_QS1D5OLtRy_2R5ZHw32RvNixbg_RlO4SN9rydZNjcK4RpnegjJZ23xLqJcJcuj2h5p775dXYJkRPqoEmjoHGyeC0joaYpoYr7pV1j-l1V2_l6FCyoD8MMYKM51wkoegfQreZH1cwdvnA_kuETEiD9CFdWeHqGyz6iMSJKaMOOg8CwY_-z2oLIQ3WDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YX-y7QmA7fY4ePU2RzbNbRtKAtgIZ6xfGsEGWbp9uloV_VTdShuk4EuIqCek83fh0dxFy6-bapAYQr9JLkggdUTchN7K5vro18CfVXEh6kCO-3NRvzWOj3s5DUT89eKvktayTU_burAVHUFkYY9Fj3h27BmknNmHFbPZ1xHUYNBezDp_rOtMbwsjEeE4M6xwItG9oly-Rg5RYW5P4TzMbTuLO8S0C30DU6U5999AM4TYR8PTJUkN9odwWfi8XJdpNk2czetYc9kDKxz-K5Nhh_9XOZMFQXyDfp6Cgo_S1T9mU-FbX8zVQw-NSEH1WF_iuExbZsmEn8yqKOpOf85i_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داشتم قیمت PS5 و تو دیجی کالا چک میکردم که چشمم خورد به کامنت‌هاش...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139550" target="_blank">📅 11:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یه سریا همه چیشون شده سیاسی، دین و زندگی و غذا خوردن حتی ریدنشون</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139549" target="_blank">📅 11:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139548" target="_blank">📅 11:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بی حرمتی و اغتشاش حامیان جمهوری اسلامی در کربلا و توهین به آیت الله صادق شیرازی
🔴
پ‌.ن: آیت الله العظمی شیرازی مرجع تقلید شیعیان و مخالف نظام جمهوری اسلامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139547" target="_blank">📅 11:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات با عمان در چند روز گذشته با جدیت ادامه پیدا کرده است
🔴
تماس وزیر خارجه با همتایانش با هدف جلوگیری از تشدید ناامنی و تامین منافع ملی ایران ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139546" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d62bba082.mp4?token=O5EwoVuY2T5Zf8Vf2Nqqty3VSDRZkoWlATM4xYNizQMRIXeWDx3prs27cYXAoLbyg5M3OX8b09OWM0hldoHv_RwgfX2tD_yol0lL686_0ra2jKpghTH-WxQbYxuy-yc_2acIDvo9QR4f_A9MAhtE_XjMg7PtG0uzKwpVsmHnaCgyiq9iIe2xvbZjt30ATVooES7II26nm_qUsROIvc_Bf-KvQWRDfUaXQQIMbmRYKR7-oeEf4T3vTk0brb9Md3omYGSzj2JI2XCRWNSurm9UeZ563gI-SRh7ysw0ABORIVqrTaIDygzJWcbhDpD-5v7h1VnxWNiTbjdOnQ6T3enZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ‌ در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139545" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/139544" target="_blank">📅 10:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سناتور روس: مناقشه پیرامون ایران احتمالا تا اوایل 2027 حل و فصل می‌شود
🔴
گریگوری کاراسین رئیس کمیته امور بین‌الملل شورای فدراسیون روسیه گفت، باور ندارم که مناقشه پیرامون ایران سال‌ها طول بکشد، طبق منطق رویدادها فکر می‌کنم این مناقشه تا پایان سال جاری یا تقریبا اوایل سال آینده (2027) حل و فصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139543" target="_blank">📅 10:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkG5Y8EbaFN1CDE1X5Wqr5b-VWHG6V0tvSpDko3mHK7gJp2lV9EO9LNbihOJ_KemKImxMtl-XaV5bKBpHKAWi4Tdl9zawfPTfCcBwSJ4RAOs7_Tsndqq11GafphooZHVtUxeha8mbe4GmRvpwlK1Kez7BH4oMUliBIOJLoOh11cp4DEsB42M7DpQDNjmaetibxPUprCK4MZDsI-SHt9QfkTlkP1JfZrGbJEPb4D6X4EXrqbNSsGd_q5jdYHYnLZKaY5hrjaDwG2AZVfnakA_z7rozuIgbcvupBWUPAK6fXv6dJSfni4FfUs_IGNcRgfpHaahocpH0i0Y9nOa-t-pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خط فقر برای یه خانواده ۴ نفره در تهران به ۹۰ میلیون تومن رسیده. این یعنی اگه درآمد کل خانواده از این مبلغ کمتر باشه، زیر خط فقر حساب می‌شن؛ در حالی که حقوق وزارت کار فقط ۱۷ میلیون تومنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139542" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره: پاکستان و قطر نمایندگانی را برای مذاکرات آمریکا و ایران اعزام خواهند کرد
🔴
تماس‌های عراقچی با مقام‌های پاکستان، عربستان و عراق در شکل‌گیری این روند نقش داشته است
🔴
طبق گزارش الجزیره، هدف این است که روند گفت‌وگوها هرچه سریع‌تر آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139541" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f5ad2194.mp4?token=ozV608yGOPb_77Lxk8NtWx8Sp-foJAq7es5eWuCz2cCPHOl6QRDBkzGaLd4fY14_5gixDamMR8MUVjTkkfvCCw16g7xaRRumxdDtwTU0Bl_JfvGKUoeg-WiWwTTRp98Q5NSkCGYZ34NKgg6LVMBwohqWuyGPk0Q_6x7_JdM5BEsudoyVKCXgH6be4yMpJWZGVC_w5PJaC8gC5lqGMV5G0wXfmL8Ht8cpBM9RPf6cKC9-J8fT_HX-X-D4PLsf-DDPXZ0a1kvx1q6jrGScsCXy3SJ7JV1EwKoiLZDSH7fsFL8OoiK9piSlfrS-aD7scL8pj6r9xLAbgweVaZCY-AmUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f5ad2194.mp4?token=ozV608yGOPb_77Lxk8NtWx8Sp-foJAq7es5eWuCz2cCPHOl6QRDBkzGaLd4fY14_5gixDamMR8MUVjTkkfvCCw16g7xaRRumxdDtwTU0Bl_JfvGKUoeg-WiWwTTRp98Q5NSkCGYZ34NKgg6LVMBwohqWuyGPk0Q_6x7_JdM5BEsudoyVKCXgH6be4yMpJWZGVC_w5PJaC8gC5lqGMV5G0wXfmL8Ht8cpBM9RPf6cKC9-J8fT_HX-X-D4PLsf-DDPXZ0a1kvx1q6jrGScsCXy3SJ7JV1EwKoiLZDSH7fsFL8OoiK9piSlfrS-aD7scL8pj6r9xLAbgweVaZCY-AmUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی صنعت آب کشور: وضعیت برق آبی کشور بسیار مناسب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139540" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خبرگزاری میزان اعلام کرد که صبح امروز امید بهزاد و پوریا صفوت، زندانی‌های سیاسی به اتهام همکاری با موساد و ارسال عکس و فیلم برای اونها اعدام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139539" target="_blank">📅 10:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: وزیر کشور پاکستان و طرف قطری نمایندگانی برای آغاز مذاکرات ایران و آمریکا اعزام خواهند کرد تا این روند هرچه سریع‌تر آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139538" target="_blank">📅 10:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مقام آمریکایی به CBS: پیشنهاد ترامپ بازگشت به مذاکرات و حل‌وفصل مسائل باقی‌مانده است.
🔴
هنوز توافقی با ایران حاصل نشده، اما تلاش‌های میانجی‌گرانه در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139537" target="_blank">📅 10:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLjNqH3IBIMk19hMjg79ReKDWoYypxrR8Ke0kz2TmkfFldbhmeUTDRGYqaF4NwYx2PKthziqi89xP_k4HoDebVILxT7BywlZ-UTzK-3gtoY-oWysiHIbVC2qjIqFgE2IR6cmlCWIEA9MV5lERqfJ8ZotyMoMYUkMvI8gk7JGSzu6TXvIUGyjfYSOiQoBx7hMmqAG4Enxwg8BCfuWhypSPlKBBaG4ifMlPRouhVi0iMdn1Zv8SlLhgTJVrI1VL9ZUgBhYJkdrNmgTmIaBIflfATouSHC5j4kJU1DC8s13Qc7wfM4savrVrABYgqLZ4z2kw9DDgJV5Hh2AQRyA9KvkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تصویری تولید شده با هوش مصنوعی از خود در کنار جورج واشنگتن  و آبراهام لینکلن منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139536" target="_blank">📅 09:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/73daa7c99d.mp4?token=BDTBt4AgLdoZoLRK9RJbHruSOPlg4I_HNNKWPWt1c-ewprTb02yVg6GkOTeJjjCo-b-UuMB-Be5GKl5PKlUnJ75G8H46V8HxXV8oDTs4m5EWOm229hzIzIHuAsMZ1AcXEUR-uGkbqQsP6uTFdPrVTZLn95N2zK4nerLOiQn8dF8WmiMNl55mNJU3HaJieZ03WSXeeVMi47QKjUpy0qRjiXXXn1vwxc_Gz4ieYNV0BoSaGykKhFrJEE3b5WHZjwrJdP4hj7Kr41hLTNyUKrMBhxDyuBghYkCyG5L_NslZbVa5UhJiOKz1PmLAQ0GwUeE4uzE0Q4pDX3vgR28VFL74Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/73daa7c99d.mp4?token=BDTBt4AgLdoZoLRK9RJbHruSOPlg4I_HNNKWPWt1c-ewprTb02yVg6GkOTeJjjCo-b-UuMB-Be5GKl5PKlUnJ75G8H46V8HxXV8oDTs4m5EWOm229hzIzIHuAsMZ1AcXEUR-uGkbqQsP6uTFdPrVTZLn95N2zK4nerLOiQn8dF8WmiMNl55mNJU3HaJieZ03WSXeeVMi47QKjUpy0qRjiXXXn1vwxc_Gz4ieYNV0BoSaGykKhFrJEE3b5WHZjwrJdP4hj7Kr41hLTNyUKrMBhxDyuBghYkCyG5L_NslZbVa5UhJiOKz1PmLAQ0GwUeE4uzE0Q4pDX3vgR28VFL74Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در پالایشگاه استان صلاح الدین عراق به دلیل نقص فنی
🔴
بر اساس اعلام منابع رسانه‌ای عربی، انفجاری در واحد هیدروژن پالایشگاه بیجی در استان صلاح الدین عراق به دلیل نقص فنی، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139535" target="_blank">📅 09:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آکسیوس: خالد بن سلمان، وزیر دفاع عربستان سعودی در سفر به آمریکا پیام ولیعهد سعودی مبنی بر ضرورت کاهش تنش با ایران را به ترامپ منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139534" target="_blank">📅 09:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ساعاتی پیش‌زلزله ۵ ریشتری قاهره را لرزاند و به دنبال آن، هشدار امنیتی برای برخی مناطق در اسرائیل نیز صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139533" target="_blank">📅 09:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3v4NX1Y89km9_IfneRs4I2BFq_gjM2E1uP7SO_73a8I5hR7VqV5Ce8WIJ7KtR679zcXytwmZ8UPpyM55qqTrhEj92vPSDDHGr6u3kkQd-LdbgOOaBgPjzGdDtUnRwUnCqB95vrN7ZkNtD9DGBTvFgzRE-Pw72Y1rvPk9uTDnFDaVG3Pa8NUlLYyf8sfgyj8nyeWQr1dcJD2U_oto7l9NiC0wzXpOkBJ7nhKdzg1fT-R0CKUntLc2rAxrb_e_25bY2cq3H9sSy4Fj3USdmdDfeEEHW_qZhLFig04XwkIo5R5qs2FvhXHDy5MF9FklI3riM_YkMc-fTlm_b9-nzL2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: قالیباف و پزشکیان شکست عشقی خورده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139532" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDhXNnHbgtslJebllo1OihZJhf6mwzrBHlJW2x3-MDMz4LHZViZ9jgYumZOyxfmZynD38mL06fX-lBPT7Z_OK4jqfNNqUTfjOodhYOfb5Ogf5pEZQrfoHPYZLTysO_O104jplCWFBGep-9KXXUfTdl7YRvfHfIzdvKju3QNEq8zJuGCFub3Nj8y0C52zhuEleChbXVUOvkqMj_eTQ3RlfFqk2mo6fYp7WgJzSDxhxQSHyXG2ImYfycAfo4DJrkqaCRokUkk3G2JbmOWp1ddzFeS8JJ1gV-5PGtFCXYzNn_MtG20ZaDBRQ9R4kPDzIgCskS0chaQbEb4r3xi9GWO-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری سنگین C-17A نیروی هوایی آمریکا، امروز از پایگاه هوایی اوسان در کره جنوبی به پایگاه هوایی علی السالم در کویت پرواز کرد
🔴
این هواپیما احتمالاً حامل موشک‌های رهگیر سامانه‌های پدافند هوایی یا خود سامانه پدافند هوایی تاد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139531" target="_blank">📅 09:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Clq564Df8tOYG-aAxrpOpFq-oFBV6GiYfniY6Q55dD6fxQaVTqfRRxUehTzeQ7pU7olIua6Qu8aGPLHe1bJ3aZsbo8kZqBBDJo48Rh82WTsfr22mNeqRxBIJmJW4EuIMi54dO65LiKq6pMQvIkp0EJEiPvPvHWSG9zpDf2BlfEW2dzpb6VDLu8aNRyfJp2EccbZn7ehwColBU-0VkgPeOAsgl0JNCU_MkWPQFBJyS3VRQti3Snlg1l-sDykM_CbCC8e4-BeBy0WfhkoYDIpDambiEFbhmeGJtm3S9kw6xln4KFkih6Wuj270PfptWJkbU_ZkeaJDOewmuAy-bvxRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه اگهی عجیب وایرال شده تو دیوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139530" target="_blank">📅 09:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884692a20b.mp4?token=i-FXajITOCcgHsVldX62lxOwJF1H0Tx2tiY0xzjORdV0Gv6CoaNLgxpLgezcHVK_YsCSCcSemdkmKFQC3nXqMJeWxufKA5X__PI-bpZv31_YPh3RgamfwzA9kHzuau2ktfIx7R7Y4H0v-Pst_9QsKNch-SjveF8SQqaV3KqDn-YrmdRS-OzgeM_rdgBH2rkDyN3WqjlMwE5tfURqc5K_eXN69BaOGltZYOl4jr8-jVNvAc63LaMC9ARYtwnpOCrPcbQL_q5mkaYM_X001q4a7SQm_IJrgMG6zwYK5dvLKOc-Hjsdp8p2Bac2WGrBhkdfBf10hxioZfmz4dtAYvn7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884692a20b.mp4?token=i-FXajITOCcgHsVldX62lxOwJF1H0Tx2tiY0xzjORdV0Gv6CoaNLgxpLgezcHVK_YsCSCcSemdkmKFQC3nXqMJeWxufKA5X__PI-bpZv31_YPh3RgamfwzA9kHzuau2ktfIx7R7Y4H0v-Pst_9QsKNch-SjveF8SQqaV3KqDn-YrmdRS-OzgeM_rdgBH2rkDyN3WqjlMwE5tfURqc5K_eXN69BaOGltZYOl4jr8-jVNvAc63LaMC9ARYtwnpOCrPcbQL_q5mkaYM_X001q4a7SQm_IJrgMG6zwYK5dvLKOc-Hjsdp8p2Bac2WGrBhkdfBf10hxioZfmz4dtAYvn7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افراد مراکشی در سئوتا اسپانیا اکنون در حال غارت خیابان‌ها هستند و شهروندان محلی را خشمگین کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139529" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یک مقام آمریکایی:  هنوز به توافقی با ایران دست نیافته‌ایم، اما تلاش‌های میانجی‌گری همچنان ادامه دارد.
🔴
پیشنهاد ترامپ شامل باز کردن تنگه هرمز و توقف حملات ایران و شبه‌نظامیان وابسته به آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139528" target="_blank">📅 09:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh5QxCIn3T40nRnmY4esxZsK9uFsJ-zdM4ISgw1aIRBoongp8HqHTOGCSo7GnASq0AVNft2HHjfCijcinc-xza_Tcpo5DPnUKnMRqyG8FWZjYMy0dMagqjqKt3cZlIK2bZccYsoEcvxfxLfdyl6qNzLzwC66A2oaCnSmDbJrQ_y2ssXNz4Ytf7wuEa4sY8JmhE8zIxqciCFPgJd0fvGpQTZNMrHobRPp6Q1GYcoPOJj4HfXcSDcaFrR11TxeYofOsTbK_Z0cGm8xEicb_5mw-mEBMv2DDjVzvQ0V944ki1andK68HHq5ODm1FIz60mkp1QD8VPljh-uaHtIZD47v9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت با حتمال مذاکرات به 83 دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139527" target="_blank">📅 09:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که با استفاده از پهپادها، ۴ فروند کشتی اوکراینی در دریای سیاه و همچنین بندر میکولائیف را که محموله‌های نظامی حمل می‌کردند، هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/139526" target="_blank">📅 09:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLnzf07SogiOgWCz9AyMMrQExC70gzyVgTEUDtdnYL9X_a3bBm03CAWtKv2mf8HuvjpG1hkBO3gCVeWJXVk-wuMBZbRu9PQIuP-mELHBe0U-2BYsHiDZqaZLiO-e927jv0hHn0Z9HGzx24dMUloU3tkkPb2682klFMGX4BQ8SmYe-57iaACE4k2-6zdCKOvZNMyiWfCEvuxUsjmrS-u8nfftxKnp32SFJ0Ad0uYlx4xQ6VtaTb1zPLxSF2u5xh7FZUfprAR4Pc9JfHKuG76ANBSK8iEzE780cdbBrswl0zPAgxPytaFipRf9k0glXaF4rw6yrHpSi6XNPXmIqelnKn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVLnzf07SogiOgWCz9AyMMrQExC70gzyVgTEUDtdnYL9X_a3bBm03CAWtKv2mf8HuvjpG1hkBO3gCVeWJXVk-wuMBZbRu9PQIuP-mELHBe0U-2BYsHiDZqaZLiO-e927jv0hHn0Z9HGzx24dMUloU3tkkPb2682klFMGX4BQ8SmYe-57iaACE4k2-6zdCKOvZNMyiWfCEvuxUsjmrS-u8nfftxKnp32SFJ0Ad0uYlx4xQ6VtaTb1zPLxSF2u5xh7FZUfprAR4Pc9JfHKuG76ANBSK8iEzE780cdbBrswl0zPAgxPytaFipRf9k0glXaF4rw6yrHpSi6XNPXmIqelnKn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیشنهادات مارک لوین، مجری مشهور فاکس نیوز به ترامپ برای حمله به ایران:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/139525" target="_blank">📅 02:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EavyIe6vyaZQPzAbU2M5A7t3r0HSJGrOfPWd_1XlnnaRfnkCMM-w5BQJ33JHwONad-PSKKwdt6wkyVKb_qPMFo0hPt6rVrOOPJqX-gubKhJSz71E_kOnsjx2NdK7g0QzhjQILlWspYxpDbaDRh_MS9oGq2kkQ3xPEBewYwcJS3W0BMLdy7hvu9Eh7hl0vAOZWRJj4sCuJAEQNBrLFennrQtuFPM6pUzU5Re5Fg5itUidI5MLiTxIyK0KKRvHCTwvIoD6RN_sfRzNaz1YCuBc1FNq6eeMv2gHDwE7afLmuDG_kkTjg9KPGd27uMCIaSMwVqspn4chJ5JzgxxBCbhSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر بشکه نفت برنت 83$
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/139524" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خبرنگار: آیا حمله برنامه‌ریزی‌شده شما به ایران، شامل اهداف انرژی می‌شد؟
🔴
ترامپ: نمی‌توانم این را بگویم؛ اما قرار بود حمله‌ای عظیم باشد، بزرگترین!
🔴
درنهایت خواهیم دید چه میشود؛ خواهیم دید آیا به یک توافق با ایران می‌رسیم یا نه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/139523" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caced3ead1.mp4?token=sPulSGr8nBN0AmBYAen6OvQNcjZWU07Fc1mx19G8FHIx-f0otoKqLzfpZF30UesITsRqUc03m1GKdupq15xRLt8FkfgsQdpUoH4ESgTcwFfVsJeD8hWZftLuNdjOGfLHYdobdly52ChASOnjPkFoXMQ9x2qtRQ7aSzsqzNQc004m_i0XrUxZ1wOZbqNZ_KypU_Mt4vaLvlcko3GtGG86kRWCDrjKXIFsK7WBkXLBr1WrZh4v1xHq9NqOVMxzkCNyZQOIKipaYDp_2rhxw7W26_7WD4-WEX67VDfvxh2dXxQG-HnYDqsFE64gJTklExmlxzFWAfAoGNJpdIw4DZz6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caced3ead1.mp4?token=sPulSGr8nBN0AmBYAen6OvQNcjZWU07Fc1mx19G8FHIx-f0otoKqLzfpZF30UesITsRqUc03m1GKdupq15xRLt8FkfgsQdpUoH4ESgTcwFfVsJeD8hWZftLuNdjOGfLHYdobdly52ChASOnjPkFoXMQ9x2qtRQ7aSzsqzNQc004m_i0XrUxZ1wOZbqNZ_KypU_Mt4vaLvlcko3GtGG86kRWCDrjKXIFsK7WBkXLBr1WrZh4v1xHq9NqOVMxzkCNyZQOIKipaYDp_2rhxw7W26_7WD4-WEX67VDfvxh2dXxQG-HnYDqsFE64gJTklExmlxzFWAfAoGNJpdIw4DZz6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا حمله برنامه‌ریزی‌شده شما به ایران، شامل اهداف انرژی می‌شد؟
🔴
ترامپ: نمی‌توانم این را بگویم؛ اما قرار بود حمله‌ای عظیم باشد، بزرگترین!
🔴
درنهایت خواهیم دید چه میشود؛ خواهیم دید آیا به یک توافق با ایران می‌رسیم یا نه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/139522" target="_blank">📅 02:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
/هم اکنون پرواز سوخت رسان‌های آمریکایی در خلیج فارس  @TitrDaily</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/139521" target="_blank">📅 02:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64bcf36d7b.mp4?token=XL2a06ky2-yC2ba3avPJCBDXQJGiea-W9awSgw1quxd2dwh076KnaxYaRt5CyjBiaeHuyP8QJYTaAaPlHE5wk5stjQE1q-ZhMQkkvFuIxVfmK3VkW_ZM0LpHCopChb_-ZjnMKNzIgeMxBdPxjiM0g-apyWk9qNP2oVTNtCzOQAs5x-hkt1RwNAsm8XWvmKThctRJh3aoNxdfU8PhX1SWh49FcSgCVlfVCywzSNd1d1q9zuEWqDv6C9PM4Zkj2hjw-EBFP5wL5lbawUpdIn0-01XGMdHYjDgj3GBhXtwelQves-1yovGLNiZbeyYHcvq3v7Wj_8My2vGWgJM0a2XYQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64bcf36d7b.mp4?token=XL2a06ky2-yC2ba3avPJCBDXQJGiea-W9awSgw1quxd2dwh076KnaxYaRt5CyjBiaeHuyP8QJYTaAaPlHE5wk5stjQE1q-ZhMQkkvFuIxVfmK3VkW_ZM0LpHCopChb_-ZjnMKNzIgeMxBdPxjiM0g-apyWk9qNP2oVTNtCzOQAs5x-hkt1RwNAsm8XWvmKThctRJh3aoNxdfU8PhX1SWh49FcSgCVlfVCywzSNd1d1q9zuEWqDv6C9PM4Zkj2hjw-EBFP5wL5lbawUpdIn0-01XGMdHYjDgj3GBhXtwelQves-1yovGLNiZbeyYHcvq3v7Wj_8My2vGWgJM0a2XYQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: "شما با کدام رسانه همکاری می‌کنید؟"
🔴
خبرنگار: "من از شبکه ABC هستم."
🔴
ترامپ: "بی‌بی‌سی؟"
🔴
خبرنگار: "ABC."
🔴
ترامپ: "آه، ABC. این بدتر است. در واقع، من بی‌بی‌سی را بیشتر از ABC دوست دارم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/139520" target="_blank">📅 02:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4dsdmDgMpN5_O-skvxkDqoWoWxux1yzq3nf3Qatnx9TlhRNldz41pmAmNBm19qDtXfGKiYJ7UvW01nHq64KFJ9GutTEXal8j6fWapBBlZp363ngF4TKOVM-LS16-6Z-XAStBaSK1WprPiXmrnIouoDOMTQE5FKMr11hd4u53JrwNoHfPaz3p56rxPENxBznOJzy8Vnr1gDM2auAYWRTXfj2hsjsanYCzsbitArO3JgsjwAQJpV1sL2jJgY8NV5zMhtmRgXwzBuZlE9UbOsT9_KRlkRn_lG45V-Ru5Hu3RqdSac-18GaHvlDb3AT6uYrs-5WJWGgg63Yf7pEUQqqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا:
موشک به کشتی اصابت نکرده و خدمه و کشتی سالم هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/139519" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گزارش‌ها از اصابت موشک به یک نفتکش در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139518" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3502c8eb4.mp4?token=K_O-tGf2scaOSJI8hiqUlsg8rAA3DpjLqjO6m4PEYJyqfg2ime1esiCpFM0cvhPF85Oxf60ASKyJXfTD4Bn-enB3yZmwBLlOLibijzBcJk8h1xVS3oHGXhlxrIT5h3CGb3cd0rShuN48kWS2yquOYntfMicnysVjYi5L-PL_m93MGOCltvbyFN5yQiIa6DMa5vckgQzONsjZhOZJ1VXhhfSdOTdC5KM6cylWdLAorqadSyASg345tZdJUGiNnrI_vw8priiMlOJOEPijWAqiTLVftP9e0Flg6Jl8O4W6s9KgJmQ68af22L-LAhOobRk-X_gT6ylVTJP6LOQwe5_Dew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3502c8eb4.mp4?token=K_O-tGf2scaOSJI8hiqUlsg8rAA3DpjLqjO6m4PEYJyqfg2ime1esiCpFM0cvhPF85Oxf60ASKyJXfTD4Bn-enB3yZmwBLlOLibijzBcJk8h1xVS3oHGXhlxrIT5h3CGb3cd0rShuN48kWS2yquOYntfMicnysVjYi5L-PL_m93MGOCltvbyFN5yQiIa6DMa5vckgQzONsjZhOZJ1VXhhfSdOTdC5KM6cylWdLAorqadSyASg345tZdJUGiNnrI_vw8priiMlOJOEPijWAqiTLVftP9e0Flg6Jl8O4W6s9KgJmQ68af22L-LAhOobRk-X_gT6ylVTJP6LOQwe5_Dew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم.
مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/139517" target="_blank">📅 01:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad698cc5d.mp4?token=eSFCvODsHtxs_qv6iXDulm7dByzr4X6Ghlv31V_0LzG_MiNKe37vYzCYGtSVLzbohu1NwhFRoMQXXDqNxBu26qD1-cliXmjpegJ8zicwYSt-FEGf5OBWGi0s2v-RKcSujPFkOeaO5hxzHL9k4D6na8Xgp66h9eXna6cUWfykwmvOGHfmQM5FNmwK_hEy3micpMmkWT2ev9uatwED0gO0UzECLCpIoH1ltKhlAx4FrGRpqMgjnKbHxm6Qw5Ut1PzmyMsEb8F3x3LvEcUXuE0Iceg2_NuI9SoP45L4YazpaGaylHW06sBd3T0t0maXnjhljIJm8WLYgS7l2eqmH0da3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad698cc5d.mp4?token=eSFCvODsHtxs_qv6iXDulm7dByzr4X6Ghlv31V_0LzG_MiNKe37vYzCYGtSVLzbohu1NwhFRoMQXXDqNxBu26qD1-cliXmjpegJ8zicwYSt-FEGf5OBWGi0s2v-RKcSujPFkOeaO5hxzHL9k4D6na8Xgp66h9eXna6cUWfykwmvOGHfmQM5FNmwK_hEy3micpMmkWT2ev9uatwED0gO0UzECLCpIoH1ltKhlAx4FrGRpqMgjnKbHxm6Qw5Ut1PzmyMsEb8F3x3LvEcUXuE0Iceg2_NuI9SoP45L4YazpaGaylHW06sBd3T0t0maXnjhljIJm8WLYgS7l2eqmH0da3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
شما نمی‌دانید که این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/139516" target="_blank">📅 01:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=kiAbsZrbEZbag6EnQo8y4WFy-8kBPOQbxVmNLDZ4VIaMh7TXtaHfJFxk9-woP5igsqptVH18TcbIVg85lfP3L7CQj9oIA-Gqjr_pAg97TR87ST8KJMIkKaVPKw7RbV8QYMn19gEMnYJ3W0Ue89RVhpwJsR_5FbYAg3Tdq82deVu755CD_np6XdTQUZl8mUUlGJMc08ZnthelqwVuiQpX_TGEskxmLI6QDsDaM1NZmKZ7BHfEaBBMku-ksI5pB_OK5xeaaLeFhtlkr1y5DgR9yR5uYB9xdxbT7RY5m4gGip9ABM3VOL7PRxQ2zYS5QxJZI6rs-KzALe78AcitMA9P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=kiAbsZrbEZbag6EnQo8y4WFy-8kBPOQbxVmNLDZ4VIaMh7TXtaHfJFxk9-woP5igsqptVH18TcbIVg85lfP3L7CQj9oIA-Gqjr_pAg97TR87ST8KJMIkKaVPKw7RbV8QYMn19gEMnYJ3W0Ue89RVhpwJsR_5FbYAg3Tdq82deVu755CD_np6XdTQUZl8mUUlGJMc08ZnthelqwVuiQpX_TGEskxmLI6QDsDaM1NZmKZ7BHfEaBBMku-ksI5pB_OK5xeaaLeFhtlkr1y5DgR9yR5uYB9xdxbT7RY5m4gGip9ABM3VOL7PRxQ2zYS5QxJZI6rs-KzALe78AcitMA9P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
🔴
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/139515" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c617d9274c.mp4?token=VbI28T1pURlJgId5Ir9Isn4qqLYTGKMCkpIiZCG4IBjpNJ7G09_QggiA_p0Dn_5IT2Bc4y1_l8c8OzLY53KutHu-2wuFs2jr-r_UXgQFBQCunt5KYuuFTk51lQ-2netY-WzTit2We9hBDB7bWHKhJ8pIBRj6imp5weur_wBVarbLC9M44-i55LybHw-odh5FlMwbEfRA_n8jTt6b-NVwLEbE4in6s2dQ5zLCtgR4hLKbfUyTfhCB1C-zW70Ogtg6K3JGAs1UHixGdxn5Odwuoo-mp_6oR9AosEw7KRqSaJ2Ox2wS0hx0fl5ThNO_q6HkeUcMdSmcqazXWDlYWZJuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c617d9274c.mp4?token=VbI28T1pURlJgId5Ir9Isn4qqLYTGKMCkpIiZCG4IBjpNJ7G09_QggiA_p0Dn_5IT2Bc4y1_l8c8OzLY53KutHu-2wuFs2jr-r_UXgQFBQCunt5KYuuFTk51lQ-2netY-WzTit2We9hBDB7bWHKhJ8pIBRj6imp5weur_wBVarbLC9M44-i55LybHw-odh5FlMwbEfRA_n8jTt6b-NVwLEbE4in6s2dQ5zLCtgR4hLKbfUyTfhCB1C-zW70Ogtg6K3JGAs1UHixGdxn5Odwuoo-mp_6oR9AosEw7KRqSaJ2Ox2wS0hx0fl5ThNO_q6HkeUcMdSmcqazXWDlYWZJuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:من 75 میلیارد دلار برای کشور درآمد داشتم. من برای خودم درست نکردم من آن را برای کشور ساختم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139514" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
👈
خبرنگار: آیا برای رسیدن به توافق با ایران، ضرب‌الاجلی تعیین کرده‌اید؟
🔴
ترامپ: خواهیم دید. من قصد ندارم مخصوصا به غیرنظامیان آسیب برسانم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/139513" target="_blank">📅 01:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ:
از ولیعهد عربستان سعودی پرسیدم: «ترجیح میدهید ما چه کار کنیم؟»
🔴
او گفت: «ما توافق را به حمله ترجیح میدهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/139512" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95889103bc.mp4?token=a40gTYKdBnOCxYgtxaDKkQj_3iZleMOpsmDF6gI5P8JcCS5OsMYOZDd0HvHRgz3nwZW5JGixx_Ldmxdx3yacsaR5SfKiK-0slkPEwnU2Aud5rXgLp77t8baG4aMJnCn1tyU9svLLGZo1GpaU-TPAs4vkVMupqHtqmF8tbI-pHbu32PtH_5NEb74hmNv7C993SUlpja-AKQomw1tDrUXN5hCzdoyGMaUSf8dyIoMeTkcXVjPo3gErOi2qU7BnRjseNCC3MHrIty4ugn1h6Fb-FZCaJfDQJhfBJCBSuYfSKLZHEkuzTXSSWqdb4Vl6Q0adeTvJ0_2cpPiyBNFBwLSCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95889103bc.mp4?token=a40gTYKdBnOCxYgtxaDKkQj_3iZleMOpsmDF6gI5P8JcCS5OsMYOZDd0HvHRgz3nwZW5JGixx_Ldmxdx3yacsaR5SfKiK-0slkPEwnU2Aud5rXgLp77t8baG4aMJnCn1tyU9svLLGZo1GpaU-TPAs4vkVMupqHtqmF8tbI-pHbu32PtH_5NEb74hmNv7C993SUlpja-AKQomw1tDrUXN5hCzdoyGMaUSf8dyIoMeTkcXVjPo3gErOi2qU7BnRjseNCC3MHrIty4ugn1h6Fb-FZCaJfDQJhfBJCBSuYfSKLZHEkuzTXSSWqdb4Vl6Q0adeTvJ0_2cpPiyBNFBwLSCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ژاپن:ژاپن بسیار خوب با ما رفتار کرده است، به جز البته، پرل هاربر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/139511" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75f718148.mp4?token=CF3Gicrte30XRmcAHaI5l3yL4C1-FSx6wLhZG7xNgmFxPVkusHlm9XlCiCg5S5y-UpSxWANwmbtAgLRW3s66DT3bT5XO6NWn9upFr-wD2oH6bWy9lv8m2dmAblHh_NlNcZuZMFjUJr4lps7FoaUCnJ6tz5IT5M7W5W2X8WDIF8OWOUK2oxfB8M0FYh4gzZ3Zz-Ng38wt8hPonaS6AGijK_GkvifOhi5pasKN_JqBbzTOVYcmoIL2luhsIWtarQouZOymxEStA6e4uLgVD5wEW6UG-r2E8Gzfx40OAU7p2lm8BixdGFMI2Nc64b-2l3hPCtFsIIREkTBwHwlvYDLF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75f718148.mp4?token=CF3Gicrte30XRmcAHaI5l3yL4C1-FSx6wLhZG7xNgmFxPVkusHlm9XlCiCg5S5y-UpSxWANwmbtAgLRW3s66DT3bT5XO6NWn9upFr-wD2oH6bWy9lv8m2dmAblHh_NlNcZuZMFjUJr4lps7FoaUCnJ6tz5IT5M7W5W2X8WDIF8OWOUK2oxfB8M0FYh4gzZ3Zz-Ng38wt8hPonaS6AGijK_GkvifOhi5pasKN_JqBbzTOVYcmoIL2luhsIWtarQouZOymxEStA6e4uLgVD5wEW6UG-r2E8Gzfx40OAU7p2lm8BixdGFMI2Nc64b-2l3hPCtFsIIREkTBwHwlvYDLF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گزارشگر: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای نظامی ایالات متحده از کویت و بحرین هستید.
🔴
ترامپ: من نمی‌خواهم در این مورد اظهار نظری داشته باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/139510" target="_blank">📅 01:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c1219395.mp4?token=gKm-JHcAMokTvL8EofNJpTSBY_DP2Okb7gEh2uq8ROurIKyRnRrJNXWz-eTH44vw8ASdcekxhAB2F97GLGvWkxVCXITWfyrFIokWoXt36O2OPXU7vydk1m9rXptgZzgibo9HteCu0O9yOBFCa1rthyF7CFaQedWTWeYDA58lxBmztCy1HM40RKrsSUOxRXuh7OCIsYIoD3QnrKyZtNT6MMREa144NOK1mDXIU6hk7QwDCgHHCj02tr0b4suJWdbisw_X3uEl3iJftWYfJdnYkft4TilBrgAnGiS8Ube7CpsVixHFzVKSA7W4Ib0SkCt_SgsUeNBfBnJke0udDj_EVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c1219395.mp4?token=gKm-JHcAMokTvL8EofNJpTSBY_DP2Okb7gEh2uq8ROurIKyRnRrJNXWz-eTH44vw8ASdcekxhAB2F97GLGvWkxVCXITWfyrFIokWoXt36O2OPXU7vydk1m9rXptgZzgibo9HteCu0O9yOBFCa1rthyF7CFaQedWTWeYDA58lxBmztCy1HM40RKrsSUOxRXuh7OCIsYIoD3QnrKyZtNT6MMREa144NOK1mDXIU6hk7QwDCgHHCj02tr0b4suJWdbisw_X3uEl3iJftWYfJdnYkft4TilBrgAnGiS8Ube7CpsVixHFzVKSA7W4Ib0SkCt_SgsUeNBfBnJke0udDj_EVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
قرار بود یک حمله عظیم باشد.
از ما خواستند که این کار را نکنیم. گفتند: «لطفاً این کار را نکنید.»
همسایگان نیز همین را گفتند. ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به یک توافق برسیم یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/139509" target="_blank">📅 01:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
👈
ترامپ درباره احتمال حمله به ایران:
گروه‌ای از افراد دوست دارند دست به حمله بزنم  یعنی خیلی ساده دست به بمباران بزنم و در مقابل، گروه دیگری هم هستند که اصلاً نمی‌خواهند چنین کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/139508" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ:
از من خواسته شد که توسط عربستان سعودی، امارات متحده عربی، قطر و همچنین خود ایران، از انجام حملات خودداری کنم. این یک حمله بسیار بزرگ بود. وقتی متحدان درخواست کردند که این عملیات متوقف شود، باید بگوییم: "خب، بیایید ببینیم." متحدان فکر می‌کنند که یک توافق وجود دارد. یک توافق در مورد هرمز وجود دارد و این توافق در مورد مسائل هسته‌ای نیز خواهد بود. ما با آنها در حال گفتگو هستیم. این گفتگوها فردا بعد از ظهر آغاز خواهد شد. این کار می‌تواند جان‌های زیادی را نجات دهد. از ولیعهد عربستان پرسیدم ترجیح میدی چیکار کنیم؟ اون گفت بجای جنگ، به توافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/139507" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: ما در حال مذاکره با ایران هستیم. این مذاکرات از فردا بعدازظهر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139506" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ:توافقی در مورد تنگه هرمز وجود خواهد داشت و توافقی در مورد خلع سلاح هسته‌ای نیز حاصل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139505" target="_blank">📅 01:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87d70cccd.mp4?token=cWAk_Ov_lXhY_9oVWGKsPoUXuMaVNY_gf-WcXeohzmjJY65dDpLyf2F28J0WPMORNY_4LpgoQ9b6cY9LgWIV7XYlzVr7ZrGoQ3pP3MTJrNLtXgQ1wQIKURRS3JnHRLjEZAmN4KJC3vOfgunLUS6MLLzSX7Izn3mYa4jvrAvlW2yp87oHFMBB3vKNQ7lzCpMclepsTLr-7xfhNLw33ieX1QY70SAuI7sv50ruI7Nz95r4fI45DV6Mz1W0B-Bk0YxeYebZgJ_bxGFkZCqFX1K05UrmD4uy9PzNAid19_lrYsDM0QBOBdBgJ8S7lzMTuzrMW9fN3h7H8cIKCFUUSE2J_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87d70cccd.mp4?token=cWAk_Ov_lXhY_9oVWGKsPoUXuMaVNY_gf-WcXeohzmjJY65dDpLyf2F28J0WPMORNY_4LpgoQ9b6cY9LgWIV7XYlzVr7ZrGoQ3pP3MTJrNLtXgQ1wQIKURRS3JnHRLjEZAmN4KJC3vOfgunLUS6MLLzSX7Izn3mYa4jvrAvlW2yp87oHFMBB3vKNQ7lzCpMclepsTLr-7xfhNLw33ieX1QY70SAuI7sv50ruI7Nz95r4fI45DV6Mz1W0B-Bk0YxeYebZgJ_bxGFkZCqFX1K05UrmD4uy9PzNAid19_lrYsDM0QBOBdBgJ8S7lzMTuzrMW9fN3h7H8cIKCFUUSE2J_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به المنصوریه، جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/139503" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ، از نیوجرسی به سمت کاخ سفید رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/139502" target="_blank">📅 00:53 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
