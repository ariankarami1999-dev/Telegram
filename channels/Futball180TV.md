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
<img src="https://cdn5.telesco.pe/file/NlRYHpfbA9eTs8I9V2rRcsntGC62IRydWo03sd5Zt6THfZ4NUaU_peuzXCT7svTbwHxXR3tc-ad6tUBsaWwp6ZGQwVArUloMGg8-C908ojgR3vG7kVuzJ7XTheoNCyYTvPeydYmyDGhoJ-VaWE4Cc-I6o3kqMwRgO15HAxAj6dMPWV-x9WRD5Xvfg__z6D_eit_stShGKDM_XnOKb-93AlG4ZzzbP1qICZKZNbRMETzYwREHiFlSC_IXNFrKL4KQdGzZRBc6_twA2zSCOzNQlMn63LDObI4Be0e1FCLa_OXBX6bN9PnkL6wbHk7ZDsJ5SHpnUMTayf73Bve2o_EhCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 714K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-95610">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbB5t5bvUxUtZPzzU-BuqyOh_H3e5GtYmwZWr9mhFfSsIDa5NYDYPBOiboqm8PUUYfHTNnc7dsMJXHQhqVV5IHGDSqiYeUhUBL5arwa2y9P1GR-18VN2xpAIMrTFbTOQx7rGeSYwQ5p0DQaxRCufpnZl6UPHneMoEEEG6D0ZbflOTox-gUSE1rY77CZySLdOobQrgfF5Je6bupgXc-dN0HMnYl15M-tL2aa6Sj0pcMoD-Pv_V4QJqg7ypu0UxVM_yu0j34OaWXd_YUKXDJV9gq71AoHvB9r_RB_4cSJPM6exKYZTFPCwrUvTsaBJFh_Vkiv9Zxb9pFVm1E-wL8ecYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
ماریو کورتیگانا:
مورینیو دوست دارد باشگاه رئال یک مهاجم نوک کلاسیک شبیه خوسلو جذب کند، اما این موضوع فعلا اولویت اصلی نیست و برای عملی شدنش، حداقل یک بازیکن باید از تیم جدا شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/95610" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95609">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgivY98dYHu1aP4qO9WvICXDPSXjV3I-8J0bEYWD2QXqmtCe7u2ilpFgDtpfo4uunS7Ritz-JeRA1i1aFbcyPhki7HWgHMKLyG4lcOtoiJS_fCjONKxF-mAHbvf8owXRwpG0cMkQgjm4HwF0hFmwCSvDBF6DFGS9IcA0MX3LZhDn8QKNDUUSvAhNysaSForwzNb_DCDdek_eVHTe4cJhpwcNi2NkZhLN1RZyyOW6H-aEwYkARHaM6YDqBElh3SOGW2kDc-lyakG0hGWV2WrYpf7aijeN0NdpCwKapWYUyjcA1jdVgJM4XZ05_T0Gy1RRtuGNf6f3M0N7GpY5rkrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7 بازی آخر مسی تو جام‌جهانی
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/95609" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95608">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود/ در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/95608" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95607">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeUJCdcdHT0W_5ukCJPB42aIJYfnJRymqZKJzaX1J8hC0QrtDSxxsP5RA2emUPTAxxDJmueSDQTdHi9tOlEyjx30TxH4Fq2iNDgzYcZaEjKnvS2ksYzTbst0zU0Gs_4_GS8HS6hwUlJaXtBoh8WGt0Q4bnd-oylW5TV564RrLEaVOJD7FVF7nZaaflUqva6GoMGbQRBzU-hzKzKsvBfQ5Jsr-coLCiVFpBJtLuvNMRuF2d8r0RAcrhqx3fE1tZcwrRxpKGZckxXtXdqmJrz5oxII9_4l1kkG1pnql2np-PJ-3wBA0UOWiEtA8Vzkfz5cVc0bu6fIUwwOA0PFoXomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇦🇷
زوج آرژانتینی با یه بچه تو شکم اینجوری رفتن اسطورشون رو تشویق کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/95607" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95606">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال شاهکاره
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/95606" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95605">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srPT8VmAf76DxD_NR9BxmK5JmX-5mlvNPgBg-R6Dssa8s3mDrvuvmOY3kDygZOk87JeoW5FXdHEbiSFmqWMZ5-O7vCP8wddcRYEl0I0tn7yEMshFe6pzQQEGqoXjtvGo6eFoEe1tab73X6NtDtqypsL9qJfqKYyvplcs7Ansi3R7kJhVLd15blih-QT-u6mFuPeS3UOdVH1dbvptqVn7d40v7abbWTPbTeduUU_CkhQ-datFfQPXe6qdhGeO7tGZXldWeaqHRkzdh1TDfUSA83TaOqtHIAYyvI1GlgtpBr1YkB7d3ixBL3tq8VhfAl1lknWTE2HN9Jt-wttYW805Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل‌مسی به تفکیک هر دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/95605" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95604">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💥
🙂
یه خانم ایرانی از مراحل استادیوم رفتنش در جام‌جهانی شامل حموم رفتن، لباس پوشیدن و ... برامون ویدیو گذاشته و گفته ببینید
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/95604" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95603">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌مسی ببین کاراتو دل کیارو بردی
💥
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95603" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95602">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
توصیف عادل‌فردوسی‌پور از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95602" target="_blank">📅 12:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95601">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
اثرات‌هنری خیابانی در ایام جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95601" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95600">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
پاسخ پیروز قربانی به اظهارات یکی از اعضای کادر فنی ایران که گفته بود: «شانس آوردیم فجر سیاسی تو گروه‌مون نیست وگرنه کارمون برای صعود خیلی سخت می‌شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95600" target="_blank">📅 11:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
خاطرات جالب کاکا از حضورش در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95599" target="_blank">📅 11:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌رونالدو بالاخره دختران سرزمین‌م خوشحال کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95598" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇶
#منهای‌ورزش
؛ ویدیو افشا شده در جهان از عیاشی و عشق بازی مدیرکل پروژه‌های نفتی شمال عراق با منشی خودش که مثل بمب تو جهان ترکونده. ظاهرا این فرد دستگیر شده و وزیر نفت عراق هم قراره اخراج بشه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95597" target="_blank">📅 10:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
وضعیت بیرانوند دایرکت دخترا بعد بازی بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95596" target="_blank">📅 10:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVSi-X9JX9Kueru6VzoZUa_1oAlaOf-2CBRWdmUtS-nv41Qu1x99YYtBf7wu-zBbFTNrBo6FVwlZJvCfd4w70erAt_-MlNyC21tjTX6ywpN8Trio8GP5jDBMfpQrDIlGh9rEMtq_uz-XsXncgpu-fg_qP4uy3knAlbTyDBHHqh5QCRx5s2-2TwA3VDjYQvAkteYXhcR4Ka0lFJJ0ptIjA2edxsWnQ53FksAW0fAJXU32MSLFF77Mf5ooduttdhR9JYIe60G0HqJnf7yHwmLM0uZchl4j6Lq6nyVRZTSv9TcsDAOVXmzFpSVb71jSq4QBr1BCrmc1hIRkTZk7DOtCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تن و بدن بوفون تو گور لرزید
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95595" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
حسین‌کعبی: از ابتدا استقلالی بودم.‌ پس از حضور در پرسپولیس با برادرم دعوا کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95594" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95593">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8
سال قبل در چنین روزی؛ تونی کروس از زاویه بسته دروازه سوئد را باز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95593" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95592">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه بلاگرهای جام‌جهانی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95592" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95591">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b286c983.mp4?token=Qy5pFvrQUMxL5aIqaiR-zyicR-Fcfoy_qEe50ensxsUipyFz_Fey0y4fu8DnbD1KHDORRlS7xesS2av80-GFQb1pUkHt_eENjCL88WzGA67N3TSBstNvaYP2QzXmOkulv477YvXwlApdC5F1gxXbLlN-oPbQrFT_s2a5LJnTJVhycrQpO_PYaFkN0jpBRl1_lxzJ8LyOpwfOfaHENHdibuhm5K-1pWKyN_rJGfP87aBjz20kik17y6xZ8l2Dm2eN9EOljaVQIORJe0-HaVrtWkYHKhIMddias_ioOnbNlwGwIREEs8ResN1WAvVTxNaoCDkViKeRXbNFZW-XUIb1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b286c983.mp4?token=Qy5pFvrQUMxL5aIqaiR-zyicR-Fcfoy_qEe50ensxsUipyFz_Fey0y4fu8DnbD1KHDORRlS7xesS2av80-GFQb1pUkHt_eENjCL88WzGA67N3TSBstNvaYP2QzXmOkulv477YvXwlApdC5F1gxXbLlN-oPbQrFT_s2a5LJnTJVhycrQpO_PYaFkN0jpBRl1_lxzJ8LyOpwfOfaHENHdibuhm5K-1pWKyN_rJGfP87aBjz20kik17y6xZ8l2Dm2eN9EOljaVQIORJe0-HaVrtWkYHKhIMddias_ioOnbNlwGwIREEs8ResN1WAvVTxNaoCDkViKeRXbNFZW-XUIb1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دختر ایرونی عاشق مسی رو ببینید و بشنوید که یه ذره بی اعصابم هست
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95591" target="_blank">📅 09:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95590">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZh94vyhr4JyvJ3ZR4tYrJwvhm0LNdH5TumZDikP5_g4l1RSyoM8bCZyY90whlSJC3Pwm4G4btcK9UMdlMP_jdrC5nje1U7jtgzI7qQ7xaRUprprtnOP766R4XyPQsILoKSU0bfOZXs-ZrlUDbmeF0G8htyVanVULqL_CU5muI1_kClFZUkY0J9ZL7XJ4RdAxuMUHrHTi_Way7USROLKdhN28_rMXZZ8m_AzxhS0YNgimM6VpUpJUuHSZ9L3l2PG6cGdrqmixhr9j5LT5uKvKzUaO50myt8vpnOCm-TI2dMyQxOi5rC9OU_iYjs2N1cFNvCF9o9o9PJ92Kd6phBzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو
: باشگاه چلسی طی ساعات آینده قرارداد مارک‌بالیسترا ستاره آتالانتا ایتالیا را به ارزش ۵۵ میلیون یورو نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95590" target="_blank">📅 08:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95589">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zxkfd_tEqaFjjraiJBEjRGZUK1IM4cRCOwbwuuepLT8fZ_IO_p2bp321l_Ld1PfHS-8ntjXEY5AcgF9QCv404958BpoW-HLPE6y0uVWuJ4tFO_zrTwgYjvvbFzJ-0QEgcHjVUW2S8feU9eAYTkdFCEzOhFbqHUjCEIdZuox0_iJGEfXIATZCoRiS-hsqaSI0ieGyKDfPS2FqUY0mIe0mk4hvO7l_gzoiYlptqDe--4YUQw0ODhp4dij5DdYpyuOwMKe5Etwogfh3h2I1xKZ8OvLbu2LFCWM3jBzdd4JDEgIWAPHiV_X0y2Rwjv9MGsgPwpax5EXUd2J7uEOl68uZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
مروری بر ۱۲ گروه جام‌جهانی تا اینجا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95589" target="_blank">📅 07:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95588">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzxi7tclmeyp48QVQfjOUU_G8Vdv2OQG9j2Hjvu3uMis0eGLHs8TChS_s5A-pCpD4vSICOwFZ4BS96H2FOOKZ3d8yFON1t8mAyEnuuPdR0VvauSJJYnfRO3Kr2bWtUPlAyX2mihh2kMPi7iD3Kr3Mfnb4ejgJ5K4O2qUbCGoYkK-sB_lfltSJs4hWxeTaHEz-jkV88224aD9lFNkorp1l_cXznBvQY3NOCs-dsEnWkEYbS57nfRXwuvpqKxFT0sYupfPThDtSq1NZqWe9FvrRv-K4kTgTj2IyuTseRCkkR5QBs2y8oXean2zDAEV2NGJ6eqaLu8hNKQ3amli2CmcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول حساس و نفس‌گیر بهترین پاسورهای جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95588" target="_blank">📅 07:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95587">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwRFt8pE8iQ_8eXTlQZ2qyth24PkaemvdrDmzFCC4URw4kE_q9nmL1prBVygZOho-8w9rLOj5__1U0qgORef2cOJ20mO0As5Y685bRi5-1aqLUgxbccqP6-5UvXpWbZ0qwcDL6l4uRZvoQvL8soUBBpdme5_49LmrBUZLo8mC5r82DytiOb5uaqpuu_lTwkhE2pEbw2C4whPtqJmEmsJ7WCOt3QsG8_etbR--Jz_BKkOA7_1Is4rWePBhaMwmGr1f3x_LhNTxxp7DDUON9n8ihY-YZjHxRUu-P_2z1H-m9mG1gEZr-K-VSc7D3FXqaDujUaa4zDaCuNwBU3Q8RTt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول داغ و جذاب بهترین گلزنان جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
لیونل‌مسی ۵گل
⚽️
ارلینگ هالند ۴گل
⚽️
کیلیان امباپه ۴ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95587" target="_blank">📅 07:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95586">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpFemvpzufO9KkzZ4nfKqXM9mVfsJkTw9tXm3nHy6mHTHOOIuJ0lHt5htOYZG9RghnwMSBtwcmZGvnwVqzYTF1drLeLyIexIRiC1cKZnwZxrCPsGkXNleLnFAwn2WSVlJyp8_7_AHO3sNeMvvdXPuE-CcHlpLKZKNfNTaZMc6yzF-BjBGPtSItwANkMLlP4yEpkRweRum7EnvjZCNrjPwmeyXNBu4IO3pgu1_prJEjHH2eCxXk8Vb8fIZSJ_4fkv9gdZ4WwC5oTlxjplt3lXQK140K3LhvFnUA2DGx4qaE_mvwmWts246_6cQrA1cj0_QS4egcRcGqTGHTdcTJmW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95586" target="_blank">📅 07:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95585">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgaWmxOAPw5q-NTQM9H6txhbJtxGANZeAJrWJmuK9kIcYnS-GhD4EYF4wavt2xwBqkATUv99nJYal4b0Xw_WsfnlYST6UN5YkJks3AonloxFDZLMnt9QnreC--ZXIWctwzzwR79kdkBUfZduQ_0-mtiELskcyuBvoU92NYWn50OF7KYP6iNsZDu3rAuAOH04IULNmQsJqjX2T2cw3ilowSIFiIRiAP0iJ3O7COGqr7K-8GL6i8fNw6aAE0yiWCXZjmUEnEsji84XaFxnpi6XA-jYyTa_fWhtLBrkbBLjgTcbAHX_Ty9EJHgxnJPvS8Hm8O5tzh7r_wi_4oGpnUEQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول رده‌بندی بهترین تیم‌های سوم جام‌جهانی پس از پایان هفته‌دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95585" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95584">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCWG9r0owF-5CWXagD9D2uwWUM070g8Xk2-6iBeLW5MydMdubFHZDmtShsPNaINQtpwEUYkJbqWYo5v-EiTBKUTv0V61xlUETGuXDGmGt_SkXaM589NwLnBfUy4MwTVi2-EvUZ1fBXshyxLEetefkXz-YAya6_yBkp0agEDW3VXV8bbQ-50YeLmoGyIQhI12Rnb_cPXES5Jz1K6h80EiI8klv5mOe62KLMMbdY1XYIKc4KE8QtDJJ39Js3we925kGQHDOoks7t80OrLVUHq5D_J-OPAZ-rwEA0DntKoP_ZpOkEU8KtxTBYg2DhlczxVH7mj0C4IIe7gB1UJx0btCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95584" target="_blank">📅 07:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95583">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYPLIB_Ju58cXU1d6FiTc5dDZyaQx6nHhOpMx5bH3hX-cBt93YI2gCl2UYCS7M9znrBAk9RR02rf2FJuy0db5B55v53P16AXolZsQ4gYIIGGFY2FxBT6jHR4dl5kYolDNEBZ1VBuIiLp-xgxxDCnXe7IWi-yzTHmFl6myhLLv6Rk_W9lkpfPEcUlVeSQsrwAvH-fkTzYkEGBVU7un8KL5YKsBkkkSdzCAiMvbGen3gKJYSUq5uAC4e1J95Utp7ew3DTA-CukYSbf1jyoWS4cTDhhRi-XXHOPdPxCIEvOpYD3xScUsC_pfKiv59-dM1EClNkCUatcgWKweBqVTWUQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95583" target="_blank">📅 07:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95582">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=JBppRfqourmByVbsT2SUuacbItTf0_0DMy7O8CXQ9W4QzXG0uQoCgc2QaKvKphjJkUn87Gpj-JOwBgqjFQcgAj9TApkjrCADrcKAPbQnUep03lcuj6sXuKgqpfqTos1wO0UyLzMsUh1AHVMzC4QZBPooxuthmKnGmUvMlBGwFjbwR85P2IxpksnjvghdkJHa5sWxSsYXn-zXfadMcYko47UdUW-mMYYR1GJDafxWmjCpHtbbinUfMnSItUWUYzSQKkA5Xyqh1XbYasA7QY0j3T_6uIUZmPtVYX-JQUR4eZ5fADaKcdJOMoytYaGRMolT-6qFMP0ZUehr5l7G4JzOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=JBppRfqourmByVbsT2SUuacbItTf0_0DMy7O8CXQ9W4QzXG0uQoCgc2QaKvKphjJkUn87Gpj-JOwBgqjFQcgAj9TApkjrCADrcKAPbQnUep03lcuj6sXuKgqpfqTos1wO0UyLzMsUh1AHVMzC4QZBPooxuthmKnGmUvMlBGwFjbwR85P2IxpksnjvghdkJHa5sWxSsYXn-zXfadMcYko47UdUW-mMYYR1GJDafxWmjCpHtbbinUfMnSItUWUYzSQKkA5Xyqh1XbYasA7QY0j3T_6uIUZmPtVYX-JQUR4eZ5fADaKcdJOMoytYaGRMolT-6qFMP0ZUehr5l7G4JzOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇴
گل‌اول کلمبیا به کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/95582" target="_blank">📅 07:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95579">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwinwJvCaGxpsdyELLAzJMDzCWlCVtUtAJmPp9aYo0b3gvU1JuESF1TiDF1xNWi2OftpwWjJJUGkDucJ3NuNuhI7iCIm1H-8lTLPozd2NCwL5cj7toJSXy09mH2jpOa65ceBsmQ0QaK30LMNWU0Odx-NVdXfHjoWrRABf6_sbk-6JczhJcbuOsIYCkFfcCCm-TZxJBNEAjwf9vjvhE0FC1TkpuTdq7CGLcCOlIe8eVm0V4qaheoQHNEWL3d7Ko9v2AnlmAJ7M12ZU30wE84u5T0Muesgj-OfrpV8TdRW7_4cP4VtNcT71Yu1XYegmAWWq7UbxXDO9zVK2bP6FMoiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9Bjapf99nFN2i-aAnwQ5seiwFe2ginGazSkKvLNqnR83JZG4oWislKmxqn-eramfcZ3t_u3HS-21Uhw88PDa9t0zzHKj5MPrn0bUUnjC62kI92CxcrijxZit68C8SkAIrXnRp7OfMi2XU-0wi2e8lJi2rTf7zRnuzAqxdyZkugF2oFD3GdRGqNohQkn2_kMJW70V-kxuVRPKILYp4wOYoVEqwMx5_gRNLyNPU19i6G70ILVVzuJ_o2njVS7vTahBHWJyyJvgB8T_Z8Ws9v5Sjt3q-twE0KUNF2a7LbdSgnMJPRWRfI4XgMP2_UZf4M4U580Bq3QqflmVbjwgk085A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jS9WjiS2QjVXjFKeckE74IRm4nIxcDHSfW8SBkBmffvN1d6F3mY2JQba8qaTfrywDAZ8cJ3jFqy38LHTO87hv-3XXD8qlCw8Ttc6B32ku-XniblbA4qzTphRh_9g_EW_K9ThH8qFMuy51dyi7mL1v5B_MByUAPOQIcTUEH9va7Invthnf0oov1BzECOrw8D6ZA8ZpoOVwDv9He5j-vfiL21xDKEZWR4eeEfwiJlSAgFD2n3oND9BAoj8IYWaiappB3LBvdajFqrJCfuPaojXjBMpuiftNMAJH7TveNNqr48GVnK91ciFYy5dn89OPVelzQC3d-gkn6I5Wxp5ITUi_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما که خیلی وقته بخاطر خامس طرفدار کلمبیا هستیم
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95579" target="_blank">📅 05:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95578">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95578" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95577">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گللللللل کلمبیا زد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95577" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOKTm9g8GxQ7IaiudAuXAEptW570ePWq7A4hzaXBgcVHGVOkHpaMl1YA6ewFaBGe6I-2bonAm6D3GuNxbXc2QHX4B8nME6RbkkD7esFwojwnC4P2zaYsQIXtJG0Ua2nqy-wZ0M3p46wp7FACyUs1y3XbsjICQpFHwGj9S5lSzYomHK4PlS-9_HFgUat2XS4LuWwaXhODB7uQSBqsf774KIaWtlNSjigIf1AIexeWda3j1j7e125ycNzpTEZ131ZDzOWIVj-lPsvSLlsxuWdxyk5qCO2jDAtEg7ZWeNAyQ2t0as-Yn8VqsoWQ53ensfrV1Vjea-NaOdgiMMhgCVUMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3xMF9gelCIJ98mJlqeZy-3KdTBYlcvkvmTWO0FVPWn4i7Y6quD5qKqhZ5c6ytE8VSVV2PT0KEXtRpyTu5uAn8UU4KZG5ADYAbzr0XcXaD1xMbs5vU2aXNaks6ggY-IBa56nVSA2AjAn-PdfcWEyVchkBhfCAFXRilKqBIrFbFuenqQYI7ezefxqKffEwfkdiRMjAfYGWM1hUN31-Ftz1Hu5-Ebj0RkIe53qw29JHg_GekzeJj8mV8xUXSct7UizNJF5d72-3UG-uNGxJrMk0EVV7cKIseGmZozBCWz3R80xYhNdD4oRFCfaReTwvNqbE647AsUvKYW88A_HeuWjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwy1u5d33JijGkMhLUBLK2IQ-RmX69RZWLJPaQK6NhbR5wHtM3eHQr13cFS-P-Apgn2SJ_j27C_WCQem4D4dAN--YftMtOYpJrlYYvtSMEijsyM14E2xq16-h9hJ0ECfcluWMNhmjv4eqL0OVPUo30h09pgCxhtN0ZjeUcBTugDmRy7avVRKz1-9K573GzMOvLOtT8Kq0bEAl-YmgS3iz8xsMePgrx57OeeqhYcHzF0D4KiQ9tLNFZ8gSu54sp3UeBDhJGiAo3IEe3dt7nlYDpQRxMlZ5VSzwbp8rTaUjDIMQ0wA5k9Ofglh-5lWgqA9U8XAciH9FpKu9hTwapzaxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
جشن بازیکنای کرواسی به مناسبت رسیدن شراب ناب به 200 بازی ملی:
⚽️
200 بازی
⚽️
29 گل
🔥
31 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95574" target="_blank">📅 05:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بریم سراغ بازی کلمبیا - کنگو
تنها نکته مثبت این بازی حضور فیکس خامسه.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95573" target="_blank">📅 05:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAH1gWEQ4sL57-tWYl44GV6f4_uqn44C7Faqx8OqdDm4-jWnHrOhSvxFcFbscf-Nae2WeahtokjMWCWg6DCJvRMh6bsnBR_TuNB7yVgOzWypQl3NXhvxkHbH0A4ZNwf7-00Fj2lDSFzSY3W2hyFbxD5la1H_4lsPATXEG0P_sGVHekspLb1EyZMsC_tYt53sPZ4FmHtfFazmuwoT0Me8_4By0a2bDKQqRWznBFjqeiqOgY6v_Acr0NXlebCAWrQU-5tT-gxz6-nKfYK89a5qIj7e2zALrezaEuoqVZd2yI2qM3SHq0hR-8WF92zqiHJZaU24DAaTC9GHXl2NjqkrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکراری ترین عکس این چند روز چنلای ورزشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95572" target="_blank">📅 05:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkPuy47QxqGRqs9qlHcgcCxZhCqwd7POk18ynu4P8gy9z2bUSRebwBJb2JCxF4--iO_XNn9bKzWrdzsFaeHGSRkbntx3kdTJR9yJTLWmz8doEoSQWHawuQjAkIujQl925wmfKsgjc3nOLJ_ppbTwJmLJSaGX8oowMwqIz6L3kK5xW04_3HpYCF7gBDEcsw5JZ2VpQhKUoCpqw3l_NrXJX6_PmcxcoeyhR1LDUUIYeyKsabI7qtgKEdbyEZnL8QyW_pAOfkieF01FizQxbB4S4pSk_E2xv4GouCdo0n_n0soo3wu5fuhNVf64X4w6YC5JYSn_Bsfh_L9Qe9Jj9ctI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3A0zicE_Q-hJIxLT66-w_Dzxg3AsBiss1nXeVYgVewYVEoF-1dFB5xjLkDP5OVnjmhJ03ekB9EV-CCKssXFxPdu-V2Y0Sj2yFDGrOdMibdMEMOQrQ3bFcWpPiVMJV5ZQ-ysc-IVAtIvjQPr20r5yG6jxQ4bjSQH9C6dUZs3y2MCSnRF8LFA-VJEoKNqsnyN45Gnq1FkKNCgHl-XfH7tXVVtm6kLN5K4OnKScrsa-mKmH_x4pXmIu7rWcdwjtzJ1wFiBydO_L4SlZsxx4NItv1Airo4eEAdB_uT_q_UBUQCTtfK53pV33krsUEL1L0YZJ9G9b_OrhFyNErTiOBQwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2PhKe5uZExWsaNz3MhqRcf5O4fzhDAMiZq_AqW9jaBLHcWGWmfd2nTBtozF2eG9hPUcgNP-6wSnrnu_yQGbAoTLRPF3voYV8IsJWW9nT2MQthzVIK1jlR9sSnbz40Ayc-6zxuExhYfIo73zvONGEdzZA_UFdBQopB0pY5TymMkQA0c_doMmX1UPu-kGKlxa_Qc9XZKHsnXo-5Nwom8OmHFjlOTIEdyWzDw3ukWUTDcUcMprLoPCnJxboHkIIcPVLkzVoCG6pxo-Gh1YYQ5936FTiltTz6_RPEe-S1V40BSnPLNQYC2d5kqQf08UGHqaTfk9iZ8XmXsswW7bS61cEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk7OmLW2qR7SzpooaeK0S_AfURi-bVU-ROWl0b9BhXuLLwGERfqCLN5gRHs2MJiMdbGyeNPATDrSJWZ1Uq7BfVDr_dPQXqZ8x5jImy8ZpFkJDl80gGub1fWtXxHjbvvj06elagJo99rcwySS8mVrR9gf0PXrY7RVNdtxYpMi6cozxzGFK_rrsXy2IsTwgVLd6uoQVg2Qy_BctXfgk52HPheam29sxM_0e9jU0K2iLIhXF3Qbt_rHex2ioyA5rE7iPcvuBgTKHwZP_x4UEtY-Ihcxi3tXwy0vMN6UAQwF9w5Yc-5Yx6Mf91drPn2pA47EQDb0e1F9yUFPAgXQd9i3UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این عکسا چند سال دیگه می‌ره تو دل تاریخ
🍷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95568" target="_blank">📅 05:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5u9dpHVgmAtJPGRp8sExyGg6JAe_OvBGChDCe62aRTrhvqUoycQGSCdQzm-vBCEIk9OehwZg36U0qT1zL9d6UudkECOeEw6AFZyNp0cSd_ApbWmviNqNEyJgUn1196Ct8hEiFFCBexbvDl5nhHZ94wcrBNF_KVuh9nX3dNCM6Aj9SmeREoFgpmo_jbX_0_HO4HWK6qkYjq273Mort156kGN0CDv3xiT8pJ6pZQoQG_x8PnksFFnDIjL5zzMptEU6L6eK47ouFwTSGZJ4JRICSkW9zM2SOSGzADmx6YWUAsoDdsNiSMYDKWs8ql5ZPOJl02Bkg_9xfH47BcYZNBvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی:
نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95567" target="_blank">📅 05:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/of05mGqhytEUjJ-5p-D3u23MsFVrTUjAm3lvV3p7sOP-3XpES3497NNYQq-ev-dkX0wxNcVUXzykwBHHka5nvh3EDKtKt3nvZRPHNLxHDqFOW_GVgaxDiQHWp_oQnjlKvRIiwDnKZwVEs6aozcHEgx6tHIHsDZwXXKguSghFc64eTeKY0o2AcIT53BRLClo6hww3ZI-rSeprUEEyQjrV3AyW79ESmc4ZhN9S8fqxttiYVL8NDXhNH2bbOwrvhweC4srHyOP2d3k5rHMr61bmyNXOCf5n0xAZ8rv0SZi6la9J-0WrOrXQQTYUCgTXKt07Ay5p1Fl5i7y0nsv6qcVngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVVIvSepcoT7PsEvGnnopGleJOhqkWqrmmcElb09aIMZbeJUB0YpLYuxiWRVOtEpKlKEaugXLqNoox8VV4DP-J5NnxKkXE-S8tUn8oZg0KsYxT6T7xnB73Z5d0mAgc3JouTn4f20_o2U5ZeAZAwzZFR6_G2hFVuG8AiZ6R3-ZbQ2GzbJGA_FwsoNZw9XJpWJjSmb-Xc-sHpzIJZVwCyhePl5_dqc0jAJwjlNR47ckhKWbV66EoMCvQ1DB-EBKQRCJAuLwaTPokrOGJIRexwje4MsBWw81aoJJlLB2xZKVqeJ0_8AJ9qrYJgakprRMJumqP3mm6NanNdKtlKUMZoeUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇨🇩
ترکیب کلمبیا و کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95565" target="_blank">📅 05:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwYOSqwdZBynj5w3who9CFKbpCHeB7qcQKpGsYb0C13lOVa9lB4BC2W9V7jtsZMbeSJAvvh9ILu838I67nfVb_YQwuILwNMsj_KVXLzUafCJfnlHvtVPSmjQ7kjGWIb5oWdPHAFILTE9F1Tb1JKM1jy1y12ODi_B2Leuxn48pT-JbTzOkK2vgyHoZDeGlGIghs8kQyhONbBD33Ae3sj9YulbwIcp0YvXl7vJ7uSnNI8pgs46AYrVbH9crycGz7DWNNUme7UK5KotbtT7OW-B1ANn1OGL821FuJNgdxop_bQDubm3myyMgf9jAcl5JXfrK_4_wqdWoXnyjFcm0ojPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
فقط ۴ تیم تاکنون در جام جهانی ۲۰۲۶ هیچ گلی دریافت نکرده‌اند:
🇬🇭
غنا - 0
🇦🇷
آرژانتین - 0
🇪🇸
اسپانیا - 0
🇲🇽
مکزیک - 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95564" target="_blank">📅 04:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbUzEhlZUAZZY8bGfcDLxhTpZe9eVIRJA5p7pTTrs4lb5H7KV8iUiFMC9nADGvNEuJNZ0BG82zsCQXPOgp0IKxRtST5ohyE1ISGx4HH-PRBYZo8yfWQ3HQV7As3Mep76O7TZEk4MVEWnXjLDyFOYQxTTiLssJB8I4IpLrkkiAS0SSqZmz-ZHkFq6Kb1ykjJ8Yz4pKmr0DExjnHvSHfNj2wdEWT6MiBCZpG1UeTcLqFGE_0nJDdNDUaDfzL5wcPkFpMojRWfh01iRs_dADu8rzO66qMG0o2JaFtIFi0VfjYRpqnVRKbrWPi9sCsl9-i4V9CoLqqZYFxZyPdk4AgFhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
❌
🏆
تیم‌های حذف شده از جام جهانی ۲۰۲۶ تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95563" target="_blank">📅 04:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqc5yKRhUrXfbQwe9UXD5rd3tE5BNJ41McutOmKwemvAjnExKvfM2_ewN2SyPM-imGk7PQjggfK5Wsjq-6fjA2PUH479B9VClyCMB8bOmUJXIQ_vjjicNqlmwKxu8e7vGOjxlf5mlOHOjtvRiCeO3kx7GK7wlWXUhi6VeGJw8VK3pJXffSXT51mbLq4IgbicCEhpIJ3TEr-BrhkcqqWhTg2KxNOb6KtanFMGhx3p1o6UHk1bTDCO5RibuduX1QlcpGzaNgPo3NmmRVMcsKP74bQO1QwW1v8TSYu1CwrHAibgeDfVsw2V1iBWbiUEORqBhXIIJPQd2ZmJJEIYTyNRGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه L جام‌جهانی با صدرنشینی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95562" target="_blank">📅 04:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVoBbIGITMwa9_nkOh8_AMTF2J_xLjB1VVIltSqigUfUz9cmYhpQbVGSJGvyFH9uoaQNsoEy8CG3VD5VKEZINLEwFHXBDOE41sgTjEfNfh7ch-o_LpVgMTs3bt3yWf01vUisAhFnS-aDXvmEPjrACABFFi1vxYDoWGFN-lEBXnN9AsbdFrjSnA-sCVULWYRwodaD5pdq1LeiliEQkZ5wNMNIpTxhCvDauAj3QQY3zZsX03ObI4XhKyL7jsuQpXwXKlcqsi_HdSp13aTJ8h4Y8jc3tG79h2M8J8B0GwdNVSdT2flXIVKweAW0JP8G4xhXZn6AvwQewYJDoullEhCZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | بای بای پاناما؛ زنده ماندن امید کروات‌ها به لطف تک گل بودیمیر
🇭🇷
کرواسی 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95561" target="_blank">📅 04:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95560">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بودیمیر به این شکل کون کرواسیو نجات داد و تک گل کرواسی به پاناما رو زد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95560" target="_blank">📅 04:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt47UDpcbwBB6m94yYlSVQIA_jGtvm0dma7pyBNbpyJSIlU-Txb9-KKiR81efF1LjfYRzZKolUILVXUQM5vO1t4antVUfsgQ1FHkMduG3HTp0Mn6dkyEcwyxbQxjeIV7gfPD_C49pZTboeOpY8NSqV3JvZqWonJF6gy2pYwfYvS-VVXdTx4WyesfU62pu6hUB0LXRUFkYdmeeLoHWG3vesRQwqAiUcRTmcbIlw7z6CPXrmWYhGoBGtyFvgTYTkmMQsQvePwEjSvVT1Dv-bHIOBnBou31UmxzwHGflHgeetXmxEMS-AAXtD_h5n11Mzy0aKhWw-ASQVP03UBfar_vjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
جولیان آلوارز احساس میکند اتلتیکو مادرید به او خیانت کرده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95559" target="_blank">📅 02:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADMgJdezPKM2uorx5rw56sDe61ZFobrMEVWeFlZIxGl7pwuvXKi7vdVk_Cy6vV72aQx7p-wEub1BuehUkZdYCCBgvam_SqxBxKAsNHLbnzoDZD6I3-6sIPkjOTQFhqPnIek25daebb-l0P_wbOK7G2dPBuGRL7iqt6hIstU2KcvcX8UnTF3sSbEFQPIvbXgT1-JlmkHTP66-ZQ8vNIpBlQLi1bmsYIV7BF053cGe5CVBpAf8qwVP0lSL-hrekjhL4TWWOIPz8jizMkRtPXMWbe5qkja_6ox-smVuBhrBgaJS_91ijuCkaTdeELwTKlG6DajTpnBFtp_FOMtRGcKp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
برونو فرناندز:
کریستیانو برای گل ها زندگی می کند و ما به او نیاز داریم که بیشتر گل بزند. او همیشه یک گلزن استثنایی بوده و همیشه تشنه گلزنی بوده است.
ما به مهاجمان خود خدمت می کنیم، نه فقط کریستیانو، اگرچه او سلاح اصلی ماست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95558" target="_blank">📅 02:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvAY1qSWQ_X5RyHdjqh7cHBQHO7MuieXg6HlJdZVUxOtOTF5HjuByai2xDs9UsypuxLBoQrjAjSHWBNliIZuUMVBk4VUysDN50EtRiIaF6-YZJn0N4_Hsx0ZRXF6haNBsKhCKcsoWqx7dZZL1ANIgrr4WVJCDDjKuWUibUK5CT1pp2vw49NTbqC2Y55rgZ2JodFm-gqjuknhXR3QOAO1oU6hx1YRk4umAgsSI_Fc1fJvSvrkzHtcGKGcKuzo-KzCfW_xa9Ki224YCnqUh-7kLYwHTCoPCHjQzqEnThja6OIh7PfB_jmpo849K-rvnPd4uoh5U9cJdV9h8CJMlyNOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v25c4RS0KlYbxO_7Pl0e0nHvk1_NF7nm3ZyaFQ8EhmhU5Wb681GODtSCxoltrGw7l2_6Cne7NnmkXONM-t3VZcViz7zANT_4YFDwpel1gdwW8wv9fZUtUuPSPoV7LrYRS2rFnKgEwoUiKZoNTUWRNr6Tds908TaEgYdv8oBt2yCa8pviSE_T_dXNCM1_OWrR3BF54IHLl2ij_F8PKd5sOh7in0DCHw624JC215QvQBYgfvbSwnF89-UNYPULQ7fS-pFInGqarDS80PEydXiftetpYWtfbZr7rOnDyrQpaFVn0QrlSIt3-tYl11PfbHynH05oX58ROfgG18FNyMoj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VK07ZaAksB2aKRWWm7vk6p6hwJPcwSRBItic_oD7zpm1k5vrMJi7ckrkOiE78NtlfVI8iy83S4ND7FzhmZ66PWDPpkCvgHilvq1RluC8KCo5HrYZqry9SIsNZp77rQd7iT6A_rSfhZXCv4l6_3hBhUvN2V-Hwu3PveK6qlKceYD13TNzlQhJgbaUSKUSiNLqWul1k2s2JGdoyHMWYj6Mof6ZK9YwLJOi79CFoQJN-lFQMxMkZGwWVerxRZLjwXJc7UrpfaEXOGIlsTgOAr21fp0G5j9gjLFjwR45BdgkAvOLkr4BQTIqsE_kBJ8I2wg3pqPcB_P0oLv52vUP79a9Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو ایوانا برای حمایت از کرواسی تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95555" target="_blank">📅 02:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در مقابل غنا 78.8% مالکیت توپ رو ثبت کرد
این بالاترین میزان مالکیت توپ ثبت شده (از سال 1966) توسط تیمی در یک مسابقه جام جهانی بدون زدن گل است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95554" target="_blank">📅 01:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc4r6R8Y3BT7LFtBolp04aH32uMMf7P16v0ZAxnsLBL9Xxo2-o0gWiBjqvfBAin_4agcd9ACQjBVf6yqdSy3Cva1M2EQWBflHabn09ElPtSfLpEJIsmyrwwX1SvL0DwFymz2KS4cnetkXDZt5X-lACVMg3BxX0DsgqfpSHwn3PNIJxhJHMaPsgDLjimyowrANN9VWTk7yjq02rJkx-Svh8TMb7GP9F9QjtN-MVPMQ3u0DVPdkaX4Ksp-XBmqWdk4wgwwoPRmLGqb3XDYfykOJVlxP7xTzS44M3rfOIlup-VLmzWG3UbCOzWWib78eUMERk-Ejvf2JqA_5VhWrqGy8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95553" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95552" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzANFafTIxgAci-UUqkHYdxraUvRbi94Y-eMKpRu2b7uzTD11ShXf3KJyBMWuUWADvJQddertoFqwM7fstWCsUxsjqKkjHcdEPUUCkNB2XCoeojp5os_vdG5QEPWHtXfI4b82K2_8cDpx2Oj-9oSUThhJ6uCrvUC7oXbI7YEKw1Pj4VZcFyqNT-tiagGJMgNFVflp96ZWaSf8lq2bB_ZeKshindX5JdAUVI7JE425b4plbEZhwKkS1IOYI0z2-0Mw_oypy8n23T8pnMUpaVYAjTkZY05wBg_zIe0k1A1BCFozRxLdRDKPw8WaBoBlPZBq6coSuW1VaCm8tnjooxMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95551" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxpTSgPr6pMEu7qHvnB3hD-IgICIQDWPdfDUZ4IVoB1WG_AgkVDHztMV_-w3LpMvXMmQmNrsDj-nOZGSDU1mSe3OQ0ni51JyqyqXl7LR2aNx10RtY1tz4B-iYT80TrkZvUi6bdtgD_bQknILPZLfo5RY2da6iHvTTbM5XPl97zthXVVpbYZxu57P76BA3NqR0XghcWQ5ED-NezCR5dUDYA0fxVrdd2JJ45meSr_Fiw2cRIgO6XGlNK4Zz15FNzdjWS_7xEs8tu0GX-DMP69cX5-fGPCILaXudOZNLn_CxMdg3aB4X2_rf4_HaVSljGVMzurYHyK3f9qb--hu40K1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود بلینگهام بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95550" target="_blank">📅 01:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB8Z0Zf2jbzFT2MMotdtqn4bbi96W-3CqVLqVMgi9SGANxTf5s59app2ccir0wHdqThEHADgXvs-Opqjl46GVh7H5VVESzMJ_zGEAtmlL9FgFVGEgeLKNrILnOcoFxyww5MkpmasAmqxzHdklfuZLfCRHLsDTyFe9m4rqV9lFIHwh4iqAErsv4Bo7a5l2rPGmIeIYF-jY_5WtTNBxL7HzFlaafEn1wimFexkFlKGVnT-liYiH0Kqvudhd80th5LiQupoBODZA66k2XsKLuhSquUkzR4tALz8eYZFp-0CYF9zTaFeL7tTPfJZmDRbPtHctOcu4rR6ps7rghT2uxbAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان کی‌روش با اتوبوس از حریف قدرتمند خود امتیاز گرفتند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95549" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGAhZlJZPTZfvaugDM101fmTaxomgKQSHCddI_P0tBbaRX_SAfV_eWM1Ltwpx49RptqazoiKxSrygdimF_cY5q8l0H8Ct_7afSGeq09btburur2q0mXGAVp3RjTPhU2Z29pv6WSTHdHuvlN87I9a-FWLcKLZW7Vp2sqcK9SwDh_5EBmYw1_wEAWSdat0lADV7I-NlDCUQwsXEWWexm5_RjEn6IsUQbW6xAgK9ZEZX93ISdMShwnQ5U9VIXEhNJ_apxzv50HnyXIL8FIlXSPyfqzsyHjTKAE43Rcs6lPVaWsJBmzSm2aUUdXjseBjfC6iSCU-gM6hOMT_6UutLOlAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موقعیتی که کین نزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95548" target="_blank">📅 01:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چجوری این توپارو انگلیس گل نکرد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95547" target="_blank">📅 01:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پشمام غنا چی رو گل نکرد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95546" target="_blank">📅 01:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIFi-tYLaITPyc-mfl5dijwDPA-XA0BgG7ZkLX-r7ngX0ePeCBbnhFVZUvtSe4ItsdpqYHSx68pog1D3DpxxTGb34pi_a60cuyBOKK0W_xmgt-oqfnSbO43YTwBvRtbWGJQ95aiuXdA_K-qL_1ydI90b6bANJRTNEqSg3PFYnZUV4spYz7ikONwdxkQvT3VyleJ5A1kExPNOfWJMeEcWud3XAoQHF5-0-EM2vVvlPID22IxfGhwwW1ujpPiXgybDnMcZP9YzOtOpigSUTnpD3YJxxCyNaKFvCCieUhnHg88fQjcoO3QLJgnzOMQAGzJ4vjunmCb-2DXjy7BlYrjEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇦
🇭🇷
ترکیب پاناما و کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95545" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-jHyuSodp1V91iVtKzCV1l0youcNw1B97jbTeyDiC7J3sIthTYtN8o4_lzHy3kZ_GL02tqkjRb6PtZwAyKAdTv_t4mr2rtZKmajW6pQ4u4cIFvRq6Kp5mQjbaYtRpz5xnV6lMTWg_aRgIsWILQGtzrsdQcQiOiA-Ppea2m2vOp7miMVm5yFpvqsURTe1eZBRp157eIQXAVtGFsFNzxTBdWcrHOnJE0ds3KVvq9641pdgy_wDQkNi2gJXH7_VYF4PtmfjbvC1Ubs60roXDXB6DM8YWLU4nomJk2MF5IiQxGbdX_aT9K55Bv_X0m_UMiSYKtcdsXUKtGPkMHnpw5iFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95544" target="_blank">📅 01:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=LT9JtKqnvPi9y8IhYvxU8R1EoZEU_DUMBfrZgk_5tE9qwLa4nHx3V8CpwqgrB2r1z05UDPbj3XVEJTlmh0CZjOapVJiOT82DLwizx812j4RIdeQtveq4SltiY9vpPwvmAtHaiCI_74QpTG0AIvqewHcfStAq8s6GPzG655BQfhBgbbQV6CJu3WhTYTc7ETpgSDdru2iKa7UF76LUAaVaS6K1kTVLFytbXGM8pb_27nAH10_wjGbx4HoQaR1-im97evjC-0D77JQJSlJdJb3LkDQXi-eIJ8Mp02ezD0nG1BzVbmwOeBlE7nVOvC87xuGN5lO5fohSChfpQnP9X6IY-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=LT9JtKqnvPi9y8IhYvxU8R1EoZEU_DUMBfrZgk_5tE9qwLa4nHx3V8CpwqgrB2r1z05UDPbj3XVEJTlmh0CZjOapVJiOT82DLwizx812j4RIdeQtveq4SltiY9vpPwvmAtHaiCI_74QpTG0AIvqewHcfStAq8s6GPzG655BQfhBgbbQV6CJu3WhTYTc7ETpgSDdru2iKa7UF76LUAaVaS6K1kTVLFytbXGM8pb_27nAH10_wjGbx4HoQaR1-im97evjC-0D77JQJSlJdJb3LkDQXi-eIJ8Mp02ezD0nG1BzVbmwOeBlE7nVOvC87xuGN5lO5fohSChfpQnP9X6IY-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
رونالدو بعد از دبل مقابل ازبکستان:
"یه جوری رفتار می‌کردن که انگار من دیگه از فوتبال خداحافظی کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیشتر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود، باید بهش اعتراف کنم، اما خب... ما دوباره برگشتیم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95543" target="_blank">📅 01:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">غنا چه دفاعی میکنه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95542" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بریم واسه نیمه دوم بازی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95541" target="_blank">📅 00:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3indWf14tjegEkJgdI3r05o2-dvpAdU4l2hVsRMd4ZUFjoWzbFsuZGZRFhj-mGFazTsX3ZmKoJtHKNPix6vQK-vCk0Ap1LcJHzfG8U_yc13-cjSsCEPSrlf5ciGjzNoht_RmZYsnDS0KAuQgt_1ASamd-ycftayeQ1-6rbaWkwz8rKqeJ66-McaWP7pogZvI1uWjGAR9FiTZReOXUIRMRXfrOnd8YLIC2r5bGbvF6oFR-MviDEdQEjCLgkmULh7fMSCK-g1EfoiYwEt6BCGgu5dZagWQIzMKNE5QGBbdvXQRTbanT3m7O7L1Ibcw3A9U1ioq32MECcbR_K4yPnCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالوت تو اینستا : عین بچه‌ها میخنده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95540" target="_blank">📅 00:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3D5o_BXAfbKUUgQbwP0F8YRH8PdgZXvmqp3AfmtjKafthNZrGfDHzTGvvYh8BPRjfGkoP5FZw0pH4hcAcPavhSrBb0E19bWYQAFXdq0KdUg-SEo87v8ZYWaPrw7vZcstDCbvZBs7518i5id6X2XZulFWZXiEfIG0qzce3UbsMe_d0Nj8O-uECuGu9rfa3crDiL8Mc0PXDdH91Bs26TxeISC8JrErW3CJ5m49Utw4HKvq3oIAsalSwrxECog-hBP331I8_kBH2Co01SPyXWSYTTFAz_EAv1tUM5PVGQvbEDzEn2IgC-9sxQUR28C4pRiqpDjTEz_R-ppuRJeo-WeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95539" target="_blank">📅 00:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95538" target="_blank">📅 00:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp1utW3QleCrP2P0bO8DPh7FbWuh3K8t9zm_Ss9282pgliB2G2qo9ECrprAMYA6jwjQPR6ifA55kLSoRKVPxWdc8pB8G21awwyqZvcrgyqoH_Cz2jVBjoQfoPgZcsc6gMTiPcInpsCIHZns_r4ChexqNal76yfmU45RhKVhJrdRgRpXMY4GV04i0QkTd7FUP0_KEr4PcWn1n_Wr9cWBiU4KTIQKDN6MLUc5fSLEsYaAf6qo9VQymI6zZrqt1pluMFfXCX2Xl5pUJ2dvHTC8TsPhtYv7it-gYWe-0lOTdnh99BqLoY45bMMApW-t1gEYMN0RoP8yLuWtocF8gaLTSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95537" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eld2uZjjA9hgCr4-dZAq8eM6BIhRlTJbfHdDzKbWHi8ShHsK6ppmv1zadbv_Nwtm1Wj3EzsHXAE_e4IMVkP3d6bo8MhKt2cD_Qhq8-Tx9FVXeiTVK7dlJFJISl5voqJmX_D-H0z4uwrel_GSUUmJCuFJUDbpyacsKZdTuvRDbN3JLQ_c2rdL5gfIYLhpiq-nrJjnLkVDDuQ25I5HdUjj6I13SI9TzVEIHk9MBv7GnXXAe9VPmC6hvehhmVptP-UeRkSn_dzZPHWgKnLegVzrY-GRuD7OOsA2LLgR6G1WvMtJO92dJkNFOXIDNIyfNkCUKJybkGAq4xoySdRj0Q4C9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
نظرت راجب گلزنی لیونل‌مسی چیه؟
🎙
‼️
رونالدو: تو جام‌جهانی هالند‌ و امباپه هم گلزنی کردن! چرا سوالی از اینا نمیپرسید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95536" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر بازی‌های تدارکاتی خوبی برگزار می‌کردیم، قطعا نیوزیلند را می‌بردیم/ امیدوارم در آخر دشمن شاد نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95535" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/095322bde5.mp4?token=Dx4WDWa836g5PIWb9FVhrQXigXRny2OGxx_GGFMpsKWLHtEU3ec0jXTvXRrDLswf2_65l_TqEtxW4bDO9KNZvRtZOzWpKsZch6fS1G0tw0Xej6ybctaXFzXqUKfrSksXOonlf8KLnEYC8krl3r2smd15iILWFI15LiYAZAnWAtVNtWqk7iryh7pQ47LION1aVtRB99-2vKCCx-jyZDdx6U6YtDx2J-fiNcOQSLEuWYasHo1T0Gx8qLp5I8iZIidfcPkxVCi-rxM1pHJ3PdjkezpChuxcBBtK6o6XkJnz5NkhhuPCM14WI0QhhKs8nMV0iH06wSRbGLNMdumyhyMHfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/095322bde5.mp4?token=Dx4WDWa836g5PIWb9FVhrQXigXRny2OGxx_GGFMpsKWLHtEU3ec0jXTvXRrDLswf2_65l_TqEtxW4bDO9KNZvRtZOzWpKsZch6fS1G0tw0Xej6ybctaXFzXqUKfrSksXOonlf8KLnEYC8krl3r2smd15iILWFI15LiYAZAnWAtVNtWqk7iryh7pQ47LION1aVtRB99-2vKCCx-jyZDdx6U6YtDx2J-fiNcOQSLEuWYasHo1T0Gx8qLp5I8iZIidfcPkxVCi-rxM1pHJ3PdjkezpChuxcBBtK6o6XkJnz5NkhhuPCM14WI0QhhKs8nMV0iH06wSRbGLNMdumyhyMHfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم/ بازی با مصر خیلی سخت‌تر از بازی با بلژیک است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95534" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LcDOeZrRLrAHCw4C_89PE9r1qd8GcU8dgd58BllgLNrINCoNOUD1LgwtHvfQhDjUpswLIjPShECK47W8uJ81TWDmypuYb4Ds40i-W9uuO6EQz0iP36a0Lnp-WhKkMczThL25BdKs2aWwljFmfrEkVr-FoFKXWlM9yijt3sm8za-w3epth1IGJj2SAl-quc1K_fRnp-WCHQQ5E_ClOT2bkwtWPPyUv9KrA1actA038QhYx4VjVQJpv1YjaEV0eq3xmpJKeEyF-pJiZcF9t3nuk9QaA3rHjnF-7SFqLaApZCMh0CjYXu2nhRwAsX-fCGpNNjGGAlGsgGq182a2p-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🔵
همسر رافینیا درباره شایعات مشکلات مالی این بازیکن و احتمال پذیرش پیشنهاد نجومی الهلال
:
راستش اگه بخوام صادق باشم باید بگم اگه حتی ۱ درصد درآمد فعلی رافینیا رو داشته باشید به راحتی جزو طبقه ثروتمند هستید. خانواده ما یک جت شخصی، چندین آپارتمان لوکس در سراسر نقاط اروپا و برزیل داره و فکر نمیکنم این موارد به منزله مشکلات مالی باشه. امیدوارم رسانه‌ها برای فشار به ما حرفای خنده دار و مسخره نزنن چون دلقک فضای مجازی میشن
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95533" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95532" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afyHba68Usk7uEX0a4bdtjrDxH5kWB47Cof_iOLjUuiOxe3qtrjQ6y3G0ES41fGtSwFHGsImA7PHzWLzugmIfXzXU2Dr8gW4CI4qaG8VQDCEzYYcqybOYEYDlF8kIL8vjmenOsOmLGO0Bjs0SWLS2iSkVaJj3RCFqRtbibdJILIHdS_dPXWgAOCoj7z11oxDhwCjA45HRJ5oOkiCi79RCl3ebAPyhyfDw360BDWz7crdhEu1hjbWBOkwNosPyspWLpcgkLn_ZfHk1CLIW014oirheF1JLVh9KWJUGhxgDKAzedrhZzHyD_is5VG_T8ZH4G9SS6yZIuy-WUQqitK1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بلینگهام با 22 سال و 359 روز سن، جوان‌ترین بازیکنی شد که به 50 بازی ملی برای انگلیس میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/95531" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بریم واسه بازی انگلیس و غنا</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/95530" target="_blank">📅 23:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaHzLIdpu3VI_KLUW2RUUw_zjnFYy93lV219sL3NQy18dsYXTcNLRsE9_P5h1M9vmr181BHpM5QnUzTMdE-pkcLT-RIlr7-_MavZJmfPFgrtb_l0zFCii5BcUQWW5TZ2RyinlO3k3OclLcYhpUSiWVxI5wkAbnEJ_7Mp_m9_7ocxsd32rPa2l9phKmPkNL6JWx6GSIPr7MnzvaLhg5TecXGssbWdF37X8BOelLi7mbxeknb7qmm9dUFp1dV7UccKaoSBt6yoCgOFk0ceSTdMSChxIJJFNaZGrFr0mI9FZsEU9Oz9peZKeO1cvhRSr4OEaTQhCBiaEXbD07tCVemKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مادر دیدیه دشان فوت کرد و اون بازی بعد با نروژ رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/95529" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9twMfjtbeoAqi9ha3MWyDBWHHhdEVifAHa0_5M5SqVqp6zmUMYHHRLk5KGkNt3S1nqFndfevH6Dy3uZPy4j2EkhVWC092Cb6fNLrQMsPCP2C1ID0UhwPalWntHh7BGB42J_fQ9ZUfGsmCwxZt8uSekSdvhdZYt5uiXzK-Q5woMatEsx6SuiBa-eDFCUt-ZN1FY0faxWcY6bJYOGQ8o1GF4H7oc3QmUmrW5fZRAwzfqKhQxrrPw6cwQuAptOUGWg-iptsxgPQQoSbo8U7YYhe9WTmNKGymoGlh-5E_xSeujfaJpbMDAz0jILBd_fSbv7tGOM5GopvN-ogbZhJ41Vng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کریستیانو رونالدو پس از بازی:  "ما برگشته‌ایم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/95528" target="_blank">📅 23:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d5f913d17.mp4?token=oKEB37FRDXql3I0Jn5QvewLf8KjkEusgplsaGX3l0VUIKovCN4ljnxQi_A7S9eVkQP_3TqRXb2ApdbLOsnVHVM8-yzYVNnKVM6uf7icdYUFiHtUuijTsUuhrGz5X4XW46vi6NqtKT1PZ0HUcTfZHuBHTQi5wZkIArqRpNPwgCS6c9uTJJ4-4r8MbXeddT323WPRJMjxjj-IorDETUctCeF1F6za3uCLbMDO6YKmw7cOGHp3dAHEJsU3Z-VmTKFPh_twT2Bo7PNn3a6KSkQF2Qxh20wnsHS6ZhnzFcYdft5LVBlzEE_oZp0PL8nVkVkqsrV2Mt4p5BpSHNh49eSwLog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d5f913d17.mp4?token=oKEB37FRDXql3I0Jn5QvewLf8KjkEusgplsaGX3l0VUIKovCN4ljnxQi_A7S9eVkQP_3TqRXb2ApdbLOsnVHVM8-yzYVNnKVM6uf7icdYUFiHtUuijTsUuhrGz5X4XW46vi6NqtKT1PZ0HUcTfZHuBHTQi5wZkIArqRpNPwgCS6c9uTJJ4-4r8MbXeddT323WPRJMjxjj-IorDETUctCeF1F6za3uCLbMDO6YKmw7cOGHp3dAHEJsU3Z-VmTKFPh_twT2Bo7PNn3a6KSkQF2Qxh20wnsHS6ZhnzFcYdft5LVBlzEE_oZp0PL8nVkVkqsrV2Mt4p5BpSHNh49eSwLog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
ثبت قاب ناب این هوادار از صاعقه عجیب و غریب در بازی بامداد امروز فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/95527" target="_blank">📅 23:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqGzRdJ9WPvJ4kOW0Pbo5INEsBiBjGuKgg5HaIvSNUod1Nw7c99WrfzOJv-_q09qGWq-VbDdzQjdSfjpmh82-DwknPnhdJesMYt9yJ6nBNmqAoNtxtBPEWCpIOLeuToXNpIbrrQFsU_k5OACd1koHC0KjOaIdeaFhYxjvdO0QINBajGeQ40zBsQPRm3J35COUew1G2l4usvYkTGjRDsLJQeLYlwKTY5hvMMljNZVIYYNC8s1LfqA9Rj53lpOCJToqynXLPMaES-qIHY9EV0cT6kGBjzYv5StVqCjlMYtZo7W5SZYcgggyPfZ-0HxyGjcT-nL2viFijn5yEooGItM15no" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36a825c4c0.mp4?token=ZE8A0WPFFB3gOYGRCO9XHLquT-aecx6XCC8j0A7AQ6Ks7KgaREUi8xbNboHRlB0EdRi7afuhycKNZ_oLp2Zgqg6Y4YlZiKYKz9m40aCF1lXnJuDsdpuw_UU9FrIJz2LGpW9uPiOtlNx0Qb_cPm_AWCQ9Y-OYrjX8lQezqDfgrQElIyL-IYmJk14dJNt0R3Msy8xvYzgMRZSqoxAIzQ5vbSD-RuQXYSjGMUkfX7ljzt5uVIBobonyk7RZy4c-h_0c9HHcKb43R3sGhZ9qBQFBKOaHh92S8jUWNF-U2zRM5jKdipK6QhtZEdxFfbJF0Av6bQcIwrTZm7q59XVxD65nqGzRdJ9WPvJ4kOW0Pbo5INEsBiBjGuKgg5HaIvSNUod1Nw7c99WrfzOJv-_q09qGWq-VbDdzQjdSfjpmh82-DwknPnhdJesMYt9yJ6nBNmqAoNtxtBPEWCpIOLeuToXNpIbrrQFsU_k5OACd1koHC0KjOaIdeaFhYxjvdO0QINBajGeQ40zBsQPRm3J35COUew1G2l4usvYkTGjRDsLJQeLYlwKTY5hvMMljNZVIYYNC8s1LfqA9Rj53lpOCJToqynXLPMaES-qIHY9EV0cT6kGBjzYv5StVqCjlMYtZo7W5SZYcgggyPfZ-0HxyGjcT-nL2viFijn5yEooGItM15no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله تند سعید اخباری، سرمربی چادرملو به پرسپولیس: سهمیه آسیایی حق تیم ما بود/ باید با تیمی بازی کنیم که از ما امتیاز کمتری داشت و سه هفته است در حال تمرین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95526" target="_blank">📅 23:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY42GrNb_Ga7XpqKWcNM5J08LTTNwYtKJXxdPeOnboAfC7j29nfuUn9AHiwZlfIhbrJvHid1Wg1U_Q4lmTBFg859qb5_czitEK8eGrMifG-TAI5Z44e61VuE5O-F9KTc0oRZDfvu1edQpyCn5FInWIyX46N1CKXWumSBMl5ysXfhvwJgvK5Ok_Dv82u-FeEKOzldme_ZOyfk-8bIOvpRovpY-tRxJIKM2O_LcRd3lyYQjgWHrLZY_EQW606ga1dMp-czy2f6e77BIKcZDjIaxjl7Mv-NxyuuMCKAMOQob9ODvTh7xxMS2_Tk7zr0Bqlj6-7tl3Dh7UjxhMCCeUHPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو: شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95525" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9qmn17irIABw8z7EdCXchBLpAZznmunEiTMCJ3xliJI0Ftqh-qrG7sgnmNpjSNTNvyfN0nR07qBfBKROCfKCa-VbiOUIK-7B-ezrH7pM8DS1NlIPhoMw5s4MddM_0MNqE3s8SXp_jWuhLzOtU6o7_Xl4yz3Qi2MfYtpWR6YwI5i-NVeHXIEpkvUWEeWNgBgv0xYSzQR1GfmHa_5V0t-jjYoHzU6lNgNPGb8UKrAq6ljo5HqK2XctOIP1-IcLjSBneK5NmABP38DjzSe5ee2RslzQ6qENTUsdIS6cIGs8X5Y8hCf2JKf2vY5cC5fzqY8M6FOawMK-30dM9-iB5gGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو:
شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95524" target="_blank">📅 22:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_-4uUqIHwmkXYPc4FyZwa-iHAAfVob5_vMBq5_3bGWiII_6Dn1kJyUrV6wPpSwTk5ZkxH__G7VUZnuT0g2xFJlTiwPvuhue9JpSE55lvdH5Ms3MjAh3CN_xRl_2qcuY5vG7V5UvYlofwsAq8f_mRgzWc5xN_T1uAFROcZBA2EGIbPxfWDyp_-x8SdocrjUNuJ_Y1KKakr4sULHTmoZ5Qpw0IMehF1RpxIKlrbyhICyo0yoir5JGXhItKzWAcr-jObPn-3A35hiuZX6XTWrtf96T3pVBrTR-fXA9OmVIdiaPp6ChwybWCXkMYWnd8V1UWZ8GJTI4OtQjSkLG5sEmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارغ از تمام کری‌ها؛ خوشحالیم که تو دوران شما زندگی میکنیم و پرایم‌تون رو دیدیم.
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95523" target="_blank">📅 22:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95522" target="_blank">📅 22:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95521" target="_blank">📅 22:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95520">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0aMMN5fG3QWTKqk6-GjUqne7lHlhyqHco7P0Pd8_BsDlVBGrVnB3x4yM1ysxRUefmYqs4RySwkkWaPI6g6f0TXJb3W3zizE5vvBPUmE4Ye3wvyK_2hAsbZKV1mqRyVEXkY4ouQ_p-KL8KSD714AWF4K_CjKAGPNtLmtgHhvZ4kT2OW0Wf5or4JMkx13ElRYT-MYcv0JGinC56PNweHkbzfqWpxelCmLt9RXJCkszKsWw1jdwHoVosb4nRXmUkzCNEacLCU9QOsNEiM3qxE7rnnZlWK_v8m5-SBH-m70Bc_cpPVqjygHbKe-9hwsAYwStg6sfFakxS3IaIdAiv505g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کریستیانو رونالدو پس از بازی:
"ما برگشته‌ایم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95520" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95519">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95519" target="_blank">📅 22:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKWHD1wCFOAdbTV5iYh_H0_0XW6OWqxA03z7W_88ASjx-4la0GT0DfyIfeF9rRrtrBjrWm9SR4UA7vnJj27B229nom_Lx0XcIxGZRLRK69Qx7oQJe6s25rPMGOv9BO1djQdPgauJfbILcHrpfqKuxEw1uRsfkHxzceV0zZy5Su-na7AVsazpPFyvIFSo0y9rzuG5A9MP77kfOwAIfoirmqpI-_Gxt1Dv2IdXqjRXRmMC6y1EromiHN8oIJReS93WAiZTHHDJU5Hu-Y9HotF4rPskvHzltSnrG77_uUc2JjpF3geLXjEzKaEFQPFUVCb-bvCqA_c2PXqm4_rNM-YUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/95518" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95517">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF97Re8lOVshg_5InXBOwk_gohqqFPZCHwHhR7cJAM4PpJPgXQvmKaeKRUH7MdVEM6DBZ283jle4zj7mBuoU01twLwtL9GOMPUcxh_TgXW61552IBonEtugh0YX-Af1KhI6XCucOwbvDadtND4mWX4HhQ9yE1wFkGwqT2AowqmQvEz-LpHgXD7Kj6PRp1s7fG70XKaLCSFSyKNo50IUrMwQokbeYjn3Q4JKLL1_Mdtk_P3mveNFB2EWKM6XdGwA-NrBRvz-P6zEHECSrJedICLsp5kIYaDXPAevBgTJ0oFrrNzb5qjGT_fysThIZsJBggW_x9S3cakw4hRRowktJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95517" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95516">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وااای کریس چیوووو نزد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95516" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇵🇹
گل پنجم پرتغال به ازبکستان توسط لیائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95515" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پنجمیییییی</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95514" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95513">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لیائوووووووووو</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95513" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گگگگگلللللل</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/95512" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95510">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEhV_zIsHHkqU9pizTKDU0oHOqFmmmNgR_zyyj9elY-AuD2LI9qZWXNpGgUnjNfGH6fsPmFd8o52RWI2WaeswcKADAEnIc8R75fKf4LT_DXHhxvavFsFbAHrWEjF4-ppm8BarrGJyNABzBqihtVRb-IJhTGengZ42V8K0spLCv8-Q6LUWK2ifZAVIdZwCVSsDMJ-q8wFEjVKQiEQHTfU6psV53o1VdUh3pvP7VfVc3ZucSz93357dOQ_Y4PajnndSpGMkGTweTf__X_1XRr22rFLdu4mLyKVSP6n43C5YVidJkt9ENYEKT0G1570GxaRPWg16YtqrkpChxP4XbclJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qH7zXuyiTZ-TwG033BioXGdUmc9u_ZZThAWmv-U1EfXMCADOmO8Z26NXCB8UccNuaZCgBCuM7daGNbED_RW1pRS3lu4Ni8p35TfLarMhg8l3Sub6Okzc-WmdJSBJra9uj4qcrbrrNGaJeD68tz-8uTzaL4e_vxW9ZiJ65ohFj7P4fosFxH0sCnxE-qD__ekMdUKb12CrZkUuLYKHrO32JNFU0kbSiywa-KtS_epkfCiJlCH_z-arUx9AlYN-SS-Vc_ghLCWjcf3XXAhpJZu8TMHjV7AWPBWHOyorJJGdrxcrTw9cpIZOIS6d8MWLEz-LTTEY2LcTa7l2QRht_G1_OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇬🇭
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و غنا مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/95510" target="_blank">📅 22:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95509">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نزدیک بود خییلییی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95509" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95508">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نزدیک بود رونالدو هتریک کنه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95508" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95505">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfaa_KGDeWMLD1F4SPvEXIbzev4yuHYvIuNYO1wSOd8eUCyklwZXNpPZWPd6JeWs5VfrDfCY_-CkuuxIGGz3pjL074L-i0geHIX5qxwAzRR9A2L9sJ-Y7EYJv3yIBgKwsZeRhUBtkCeWxhPIkdhJ2c6Sshy3Lds4m3J5YdVJxAWwbZPk1pGg1P2XBSFqIixy2uCED1d1snEMytPcwNCXbT8BbWTRx7IZrVEoPsk2_bU7syrwvocIfJAm45JLiLHcEuEpIVub7_ThoraCtYo8XAQwMpO1km9QJsTME-Bar9gaG59zhMXwjasE6BNYxsltbNRDbiiEDjy4hoNe63JkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSC7IkAIUVj66Ft4_QHDOLjbftd3fqDUKuQxD5GSxZ2kccVtzKn-Z8awCDC00HfTPJiTSh-x8g8YDJ_ubBcGQ3huWk13ymPz5BoKCC1Dg3I_HfJmJKtwMwLVKW5qWsHpIC8krVJZUO9XV6v32bTvYnEYQ39mPq3Kt-NCW5TWi2VEHFudQeYOVd-WwrWgsqUwxkRsW8WMYrIBMfza3B8LJxcVQxrRU7d766eHEhCmOJyUxhInGwoOjYv0x7iS8BqPdaH21P9ELHUVBGAZ8zGhp1RyXwASAxcDEL9BnCbr61aJ6GrInIehxmE-tEStROaWVGo3Jtgq3w6HzPW3qzxeQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوست دختر نوس تو استادیوم بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/95505" target="_blank">📅 22:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=VrKXb16-RiwtdZnSte9U0Zi7M7MO_zS7qpSS_09u7Zm7A9DIcgApGbS46Zkp790o3rQ3Z-4rvBaIG9KiSI1Idv22nahbznOOoe-3E7FNzExDlLmsB7iMA-qdePk22PyNzJMQCjg44Jxm3q9usyx4hhTrMT51PtGsMQMVEkr8ILmF4LGwYn66xS5JjbZzKsl6Z53916SVcXhjFmBBdOHR1ZYuozPZs58yLouEAPftKWLg0F_w_W2-p6HD8ZlDyAyxa17HMgtDJrXxBWhFO2w86xJwI4G4NnhxNmActDvDKWpZIzCpu_oZBN97tT6NlaY8ixWhTOZGrFZF6QpLsYAmXDq-1IbXS8GhFZmLRoN7R8RTVkpfsUdmsy5p2QGlkYDgHonDpLVNpXRfcys6MHOn4cx44SmKWr3bvTP3fcuhBazvByNl_Wvk_rAfimhbnEpUeVMiA7BlaUMBquVJOWkz1RX9y6OKbBP5E_BxmnDZ0I46IfPuSSktDzqzzRKxYJehwVx11hqsQ04l1vWrq_K7Oy7lmdn6-8zXi_xQ7GbO2QFNxMED66OYDNawFs_g9pZsliLkJmElSCD7Hg1_sEIkwLdFAfdj0ZrNvm-B2l4DjDsfT877QMP_DDogAMAb-3HB5JFdI_-wbp75K69ShDYxXmF4HTm24kUF6IRYtSpB1Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=VrKXb16-RiwtdZnSte9U0Zi7M7MO_zS7qpSS_09u7Zm7A9DIcgApGbS46Zkp790o3rQ3Z-4rvBaIG9KiSI1Idv22nahbznOOoe-3E7FNzExDlLmsB7iMA-qdePk22PyNzJMQCjg44Jxm3q9usyx4hhTrMT51PtGsMQMVEkr8ILmF4LGwYn66xS5JjbZzKsl6Z53916SVcXhjFmBBdOHR1ZYuozPZs58yLouEAPftKWLg0F_w_W2-p6HD8ZlDyAyxa17HMgtDJrXxBWhFO2w86xJwI4G4NnhxNmActDvDKWpZIzCpu_oZBN97tT6NlaY8ixWhTOZGrFZF6QpLsYAmXDq-1IbXS8GhFZmLRoN7R8RTVkpfsUdmsy5p2QGlkYDgHonDpLVNpXRfcys6MHOn4cx44SmKWr3bvTP3fcuhBazvByNl_Wvk_rAfimhbnEpUeVMiA7BlaUMBquVJOWkz1RX9y6OKbBP5E_BxmnDZ0I46IfPuSSktDzqzzRKxYJehwVx11hqsQ04l1vWrq_K7Oy7lmdn6-8zXi_xQ7GbO2QFNxMED66OYDNawFs_g9pZsliLkJmElSCD7Hg1_sEIkwLdFAfdj0ZrNvm-B2l4DjDsfT877QMP_DDogAMAb-3HB5JFdI_-wbp75K69ShDYxXmF4HTm24kUF6IRYtSpB1Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل چهارم پرتغال به ازبکستان (گل بخودی نعمتوف)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95504" target="_blank">📅 21:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گل بخودی نعمتوف ثبت شد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95503" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پرتغال چهارمی زد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95502" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95501" target="_blank">📅 21:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چه توپی رو گلر ازبک گرفت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95499" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95498">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO3DCqMq4ykbkWR8XaS1-5NWQAZl-8l_yWUnfE5motcHr5_SjOSwpt4l0WK5J5YsQEn7VIU6Cqwctk8gbr3DsUMCDGBt5EzeE2Zaseesvwu8grgaNSfu-ZjsUauFXWyu8BRkQykX7SxjbtDZnekqNMK-h6pKIo4ITW-NFcprNB0UfSPniQQyIPT6ZsgDmmXjtVMU-_X0O0JW8yD22yyHFYY0yktntU5WYPenidYKP1Iw1FBwx65LwVcxmE6YeWL54O6N9sRg2vQSYaiYTbeAnmWNJvhnOEu9djEBKlR-nInceqZc3ZpdgEPitNagnC25lm7hAuonsshLYFer8J7L3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش ریو فردیناند به دبل کریس رونالدو: ببندید دهنتونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95498" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95497" target="_blank">📅 21:39 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
