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
<img src="https://cdn4.telesco.pe/file/a_3WjIVIYISIMsgv8675GW2cgHG0WWaOOOcI8niNhKpKpn797juWnbTYKAII-R9OtBRMsyCudfUn5gE4VSALtrKudArCj4Qfquqp5uD417Uru_Nb9AplFyA_ESm0CwWovMcpUsiSRgCZj2MtP8j2KleEWQPwrdO2t70RzU_IPA9leaFfd_-ytkukJmvGQChGWi1TaW20GSRF8UYK28z26eRWqYejY56WnCi_bqMgebnyFllWjEvkzBH4i6c6zxu02mVpUagGllaxAaSX01vTxuqZLwc1GNG1U1uP74aGMpDy8XPYUwHxgYzvsH3M7VujX2UU9L0setXBohTlyfKPRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 03:41:54</div>
<hr>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇦
🇾🇪
بنك الأهداف السعودي في العدوان على مدينة المخا اليمنية.. 6 شهداء و8 جرحى من المدنيين، بينهم أطفال ونساء.</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/naya_foriraq/91215" target="_blank">📅 03:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StwTKjVGaPjYzanCXyxD_xwNtiBrXi8ZNZ25Thh752OiBD-M0ePIee_DcNhK0WsYD0Jkt-YbwGORF3dFs_oxzh9w3eK07z7yv5Kf4dS_QAY6z3gUjK8jivIwYJrepGsdhwNFYhMUqFL5FKgrXBr2t51l-8Z6FXI7za4ht0_rHt061fyCobNddefi_dul3ApHSGZ48rOoJaHfQPZbYjVUCAi0JfGNibr79_-PvdhWD-TA9JcEyxoL8tvk-iO2fmw-zkDa8r404wGQFblI7Dk_wDKK8FhMCKDPZQFexQObS6W10lq7FYYzK5sjfWZKbxrd90R5S_uTeM4M9tm_rs5Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/naya_foriraq/91214" target="_blank">📅 02:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇦
🇾🇪
إندلاع إشتباكات مسلحة داخلية بين مرتزقة السعودية في منطقة زنجبار بمحافظة أبين اليمنية.</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/91213" target="_blank">📅 02:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPoBh3Q5s5dDXzCdiOGVmAQvY5euEyr2rJippwX4VcKo13yjL_Hkh9ELUpVOelioV0uNS5NIAoHjuUuXmXk7THk-CmHYFk6KTTlTe0tGX3GWG5-Ban_0OuAKKG3JKgqiKay2dswnOdaT8GN8M5B6lbjddoYA5kn8J7s2bpsTl6XtrYFObd52jMMbEh1dziuc5Gf3qJSBAkPV9lp-GPvl23Pa1U3gqFe1ArLjDN8CcfDC60c6u97aM5vXchRG-uhK28ZE-B9UJeB7gP5538NKMh_bqTH62D2iwh64ghxYvDwDkV3Yl_C4ACQQNLXbQhb_J2VU--9ymDSUhTqd-E7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق: حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60%…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/91212" target="_blank">📅 01:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله "حزام الأسد":
تخوض قواتنا المسلحة، بعون الله تعالى، معركةً مصيريةً مع نظام العدو السعودي المجرم، واتساعُ رقعة المواجهة سيحتّم توسيعَ وتنويعَ الخيارات في اختيار الأهداف.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/91211" target="_blank">📅 01:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsLMzd_S322Jz5dlIP27K6oCsyv3ARWfadaOlg8UHPxsNJeiz5V_ozcIo6VGvOFd00wzaxwCBNP4b3EaOscwYXdxvOdln-QVX8ffuQ6cV3rO5ff_TWmX2ogQidqzwTdE8mxG2y9GSsHcU941M1qEsgWAG-_crvcPmKDID1yvtc9d-Dx_zTmrjqxgaOmVuNz0Acf0BbmKFUnH-vNKrN12FngXaYShOdg9ye37ByBVypKVM7v-nlG8KlUY5x543r4fZyCt2V_xK4LApFFFqqMCbrvvnJeVy_Q8J-jPUwgqRLjROvzU9YK3RogLSOiV4vUwrUSl6V-qCe8Q87cGt3OGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5LHuA-8aYCVeLaXia5ALOD1y4A3KeBSFoR-pvEaiI2hXZFWfe-ulbWJzs_-6eOxM6vUxZwVJwZuo1R2UnsNQgnGYq-fnlc3xsJHzgdWyEdIFBaFuWEalaDtwkk0vOzyk9ke1_2AqhEwFN-NDR9WJsoF1oCP78opMx3WXkhYzknrrJuapEKLsMNUufk4YK8WJXxiuXEQmVQO26jqzCqEwUrDRiHhInKtfwiUAtW4PMcNGf_my6LEGZlYCslDcuivcMcnAeLQvD-xntuhsYqPhPuH91drMq65GeXSJvqca4jTxBKRV8-fRyKQOZUFUn1JJVB2VxNMmJTvchVfdf6XWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibeKVs1fn75m1Mbg5R60XoZ8sTyBvx_CFuWzHpHOLyXqfccUhPYnUcfw_TfjC7L5-JUmQip-BfD-ixB_fkpgzbdf6bifaigWjw3nE59lX8kXcRHTJpGsren2SOrCdu-snNaTmETxu7itVSX8urGB438muMxhW2NKQB8Be8PnW1yve31VGtkMU8KH8VLE-32fPFEbeKuF3Hh230dIwV_FAT7nSfUjrtjbUh--908o6GZZ_b2jRs4fFgPki3pksFo3c1Pnf335jvdi9tA654eXOz7__kJKojxBTsl7nesvfKP7HzyC7IEN572kaB9wGK-GrVLKJ5zPX7ySnmcXAvtr9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علماء اليمن يردّون على مزاعم استهداف مكة
بيان صادر عن علماء اليمن يرفض مزاعم استهداف مكة المكرمة، ويؤكد أن المقدسات الإسلامية يجب أن تبقى بعيدة عن التوظيف السياسي والإعلامي، داعياً إلى التثبت من الأخبار وعدم الانجرار وراء حملات التضليل.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91208" target="_blank">📅 01:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=q74dZX_bxswCUjNPL_vht722MY4N_9eMZs7JlsG2w-qFbByezrQiM1e5ntkoFIZ41133DPsVcmSjzgq43sVHb9W1_zv2K3pX-tQ8Hb2tg5llU_sSoMbCjXr-HFfs4FD_jxdOdvJagHrASeaTSrTDgFVopxVduPEwmxfKdU7SBXo03lh_93aA1tDznccm9wy-W44zw8kKv9xuAMgbfvFPaDYIh0UHw_O7IlktS4HmhLqMHPR18-8x3JL8W9Dk2F16111xbaxoMkJTqi30xJ2ZD5kj8Nlt8yBe7piH02CI3hH-vxEEMG7tm5wht4ddLI2jAckW9Eh0d8eBlY9hEdlJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=q74dZX_bxswCUjNPL_vht722MY4N_9eMZs7JlsG2w-qFbByezrQiM1e5ntkoFIZ41133DPsVcmSjzgq43sVHb9W1_zv2K3pX-tQ8Hb2tg5llU_sSoMbCjXr-HFfs4FD_jxdOdvJagHrASeaTSrTDgFVopxVduPEwmxfKdU7SBXo03lh_93aA1tDznccm9wy-W44zw8kKv9xuAMgbfvFPaDYIh0UHw_O7IlktS4HmhLqMHPR18-8x3JL8W9Dk2F16111xbaxoMkJTqi30xJ2ZD5kj8Nlt8yBe7piH02CI3hH-vxEEMG7tm5wht4ddLI2jAckW9Eh0d8eBlY9hEdlJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های بزرگ و رسمی آمریکا، از جمله CNN، Fox News و NBC، در اقدامی کم‌سابقه، پوشش مستقیم سخنان دونالد ترامپ را بایکوت کرده و حتی از اعزام خبرنگار برای پوشش مصاحبه‌ها و سخنرانی‌هایش خودداری کردند.
ابعاد این موضوع به حدی رسیده که امروز، هنگام سخنرانی ترامپ، نبود خبرنگاران رسانه‌ها برای پوشش مستقیم و دریافت صدای او، انتقال و انتشار دقیق اظهارات او را با مشکل مواجه کرد.
@Naya_Press</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/91207" target="_blank">📅 01:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91206" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
🇸🇦
رئيس الوزراء البريطاني بورنهام: وافق على طلب المملكة العربية السعودية بتوفير خدمات تزويد الطائرات بالوقود جوًا جوًا بشكل مؤقت لأغراض دفاعية بهدف تحقيق الاستقرار في المنطقة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91205" target="_blank">📅 00:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=ngcJPL5ScJdmJ8oRGjcen6VnXJT87yUTmb4XGDo1-qpeOg1Jr5Skzp5cfQN5L4G_o1MQYFKsrzX15U-8Vxi8UapPYk7ismTAzHX-w_BG3ws_wM_NZjeTRXkAtexogcVyIv1nliVB5Dpr-EHIfkeYaEC4lSrwWYTeKNCXSK08QuBHmn2HuSf1IMk8ZADTq2e2poCB_GGLdMlOTAsYnnDpHeezLcqtQgPrYdFLb4yUK_LkegRQhbFaKgu21afL-ggrpFQIExEjKbbMUDTNomGVFJmv4kMp9eELfEZr7rzolgQdC6mbrIvLkVtaAYeq7K7sDKZwJrtlsFU0AlOJA7suYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=ngcJPL5ScJdmJ8oRGjcen6VnXJT87yUTmb4XGDo1-qpeOg1Jr5Skzp5cfQN5L4G_o1MQYFKsrzX15U-8Vxi8UapPYk7ismTAzHX-w_BG3ws_wM_NZjeTRXkAtexogcVyIv1nliVB5Dpr-EHIfkeYaEC4lSrwWYTeKNCXSK08QuBHmn2HuSf1IMk8ZADTq2e2poCB_GGLdMlOTAsYnnDpHeezLcqtQgPrYdFLb4yUK_LkegRQhbFaKgu21afL-ggrpFQIExEjKbbMUDTNomGVFJmv4kMp9eELfEZr7rzolgQdC6mbrIvLkVtaAYeq7K7sDKZwJrtlsFU0AlOJA7suYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب
: سأعقد اجتماعات اليوم بشأن إيران، والأمور لا تسير على ما يرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91204" target="_blank">📅 00:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇸🇦
الاعلام الايطالي:
إيطاليا نقلت خلال الساعات الماضية بعض طائراتها العسكرية من قاعدة الطائف السعودية بسرية تامة وبسرعة بسبب المخاوف الأمنية من الاستهداف اليمني لقواعد السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91203" target="_blank">📅 00:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🇰🇵
كوريا الديمقراطية الشعبية العظمى تعلن عن اختبار نظام أسلحة قتالية جديد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91202" target="_blank">📅 00:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
🇸🇦
بريطانيا على وشك الاتفاق على تقديم المساعدة للجيش السعودي لمواجهة الحوثيين.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91201" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
استعدادات في إسرائيل لاحتمال التصعيد مع إيران.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91200" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
تدفع الولايات المتحدة أكثر من 30 مليون دولار يومياً مقابل حصارها البحري لمضيق هرمز، مما يُرهق ميزانية البحرية الأمريكية، ويُثقل كاهل البحارة، ويُضعف جاهزية القوات البحرية العالمية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91199" target="_blank">📅 23:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق:
حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60% من عائدات النفط الشهرية بسبب الحرب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91198" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDsRIpiq1ecixa-Q3aBkX_ZZ7a39lYz1OI9_7S6A1YwOejBrqnGGdMiJ0Cle0ViIAcdG1mSRx54a3j6qH0Rys_jKtkwtuJjo5Djcq6F-zsO7h-edWOe67CKHW0HjUBruyAwKjTjQFAiZStjynKLRL-BBJf5w63vmh1zEcLCNa6cVrfwmvinoeCjPZt3KiwLWz-uWoHUTSRsoz3lziUM5FRuWLKOiwpSGErXWt3GhavQPiHEUfyEMnuY_CF-PYmoQcnTREzWiVdvFGPHxXNBMvxdmKpOnuBdntuP-rn4IE0_2pv6I0m3-PRFPSdCONMLxzh_xJbsokqHMmT7fnffCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الناطق الرسمي لكتلة بدر
النيابية:
تحذير للحكومة العراقية وسلطة الطيران المدني من الانصياع للإملاءات الأمريكية وفرض حظر جوي على الطيران المدني الإيراني ومنعه من استخدام الأجواء والمطارات العراقية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91197" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
‏
الجيش البولندي:
بدأ عمليات طيران عسكرية في المجال الجوي البولندي عقب الهجوم الجوي الروسي على أوكرانيا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91196" target="_blank">📅 23:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91195" target="_blank">📅 23:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
المنطاد التجسسي تم مشاهدته مقابل السرية الثالثة مخفر المصطفى الحدودي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91194" target="_blank">📅 22:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a81398ab.mp4?token=ktizWqptJZhsmiVF5DjRFXDGHXYQgFp3qzIBYh6PLYwJxF-ubq-wCnLJhE3et_fh3qoTEwRIs0xcLw3zYVuvKR9SoQp3Z2gOZa6X1EG63XmT4L3hbWAHJ8ravVEhFHCelo62Mweaz-W1WIgGB897UQchdLwysdzD9_cwSPLYT2pvsWMlgutNTlhQhoHajfDrAdJWk4M1egOLgdXpdf3f4-3jDSISZRbJ1vZciQoHZSkEtQ9vhY_dDLsRRWtnvN9XTqIzaY6n_R-Q33gvDpcbTReK66N1crc8k8hWPHtJyYfEdvUe25xfGqhzVlnSsosY8xZhDwQylcy4kw02ZGNlEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a81398ab.mp4?token=ktizWqptJZhsmiVF5DjRFXDGHXYQgFp3qzIBYh6PLYwJxF-ubq-wCnLJhE3et_fh3qoTEwRIs0xcLw3zYVuvKR9SoQp3Z2gOZa6X1EG63XmT4L3hbWAHJ8ravVEhFHCelo62Mweaz-W1WIgGB897UQchdLwysdzD9_cwSPLYT2pvsWMlgutNTlhQhoHajfDrAdJWk4M1egOLgdXpdf3f4-3jDSISZRbJ1vZciQoHZSkEtQ9vhY_dDLsRRWtnvN9XTqIzaY6n_R-Q33gvDpcbTReK66N1crc8k8hWPHtJyYfEdvUe25xfGqhzVlnSsosY8xZhDwQylcy4kw02ZGNlEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91193" target="_blank">📅 22:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
مصدر امني لنايا
...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91192" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
اقترحت إدارة ترامب تخصيص 5 مليارات دولار لإطلاق صندوق استثماري لإعادة بناء مواقع الطاقة في الخليج.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91191" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعلق الدراسة غداً الاثنين في كليات جامعة الملك خالد في أبها وخميس مشيط خوفا من رد فعل اليمن على الاعتدائات السعودية الاخيرة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91190" target="_blank">📅 22:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
سپاه پاسداران انقلاب اسلامی:
دشمن پس از ناکامی در عرصه نظامی، به جنگ‌های ترکیبی، شناختی، اقتصادی و رسانه‌ای روی آورده است؛ اما ملت ایران با اتکا به ظرفیت‌های درونی، اقتصاد مقاومتی و اتحاد مقدس ملی، هر توطئه‌ای را خنثی خواهد کرد
نیروهای مسلح به ویژه پاسداران رشید انقلاب اسلامی در این نبرد همه‌جانبه، دست بر ماشه، آماده پاسخ‌های قاطع و ویرانگر به هر تجاوزی هستند.
@Naya_Press</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91189" target="_blank">📅 21:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يعاود قصف الاحياء المدنية في محافظة تعز اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91188" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇶🇦
الاعلام الاجنبي: ‏
رفضت قطر تقرير مجلة نيويوركر الذي زعم أنها مولت حماس، واصفة الوثائق بأنها "مفبركة". وقالت قطر إن المساعدات المقدمة لغزة تم تسليمها تحت إشراف إسرائيلي، وجادلت بأنه إذا وصلت الأموال إلى حماس، فإن المسؤولية تقع على عاتق إسرائيل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91187" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91186" target="_blank">📅 21:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
🇸🇦
بريطانيا على وشك الاتفاق على تقديم المساعدة للجيش السعودي لمواجهة الحوثيين.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91185" target="_blank">📅 21:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يعاود قصف الاحياء المدنية في محافظة تعز اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91184" target="_blank">📅 21:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار انسحاب قوات الاحتلال الأميركي من العراق باتجاه الأردن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91182" target="_blank">📅 20:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
في تصعيد كبير استهدف العدو السعودي المجرم  محافظات الجوف وتعز وصعدة ومأرب بـ 157 غارةً جويةً وصاروخاً، من خلال طائراته الحربية نوع "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران وجيزان.
ليبلغ إجمالي غارات العدوان منذ بدء التصعيد 917 غارةً وصاروخاً.
هذا العدوان الكبير لن يمر دون رد بإذن الله تعالى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91181" target="_blank">📅 20:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxRNzQQzTOb0ZclblEhnTrb0X0EaxMf9b7pXC9ahsDnbj4cMvozp8zwiEBJuRXPqAspCKFWWpt2YAriRXur-nrkYvBdhESLoubJiWhush3PESiBTUE6gZtQ7ssCIHYaJTsgxPmBEWRxjVlfk8fqvAJ6oe5u3FtWpyrMqPHxM2oy4PrUyVCByiNBRA6MLXOuWWgM5lwfm-5xhYLhbNwc9MBPUAxuF4YP13bkiuo9XCKDNoWm_iqfat0kgWLeu6LPnnIev0kjG2dnsCcDiNV_EqV-lfXdbd_bjCOgxPMsQ_m-FhViRwYhMP1WyQV-RXg9f9Qooknj2TpuI-LnNfRBZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بقائي
:
عندما تغلق إدارة ما أبوابها - حتى في وجه الصحفيين الأمريكيين الذين لا تحبهم - وتمنع المراسلين الأجانب، بمن فيهم الفريق الإعلامي للرئيس الإيراني، الذين تفضل إسكات أصواتهم، فإنها لا تدير الوصول؛ بل تحاول إخفاء الحقيقة وتعزيز حملة التضليل الإعلامي من خلال انتهاك الحق في الوصول إلى المعلومات.
‏أمة كانت تفتخر في يوم من الأيام بإسقاط الستار الحديدي، تجد نفسها الآن تقف خلف أحد أبنائها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91180" target="_blank">📅 20:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اعلام فرنسي يزعم:
‏العراق سيعلق رحلات شركات الطيران الإيرانية الخاضعة للعقوبات الأمريكية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91179" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfTeWftsp9OG1h0a5cqP_2mD7GlKuZUhgiAdnNkXJ7wJGSWbzCB6XGsuFOU9A9-I2cMVjYAx6jUXA5mxtWazIjo7lg68kAV3S95OYrGB2x1wjR4k___m51uiJyR666GGsV2ViSiyEtQW_6l_xzih_mz6TepCXVPukNzGCO00u0fIAQi-axKgv5Pfeyf9kk2ieJ5AALn8etScVmAIufISUwE3RuoNVQT6lwBnAwFTgRKltNEU4uColJRMZSxbFsl7VYuk0tnqW1YFFPtCT1m2vZeKb0DKItLO0dzJ7R6w_GRiVpny7POGFKM6NX75X1pnREAHbTiFSQWCgtF5kUPo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط: 99$ للبرميل
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91178" target="_blank">📅 19:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NckEuWeb-9XAbAqfnEnkZq66hJYvX4lyWSr6ruAXCzCGQWTm9d5IONnjliDjnCiXOUPKAwYGrBMCoRlx3LCVceX-PA0MQWCjcV7GqPsnqrRDDfJaNuXpnuzOlzy2ES9i8TJRR3V_1SWjyeo7sIeBuzqABr7bfOGKiuHuLo07DNyFH4pb1b678ovzHYxpigsiCQ7l70Pb1LKkUApGKLlc5l5sWYi7MjdrfT59HkMZTqxUbO3361Tm7Gs1ImEp4QtJfAnIQmWRMyRl-J4GcxucaokFEy3nmnaFmt0cT1QQZ3I_H7bVOIOoCPnl3C4NEKAImycplLyG_gp--Qi1p-CyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇱
🇺🇸
وزير الخارجية الايراني عباس عراقجي يعلق على مقال في صحيفة "إسرائيل هيوم":
لم يعد اللوبي الإسرائيلي يتردد في إظهار دوره وتأثيره علناً فيما يتعلق بالسياسة الأمريكية تجاه إيران؛ إذ تصرح صحيفة مملوكة لميريام أديلسون -والتي تُعد بمثابة لسان حال هذا اللوبي- صراحةً بأن السياسة الأمريكية يجب أن تُصاغ بحيث تدفع الولايات المتحدة أيضاً ثمناً لأي عمل ينطوي على عدم احترام أو عدوان ضد إسرائيل! حان الوقت لتتحرر واشنطن من هذه القيود.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91177" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExtjnsthFVNnAzlopdEsgb-V6iiGIRXgk4_L1yeP6s3cpAciEDJAhI6hKAjWRLOf-VFeyC61lJWhpG45DC6tmEkSBuVuS6QNBN4En1RHOyCvUKKvDSayThc1lDBW_NBz1mQtr34OSrvAMhpuRTYLsH2Je4m_QE7EdE-47PhuTJVdr3uqnmqK5xRAHZZ5xQXI9_vfeC8mscPqrA9qYkfiw6TCh9HEy1ZkSAo00f4qydbjEIAydEVscOZ1Xlkj6IEYu7qXHgbaa4ugVr7YRvhP_GZezxeumNZ-p1Eg74bP862i4tmAGfGlAilAjVjFEHPPeYlunpYsznmD2n_QijA2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب على منصة "تروث سوشيال":
الولايات المتحدة تعمل على صفقة ضخمة تتعلق بشراء البوتاس من بيلاروسيا. ستكون الأسعار أقل بكثير مما ندفعه حاليًا لكندا، وهو خبر جيد جدًا لمزارعينا ورعاة الماشية. شكرًا لكم على اهتمامكم بهذا الأمر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91176" target="_blank">📅 18:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
🇮🇷
شركة الخطوط الجوية الإسلامية الإيرانية:
رحلات شركة "هما" (اسم قديم لشركة إيران إير) من ثلاث محطات انطلاق: طهران، ومشهد، وإصفهان، إلى مطار النجف، تجري وفقًا للجدول الزمني المحدد.
رحلات شركة "إيران إير" في مسارات طهران - النجف، ومشهد - النجف، وإصفهان - النجف، وكذلك مسارات العودة من النجف إلى هذه المدن الثلاث، مستمرة، ويمكن للركاب الاستفادة من خدمات الشركة الجوية في هذه المسارات وفقًا للجدول الزمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91175" target="_blank">📅 18:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91174" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91173" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">السيد الحوثي:  العدو السعودي عاد إلى التصعيد بقصف مطار صنعاء واتجه إلى التحشيد البري الكبير لإبادة شعبنا وحشد عشرات الآلاف إلى صحراء الجوف والمخا والساحل الغربي والبيضاء وتباهى عملاؤه بأنهم متجهون لاجتياح ما تبقى من بلدنا وأشرف على التحشيدات في كل الجبهات…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91172" target="_blank">📅 17:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">السيد الحوثي: هل يقبل التركي والباكستاني أن يتدخل السعودي في كل سياساته؟ وهل تقبل الدول الخليجية بذلك؟</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91171" target="_blank">📅 17:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">السيد الحوثي:  الكيانات المتعاطفة والمتباكية مع العدو السعودي على منشآته النفطية وردود قواتنا هل ستقبل بالقيود التي وُضِعت على الوارد التجاري لتبقى في دولة أخرى للفحص والتفتيش قطعة قطعة!! هل ستقبل الكيانات المتباكية مع العدو السعودي الإجراءات التي تضيّق الحركة…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91170" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">السيد الحوثي: وفود من العدو السعودي والبريطاني كانوا يذهبون إلى جيبوتي لتشديد الإجراءات بما يزيد من معاناة شعبنا عبر التضييق الاقتصادي.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91169" target="_blank">📅 17:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77280b847c.mp4?token=V51M4hrTpUtu2cGZdqsQsAruYNGKSzGUls_KLi1_MJ3iGjT6US_ZI8D2_-K3XJNZS7JcAI_vyWT_Sg6un0IJEPmZbHpe5ehDLHAhwmZpdSWy0Ghsaz2XNInbkFQtcGzQdHju5qCkk7ojy6-rAUuVYVGES3ZALbY3DWUrFC-g_F44pUcBLpfg2nnzQ8JtIWeUMANM1L_d62QgIREgGMQVqHRF5FuOqzr6eejP8DojE5d2rbsyKJDXLs-1s30F-R0cDzxgEfJTzQXklCEzVYKdjrFEBcI21kLi5kGBcAwjNFkxfOVz79oGTMQRfxmXpeH_40hqAib649FBc6HWmk1Frg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77280b847c.mp4?token=V51M4hrTpUtu2cGZdqsQsAruYNGKSzGUls_KLi1_MJ3iGjT6US_ZI8D2_-K3XJNZS7JcAI_vyWT_Sg6un0IJEPmZbHpe5ehDLHAhwmZpdSWy0Ghsaz2XNInbkFQtcGzQdHju5qCkk7ojy6-rAUuVYVGES3ZALbY3DWUrFC-g_F44pUcBLpfg2nnzQ8JtIWeUMANM1L_d62QgIREgGMQVqHRF5FuOqzr6eejP8DojE5d2rbsyKJDXLs-1s30F-R0cDzxgEfJTzQXklCEzVYKdjrFEBcI21kLi5kGBcAwjNFkxfOVz79oGTMQRfxmXpeH_40hqAib649FBc6HWmk1Frg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91168" target="_blank">📅 17:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91167" target="_blank">📅 17:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">السيد الحوثي: كل الجرائم السعودية التي ارتُكِبت في اليمن قوبلت بالتفرج لغياب المبادئ في التوجهات والسياسات المعتمدة لدى معظم الأنظمة، لو انتظر شعبنا العزيز للأمم المتحدة أو لمجلس الأمن وغيرها من المؤسسات أمام كل تلك الجرائم لما فعلت له أي شيء</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91166" target="_blank">📅 17:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🌟
اكسيوس:
ترامب فكر في شن ضربات على الحوثيين في اليمن خلال عطلة نهاية الأسبوع، قبل أن يقرر عدم القيام بذلك.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91165" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">السيد الحوثي: الموقف العربي والإسلامي من العدوان السعودي على اليمن كان متخاذلا عدا محور الجهاد والمقاومة وبعض أحرار العالم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91164" target="_blank">📅 17:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇾🇪
كلمة للسيد القائد عبدالملك بدرالدين الحوثي عند الرابعة عصر اليوم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91163" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
هجوم إرهابي في مدينة ايرانشهر جنوب شرق إيران؛ إستشهاد أحد عناصر الأمن كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91162" target="_blank">📅 17:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
وكالة رويترز: مكالمة هاتفية جرت بين ترامب ورئيس المرتزقة في اليمن رشاد العليمي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91161" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📰
وكالة رويترز:
مكالمة هاتفية جرت بين ترامب ورئيس المرتزقة في اليمن رشاد العليمي</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91160" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bd78ec90.mp4?token=Ug1-_n6wgt2mP5GprRSrQxQ3_pHWb6XHwYvOtj8skKT9lbWn5j84LGLJWCJ-4E5DMw5s24ngAcwdUQOEKbHe_OMRLNh7aYfSFzI2MFENMVWuy9ozhIDVHhD5cwpqnaHNgA7e3WHWiSiSyIaKXImJbmJjrqRUBp_cLVRBo3RUjmesZmW_TtWsZuHnFy4EtdZbVV9uSfNcPcG5SPIQcaktN2sD4EFon_0TSGb-i2z-6UGI13UEt77fdRmzeinfY-xIMvSCe-AlceqtPFYc8buQtCrgIV9uucqx6bboPFGQhCRBh7RYqjC2xxcFU4bIZqEiRglWJ4mTspUmtlxSXKvrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bd78ec90.mp4?token=Ug1-_n6wgt2mP5GprRSrQxQ3_pHWb6XHwYvOtj8skKT9lbWn5j84LGLJWCJ-4E5DMw5s24ngAcwdUQOEKbHe_OMRLNh7aYfSFzI2MFENMVWuy9ozhIDVHhD5cwpqnaHNgA7e3WHWiSiSyIaKXImJbmJjrqRUBp_cLVRBo3RUjmesZmW_TtWsZuHnFy4EtdZbVV9uSfNcPcG5SPIQcaktN2sD4EFon_0TSGb-i2z-6UGI13UEt77fdRmzeinfY-xIMvSCe-AlceqtPFYc8buQtCrgIV9uucqx6bboPFGQhCRBh7RYqjC2xxcFU4bIZqEiRglWJ4mTspUmtlxSXKvrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية ينشر  مشاهد لاعتراض وتدمير طائرة مسيرة من طراز MQ-1 تابعة للجيش الأمريكي صباح اليوم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91159" target="_blank">📅 16:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
🇾🇪
التلفزيون اليمني:
- الوفد الوطني التقى المبعوث الأممي ووضعه أمام موقف اليمن من العدوان السعودي
- الوفد وضح للمبعوث الأممي بأن العدو السعودي رفض إنهاء الحصار على المطارات والموانئ اليمنية، وإزالة القيود الاقتصادية والإنسانية وصرف المرتبات
- الوفد الوطني وضّح أن تلك الحقوق هي مطالب الشعب اليمني اليوم أمام الأمم المتحدة وأمام كل من يريد أن يعرف خلفية التصعيد الحالي
- الوفد الوطني أبدى للمبعوث الأممي أن الجانب السعودي يتحمل كافة التبعات نتيجة عرقلته ورفضه الحلول الإنسانية.
- تم التأكيد على أن السلام هو مطلب الشعب اليمني والمجال مفتوح للحل من خلال المطالب الانسانية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91158" target="_blank">📅 16:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جيش العدو: نجري حاليًا مراجعة التفاصيل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91157" target="_blank">📅 16:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تفعيل الدفاعات في شمال الكيان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91156" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صافرات الإنذار في المالكية بالجليل الأعلى</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91155" target="_blank">📅 15:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صافرات الإنذار في المالكية بالجليل الأعلى</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91154" target="_blank">📅 15:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏ترامب: يجب إنهاء هذه الحرب السخيفة التي لا تنتهي مع أوكرانيا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91153" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارة الخارجية اليمنية تعلق على اقتحام المسجد الاقصى: ندعو المتشدقين بالدفاع عن المقدسات لاتخاذ مواقف عملية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91152" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v05pF9HS1jhUkqY-WIo5rKmlz2nG7uKe7hutgYepwI4L7BGaqlTNdumC7TmzhPqI-eejY16sQ-OSWtNVC5fvun-AmxlvfSoB6ayVTSgaRAVdSdrsdiyFlV-wgZAiPQBY6B9PtEjps7-YV4bBSZc9movkwI3UMABEGjhlpanTMQakYWHnkjqabPqhsqvWC-HJ5oslrGoCsRFzZnv7v3NRata8S-RpPQ6wV4rn76npWu4xnJg-IZoMOtioHnCMlHw_owj8OKlikWW-pQZwMQz3nPkjtlXxMLwPvDe7A7Lu6YRxyx7fkwa6pXFQ-yaXLapoIR9vEbOMJghArAp-dwvxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حق شهداء المقاومة ومجاهديها وجماهيرها أن يفخروا؛ فالمواقف تُختبر عند المفترقات الكبرى. وفي مباحثات تنظيم السلاح وترسيخ السيادة الوطنية، لم تطرح قوى المقاومة أي مطلب شخصي أو سياسي، ولم تقدّم أيَّ مصلحةٍ على مصلحة العراق.
إنما هاجسها الأساس هو سيادة العراق وقراره الوطني واستقلاله، ورفض الوصاية والتدخل الخارجي؛ وهي مبادئ تستحق التضحيات وتتقدم على كل الاعتبارات.
حقًا هي "مقاومة.. حتى يكون العراق سيد نفسه".</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91151" target="_blank">📅 15:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA8dRzeP31InrREIj5mYV4cetbaIMRQU8NEPvk5jmbXFzyehRRYI9hUIi75HC6rfgxt2LyaqPD_WEsdlUYDffqWIJIFRFxos7v2DuL38mruHzK-PMiYZwM17UOHYWYu5TaRlW1xBaFPO4VhdEBN_ZpyLDbilDkLo5MMK1rGLWn-i_WRIURX_Y_msrRsftsP4SJ6E3ao6mI9fp8i5M6Kfm_jI7FRb_GAHnl4QDNwXiVS9Y9JPLzR4FKa5iYjikNu9gszk2cxAbDCKbKLCxrdV6mh4zX8penMT97O4MQeGsenFywJL6h2pgjuJaTL939GyYPpC4piBE11kSqLZsPwt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل 5 جنود سعوديين من القوات البرية السعودية بضربة مسيّرة استهدفت آليتهم في نجران بينهم قائد الآلية خالد حسن الشهري، وعبدالله السلمي، وخالد السلمي، وإبراهيم المرزوق، وجابر الرزاق.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91150" target="_blank">📅 15:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8QMxVrxESm6FBoFlQ9582xqEpU5-jREUo3rBTKXhK-7J-ZIfvDvQ2U6yRnR3bEUnsSGz6sEBuOi79eh6OmC4ZJaqV0ed7MV-xa3r-AGnVGV0h4tcjrLmM9wyNxF36wH-NqlwGdYyp0J5cWqocxxx8zOshE9XsULDC_uohExaZC9cRSu61bNNaoasqCUf7nzFLbHNtFPtSU9SWu2yWY6xSVunBnbj9rKCkWlLwL03MSE6R2nlbbDo9N6TOIbLOwCRRYSr2MtMWNrd6g9vr8D1TJs9OtvNDAnvsk4df6ER1rD6dJLsXQNznk4LgpukJAPbFIFMZQ62O_JiIEWNguBnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرع عدد من الجنود السعوديين بعد استهدافهم من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91149" target="_blank">📅 14:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مصرع عدد من الجنود السعوديين بعد استهدافهم من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91148" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
مسرور البرزاني امام مدير مكتب القائد العام للقوات المسلحة العراقية: في عام 2014، وبتوجيه مباشر من الرئيس بارزاني، توجهت قوات البيشمركة إلى مدينة كوباني للدفاع عنها، مسجلةً بذلك صفحة مشرقة في تاريخ الدفاع عن شعب كردستان.
تصريح لن ينتقده نواشيط اربيل ويقولون شدخلنا بكوباني كما ينتقدون السلاح الشيعي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91147" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامب يغرد على خلفية حظر دخول مراسلي مجموعة الصحف الاميركية الى البيت الابيض.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91146" target="_blank">📅 14:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">المتحدث باسم رئاسة إقليم كردستان: قوات التحالف الدولي لن تبقى بعد يوم 30 أيلول الحالي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91145" target="_blank">📅 14:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
بلغ استهداف العدو السعودي للقرى بمديرية الظاهر وأجزاء من مديرية حيدان أكثر من 135 صاروخا وقذيفة خلال 12 ساعة وما زال متواصلا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91144" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فاينانشال تايمز:
ترامب يضغط على زيلينسكي لوقف استهداف مصافي النفط الروسية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91143" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار يهز مدينة منبج في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91142" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار يهز مدينة منبج في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91141" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE-Wt-xN5LBjaSg4gKWVhM2L0KYhXquMvBE8m0rFtar6juBabc5w-Y1vvJ9rQUU7NGbf-7GjiBauv7hJneNCs1f2bty2sShF1Q8idehvvJ2sflvwu5XrALMzeVvBeBnWpboGgeJbrOfk0FFK_k1DSZq5OIVUv5lClryVXd9y_p5hFaf6GVt16dJI4f13plLl8XQGlcKXujsZA3ZgrB89IT-uoN5chZxxG1S7hOfmd--EkLbl592dfZvYtogLWBGWFaORXT79buFcOAksRfZAaSbrF9njlgiPEE8yDUTn0KJAiJj9l0l3nJa4nq3_61b2yUP_xeLL8sVJebjEmsuwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمليات التجارة البحرية البريطانية: ناقلة نفط كانت تعبر المضيق قد أصيبت بمقذوف مجهول. وأصيب اثنان من أفراد الطاقم بإصابات طفيفة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91140" target="_blank">📅 13:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91139" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbsNr2MdhXUe6zdPsSskhQP6n-5X_zSUxqVYIu1bDDRODD4Yi4w1y7-SK6vmkcPuqQJSAUmkkhktgwKn5--5NipjwbXhi1nUuLfhi1Zjvkdir7ov6WyK4yow22i686VwZMu5WJu4eQmiVohH2usIRmNBcih-8BGho5nbX5Axz8wOIi9qkrgLA8n_--NWv-G_YxUuFZidq_l6j2SaEy9tAapUH4KQR2fWXLiE7A9DK0b7H4-J3i8uZQlZwECWzkLLI1k8bpnKY7nsG5h_baQsFpouBmpqsAMS0XeCnq-UAnQo6kSAMty7IZJBMLRC7RJdo0ZigeDZt1fzjYTWqaxmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91138" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
الحكومة الأفغانية: ندين الغارات الباكستانية على أراضينا وسنرد في المكان والزمان المناسبين.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91137" target="_blank">📅 12:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
🇾🇪
كلمة للسيد القائد عبدالملك بدرالدين الحوثي عند الرابعة عصر اليوم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91136" target="_blank">📅 12:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇾
إنفجارات جديدة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91135" target="_blank">📅 10:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجار ضخم أخر في مستودع للذخيرة يشعل سماء ريف حلب الجنوبي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91134" target="_blank">📅 10:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
الحكومة الأفغانية:
ندين الغارات الباكستانية على أراضينا وسنرد في المكان والزمان المناسبين.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/91133" target="_blank">📅 08:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
الحرس الثوري:
إذا حدث هجوم جديد، فبالتأكيد ستحدث تغييرات كبيرة في دفاعنا وهجومنا المضاد.
هذه التغييرات ستشمل تغييرًا في جغرافيا الحرب، وتغييرًا في الأسلحة والمعدات الحربية؛ سنُدخل أسلحة جديدة بقدرات جديدة إلى ساحة المعركة، وسيتفاجأ العالم.
أهدافنا أيضًا لم تعد بالضرورة تلك الأهداف السابقة. لدينا أهداف جديدة لم تتعرض للهجوم بعد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91132" target="_blank">📅 08:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من إسقاط وتدمير مسيرة أمريكية من طراز MQ1 في أجواء مضيق هرمز جنوبي إيران.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91131" target="_blank">📅 07:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
اللواء السابع بالحشد الشعبي يشتبك مع مفرزة جوالة لعصابات داعش الارهابية في حوض الثرثار ؛ العملية أدت العثور على زورق وأسلحة ؛ المنطقة شهدت قبل ايام عملية استهداف لأبراج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/91130" target="_blank">📅 04:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🇺🇸
صحيفة وول ستريت جورنال :
إدارة ترامب تستعد لفرض عقوبات واسعة النطاق على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/91129" target="_blank">📅 04:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
🇺🇸
من المقرر أن يلتقي وزير الخارجية الأمريكي روبيو برئيس الوزراء العراقي في الساعة 4:30 مساءً بتوقيت الساحل الشرقي، كما سيلتقي بنظيريه الياباني والكوري الجنوبي في الساعة 11:15 صباحاً بتوقيت الساحل الشرقي</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91128" target="_blank">📅 03:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارات في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91127" target="_blank">📅 02:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
أسعار النفط العالمية تلامس 104 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91126" target="_blank">📅 02:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=gAUu2bGN_wPV4W2CtG5q78oSjioamUd5PC30x6XEAxgLkUVE2sJpX83v3K_kWQVogrXVp7s7Y8FdLGHjV7WkL4uA0ScH5BtExYj3qKDsBt_Z609KMkltAYAUjlDL4RGRA68PIfqOQKckVcwuVTEddxZmeWEepGxQKAVL_vsqLv6nta2yzFfshC7d2OOr2ZwhPRd3leFkPuG2Ubn0DlMagjaa62Uc1wku_6nrWfESiNgeL-LLV9kVMApoDyeW4uqz87pSnFUH3JyALY-Q_7mEMC4_u10idJ238QzLJL9Xbh7MCLLoLlFRwCEZPKrztCS5MIOpqDTTGPvTIvuaQOrEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=gAUu2bGN_wPV4W2CtG5q78oSjioamUd5PC30x6XEAxgLkUVE2sJpX83v3K_kWQVogrXVp7s7Y8FdLGHjV7WkL4uA0ScH5BtExYj3qKDsBt_Z609KMkltAYAUjlDL4RGRA68PIfqOQKckVcwuVTEddxZmeWEepGxQKAVL_vsqLv6nta2yzFfshC7d2OOr2ZwhPRd3leFkPuG2Ubn0DlMagjaa62Uc1wku_6nrWfESiNgeL-LLV9kVMApoDyeW4uqz87pSnFUH3JyALY-Q_7mEMC4_u10idJ238QzLJL9Xbh7MCLLoLlFRwCEZPKrztCS5MIOpqDTTGPvTIvuaQOrEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم جديد يهز ريف حلب السوري</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/91125" target="_blank">📅 02:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RzUqldZDU85cyHFxsU2QbaGuR2F16Ra1oBbRH_q7zZ4WnuxPAN1w1gO2BqnfByQg1wvoPJUai7Qf5uCNqUdpMzW82BB-q4Is8fMvZGlklcvr8MMP6Z5YdG6tK6owg55iHnOjLigrI49rRbNs20TItP6MaZfZiolQvrvm69U2I1577zTrlql940BQwbcPjh-Q3Rpru4ntGl2KaHtpvzhg5Zztm8duvAeY2BNyo00gU3z3AYmvFBW-G6zfWH5WcKg-NWnaGXPwN59zNQ2WusxzmDwoE9nOvI3B42pHW4fwIoz440JXDpu8ZqyxoVYSkoIHdSVthuM2b3yXhOs6duLa1Rd5yalyt-ov2tobOZkf8H5_w2U-OroCsLUCfyeO1TS__hxEhalgtGsgx8lJQ-Nd97KyYIeIq1nMrExXeHCTv7exabm26hUMAkPPzixjorbqIIRUWpuBjGBMEityEG5tPJ12fsnsK-JCxCntdcoQo8LYE-gOkO7mgI5UqIoFKUPCvtV3mqtWL0tbWExMS0T8YoCbFYp_pl1fjI6BJ-1h7-VqFVwJ0UOcLeMiCEu01RXt7liEiH1SWZ22bhdV1v3BiG5Qd71OuRpx4_qkStIdNrWnfr_3vUkMA7vqY7m3V6Xl_FYuE515BXTP5SV-CNwSDdHcg-YySLNetKxrXsXs76E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RzUqldZDU85cyHFxsU2QbaGuR2F16Ra1oBbRH_q7zZ4WnuxPAN1w1gO2BqnfByQg1wvoPJUai7Qf5uCNqUdpMzW82BB-q4Is8fMvZGlklcvr8MMP6Z5YdG6tK6owg55iHnOjLigrI49rRbNs20TItP6MaZfZiolQvrvm69U2I1577zTrlql940BQwbcPjh-Q3Rpru4ntGl2KaHtpvzhg5Zztm8duvAeY2BNyo00gU3z3AYmvFBW-G6zfWH5WcKg-NWnaGXPwN59zNQ2WusxzmDwoE9nOvI3B42pHW4fwIoz440JXDpu8ZqyxoVYSkoIHdSVthuM2b3yXhOs6duLa1Rd5yalyt-ov2tobOZkf8H5_w2U-OroCsLUCfyeO1TS__hxEhalgtGsgx8lJQ-Nd97KyYIeIq1nMrExXeHCTv7exabm26hUMAkPPzixjorbqIIRUWpuBjGBMEityEG5tPJ12fsnsK-JCxCntdcoQo8LYE-gOkO7mgI5UqIoFKUPCvtV3mqtWL0tbWExMS0T8YoCbFYp_pl1fjI6BJ-1h7-VqFVwJ0UOcLeMiCEu01RXt7liEiH1SWZ22bhdV1v3BiG5Qd71OuRpx4_qkStIdNrWnfr_3vUkMA7vqY7m3V6Xl_FYuE515BXTP5SV-CNwSDdHcg-YySLNetKxrXsXs76E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91124" target="_blank">📅 02:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da96c42899.mp4?token=nP2g7C3iSBzPXjPkSHmQH_LUX45dw5iEJE7X9AZp1cXqYsdT5A7ICyBh8AEMkfmfDHr9vn2cHhF9A53VJZlUB0Mdl9RQ6yRedyBHwX_8LlvN7hstNKER167RUSJZeeDJ48HkeHdqw-mvQxSeVrYCXd5Uzd_aGB8plzrpbBTLBjJj2E1tH17l1I0dYpJEX-NTJD5GtlxZC55r5ul66BEdRIWbuMFwnEzdjSo0ZzWb_qUd84CsQoDc5C3IdYzaA0Tg1Q9-PN39XuAmyP54qmNLycJUV0y4lNO_3o4sTqPwDxYBulB3edpcjxQMvQoAiyAJtGZdfpou4-HZhHYUjSvPSWy_qAgdBHFBQ8RkYWg1P7Sp7-UB4HAXPnwKb5Zy3m4ldOoQXqTQASrClzZZ_AQjmddOKLIP9cIIewwVfahHdMjmh7m2v9tYDu-n2dho6i17gRZBdf6GKUe7zdIKkZn00TKQ6uX7wNy6vsO2g0GPPtMIG6XQH9TxSAkhRKt8tNDuHaR38CoX8WO_9jeehKvBskjyTwwAAdNQSlTYKIw8bl-dqo8tGYRabDDbCMqkvB6gWmyS2RV96gyjv3idH7Jz5f5Rknsq9dUQkmVQKtaYM1AcBiEfgp37JlEZeceUqfvcKyrWvwAoTQTAmzHlby_WG0xIioCnmzwIcam27dOga4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da96c42899.mp4?token=nP2g7C3iSBzPXjPkSHmQH_LUX45dw5iEJE7X9AZp1cXqYsdT5A7ICyBh8AEMkfmfDHr9vn2cHhF9A53VJZlUB0Mdl9RQ6yRedyBHwX_8LlvN7hstNKER167RUSJZeeDJ48HkeHdqw-mvQxSeVrYCXd5Uzd_aGB8plzrpbBTLBjJj2E1tH17l1I0dYpJEX-NTJD5GtlxZC55r5ul66BEdRIWbuMFwnEzdjSo0ZzWb_qUd84CsQoDc5C3IdYzaA0Tg1Q9-PN39XuAmyP54qmNLycJUV0y4lNO_3o4sTqPwDxYBulB3edpcjxQMvQoAiyAJtGZdfpou4-HZhHYUjSvPSWy_qAgdBHFBQ8RkYWg1P7Sp7-UB4HAXPnwKb5Zy3m4ldOoQXqTQASrClzZZ_AQjmddOKLIP9cIIewwVfahHdMjmh7m2v9tYDu-n2dho6i17gRZBdf6GKUe7zdIKkZn00TKQ6uX7wNy6vsO2g0GPPtMIG6XQH9TxSAkhRKt8tNDuHaR38CoX8WO_9jeehKvBskjyTwwAAdNQSlTYKIw8bl-dqo8tGYRabDDbCMqkvB6gWmyS2RV96gyjv3idH7Jz5f5Rknsq9dUQkmVQKtaYM1AcBiEfgp37JlEZeceUqfvcKyrWvwAoTQTAmzHlby_WG0xIioCnmzwIcam27dOga4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91123" target="_blank">📅 02:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde2971876.mp4?token=IPUengSxNOOmapcIH8tRvdEnodXi3ix_qQvpNViPuG73gLuKTzJoPRiCRBwhDtOBbIj6rlZ_d7R0_6as0S9tYxBBexWbrYvOgpshJIey95nqOyoiJz0tBMJ3bidGHjESSbUqh0j0aoxDWXt1pNEcAwjZJKE9MAMFpwZW--qt8lLb9_ny0KQgOjQk6JEpKkrxYO2ifIdQADpLUIFPqSp8QYloKszFocjUETND8Gb3zaAdhBbD_u-7D9laGjhYb3FXVYBnCOAJKD23e9tSKPJEFiBcaX11wIhJL_L3AkaugaeyUkEFrK_RgJGoUt_tzcL77QpzdDTtnx6pEYDJaUlMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde2971876.mp4?token=IPUengSxNOOmapcIH8tRvdEnodXi3ix_qQvpNViPuG73gLuKTzJoPRiCRBwhDtOBbIj6rlZ_d7R0_6as0S9tYxBBexWbrYvOgpshJIey95nqOyoiJz0tBMJ3bidGHjESSbUqh0j0aoxDWXt1pNEcAwjZJKE9MAMFpwZW--qt8lLb9_ny0KQgOjQk6JEpKkrxYO2ifIdQADpLUIFPqSp8QYloKszFocjUETND8Gb3zaAdhBbD_u-7D9laGjhYb3FXVYBnCOAJKD23e9tSKPJEFiBcaX11wIhJL_L3AkaugaeyUkEFrK_RgJGoUt_tzcL77QpzdDTtnx6pEYDJaUlMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة جدا تهز بلدة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91121" target="_blank">📅 02:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=pFSlKMKLDNznzzxl565DJy1LyK1HsLgmqKJSRIp66rag-NVjGEbMw8dIiUGx91QLpQTf228GgHJZRDv3w2Z6Kp9CRDFKb_pKZoM-R-Ad2mUhU_OQsqGOgcR2m_tlAhfGmQg7Hvfqv1-FFzo4-QC9KxT8pW4x_iHLNNsxF9_VXXYSO_qNmtrYLOf9_j9xV8I20tba1yuU7Vmj7GwwZqP3OirwXHyPVTHKWoWOdSzOhHENB4JY6hyRYDP3yXc5NYnF37AbZyGnN0xUsJ8O_YY-HdrWoWzSnqXeX4YKY_Iy2qF15jJWUWizojrwUy7kBoCySvJeXho4e6oQE_qyyRKlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=pFSlKMKLDNznzzxl565DJy1LyK1HsLgmqKJSRIp66rag-NVjGEbMw8dIiUGx91QLpQTf228GgHJZRDv3w2Z6Kp9CRDFKb_pKZoM-R-Ad2mUhU_OQsqGOgcR2m_tlAhfGmQg7Hvfqv1-FFzo4-QC9KxT8pW4x_iHLNNsxF9_VXXYSO_qNmtrYLOf9_j9xV8I20tba1yuU7Vmj7GwwZqP3OirwXHyPVTHKWoWOdSzOhHENB4JY6hyRYDP3yXc5NYnF37AbZyGnN0xUsJ8O_YY-HdrWoWzSnqXeX4YKY_Iy2qF15jJWUWizojrwUy7kBoCySvJeXho4e6oQE_qyyRKlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تساقط الصواريخ على المناطق السكنية القريبة من موقع الإنفجار في منطقة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91120" target="_blank">📅 02:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=Ik9bHK1jGet7kNUhNP8XQX7VBvByRkrAfAzG5uEagYSHKefWa6s2E14gXiY0AP8M3x-1dfWWeMHdQflr-ySayZZ1iIB-VxMb1fOZD_j_go2JYlcbUJsR4p7yAEC8_h9Lj6QoL55qoeHRhQdk36ZYgRfpPZiBuqFLgef7Dcuh_uXiP_h96eW2g1CGYrJb1CiPjKN4-do3KxQ7IlBY_RttBR_UOE4POIPw6xOHTRj11knqfWsqDf4uepFZyCuHHGnBWpfEPRijCQxr51JvBIXcKPtAdUrM9TdUfyftwzpFWLHlGCwbIc2OL5MsSO2XA14PfoU1fZv82RLbfxl29o7RPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=Ik9bHK1jGet7kNUhNP8XQX7VBvByRkrAfAzG5uEagYSHKefWa6s2E14gXiY0AP8M3x-1dfWWeMHdQflr-ySayZZ1iIB-VxMb1fOZD_j_go2JYlcbUJsR4p7yAEC8_h9Lj6QoL55qoeHRhQdk36ZYgRfpPZiBuqFLgef7Dcuh_uXiP_h96eW2g1CGYrJb1CiPjKN4-do3KxQ7IlBY_RttBR_UOE4POIPw6xOHTRj11knqfWsqDf4uepFZyCuHHGnBWpfEPRijCQxr51JvBIXcKPtAdUrM9TdUfyftwzpFWLHlGCwbIc2OL5MsSO2XA14PfoU1fZv82RLbfxl29o7RPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر حجم الإنفجارات وتطاير الشظايا جراء انفجار داخل مستودع للذخيرة في بلدة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91119" target="_blank">📅 02:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=pQF4nVTGwQoXUdVNS0Gv10lSJFbjM0eZ4bVkPjvSu9i-FAEhbYzFaj8zP7C1R_hJkuiGuKxJmEVcfiuUD1RB3p9ZG5fOWwfrmwBuWDRES5bQOiahQqCR7YLenlBk6F-LUtC5gTG0LVImW9w6Q8oynVah70A__EriwbO2tuD120wPowedpp8fnUV5lYczR7PYerSlVkMbrCpVM1KyDxA1w48YV1-xxC1UTjRSeTcRx9bZAE_fqSTcRkauXCKLQqlyivr94oNo_eLVqJrPMwhjSGkM2o78iiQY_wCxBRmVlAHoXRNn14VguGHL327C519OEnuBow_cI02kbQrXDvCFEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=pQF4nVTGwQoXUdVNS0Gv10lSJFbjM0eZ4bVkPjvSu9i-FAEhbYzFaj8zP7C1R_hJkuiGuKxJmEVcfiuUD1RB3p9ZG5fOWwfrmwBuWDRES5bQOiahQqCR7YLenlBk6F-LUtC5gTG0LVImW9w6Q8oynVah70A__EriwbO2tuD120wPowedpp8fnUV5lYczR7PYerSlVkMbrCpVM1KyDxA1w48YV1-xxC1UTjRSeTcRx9bZAE_fqSTcRkauXCKLQqlyivr94oNo_eLVqJrPMwhjSGkM2o78iiQY_wCxBRmVlAHoXRNn14VguGHL327C519OEnuBow_cI02kbQrXDvCFEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91118" target="_blank">📅 02:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=rvol0x1BnY5Xm5gB_lj8PxU3BnTdFvosFP8d7HMrgIu8D9FSLrL0QqpV-jN5iz3hpL4hmQgYcCSbpEgzm1xaob0HZVDqWymWiDSyqrmQlapUhR86VYbyUSXr1mNu9SBo7EGvip9UEMHjgK-KOBI1ekMU6jP4jMPxhbDHz0obZVVZMt2GSEwMc506eJIsRp-DWeMs5mYj2LR3OPOcs7fIZRMO-wrOZaC7B6q8zrLTkiqxkKJxnNufmkVpNPui5GZHCRGTycOWjm_sPf5dNEE-lK6LfOs3bgaoVYb3J3d_jIO2XmR3dLSP7nCZUcQ7kP-WIGgkY6SArvE_-M7WkK4wkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=rvol0x1BnY5Xm5gB_lj8PxU3BnTdFvosFP8d7HMrgIu8D9FSLrL0QqpV-jN5iz3hpL4hmQgYcCSbpEgzm1xaob0HZVDqWymWiDSyqrmQlapUhR86VYbyUSXr1mNu9SBo7EGvip9UEMHjgK-KOBI1ekMU6jP4jMPxhbDHz0obZVVZMt2GSEwMc506eJIsRp-DWeMs5mYj2LR3OPOcs7fIZRMO-wrOZaC7B6q8zrLTkiqxkKJxnNufmkVpNPui5GZHCRGTycOWjm_sPf5dNEE-lK6LfOs3bgaoVYb3J3d_jIO2XmR3dLSP7nCZUcQ7kP-WIGgkY6SArvE_-M7WkK4wkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91117" target="_blank">📅 01:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=HUvkZSS1GJcVIu2Tm67Jk80FPG5p3b1eIh9GBKjFJWjtCKbUcQai17R90YCT9WGdO-z2Eiibc4HSCqBqKcKBBTyenGiU6aEGi37GRlD8uCFyK4VZGYLzde-VJcLcVv5uVgZywPXxr4QdFbyvG2AT8ZH-GrdKmSZPNzmk-zL-ltg1k-FBjQ7gtTaX2WmdfzfAWTMkpwTLbIibCEmYk058gTN0oAeXcCiPaDJJusbmDa2huxJCdSKcry894Zb0bKO4yVCBi-TpbnVkb3uFgTv16L5K4ISQED-Wc8Ptzh_Vjr0OpQiaW7EkoptZJzenAvBUa5TZZ8Mx9hIl7ekJAV7xJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=HUvkZSS1GJcVIu2Tm67Jk80FPG5p3b1eIh9GBKjFJWjtCKbUcQai17R90YCT9WGdO-z2Eiibc4HSCqBqKcKBBTyenGiU6aEGi37GRlD8uCFyK4VZGYLzde-VJcLcVv5uVgZywPXxr4QdFbyvG2AT8ZH-GrdKmSZPNzmk-zL-ltg1k-FBjQ7gtTaX2WmdfzfAWTMkpwTLbIibCEmYk058gTN0oAeXcCiPaDJJusbmDa2huxJCdSKcry894Zb0bKO4yVCBi-TpbnVkb3uFgTv16L5K4ISQED-Wc8Ptzh_Vjr0OpQiaW7EkoptZJzenAvBUa5TZZ8Mx9hIl7ekJAV7xJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من نقطة قريبة للإنفجار الذي طال مستودع الذخيرة في ريف حلب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91115" target="_blank">📅 01:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
🇮🇷
الولايات المتحدة الأمريكية تصدر تنبيهاً أمنياً يحذر جميع مواطنيها من السفر إلى إيران "لأي سبب من الأسباب" ومغادرة البلاد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91114" target="_blank">📅 01:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=Uwu-ThwjpfrXE0KughKZDlFMPpF_uoFBlJESmhCYMO12Uh5_ENrBMHwnCLp0mWTgLqYr2eEdLLlnbin7JGs58VgHS3Aytt3KKLDlYPcLh-aypzodmnUTEVET5A8Od6OBlcSvcn_12TCTQUzVFFEpZ1Kzi31dWYcP80kprbK0MtSZMyEl1LuBcXaO9Z09DjQgwZ46ykhgBsKVucxtnh3siykmM5XQO_dOX4cPF4NdvLMqBnwueM0lOfjwkBHpCI7jqDC4HiuB8zO5eu9bNy-5fM-p1tOgpHptK7FfrjHjDNYZVVMsGa-FdhGXoDVIjeJ0sLHYJZU0Xql8zOMrpQ0cXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=Uwu-ThwjpfrXE0KughKZDlFMPpF_uoFBlJESmhCYMO12Uh5_ENrBMHwnCLp0mWTgLqYr2eEdLLlnbin7JGs58VgHS3Aytt3KKLDlYPcLh-aypzodmnUTEVET5A8Od6OBlcSvcn_12TCTQUzVFFEpZ1Kzi31dWYcP80kprbK0MtSZMyEl1LuBcXaO9Z09DjQgwZ46ykhgBsKVucxtnh3siykmM5XQO_dOX4cPF4NdvLMqBnwueM0lOfjwkBHpCI7jqDC4HiuB8zO5eu9bNy-5fM-p1tOgpHptK7FfrjHjDNYZVVMsGa-FdhGXoDVIjeJ0sLHYJZU0Xql8zOMrpQ0cXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات كبيرة جدا تهز منطقة العيس في ريف محافظة حلب السورية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91113" target="_blank">📅 01:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=sAMZ07xdjY8EiE7tMZPB6UiMy1zLu33LBsyB8rMJXHpLgHEmZSGPM_3D2QaHm0xcwX68VmWxBzlSlcms4ZDgBwysUZ8Un-04t8L2ppZoTWgTCQ0cYJLMV9J6ZClfuhosu0aO2_wclkUo3lCVFV4qaMjTxL1B0vDpsY0qEN3r4YvHdzQ8-r0p6Sibx4iKlN1ho1vGhhISXUiXaTrY_q5OrMmOa9x_d7cS0qD04mnbUKlJLHnDDiyR402NPRP7UhlbSlCLlJPizKUEPkSDYWJg4aIg3rhrTrOC5nnkRYSmMh7ajzVDfL9gQfi437UN5DVCGZgYFXWKNfQAGtJa-m8VOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=sAMZ07xdjY8EiE7tMZPB6UiMy1zLu33LBsyB8rMJXHpLgHEmZSGPM_3D2QaHm0xcwX68VmWxBzlSlcms4ZDgBwysUZ8Un-04t8L2ppZoTWgTCQ0cYJLMV9J6ZClfuhosu0aO2_wclkUo3lCVFV4qaMjTxL1B0vDpsY0qEN3r4YvHdzQ8-r0p6Sibx4iKlN1ho1vGhhISXUiXaTrY_q5OrMmOa9x_d7cS0qD04mnbUKlJLHnDDiyR402NPRP7UhlbSlCLlJPizKUEPkSDYWJg4aIg3rhrTrOC5nnkRYSmMh7ajzVDfL9gQfi437UN5DVCGZgYFXWKNfQAGtJa-m8VOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تطاير الشظايا من داخل مستودع للذخير بعد حصول إنفجار كبير بداخله.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91112" target="_blank">📅 01:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=feIG_mOIUPiuTulurRRor2EE1_9fqCwtrOp383RRHRmZpMABh5keg_bdGtRWpkn0bBIOOPfqvWqZ_CevdUv9-nDLMaO2eBbmQpqS7WqW9Vqola4EWS7h699gQL5VOVW-_4keehpQwiVLkPZC5w751IE7wNtjt4_oxcbLtNIu6hd4JQiqnl-CRAVdQZA84eNTDv8x7T7EvDeVoSHy5DD8Y6jMXtenOPA8G-j-A8fXfMkoN5UHEIe7ktzq0Ua1AzVyXt9h1G5VKIDR2lxm46IPFJS1697n--o5Bc42_m6BJWhKeiwc2Dqo2XaM3GtoWSUB0fBl2LPoAqRk5BxCo8YrFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=feIG_mOIUPiuTulurRRor2EE1_9fqCwtrOp383RRHRmZpMABh5keg_bdGtRWpkn0bBIOOPfqvWqZ_CevdUv9-nDLMaO2eBbmQpqS7WqW9Vqola4EWS7h699gQL5VOVW-_4keehpQwiVLkPZC5w751IE7wNtjt4_oxcbLtNIu6hd4JQiqnl-CRAVdQZA84eNTDv8x7T7EvDeVoSHy5DD8Y6jMXtenOPA8G-j-A8fXfMkoN5UHEIe7ktzq0Ua1AzVyXt9h1G5VKIDR2lxm46IPFJS1697n--o5Bc42_m6BJWhKeiwc2Dqo2XaM3GtoWSUB0fBl2LPoAqRk5BxCo8YrFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مستودع للذخيرة بريف محافظة حلب</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91111" target="_blank">📅 01:39 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
