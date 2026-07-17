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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXZVcM6POZolmrDd9b7HeQx3TZnG_s6iZfOjvDpyUdtIkMbje4hhnMRUy_VYCtq3ijWKAZlXX64pqXtom62X7wIfrliJONLPjz8tC-c5iMv9uqzHS-Drcm9m4-qUMAVKXys_UvAfPBfSk9DhAuQssT3Y0A3QSzV8jbjZqdOly_JELig1PEU47Q7_sfEb13vPUMEurxWqqUBEQgo1ced4BqIKPBOQ75Ro-4dm8vAudRQgFZGvjQIHt-bTAKd3v0hkdd-3jB0l6PRd3q9w-tnIDMs-RuLbTaJkfPnKzofwlTuCCL19XJ7jsLKYWbufafo3ErcZwRuJ0B8cmLEPSRgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eke00M23YA83nOZLmZT_azxkg5sl1IlOf1GGszyzysK_EHrIjhrBuajxt1e5jaSrb6Si4hctkMr7fB9iQNQFlGqNCzYCzexXivWxh7kDE_Z9iA3I9IwxCNDPQLCrP7mCpRnLBo6nLhxTDY1XXZ6tjSERauYf4ng95rL6mTQj8_GFN9o4PH7qnWbV_OE-GQ7TVUWmI-GdrjHfi_b7uSexMEfkm3Q5Ak-mguYqCgtBV1eB5G9Qb50FRyOFUcVMIQZFzRUGkYS0u3Dcm5SPChZHRl-dq8AA1AGdMuCZwmlbLcY23xAx7sHCXWIGkaJbNX6HIv01mjkca8gPV1j6vyvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBdYO6xkIu0S9-9hoGCl1iSbuk-8ELDB1f3eXTmk0b7HbsUzvjaYh7VMbnJnvo5JDI_PVnwPg7BAgf-rSjJ_oai_dl5TezvVomr--Nw3pBH9EOoAM82af4zykWLRu7cTcIrrZ9mXo9rdaUCtT_QObg-V4Yxn-F1RJbtedjHoe83RRY4_T2UqHdRwKihY8se2HsEEnjQI0y3X6MnatkPd7zu_YknYVMNI89d0iDDCjXxnvg44-79KVUEF-98HhamoSZiLXiJWUdAvYHeyBGFZen92oNep-faYfWwkeYKN7HRsaUixScXCwYKFj4gPxNkhuDcw2LKLcLMlCLTwxegmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=ZlAbhPWYBm-J1Zmw2oYpq6egbdGJxdR9cCEPZCNN3Qe_oZtiuHFBlZn2KgGLqsi8gf4Qros18gSP120krKMZ6q-weqfXvzL23k_0X4dpWZT6-lgfgOzr3C3odqqG9gdDFSPMAY9JJ95DP25_yAQA-JmkGMFjJPpvuX1lg0IwiNVepyyv4r9IKn5n12cGsBSXbntYPL8fvcuppoTmyzu0hHtCA_qYxJPwAedPi9UE4Q6kaHA8kDCdd-eroPNKVDXDu2hKT2xl5R6FMb1Rurxmo-auxxrjigpAOox_jHtz8bmi9UyNMghAk4oRSn7UrJDjISfyQP1f_z5OIoVUk8CFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6-bfOVJBBPcfzCFSXCuPO1Dz0lm6QQX-5_tQtYX_m5JRy5zTEb7cEmCXqPkZJNR-Z7asS0nUskqx8usN8VqF-W5e_AS3m70MAl7UqZO8CB97OZnTbnnRIyPpeUsUxp8Obm18Ts8n1haii3zsN3RepuQKcQpjY1mJYRMWq96UhmNGrNk1r0DWqPyZWf7Gu-GcdOsYnLB-5bDYTf8kaclqLrxx6dwQxtM3zcGfCgDvkBdmM8bRQdukcDqMeq0L9ScGWS052I73M9uRzMn3YgD3SoP1kWtqEEt9-7tfcQX32rtWbyuR6MHCkdrOYlZHk0pOfWSAlJjh_-wlO6ZRiL7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4GR775Lf9IvKuBnYXUVrd0kmwe1Wg3P9SH6QgH0ftxiWxBwgivzygaRanQ4kXnDdQgOpbzbpGO1T9KjEhBEmphn1KFSW24jRrelpcsFMRtyrDDw1IeR8e7yYFO71CnHw5Nd_hfjn-wnVvQOq_odFTRrLDgwHB64UpSKzEIkjSxzQ6aqwFSswKyj-t4dkWIQfldfedmUOuyxJuuOAowxqnih-zG88hzIdnq18IZc6alFl837bghChZ-VWinvZO9Sld827yZmjd7PSqyPo_faTsgpIKyMFHaSLvCzisYvcGSRiGQcGIhwdlLwFyrFG-xamFACa6BzIDsXqNgeuEZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=iUKciMgzHsiocmcDNUu7gxg_BhBhHaXwihbYRWsHlZrrkC8363Eac6CA-Xoo-LttLSjWnGAMAeYbnYXS3YjWSsloMsZyLqanE92a6zEsv1z8S2GNDp8aC5iqt5Tm3USy-0HeUgw9VOdR7dsPUV_9XDxqeflN3a1SPDzxAXcUiqsrtzUsBAc8OaEFIeIPBFP19UAVc-kHFKIRXilVAFGit9VtlkemagBxJ2veJyIpjEL-1WWe9-jA13jXdZdDy7_LqxnjkEPaQ-br-7o22kdTSUAR63bFca3Ht3if6eKOguUMLHFJOZ4X4ntxbqfLwK9-irlFkWSNuOZbHof_sNmqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alGRWVYmul9sl1JYPSbTelcIFebyte3XqVP1yRg1LiYzahXATGMfunxtXQkorDLPVcR0Cg-KAmFZLSle8MSLV0JP9ee41qLzIevhlxxPzL-8ngvgzhXdmyE4OTA9GNYGgofb0syarORTp8hj3dQDhqHmhXk707f0OcfeEcbBy98Bs01IW56WosPUMbD2dYJitWcDNf93dIRVU8f46wGLXhGKqCTMXF5ptirf7ZhnmkyM-6OwWdWdELN8Rqo9Xki98IEnyHOEI3o4pz0p_pJVsonPsnLDw-HNLcX4_L3dga5KURnCMO1H80C1G5bzzhtapwSHS3DWJSqLEWKavlCQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYOQoqh91OzBBEa5WEYFpWDA1JnklQai7fwysym28koUT9KzOXQIHcKZqoN_DGepMleNKW09Zv0_n2VqMph9cZFad7lOhOgXmsVyVrirAj_3gIW6WOi-j4x_lwS2sewDNGs641wC723JHmdERMWvc228h4X861tHypRtNGDQG9xWi10LIY0UMREfG5sN-CbtFQE2GJTECrGkdKzGD9GGc0pUTT4m3ar9j_119NRXCKz6PnHmbS4iuhpMLSqqLcYRnOQhBEEGllIzJKpnfVmXDXJhfBG-N2CpYUPv3scqg_hW_aU7h_YLqXwTILO7R7med_pMP0oOKYasfXnOgWGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBpnh50pdv0AA-2BCq_JG8__Mw-y_nulShVksAf6QV3bm8yIkXyJw_GwCrqDr5pgcvdSlctGctM90WDBZexo6o15aWYFPrTgf6YXTC-CFOJ2kf9-IETONoWJMEvBGhSJReGJOjKdVwShTOg_CSAkA9Ld7RIDRspPyNsgCQ1fnsTP31oFfO10jRnUqBkAcN1A5ApGEPzlqg6jutQTl82zb3SOXNvb8yH4drX17QUTTmNahz5NVMVPG18OPxHFEQPuNEa9zXULOedUJgQ9NY3M_6nuTLrKu-wY6Di0_LRfYiEbAKzF9Kt652T8wN9XONhy0FBBbk0QvWvbvhRYv94i9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVUG73lh0NCDK-Jp9gpKbfUyvxYIe-8q-ds7Dro5IVLp0JbzLwu-QNGFj72WQxz6wvAdYMSoBm6Le0ZJrGrUXEbboefe4uV8AcMvDZKr3XZ4vYqG2Nz8Dixlbv-xvue6_saHhN3717g-XqUqvbVKn4KJ2JnAvUitVvYOPzrQqGySQeZKORJizLxObDBT1LZOAH5CCYppmRp6mBJ5tjP6UNJ1OMk8e1NlT3IylXwTmnbU-Lq0voxvhGRRVhfJSyrcGLEbKAp9knEZ5_yXUQcqTJgARjyFwo8IrWYLJPZFZ2YSk4Bkjn3zxl5hWdr8GlsWc1fCPfl__TAB6__d_intaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huiAZ_Nki3KeEY0ZZaxFuIe5z8BZl_WQaKSc81qrohmbvmjAkcV3Swxh84glBLLPEqyOwJXG9T4dytka33c9eaRFWyer66lYxuKTDqnj4lL5krrmXhxAGuKzKg-lOmAJPZbcvNZGZzeG54tqhTTSFR-zkzJiJEnk9_YpF5u4tYTo3I3y88wM36jtkE3WvZjNTq2tvkAUs0zQaOzbbEfc4N7elX3lRCZ6t43JB5cQZA-vnMgUR9-N_j5o86CUHBHGxBvsiV3hI2TthGtcdi5rH1OqUPh0YxYFQwqjAPQG7pp4BsMINGzNseNlRfEKQS8xzDAZ5EneT5TJSSVcfhN3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6wuXWgcOg7Wd_fgB_lWzO1i9GZs_pRfAgLD1Nf5oObsLcvKpghRNiDzbohbz1kKhRxSe-x3936fOo_o66F38vLAvoL6gRTYi7XBbZvqMX3Wo2bouGKiZxZaiVuvgHSLfqAdKFtyw91EuQsrWH-PeZYrZod09IQJw-kiRBP3Uc9QwsAv2zw-ECnx16TXhMD2u6RF83UvF1o2u_FlS_jZ7rrUb6cJzBd3FXihB67DPEm8ZUUZLCA3izCMJLnneUsdAaVk4B1Dd8ji3rnfd2H2py2aYs959lgsOzO9xWWyhBY-IMCvD-5VICDGXzd_jyWOn4pgcMI82m0jH43HOWtHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5_KiiqH3LDUvuB6H2rcrakvbMMXzOp8vUbvteXh13K-tsoCTgEsHdgHKs5hYJwz5GW3LYxk3737Lmhm64fHM1ZrwCCyrV0AWByeZcrPcLXhyhBtd3siuX2zFJQj4OkmYMLPYjYtXSBpM9f6jutf9mNEvbswccf5E5Rb9m1WhB6bewTUt4dzZG8rrjMORHLZCbKUFSK1A0-LbU6keWR90NX9m3v1ts4lqQ-zcQH4yEfi-IoVHmMfnFv9m0Y_OjfmSdc8JpRDGR6V7HhYxGoA_ziF42yrn4hfyzW1ecYv3ipb8bSznnMbU7qkUuXrMbrUlb8JRdMTsMxbIjhb2RV1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYxwz40VJAKZW-Vru1CjCsxNgwkJHxRycpCtyagqzewhbrIICMLSc77XauC5x2leRrxyZcMmXWRTI6HL7EDb7iTGGKae1-BhZn_JvSYKBA1F_mfj2OZAQkIeeoLNResqTWv4vI5o-wDmMmFgLLVoN-3wpkL8r7iHw61Nzk4_scXkFLPuxP1H0u3Ie269IbhQpeRmV33BAsyOrAVaynSiTabzjy06-WpQnRIo2dXo9zEffeFeg12zKeQAHTltaxz6YH_2uR_jUimbkGqzTaHNfzcGctOi9MFE2WDzQEXUNHdnyOI7-hGysR5O5LhNJNj6yjNBlYkc_cRop3BDZIWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biS5Ywz7qhof6LqoCA3uBVcbZLLNEgnra7vF9UBGG_WVZ98a_FAnLz9PvjRAFpuz97j_UXk-qPja4a4Wxa33BWtFibvvwu42vbpHngN-sg5Jop_T3h-fN7YizaXMqFgwFO5adugI6ttW-AnTtnYg0etOQ0L_wEW3Da0KN1QKgOlOJUfCc5zBviAlxHhIiSC4FKy8VXf_FQSYXX5fg7m1xsUz6kf5YXXDemdmU5_nKrsUXJ0lEZzy_Ayuz0ylqNv69lhnaowKmXQHd6-bsDVmPHKm88g9QJtc8j_gsitdQ-c42BcqkFYdrs_H3i4p11KYxmxMS3vl5fWligHMBtxs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrmhroM3OltksV-N2HXG5Fyu4eEuExEL8qeQ0yEAMbJe0JApxN0yR7A3xizeGZINe5Mt5WhYz8sh_vAhIFaL15pOEPpABsYcUU5jHtYIfRglsO9XYIQAksJSVPLQNdoVixQwxpvQGJVNQsQEs-4khNj4KaKL5rCnbqPLZVbz--qno9n5Z8WQfqEcB1JW8Q6oyPPjmxVCETeIqVdIYEGgHier-8aNeTQqPCo3kNTFZXBNkPzL-U6LRzVi9hNpdaIHGk_VU7DS4buKEeB5t_oZ5sna7hUSlYVkUqxREYtTUvdTLnq9UaQbOutMXDPgxq5hxeF8rQtda0oLRa30oxSkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-asvDoFw8RCEyjgFhXkjFi5aFE-ExDlhUy9Dklcel14FTVCEwd0S89t_kqhRwcAZJDjnhpXIxx1QIYG-BWl2dtjiGywFbPjffnSk1VQkwdqlNxtsM6MB66u7LH-S7r0MqB40TD7rI2iqZcO25cUQOQtBosYH9934as90JZo-JzFVNL5rCKRQhTuil5Jg0yEplEfwNgo_n-dpxybawvL2xxE0J1gFpB3qhzI6DuF_cVFmGDEEb9SiRfkL_8eET0Vnd1wGXKNbugX2wWXxJXD88-nVV1mYuPUSL-9LjR05OJjCMFPDMvja4NhiksBKOyk9U67bYDZmOmcODIaynr7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSfPM6yUx9x37hkNJckB3gvbihuzY2hX0SfmNgLePtCBzDVs30BjwiwtqPgr7uTeo3QydQ_jBfZbHvdicnBeG53EQChFgScu-VjZvdi2XsZVLpK7fV0Jy8hFbNNJuj9EHvNHnbF9QTn74Ol3V0LtqZ4EiGPO9N77oAaAhnTrjerVM_cOLzYQNcnBqthq5x9ADtNDqvDk46nHR8Pz7Ghcy2zJTOib_Qqp8GyFyQi12ZApxJw8ba9-Sgk9Xs2IwUXkjdwhSo7Glk1UIVRXxOtld0UUxcAaeX3PX-qo-NrEfHZqlvgQnclQegwtigWIy1AktGL06fu5Qk2DOQkzOD7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unr3z-bRva4d-mGyAS2zneFhedZ3ovXfsxFD2hU_aSlf_suonjPpVKjIVzB1AsylicMsQ7QxEf0-njUl_Ii4Umw3hko7dzzRGV8v6hvwLLJ3bFB4f8lPNeemLQVm8twIoodGU0ntdfhOAtcNOwGGjpXcemhGFLbbBeTD8swdqD_jZiGu8MfjE5J6zTS21JWT2PeRj6_9T5tqZGHPJarhHRRnMJ0fmMvZO5lP5STq9mod2-tzOxp_u4Ryje7VFSh6Q6kFLfv1cysKdUvsXOXkDRYwVE-6kMYzIPbpjm-ZOOCk04hC5_fusGZ0FkQPkBA6VCm9ra8dWH-zV7qibKiMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=H6h35Tsrnkd1kfTHGEBjYyssC_mt3Y0-MnrvTCnEPF4m_V2H3VNbWdpbxAqTtlR0izJ9CTXT3eB65gzjqdna_C8HC_1SwqcBRrggWBZq50ivfvmHabnzsnjDL569qGBVE6AR1Rk0XVK5MtV1bCiiYnGwoFb481dYRBH6Pp7fbX-QirptEA62Vvh-H2OJ_o_LwH73NvBtGBl5Ac-nRARpLv4FUpa-M_aaNNnefucM7Kz7pbd0FU6mLxmUo9ipq5v2glI5z0BDwAdKzOSr_4z49-VRi4NxH1dITRtRmv-NKuloQdVyNsnTMS-oXRB3DjdNOWloo8rMtV8KQsAKuVGhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRwktfwSrdyAjQKbe52zd-JoCOfLvEDh4XgTZc8FYt7_pXkNsA7RaraxkiWoZHedkWMdtnbZLpP1RsVJKC9cWylyqzKp8oCpui56Ac-PQZrd-gsqiDQJQ4basDN3YI6ZGFPiRgJ3s4HKjAZXpu5JdpBm6I8oU0vVQOQQXh5xcF57iCN90qN9D3dKxQCaYdSLWeFb-9S3f0KaTpiX-PH9i4cfu9VJr99xROewrSczA7WZn3SeViqShvYXqpxn5ugYY9vaWwTThPhLcBz-zpCQJCejtuQWypQFF9sXvwW9p2Zm2lG2KbCDb7Ew06InUxleS6FjFzYj6mtHkmrENTYWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=ILS9XgTF5nimT49i7Dn7z_8DAgRS_HzpzhhAW4FU6qhCKULRFfAclk7-FYfe2RLt64YPnugZdxUvPpgD3kqdhEYaqyw78cLg_-YUCHvtW87FwJz5aVKHLdGxhx-3LsZXB7EBHpSFhQeL3EvC-bZCrRKago1__mOLDYEf4yLoMnqytwSoyi9NnR8gps3EEIAL9pdtx9_SG_vSS4QcQiEHDTnWBlfCqJNiiKf2bysiJALLjPqGLuYyjvygr_caqclXk2g6lzCg0SqmaNGhEU4aUA6a0oWtYlaY8X3OXuHqQCWcFxHD-05mM0T8kZAy5kc7O0PDroHERuHzC8rb0YlbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuB7Lo870jOcZb50bu1Vo58KumfxWoSD-Yh7kjXx9wQIf6Ga2QV837EKTcL_AnXTUF0idw8CEdc8KUrjtvamdlWhcEPRoZRnGUQo42BKb9tvDStEI2iCBat0tIIoXqg-tu-ORDW4jOdXZOBNUE440HlaVJNocESV4MynO8hTyEimPx4BFgt4bqf4zgLO9LsZgnfhboAA4_0d53fKamZc59NWumCT_HD0hMuXXp0-bPmSS2jTPW9EKOXbd-zrzGIOKBdt7wylimFiuMWyYr0t75VNdTa2V2GjRMBcL5UhwMDrxL-xc4Js5DdCXFRlZULO1ERVLmc2wpriASb8c3_whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epQydzNd9EDjoDb2RPdC8iHTJ7qhWlUAFyf1n7YK6-1GJYmZiQ4KD2SmSfWjPzS86Ky28bf2TXGOke4Yj7Y4TQybUBiZiYg-66VSy46lwe8r5NeehC1aJACiW5Ma66Qyrnq_Nn_WwjJjmVPwwNAuDWsP8i9QSngNcvHDcr2K5fNo4vzxVk2ZAZoEkjKO4pizW1BGk1wifzYVUrK4jBpFlDmpRhOOzJfliRMxkhw3XbjOBFYHGnaldL3pTi21HfpJHkGbKCuShSuh6IsUH2Sea3VGPGV1GRGtrBA-MftOiP5vPNHUBYr5ioMx32cx96IAjcu2_wIC9Y3uM64qDKkUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polHdQ935e_pGQv67DLjP14UAZLTUGvokZKJcjn_fNLIziDmoAZg1sDPxKSIxfO2Mc8tSCWIFPDl7PJJTHa_5izIpNd7II_-iR5lqRLiwL7rD8lvnlhF3cAIbkQAHIn84c3iu36qsqZTKbKhgGOKPbHCqzBePngrsg5gxfqmYvaBELDWPV7uauJfmZCUHkDJhITPQP00fIByJrf1x9jk2N-qspE_HSG7SPd5mhBAZC0dOVB-ZDyKZ3uXNElgjT6xNjBxUnvdy1yl4BALOPiTielEn4qyhjAuV9ezpIeGVvHP1gNf6clOGCHTOkUko_qeCO5f755ok5LId3DoJiZdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRKBwOwshsqZDrk9u_mPjIXEc2bzj01wDwWBFCUM7a2T5GCT-btt3H61TXC1LhGi0YEE2qo8sRyupio4NN1MOVM6O5LXv566f06t-FkMgiFbAexMalibwIrA3DjoGRizbtRScxN6jC50ACJk6hVlo4JRK1ESTd53tCRJD_yGnQYSf16UQz_YOwT4vRifVm_FNkuG4BOHfYt5s3SYr8YqSUJMcjkdMNlD2qAx0PLNOMUbund2cTO3-CXSUJNv07a753-gnBRjPASz6BWvFEWmqDgigplH-FnM-LnYp2OmsdKcDAd-O3peoH6f7e7XbflC6LIaMs9LEoP8K9IQuUw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl0_I2nLlDENC4-Er6BiHP59BU-46gByp78P3hUDa2gDk6qo2_O-_i2hxaLPLGgfQWjaoTOYIjrsfAEtqavy8LnkJLe8J68VqP693Sf7Nd_GBZ80G96fbGyFprlGrQG13CIjbWz9KuQftyempBHZ_Q_720XTkm0reaeUv78AdMXwexhl2CVxeWU2Qk_ODl4rf0JBobOkCsFjEtp1PhgNKNEsa3qecKw_BaEOKKRL0FFTwu8Nd8xX6u4fRmr57ekxFhS_rNt3ib8PFznP44dy0A8yw7Cb1dMvhZzn_I7zL6rU_v2snwfmBMdxeQ3kfo7X-sp03s8PYZdBRW7nfMZQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=UGzhoGjAQU324oenVao2vlKw0MeZDYW0Bp-nt64QrGrV3z70G9zpomKrRPAhaFGep-UvDLLB8gtFFMTP4zta5EqCNfo-ZBUgGiTZFFgo_qM0vZjEl6uiEIy488zETPkp6_1-a2hrgC6Ixi2PmMyxUmHD3zDMiVF_p55rvExyTKpQwUuTCKlnbIzy5i3iZ4XD2cPOdogy3mbd8cDq-rBvVT_7Bf31kGvwbfRsxIYW4kuKUB6V3XxRHcipNCqIiaMeh7NuL3unJjCdp4jaWYBDYPjMEXg6pY8tBDQNrBSy_A-GRTtjG_aA6ReYdts7dSnPN8Zoj5Hft0Pgfiw63XQ5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=UGzhoGjAQU324oenVao2vlKw0MeZDYW0Bp-nt64QrGrV3z70G9zpomKrRPAhaFGep-UvDLLB8gtFFMTP4zta5EqCNfo-ZBUgGiTZFFgo_qM0vZjEl6uiEIy488zETPkp6_1-a2hrgC6Ixi2PmMyxUmHD3zDMiVF_p55rvExyTKpQwUuTCKlnbIzy5i3iZ4XD2cPOdogy3mbd8cDq-rBvVT_7Bf31kGvwbfRsxIYW4kuKUB6V3XxRHcipNCqIiaMeh7NuL3unJjCdp4jaWYBDYPjMEXg6pY8tBDQNrBSy_A-GRTtjG_aA6ReYdts7dSnPN8Zoj5Hft0Pgfiw63XQ5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa5DYdycVwUX0m4MNBTGwU-pF4pT0cSl6HEDy0vGFbkJ0q9EHyHjdVk2Jr4w5lXD921ht4KNXUdhSpgQlUW2Wp_VA-QDH2MqECvQj3AiAytpti7t1njx4T7VKD6DFLj1mQYWRsrRN_TTF04vVNbUCzbf17OU1BXn6E92hWZAC-u3nYkeWkF4RYFW9WKUzu8h5Vrwt7A6bftlKEWV2KH0PxJqJMXKXtf8uDNeGvY-CQhNnpyGt8GPrDg7u0YWgYIm-H9Fh1bfWV3DxDANX0_04aMSOavXUElQfRMCcNEbQJlNhbrwcjcNcHMD8YGem83JNg9yj_q2tNOP82Mn8HkujKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=YdrMBDm6GRGG6QtA5GxPKcwdPdK7vSxwEExcj-HD6u8IBiyYdaeg3K_Wn-Q9dJBsXUvuni8clZu7UYGjVGCo1eAF4G-cLE2K769ppTK9waNneZ-w4Nh7qV20rzXIyhtd0YxQpzCxEqaBtouIfQxVWmxW7ISH29FZyalTXtikLLkjopdqzBEg8anrTrvM1b6LlDSlhtuDYCEFZ9l9m8mKoS41BY4-elx1Sslgv4nNJMkAvB0NgrsPtVNLwpGG7hIDmVgV_gq_gJKj3_kQvPe2LK24FJGSC6lQznenT0eZNPydt9TKYxVjPeAusFjCuoi6wk8USPZmjg1MnzvHyjd7wa5DYdycVwUX0m4MNBTGwU-pF4pT0cSl6HEDy0vGFbkJ0q9EHyHjdVk2Jr4w5lXD921ht4KNXUdhSpgQlUW2Wp_VA-QDH2MqECvQj3AiAytpti7t1njx4T7VKD6DFLj1mQYWRsrRN_TTF04vVNbUCzbf17OU1BXn6E92hWZAC-u3nYkeWkF4RYFW9WKUzu8h5Vrwt7A6bftlKEWV2KH0PxJqJMXKXtf8uDNeGvY-CQhNnpyGt8GPrDg7u0YWgYIm-H9Fh1bfWV3DxDANX0_04aMSOavXUElQfRMCcNEbQJlNhbrwcjcNcHMD8YGem83JNg9yj_q2tNOP82Mn8HkujKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25912">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCp94K0eE7jqyvzmBWth2ucpr1nifrXB-IHPJuVubt9UZeyRRv8Cz1MyfweXS01ImeC42hRTH6tbX0injd5mshtyev4CoO0MZ0uF4hMhZZ1kifvaI0rZw_b48_dnIp2-BrgWxhW8Zr8Vtefrss5Y-GfIVKKbI564r0LjzZ-t2YrzdCOmVqg-7lgzFR9alx8dsF31s6YnM2eajG_Ced9tvNof1ryWKmkeeqRmYqZB6KlPl46zWwdwGRChqC9eHzrdMDeJEDTwPbMqx998JrMjYxCebGusdAO4WROUeA7vBbYcfsOKg_A9Dwq5LIL3qvduLJpq-KXIwtk1MC1qDGc40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr26
📩
@winro_io</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25912" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTfJ7vqKKMa0ipo2QzakqTGCujzwCqSvnQ2LVNhbOM3EKjkmWRBm_iQEesFskkQa1EEtQyAUix6mB-MgQuXrhGO3JlWnKSaMENaGxBJ9iOO9Ovatj-r0w5HapbPuWcKQe6SxkG2W2lrOfsDDu-ZjnWE3mk67esDIm2DLyaXyaZBf_Y78rCsdz3ZtOyLpAggGnvfVYEx0cG117B1AnIZvanGJuCXtZwaulWNgE4uCRKGNz8NXZKfVov5b4hr26CMNLaYqLjoDdSrH4mweqwdJuohyM0NO7dpkovLmGkVG2DGnm1yT9IrYWXJvZqS3iEs3NFrVoK1pVNuzi84fwjuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=JTwg_0u5WC4ScHn72NkGNCxezKuh3XMcko9-kUlgrb_7crUEDhhSkeBeoOWfN_eqRFkQT2jkfSy6cWAUEHEYGs4vq8qg5DbmjLjZp6W5ATdJDOEKDj1upEWMO-pyR0BsjJCtpo0SrigNN0YozbOG1a0VkqBKFgl7g6Ec4kJHhVDhR7OjlWj-Cv5kXqDFO70uo4Meaz4cZhyshNUv8ynSp2kZfqd9eBzFDPS2FKvYSkx2r0Z4dTYty46PoEK2R_VIroODzuAmyfbztN1QlJzgjHSWO7AzpoWyvCW9bZyu_flAfj3YtC5ek6b6QkXUcAYRsR9N7vBXDs9caztD6w2qxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=JTwg_0u5WC4ScHn72NkGNCxezKuh3XMcko9-kUlgrb_7crUEDhhSkeBeoOWfN_eqRFkQT2jkfSy6cWAUEHEYGs4vq8qg5DbmjLjZp6W5ATdJDOEKDj1upEWMO-pyR0BsjJCtpo0SrigNN0YozbOG1a0VkqBKFgl7g6Ec4kJHhVDhR7OjlWj-Cv5kXqDFO70uo4Meaz4cZhyshNUv8ynSp2kZfqd9eBzFDPS2FKvYSkx2r0Z4dTYty46PoEK2R_VIroODzuAmyfbztN1QlJzgjHSWO7AzpoWyvCW9bZyu_flAfj3YtC5ek6b6QkXUcAYRsR9N7vBXDs9caztD6w2qxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=IeuICwsi0YC4Z0roIzOWLS4-6ritP1yzSZP4ToYxmq8oJvd0LiDHGtIS82M0VcLOcgGMcwFuLfqVM79am2u_rt88C_hvLbxc8DO_Qy2Q0GDnoHl_ZyG0RmYdn7tLoNiZSZLNup01wneH5XrHHjiyUfrBrR0ZwJtkNQzUYgJMRaAjIefl7g_P3PgTZwVZoSEJqthebeb23LanXHsRWD7LQaxgQY0GXZ_9aCAAfrio_Js5FVddaRUMsJTvjYt57gvnuGejmGfJ0MW69sq3dADCcUV6De_bEtTgQgawKvFJksO7xzAwC6GctExI8eF50Tfe_5ViLvZhNWPJM72k3puhe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=IeuICwsi0YC4Z0roIzOWLS4-6ritP1yzSZP4ToYxmq8oJvd0LiDHGtIS82M0VcLOcgGMcwFuLfqVM79am2u_rt88C_hvLbxc8DO_Qy2Q0GDnoHl_ZyG0RmYdn7tLoNiZSZLNup01wneH5XrHHjiyUfrBrR0ZwJtkNQzUYgJMRaAjIefl7g_P3PgTZwVZoSEJqthebeb23LanXHsRWD7LQaxgQY0GXZ_9aCAAfrio_Js5FVddaRUMsJTvjYt57gvnuGejmGfJ0MW69sq3dADCcUV6De_bEtTgQgawKvFJksO7xzAwC6GctExI8eF50Tfe_5ViLvZhNWPJM72k3puhe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=ZDliMbGV7BVKwIt2hsPwAPqdK9AYMo0JU4F0Au4bBf_K_UfncwASmwNvo00_XjNdeOcLOe72sKQq2v2EpXZ81YY9Wpk9d-cSpTzS8bGA8bIWiavBNDfBi9xtZF9aS41ZCTY8nCj-Zc3Evlz5-c4jysA4Id4pMqB2lLQOsWHMqYfMCIK1Y_zakYz7bYUjDzgpRgIIB88AqmHwmP_76x7iZINHo2h-vjz5UglDr9MhrgfLZaq4vvPPF9_kJfnPtRFcxr80gf8DCVN-kFNqdampjO18gt8CW9vonJ35uqKRGPibsGPGJbV1zhFpg4epdZphhSHgQq6u-W2uFj913T5_E0QWdAj9nqp7sTm6yTkScqzSPeuvwhtU0-9ILPx8NVOyQxVQu9reM5d--GuGqDpxNXE35-aUcxprJwrwmdIDENFR3PALqfbrAaox0QP5YKKZRaEVRCw7iCYki6Eq-SLFhnFNBWRsOXIhktlXnqqL2Jvjd7vfC2KVeLiNaH9nNSMKBWAniVGr84giu7hn0xRWc_w9M-dduzdl0uxEZFNEz8ZmWLM_wlGK_TqeznHT2XaeEa4Ow7yDmHzxRglmM3ZmY96DuMba8xWlPJJ0Hu86nxoehlRyBd4UYTlWclYIHdWGYpLecNjjgUyLOuC1FoMkmh7V30zwAtOyGoo1CpISopM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=ZDliMbGV7BVKwIt2hsPwAPqdK9AYMo0JU4F0Au4bBf_K_UfncwASmwNvo00_XjNdeOcLOe72sKQq2v2EpXZ81YY9Wpk9d-cSpTzS8bGA8bIWiavBNDfBi9xtZF9aS41ZCTY8nCj-Zc3Evlz5-c4jysA4Id4pMqB2lLQOsWHMqYfMCIK1Y_zakYz7bYUjDzgpRgIIB88AqmHwmP_76x7iZINHo2h-vjz5UglDr9MhrgfLZaq4vvPPF9_kJfnPtRFcxr80gf8DCVN-kFNqdampjO18gt8CW9vonJ35uqKRGPibsGPGJbV1zhFpg4epdZphhSHgQq6u-W2uFj913T5_E0QWdAj9nqp7sTm6yTkScqzSPeuvwhtU0-9ILPx8NVOyQxVQu9reM5d--GuGqDpxNXE35-aUcxprJwrwmdIDENFR3PALqfbrAaox0QP5YKKZRaEVRCw7iCYki6Eq-SLFhnFNBWRsOXIhktlXnqqL2Jvjd7vfC2KVeLiNaH9nNSMKBWAniVGr84giu7hn0xRWc_w9M-dduzdl0uxEZFNEz8ZmWLM_wlGK_TqeznHT2XaeEa4Ow7yDmHzxRglmM3ZmY96DuMba8xWlPJJ0Hu86nxoehlRyBd4UYTlWclYIHdWGYpLecNjjgUyLOuC1FoMkmh7V30zwAtOyGoo1CpISopM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhHJ2v41aATgC2VfTZbi78TSNiADbhsd6BrGx8iKBt18WW4JnJ4AzFcs0HgBGGRe0mqzFyIRtbKnEupPMqIkdqSmUkOhm4MUaDnrdGiNznuBq-VZxkfpEScuvBCW8K3AS__ohSaVmxCTcbmKMu-OHcHZqpnU_OW0a1akW0w_7KEXKbJVLQuetz-_Uhn4hzkGGrD5gBaKdR0-kDGh-l3cEHsM1B8uETNxV-e5pPfm7kH1qcc5CXmn5jHICbDpoiuLnTgvWFx3e8vxz27kcJY6nt5JNOPQ2XGwDc-d4tIX1Jr5y3Xocw7P9O3lh58owl6lYkvgacFH37LGTbCujZZS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=pCxPBfO4H5K7PjyX_9G7Kzdct80795H6QuD5OAx75MIq-c7kSbRWaoQBRAfqazDnqGK4KXIbVtP04Md4ZRJoW-OACr3pNlc4nUCl_m0lMcdaWPvyVZYfPZsAejbz0thZ92_j_zNYM0rTV4BZ0IhPmF0iHPD2cgp-5Lqd9o5E6GVAMZGfIrlMZXXKo95lrU9XuNE2SAruf4A6vRCfvYHg5ImPUqobo9xEzzjbm-0AK8hfgHiFpJT0J1qe-JMJnHezSnxheJbq4FGLM2BMCdKlWX9r_PmE1uDMMjpVupuVyUQilZezgeEJ0oBmYvPGwTGlwrWl7Oz4TAxN7AIP3LGi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=pCxPBfO4H5K7PjyX_9G7Kzdct80795H6QuD5OAx75MIq-c7kSbRWaoQBRAfqazDnqGK4KXIbVtP04Md4ZRJoW-OACr3pNlc4nUCl_m0lMcdaWPvyVZYfPZsAejbz0thZ92_j_zNYM0rTV4BZ0IhPmF0iHPD2cgp-5Lqd9o5E6GVAMZGfIrlMZXXKo95lrU9XuNE2SAruf4A6vRCfvYHg5ImPUqobo9xEzzjbm-0AK8hfgHiFpJT0J1qe-JMJnHezSnxheJbq4FGLM2BMCdKlWX9r_PmE1uDMMjpVupuVyUQilZezgeEJ0oBmYvPGwTGlwrWl7Oz4TAxN7AIP3LGi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=L2N-pCXbUECuL7HuZo1bqGhBQBDvRKhsYInJ_SWfIBTfwfu_kgUN-f-H3ERonb5czh8BEll0ZRW-rCiKkJjV4W2ElDAVHlxhldHLZ8fFFsx4aykBBdLRMFqMlK2SfPT7DOJwk-nk73hYuW_TB1ImmYY37zT6OyOzG0ph8rdPsSVFse1R4fAIQ3Fscx1TmqN5s-VUp_ak9S7jOq0D_hoXl1xV0MlbrpeJvrzqVsyr3R6VKnJ5VKK0SvSas_zSFcdBp603WUavpTuPZORiBnvKNKw6ZnFHUOm0pZ0c8g2zfTmaj4Ag_bEe6K-CnKBQHtRK0zEiVl06nmo3gGRteYCYhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=L2N-pCXbUECuL7HuZo1bqGhBQBDvRKhsYInJ_SWfIBTfwfu_kgUN-f-H3ERonb5czh8BEll0ZRW-rCiKkJjV4W2ElDAVHlxhldHLZ8fFFsx4aykBBdLRMFqMlK2SfPT7DOJwk-nk73hYuW_TB1ImmYY37zT6OyOzG0ph8rdPsSVFse1R4fAIQ3Fscx1TmqN5s-VUp_ak9S7jOq0D_hoXl1xV0MlbrpeJvrzqVsyr3R6VKnJ5VKK0SvSas_zSFcdBp603WUavpTuPZORiBnvKNKw6ZnFHUOm0pZ0c8g2zfTmaj4Ag_bEe6K-CnKBQHtRK0zEiVl06nmo3gGRteYCYhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQtf-Viw8NVnUgB_u20I7Cz3xEM5e2wj_Dt_XtjkS2UQiXGt0C3qXDyHCl6ab4VLkTGsSxOiUzfzkeDRXH2L1iIV80k45olrMn8dgQ3RX9aNfaytQ7Mr5iGVaz1p66SACzhuLI-XVGzdW4BZ-eGgnNsLPNC-SKeYhgxaqEolG2SAGfan-IucPzfX9oTkoTImbb8uCGraskTnLNpsJopIyVE5RI3UtNwS-svYZ8x7Qu7K1Tfb1YqEHDsYwu3kGF_Jl4aFaYUoKo_RTBgT1NS3yW-eXSmNU1e2nw3tveFVlQ1cBcD-06iFhJ60EKyVKbZo28cxrWIDAQSws5gT3fAhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umkiHHOXK8swSqJX6jtKVcc-crANtHkVEsH5wH2RZG7J7waWwdqtI7_KePwXT9BXpUDrScMaiZfWR0rrzIJGNAaSULhFQ25d4cC0e_iovSAEpgFR5bFaj4FvpIdPg7ySJ9_-eA_MSdY2fjZEm7ISzl-twRISNFFaZin7chvdOFEiTDWnyd_4xWwXzBIZFusVNI83_bz3fS-9KZ1h76Q4YGyTyQeTEkCiKZDFHhROvrbc7NEavxz9_sKfAYxUONcBI3wliOiXQ9F8jZGFfai1uUlPjIC9BliYVGWW4DTd_lwQW_pyQg9P52oxKyLWKV5ej1aoFrgjDDEv_whXU2gh9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrqifjtqRVIA51eWknUQbFzuycsA4b9ohS-cn3Q1cN50mtIhpY3mdviM7bF-ZENIqxw8Iwb8MPMtfUzSaTE7bqWz7ULHvn4sHAsUQJDl1RfMqAAEWKcQXUa-R12vX1uAJ46S49RT8anzgR2Q53dPqrZB3dfDn8nMq1H3f5YqQgD41CGUl3n8xObcAN-YvpMbPBcp_wCA21XeFL3gYcYpfCpw2Cxii98KpqRvmzAr7quIP1TKI0Sbcb8UW2AjhOKiNOThr7hZ-PtyzBHR9MQqimBLs0cOLszhaDmSPbnGrrdcqW_I6EpnfxIWjGtTMObPLmfsGkISfdcWzYueXRUWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apKr73Uyu8LQ4jkk70DRHIn6MhVH3HvQqFwZSOCJFGPvy3BRZOdKyGBc2AYT4pQHHnRexbZAQ6V1zwgOvXkLBtd9-biIPAMIohDBefFZE2CWSDEfIokzyUZa4bfE1IKX9MxJslxI9D_GY25nwTGyF94mihbc5f04T8-d_vvStWWQx8OO7ctHE0NJaDjLFC4X9RGX8sqLNMJyEjHnzuQuDWkTCEMs7eWWPpWHtZDG_bcp3mCtq6FxV7FoTRId67eEpSf6RyIUOfzzWdWgkUwZeeWZdJjW3y5VWOynk3rZlI1TwmiSTshwTWiuQSY7o_isxWQzkxA7KY4m_yAxUI7QCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1F9DD-su4SXkjui0ZZpMH5CVj4EgDFge74MJyp573w8Nwxo2jw0ZUMGgzcoll-xDK3pI3_nHGtCjACHOaWrSkRTXgNTv38ynchWiuIKE8L437J9s9E50UsUEeeVmj8-yjjduIIVl1Co4j1KW2OJvWl2BJ8U--vcoic86sKVc1x6YhlRwgG2poyaO21h3U1tfXNQzLQjOphxIArnVq_fCvx4_cxhwkzCZo5eKOWeuAnIgy2kBOeo76PNGpsEXSooL5o-Ngia1IwG1FArvkADk6te2VN4bNMWGaRdK3QEclE8enuzdOnsxYlUR44gIYE_v8bkQiWt0gj4l43ut_Egkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPIaKQFc48iepjS0ZsIMXUwdIpJunJjRrh4egpwDj_RexJCIZu5_0HMeYp6Tuwl_ZWguDcwVgSKWs6GIRP4ulCvFHf04v_obHgioyVhhpSZM3X8Ejkd1A2_KRUwGG_UVgDfRkzqro3JhI__Dor5sfiPrEquNtkNZdVe3lIqx5hV2N2wnqG8hRK_KNrOWjPS56lILbTX-w_z5IND-tzD_ET_kFKwFzUbf4g4px-qwkBXLBJAbxrrnyrf9l_A9-rz5kE7tFaxSOH7ZaBfVnfqnqzov-Zdzs9NyR379D7ycrakUDv_bQ_vMc1JdwMdCiZwKbByCPzkHyKUpqzXDdKoUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=PF8vw4t2_lSYse0NUGawEAw2vD6Pkz9VCh1E-0xgAf5gY_AHD75NXpsxHLeE0CfSFOYjlGtzyp7zWu6RKxipn2c1mO3gfVfS0HyqoiNs8JG6XL8dFWU5_JYw0jyI26Q2fCCUmt_PQfCxZmjqpAGIYb08bTlbfsLai0dVOqYNllTc3CP1KM1c8k3L4ju17EH0f9shD_i0lH-v82eOhV-gEbbGXeBdMd1S-NGV1E032CBbbTeiSkZjU1QraGNuc93ORoObeyU8SdbIOExNp-qSQUlowmq9a-1f9Nd2z451dBGsKcRusURBbWdUKf6LKHGR02-iVpLgyPzKI7JxFiLvcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=PF8vw4t2_lSYse0NUGawEAw2vD6Pkz9VCh1E-0xgAf5gY_AHD75NXpsxHLeE0CfSFOYjlGtzyp7zWu6RKxipn2c1mO3gfVfS0HyqoiNs8JG6XL8dFWU5_JYw0jyI26Q2fCCUmt_PQfCxZmjqpAGIYb08bTlbfsLai0dVOqYNllTc3CP1KM1c8k3L4ju17EH0f9shD_i0lH-v82eOhV-gEbbGXeBdMd1S-NGV1E032CBbbTeiSkZjU1QraGNuc93ORoObeyU8SdbIOExNp-qSQUlowmq9a-1f9Nd2z451dBGsKcRusURBbWdUKf6LKHGR02-iVpLgyPzKI7JxFiLvcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGZ6yAw3gpT_pfVdYb9ALQBs1rvyq9LXfMl2LxE8K2uilGDZyMw0mjXvjSj5t0zfBDCxWOtzpH18YwYnHuBX7c849unfNnqDESTlp12bIa25pDr3uzLtuXf9gft4cKq1a7L8u_Rij7K-agfVDk9EiSqnV4S1mM0E2S7mnmHZfOTEk2ltutG39ug4MI14PDldcRZC_lxRQfhSPFPjTTT_wLf3MS4B0w6WCyIo3B9m-qUobQ90thw-AUjB60Ok3fFq26OPkufH16ovjHZTZ3y320seSvG7_lG-p0qeOKJkpO1WRmYqzW3Y26qZcgiXECCcbdL8zhRsc7dLkPcVPzd4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGdFq-vUOHG3D2UGafWlKAAbPm2cF-sQCR6Zu5HLN5Z7ZG-P4M6sZY5rVeWGMlt4vyKhwXsqc5gqNnmLi35pxAEMHWqnmvA0lX5z30wHCd5cjqPhmOIXugSjoCza7_oEijI6U_7JzxYJD255vOTlTIVXfSvAbR2idHoY9aEdqzJITwha7BQ-U0kUWdCr0xkLyj7f7NfT_BjgeU1MEjGreSQ1Dd807DcIpoMHmJCKT4t4H8mr3Szc2LQBSpk9x0XwMxhaa4f1AuAMoMXazx2Cg9Aw-gq-p_rI2XGmXu8D484UDf8NGeg8TZrUxtVEjjMgMjISUXflyyTNlQgbAQZf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn9smAGhTIOS_ZZ_n2ih0ffMXC7EuuW-UzJtlUhirQjAm0jvccEtlO-eCoR_ZlICI78PGDcjaxYiAeyVmkgWx4M9Pr5Af63sInoVTYzXRAX_PWzO65vuTlrGFjXUGto6RMWmbVNoE3lYYD2lkJMS7aUMzvPlXLPIUBYWfcUJ8L75Uj1yPQROoebJaywQWa1MouXoC_LVWE3b-Ot4G2a1isHaHdWhx7W2Cc5e1UXXrRqhdw4k6bXS76HvWJ5LWsx3YcmH9PX3WdFJP5GGn3YnvkYPmNQvLyJsBzgLn0QT6kFc-GqA2l-fp_KVaTjSCuXeQ7PNJqC5MlzzTMhFGMj3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1SAjSfcyNJanasmyNc01q9xW4LaJUz_tUKsMY2irGt4opSH9qiNoYrFNKe3juuvaVPv7R52jw85fq1ztatxtYmM-dp098_Jh0ENLBOVBtCLg3i9xoJ767DSWRcX1FP9XG3y0_3jciG5mtAwMAJpgYuTOf7kWwp4mjtqLzDQte8ofo283PMMg4Tz-QBb8F7UWfl0woHkAmLXodyqQGDJxrfjL4jcbFcCcsTTwz2Do7yIQ1LEWipGssFxdsqj8ybuMpY8IZFipGzh5nOGTg4LH6L52hiC3ET3D2E8A8lGpBVmrxB8I6sAg2MFKaN6YJ1iTD80MoqWJp3XvUY2VHB6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6dUiTt_cjjh_9iFwqDNxzGefYUQARJKL--80TiDM8oNm9_IVRpZnfgXY35Vzy5q4M1D1OmE0vU-uFIpcGy6oj8jhniWBgKP7DRUokJyKqN2CkG1hkHkaVWG3Q2oOWyzdm2JiFoX9b68xf-FtOEVZUjCAHAoKQVTZW6xe8UvBW-PZbsWGshom0dkt0Dd8rQmnDUKsh26uZeTHR_pSWn8OCQDfLVWVK-N-G-v_lh8X8VKWC2wU9KCVrJ0AE28I1q9RhN5e6owo3dvf07n1N79JK_-Aik7yybklNTEZgod5KJ39Lins9zTq9osJB5CxaoT5b5CiQCEe1Dete3vVPCVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsGvf0fjfYoQ0m0HxQn1239ctjSda3uF2iOfRchR84bsnTfFsbr1uGD3crrC6k8qX10rmuDZ23eSZGqRplKY_S_GAXfGLnDFsOmeWofdF05IYIGdDfT1O6TiUf3Lm9qx9I_9o65XlpRXuG7Izdykv6OqDBx1OqktTgeKlqe1v8NgRXVD3qiP69rPFzd_URprPBuhXGgRMfEScQ7SLRbK6ipaKj9lsOahDCHvnBb5tXqh_-eOMQfJVOGvCFHr8e4-5eGAXEKrdF_KADEYmwM50pya7Rn6l2mjNIbPCvvK2MoYFec5PbYDt3ctZHLvJjbeo2l-gFBTuTfwwv5VFkNS_tac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsGvf0fjfYoQ0m0HxQn1239ctjSda3uF2iOfRchR84bsnTfFsbr1uGD3crrC6k8qX10rmuDZ23eSZGqRplKY_S_GAXfGLnDFsOmeWofdF05IYIGdDfT1O6TiUf3Lm9qx9I_9o65XlpRXuG7Izdykv6OqDBx1OqktTgeKlqe1v8NgRXVD3qiP69rPFzd_URprPBuhXGgRMfEScQ7SLRbK6ipaKj9lsOahDCHvnBb5tXqh_-eOMQfJVOGvCFHr8e4-5eGAXEKrdF_KADEYmwM50pya7Rn6l2mjNIbPCvvK2MoYFec5PbYDt3ctZHLvJjbeo2l-gFBTuTfwwv5VFkNS_tac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSXc8EBmsTOEg8uwCHWhsAp_DQuHgcF1fGRjkQw9-bw_QEYWXpN1jaA1CSG9BZEjWN39Jej9MELdaif9MpCGe2ez97PZe4qUtLxfMzWpiXrqwkp2jKMxSNRTFLBQgzNGgmkFHP48-n7sWpKX139CryVRvYmEtj4jmP6LfETLN4VWr8Q47HJ-xzjCRfs_tyl3sORJlvqRVLSBg2sNFs6bt1kVeq_DWNTm3p8XID_MzWAs-IbE7ZUIXgN5H0DiF4WKxXupfEKrYwlM5GGTV0Bd4vN0Q0jWNzSeotVXkUm0jy9X7leewp9SjGuIZf9wY_EiAlG7tfzGHA4XTdPcVfcn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6BBfy6kZP1hVjqwVYJWZ_i-WUJCjtr8xUdEjsMNadgkVipsZL3FYfAWlJ-cAMn6rIWZkMfmPBJvxcijHpYSoNWMuvGUCnqqHqjX1Vl2DQ7eOOFOeCwfB6VxfQFEnCr7mcCwP8PVq27e790U_y9HkUn2DjoEweAxs-r604YaowEoJkJKn8T-uDa4QSLlahx6RBa-BUcighWH0_zMYZaH7n44tI_Ot2RwS4mmOyjl5T3CKdL8Zjk_WDGi4efG1likhPSlprk2pNkzIcdaq6HYAeJslmVSFPL1K5dlaUlk8XvA-O1hou4hQCEvDyOJjrYC70ozXft2mz61bJHVU4A5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=Vf81S7fFiLwbe66Tu7biG9LnzkuqowxgHmjddyfhCa5VsTD741Ly-Vn83QScIQs06X242zpBuAI6wXGLezcpP8BEUREmEQEWbBK8BiAfYeFk7_qoihwR-BX4kdd6qwHnQtsxelnrhxNsOnaX5V-VwfsRk4Vix_floD3kcke-Af6cj_eM8Z6KQLHn13fqhzEKJDc5ISEKH65I3JNCUTdQrXwALrBmAgAsGYktzRNGFxkZe70Z9pxQDqIVOU7l70rhA-cHtzXpFcygttQLip7fDueU_nZJDdSRREiFzApl06NuDDs24zkDpZONdHQZpEdL_-C1f316h0KeYeP51_pLKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=Vf81S7fFiLwbe66Tu7biG9LnzkuqowxgHmjddyfhCa5VsTD741Ly-Vn83QScIQs06X242zpBuAI6wXGLezcpP8BEUREmEQEWbBK8BiAfYeFk7_qoihwR-BX4kdd6qwHnQtsxelnrhxNsOnaX5V-VwfsRk4Vix_floD3kcke-Af6cj_eM8Z6KQLHn13fqhzEKJDc5ISEKH65I3JNCUTdQrXwALrBmAgAsGYktzRNGFxkZe70Z9pxQDqIVOU7l70rhA-cHtzXpFcygttQLip7fDueU_nZJDdSRREiFzApl06NuDDs24zkDpZONdHQZpEdL_-C1f316h0KeYeP51_pLKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anj3tHdcpzYwxunpVx6qgfg6fNh7ekx4jv0LV-aizwFxxzY652QKKa0CHOw4BlAYOf7w2TZRXb5sNh_T0A-pOlezK6JtTUSHkiiQq6fx2MxCJ84dxE7HXMi2MUMSfB28ttxPSgqZqFt2etQpRtEJmMSGuaOIwM7SuuawSWaDtswlBcZ6MxeUxSlnMyGoXc2fUZ2AEZzaim5JcpaRwMn8HAKoZvpdpBb3R0-XhhhyXLQlKhld01bQNFMt-5DI7wcQJJmZBsxCLv6_ckIDpb62TsYE_h9U0xxouzh4CcjBfPRza0W8Zp10juC0vAHuH0ytzP4sPhe7_2PE_xSJCPz4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=lKznes17btynRz-h22TcwHRpOOixei4xdrR6rzW0E0uGOYFV5JiO0K4Lk4GRPSK-3ubEsl0-bEH5zcYeNZmVfX_u_JyDKpZAGmMR3a7FqLHhKrYenf3A7YrNmdA5YDLlROxwIJ61l1r3Ht_mCuJXX-8GO-CR2U2WIRejfYh0uzy5ZbA2zody0RFbxeByci0fswFeKenwdR3sEL1uv9lnpQwLof1S-yZ76OwwmjnXafxS0eN4WZr9o3Xw9lPMzxtJXoGAjJzxdC-ZHvMBbLDww_vmFmIku2am031rcMN5HzP-jOnlOKlU6_ZMPZabuBufHTW7sfr1P6Uo0k656YXEGXIX_eb9b6HKQymDb1yCsAZm-ElCW3LuOoPfoppUXsl4_RAo4C3hDuvu7-2HzPgAAOmH3CV-NN1ftTpQb-QxhcnS4Z9tfT7F3yx2dcpJk0MumE86XOUTMKoOIXkhSzzjWzUX86T8vvGevfQQgf4kHGg98WurvsRsReiNE7efnaBbW_xVNSgrDAF7ahfAlBoKj2ggPJcSjQVshwUftNNm7VWykCTpwrX8lE6FSTrJsG_SjWpop4FeXpZohSVSpbTPGD4kUlc9VIDDreiYRYCQkpYUpD6M2x6VIT1BD7XPDLPrnG40YJLQNBzjzoo2wnlpNt-8HLM2LEM3z1UyQ-Nj1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=lKznes17btynRz-h22TcwHRpOOixei4xdrR6rzW0E0uGOYFV5JiO0K4Lk4GRPSK-3ubEsl0-bEH5zcYeNZmVfX_u_JyDKpZAGmMR3a7FqLHhKrYenf3A7YrNmdA5YDLlROxwIJ61l1r3Ht_mCuJXX-8GO-CR2U2WIRejfYh0uzy5ZbA2zody0RFbxeByci0fswFeKenwdR3sEL1uv9lnpQwLof1S-yZ76OwwmjnXafxS0eN4WZr9o3Xw9lPMzxtJXoGAjJzxdC-ZHvMBbLDww_vmFmIku2am031rcMN5HzP-jOnlOKlU6_ZMPZabuBufHTW7sfr1P6Uo0k656YXEGXIX_eb9b6HKQymDb1yCsAZm-ElCW3LuOoPfoppUXsl4_RAo4C3hDuvu7-2HzPgAAOmH3CV-NN1ftTpQb-QxhcnS4Z9tfT7F3yx2dcpJk0MumE86XOUTMKoOIXkhSzzjWzUX86T8vvGevfQQgf4kHGg98WurvsRsReiNE7efnaBbW_xVNSgrDAF7ahfAlBoKj2ggPJcSjQVshwUftNNm7VWykCTpwrX8lE6FSTrJsG_SjWpop4FeXpZohSVSpbTPGD4kUlc9VIDDreiYRYCQkpYUpD6M2x6VIT1BD7XPDLPrnG40YJLQNBzjzoo2wnlpNt-8HLM2LEM3z1UyQ-Nj1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ_EzRIf6nNWI6ru6swlHIvbtBka1-Io-41_ZY6q-pSqoX1iupXlkq2h0TzskhV1r5bfTGiGA5quNnqxAyf4WCjmiERnBxDCK9w1cNEJzrq8L4VP2p-O92ipby6rAGHn-1YtVNgVMdLPHZUbIcQIiw5AqDhMZTkITWPm_odxTR-ZO632YhCwEE5xMN9AHFDV-Ao4jQwYSh99Hj4i4LlPoaulHVcMl600CUOgibJZtp2hSsHgfW2p7cnXKuBoceWuxuMMDCoyuv40Y2JRGc5pwqjx0dDVEi47AgZn5oTzmsNVfCBejPf9q5WBvDNhps6cycT8WU24u9BrMCbHE89wDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvO1hPwougj0QhvJ-RQt2YVXvFWw0KdZ3ooCyfLL-CO4Odop73K6HsSpRL8ZrOEWbwtWx1fSZNBkmYLLUBhTgFAgcf39dUKDQrWkZ3pIBDiN7oo1hv8tdYpykmIsg_P4J0fNDTOzYYyEdgyLhXuRwNcPA7RpKhU_yR1VnzVq1r70-RxMPD4lcIUI7qZnUye8BtKayc8gxdZMUAFzJ7PPVeLrMsOqRFsGhVJO8_oHV87Vek5lAwIYE6flNZaVseb598k90wIU9VVeiDnXDmeH14EBAgfp-eWZVT-jFM-UBAH_o3YJwlVMJwnRXCSkGgsEXQK0wozbOc0I3XCi_CSRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7agUmSG-yrJaInKGFwm17aowT93FBDE6_zmLfgLcWn7NBkaDhnBZVfujWRNQf9rv1p61W2GwqPPnjZ5_1FJuXeEwbfTYCRLYQBpjU8Y5NfKynXSVL-wlGRlO6OonOp8izHw32jEk364JeOKM2OflNGXlgFquXKmn3V0JTTmin4XHppoYLIIP6a8j00UljQUkIRxgBeSxA7UIxysBvJVPi3rd0tJMG_sFO3pi57ILqRVxs1M_nwid7-erViLp4imlkuutyGEOhKEYuocC_KSkbOlXXbl7o5dpOibVc29QxfpcYK5ACRmDf3Gomdbazg0Vz6S2uQdMX4IWmSZsOZuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=upeEQHv_yjVSy4irMi_KOetxK3KCgsYuylIFUkRzKLd_lnwGqiUX_n5PibQ_0GJpRfMgk1d2pKTsRPD3--CCBx0OuptXLad20ep3OgnbjoY07rpyt0BzX1I97dfNS9BE1_vHxkHZf61GezGEj1x6d00BufQLnWRuJ_uvIMadsR9MvAQCCfUh08WzmW0hfdm5XJbfO7BlVF7U73Kqd8Qx3JCikLs6DjOL-nlZb_6nTusjrzLz9GaYwADTMc8qfqPFPAb9OwNQGBGk3oIidQN8yWpwxkCGRgVsC45Uyw6wNBx96joBu39NSqlm_On015UthFMeEcy6kpNnFx8VpHIHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=upeEQHv_yjVSy4irMi_KOetxK3KCgsYuylIFUkRzKLd_lnwGqiUX_n5PibQ_0GJpRfMgk1d2pKTsRPD3--CCBx0OuptXLad20ep3OgnbjoY07rpyt0BzX1I97dfNS9BE1_vHxkHZf61GezGEj1x6d00BufQLnWRuJ_uvIMadsR9MvAQCCfUh08WzmW0hfdm5XJbfO7BlVF7U73Kqd8Qx3JCikLs6DjOL-nlZb_6nTusjrzLz9GaYwADTMc8qfqPFPAb9OwNQGBGk3oIidQN8yWpwxkCGRgVsC45Uyw6wNBx96joBu39NSqlm_On015UthFMeEcy6kpNnFx8VpHIHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg0NAZJD3UV6cN6eYpWM9JdXOXDSKNhHG33EE_c0MqiN4HRCx_NOicnGEplqcdyI4WYZ4G_pW7ky0Oywk9NU66-XEp2nQ9YtdGut4ST9jgULbQWLqRVLlh5vqvJM8QOSfEC6iRwtnykRN3mzebS7myFzT0KYoGNCeSITGpPfFlTiF2V2sLuj_x4yOzyRMKvLBMQ9BuAS0cQqN5getT9riob5aTefvg2aJxa-tc2r0LtN5Vno2GoRGCgbfGJNdg0_6vy_yEx5QP4nMfJyWaedePEKOOHqW7CEwAYpEKlqGTIeKp2g_bYIUeHRIGF52ulW2uBYlP85C4FnGPDL03-hRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu565nvQ58yjqYcGsZ7cM_SQscsIVfJr3i11Yg5cgXaJsNnK4Wmau27XhePWFeQ5DHEYcYSERCxi7kb3TAru-gumk_0fcq54ukYyu3qk1bAXCaowEJESPAqSunCciLa8FKw8zvRYTACA95h0mPqabTSayTgvuMzz5jl_WogSBeFvFjF5auME6WgrwyCrJi_pHLHzLEnf8PzXI1nomCAGSV9lExtYIiiPxav4M9s9KwHc4lTvheZVDfwF6YEpQuvGMuXH39hAi-a65XFtwDgybIkFsF-rj0bRuP6Yqk8MLwyQqbhHdWEU9dptsOt8BVfYlkAr0pLXzg68x2MJKUPuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK6WPC_bJyXWfz-qoK_PQwnk5ZWwLZ5xLCnBtFSwiY0YSS5pjIj9OLLQnKziiCYsmtMGQfT7Srgh2WyA3SyUfyR8WTDfPfMgekIlqFJmOMLfDYQeg6pHXSCH9Q41u9w3gccmij660wrfMemJIPxfMNmp-5QKu00uaYxrhMzvQDpIJTnMYfEtrWfaDxxwbS0_y2tR7A7dKH20bD_rlZTBjbMPD83aI1kq9HiaiPq_dQnT2xoQnKlL3e3a_0Grm1UzB1nwoxG0gQ6_xFJt40FgzMxwP-GWqiS39mcteHmPBDzny5vF6JOIts5BJCrjkjEd7kHlszhyvnFUsRy4tiSrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=CsS_sO9VH37lQQwsCc0hgVTXLT2JcSZm7-l7j7Nv4WzyErQwy3-PggJflzAsWqqMLxNJSideR35qqvGkWl7LcBojABoj3wFxrJYj0AAwWVPtsJqL_PAhp0xfwu3zTHez_CyNF33O-wnAeBpZmSRxt7RFC8z0TWYTLFrNO0IsWHioBJlgaNeCDKWBLu6he5d8B5R-hdHf7R1jgRAfnXhflErv_aUG1FvN9hNcK_t6qjw3vTZLurLIwrVI8ASKU8XPjC8tCUYRaxDX9E7Ig_2TbP6x_bxjinNfc3UYwk5XFbNgknHxtP_rTpwbn-QkX0IGtKrrs_J4GjYuK5ZF0HVrVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=CsS_sO9VH37lQQwsCc0hgVTXLT2JcSZm7-l7j7Nv4WzyErQwy3-PggJflzAsWqqMLxNJSideR35qqvGkWl7LcBojABoj3wFxrJYj0AAwWVPtsJqL_PAhp0xfwu3zTHez_CyNF33O-wnAeBpZmSRxt7RFC8z0TWYTLFrNO0IsWHioBJlgaNeCDKWBLu6he5d8B5R-hdHf7R1jgRAfnXhflErv_aUG1FvN9hNcK_t6qjw3vTZLurLIwrVI8ASKU8XPjC8tCUYRaxDX9E7Ig_2TbP6x_bxjinNfc3UYwk5XFbNgknHxtP_rTpwbn-QkX0IGtKrrs_J4GjYuK5ZF0HVrVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8zWzG41ttpQQEFif6YneGaWYjkV4RjEf3AYvHZLB-__7F60jS8sGahFqvrfVIpbGLcT-bIA21SODmkI6CEIrZdrsUoax41thEt3RKFe5XJ7tPyF4g4e5ywTEzaIyLNvDOMbCc3MqSyKYdevLE0G99HyP4zktkLtxzDxScGpZZ9bs5o8dHnHj49aEXhVmdCj5j_L0FQ5CEqhZf_dkk_YiuQjgcs7ug2Jdxnu5zS_K2XM3AFDlHlIXuNJ6LVqSi7jMWlrr7C50Z3fOLFQ6hd_BliC0aCdc0NZr5Z293VxcV-k1we1nDI06-RnQBiKoD_JEy4agfCGC4mUe0YutNh_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNhtXx9mSYa2gHQuyLOiuOw6kx69Cu2WB4vjyveGV1-SR-18oOWlHl88U0p1hJtpxOXyN_V4vS0MUdrqqijjdrMludXDdSKWwayI2c7pZN8gcsilJw5cnq0npoIN9oc5Rk6GL5gsJLO7oOJ6nmLmfNwJUhxvDhEQtizYe-N8CCF-lzHBcSqyNy-SbDWr_AF24UEUiht1XZfzOkqtoH0lqUcT1HMjowsZ9Y9R2rUtyNrDXfXiHAFg11JN3nHsRFe7TfN7o5YzXZGatRuI2IvV3RcbwXwM1OaIcF1IZDnoC3Oe5r8DK_viqjf-x8dkVdkUSRZTNRmBwyO_UR_Me9oYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdKzzYkvZh-i7IOVW-ARhaKwMwj0i1-keaVr33cUS2EbI37vgcRgvt03Uhmm2-vjmteVpSOg7goMkgZg0kRPsXwvt52c7qDad6SVWK3rzDB4pIRN0XRDGSadamiaRQ8bNR1Yg319B8YngbDZIHCeG6eyo6US4jEQi2G1F4Y-Y0LQ4JUyrdbj8OuCwt9CKMCqV6_b6kdjpZsJrScvLVo2xSRO2GbOuvB4OjuHZubQy-TUZQEZ-SWvnyheJlafqWCr9w1VZnWN-kJpsu0HUvLAhUVid61DOQO-DkW1gB-Szi6kaXTCZTLDkx3YG3Z6q35CYj8AK4tMNtq4lW3Aw6o5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jta6Rwe_6QhD-3BHaadGIIqbrU17S1R2fTcu0ncsOvi7pPUoYF9T5x6SbYEICw0pnkuiA8hqFr6glKLI6nRFsk4z9VS1SHmtlc7Lk5zag_BcTcgavY9AeTEHKKZoSHi5ehsMOxX4_rQc52E45Jv3-AYXSjaJd_SPj9wUKwYjN7rDW-wFO1Tld6pfWrEqPSiTVpD1jvJA5ZZGr-Xc8NBPlcdSCDjDa6FDTuavMrBcxL0BIJ3GRB5lv_RweHYFgHnLAeKMGhxyBAFpEdjz0eIA_0ptdMWT-4kUiI89oTAXI5cffryPIppJnTOmQ7AkWypCHvs-3uklmfmW43O0OsTlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BO29MuiJ1LzbMG8zq-OSCrnOgsysBrqZcXfeU-Ys4ypJSy-A3NRxauo3xxMhTmTVnuiYO2rq5NJQ0DdJSjYtFsvBmePZKWF2WpRltxQnyJyPxXpz7R_-q6imj86XZr28m2KEd7_p7f76Vhyeqj30w4MJ5vPTxRad9zA_KJNPoWhnr1EEAaImnXLn8zuMvNM4KTIDKrzjy0yAW2m7ZaCb_UN7NEIFgNbskuns4ThF3tXmL6oFk7tV4Ru5rSsXJU0U6eaWIdNySqlVHImd77jLq7JvrigwieAsAu7ByC75PTOU_zZr6JZKZq2SNqwS-f2qmjgyUurK-Az9wIK_9QPrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-tiNKH-HcMkmjLaDSxmZ3AXZ4hClMNc9tqUctrs6B1cgqBl77SbTVk8PLA83meZZ0PwUdunOM99UChwiR4kx_HaqzB6eNeEdfkepVqFYaM7IyioGeC5QE1PqTVzApIKG5LoWk6ZJsc_OLBsJjcWkNrWJs8YrdzVtAf3hjBCiE0hCkW5t7hMsoNBt5leDIfkgFPHVgkIekYLFFmXOLLkxbHgjR2xBCvQwxDV2Olv2gkgJLvCDrJ9nQwKbfQQ1p2vEmIEaoN0PE_TIt6taNaJWutLaPSzlve21B__zqK-FOtlsdZTBg_COVf_OEdygDjKjdxp1I6XS-TmR2miLlq7cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVoeFc61XM-t_9Kv9ATZwmIyA3fJK6D4zjcE88734GPYu5eD03zTJwZVsivi94Wrxq8Iwrp_IJ9Ror6iy5DrroQ3TT23zZJHV2EApu6j-IezgtWXLU7DVBvZ5YYHc2C1YuJFmEcbmAojP7cJkuVRXXJIP4Bhdd05Jv00n3CS7waB3f4zYhL1PONoE-SAS2A50UjvzUJQn-ToRs4hc4kR0KlwmAr7a_6awdY63GsEMKFzyAixpiukwplMWHKvxoTsvhJwb0chG-ZmQfLTZMtcN7cY5tnC6mweTzynQaFoGBKXhZoiljUPiPA6IdQq6GwZ0sod0ReTFsOMWYGuEq2j-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=OG3EMffAS40zbFtFvf-aQ2AsojNo9G7RuIRktGmM49uN9qe6eo49rLhMEGjHNdKPhXoBqvMmL-lVQVS5ZE47VGPh6WdstvBLJaxlkZv031IdhvOf8u2u7eEu6zppKamE8RnZ0mpYk5wRwhYXDuQOS_1mAwumP97p0r7DqA3O1q-J8DhaGRfGPbhC3jXgW2fB5NeYe6DTMBXFD24blII6lYs8Po4m3t_HXvjiCXS34NzqhNGNsxpEd_UgTwn2T8PvotL2cuKCb_aZeHuACvsTiRoU6V-Sd_xo3jjj6zQYAKtz-ctVV91bkhqtEg73lMKobp16KAFgM1F6EOXsITGCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=OG3EMffAS40zbFtFvf-aQ2AsojNo9G7RuIRktGmM49uN9qe6eo49rLhMEGjHNdKPhXoBqvMmL-lVQVS5ZE47VGPh6WdstvBLJaxlkZv031IdhvOf8u2u7eEu6zppKamE8RnZ0mpYk5wRwhYXDuQOS_1mAwumP97p0r7DqA3O1q-J8DhaGRfGPbhC3jXgW2fB5NeYe6DTMBXFD24blII6lYs8Po4m3t_HXvjiCXS34NzqhNGNsxpEd_UgTwn2T8PvotL2cuKCb_aZeHuACvsTiRoU6V-Sd_xo3jjj6zQYAKtz-ctVV91bkhqtEg73lMKobp16KAFgM1F6EOXsITGCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6ekXDLkhWVM-lpbhe00WKfMRg2Hl_CnSo2cpO9pxzFYiRVTS7RrudvpmHOy2fBevAMupcidW0NsHFHkxMOcZaUESrQs4dMhUCTtqZSxlzykbAfXamasT3mYr6p98WKwLh2tcR64KJUn37tUx4GsJTph4cfo5dKz3yTvK6UNecIZhANYSIscoVQpoMSVd0KFT3D8meFZx8MmXklYPQuIhl2u-_dVX-Wc4dlrgwd-IZvRC-rnNqX1ubmBqnuP9eYWBGGeB8Gwiyl9kcMVJYjRDzwix76eftjnL1izZKvdUUejz7bHqy1amcrslO0DXbdtjZi63-EYLDe3YNZFg6ecIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7DIyYjModGTAcUFrmnD9F8q90NlVKkbgjdXb-UZYh4RvvoMpCFdGkKhev3mi5LgruyPJGBhykdi7Miu2s14H_PSdszM8A22Br5u9OwpbNJuDNi2gR-P7Uk7ttqqVAh9N-ykzjH6BFf75kuWZYqZ74X3vy6SVKIEuaL4IENbNYkSxO95nfn4RjKsuf7NrOS2iDr3TibLtMKtBSOFt7ElGxot0PBQmmRU6MHXrc242-YgXmTwfmi0nrUxTikobcix4h44-sIXWt-fqVNH388ESK6wQLcFGtotI_Jl2L79EAWjJYOJZj78GlhqNruDwXb7JAvR1FAt5ewC63wAlnUYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlqPLgByRTUf8ORldCF86xnNu30ej7Ce9l-Txw1PtXZRUicN_2cxwgz80pGlaU65KfmT7iDFOLPrXzquECcFeHsCb-APmK46igTFzWlrIr7wMz1E3UpCAA-Rop4CDOXNHslDw6BFSiwffeV5cDmh7cgirSbE1xc83Y9A8XcFZNFxCb8u0he24q3MApBpXA9i8yQMv5NaAgJqpeObsnFmupN8Mpbc5oNj7Fhbd_M67KaXFzdDtLmXYvYu5ntTlAhla-BT2UxqTrzHdmsFxgn4PlBxOeBSDAfeFFYzLwYVy-4SM4f6oCQ3dN0muiJYrqLevbEnCCJmEOz2dbVkfvQCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=bTVk0jlN7Ig5Xtw9CWwTgGd9Dee_XrLvN6URtj6ugMaYHYMNbyq_6-Kita6OGCRbWx3UgonOlnlrqcwkGy3wImJ41UXr71sRyHAxyB1X_asyWtlV8ITbWUpnM2CAyTuZQGvFeBBY_wbpaAN_DoU4uDfthhsnwBU5HSVnuwM5LGC37xTVAM77NacbfNw4KXJuHpmcHMXT72w3pwxlZJchNg37avDrUsDibto5_sgWvWMxTgN3yVVooOTlvbqjpG-1-Ifa85fzG-1ZlPlrZNjkJ5y25Oau6vixxStRLu3JdKE94wCgqvs_x2cEa1VYBXaFKjiPvfFnJGIRKntbLwn8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=bTVk0jlN7Ig5Xtw9CWwTgGd9Dee_XrLvN6URtj6ugMaYHYMNbyq_6-Kita6OGCRbWx3UgonOlnlrqcwkGy3wImJ41UXr71sRyHAxyB1X_asyWtlV8ITbWUpnM2CAyTuZQGvFeBBY_wbpaAN_DoU4uDfthhsnwBU5HSVnuwM5LGC37xTVAM77NacbfNw4KXJuHpmcHMXT72w3pwxlZJchNg37avDrUsDibto5_sgWvWMxTgN3yVVooOTlvbqjpG-1-Ifa85fzG-1ZlPlrZNjkJ5y25Oau6vixxStRLu3JdKE94wCgqvs_x2cEa1VYBXaFKjiPvfFnJGIRKntbLwn8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5vqLKZ4cISfpgLgVILGoG9VMZzM4IOVunUjj3R8OlnXhoqNllV8MwjGwe-SUQ8wv0uXpPFBsn2MDRMqGBPfdMy1S6LBCrZkk5E81k7XYoS0xZhxwE1oBj71LRKHZ1d_yv2_HWdPiesVimREazJ5xQiwzFvnoia8NNFDNGsx14O-UGKyBpEKVY7OlbqIsHy5j1Jf7kyoUQN4v74_kPgMEgFHooA87bO68Ic-NAdugBB15YD75M93WfTcvBuOdOCF8kGU_i5Ob7v47vEgcQRekiw4-UDTt2lFvy1vImMFjOan9SplvNjLSND3IgIqG_LtqzsgFxO5DCU0p2qnVUMOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrVnRw6Uvz-i_yrnkPzHqKsIidj7z_rETCDCHVmEsigHVjKdbuvqtemFbAMJCY0gYYYrlj5b8yjSavFXWhC4TVLp3loSJMdaQ8onjSOVf2WjgE8B7ENb15lhiLNe5i-Lo8SrHL4-tJ_1LkgTVAENB0-IQLBKm-8U7nUwmQlRZqq4JjqUBBE3MzAyBgpIugy-hMRVaWyVMLJ5C6RJtcTbuFONeYI7sgGQiaQvxnF03nqvB2Jl5S4PKEQSf0MJbp4D1cWNNEsCnH4gTOYFLol20TFu1FkEI_16V_lffbc_jpSHhC90p7W2xv5FRDGKxY4H8VtQDWdjgigbZJ76wZyybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4WdgtvB4qrJeTvg_jn4b3bXJ0JZ8iJt3-1ii1yuVCyQfwAanUPq7_mRAwQTx1ARwXBM5BqiUxz27Uqr_V9U_yEkc45yctxpaIeEH9v7vsuJgSB17sAnOajyPaiVkS8xW3SPO7NTDYQtR1wn_rRhij_3CQedTFxxsA5drOwQceIF-5ohABy15_dEaGszAUmxwFqnbqW3G4IgkON07jYSy12MwhLG_D1V5xQhgtoJqTnOU2Sm8QAVM5B5FM_Y-aUhluRr8S2Yl2btmXLojGHSIJkGt5C9a96my-BcdGhWr0iwXVFEIcHJ3Ts1f9ifizGYdMlcPI3G_aToUEOUfMWbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz01KBxZ4yXIEEi9Mz6CVPUCgDpOKscuVaMAsJ-c8XTGCxMuhnINEUIt2wH9AhdOKQDpHbtHiXF99ILc8H3qViAckPZHXjMcXR2eG_2vQlaMqDR1fFjoW41oAk5Q9c_VqhNHQc2xpzCZHkSxhIONeIeAvl4X7VZF9BKmUSOzVxZN7lXBy3Dth2hmZq7sHOFFmaaIi-gCVeCEGqn-8kuDPG-OIME2Y2w699PRE6N8ySkCWHtAYFHbHnIRvgxh14I4zhPzuM7zubTMQejAxmIS91S0M-hrLqHhZHJHw7QKR-5jyJ4I25oJ3Z4SOq9zBFNnXUtfwv4g08LrjqESArFS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD-lzSf17ypkplt2zqkZaYFRnzaNq0UNSPhc5SfyAm5RjgOGm1hwCP6eqEaxiHQ-WN6n3ha_IadvUC8FqblrhQR01OsOECPOyj159DicaQyf2dhs8yVi8aUh2F-aH-w8r6RJdAQ-ZcZnTvd3ssrSnqNyzyqGWjoc1lhdzI7KzjnSgFxBSLfVmTcjTUtbLfF_qpYU73naMvJ6s4VJckx0LrHeDZWRF0YN7pV-TqpdgLfY3utneBAyxq_lCgJF1vg-NhI6Kb6YkzSk65bF4vQ3wHr7QnXhvM26s-NUkoSeYMdaiA4mIFZ-hWlD0vQrmH5MiFDjBPxMdEq-hFlI1ShC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY9TCsfS6tWi7jyJIqVrQasExwK65aSoiZQX9WW1duLalMN7tzmhq0_oE4H_HmZwSq9HO9z1EqynSdAoCCscMdaKs6SGCNt7pY33PDGOK6Tc9COm6f1kiDYzPuDtaySv_hPlwHEwHPx60AkCLGYORU9MY7wXCXiWIOxBAWEyQocYkslMFFuTEk2KsxJ8PMNZX-pGPH0wG3WKBFXyJBwdXuvdDBIs_UBWHiFrGgrhS3OYV80JwtS2Mdm6zM0Jn74147_LlHOpa3MAivEP942Xu9NGXFRm-iLtnGqfsUKmRH_xojC_78uddrJ5VUXlOBkzOhuW_Wv5EVMgOP0uAywwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiUN5AxN5-ltNeAdaYw-ivOwRIV1mOg6hZ_-xW2GjjsMvj264eqYXb4lz3gpNTr9HVfMITpbmAVazb-OH-7tNHFXRXPPfWJpoX6gPY8pj9u1a6qAqLA_2Zgjkv5ro00lKE_vDg4o3AMUuAiPjqsX7v0qlKSrHsA-i6ceOo4lS2Inoi9ijBNUQ32rt9DCGS8qokGVJp73EdAtyjvGIyQltOkGdJDVSZ6rSZj-VmXy4-isyStkN9aAabUishuXMmaa7EIILkWlFK0GDEVmCpoC5ZYUOMD5quuGdz78ae46PUXHWeFESIabdb7F93WtXLTfs_nsrxqoYRU6JQysVDmyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=liWHBJPJHSRV2FszyGQSaRnkXOzLk2oxXYobYBl79bLrTKfXSAac9MaKdfJa5O8Ee6eB1GK2mBQ_UAAtvIJuAec6772suNJBW_EXzWMGVg6InaFTc7A-h8Y_iWo47x6aNaJqeyRDEBphisB08d7jGb5IY8VbY7vPokI510eN8nAm-yy40XaAh1h3eWQmAUs40e7Rb0qa-AoMoLf0wSF96y75O3YQU2PUWYaqtbBSO0HpjzbmE6YoNFD5BpkPgM5AC-DMI6O6ve0nXeVhytq1j-l_FR8iXD0c31fjM6czms24Au5BEmioIBbz29uT4DKDGtkvfk09cBBKJPZKrPcDjZo9Dn4V-YGNc2p9bTwUn90zT8st25WyLQg-4UuH1eFBq-kk32GP_ZUnRitqBgvk6BxJGUWkFMQqTXAq6ZcdMRKTQd426JW1itmPtLl2hvO4synYntEqdCTB0h6xqo8KhvNQrp2IN0_xft8xBcDkOyypAUqPHqsGI9UO8u6k7JWvebIHtr7PxrC_K_fp1V6l1kxDjwPH59bdooneLLw9QuKFQSjMfnFkqLJ1Kw1u7RasGvzU-Q7da2WBYh5lpQ60-ofA29y4vaJLzHOc0ROc7DUVT08ArSM9t4kZdNaoBlsMw3Um_VTSgtEaPUuroN8_kppX6o5T44XpBK2Yh6FIazs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=liWHBJPJHSRV2FszyGQSaRnkXOzLk2oxXYobYBl79bLrTKfXSAac9MaKdfJa5O8Ee6eB1GK2mBQ_UAAtvIJuAec6772suNJBW_EXzWMGVg6InaFTc7A-h8Y_iWo47x6aNaJqeyRDEBphisB08d7jGb5IY8VbY7vPokI510eN8nAm-yy40XaAh1h3eWQmAUs40e7Rb0qa-AoMoLf0wSF96y75O3YQU2PUWYaqtbBSO0HpjzbmE6YoNFD5BpkPgM5AC-DMI6O6ve0nXeVhytq1j-l_FR8iXD0c31fjM6czms24Au5BEmioIBbz29uT4DKDGtkvfk09cBBKJPZKrPcDjZo9Dn4V-YGNc2p9bTwUn90zT8st25WyLQg-4UuH1eFBq-kk32GP_ZUnRitqBgvk6BxJGUWkFMQqTXAq6ZcdMRKTQd426JW1itmPtLl2hvO4synYntEqdCTB0h6xqo8KhvNQrp2IN0_xft8xBcDkOyypAUqPHqsGI9UO8u6k7JWvebIHtr7PxrC_K_fp1V6l1kxDjwPH59bdooneLLw9QuKFQSjMfnFkqLJ1Kw1u7RasGvzU-Q7da2WBYh5lpQ60-ofA29y4vaJLzHOc0ROc7DUVT08ArSM9t4kZdNaoBlsMw3Um_VTSgtEaPUuroN8_kppX6o5T44XpBK2Yh6FIazs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKe8QTzIIp2_x-ybfrf-cx2kiEVnaiWpCoVSKnN7vm3bliXP9XwujAS3DUE0kSTr-jVzaWxmHfXyCVmbUFjnGueSVxQzvf2FX7oaonENHykjfCHn1iwsDTEcCmkoxnuvnhZAhDgXKwl-103D2KUsLuyXgoJ5iqjaiYai0APkCfQShkm9R-EWI1J1152a_N9t35sKaMpZPZ07WBsJ3Sgg5yGKHaFSWQEhEGaiDRoOQTrI6VKu_e4WyYyJm70n_vZztciLgyuwdxMFcemGTDTM6ev4RH3Jp9zftZiieQgBgpITqSQ7XJ0jLgMoWZ000J-n1slPKrrXDmDwsYWYxwm3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbFSpykTOLPUZ806h8DjhnUGwXzO9XO0HkQpyFT0Jsf6jUZjK4BUZ46TM1_4VnHJGaXED9V-BPd3VXxN5HSyZR71XkjPdho1o_HIS7mZmpuiK13m3l_npO78devuVL_wya4ggthmAeODxyEzQ5DwoxSkdAi3OBTqaII7KBZJXaoshqn-Ddk3oRkZKJP3t3guoQ3EtxCemaIu6wChz7hVvIiqxg997i78743YfRJPQNFjG7q_f4_hSw25xVSU_qnkI15CYfBQGnYsJa2gAs2G2TRmJ5cA-BIp3NFkS0S0DYIMgBMMn97ToubW3_gg0UgEONbmKf0ULDVq2lWaBm8gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbD9Bf7a6MalbXv3LLcSpEUD3Cx11thx5JTVl2Qe_Qkbyq_GZuCb6MsA6D72E1u6ChQxffjSEsQGiRWHcebhVdO7sYa5SPpn_DB0sd17p4abcpRhx9lgRJWhf7Igs5Y59ajuxG41V7EBCagzNFiDtsP8cUJ18Oi3Omi4bmXLaS3GitcwDoaOWgzEKcIQlFTMkBZBHhfXQzaS89DSACv3AL7fHAUOwp-FgrDKUzcIw9ktLvRSnp2k7m1fx2MGuiN68hYAFdKXdflQ7rwT3IKmWLjzfekJyWbQCFH42NJ1it7FJhaNSgMP3oaScxkgWBvFomX6eiyKJoxJZzO6bqA9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWpASbP8UrRP2BWEw5VIVbK0cTgV2QWUbVLJUGDldZIcqY3U_B8HwieI0S_gSHqGOlBASZIx-_n4PqHZOIgA2MFM5DelScOMy42L5C6uawiGKFoIIdM004RcgbB5gzqkE_zU8Io0ehCGpFoiR63LwyupjHb8qIw-uU_Q328tIgXTC-UL6ZtBtQuFbUE45HEqkr57Zh8c-WJTiqQPo3xMXo942osXffZCAU7EFwRIwMNOsg5rYN537S5SPI8skz5PXku4Ldl7zVW1z_nQgLsJWeELi4AECFVbuyIohscJ0FXAV6OTBeidliU-K5RwbcuA-7S5MkibuCt56iqwTXUb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
