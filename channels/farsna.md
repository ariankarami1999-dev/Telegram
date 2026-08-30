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
<img src="https://cdn4.telesco.pe/file/DSDJzEdDq7NjvIDWDNOAuDsPTeZKzsa57xijsaO6jKbsnylZXUjhp0VrgEHlz3I515TRpb-qDBNb6-wfPrXOIpM1GE-vixDvuLDAqgLb-hXk0dwPX_vORQ2NY_1w7IJsbPzF7PiBJvdf5qeJ5Hl-wfIP1IyTZTJpELFi2JyZQ3yCcJZXfW5KjycseiySCUPr8Y-ze_Ar-UCk42_kh8ClffAYplhDJmZysUH7rOj13Gz5UAKomzwcjahH-Zf1zJEFBalkKYcwJ5nXARyR3mYQc2STdV99tm1xnmyAimEbtgNhEZainSRJM-iqEyyketx3uHUhgJ8q1xBot3xi4LENeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-459057">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boc97_-bjawSrn_ReB_vwhf1rSJ5H7w9Xzxfe6S1K1IIsa690PMDWA_F8RE5sX0Aavm14py1_Op29WnCGFEtIOkWlCAyM4HOEaOpCTxV0oHXslNzTRD37pwo2g51dfOGrELbiqYfSMrjIZ82CoqpFp0DfqkU00AKixxH8SZdheBmWhcDvHsyUtXFQg_LevkSaSo8AC_gbQBYY6ZP25Lh3FTeC2SFRyU9FhnpyHGy3m1Y0lYfo7IbCHEymO5n5vqd-G3RDjjwaAlW2K5_FWD_Iq4eNVMipwh5ngYFFccE_ZB5UlGJ1w897kk29yalNZTUnfAx2B6eAJc3bWSsRNtaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ فعالان رسانه‌ای در لبیک به رهنمودهای رهبر معظم انقلاب
🔹
فعالان رسانه و فضای مجازی کشور در لبیک به رهنمودهای رهبر معظم انقلاب اسلامی بیانیه‌ای منتشر کردند.
🔹
پیام امیدبخش رهبر معظم انقلاب اسلامی به مناسبت هفته دولت، برای ما اهالی رسانه فراتر از یک پیام تقویمی و در حقیقت نقشه‌راهی روشن در میانه جنگ ترکیبی و وجودی با دشمنان این مرزوبوم است.
🔹
ما فعالان عرصه اندیشه و رسانه، با گرامی‌داشت مجاهدت‌های خادمان ملت و یاد شهیدان والامقام دولت به‌ویژه شهیدان رجایی، باهنر و رئیسی این رهنمودها را جان‌مایه حرکت خود قرار داده.
🔹
هم‌پیمان می‌شویم که در این برهه خطیر با بازآرایی صفوف فکری، بازوی توانمند جهاد تبیین و تقویت‌کننده پایه‌های انسجام ملی باشیم.
🔗
ادامه متن بیانیه و اسامی امضا کنندگان را
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 100 · <a href="https://t.me/farsna/459057" target="_blank">📅 21:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۸۳ حضور مردم بسطام استان سمنان در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/farsna/459055" target="_blank">📅 21:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuySauF09PMFa_1e2WiSGk43AcrzVlgjVtENv4Rd-BE06ArC1VQDEjBdajuUvdiNzTCnllc4gveXtnFDX46Ex3nDQjDvILLxgbT_FzUhNDWWYxgz8e0jhBSD29uqKfXWfW-5f1usf6yio3VMyoRVGc9DFlYwTX58ffBX__LxajAM8qdCo4E7dZwlxB619FfPH3by6aMhiptsyudt7-5_2nL_iSRm0RfkrsN0Um-bCT_oFdNcVi8MVXLruSOFicmwopc_GpxxT_xzK6_HzeJXe8KngOdQfgNTS6nSR_2P-loy1XJcUMskczMMhIKWotmF3z2RI3GP19tFvgc3NPVKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوترابی‌فرد: فعالان سیاسی نقش جدی‌تری در حفظ انسجام ملی ایفا کنند
🔹
امام‌جمعه موقت تهران: رهبر معظم انقلاب طی چند ماه گذشته پیام‌های متعددی داشته‌اند که به نظر بنده فصل مشترک همه این پیام‌ها، تأکید و توصیه جدی بر ضرورت وحدت و انسجام بوده است.
🔹
احزاب و فعالان سیاسی وظیفه دارند در این حوزه نقش‌آفرینی جدی‌تری داشته باشند؛ نهادهای حوزوی و دانشگاهی نیز نقش محوری دارند و باید پیشگام وحدت و انسجام ملی و تحکیم رابطه دولت و ملت باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/farsna/459054" target="_blank">📅 21:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRqjMVfoYom_TSR-SQXT1Ge1qLAro4Ohjh9sBrbj58mUI3f4z7Iws8hz3nxYNlpTBJUZWTFx888ww6C79xCr0HPjuEFEba2mURLw25bK-sYYCDgWHmDYIJXqdvDyFEAVh9fGAxVfW6iaio9nRQtZgSjoS2NHJNQb_7uSkCM8umhyd4JMyD_7uUGP3Nu9d_JAPaJ7v3HwCrvi7mnSzK9vOeeqecVKYDxeRVp_YMbL1-qEAOYVchVbdwVAhoQkpgNZP-hjmW5UrNCLxgzqIJH4y73fTaAVx5LT8C61-_LdS2DDCgm12JumFLn3Ca36r2SqcNKJBaf4y5Iwwx3DwOojTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سازمان اطلاعات سپاه: دشمنِ مستاصل از مقاومت ۲۰۰روزه ایرانیان، «فرسایش ثبات و تاب‌آوری ملی از مسیر جنگ روانی» را دنبال میکند.
🔹
پاسخ مردم ایران روشن و مبتنی بر اخلال در توان فرماندهی دشمن، ضربه به شبکه همکار تروریستها و مقابله با تخریبگران ثبات و وحدت است؛ اراده‌ای که دشمن پیش‌تر قدرت آن را دیده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/459053" target="_blank">📅 21:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی پشتِ تیراندازی؛ این بار در نیوجرسی آمریکا
🔹
در پی تیراندازی در یک گردهمایی در نیوجرسی ۱۰ نفر هدف گلوله قرار گرفته‌اند که ۲ نفر از آن‌ها کشته شده‌اند.
🔹
انگیزه مظنون‌ها از این تیراندازی تاکنون اعلام نشده است.
🔸
ساعاتی قبل هم در یک حادثه تیراندازی کور در نزدیکی «واشنگتن پارک» در شهر شیکاگو ایالت ایلینوی آمریکا، دست‌کم هشت نفر هدف گلوله قرار گرفتند و زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/459052" target="_blank">📅 20:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">توقیف ۲ میلیون لیتر گازوئیل قاچاق در آب‌های خلیج فارس
🔹
فرمانده مرزبانی فراجا: مرزبانان پایگاه دریابانی بندرعباس، بعد از اطلاع از انتقال سوخت قاچاق به یک کشتی خارجی، مانع انتقال ۲ میلیون لیتر گازوییل به این کشتی شدند.
🔹
۶ نفر از متهمان اصلی این شبکه قاچاق دستگیر و به مراجع قضایی تحویل داده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/459051" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459044">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-VIY1_dZGXnHSsLnaIlwZFRGS2wi25mjkUx74JDdgvG_rOwsowXIqBCDeSpiLH5xnehDGrom_A00wHwCbvYizdsuuDVAMZ4rNJZRxq5rud3s6N8JvNIf6maOFjLrH3-ULCYWu9oiiwvyukDP8XrwEDP46tPvzvU7NEy6AD4P4iyx0JO5qQCkBAU9qww0qM2Ze-R98-IKVYaQWaagRdBRyokUS2-Yf2NUNju6JsyYaWmsB9qBnJdyo2bXOWTVTZnOPy6_fbG4phwIuv5B9YsqmNk7zsC9TVz81WY6o5ArYYTwdQ-s7Y7cfLtrGb0VB4j3Yo5-p0cMI0P8b-FJWpz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhkA3wfDV3Gu7Opnw4vYdNCmoAu5hcv66PV10ibZ63QTsln2HxSXpExLFswTFHsBjSvYlhC_UXpSSfAIPqxLzcKGvxX_pBxEY6X2FGFbud_ZWKerhgz5I5wG3o9s6jsTKqkTUdZA20v3KueMO5Ta_ptJC_cm7ZEf9H1GC5Q0VdF1-ELRTMZRjhEGCVlt6ppgPAgPOZTyCyqaR92H3viwpaGNzorRjB4dUhneC0RZYf20VUNOhYDfmKjxwBuu7CZJL-DGzRDYtwwzW3sc8lStbHENAroLasAjSzyY0UCYqMSLZc04aSkZfRsnc0I0NOzeHxqPTI5ib8pGn9Uk7SrMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhlUA-QHZJZa-EgjxawXANWPuI3E7Ru2TXQXB4ANJ8p4RXLccpEVBVxK9voRlmjn2oY-DObgorg49zMac82AQbgy-Is0SAzkvFQ8m3C8yPLpEgIC_V1cmEVP1y6pikcLNvDjGP7pKdeMrFm6EjB50U1G1uacJ16rnGA43HaZVX7jSDzTwf_rry9ZnYF5nL5tG2GRXfs0T4OKs1BpovjCU88H-kyWlf81w5j2o4pPvmTOhw_4eiZTIG1cOs4ryZE3U-yE1B-nPdLwWexookzKrihajTildqQ344VmsGa9y8V-5fyssNFXyHJWDfbjuElAOO5Ng_3L3X5WI4o3fYbtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfuW4EDIthkqH_R5qtJa2BjSPiHiBqlmctfHzVwsbJp76oQ4YTGMKFS5KWlGlbppxrTovqqaO7bTRkJBXGCNH55KQCR6JxlI3Ram6S7aw5q_XxKEL4Jg5CjHdfZh2f9AREzyj7isM2zuIvoP_AFDN_DP5gnrL3u3wmdeknYXJZpwlAeun_Z6aiHk7BX01-ZnARnVpA0W4UI2zueasiQlU9zQulp-VciRv-KyL4P7fdoqffS-mC2m0KRCE3-W7wrW_VrFdesJvTbFbjbRz91kOCRIkg_W-Z1wIav9ihW3Hww2aiJa5jN08RUhvViw0RXVye8EeSmkKg2EMYj8KVMv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGx23ZC2xjwu7g2bFdlrx9QWDkEVL4Wod-dP6zM-lgaC2ucqsyKIPL3jfOgK6uWxtUcFEVuOZ2rMr0EnRhRdJLda-WhcWKOLczxdWOVOtTcoQ5pLAEMsQXUN-e1y-pyAvP-95kD_Z383wC5FONyp_qnJFsfyOzWItz0HZwumhbFQFJcPzhD3R8TcmZGp_MBfaNyE-bu48BWFxMPn8bUSb3FQF0q9prfOZyia3uEobv_54oxCen9zENWilg_9RSUdv34pFve5m7yGLfCRLv9z9ZkHuO6n6cusHpdQwNbWAslryqDiFjbj5KxSiHWgCpKLDrZY98uH0pDBAJXp648ziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiGMJOo32Ibwgs1RzoMq2Ivn_R5wt3SWi1t5PPHEfJB8cf2ddCU0aaq3hVufjTVR-IZwHjZnVXX_cKP1dji03WNHqFED4KRqaxmUysntQlh3XqoIFBz_KItbS_4b8IWv_U-UvqW_m46kWlViXuewVy_cf_kEuo-us3jn7KHHzmTSO7oL6Bl4xB5zrJoJZqniGI1Ha7XOsxrOfpb7Q9jiukq6v49rAPKdO9Pycz8tvWU1tKyPJUeWSjhfcGK89xADECLbY61ha0ErsyzaZJNwu6usRV-vd1Z493Mb5rskr-myLh31URjyWoBqd_nkvhwGM4QdpbDShhH8eyQJlxMvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qep7qANuwV22l-H_M68CiZRw4JT6fSHWhgqXae12HvCjCfn0T2cLEf9mgpvZgiLHc5aiF_b9Em8QrVEikzffkWnvM0G-eBu3lMWEF7siKGamKuIxs5gyyDAsJ0lqu8liYsnzHiJYd9xYJKdqfgDo-hiAcxLyPNk3lrktd9d7SUrt2OvvcLKDqn13XMotLgMJUT2WE1a2qePUdtaJ5YN7nuEoLNdhnfzqBz0Mb7zTqZqAhCTxpzOTKgMOLO_8c3kkut-asapYM34-LGYdmtWILhdk3bc4NDh_5I88xMf-aIhDHTLXHx-7QPzbcF8IUjaCi6wScrkqzoWCtZKTIXohPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/459044" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459043">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت پخش فرآورده‌های نفتی: دوگانه‌سوز سازی خودروها در دو سال اخیر  ۴۶ درصد افزایش یافته است
.
@Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/459043" target="_blank">📅 20:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459042">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم  @Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/459042" target="_blank">📅 20:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459041">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbXjhxWHOyluDxRc8OhyWakPwQkR-CcZcyUQmdalr1g8klL-0kCTpTo6Mkb7s7aeWVFIiUH5bizNF3ZTphfw07ob5xzqgwK2sz_izhvJHknUFcmfBbQmdX_ILvu2hv4cp0xtVN3ja7Yfe8l2fX5t3C3iAOh229NCZX1Ac4X_WPGj39Pq0T1M9DlHp0dcVQG9SofbNQS1N7PlpSgfvSVhZt2v3an8sKirWz79GwLCx1GYcjO_GLLSDbTKJ_xTO8NbxudYGD8JqAi3urbFu0bDH_bZk5F3uNKYZZ1aOaKUaK1yDOKL7k7tjjuGakX0uVq9JvjbsCdWNUACUfIWTKI_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنوانسیون خزر و زنگزور دو لبۀ قیچی علیه ایران
🔹
مدت‌هاست ترکیه و آذربایجان با چراغ سبز آمریکا، کریدور زنگزور و کریدور میانی را پیش می‌برند تا منافع ایران را از معادلات ترانزیت اوراسیا حذف کنند و با بازگشت کنوانسیون خزر به مجلس، میدان نبرد ژئوپلیتیک و تجاری امروز در دریای کاسپین است.
🔹
دولت چهاردهم در شرایطی پرونده رژیم حقوقی دریای خزر (کنوانسیون 2018 آکتائو) را به مجلس فرستاده که نقشه کریدوری منطقه دستخوش تحولاتی اساسی شده و رقابت هر روز شدت می‌گیرد.
🔹
پروژه‌هایی مانند کریدور میانی (ترانس‌خزر) و کریدور موسوم به زنگزور که با حمایت ترکیه و جمهوری آذربایجان و با چراغ سبز ایالات متحده  با عنوان کریدور TRIPP دنبال می‌شوند، در تلاش هستند شبکه‌ای از مسیرهای حمل‌ونقل را شکل دهند که از شمال و شمال‌غرب ایران عبور نمی‌کند و عملا ایران را دور می‌زنند.
🔹
نتیجه این تحولات، شکل‌گیری کریدورهایی است که ایران را از کریدورهای شرق-غرب حذف می‌کند. این مسئله فقط کاهش درآمدهای ترانزیتی نیست؛ بلکه تضعیف جایگاه ژئوپلیتیکی ایران به عنوان پل ارتباطی بین شرق و غرب است.
🔹
تصمیم‌گیری درباره کنوانسیون خزر، یک انتخاب صرفاً حقوقی نیست؛ بلکه یک تصمیم ژئوپلیتیک است که می‌تواند آینده ۱۰۰ساله ایران را در منطقه رقم بزند.
🔹
در چنین شرایطی، دریای کاسپین به کانون معادلات تبدیل شده است. سؤال اساسی این است که آیا صرف تعیین چارچوب حقوقی، بدون تضمین سهم ایران از اقتصاد و ترانزیت خزر، کافی است؟
🔗
پاسخ این سوال کلیدی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/459041" target="_blank">📅 20:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459040">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امکان ضربۀ مستقیم به اقتصاد آمریکا و لزوم دریافت غرامت از کشورهایی که مبدأ حمله به ایران بودند از زبان کارشناس مسائل منطقه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/459040" target="_blank">📅 20:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459039">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n511R92lz99A6f7W8kQ5_ABIZlbAQ0zvBI6d5eOyP-z-vp4FS7FiI_NNR7F8DIEVuORazTQPhDFQXfYWz8hQe9saa9SxRtNQqup4NW8PSevN-OdPaoXTWhquHln9UuHS88ZAUF3UTPDHD1Ptfn3uCpzv4YDKQ8YlZUMwSXg82u02wfzBM4FC7SdTp4jupS1YHGLPm08gX_WYUnqQP_ANn1bI0ovSBO6WyHFP9b8RRnjyxahmDdbGbLDHRbpHUcn3HrAzfLkdYuGRTmFiTwzUIshClD-N6wHpBSxDTdksoxRZ_v64fHXsl_eih_jGSdg_k5TQlOr18fi2huazVgslRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت دبیرکل سازمان بدر از بیانیۀ گروه‌های مقاومت عراق
🔹
هادی العامری: گروه‎های مقاومت به شرط تحقق حاکمیت کامل ملی به سازماندهی سلاح در دست دولت باور دارند.
🔸
کتائب سیدالشهداء عراق امروز در بیانیه‌ای شروط ۱۰ گانه‌ای برای انحصار سلاح در دست دولت این کشور اعلام…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/459039" target="_blank">📅 20:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459034">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abCnoj8xgcirqXjaldW-eNILMOuxZ7Wbk7PZf8CbpcTRwE0S5lScXnoKWtpkrx_ZC1_tpPEzkMa5pQg6BC7MZkbU_YSejHYe-5S3R6mk2IXeVYx53X1PQnqZ-aclTH3FkuaDY-8LZWVqPKm2FygYWo-kFbcakFK7trTwr2BtfmtJ4PIR3fgKFfIjbq_F_UvufJJm0h6BQ_Ca6ENM2KGFXSxqK9RCUOFknQypgCIcymT6crYBWZoWsEUAgViDiqwIxaKCom7NKsgk_QfkovwH6dZ8LFQ-IMI6TAx5DTCdy-eJ1BUe4147q5tt3PK8JI9D7lFLPtJYFUwnsLy0wy8fLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzU0YoSwQc6CNGX1xjs0iJvj7UN6AUeRIzrIq9iC9E2NI3XSwf8X0HmHSbn70OettabWBoeZiV8XvMPAr6lEFYI_46JztPvx3yPA-zxZ-nnxLh01torfzOtYCaBembogdTjP7iNgZUEHBfHRFEYyHp731HKYc5cp_Dp9WL2QpT8Quaicx1I8irHjwnailgWl0UM1-uN8b_gHcshH72JYf8_l5qgy-HgH_bBGB_mh0jy0PwnM_BwvJNKeELYjBe7NxhcdSzCDHvace3FL15pqy-iIPEW0cXqgAPr-_rf1kz946YOjyjCCo_yw5Sm2SNiii5WxgwWJnMOhp7s5VPaQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIhnJ0BGsLY_jSfDQGK8K4VxXpy-U6GbMkeoWmWcpPT2Z32BfH_t3fn1IAtiNlCMseCiwDWEwzhDwJ9lzSLm4HfPVeQ7gO7_Ucj7Wk3UIn-JRwGgkyCuRrcz62vn7pngXVyXaGX91KJlLbkQZ3U6YzC7lCNTcd2wRrycaPjCdHUssjKbVo_Zcch2VF6PNWFtbRGMAUvkk9Nhi2DdJMUZsW4EYqg56x6JKP4YE6J9NnFdeB6BhrpeBWO2sA_UJc25fEk5apDLgcmyeY-zoU9mVg73szgV0ljpH5N7ZcGwbt5e_UrbyduSpraENPuFqI0QmxgQ8S5z3dpnONOhsBwt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg8RR5A9U3_34P3X9Kf1JvtiRGJziVz0eDLJYWv8ehqhQwKe14LGI6L0vo_5GUKfEze87R5LAjXv2HoqZfSQPOItH0kE3Yj0ZdQan_aBsbfCM_vHczxlxN4dWYTQcLbw8vVap_PzZ4DFOEZ6SReudCRnA-aONP4Sj6QxqLYAaJGYfJdZr1rIFc1vaVKA4Gmz_K89bV7v-Do-tQvlAbFaQ7NDRNAKzXDv--qNj8cjb-MzJO_vgqIMsT4VX4y3AS4Ebc0vJo8AkXZEPshaJRPzuiiEaxeUmbpLQ5pg3fkb5yl_5r8Ph-07PgsJ78nt4CvtK7cRLhpiLEg06y6KvNM43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIlUDj0g5eEdbq0QO_eXCgXhP0oKECzIPdk51Ls1lp7oBZOydrLNN2aRNY5kxkpmLyn5tyS1eXHcS1qKkiSZ0ZobovZMIVsn9kAuA8awm6lZqGCxXGrHwOQ5zmEUnnoTYs8iQOhg2qkKlle03ub7QclK1BMNoqyumoUMznGLcE7mjvr6dt1XGBulELLPyhqBMWJjiV7gvzWWIZeSbZwMR5jTWBNh-GHeFMCx29Fmpq4PI7VVOpVF48sdxT93-hQnqpSVwJABsuKdGRGNplYmukpo6fFnvp3rIG_RfqeAaUACKIIze2Fxxjy11rZwgWoLeDxoZpn6IKgMkV75bghFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در بندرعباس
عکس :
عماد یگانه دوست
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/459034" target="_blank">📅 20:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459033">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzYdhl2OCnUsy900F70SymzfAa2CrxEi5fYiNwUhdzTDwQh8DrM76f0DD_PqU9xn7JugfQnC84i8miH-57ytCSM1LZJvIs4pbVoKXIYLx7JHfCLX9tI6B6rgARGRaHQLHqoHLQHMKNNCoy_vZ98GqyX5YWc-Gm0Jr7zFWiqPqVdH61BfY7Ap6opvwB8Nigyqis3QLbyRPqQIs9t05-FteyFOhpySopGMNr1WDx4vi0rkK-3j0vbpeepZ74oAP3lqIxcuc3KQqP4TYA3tj2jW135uD3UM5tI3LQX4jeSeziPKnIvXAjUkJlCmYYHT8aKm6ejrhAkHT9nc-eRCiklq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرارگرفتن یک نفتکش در نزدیکی عمان
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش روز گذشته هنگام عبور از تنگۀ هرمز در فاصله ۱۲ مایلی بندر الخصب عمان مورد اصابت شیئی نامشخص قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/459033" target="_blank">📅 20:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/459032" target="_blank">📅 19:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459031">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور پرشور مردم در جشن امت احمد در تهران  @Farsns - Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/459031" target="_blank">📅 19:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459030">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
تصاویر جدیدی از عملیات پهپادی یمنی‌ها علیه مزدوران سعودی  @Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/459030" target="_blank">📅 19:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459029">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l66lvSja2zbHDxwpdr5mMIU33TNLlG4GtXmjeXf95yUFs9iLEJ8KwwZ08nSnu5gsGpWWAGHfcJmo_Xi5ISye3nzQMWj5UvHFO5EVLQ0iLraDeX8bgIYz5UlzlirOW_Ma-b0JwGol4zunWt-vcs-IJYAwq2vUchM1C8azDy-qmmWRUwTrWpIB--ElYhcXcxfLKXW9lfE1-SJe8XvVaH8oYwsQta28Cdo0p8ocJElQAAOUhkWmfSEP73yqlTeupkdx7ttUgmB1GXCh4HMLfXOqAxZ91eaxE4YL4IlQLeWsqn42E1RwxWddJL__T2JSf5Gie675Il55oqfJjYScHjL4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار ناشی از عملیات ارتش صهیونیستی در یحمر الشقیف در جنوب لبنان
🔹
منابع لبنانی همچنین از حملات توپخانه‌ای ارتش اشغالگر اسرائیل به شهرها و روستاهای المنصوری و صربین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/459029" target="_blank">📅 19:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459028">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2658b97b.mp4?token=EBflCjW5-IEXxeZTI7KgHB9EbLJX8k70a37ABTQxnGOYZ7QezAw6glgf6_FvNCVdbX_1-IMQorYj--Pi28bk6KAM1EQ7x4VlEGS_eK5QNGerX6SGcR35CAO_S3Fd49cF5_8ZgXU4fgAIVLGo18P0D290kCRM9Vk71jYOzunktmqm_wbPsofFBN2ALtCF6m4eXf2pbUxg2H-WAYKGQjQ6LbOggG5XyjKt6GHqvZf4wfT_VU8YQ-ktJIwMpXlD8rQSWvpRLhr0ClPfHJWBwwEih8K9WnYT8IrExBc_Y3SJyLuegM3HX1_A4FJw4OWuMy7cGPyzF-J1iTvzZQwxZeUCkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2658b97b.mp4?token=EBflCjW5-IEXxeZTI7KgHB9EbLJX8k70a37ABTQxnGOYZ7QezAw6glgf6_FvNCVdbX_1-IMQorYj--Pi28bk6KAM1EQ7x4VlEGS_eK5QNGerX6SGcR35CAO_S3Fd49cF5_8ZgXU4fgAIVLGo18P0D290kCRM9Vk71jYOzunktmqm_wbPsofFBN2ALtCF6m4eXf2pbUxg2H-WAYKGQjQ6LbOggG5XyjKt6GHqvZf4wfT_VU8YQ-ktJIwMpXlD8rQSWvpRLhr0ClPfHJWBwwEih8K9WnYT8IrExBc_Y3SJyLuegM3HX1_A4FJw4OWuMy7cGPyzF-J1iTvzZQwxZeUCkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان در مرز پرویزخان
🔹
وزش باد شدید در محدوده مرز پرویزخان بدون هیچ‌گونه خسارت جانی یا مالی به پایان رسید و روند فعالیت‌های پایانه مرزی طبق روال عادی ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/459028" target="_blank">📅 19:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459027">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p96Xe0J_dMH6FO277BCi0lKmjlTmgCqseTLuvbK5oXTQ0j6vofkZkHi7alMrNSEFhbdIWmaGEkqGx34u8S6SBwWeEEVF4gXo8nKnzaXQJHo6i-JOpJhxNRreQCxCsskulrVOGheTQh4psYyA6yLmqnx3SKCHoii25lCYtmCmY__h3yyWCFDIEwpt9y7X1wthEFbgRSMyJS1WUDMjHyN3qVmO1t_kiiJ3vImkvadh8wUCDFjKRlhpdEDNLqYo7yRwLYYvmHXcCPxDqzS4vwu-dWWacWg9KpCo-zxz8zXlHvgiFPxI8IgcDc7gZsstPrS-cGGzqtw6BvW2FXDiaoSl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر لبنان باز هم به حرف‌درمانی در برابر تجاوزات اسرائیل بسنده کرد
🔹
نواف سلام: مسئولیت ما این است که به تجاوزات و اشغال پایان دهیم، مردم جنوب را به روستاهایشان بازگردانیم و حاکمیت دولت را برقرار کنیم.
🔸
نواف سلام درحالی مدعی تلاش برای پایان جنگ در جنوب لبنان شده که ارتش اشغالگر طی مدت مذاکرات مستقیم با دولت لبنان همچنان در حال تخریب منازل مسکونی در مناطق اشغالی جنوب است و عملیات ترور و تجاوزات اشغالگران صهیونی طی پانزده ماه پس‌از آتش‌بس پیشین ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/459027" target="_blank">📅 19:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0e714a8.mp4?token=rxWErPLD1D3OMnMQjEf9Il59gwwRRZJWmJfxTXyHUBmdCxtXiaBd6iseksU4EYSWK-iRKUCYtSFDRzLHF0ZG3BAgAMZ3q-bWyYrAg-TWRNM-PImiLWPZuQe1ckrToj1cm68h-bXGqo23IPwnGXl6_uAjuciz7zUDL44YYszUNfjym1DLx7OUowB4lhGqWSM_2xo6tBs_tz4Cv0j-h9NFcZ93tx0GTOBDhcdfZxfVAIYeV2qO1ydTjHx8GAsDU80lyo2xK4-hqhmewAXs-LlgtHXjW_G_UGWUaCOotBGPwHP6uUhQwZr4gK9P0eMzDTRfKxbDgcmD5EhECBzF9cqbQqsGWEd05hT-dIxdUBIzES_FBQ7oCUCfY4kqrj3HIjXNr45W3wUXOq5g8jpm-4lbDvhycspW7HZKWiFrUO7Al1TZuBcv_HVpTLD45n_3Is2fJ1Gj7VPCj7-gW7ho8GA6b7-2r6RA2svKiuLJVCcOEECoubenanFYH2pJbgAwOcc9UtvsAoZylibLeerO3U5UoT-ez8irfVP_6B0nW_3PEeYzkWMW_Q5-8y6s2XsT1H2kGK2Xn0U1xlJ2EHmIQX47TpQDt67yVYdjQxPYnoMIJZwULTY_ZOoWnlDAGCY-s6Zd3daHbVagZeXWtyF7zI5TY2-z-UkYmWKuZoai-N9wj10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0e714a8.mp4?token=rxWErPLD1D3OMnMQjEf9Il59gwwRRZJWmJfxTXyHUBmdCxtXiaBd6iseksU4EYSWK-iRKUCYtSFDRzLHF0ZG3BAgAMZ3q-bWyYrAg-TWRNM-PImiLWPZuQe1ckrToj1cm68h-bXGqo23IPwnGXl6_uAjuciz7zUDL44YYszUNfjym1DLx7OUowB4lhGqWSM_2xo6tBs_tz4Cv0j-h9NFcZ93tx0GTOBDhcdfZxfVAIYeV2qO1ydTjHx8GAsDU80lyo2xK4-hqhmewAXs-LlgtHXjW_G_UGWUaCOotBGPwHP6uUhQwZr4gK9P0eMzDTRfKxbDgcmD5EhECBzF9cqbQqsGWEd05hT-dIxdUBIzES_FBQ7oCUCfY4kqrj3HIjXNr45W3wUXOq5g8jpm-4lbDvhycspW7HZKWiFrUO7Al1TZuBcv_HVpTLD45n_3Is2fJ1Gj7VPCj7-gW7ho8GA6b7-2r6RA2svKiuLJVCcOEECoubenanFYH2pJbgAwOcc9UtvsAoZylibLeerO3U5UoT-ez8irfVP_6B0nW_3PEeYzkWMW_Q5-8y6s2XsT1H2kGK2Xn0U1xlJ2EHmIQX47TpQDt67yVYdjQxPYnoMIJZwULTY_ZOoWnlDAGCY-s6Zd3daHbVagZeXWtyF7zI5TY2-z-UkYmWKuZoai-N9wj10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی صنعت آب کشور: میانگین بارندگی کشور به حد نرمال رسیده است
🔹
بااین‌وجود یک سوم کشور و به‌ویژه تهران دچار کم‌آبی است و به مدیریت مصرف آب نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/459026" target="_blank">📅 19:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07481a4b03.mp4?token=Dkggb_6GnoYb7rfhEk3ZopGuP0_Sycc0t9RATlRX7EWUCwS9CB-IbAPWp8WlPZjIMQ28VT2HuRYtsHy2nlis3EVuoiNHtIT1pfhAIMpax07BAoWwkEt0u-Pc2Pa6m2CDLIIUbCMy_jbPQO2hh-VYlxblAsDIWe6o6W7nSSj1RjsV8ENcyNje-wVCU2ZRQnh9uKRoZQ2D7BIBG1WAO0GZuKjxpw4_ZvLcajrCtv4By4KLQ8eIiVMMyci7XeWwGXnQeLXkL8as_sq8QFl566yZw4nKDXMXJ3DilaO94o_-PFXPzMHimzGQ2De1VTmnGFCI9MPv9fPOUrwBoET7cHyOAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07481a4b03.mp4?token=Dkggb_6GnoYb7rfhEk3ZopGuP0_Sycc0t9RATlRX7EWUCwS9CB-IbAPWp8WlPZjIMQ28VT2HuRYtsHy2nlis3EVuoiNHtIT1pfhAIMpax07BAoWwkEt0u-Pc2Pa6m2CDLIIUbCMy_jbPQO2hh-VYlxblAsDIWe6o6W7nSSj1RjsV8ENcyNje-wVCU2ZRQnh9uKRoZQ2D7BIBG1WAO0GZuKjxpw4_ZvLcajrCtv4By4KLQ8eIiVMMyci7XeWwGXnQeLXkL8as_sq8QFl566yZw4nKDXMXJ3DilaO94o_-PFXPzMHimzGQ2De1VTmnGFCI9MPv9fPOUrwBoET7cHyOAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن بزرگ امت احمد فردا در تهران برگزار می‌شود
🔹
این مراسم از ساعت ۱۶ تا ۲۰ و در مسیر میدان هفت‌تیر تا میدان ولی‌عصر(عج) برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/459025" target="_blank">📅 18:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-f6LIeyFQO68xTljPyiITXvcY-4XwQX9LBMpDH2c31waJb70lFoiLAx7oXpPe_LxTTUPHzJ1eP0D-GdeTz6Z4cBOU1vjDdWLD2c4HaF8AJDZaKyzuKdeZ7zl-QNoe6E1ItKQk01zudwpelGsKeHmh_IVFp7u2z40rPc5OLQyW-RpPIrS8vm6VldWdTe2LOITC_7GCpuScxK1Jo2pEKcdQdUiyNX_Ge9C3-oacMLbHM_l1DnOgmLaEjFh0JoUnj7LK1Cf8kUPOwuI6ydWkjFYbZfWmqEtv_zjAfAChXHbEfGariWQN-tur-kh_jH_WZC2wxP5kkbrIDCnYuiVErjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: نفت ونزوئلا ذخایر استراتژیک آمریکا را پر می‌کند
🔹
رئیس‌جمهور آمریکا از توافقی نفتی با ونزوئلا خبر داد که بر اساس این توافق، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شدهٔ نفت ونزوئلا را به دست می‌گیرد.
🔹
ترامپ اعلام کرده که از…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/459024" target="_blank">📅 18:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTucY01AbbpSeZ0szCkFAxNd0QcVMagiNc3s24MLiVj8ZTs3wh9m1VlZ8BPxs7Xwy7EFz6Kkh4ZxJVT0a8ghJmsWGj0YohYhOZ1yqlS_a_yjfX3oCQwlcVpHA4wX6mYiytPVTI_hxu47aOxyHY0tPAahbUFPN9rin4gLTHkTJQbXpzoyONdMG8Qd3EF0Sm8wpez4Q5lQJKmryCiPgvrwrn9QUHKevCHgi9-rBxqyw6r2-ISjXLPkIxVH-9z8ApkZi61v1kO2o-VvVxgLDdpE1SrIYbHCoPf8Q5QfQYjGMjuZzcuM31S-f14BaEGvQqJ93sPlhbAkBy76GXwWHEmGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام صادق(ع) مظهرِ امیدِ ایجادِ حکومتِ علوی بود
🔹
رهبر شهید انقلاب: اوضاع و احوال مساعد و نیز زمینه‌هایی که کار امام باقر علیه‌السّلام فراهم آورده بود، موجب میشد که امام صادق علیه‌السّلام مظهر همان امید صادقی باشد که شیعه سالها انتظار آن را کشیده است.
🔹
گویا هموست که باید حکومت علوی و نظام توحیدی را بازسازی کند و رستاخیز دوباره‌ی اسلامی را برپا سازد.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/459023" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjvSGKozih8MJxSA_XHTL3VsBIDr9w0oqX27zsfNMZj3CpLbPtstWwGbtoL5lftJi_gH37pKUPj8pleXJVg9RJRfSLBoa6zqd1nqAGz56PdCGR9hvRj2QKEXbP-lkN2vKAe1nvu90KYaZf6CZ0DWBgVlBUjkB-U9Oy9joVupFBw_2C_y5QcnPfnp4qpoQGMeniBC-mYBC12MyUlv1h0t0K4EdN9c2Nqtrz_mk7Bl4KTyY4vkP8MxjURqYCqQu19_fwvZBuG72GqsnlKOuXhzGmWIZDUK_u9vfjTz1CcIz7QkWo-stVy3zvkTYgnEKWVFeOII_5QQqneAzsSnPQzm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلیلی: صرفاً بازگویی ضعف‌ها راهگشا نیست؛ باید ظرفیت‌ها را به میدان آورد
🔹
امروز در یک نقطه بزنگاهی تاریخی قرار داریم و ایران، به اذعان دشمنان، یکی از چهار قدرت مؤثر جهان است. این شرایط، فرصت تاریخی برای نقش‌آفرینی ایجاد کرده است.
🔹
رهبر معظم انقلاب بر «ابتکار مستمر» و «نوآوری» تأکید کرده‌اند. ضعف‌ها وجود دارند و باید آنها را شناخت، اما ضعف با ضعف برطرف نمی‌شود. باید نقاط قوت را شناسایی کرد، برای آنها برنامه داشت و با تکیه بر همین قوت‌ها، نقاط ضعف را برطرف کرد.
🔹
صرفاً بازگویی ضعف‌ها راهگشا نیست؛ آنچه حرکت ما را به جلو می‌برد، شناخت ظرفیت‌ها، کنشگری در تراز شرایط، نقش‌آفرینی فعال، ابتکار و نوآوری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/459022" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
خبرگزاری لبنان: یک گروه پیاده‌نظام رژیم صهیونیستی به سمت رودخانه زوطر غربی پیشروی و چند نقطه را منفجر کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/459021" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auEJSO-gc4qsks9Uo1SACI9YBY0Zy60P7f5fqLdI0t1GKKDTg8SAeG_6P-4BhVcao5EgiOM-1ProV8go5CkyY2SqIed82zTaydH79HSxnBeReHBfofpRGGMIXPr5mckwPxfqLFtzx2VXg4KG9cI4yh5p_MZzYPR5uSDSo0HFiQ2dTgtEA5NrQvjYO71Z0LdZw2FerLhXTqvjELXC9oyZC5pgMY_KLrokoq79Mio9ME9Z6yH7YH-QzbVtvPXHcTSWdiL1hAvKLErEDG8m0FpSlBYqmykj-OzdevFLyOCfaTfErUDgpQ2Q4z0Wk5Tg-iaeXQuefuqYi4_v7jR6lMvS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بلوف ونزوئلایی زد
🔹
بزرگ‌ترین کسری عرضۀ نفت در تاریخ به‌واسطۀ بسته‌شدن تنگۀ هرمز رقم خورده، قیمت سوخت در آمریکا درحال رکوردشکنی است. نظرسنجی‌های آمریکایی هم از احتمال شکست جمهوری‌خواهان در انتخابات میان‌دوره‌ای خبر می‌دهند.
🔹
در این میان، ترامپ این‌بار…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/459020" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01c72e934.mp4?token=khkXmicspkJPgpG11MzCbMVxJTWwi19k_E90TbQpUxK2nyL-GdoiWJ9m9Y9P1Lioe4WS0F3OblIYFOeRVeVwJl2fY1xcTW-bbAh2oajy3NcLwnhSD8r6zyCbYmd9wn1MCKsP9QpMjcITDD90Qjf9WGoFYx6esr4GbYYFQ6xXW68chqWB3I911SPdI39LjxyMvhS6HI_n_QcGB3sUsHcUbG4B66NPo4Pa1pPxBFKSQsf6GMlPpv_kWM0xJ_BRBreyxf7WiTjLaOO-QpQV0uNVRYVcvfjHj5v1opqWXSeQu-Df1mskjID6l9Dxlz6UYmPX3e5dagFQRUfEGZGxjS1j0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01c72e934.mp4?token=khkXmicspkJPgpG11MzCbMVxJTWwi19k_E90TbQpUxK2nyL-GdoiWJ9m9Y9P1Lioe4WS0F3OblIYFOeRVeVwJl2fY1xcTW-bbAh2oajy3NcLwnhSD8r6zyCbYmd9wn1MCKsP9QpMjcITDD90Qjf9WGoFYx6esr4GbYYFQ6xXW68chqWB3I911SPdI39LjxyMvhS6HI_n_QcGB3sUsHcUbG4B66NPo4Pa1pPxBFKSQsf6GMlPpv_kWM0xJ_BRBreyxf7WiTjLaOO-QpQV0uNVRYVcvfjHj5v1opqWXSeQu-Df1mskjID6l9Dxlz6UYmPX3e5dagFQRUfEGZGxjS1j0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعویض گلدان‌های ضریح مطهر امام رضا(ع) در روز
میلاد رسول خاتم(ص) و امام صادق(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/459019" target="_blank">📅 18:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1267e25395.mp4?token=mrMErveUGs4ukhcFTnLL_Px6Z2924XIkLVqi6uYRBXJ3dA1t3Zu3kDrnxj6F-V4Ui-HIMOFNi2XBM1jo6HC205L4V_sKVqsnQqIebgjM4Bj8muVqNruq-mhFHYIwxSD1SWblNsRTRn1Fa1HaIZFRTFQe8MJVN7MqaPF1qGMhRjHNurfBWsrSN10OKwNfmuH6WfEBe-PqXpW0SS9AO_1B89YmH1iZXwVRW_54qwDoPxYzxTy4dNOFU5r5JcEi4urlCciHJBjlh7PfAJFH8UwRUFZngkI-tSYxf3nuybBRkdplOwIV2rYyVGYQnX-LsBpKPMJGA2oz_R3a50L50XWm1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1267e25395.mp4?token=mrMErveUGs4ukhcFTnLL_Px6Z2924XIkLVqi6uYRBXJ3dA1t3Zu3kDrnxj6F-V4Ui-HIMOFNi2XBM1jo6HC205L4V_sKVqsnQqIebgjM4Bj8muVqNruq-mhFHYIwxSD1SWblNsRTRn1Fa1HaIZFRTFQe8MJVN7MqaPF1qGMhRjHNurfBWsrSN10OKwNfmuH6WfEBe-PqXpW0SS9AO_1B89YmH1iZXwVRW_54qwDoPxYzxTy4dNOFU5r5JcEi4urlCciHJBjlh7PfAJFH8UwRUFZngkI-tSYxf3nuybBRkdplOwIV2rYyVGYQnX-LsBpKPMJGA2oz_R3a50L50XWm1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وبسایت آمریکایی: حجم نابودی پایگاه‌ آمریکا در بحرین باورنکردنی است
🔹
وب‌سایت آمریکایی «میلیتاری تایمز» در گزارشی به ابعاد خسارت واردشده به پایگاه پشتیبانی دریایی آمریکا در منامه بحرین پرداخت و نوشت که این حمله، یکی از مهم‌ترین مراکز نظامی واشنگتن در منطقه را به‌شدت تضعیف کرده است.
🔹
این وب‌سایت در یک گزارش تحلیلی درباره حملات روزهای نخست جنگ نوشت که هرچه اطلاعات بیشتری درباره حمله به پایگاه آمریکا در بحرین منتشر می‌شود، ابعاد واقعی خسارت واردشده به این مرکز نیز بیشتر آشکار می‌شود.
🔹
در این گزارش آمده است که گستردگی خسارت به این پایگاه احتمالا یکی از دلایلی است که مقامات آمریکایی را وادار کرد شدت آسیب را سانسور کنند.
🔹
بر اساس این گزارش، میزان خسارت واردشده به پایگاه بحرین نزدیک به ۴۰۰ میلیون دلار برآورد شده است. مقر ناوگان پنجم آمریکا، یک پادگان، چندین انبار، برج‌های ارتباطی و یک ایستگاه تأمین آب آشامیدنی از جمله بخش‌هایی هستند که در جریان حملات ایران به شدت آسیب دیده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/459018" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbmMqqgKdl-mUNwQx4BXrBobKfrcNrCbZi__RgWIEMexLB6jFYy0S1fNDh8BbVCF-Ziuq32woI_hdynUEABmhhOmK1QVc-Rqcb9fjh0Jd2i-TExJD2BnxapsSUxu-f93oxqk6WI9h9xjU0A0To1sqbBnOtKJ_5DhNdMtu1RUm89H6l0RuPrRMfSaEpL_KMmHMG_JGeFpsHUozXG7kAHa2-r_zwqoJaihAkQlHnt5kJf58Uyc3TvG7-dDKFY_MlLQ2PRv4v10AkyHTpLSBKF8Ai-bSDaaKiNQoMm_k7hVHsviwEkK-gxY1dcy5QMBM3MrO-xFr4n9crdSi0bGmnJIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq6-pXbqFHuqba0G1avIpuLIQyAWH4Oe0lVjmbSrFyey7NlBs_e-huFYUB91HVMcx5KVFU2MddF2tAeP70cQZ_HFZSW0kQ8366oVbZOrD-onX4YEhtibHUD--HuIFN6C-kN4sWJx8fCpQsJA6kEEZARXJByxUIHobL6Gx54rEIeJGcAbAihJwg0p-BmaN0lXV-IIKApdSE23sn0tJcE0Rpoc0Q5uGcInRdRfNDg-9gbiRqDEnafIeYPW74xwJ_sGY0bpp7ZVRCZdcUadmxOjKxmSSrA1layvIvpRLcZ_nPeFkm5RB9F7t0__-vS1AXk79CJ8qz8xIfvTK2yDbl_xQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_loN-hnfcNOZ228QmOtbATsZewXFmzKHfP262xWD-viMRu4xTTBP0qppNMreNl_bm_tWgeglLEU4893ACGofg7dZ5HQrCyAaABc2MN0LiaT2iL6kV_lpzVWiPJXWrYg8KOY6ppIaK-2wOuVhhlO0oABrZTlNZm-_hVTIbEZUeNNECkNeGJK3Aq6YGDPl7tnIYA3c0wIlltLZu10Y4KzOVXFLbadzKUaDiX0__0PU7Wp-bb05kQVq-GX2scj_ZuUT8DUpm4dQnGVqpap2zhBb1quBM6BGs-3ESChdfIYCQAOtZwS6FQ71VDnWStT1ShVMFvumFeoDsShqvO0kqt8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTi7CyRQKOLFmiaVI763Jv6K9oMy5ktsXvAzUAumD-2uyW0aUOcHAiTAyhkKuF5Y5I-Nk1fO4O_K-zI9AT7zCbK4OynYVOfERI9fkzawnHEvtVy27q7TtTdk8Dp8O7UvZ8e6e-X_zeOgQS4tYjwEwtytinz1S1cPSzwSU0jXHQrFOITm1C9BBLM5mcjaEHZbP-pqx49-IElLRqc24Fj3oy9zgd3ZKrH2yLas8MBQ6nb2vCbSjp-RooKkCceOjNCr_dYk98fSD3ZvAI9-8-d8qsikBDilydGEaqa61FQPpy27tAu06dJyISHE8w6YS-BfofCpeulzTDfD4Ou6BBQn-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور جمعی از میهمانان چهلمین کنفرانس وحدت اسلامی در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/459014" target="_blank">📅 17:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d136c2b860.mp4?token=R0EgIKlJPc4coTgSeHLZaA5ZIFS5xtd6h4XRHZNdxoOvVHAPdkPVsefhD3-M2RSYpHSxZfGGjIQrxi8lgIVK4Y-Z7d_QOhZqC9Ka14b__aIpWc5CMIK2bKtb5ehNqId6j_WAJbkmR88U0PA_dlim3XomhRkJAYufJu4NcxLrnoPqoYMohiZoxc_cGKc_x8ikazN-bfe9vBTBpH0unyhxA_szK3lkY6CLlz25Kgts_YW05nWTj2L0ii1ctVm0PAVrfsL7tshREpEF9lejn6Qr5yAAN0R_CUR8NZaGJYBRuIDNvvT2DfRtsSNDhjXXF4PAYcgKWbrUn3pjQxyem43CD0hMyQoapPo8hWEIAa1vfEWSa4nawEOFoA8qkgUGqLNXfCVOa61X9XQBK-9JS2lkNYLenJC7Uxyk6s7VxwAUvM8sgjP_kgNpOtbLjv9eqFwv-8nsD-2p5ScDPDyITH9o5uKull8ZovGNp_ydg1lUYQDu1SPKXxEOQboaeBpoUnUoY7FWT7fNTThylPS_ItqZuBMzWZus69I-VOZ_rX8eQ4raZ2-35nlpDUpvhPF9ApPFVXCfYyScGoYkH5_6leMrTeN1GuIczPNywxwidj2YjFmyHBEZJZi6F__gwNijVyLMlP67CIAsETF2Il3vUSwU7vRQUxlTNiCeHTttSABqVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d136c2b860.mp4?token=R0EgIKlJPc4coTgSeHLZaA5ZIFS5xtd6h4XRHZNdxoOvVHAPdkPVsefhD3-M2RSYpHSxZfGGjIQrxi8lgIVK4Y-Z7d_QOhZqC9Ka14b__aIpWc5CMIK2bKtb5ehNqId6j_WAJbkmR88U0PA_dlim3XomhRkJAYufJu4NcxLrnoPqoYMohiZoxc_cGKc_x8ikazN-bfe9vBTBpH0unyhxA_szK3lkY6CLlz25Kgts_YW05nWTj2L0ii1ctVm0PAVrfsL7tshREpEF9lejn6Qr5yAAN0R_CUR8NZaGJYBRuIDNvvT2DfRtsSNDhjXXF4PAYcgKWbrUn3pjQxyem43CD0hMyQoapPo8hWEIAa1vfEWSa4nawEOFoA8qkgUGqLNXfCVOa61X9XQBK-9JS2lkNYLenJC7Uxyk6s7VxwAUvM8sgjP_kgNpOtbLjv9eqFwv-8nsD-2p5ScDPDyITH9o5uKull8ZovGNp_ydg1lUYQDu1SPKXxEOQboaeBpoUnUoY7FWT7fNTThylPS_ItqZuBMzWZus69I-VOZ_rX8eQ4raZ2-35nlpDUpvhPF9ApPFVXCfYyScGoYkH5_6leMrTeN1GuIczPNywxwidj2YjFmyHBEZJZi6F__gwNijVyLMlP67CIAsETF2Il3vUSwU7vRQUxlTNiCeHTttSABqVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز عملیات احداث برج مراقبت و باند پروازی فرودگاه قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/459013" target="_blank">📅 17:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
یمن تصاویر حمله به مزدوران سعودی را منتشر کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/459012" target="_blank">📅 17:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
رگبار باران قبل از پاییز به تبریز رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/459011" target="_blank">📅 17:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W33E_zqRfutswT6t_IVFOvr4gUzEcjUJXYU9_EQT3Z-d4gF1fDLJlyAYdDjFtYRcTU6zHIUN3zjQQynhaxZeiwjp7Vkme_nXQ69DXaURces54hndF7cW9fYCgbmrNihhFRUE-WRAzuBDs6YVvJOhc5YUyzJdQzhV-ucjJnWTnbRRsVcPsh1oraYz2x0DQ8iFd8CHY22zgyVAzg5gG5QW0xHbBrg3oHbyxEbhf99Tgzm_0Fm5GnaqDNA_f-nG-1U0y5TolINxY5RxIJhme6MFwsGI32EaOc9iqXog98X5igjeu13d3ZIHjaKDMK7CwRn70RKiVLKUIkVWBB07nxwAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان برای شرکت در اجلاس شانگهای فردا به قرقیزستان می‌رود
🔹
روابط عمومی دفتر رئیس‌جمهور از سفر رئیس‌جمهور به بیشکک پایتخت قرقیزستان برای حضور در اجلاس سازمان همکاری شانگهای خبر داد.
🔸
بیست و ششمین اجلاس سران کشورهای سازمان همکاری شانگهای نهم و دهم شهریور امسال در قرقیزستان، رئیس دوره‌ای این سازمان برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/459010" target="_blank">📅 17:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برگزاری مراسم یادبود اغتشاشگران دی‌‌ماه در مسابقۀ پرورش‌اندام
🔹
در حاشیۀ رقابت‌های پرورش اندام قهرمانی کشور در اصفهان و در سایۀ بی‌توجهی یا اقدام عمدی برگزارکنندگان، مراسمی در ارتباط با یکی از اغتشاشگران ۱۸ و ۱۹ دی‌ماه سال گذشته برگزار شد.
🔹
اغتشاشاتی که به‌عنوان…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/459009" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQAZ_yZuJmGMwp-JIg-Sx7KANEqxosyC3WAYmpc4bm8oxBRDJHTr1aueDQ3SwO00JErQEZWONN3JL0pYCg1BpJN9gCKC-x9lxCeKw8SYwbKYESxxqBJ0OgYt6RJHOQ26rX1MuYZENgXPym6UWlySW4PocydRJ9pLZ5iLWN-5J7e9Z0ZfqdqIH4qTs1k0X73OakYc2DSmw4vwxlS2sXR-dyUReeLO1I0ZDq4HoH_t0OSNOMusDz6aW-W50uxCGH4Gutc9FIYeAmCzDJvU2HFGBwY9oQ4EERIWsFusZJGXTsxAe6Vq0OB33X9wVruRYDLYuK7c-Az1B9Z3uTYiUzwVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار صریح ایران به صهیونیست‌ها درباره جنوب لبنان
🔹
پایگاه خبری «یونیوز» گزارش داد که ایران به رژیم صهیونیستی نسبت به گسترش عملیات نظامی در جنوب لبنان هشدار داده و به صراحت اعلام کرده که این امر موجب حملات موشکی وسیع ایران به فرودگاه‌ها و پادگان‌های این رژیم در شمال اراضی اشغالی خواهد شد.
🔹
بر این اساس، ایران در هشدارهای خود تصریح کرد که به واشنگتن اجازه نخواهد داد بند نخست یادداشت تفاهم درخصوص پایان جنگ در لبنان یعنی پایان اشغالگری و عقب‌نشینی صهیونیست‌ها را زیر پای بگذارد و این بند حتی در صورت نقض آن از سوی آمریکا، پابرجا خواهد ماند و ایران در مواضع خود در حمایت از مقاومت مردم لبنان ثابت قدم است و اسرائیل هیچ گزینه‌ای جز عقب‌نشینی پیش روی ندارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459008" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05793a0591.mp4?token=rp8vguqETW-GUSVIu6dn4rVtoT5YVAjFPgWXaurZxHys_NqIxgWqHvlVU1U1wnhi7v6-FzQoSbk1nzjpHsyrhyX2e62Z9cYHL2C64IN_TAhXald54SV7lVGnb0WLvJLTjZ2NXDtQDgHJY4kxfrPRHR5fCnBzdkvEot2DZEBJVPyL6rHz-Ln5xrbFf2QO6DHFvu7CL-xCGiA7bP993KjHpatlZmPFbVY99kWqGNGx4M4rKU8p6UuizDQqqmSUm3L-cZvGD1k1lRUMH51QcnuCG9TvD7wfNJjZaKAIOETIV0kjgyE_5lRpAOyYX1UkdxloNHzQrVGzBWLmd9v_WnCQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05793a0591.mp4?token=rp8vguqETW-GUSVIu6dn4rVtoT5YVAjFPgWXaurZxHys_NqIxgWqHvlVU1U1wnhi7v6-FzQoSbk1nzjpHsyrhyX2e62Z9cYHL2C64IN_TAhXald54SV7lVGnb0WLvJLTjZ2NXDtQDgHJY4kxfrPRHR5fCnBzdkvEot2DZEBJVPyL6rHz-Ln5xrbFf2QO6DHFvu7CL-xCGiA7bP993KjHpatlZmPFbVY99kWqGNGx4M4rKU8p6UuizDQqqmSUm3L-cZvGD1k1lRUMH51QcnuCG9TvD7wfNJjZaKAIOETIV0kjgyE_5lRpAOyYX1UkdxloNHzQrVGzBWLmd9v_WnCQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار همتی: اصلاح سیاست‌های ارزی از ۱۵ دی سال گذشته باعث افزایش ذخایر بانک مرکزی شد
🔹
اهمیت این تصمیم باتوجه به شرایط فعلی و فشار حداکثری بیشتر از گذشته مشخص می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/459007" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7_tDixFXGVwxrWrSZ36eGJJqDITS_BeYlMYDPP3tzyUKxrQyycYHXsrqewu1xS1co7ffEV2KkSyNT5E8mkohgzWriH4lT1sEkDwsKVmAkeRvyGeLa9Virym8yUokh-E8FmSjiWV7W88r8g291UehnsF2FHVT3WhnSTqkB4ldeQvFtHB4oAwd9M_V3M1-y-HKJeyMgd8a3t8Jvq9YFM4V-q1LD6Gx9Mh2hh0YisrEmhNaV4LpwugH3d8K1EqUia9r_zG1_CVkOr61CjAm4iWqQ0Lo0pqswg_U0XUwFHltQWSF2DxstC_u7PIYnBfyJYl5VwX1UeT5pQpPlpwfDzGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درپی معاملۀ مفت تنگه هرمز
🔹
تانکرترکرز گزارش داده که میانگین صادرات نفت خام از تنگۀ هرمز در ۷ روز گذشته ۳.۸ میلیون بشکه در روز بوده است.
🔹
این درحالی است که مقامات آمریکایی تلاش می‌کنند با ارائۀ گزارش‌هایی این رقم را بین ۹ تا ۱۰ میلیون بشکه نشان دهند.
🔹
طبق گزارش کوبیسی لتر، برنامۀ عملیات روانی ترامپ با محوریت بزرگ‌نمایی تردد نفت از تنگه هرمز، ۲ هدف «آرام‌کردن بازارهای جهانی» و همچنین «مهیاکردن زمینۀ معامله با ایران» بر سر بازکردن این مسیر راهبردی را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459006" target="_blank">📅 16:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e17753a40.mp4?token=TGDHClZodaoB1oaLkteZuYUO1cfIzPSZHYtcArUnMYq1A-cVtjwcgzNUAzJLpccGNV7BopVZaPAKzHwn4QAV-kDT6mo8BHociqaJYOmeCDsCJ8nIYLGVIHvJS8IbBRhLb9xlawD8UNqs4o4QVZtB5p8r66FqIZKBlCGp7wBOGc1CQ0zytXpHjp4wOD_PawJ8c5OA9iZB6_28kwXLdgz0JSuPNXtDYb2WW_DPo7G41OZ7a3V8lly_TGqiZxWgKaqbJbDWXb5xEVRCwiSneAKTV3vSu53FflMP80xUnuqdh6RMff6s7AMc_K0BIda49_4_V2wT5emPPpqVLmkzILyd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e17753a40.mp4?token=TGDHClZodaoB1oaLkteZuYUO1cfIzPSZHYtcArUnMYq1A-cVtjwcgzNUAzJLpccGNV7BopVZaPAKzHwn4QAV-kDT6mo8BHociqaJYOmeCDsCJ8nIYLGVIHvJS8IbBRhLb9xlawD8UNqs4o4QVZtB5p8r66FqIZKBlCGp7wBOGc1CQ0zytXpHjp4wOD_PawJ8c5OA9iZB6_28kwXLdgz0JSuPNXtDYb2WW_DPo7G41OZ7a3V8lly_TGqiZxWgKaqbJbDWXb5xEVRCwiSneAKTV3vSu53FflMP80xUnuqdh6RMff6s7AMc_K0BIda49_4_V2wT5emPPpqVLmkzILyd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلسکوپ رومن ناسا به فضا پرتاب شد
🔹
تلسکوپ فضایی پیشرفته «نانسی رومن» ناسا، با موفقیت توسط موشک «فالکون هوی» اسپیس‌ایکس به فضا پرتاب شد.
🔹
ناسا پیش از این اعلام کرده بود که امیدوار است از این موشک برای مطالعه بیش از ۲ میلیارد کهکشان استفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/459005" target="_blank">📅 15:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ_80P18ectUZySTc-RoidL8jIT6VSuHH8AHyVo0YLAmqHCtanE6jm3PY-oTzaE7Zb6Ku2dRH_u5RPeuW-rqRK92im5naePSDZlIA0OoN7wPgHq9Rg71p3X1g4iDKkhKKr9X_6wobd6zZUbe_RsPfM0VskAbg3OpuCmSe_anfhHPTPkRI432nQLlxgHh8p44LW_vbsgIvSko8yx6oMqdnxzuwvFrXNShPM12AisGsm8PjTwYtFdLGs3mb0DpVLtl06vExNNvQe99aRmTsHcx-TF9iU0MGmMe6EhSg2b_hn83fmfh29ozYIYi9V_kqYJAsMx7kgcVaOaisVgeAMBq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد قیمت بنزین در سرزمین‌های اشغالی شکست
🔹
وزارت انرژی رژیم صهیونیستی از افزایش قیمت بنزین در سرزمین‌های اشغالی از ابتدای ماه سپتامبر خبر داد.
🔹
براساس نرخ جدید قیمت هر لیتر بنزین به ۸.۲۵ شکل معادل ۲.۲۷ دلار خواهد رسید؛ این بالاترین قیمت بنزین در سرزمین‌های اشغالی در ۱۴ سال گذشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/459004" target="_blank">📅 15:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d91d7afef.mp4?token=pSGRCgVZb1-F0UmKcLv_0rKi3DM7nDpKP3HG8vM2GaKrsNprl6QC3nurAizGrFeZjQ9VAOfOXX5K0KKsIPM40r6GCnHvJvVAhAdNw-RcA_FfGNr37dqC0Ljn_0UCK6gd_A7w7BduwVq6dpskedpo37sHS5c9S3Dz12PBn9TT7ApEc1-5d1mEUB_9B7iEA07YgVYsHxEhtqyvUq_xte8aFTPBA444I3t6lhQg4wK2m9EykmbbRaWByiRNi8aDuvcnUdbwGtW43_10X3egYfs8ENc9GaIdBnfahhQsFbItgkRs98KsQGkBcZ9Hwb3Epue9OSuSDrcAriz_VpMC1OhrPa3zp9k43LuZ6n0_WHdywOgGUhPPrG0u8iO0bHQJIY4TcfcTDXD7U1rJ8QKqLzggaLWhoPnUdfdQhovwDOsps1_0-90hSPABWk2rZ8akZkfJrTJMlUMO6puMqD89TZGtpPo3qSG1MxDSDkx8bnBtQMi6vlOmHCRyBLT1QdyWABaIzx80ghsLORzQovke_--KzGmyHyLSPodMlH18XKVjT0N0hr2mL2jlTfQ7vCk6UfHYNDPWmQ_QcjtzCSbRR1rEeDnkKUevx-a--4pD0dL5DWQN8QD0QsF2s5zYWsbn2upO8RpaNME_1Zkv4q5_1J7JG_OAzgvAqzSXanHFZF3u9E0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d91d7afef.mp4?token=pSGRCgVZb1-F0UmKcLv_0rKi3DM7nDpKP3HG8vM2GaKrsNprl6QC3nurAizGrFeZjQ9VAOfOXX5K0KKsIPM40r6GCnHvJvVAhAdNw-RcA_FfGNr37dqC0Ljn_0UCK6gd_A7w7BduwVq6dpskedpo37sHS5c9S3Dz12PBn9TT7ApEc1-5d1mEUB_9B7iEA07YgVYsHxEhtqyvUq_xte8aFTPBA444I3t6lhQg4wK2m9EykmbbRaWByiRNi8aDuvcnUdbwGtW43_10X3egYfs8ENc9GaIdBnfahhQsFbItgkRs98KsQGkBcZ9Hwb3Epue9OSuSDrcAriz_VpMC1OhrPa3zp9k43LuZ6n0_WHdywOgGUhPPrG0u8iO0bHQJIY4TcfcTDXD7U1rJ8QKqLzggaLWhoPnUdfdQhovwDOsps1_0-90hSPABWk2rZ8akZkfJrTJMlUMO6puMqD89TZGtpPo3qSG1MxDSDkx8bnBtQMi6vlOmHCRyBLT1QdyWABaIzx80ghsLORzQovke_--KzGmyHyLSPodMlH18XKVjT0N0hr2mL2jlTfQ7vCk6UfHYNDPWmQ_QcjtzCSbRR1rEeDnkKUevx-a--4pD0dL5DWQN8QD0QsF2s5zYWsbn2upO8RpaNME_1Zkv4q5_1J7JG_OAzgvAqzSXanHFZF3u9E0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضری برای ایران بجنگی؟
مقایسه جالب «عشق به ایران» در بین سلطنت‌طلبان و مردم کشورهای منطقه
ساعت‌ها می‌توان درباره این ۳ دقیقه تامل و گفتگو کرد، پاسخ‌هایی که باید در تاریخ ایران ثبت شوند.
@Fars_plus</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/459003" target="_blank">📅 14:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVuddbfvAfkAi6d3M1pXebdaLEjDYDiA3HQ6FlWTcW_3gorXzOHRN0dhbbJqwBCAyodBmanIMHnfp99EV8Du9V2Fvz4QZ6b02vmIHlJrzxXLDVFhFDKcEmLkgWEnRh_99tBXQzs4cwAOC1yIOuw0_FgoHlXf6vSaCyxI4wkNxFfXmdSrH37GcVOt6WrD6RI4_mE7SdHKHPGoJwYFqBEI_clwf2n2yNj11FC23ZRw4xk06rAF6qN8pUyWFDvfYgWt5WyWxn3lKNDcW8yUzA7-IYgH1O5ugyg9855uGjS_0tpOgVLDWZSS7SCWLuQVK2uNfzU52uTWNKmhh6kF3X2CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، پاکستان و عربستان گردهم می‌آیند
🔹
مقامات ارشد ترکیه، عربستان سعودی و پاکستان قرار است دوشنبه در استانبول گرد هم بیایند تا نخستین نشست توافق دفاعی مکه را برگزار کنند.
🔹
یک منبع وزارت خارجه ترکیه با اعلام این خبر گفت وزیران خارجه و دفاع و همچنین رؤسای ستاد نیروهای مسلح ۳ کشور در این نشست حضور خواهند داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/459001" target="_blank">📅 14:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2ZOkahBN8cc22NVhCYHN4acbG2ZeC2kCKyaDJHgiAlp3mHdprMDpzAWr3N3Z_znt9VdIcm6TJsehOVxcD5JwE9No8pzSjdt_JGZgI6LYclr2ZCz-efPLbJKLQIcqn89lBx12mjX6kpY81fxILBnp3DV2DSwlBAHKfjHhqwgyoWL0lMdX5kuZBxPhdaLiKUqgSH3hZ0QwO1WA_HY8v4qVYgqgO6nmSn5jULcXCpkYVrYPc7e1pt7iJQykC8MC3IobrdvIMWfXEcUEOTXyQLNxrD4kXHa8F5R5Tu6Iwx7pFCl-s1BovrMMKSQCkwBklX_4F02bSFX97ZuakznajzCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RIx40xQb_BZRydkyCa1PRwC4MA4eH5SmNav2cZraB7noKChvpp7we4VQUnmKRwzvmv-gKl_G-ovmxj7Y9ip8q13zsYeI9I3rU9CQFIijk-i9dTwl5TzZbPI_mwr51mLzSgLimDYDmphSa4sZCiK5Rp2c9Lq8Ta8s2xvyvZEw1YaQAxK1NQGw9vWMKsoB416HM99qyuJcSSjFST6mAG1J6SxbGDemOP2dTR-JSX-53xO2mhH4CAO3rPLClu-TpWe5MujdDMxKz3muiNCL17S1R3AoDiV1yUjPpywFqtlMOzqnW5Lpxl5urTDC0CfGxWe4XlvbVguZFSkw98FkdqGloA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست‌خط شهید لاریجانی پیرامون مقام شهادت
حدیث اول
🔹
پیامبر(ص): هیچ قطره‌ای در مقیاس حقیقت و در نزد خداوند، از قطرۀ خونی که در راه خدا ریخته شود، بهتر نیست.
حدیث دوم
🔹
رسول خدا(ص): بالادست بر هر نیکوکاری، نیکوکاری دیگر است، تا آنگه که در راه خدا شهید شود، همینکه در راه خدا شهید شد، دیگر بالا دست ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/458999" target="_blank">📅 14:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7B1KEwKzV_M7Tk6hsc1WQa_G_KZvuy_PIbsOfY7s7lZ4vZVJ1ovb8TLH1-ClzX8SaHWrdx6nTFJxtyM8PXytL4RkqZ0ijbTvv59XzQLxHDHWEz8yk8627bWcdTTnmPuolC_rj2mzgAQzUNEmkTPCKtfdaISO4DIsW_sf741-2Mw9tKkIgnEKmdoBOJtHkdJPcjHozuH3NmGAITNu348kP4BwuYu7hSwIjHqPWWzUgsi8_TidNe20E8wW7abii5CymIJFk23lhSlqBZeEBrFYqSyFzxWN1eQsphCx-aBkvfw7EVN-wTx7eshYmjPJxdOTgbr5ArHftkjBdqg1Wnalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریادار ایرانی: نیروی دریایی ایران مقتدرانه از مردم دفاع می‌کند
🔹
فرماندۀ نیروی دریایی ارتش: امروز نیروی دریایی زنده، پویا و مقتدر ایستاده و کارکنان آن با همان روحیه‌ای که شهدا داشتند، مأموریت‌های خود را دنبال می‌کنند و از مردم دفاع می‌کند.
🔹
دشمن در شناخت روحیۀ ملت ایران و نیروهای مسلح جمهوری اسلامی ایران دچار اشتباه محاسباتی است.
🔹
پرچمی که شهدا به دست ما سپرده‌اند، باید با قدرت، عزت و سربلندی حفظ شود و به نسل‌های آینده انتقال یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458998" target="_blank">📅 14:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یمن: عربستان در ورود داروها کارشکنی می‌کند
🔹
وزارت خارجه یمن: رژیم سعودی طی ۱۲ سال گذشته، از طریق نهادهایی با مأموریت بشردوستانه، از پرونده انسانی به عنوان برگ فشار استفاده کرده است.
🔹
نهادی که سازمان بشردوستانه فعال در یمن نامیده می‌شود، در پاسخ به فشارهای سعودی‌ها از واردات داروها و در رأس آن‌ها داروهای بیهوشی خودداری می‌کنند.
🔹
صنعا در برابر هیچ فشاری سر خم نخواهد کرد و نبرد خود را تا بازپس‌گیری حقوق مشروعش ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/458997" target="_blank">📅 14:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76a09f6a8.mp4?token=B-WBl1TeZEIGnrcsA2Dn8xvhi3HRKzJM3M5u3SPppTjrciIZUSOuNBKAluTphKjU47hSS0iXgOuyC88v0CETigVtAASZYYfq-wOeiL_gh8AJh2A7bZqk6c70SQGFhr4reHSPIIgTTDpKD-DjZCJcfnJFrvpvbq-JXlNH6SnXOfu6RkqeRS07Ymb74V8BGgO5DclOIUFjHWrMdxmT7vjl4qWY1Pa7J-bQwrokqaJTcFYLqWI2eY_Uzh31hlAQ0U4L57Uxgy7mtGvOU-lLn40nV8dKhWivWbYuHKFzvb6x7eTOA_OVZldLezFtl-H2RVr7ef6juEBIa1mJaoZ9oF0tWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76a09f6a8.mp4?token=B-WBl1TeZEIGnrcsA2Dn8xvhi3HRKzJM3M5u3SPppTjrciIZUSOuNBKAluTphKjU47hSS0iXgOuyC88v0CETigVtAASZYYfq-wOeiL_gh8AJh2A7bZqk6c70SQGFhr4reHSPIIgTTDpKD-DjZCJcfnJFrvpvbq-JXlNH6SnXOfu6RkqeRS07Ymb74V8BGgO5DclOIUFjHWrMdxmT7vjl4qWY1Pa7J-bQwrokqaJTcFYLqWI2eY_Uzh31hlAQ0U4L57Uxgy7mtGvOU-lLn40nV8dKhWivWbYuHKFzvb6x7eTOA_OVZldLezFtl-H2RVr7ef6juEBIa1mJaoZ9oF0tWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای پارس جنوبی چگونه پس‌از حمله مانع اختلال در شبکۀ گاز کشور شدند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458995" target="_blank">📅 13:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ad1e6014.mp4?token=N9LTiEHJLT4-V_tMO4OuNtqLEweduEdhkkjGaB--gwdAl1eWQ7eChQMCwa6CljFRiQ71Wb9GVqCAqm8vKLXepLmgGUmR7s3mcvSJJzeO_RgsGck6V9gmF1kaBQaazlQ2j38vIAp4H9v0a3oOUJBxP-0tXYN4oXNhjnZRgdIq1F_o5Md3ifwBCFi1D60sxvI4PjxRVWSA2KqfvTEB7vcVQiYVoP9M3-QQzgMnPPkgAFuWJWN9oJEVXoRon-lbcFjxoNlfq_Bkyk5m2FYlEyyr7g9XKHXUeRv9QCgM4fGv-s-tLjnApFmKYcBMS_MZ5tyrntuIa0Ivov3J3JD19uW3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ad1e6014.mp4?token=N9LTiEHJLT4-V_tMO4OuNtqLEweduEdhkkjGaB--gwdAl1eWQ7eChQMCwa6CljFRiQ71Wb9GVqCAqm8vKLXepLmgGUmR7s3mcvSJJzeO_RgsGck6V9gmF1kaBQaazlQ2j38vIAp4H9v0a3oOUJBxP-0tXYN4oXNhjnZRgdIq1F_o5Md3ifwBCFi1D60sxvI4PjxRVWSA2KqfvTEB7vcVQiYVoP9M3-QQzgMnPPkgAFuWJWN9oJEVXoRon-lbcFjxoNlfq_Bkyk5m2FYlEyyr7g9XKHXUeRv9QCgM4fGv-s-tLjnApFmKYcBMS_MZ5tyrntuIa0Ivov3J3JD19uW3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه: ۲ روستای دیگر را در جنگ با اوکراین تصرف کردیم
🔹
وزارت دفاع روسیه با انتشار ویدیویی اعلام کرد «۲ روستا در منطقۀ دونتسک را از وجود نیروهای مسلح اوکراین پاکسازی کردیم».
🔸
وزارت دفاع روسیه وز گذشته نیز از تصرف ۳ روستای دیگر در جنگ با اوکراین خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458994" target="_blank">📅 13:22 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D97W8vTD9JENSGxDLUJaUfZNQkjYO7GR4OsJVQDKMigcDU9Ct0MVuQxmpAQK5zc7SeoxYgQ3t_UC5ehil6lRUz1FS8KSjg9OZbmG-jds0Ut2_rw0hoqDmDb8qMdRkrj0toIwlAGlqrmBBNTX2bJHjfx_Y4_pCiY8DpBkSic1KnpQhSSd5ri54WvBloX-D0FiqLCgGAPG29V4DMWaqmXI52aU43Et8poRABf5-YvylySA4HzKOZ_HiwadmAAHyc-mAPHL_ASbqeB3ktDjckz2vjPnzlg9lyXqxjFnwcqXBV-R6JJbNDw5Rl5fwYv7ZrmqwigUcQHuKWox7gUxsbWaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ نوجوان اسرائیلی به اتهام جاسوسی برای ایران محاکمه شدند
🔹
دادستانی اسرائیل امروز علیه ۲ نوجوان ۱۴ و ۱۶ ساله از استان حیفا به اتهام انجام مأموریت‌های مختلف برای یک عامل مرتبط با ایران، کیفرخواست صادر کرد.
🔹
روزنامه یدیعوت آحارانوت مدعی شده این ۲ نوجوان در ازای دریافت پول فعالیت‌هایی ازجمله تصویربرداری از اماکن مختلف، نوشتن شعارهای گرافیتی و جذب نوجوانان دیگر برای انجام مأموریت‌های مشابه را انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458993" target="_blank">📅 13:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458992">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAToLCjkMS2AYrCFGIjDSgf0-e4ZiK9H96ZKmjSv7BSIdZUO22evaE1hGw3mB7BGAI2lH9Bm7iYPOAJk20EHZWfhKuQkF-pmlzg06BoEZ3I7og-xtq11viDZMfSZsy9UNL3qEBUBUQpOFNEjuqj326rEQlc-p3DjuegVW4_bbcWbjsb-aGa7qxH9_ZHY8H6kNWjjCwfhhnsB5HXiUb1vUn0pxYA0YpSE8PgbhAH7mEkk4ixmf_PWBzHc8WAlGutaovjpCjj_mSKZaYr6hdHJBL8nFzDjK4w-bIhui-OFeYHCxmVlEND2BiuCJuMpij9Z2z_N5pRztXx-ySxk6H5Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز امور اتباع: جمعیت اتباع خارجی به زیر ۵ میلیون نفر رسید
🔹
در طول یک سال گذشته نزدیک به ۱.۸ میلیون نفر از اتباع غیرمجاز از کشور خارج شده‌اند.
🔹
جمعیت دانش‌آموزان اتباع خارجی هم از ۶۰۰ هزار نفر به ۳۲۰ هزار نفر رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458992" target="_blank">📅 12:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار و فعالیت های کمیته امداد خراسان شمالی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0a387ad6.mp4?token=rygKSAVzzkPgwAiqHhddLG4cWfCu3NDKyRta_fsqyvEQRU-LpT7BY2uAYnTCqTeM0CrbalDvUngoNpSKDiSG5TpRxajYuP65bmADWzi7RsY4BmwMBXiFSbEG8_sauRoaXozK237JX5pVog86LM2l3-eK9E-y5wOWemmtNpw5QooXu8rADNV_SKERog_k9L9aHhtlbxkAxwlD-X9Fv84ANd3-q2Pf-3p9ddTge1V3cOhrXoEFFJQBrbM6EiZzWo0DCJc-tXCSuowbG6yCZsu54ezju-RIs8FVMV07PLgdYaR1PtCpuekGDqC3g0oS3hR5k68AovteU9nh1I10qGBvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0a387ad6.mp4?token=rygKSAVzzkPgwAiqHhddLG4cWfCu3NDKyRta_fsqyvEQRU-LpT7BY2uAYnTCqTeM0CrbalDvUngoNpSKDiSG5TpRxajYuP65bmADWzi7RsY4BmwMBXiFSbEG8_sauRoaXozK237JX5pVog86LM2l3-eK9E-y5wOWemmtNpw5QooXu8rADNV_SKERog_k9L9aHhtlbxkAxwlD-X9Fv84ANd3-q2Pf-3p9ddTge1V3cOhrXoEFFJQBrbM6EiZzWo0DCJc-tXCSuowbG6yCZsu54ezju-RIs8FVMV07PLgdYaR1PtCpuekGDqC3g0oS3hR5k68AovteU9nh1I10qGBvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
افتتاحیه کشوری در خراسان شمالی با حضور جناب آقای سید مرتضی بختیاری رئیس کمیته امداد امام خمینی(ره) کشور
@khnemdad</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/458990" target="_blank">📅 12:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458989" target="_blank">📅 12:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3a5b28.mp4?token=QKSyKs7dqKCAHp156qPQFUPGM_vxFdsASmNlrozmeAABEluCb2LXAex0YA5936Md1KiLuKzB0NNz695vMvrK8Yh9SPYWprq_y7Wpx74vTRpFqfUwXYD4RhlaX4361XJjFTO-dFpqc-M_W5KoHZy7-TI4cDPogspTfUXRrRRAY4zEGCCZMEeYvq-LBto_wmQT9Gxbt7svhKEDmWPVJ4BT43Ww13gteYs4yrYPf9nYpNa0DZGEB6ozD-GfDxdSualXkft7SnZVgOCaLtbS-MZWGg7n4Hmw24iT6Wwv2YaJG5j0UpdH3hwGt4e_-gIFWKnxLNPeAlVdWRnR84nvdT-oWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3a5b28.mp4?token=QKSyKs7dqKCAHp156qPQFUPGM_vxFdsASmNlrozmeAABEluCb2LXAex0YA5936Md1KiLuKzB0NNz695vMvrK8Yh9SPYWprq_y7Wpx74vTRpFqfUwXYD4RhlaX4361XJjFTO-dFpqc-M_W5KoHZy7-TI4cDPogspTfUXRrRRAY4zEGCCZMEeYvq-LBto_wmQT9Gxbt7svhKEDmWPVJ4BT43Ww13gteYs4yrYPf9nYpNa0DZGEB6ozD-GfDxdSualXkft7SnZVgOCaLtbS-MZWGg7n4Hmw24iT6Wwv2YaJG5j0UpdH3hwGt4e_-gIFWKnxLNPeAlVdWRnR84nvdT-oWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلر تیم ملی آرژانتین به چلسی پیوست
⚽️
امیلیانو مارتینز، دروازه‌بان ۳۳ سالۀ تیم ملی آرژانتین و باشگاه استون‌ویلا که سابقۀ قهرمانی جام‌جهانی را هم در کارنامۀ خود دارد به چلسی پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458988" target="_blank">📅 12:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amyg5t4fmPUqaVkqLwKVV5WqUd95KYSPgW_L5tf_nUPtrCh3GlQbI4vgLRzJRH9FmmGVB5JpWnxh3W5oBoTeK9MZULt4FWipgQgZ1yBvXy6hKBG3Xi_3aleTUNQmPpHaHgDoLBiMYhs6xJbpyMWnO0P_8dGVJFnVp0b4NubpFZC40_08VBvhg5_qc0qsuGseG0worZA50Wh5EBIWKIbsuv9f3sb2DjGaJtq4kpDt_peariRy97WlrEqG2DgMEZ-bjeXebXlCPBZJkYNrZd71-mx9iq5_D_5Aiaklbj5uZ8kWGRY0swWnh4NvPVCqouxMDBuM01SsqoZDHyCHrRr7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: مردم ژاپن دولت خود را دربارۀ مشارکت در جنایات آمریکا پاسخگو کنند
🔹
وزیر خارجه در واکنش به گزارش‌هایی دربارۀ اعزام جنگنده‌های اف۱۶ آمریکا از پایگاه میساوا در ژاپن به خاورمیانه برای حمله به ایران گفت: مردم ژاپن دولت خود را دربارۀ مشارکت در جنایات آمریکا پاسخگو کنند.
🔹
دولت ژاپن در قبال استفاده از امکانات مستقر در این کشور مسئولیت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458987" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438a8cbf8c.mp4?token=D0Mji4m51LuwsH83lf4M8a9XKhKEcQS7kjn1u3DfJ6iE2xm4LKMmWTe2WxC6hMfRIkyh7XJ3gsTP_5cu36dN9ES-f9crRMikHH4c9ld1ORikcPtLFGIVupG7jLE9l_uxaYcaMKp0dubRMW1VzyQMsXqAuzbinSV9hoG-CN79BIVNgkpXw9rrI41LBUUjqIw-QFiRpsw5krX9CJyIoXWG3G-cTg-KCzjOFDCPEEmqS1lw1YGQDT-IF0omdvhwOjgfw7pSbmpgYjrbG6ed45xCge9I2SuR_S8TRC_BZwYwrdzU74eGxrQycfrZEoS64c8uoavr_ZPW6TFLu15QeGYesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438a8cbf8c.mp4?token=D0Mji4m51LuwsH83lf4M8a9XKhKEcQS7kjn1u3DfJ6iE2xm4LKMmWTe2WxC6hMfRIkyh7XJ3gsTP_5cu36dN9ES-f9crRMikHH4c9ld1ORikcPtLFGIVupG7jLE9l_uxaYcaMKp0dubRMW1VzyQMsXqAuzbinSV9hoG-CN79BIVNgkpXw9rrI41LBUUjqIw-QFiRpsw5krX9CJyIoXWG3G-cTg-KCzjOFDCPEEmqS1lw1YGQDT-IF0omdvhwOjgfw7pSbmpgYjrbG6ed45xCge9I2SuR_S8TRC_BZwYwrdzU74eGxrQycfrZEoS64c8uoavr_ZPW6TFLu15QeGYesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بن‌گویر اسرای زن فلسطینی را تهدید کرد
🔹
در ویدیوی جدیدی که از بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی منتشر شده، او درحال تهدید کردن اسرای زن فلسطینی دیده می‌شود و با افتخار از اقدامات سرکوبگرانه که علیه اسرا سخن می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458986" target="_blank">📅 10:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e606af461.mp4?token=aFp44OpZzsp_qvuK4vt31zVN10fIjwnxTwroXW6OsrIgqVfWnChOZnbqOKxiEEfYlJleeasD5UC5MhkNh21SU7HVqAhUlvBRmhUyKL6YUw7e6aumBgXokOWgEV70QbFsHVbnlP5YH3rAJF4GMVb4LGYJZvQvncbTKmtZiqxzOVhK9-72SIU1-PlGmP5Lx0VSjDLZFHFKaA6wWG3m71XSwiyeuO-cLOgIfvY6AuFwIkbmcZRuhOXFLVLqRVKrjRIx5OjInts7tQpocX-RRzDC3-ycO64azyhkTYD0EUAAs0uKZkuhZej5cN8iG1t5rDwwPP5PVYUEswFTMggHl87O9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e606af461.mp4?token=aFp44OpZzsp_qvuK4vt31zVN10fIjwnxTwroXW6OsrIgqVfWnChOZnbqOKxiEEfYlJleeasD5UC5MhkNh21SU7HVqAhUlvBRmhUyKL6YUw7e6aumBgXokOWgEV70QbFsHVbnlP5YH3rAJF4GMVb4LGYJZvQvncbTKmtZiqxzOVhK9-72SIU1-PlGmP5Lx0VSjDLZFHFKaA6wWG3m71XSwiyeuO-cLOgIfvY6AuFwIkbmcZRuhOXFLVLqRVKrjRIx5OjInts7tQpocX-RRzDC3-ycO64azyhkTYD0EUAAs0uKZkuhZej5cN8iG1t5rDwwPP5PVYUEswFTMggHl87O9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک کشته و ۵ زخمی در حادثۀ تیراندازی در سوئیس
🔹
رسانه‌های سوئیسی صبح امروز از وقوع خشونت مسلحانه و تیراندازی در یک مهمانی در شهر آرائوی سوئیس خبر دادند.
🔹
پلیس این شهر شمالی سوئیس  گفته که در این تیراندازی یک نفر کشته و ۵ نفر دیگر زخمی شده‌اند و تحقیقات دربارۀ انگیزۀ این تیراندازی همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/458985" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8d66fee.mp4?token=jxo9Xdc8FDbjJg4UOFsOjvTSnXYE29DgoG4t_9Gb_wtbgqddfV7p6bBTp1KzLwFfwFjzA7xHNm2RIu3Gfy8SmNBrAGhUVQaLP4SqhbPzLGvk70UubLpO0teWlCYs1A3HzWVayq36s9nJd-ppb5Crxv75MzOYBwuA0PVQz6q8XqIF4qtPZY5TJm6UpNPfIo5bWFgseGHKI4y-LwVCZQ6mhnXSs8HWd1lD_t79Zr65_O_hQ5iQDbOwBsFxL6h-gEkxeJ41GO7qskD0wH0JhGDdgvUjdyaRmoqUibDY1moU-9hQY5jgkscR3M82mSrqvQG7H8djOd7tLkRjwbgXWAAVXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8d66fee.mp4?token=jxo9Xdc8FDbjJg4UOFsOjvTSnXYE29DgoG4t_9Gb_wtbgqddfV7p6bBTp1KzLwFfwFjzA7xHNm2RIu3Gfy8SmNBrAGhUVQaLP4SqhbPzLGvk70UubLpO0teWlCYs1A3HzWVayq36s9nJd-ppb5Crxv75MzOYBwuA0PVQz6q8XqIF4qtPZY5TJm6UpNPfIo5bWFgseGHKI4y-LwVCZQ6mhnXSs8HWd1lD_t79Zr65_O_hQ5iQDbOwBsFxL6h-gEkxeJ41GO7qskD0wH0JhGDdgvUjdyaRmoqUibDY1moU-9hQY5jgkscR3M82mSrqvQG7H8djOd7tLkRjwbgXWAAVXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش شمار قربانیان سیلاب مرگبار در نپال
🔹
پلیس نپال از افزایش شمار قربانیان رانش زمین و سیلاب مرگبار در این کشور به ۶۱۶ کشته و ۲۳۰۰ مجروح خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458984" target="_blank">📅 10:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgCam3O9Jadz9vUMevzp8LovPB_gfrZdHoq2jBVYPkWKF4qB5ym-8s4Vigw5R5fZPcs1R5ddzVd4YRH6y7cQp09wU2NKeg4ZZFsXjrYf_mXs_lxWDlDPt7x0DZYos3zhNTRCOunPoJExfPtmEcaWzME9mKRP2MiF7Z6jCuaCL8hQb7obcK6-uHFXw2vMn6I730oU8LZa9kK7GbYmEUec82UoWnFfMzi88xkBo7tj0TsC7OckMigSMgmcPzNgMn_WQkbbSTXEIaOJ63t_OcpMFQuoSmS7_UCGc886AVwMT4wtB8LkolXKgj5y4tY4TZyxPu4I3KRin-6Fuk5N9geN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسران من را ترور کند
🔹
نخست‌وزیر رژیم صهیونیستی در گفت‌وگو با شبکۀ ۱۴ اسرائیل: ایران تلاش کرد تا یکی از فرزندان من را ترور کند، این نشان می‌دهد که محافظت از آن‌ها تجملاتی نیست. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458983" target="_blank">📅 09:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBeFf5srR6-IaA9bqGXFATOiQQj4ioLViDMbvzAkD86XkL0zwnrJJm2jsml59BeMvnsbdnZFDpg_WYujmNDoXse-7hUAC79hXHOITUJNT0kmcMhk91VotHfzX0EVnaeKH8ZEfKHX7C-AQftJGRWRDe34BMPQIei7W-LitocNaUs_WhYzMj3nU77drbfEPCwMSO3yIVnzvj4yLAjVZv8PRh2012uyRr3Iy0fpMwD5SaUOVr0k1QxTnZMf5hW9uU3fewNZn2uuaqs_ONWJLEAf032Ck1kFBi7pO6omNyx2ac37lkiindsW63Qu2mRVvRxcoggXfasVMDeaJB2UyCj_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458982" target="_blank">📅 09:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHDX_RgFPuILJa2JgZnaRIIfGXaWaJiKeypBBxO1me3meIqaL5JMR9cbG56oD8uPO_10oyRvqz5d_dj9JNwlHoK_FwORdhLwBZoknxGLgdRm-iCBywPo6tZq9XNffQQ5E99AYKO7YwFOnaLhckY8qNguiIrw3owI5nnU1CC9ihY0veEa05GgAzaDERHOivT0dcQr1kY1TvTP4CEyVebNam1STz3zePcjc_wLJjlA32wUCxiaRyz9R6MfCNu0lGoKdOeM-5mxfIr5fZBVPCLJ8MBuaTEQIV3B_-4EnLmBqwMrVjMPrx5BAj1oWrlVRVuM-JhvnmrigU3X_YKycKhhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: معتقدیم روح پیامبر(ص) مراقب جامعۀ اسلامی هستند
🔹
ما معتقدیم روح مطهّر پیامبر رحمت و همچنین ارواح طیّبه‌ی اوصیاء و حجج طاهرین صلوات‌الله و سلامه ‌علیه ‌و علیهم ‌اجمعین همواره مراقب و هدایتگر و مهربان بر احوال مسلمانان و جامعه‌ی اسلامی هستند.
🔹
آنگاه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458980" target="_blank">📅 09:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clvDKqvf5iA2SGSR1a7WONAM4-z0prSxhfWlAREmsxY4pUJ-QUI9UFaSNWizh6djZBtwXmBEEU9AXnbkohqm4x98dPWAil3zze3MN8TR8aI3tuU9jiVHU6vFyEfSXGP72AGCe_rm0BpHBYc9_lvP0dupfYBJXJmAHYYr17cjzuwjdh5dX_DXiYmsu-xwx0s_KmZ_ySCrDjAbu9UFaOC_9XPK-Wcap2-H4QLdeQdfZm_K2JObqoB1CDH1QNoDoF9NzYvMVUl0bBTQR7Xf59b_3Rd_P2EW56ciri681xGLZmjZSdUM2qNTSlhFkIYnqxqKx-LaKbFFs9I6cK_dKYTYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌رهبر انقلاب: اتّحاد، دفاع متقابل در مقابل کفر و همکاری مسلمانان؛ ۳ گام برای رسیدن به تمدّن نوین اسلامی است
🔹
درس مهمّ اتّحاد و عدم تنازع، درس اوّل مکتب اسلام در مورد نوع مواجهه با دشمن و دوست است. امّا درس دوّم آن، دفاع از یکدیگر در مقابل کفر و درس سوّم،…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458979" target="_blank">📅 09:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ رهبر انقلاب: حاکمان آمریکا و رژیم صهیونی، دشمن همۀ امت اسلامی و حتی حکام این کشورها هستند؛ بکار بردن تعابیر زشت آن‌ها نسبت به بعضی سران کشورهای منطقه در حافظه‌ها موجود است
🔹
حاکمان جنایتکار امریکا و نظام جعلی صهیونی دشمنان قسم خورده این اتّحاد و دوستی هستند.…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/458978" target="_blank">📅 09:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رهبر انقلاب: حکّام کشورهای منطقه دشمن واقعی را بشناسند
🔹
اکنون وقت آن است که مسلمانان به فکر فرو روند و حوادث را دقیق‌تر بنگرند.
🔹
آیا اگر مسلمین یدِ واحده‌ای می‌بودند که مشت خود را با استحکام می‌فشرد، ملّت فلسطین این‌گونه بی‌پناه، مورد ظلم و جنایت اشغالگران…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/458977" target="_blank">📅 09:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFrH-ZdqnGrMS_32vbwEMPfQklYhvGyeTy6cJV5kz5ZEUb-sPu0INNZssB0B9w0Een4vp1bkpqcOtZVKXRjiCZRjh7HQfkGkbPLt6ItCxOWYdL6fyqdnETo8f8D7QZg2XPvKAbMJ5IC9_fKFHsFDofoGbcaBgLouvJP64v2AahxhRcT4k0aYa7BID8ZnOvflicZsoSQvcHu4sca3XaXDviiVd7xwUCI6yEkgsb_F8JMvaNTnA3hPY68npSkcfUCDluThbXkten4Wc0VXcZ93b71zVY5BemS0K_iRRIl9lG389DBHldDX0-XIg0p-Jzp3Pzy2ohMYv6gMzi3dVifzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: هر کاری که به تفرقه بین مسلمانان بینجامد مقصود دشمن را سامان داده
🔹
اختلافات عقیدتی و مذهبی گرچه یک وجه مهم از مقصود دشمن اسلام بشمار میرود و او به استفاده از آن بسیار دل بسته است، ولی به آن بسنده نخواهد کرد و تلاش دارد تا انواع تفاوتهای نژادی،…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/458976" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رهبر انقلاب: بدخواهان در کمین وحدت مسلمین هستند
🔹
زمان برگزاری اوّلین هفته‌ی وحدت به اسفند ۱۳۵۶ هجری شمسی و دوران مبارزه با دستگاه ستم پهلوی برمی‌گردد؛ آنگاه که رهبر عظیم‌الشّأن شهید اعلی‌‌الله مقامه‌الشّریف در دوران تبعید خود در ایرانشهر این فکر را مطرح نموده…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/458975" target="_blank">📅 09:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH_OH7BHexmN0VHpBMB9Kfz9CHSuawpqcIe-WeM1Gj2rYf1yaueq1xXyk5ColH8VdXonn6Hv4jwnlitGk05WzrECBdq1xqXCsp3l9ukRdgO24vctElMnDQ5NdzDM6mTS6mWWnTD9JFAIWOCFHr_uJ8VhhX0eWk1detrymLUTsw4cGZmE2UmqIsT8nGUhMQVlds0S-ZVscgtAbJkmdF2DfBY3Erp81VDjJgNvgdoI8Bpv2GZ_36w488ydn_edRG4dQ66P2hGTPF7S4nKgL47mcdi1968CpIIlbdexZPDA0oqo5ECkpMFfcxfL1Rot09VSk0PIqa1aNPQL3VyXGEsaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: مقصود از وحدت، محور قرار گرفتن نقاط مشترک میان مسلمانان است
🔹
مقصود از وحدت آن است که در سطح عمومیِ جوامع اسلامی، نقاط مشترک بین همگان، محور و اصل قرار گیرد.
🔹
البته سعی می‌شود تا به پشتوانۀ استدلال و در عین رعایت همۀ شئونِ برادری و همراهی و به…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458974" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCIhS1lygxLZM9bT1okurPqo0pA6RoaHwsOWSpXM9cgfJGI8M1aC2oGxF58NfRhkv6dZIklFdhDTuKwGUElMfYD4jcB_gGy6qYZaynwTYvqLYZjwB6i4W26IKRIz84Y8dAo6Eca336kTarypIrEfHl9dmWDCGa7Md64P_WcmuJG2jaZWSCzupObVIvztwCtv6Q92QSRn_xJFthiDaYojCfvzOb-mIbJTkxAYvU2z8-Ok7kxSDkqwvHN46puYFdxPYA26Bws6yaeyElNAQTIcsrTHEHobYfRwiYUDFN0xVWemq7jMDeutfVThMeXMpVVaA3qvgHOZgHzinAMejAFgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: چشم‌انداز غلبۀ نهایی حق بر باطل بیش از گذشته به عینیّت نزدیک شده
🔹
اینک اسلام و اهل آن بعد از گذر از دوران‌های سخت و پرتلاطم و طی‌کردن فراز و نشیب‌های متعدّد از صدر اوّل تاکنون به مرحله‌ای سرنوشت‌ساز و تعیین کننده رسیده است.
🔹
امروز مسلمین نقشی…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/458973" target="_blank">📅 08:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رهبر انقلاب: با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/458972" target="_blank">📅 08:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VK0fq-EFbzwy97d0fs9U37S9Les9sUh8_ZUnrisnFwkGEHNcVr1vQael1nhpynTtEYCxR0G0bgrjm-EyhgGXd8eZmaoaGRHOTrNhIt2l6n8sS-VShjGfCQXCdjuvTD7-2j_5WJrFexuhADVRgRB_dvriQsj8ZbCV1_2GYYtysPnFrNyVT546vURGpI5pZy88tlXkHWW0mI07DoANA0scxnEuxe3iSIZICnrVoRIzlUWu1tYLYQXqhqayDGhydFrj6rKuHdQ0kzjR_hk8VKpYAyUtd5K2Kp3IZhaN0yk8hV87HFNIFylGR4u-Af7EA-xiMzKFJS-gK1Ecani-2habDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی الهیّه، حضرت امام جعفر صادق صلوات‌الله وسلامه‌علیه را به ملّت شریف ایران و امّت بزرگ اسلام تبریک میگویم.
🔹
از آن وقتی‌که خورشید وجود حضرت ختمی‌مرتبت در مکّه‌ی مکرّمه طلوع نمود، چشم‌انداز سعادت بشر که رَهین کمال بندگی و اطاعت از حضرت حق جلّ و علا است، درخشش دیگری یافت؛ ارواح انبیاء و ملائکه‌ی الهی و قدسیان، غرق در سرور گشته و شیاطین انس و جن، انگشت خشم و حسرت و غم گَزیدند.
🔹
زیرا برترین خلق خداوند در همه‌ی‌ عوالم بی‌شمار خلقت، پا به عرصه‌ی خاکی می‌گذاشت و به‌زودی با خلعت نبوّت و خاتمیّت و با در دست داشتن قرآن عظیم و مأموریت هدایت همه‌جانبه‌ی انسان میرفت تا حرکت کاروان عظیم بشریّت را به‌سوی عبودیّت و تکامل الی‌ الله رقم زند.
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/458971" target="_blank">📅 08:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a852896cc2.mp4?token=Wu4pBEMMgdpLy7eujgp2cjaMmTO1pKpYXsP1IWppS-rCdY6SpeZ0j1iMSMwlZIOyb2x0RU1EUNDAtaLYghNxNcvKIvd7ch59_r8HxtcFQyjrf-HmThV5fIElda5yqzufzDUfgFxif4Pz0H3a0QVmR-BIY3S6bA63g5PoNIdRqy_pIuG8AwN7jWAlZqA-rwHj39AUBCOJ9PLCLA2y2LYanIwfgk9RTEyqKJ0tmrD3i0BwDwoQOaLhPYY-e7DfwA-yVlGfD0gZ4yqdKwBAQMjxpp3wgXlHZmucOExS60Tt5y2Sl_RCBzgHcD8ZQCC2D8Fh0b4490rW0lPrZhjo9ZWXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a852896cc2.mp4?token=Wu4pBEMMgdpLy7eujgp2cjaMmTO1pKpYXsP1IWppS-rCdY6SpeZ0j1iMSMwlZIOyb2x0RU1EUNDAtaLYghNxNcvKIvd7ch59_r8HxtcFQyjrf-HmThV5fIElda5yqzufzDUfgFxif4Pz0H3a0QVmR-BIY3S6bA63g5PoNIdRqy_pIuG8AwN7jWAlZqA-rwHj39AUBCOJ9PLCLA2y2LYanIwfgk9RTEyqKJ0tmrD3i0BwDwoQOaLhPYY-e7DfwA-yVlGfD0gZ4yqdKwBAQMjxpp3wgXlHZmucOExS60Tt5y2Sl_RCBzgHcD8ZQCC2D8Fh0b4490rW0lPrZhjo9ZWXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار قایق در نیویورک؛ چهار نفر مجروح شدند
🔹
انفجار یک قایق در نزدیکی جزیره «سیتی آیلند» در منطقه برانکس نیویورک، به آتش‌سوزی گسترده و زخمی شدن چهار سرنشین منجر شد.
🔹
به گزارش تلویزیون محلی WPIX نیویورک، این حادثه احتمالا اندکی پس از خروج قایق از محل سوخت‌گیری رخ داده است. در پی انفجار، یکی از سرنشینان به داخل آب پرتاب شد. از این قایق ۳۰ فوتی (حدود ۹ متری) Sea Ray نیز پس از انفجار و آتش‌سوزی، تنها بدنه‌ای سوخته باقی مانده است.
🔹
پلیس نیویورک اعلام کرد که علت انفجار تا این لحظه مشخص نشده است و تحقیقات درباره این حادثه ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/458970" target="_blank">📅 08:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458963">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJfpHBxDhnNOIlp2FvscbiNkGrYv6vuw9ndhOwSUgaUHuwhgKhk71VkdfGSLBXTvAmEW6tykgWsqLS9KTAxhXepPBHuPniGatJ0NWPMGtiifmnPYijM_5Lty0qX003KA8n2qFVNTQLrQhkRN2T_-Km4mJtdvRdoqJ2lpXW7evnmvrjl3SIIztVcpDPYCCerTUU2kTbEtXanlGJE8iSxIovhg9yQ635GoYFQyLWT62jYiMJy3mPXQEIcU-zKf0rp4WAbJHA5Y9yN_DAnVUWgOUsqzcp4dVVBHSTlls9niOTu4jU4pS27FrSD4hhYiz6XkIo9FZSa0PnTmrji7BTllqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kx9jMzQJjtVbc3P0L0RwvCtx8zdMz76hYHFg3mqAKC-bYBACsYB1l-hGnSnp-yLDjpOTL3lKiCZulHVdqWTWBJpg0He8rDg0OuMG5tJfxF9c5sXBf2w-EwECTxvrSX7rBOfbhZYf7x1hQKpLsWhLlSmQ1RrkGgfslamEqpMUyR2nIts-U43kMK0sHq0CZhKCPWjJoezOcrox9aLpjnyyA8JyCsDnB6U7U1ttE9SgQO6uO3gXsIEDvwe6miiTotRvxv4iId38LlTwZnDXOtSH82PrJtPoAFaMFc-7Ld378pvrEKjnnZnzt_ZDec4t5qm7axq_PFGXMkX-MsbsYFcH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0U5HaQxTsolpGscLZt-0uVnyArm294WiR5M6w3iQX1-YUucgC2WOwwHgNnogIQYLI-Y_uNfV3JXIjXntWRTNZVBppbKZlCtnazIu3Q5xhP6I7r35Y5YhLOKFO1CWOX9CAI7LtAq23Fbe2hmms-Pw1twxHEjDAHo0TymlqbvB3uIEWWNNYEWUxMczNguUF9UHe6yvUqxdGhOjNJdRDYAmjsSwiNKxzeGG4ntJ-AwgtH1B3PvnXT6Qm1e09X1zfBZHtV5KVp69wilgd1VeBmi5FE5o2bqMiX6aDNyf8oztjac6HAC933ItWuuM0onQBa6jj9tsah3E1BRG8B0MyArrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jS7eF-NC54tOf-4dT7JcZtVSkB442IYigtYH7F68YQGgvf2kDh0VqlYmrmd9WZw1AxxDnu7bExxFpuiKYJ_d4TXE5IhHo1LvOnOoeqVRWo4AZOmRjfLlsnDrdpyG95YZYiE1mOZTdFmzdPBkGRkTMdBTqOA5MTpHVkQ7LdhDMECvE5gD097y9cumZOQqRwv2lq3Ddp3vNMS5rzuHLyllpDwGt9WU3yuehBNTHVCHRqr8oPoyGBEIZW3bu_ShvVYJZ82CaklT7dmtt_DR_3vDZhP5vDc39aznBg9wCjrnGqyKwUjbCC6e0T6OhhqBRemNfQi9jxrbCp3vZu1GRInHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REauebpHoiRLp7bvnAopn9dRIC1du1KEHwTsuEr5MfsypU3vIKxXC5yXB9D9amY8jt8dGHVblTQ32N-DJhEIPz-BaOBXOgLpUbZIdpL3YSVSPtoEgxkygGU4Op1dKVIAIlhdtws_hzQRbF_pQldSCYVm5S3hUFuF8SJCeH6PM09fO1CwDR3pjxotaBFQnVoYBFcmzO4IP4oAmnjmdhuqTwqLb9YtoFiDcY7f_ue_m0S5gS1iUlUPNxSVrppYofiVso3mINE6QLGnkCOQMSfThsEfSjKVarDeAbzQyDKXEXY-Lw1pBh-TlWctfgMWBG9xWpI1LfB6ZXbAUD9HFEhULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4euZDurIwsAKBLoaEJPfp7YEMEeB0ce6LC8q0RDFJ2kg8uajjwCC0pl3wc7CIKTPZJKvm-jxaOc4gqZXWjFY2F9gkI0qYyw7uNfNIwUDHXTTyYo_wprk8CCZwqHOxpofqHsByAOM9KO05X_AR4hkHOEORXK2czz8NyQNtMnEagGAN-COED8JUOIS0vAWxr9C0JGE-Ldt58RAy9d0MR5cXrPJoJWZhK8_zi9A0fTXZyy3UFlX8KeuW2v6OKgAJeo5vraKM-ZHXDLeVCmRSjuDRNSirKR_TBPvLmELw3ptWOtP5XauAV-GxG_MUJ8LcSQHWbQdVurQCrChbrjQwiY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKNoV-cr8lmen5UCmDoH5UQEExz4dS-TCU52EYV20vdlShTQA5QeKvBwLXfldoJnUb-wqpolU5s6AVjRnawJtWDrjAeNy3_q21IbLbC46ygiuaSV79T0X_Jn_oW355y1GzEdh4xbsikL0bLzsKQZ6LtTfMXo2jVFhVVIhj1M9m0F7XBIozpUdvs-VGexKC3tl9uRPuY6IpBX97p8bVBLyxxQfHo_NsIN4d_EVZrGUS73UtZv_rOfaeUsbyc4QgBcum0r0TElh9vnXB8u5CHqPNcRwOt06tclXhbLbYzsm9Thnxpdoo-6KMpzsSnxy_ORp1RYHM9otZ-U3AYt7_6Qmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رویداد «رحمة للعالمین» در باغ کتاب تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/458963" target="_blank">📅 08:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smj-L7utpq4ri1cRm3AzB7HaBKlZoHQWUdvrFTUzAF7VVNb6ni0DzjNSS2DAXi9MfoyL0pRVK-ObSPZzbrQkYzJAptIgkL1h4Xjufi8HCdz5ib-JYP4Yc-rhCJaIl-vT00w3kAHsXeply5vAsG9I3pEyb5xw0sMRHiJICOoPPQsFkhu1UWXWwPHIIZtUnY3VYqGQtxUsyKxpUvjPKQ-4TwBDG_1SSQMiTIThrsF3ATb7hXMMM6AS5hvmfNaLo9MNs38mBMMiAYMNoQ70V6wjloTKKEDMNXQ-zP47tMYUZGjBUWXAG7RVD8ZnMCUhnS11MA4dDPSflSxDAlYCnFY7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار بزرگ در پالایشگاه روسیه
🔹
اوکراین شب گذشته با یک حمله پهپادی، پالایشگاه نفت کیریشی روسیه را به آتش کشید.
🔹
این پالایشگاه که به‌ویژه برای گازوئیل مهم است، می‌تواند در روز حدود ۴۰۰هزار بشکۀ نفت فرآوری کند.
🔹
تصاویر منتشرشده، شعله‌های آتش را برفراز واحدهای تولیدی این پالایشگاه نشان می‌دهد؛ حمله‌ای که به‌گفتۀ کارشناسان، می‌تواند زنجیرۀ تأمین بنزین و گازوئیل روسیه را برای هفته‌ها مختل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/458962" target="_blank">📅 06:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDzFLT9EhFcYUSnM-SpX9CcqGaEXr3T6VR_9VMOSSeALhWc58ek1FJS_EIoXZFaM8MUeG5BU8yWmgVrdr12D_UHjVDPaX_CN8hlOwOafb_XUQgOCJt-GXxhGfcr55WprXN2rjpohOkZiYGeBbFQxy5xFg_qbpiGnHV07WPYHQq8tZfyY3E-FBqu47_Jj0sKslBvv5lbI89jXWHhxU1epQNcLK11HuYeOGKn1OyhYjghWBVQe5kfOlgV68GjmMTHMPUZRDagsAiCcNvy6mimZp886k4Y-7oQ8v0SOszUs9gJlRB1IXVtTX89LA6JryuTiZoEFFzVAoVdoctRJVqDlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بلوف ونزوئلایی زد
🔹
بزرگ‌ترین کسری عرضۀ نفت در تاریخ به‌واسطۀ بسته‌شدن تنگۀ هرمز رقم خورده، قیمت سوخت در آمریکا درحال رکوردشکنی است. نظرسنجی‌های آمریکایی هم از احتمال شکست جمهوری‌خواهان در انتخابات میان‌دوره‌ای خبر می‌دهند.
🔹
در این میان، ترامپ این‌بار با طرح پروژۀ نفتی ونزوئلا، کنترل جو روانی حوزۀ انرژی را هدف گرفته است. او می‌گوید،‌ توافق تاریخی با ونزوئلا ذخایر نفتی ما را بیش از ۲ برابر می‌کند و منجر به کاهش قابل‌توجه قیمت سوخت برای همۀ آمریکایی‌ها به‌مدت طولانی خواهد شد.
🔸
این درحالی است که فایننشال تایمز  فاش کرده قرارداد نفتی ونزوئلا و آمریکا برای ۱۰۰ سال تنها ۶۳ میلیارد بشکۀ نفت سنگین را محقق خواهد کرد؛ رقمی که میزان روزانۀ آن کمتر از نصف تولید فعلی نفت ایران و تنها ۸ درصد از نفت خروجی تنگۀ هرمز در شرایط عادی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458961" target="_blank">📅 06:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وام اشتغال‌زایی برای سربازان ماهر
🔹
سربازان ماهری که از ۱ مهر ۱۴۰۰ تا پایان شهریور ۱۴۰۴ خدمتشان تمام شده، از دوشنبه ۹ شهریور می‌توانند برای بهره‌مندی و دریافت وام اشتغال‌زایی در
سامانۀ سماسو
ثبت‌نام کنند.
🔹
گفته شده اولویت با برگزیدگان مسابقات، سربازان متأهل و سربازانی است که زودتر ثبت‌نام خود را انجام دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/458960" target="_blank">📅 05:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
شناسنامهٔ اخلاقی خودتان را شبیه پیامبر(ص) کنید
🎙
آیت‌الله فروغی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458959" target="_blank">📅 03:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZzfDqNnADsmdj3EHXJuafzb4cQOjup69g9hOMyifXyfG6MNpcp7mwla4N_vcpX0nSf_7N3J9Xk5wcydkiA8S1aoxH69HIjrQYsBXQAicybcSp2SSa0S_6MKu-z9o5FL1rCIAwRCWEodoPTb5rfT_KtkHA2AjQOWWL2aFlMMb8hclZB11ELWcdyHwCOgsq-3iYJlya6FbOkEXgeQcysNCae03UMF3WJ3hzQg1BlqS5aunT6jvJ5v4KxeN8iUF8upmJeNY7PMw_x5PQbnP6YE1upvoJfncNAkmZlwIbNg9dj6IeEqr4U6_PzZZHda9dqdqoAO18YPIKF-yM1ACyToKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تیم حسین عبدی در ژاپن مدال نخواهید!
🔹
مسئولان کمیته ملی المپیک و وزارت ورزش و جوانان از تیم حسین عبدی به‌عنوان یکی از شانس‌های جدی کسب مدال طلا در بازی‌های آسیایی ناگویا یاد کرده‌اند‌ اما این تیم در فاصله ۲ روز تا آغاز مرحله نهایی اردوهای آماده‌سازی خود برای این تورنمنت، با چالشی عجیب مواجه شده و مشخص نیست چند نفر از لیست ۲۳ نفره‌اش در اختیار سرمربی خواهند بود.
🔹
عبدی در چنین شرایطی بیش از هر چیز نگران این است که هیچ تضمینی برای حضور بازیکنان در اردو وجود ندارد و همین امر منجر به استیصال سرمربی امیدها شده زیرا عملاً فرصتی برای برگزاری تمرینات آماده‌سازی برای یک تیم کامل وجود ندارد و به نظر می‌رسد حتی عزمی هم برای اینکه این تیم با حضور حداکثر نفرات تمریناتش را استارت بزند نیست اما در نهایت وقتی تیم از رسیدن به موفقیت بازبماند، همه کاسه‌کوزه‌ها سر او خراب می‌شود و هیچ‌کس این روزها را به یاد نمی‌آورد.
🔗
گزارش را در
سایت فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458958" target="_blank">📅 03:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458953">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4pdxcWShAayQKoZ61TlCnmu282MKOC7CVjgM-CaJIDG0-SXR8tQxZu_l4ytIgSzQL7KEbz0a1FaVIJqyYpDQ4oY7zBjAOViJkc5jv4KR-2H2heWGhOCJXxsGHE5O6P8L4VxEyCKGJWSh7p7yXL0FGDnfEOTaOWECfiU1O3f7E340s7Fa9hzQmhZbayEXrE8e7YWxS8RyLC92FAJIBvM8-4E6tFEXFC5BbJ9kTkhKz8NQvTiaByBkjZlvs6KoRKvG1RR-xZBGa2RDm2wI64pMHIXa2ijOYi0o6rO619SAgqia6mrnRZoO6u6fmFkTOFaMPzSAJ8_axBcFH9fan5GDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpiPaDWRk_GLFww00l8uPdpWx2gR8ZovdP6xOLH7oh4NEqweatiqj-04KySLIvbbP9p4Q4YJ3TUjJsoRZDM0KAT5oIqfHKNumjjv2vTaofli5LKXDJ3N9qPViiaTUyanuiSOU70LR5j4gSulkezy2RftogH-hPDNp8thj4fDvsWaiybw6RMgH1EYPd9qcw9XlEjntyquXNKqnn5RPMSSE9UYxxuPvfGNOcyVXkoNVvfV5M9Yw3jGQrNxSmDhJoiKnASvstMMtRl8zZZB8YiAOHzDPuiFPldH8bRC21oi0WE7W5_KwN2iMv-ITUjZZir13nD7oj9CqqIKzYdaVdMBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQhks2k5lZDGulzcTWuk8RYEIN8m_bdwwU8EWymDw4ofCS_uzbo95CrQhilDHmWsTCRLslqVWaizgstQwMBuk6AIpybVpniDM0-I11Oot0ywExqtgneZjY69OcfPNJYkniuT4REmdV6ICeYLZovLunZU675VV42uLZs1QclQAaQNCkDZsZ9GtLYh_O60EMCV-9oMhTNgIfQVkO6qh8N72P2q7qhtpy6zP1ZpUZ7TUALGagEujjhY-6vvcUY3Ut_jEDaJ4u59XaOsg93jCKR6DbuoMHlIcfTOiRObFSJ4vDsQ2_30g203onMugqIVGNR6Lr9OMXWfpFYdP-qMM2dn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3BA3c7pznBNP1fT9l_BXAzpzneHWrtqzrj9i8ILqexuwocDiQpdiPFJejUk9UAkOmY7Io6PcojaA2AKeHoq9H3Y10awnQJbXF8q-15pErZPN16Tz6ektCzOU4D6KdibGJFcWbhIFqwaNn58E-u3VVtPRRfOoibPY45eRZscK_mUvnGzsLgDR8tSbGy4OFR6OyOVC1dLTvdXQSrXtLZUqMLSCXDxssiD7zTg4q7AXBzb6zudRTseI9Nsjqn_SlEixmWvMqewsQvhwvFLmHiML9RLW0aL9lIxIB0LCset09l56PElL3b39m_itoW_FiJiwgd3FkiCp6IUBPpdcoVf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQI0l-WEU-n8ushcOqv3yfgnlw-qNH49chXvcBm5-gS28_HL5dwekpViLInOIAAvfePfsQ1JXFS4RB0H4gnpmP57yr49-u-gyMrmOi8KIGvXj9dLdfYvRBlHXuvxrnKiVBu7Vl0lOH5KrJQpHlCus9WK2Jf9s7GEANWvy2kQXrfVESoDn1XnEnWoz7Hm8VBfnZ-teh5_oTojxo0q4zmZPjXSYzWGXXRrXxCE-btxenSmwjQHycp-WN5rlp_waFOnZfHg59abmKswtCPMAVA1o2C7Z0hwDCPRaqk4xuqWO2Tt6NbRbMPYKEhzuqkI7diGZM-b8Qmt5FhWII9hR_Xx9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن میلاد پیامبر مهربانی در اجتماع شبانۀ کرمانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458953" target="_blank">📅 02:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458952">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برگزاری مراسم یادبود اغتشاشگران دی‌‌ماه در مسابقۀ پرورش‌اندام
🔹
در حاشیۀ رقابت‌های پرورش اندام قهرمانی کشور در اصفهان و در سایۀ بی‌توجهی یا اقدام عمدی برگزارکنندگان، مراسمی در ارتباط با یکی از اغتشاشگران ۱۸ و ۱۹ دی‌ماه سال گذشته برگزار شد.
🔹
اغتشاشاتی که به‌عنوان یک اقدام کودتایی علیه کشور، با آشوب گسترده همراه شد و به شهادت تعداد زیادی از هموطنان و نیروهای حافظ امنیت و واردشدن خسارت‌های سنگین به کشور انجامید و در ادامۀ همین اقدامات، جنگ رمضان نیز رخ داد.
🔹
در همین رابطه رئیس فدراسیون بدنسازی از همکاری کامل و همه‌جانبه برای روشن‌شدن ابعاد موضوع و شناسایی عوامل و مسببان برگزاری مراسم خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/458952" target="_blank">📅 02:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جنگ روانی آمریکا دربارۀ تنگۀ هرمز برای کاهش قیمت نفت
🔹
یک منبع امنیتی مطلع در تهران در گفت‌وگو با پرس‌تی‌وی: ادعای آمریکا دربارۀ انتقال حجم قابل‌توجهی نفت از مسیر جنوبی تنگۀ هرمز، تلاش برای تأثیرگذاری بر قیمت جهانی انرژی و بخشی از جنگ روانی واشنگتن است.
🔹
این ادعاها با واقعیت‌های میدانی مطابقت ندارد و واشنگتن تلاش می‌کند با القای فعالیت عادی این مسیر، در مقابل مسیر شمالی را ناکارآمد نشان دهد.
🔹
عملیات ایران برای حفظ محدودیت تردد در این آبراه راهبردی واقعی است و برخلاف روایت آمریکا، کشتی‌هایی که قوانین و هشدارهای اعلام‌شده را نقض کنند با واکنش مواجه شده‌اند. همچنین تغییر مسیر نفتکش‌ها پس از دریافت هشدارهای ایران نیز نشان‌دهندۀ جدی بودن این محدودیت‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/458951" target="_blank">📅 01:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458950">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icf86FZKqnCYr3CDgzTdkY9gzNLX6xGGWMgEywA2taiY2ShifZPdYflQySZW05r0f3NJ_JMvTqyj9WLxoywJGLwg-YSQvF0J-73RvwazwDhJHtpc_B-rEhac0-Y3VjU_Xwr3easJ8cXuLw7amKDnJr9PFlKyZhv4gg5aAycmqJJNjJeT7ycUh02G6ELbzPBleIKYpV1zbYwGDeb62dZdTZ6CC4aWAMcDn26D_qAXxm9l4M4E4nd1uaqu-Grky52O236a9exL-1MsSilZyzHp9sqQnhPMp8x0PbSs8y2qkUVZ3ld5y4GSulReFPqjwxoTZ5S2IEz07aCfHTh_Lq37KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام خیر محسن چاوشی برای دانش‌آموزان در آستانۀ اول مهر
🔹
محسن چاوشی، هنرمند سرشناس و خیّر کشورمان از راه‌اندازی پویشی تازه‌ برای کمک به دانش‌آموزان نیازمند خبر داد.
🔹
این خوانندۀ محبوب و متعهد، همچون همیشه از مخاطبان خود دعوت کرد در پویش خیرخواهانۀ جدیدی که این‌بار با هدف کمک به دانش‌آموزان نیازمند راه‌اندازی شده، همراهی‌اش کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/458950" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458949">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhXnoPol1T1363JFzzpiFGYsvMnWuMRRcsZiHuNnhdMa5dmnsC85ojwLLaXwloswwlVjwY3qbix1_MiTcmDJ_xEzpe5NqP_PUbPywu_e0dkiBQhqJL4rEeMrCigg6YpSUlpheRUb0NU1OyMzFbRA-LR_G3NjIHq_BVt_I73jt23aq_MQWIWpmWIo_DvLOkExW4CrgtW-Y1jZMD9fxQ6pYn9FstWupDF-vLX3Vz72vc4J7g67zV3vJnG0WDCXybcU26fw8liNFqoBrvRC_WjlQj_oLNlVANClHn79kO9qlLygmBAOnBnFo2anF8EWyksHk1XR_Usn7jvy8bBq7R3nFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات گوش به حرف آمریکا؛ بازرسی از بانک مصری کلید خورد
🔹
بانک مرکزی امارات فقط ۹ ساعت پس از اقدام آمریکا در تحریم یک بانک مصری، از آغاز بازرسی از فعالیت شعبۀ بانک مصر در این کشور خبر داد.
🔹
وزارت خزانه‌داری آمریکا پیشتر مدعی شده شعبۀ امارات بانک مصر از ژانویه ۲۰۲۴ تا ژوئن ۲۰۲۶ حدود ۱.۸ میلیارد دلار تراکنش برای ۱۰۳ شرکت پردازش کرده که احتمال ارتباط آن‌ها با شبکه‌های مالی ایران وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458949" target="_blank">📅 01:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458947">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75afd74b23.mp4?token=DDqhCOcg5JYi3tGT6tXkxLqLKklElukb65MI1T6CLPU1d6QqnKtAQVwJIPQay0GqpEHaPouUmT7L0GfInRvs1BVcu0JDULVIjqma4zgrl8SJPgwgUeo6Uu7aGyjkyvVyB4WTBbK0R806AbFIesTJ1IjXhnoVrCzODSKtSXJha1Ij7RoQmlOr3kInJ3Ku-rLZqLBBM-mjvxdNTiQsv8FNu8RbIG521f1YNPJ_6XdBXyR2dfiX5OqrcCujrmaf5Svd_wSD4S25p4gF-J98MXqINdGIm30YZrHjCxSA-n546y1sxI4x0V1vVFKO0J60PbECZRT1Apjc6NNMj08e6Q6euQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75afd74b23.mp4?token=DDqhCOcg5JYi3tGT6tXkxLqLKklElukb65MI1T6CLPU1d6QqnKtAQVwJIPQay0GqpEHaPouUmT7L0GfInRvs1BVcu0JDULVIjqma4zgrl8SJPgwgUeo6Uu7aGyjkyvVyB4WTBbK0R806AbFIesTJ1IjXhnoVrCzODSKtSXJha1Ij7RoQmlOr3kInJ3Ku-rLZqLBBM-mjvxdNTiQsv8FNu8RbIG521f1YNPJ_6XdBXyR2dfiX5OqrcCujrmaf5Svd_wSD4S25p4gF-J98MXqINdGIm30YZrHjCxSA-n546y1sxI4x0V1vVFKO0J60PbECZRT1Apjc6NNMj08e6Q6euQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تظاهرات مردم فرانسه در حمایت از فلسطین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458947" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BW1rzkGSRusx7CLSiYeXj1BnoyAqM6Us7ddlKxKbun8q8BnE2VvQdIwyJT6vfn_LEkRzZBMqVEeKbMS8XGzI0ox-gIEU-5hLIxVJaKmXtDq2v0FSrZXZ3FhlPYf6oqS3FDw48TLPem83o_m5aJwLTA54cKaxBBMyn82XcG6-oIZ-yviqwpTUSIUP1krAoWZN88pc95F5tbxubyI_HDaGoOhIrSESmN36PPg6YuI_KT4Btc0mKFrzrpzQjNfHyL8-_p4Wc37fcBWtCujGROyN5b13hlcfqc10fHOkR_s_hv95NcBqMGLUnETa_5NApx7ljGavYCQ5pfUd53RXcPrf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmWed-rwICcBetJUI1VJumDsb50lG2RZOiWGMdcNF0KSMmhcq1lg-4we2B3FwAwJaC4zXRByS-8AEdCNIJjiAxBAgkNECjMjFMAiBazsNsquPoBG4Vl4w1Fg0VRTUod8XaNaH36sofcbZnEuGwqBKVWnDghzlHEJNWDyhGBIDrwAeZS_4jxFrB4Y_QBG76Wv0hXzNFqYzOgENslkHB91QkwOUSlOsPkFGRxd2U8r-lvGxmftsHLw_BiLW6nKn6XL0-1rU4tDnjxsVjWwKCMyOrPLw81iTYzz4sJyFiDOFMv-mzoyQEMhWUD_S3T_J-sL-8U18t_zOVW45i2JZhAtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkbwjFfpBxuDOu_ZHD2QhM6si_kHGxx5T16XTS4DHVNQZ-9t-AqE18SQ2799O9ZB-vXFsJtot0rsQpNhuQisj95ei7VeGCLIrx7vCZ9afTuZLQLYrr1Tt69rzzUD5jeDfYoRxaAC9G1GStbWhdYi7S5r_TT_X8ZLZ6Vd52fApjm4AH8qcyr9cmnicF_uqRANVkVrHnQqF5d1V3PkiD4GyiktTeV3PjMuZO4VBxUAhnJPjPhGY5Bhp2P5bj4NAkOp3Ab7wcdlcvZCc2qaLwFa0NIEVzXXvUfy6Bx9_c1Fhret4ahXZfVTaptOAwGS4VOkgiC9C5h2-onDpaJ6mEKtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKmL1Qgj_km3NnXDLlc4tKBIoWvhrlGreveG6LrmaxLPveyLi4D6baRJNZfMkJzUERsjDUT1tXQOz0uMcBoAcCMVJyEx4g7bby5WKysZFTaR9BD4RE2EKH4ykuSj8e0ykPPSRfYtziLV1M0-6KJ9nA4RGSSvTJh0PdgUJ9dlmk-DiMwF9v85ThM711q73rVpbqBe7vECZBtVVFXJcHg7AqAyrs6eJY0A_iUPo0q7bpeWvO0d1yODciBgiQ7NLKV-XvuBIjdFfX6rjFgJVwHLx4cAAKHdRAUPIA1lM-gSyTSYyOUxkFq8HTHCj8AEPeKpO7cDOe44Yg663YxS69gs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0kfD1U3YbyqgqfXKFaajnpIdUBkvJhNv_uu9BUmRP9SiyKjTPr290KUgGIdWVrsA8MDLIg7Ye9XegAO3mHmElP8MA3ONzr6nbvZNb-pjZbl0XnA2wDFKHZKT2Jw7CRfm9bVpuCz5ykt4MADexDOSNLIIRk1O69tsaInP6Z1tIWj9S8RiVvIg0HNCq_0CoKRZS97Oh5D7dOd9pllCq5ix9BKTepLHQV0L4iP9N3XtUKGuk6vR1wQYDuaeiDaYHLvC98uanNQtq3aXzqTJTsAAx8th6mPdwyIq-TnAB9mSJMQNeKP3e-jgyt64F4Jeq3KdNRGHSNeDmxsDNafSpzoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo-TEvHj2v66o9Up6K-BNFpb1k_ObbDTaL6FkpuvevBvrmjicgK9g3MRarWNrKLK1sud9O9y80uiBsUx8nwyupoOxFt4sGRMNezkfrbhUPXJH0gzXLLIwAGEkXEdeyLaJ32ymCpe5kWqbCw66y6eocZpyYXIkqz-ZDtYVGn03Dza3cVBydv51VKxLFmMEYbqVe2vqVX0ymNetNUMJY6g1bP8dhG8RLQSvtsfUeWAs8hvG1SD1a5pD7YKldWZMM_Di6yXhnjgBn61tqu2iMa_FdodKXsCpYFGypPlFU3AIYCcxZJIZ4z4q_b_mRRPs8EbEqnXhKupipDMK2MSSUjMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCxRQCmo13Cp9-Ps07ZMFtSIRRyJnr43bvoPgUSwUE1qJJOtVIkGTSIPU7Jn5npgSr-xn9krIjMcgrhpxDsn6ZjKFZwGC-OhNQtc7gQuZqicFAXa-NrNNIqj1oXDxRXUtZdPwBSg6IYGUrI4E1NYpDwpIFHvHk6F9rCSMTpuaQswvs6FfWsEaplKBWbgeaAOqLDS-XOf4IpEtgMEnPy4qFxdp9kSSqxeuOWYe3EkkJBRPdgpElPgjAx_rmUk_OaR-Y-aVaMxtvwBv4Vl4NVKw-f-rXbAyPaMAJWqWFQxumSNfovF70hiuRbQsHUqwbAYmPFx_QBejvdrLkvanP7PLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن میلاد رسول خوبی‌ها در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458940" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">استارت عجیب تیم امید برای طلای بازی‌های آسیایی با ۲ بازیکن
🔹
اردوی تیم ملی فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا، امشب در هتل المپیک آغاز شد. پیش از شروع اردو، با توجه به مخالفت برخی باشگاه‌ها و تداخل برنامه‌های لیگ برتر و لیگ نخبگان، پیش‌بینی می‌شد اردوی تیم امید با تعداد محدودی از بازیکنان آغاز شود.
🔹
با این حال، طبق پیگیری‌های انجام‌شده، از میان ۲۳ بازیکنی که حسین عبدی در فهرست نفرات اعزامی به ژاپن قرار داده، تاکنون تنها ۲ بازیکن خود را به کادر فنی معرفی کرده‌اند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458939" target="_blank">📅 00:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ytZMWbiIg3or42k8Dsen0A06wb1AeRKPZ2nPCt62V8pCD-RlPU9qQhugRDu7zXCTWavXhW2scK7hMBRTUtneV32A-DVHikZhGWdSr9MfYZZAB-xOsNcoc7Bjm8-NA9TsknkR-7AKMjjN1m3ZyjSnLUgBaMx3hrtnmlDznxC3bhNCiaVDHljWK2PbJBbFHLzxGJlH8wI-AvZ-eCwqp1DKQBnQ-yyG0VUCIogqE7tneSFsDBfdce54cZss__f7zxp5yDJhzo8-cNrRMdaGX0b0ugmWMAf8WIfKY7ozUraKjW8VIch3d6Ifx_PiC9fXYbLgOmkH5PUtCqWA-vhERxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: طرح مقابله با نفوذ بیگانگان به فعالیت علمی ضربه می‌زند
🔹
معاون اول رئیس‌جمهور: تصویب این طرح برای فعالیت علمی کشور زیان‌بار است و می‌تواند استادان را نسبت به تعامل با دانشگاه‌های معتبر جهان نگران کند.
🔹
فکر و ذهن استاد و دانشمند باید بر پژوهش متمرکز…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458938" target="_blank">📅 00:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPNJ8-k6wdF4lEb_RydGu8Uvd6n_VxvKLb-Ki3xOXWPB2ay2KWGeEEjeKizwnhGbIMbY4itm3NRNmNP7B9qBtaHosTYH12q7aGv3HPMxJgACFmW9P-V_er6kxsh9L6K0NBfXVwaVlaoYaE5Uf1OKmnTiUQO2ucc0wc1H2r4pI5D7g6yAkIoE0kzh8lql5HvQeg5bG578i_OA8QA4SPv7ntJGZqltX-L4OkD4gQsyabybzydftOKQ7MmnGe8Fbd8qwHBQTuRzvClNm3xglY_sGDI0c7fBoYNk8pQlHHfto01_yVfwTsF7Vp-LgyRo4UCLpv7VNoF2sXGoRSbDUmV9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: نرخ سوم بنزین بیش از ۱۰ هزار تومان نخواهد بود
🔹
زمان اجرای این طرح هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458937" target="_blank">📅 00:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c721af0cdc.mp4?token=hgJzSnKAWHJkQN6FnQXqMFac7sb2CdoODKEitAtEt_KBb1IY53zKaoomYJheWB2VQbS3HB0V08V23kiGoLLcmzqp_Nw0Z9y16S86AFugWKHqzrt_196-XFChBWynF21iN_5Kfpn_S0_esxrhup8iGsfYTcmIYgoF1vh5qdHJuF6KUx-Tc9mesfVrvYoyBBtHDQ0PCmp98HnOiUlJzPbrFJJ7gtXV3aZ4dlkhO4Tty-JkxlavhdNtWjRhd4fJUGYtxNZ8xDURhD6UljJGjl4vZFM6VehYVh2Jlmz5n5VBpkWZRv89j-9aqOLYXESsBzeOCH2sZNEFnYYJGHhwh0YqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c721af0cdc.mp4?token=hgJzSnKAWHJkQN6FnQXqMFac7sb2CdoODKEitAtEt_KBb1IY53zKaoomYJheWB2VQbS3HB0V08V23kiGoLLcmzqp_Nw0Z9y16S86AFugWKHqzrt_196-XFChBWynF21iN_5Kfpn_S0_esxrhup8iGsfYTcmIYgoF1vh5qdHJuF6KUx-Tc9mesfVrvYoyBBtHDQ0PCmp98HnOiUlJzPbrFJJ7gtXV3aZ4dlkhO4Tty-JkxlavhdNtWjRhd4fJUGYtxNZ8xDURhD6UljJGjl4vZFM6VehYVh2Jlmz5n5VBpkWZRv89j-9aqOLYXESsBzeOCH2sZNEFnYYJGHhwh0YqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از آسمان نورانی تبریز در شب ولادت پیامبر(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458936" target="_blank">📅 23:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c526c62f2.mp4?token=eyGXwG_TNAh3KM8tOl4a8XoXnnjkO8FDlwuo377rFR2Cta5VsRHPOHFicYOYDnP3U8pU2gCJwa2aToCctNOqTPecvwq1zZNaQY9aqarlpFeZ0fTQ7fqzVtOSbgOWTJ5efB7pOEL1Fx9vv-5K94Xh66X_5LwqEi5e89RnxfRtv6lnpkzzSRAci5rBZeO62RS07KhEuJWSRC_mldDJJrULoqNOPOlMiVvXGn-oXKyOOAQFgLGo1y463qWcSv3h8RPvGqcVnunOKyxczSRemSbySDoODvW7t1QV-Cx70VN83IJOk_0HJEmK_kpEccqxSuNo0-5yWiVflo2_7DFKhc27ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c526c62f2.mp4?token=eyGXwG_TNAh3KM8tOl4a8XoXnnjkO8FDlwuo377rFR2Cta5VsRHPOHFicYOYDnP3U8pU2gCJwa2aToCctNOqTPecvwq1zZNaQY9aqarlpFeZ0fTQ7fqzVtOSbgOWTJ5efB7pOEL1Fx9vv-5K94Xh66X_5LwqEi5e89RnxfRtv6lnpkzzSRAci5rBZeO62RS07KhEuJWSRC_mldDJJrULoqNOPOlMiVvXGn-oXKyOOAQFgLGo1y463qWcSv3h8RPvGqcVnunOKyxczSRemSbySDoODvW7t1QV-Cx70VN83IJOk_0HJEmK_kpEccqxSuNo0-5yWiVflo2_7DFKhc27ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجلی وحدت شیعه و اهل‌سنت در جشن مردم شهرستان قلعه‌گنج استان کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458935" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15212f3f87.mp4?token=Aw3fiuNz-o0HVERx_JSuC8EamWm8hc6MsgBHEAhwhs3_DLfZTgcRBN4Loci19J36CJE3W935etEKAN1FtXmzUVeDC5XbD_UudzwVVuLKvUILWVl9xFzRIbmGFcPTIcWajWPXgmWXdZkdPTexwtvFJcKt5ebNiBFPndPo-3bE_vhWANSlb1VVl8v4BVHyteBxl_ThiE942HC-DahGWP9iLewupu22iB-X5ApMoo844-PZlkUaavDvIwneh5v2o-0SPSoumm3R6O5yJqDJJL45fy_UL9-svZxBvIPxTDnHqUkW5iNeqF08wnRbgzrCLvC-_u8GS8YZgk0eC4nCZLdkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15212f3f87.mp4?token=Aw3fiuNz-o0HVERx_JSuC8EamWm8hc6MsgBHEAhwhs3_DLfZTgcRBN4Loci19J36CJE3W935etEKAN1FtXmzUVeDC5XbD_UudzwVVuLKvUILWVl9xFzRIbmGFcPTIcWajWPXgmWXdZkdPTexwtvFJcKt5ebNiBFPndPo-3bE_vhWANSlb1VVl8v4BVHyteBxl_ThiE942HC-DahGWP9iLewupu22iB-X5ApMoo844-PZlkUaavDvIwneh5v2o-0SPSoumm3R6O5yJqDJJL45fy_UL9-svZxBvIPxTDnHqUkW5iNeqF08wnRbgzrCLvC-_u8GS8YZgk0eC4nCZLdkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن بزرگ امت احمد فردا در تهران برگزار می‌شود
🔹
این مراسم از ساعت ۱۶ تا ۲۰ و در مسیر میدان هفت‌تیر تا میدان ولی‌عصر(عج) برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458934" target="_blank">📅 23:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1beb11f27.mp4?token=h0fKyxG-kvAQAza9Ub50tUy_IhQReLFIGRHohUzmFpw5Yrhb4cnCER97bVxHN8PfPwV3-FVmtBsH45WxdVDFX2n6Wq5rvViDjNF8oM_vl4mGuSYvlgNViiGj2dQbAqQqGta03LNcmkdGDqh6xqq8SWcBDnzCVIXbaxIUQDq5fTMwbLbu9f51bpw8qtuDK4rWdrJmn8k8SzLwnYdOLzvsjtlkcobiIfi9wAbgeupsHddiwFO391soFpt6Rlr2oK7faFtIG-QCxJ-LbeptaQxJkjCW7qLGT6s2NiIGh2e24_D5xTau7ZTw1XQ2lrRMfPQ87Cw4CXVRF21cySpLl1uBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1beb11f27.mp4?token=h0fKyxG-kvAQAza9Ub50tUy_IhQReLFIGRHohUzmFpw5Yrhb4cnCER97bVxHN8PfPwV3-FVmtBsH45WxdVDFX2n6Wq5rvViDjNF8oM_vl4mGuSYvlgNViiGj2dQbAqQqGta03LNcmkdGDqh6xqq8SWcBDnzCVIXbaxIUQDq5fTMwbLbu9f51bpw8qtuDK4rWdrJmn8k8SzLwnYdOLzvsjtlkcobiIfi9wAbgeupsHddiwFO391soFpt6Rlr2oK7faFtIG-QCxJ-LbeptaQxJkjCW7qLGT6s2NiIGh2e24_D5xTau7ZTw1XQ2lrRMfPQ87Cw4CXVRF21cySpLl1uBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: در زمان شهادت شهیدان رجایی و باهنر، من نیز در همان ساختمان حضور داشتم که ترکش‌های انفجار نیز به محل جلسه ما هم رسید و من به واقعه نزدیک بودم  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458933" target="_blank">📅 23:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c781c42238.mp4?token=UC09mSFA4urI-AbdUe4F48Nd0PVfnTOOn0dJSVBqpn0UFbB8-Ue_LOa290-K0AmN56kZC9Kk9ZyUXsOu4bLID-_6FJ8qxGhOmFs8TAp5Np0iAYGzwRUcV5224Y-wYqORXl7XsfMBRSLlWoG7-amAgDvucAm3XwTyrwKS8_O12ZXdEYm69saZ17CzRNn9MXYXqi95pCe5a_3TXMMn_CVk-NHNt42Ek7cQVmsXQEnYB_BPySDMtNF4ONttja1gR-C0iwRkXjxHPbWt3jui50r_r7BDy6-k_INMXzd8oMUV3lIyR_wq7SafOnZ76FWCX47l6Bubj6uHLBX8ZdxwnYYLZR2GHyHTE42_xeMEyRiVXOHdvIM0B5egG5MRFA3qBA2isRZ7kre-S6agW2js9mNpJphwM636EKwE-pSD0AiJKQWcYwHmOXIFsgPZnzTSM3RBsN0fJwXIj5SHWWLr4YZiNCQMN6Bpya2zIS_kbopPMFtkWx2cbYeGIAjF9dSHMcWNhvK9OxsjqkQAL2dZuVRAApddaLK3F8U6chEyGmk05CXAFaQqy-LFWwxk_6wubsnNGh2I61qHpzIQCBED5XaC_mjKi3boU-9r3C2n8sF9-p2WfKBjP4kt2IkZ6AN53XocurPJtHmJ2UbSdgstWFaL6g1LtAU9-CBnVSE-_2OOp3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c781c42238.mp4?token=UC09mSFA4urI-AbdUe4F48Nd0PVfnTOOn0dJSVBqpn0UFbB8-Ue_LOa290-K0AmN56kZC9Kk9ZyUXsOu4bLID-_6FJ8qxGhOmFs8TAp5Np0iAYGzwRUcV5224Y-wYqORXl7XsfMBRSLlWoG7-amAgDvucAm3XwTyrwKS8_O12ZXdEYm69saZ17CzRNn9MXYXqi95pCe5a_3TXMMn_CVk-NHNt42Ek7cQVmsXQEnYB_BPySDMtNF4ONttja1gR-C0iwRkXjxHPbWt3jui50r_r7BDy6-k_INMXzd8oMUV3lIyR_wq7SafOnZ76FWCX47l6Bubj6uHLBX8ZdxwnYYLZR2GHyHTE42_xeMEyRiVXOHdvIM0B5egG5MRFA3qBA2isRZ7kre-S6agW2js9mNpJphwM636EKwE-pSD0AiJKQWcYwHmOXIFsgPZnzTSM3RBsN0fJwXIj5SHWWLr4YZiNCQMN6Bpya2zIS_kbopPMFtkWx2cbYeGIAjF9dSHMcWNhvK9OxsjqkQAL2dZuVRAApddaLK3F8U6chEyGmk05CXAFaQqy-LFWwxk_6wubsnNGh2I61qHpzIQCBED5XaC_mjKi3boU-9r3C2n8sF9-p2WfKBjP4kt2IkZ6AN53XocurPJtHmJ2UbSdgstWFaL6g1LtAU9-CBnVSE-_2OOp3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنزین کدملی در تله دلار
🔹
محمدحسن صبوری، کارشناس اقتصادی در گفت‌وگو با خبرنگار اقتصادی خبرگزاری فارس، درباره طرح اخیر رئیس سازمان بهینه‌سازی و مدیریت راهبردی مصرف انرژی درباره اختصاص بنزین به هر کد ملی به جای خودرو، گفت: اگر قرار باشد بنزین مازاد خانوارها در یک بازار عرضه شود، قیمت بنزین در آن بازار تحت تأثیر دو متغیر اصلی یعنی قیمت جهانی بنزین و نرخ ارز قرار خواهد گرفت.
🔹
این کارشناس اقتصادی افزود: قیمت جهانی بنزین متغیری است که اساساً در اختیار و مدیریت ما نیست. از سوی دیگر، نرخ ارز نیز در شرایط فعلی کشور متغیری نیست که توانسته باشیم آن را به شکل پایدار مدیریت کنیم.
🔹
وی با تأکید بر اینکه اجرای این طرح در شرایط کنونی به‌هیچ‌وجه به صلاح نیست، تصریح کرد: اگرچه این سیاست در شرایط پایدار می‌تواند کارآمد باشد، اما در وضعیت فعلی اجرای آن را توصیه نمی‌کنم.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458932" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17429cccc6.mp4?token=jy-94LZ4ZFAYyOZhKnYjhph7GBDzUeo8Tsc_QZuc1iY02OXrZxDZEqZYX-93M-Lo7_lKbGZjFutDVDEUDBOHXW54kJkgNpLOBFgREmkpO8OXvPdG12NsA-OhukAGTaICH4yiY4UrqeAYnsSaZya_MkQJR0x2ZlavNxdnUHp7mFV4PqFQxk0rzIHzU929pt6Ti4g7nFDPiqxwA3e3oRBCR7o8_NWi8RB4VST1s6WBlKjzjhcR1IJvMQMBwjdUHF7Km0w4tlmcuXitUXvPuHkJefl6FA7P2WNN_TnOuh044mSMeNDj5g7SqEEOLzqK0YnOoaew0dBaV48oBhGwocwfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17429cccc6.mp4?token=jy-94LZ4ZFAYyOZhKnYjhph7GBDzUeo8Tsc_QZuc1iY02OXrZxDZEqZYX-93M-Lo7_lKbGZjFutDVDEUDBOHXW54kJkgNpLOBFgREmkpO8OXvPdG12NsA-OhukAGTaICH4yiY4UrqeAYnsSaZya_MkQJR0x2ZlavNxdnUHp7mFV4PqFQxk0rzIHzU929pt6Ti4g7nFDPiqxwA3e3oRBCR7o8_NWi8RB4VST1s6WBlKjzjhcR1IJvMQMBwjdUHF7Km0w4tlmcuXitUXvPuHkJefl6FA7P2WNN_TnOuh044mSMeNDj5g7SqEEOLzqK0YnOoaew0dBaV48oBhGwocwfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وحدت و حماسه در مسیر گلزار شهدای کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/458931" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سهمیه‌های دهک‌محور؛ گام بعدی اصلاح کنکور
🔹
«نوجوانی که در خانواده‌ای کم‌برخوردار بزرگ می‌شود، اگر امیدی به رسیدن به دانشگاه نداشته باشد، مسیر پیشرفت را زودتر رها می‌کند»؛ این موضوعی است که دبیر ستاد تعلیم و تربیت شورای‌عالی انقلاب فرهنگی آن را یکی از چالش‌های…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/458930" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82a48bd9a.mp4?token=ObpaK8oTsB2Zy6CM0Jl14QiMq4Y_qP7B_sIP1eXLclRuOR-MgUKXI89JqClPM5zZ4kfd5iP_HCy7vwIJaqa0XIEKdOmTJjC6l_J54o2v5hOgujPX2qP8q78s7gZ8bWI-HKtfZQwEh5XNwhfUA71DwaqlzCV0GEAF7_85Hfk-m7TKcegdVhOcMZcjFLTHbq3AR2ZeqKR7t0Jw05z7IhbCHcNsu8wlUm2_0X6wbSx3pDjqE8IV6DOfePo2DnfUjr3DPfXLIgqRNs1UeClLlZ2d-P2cdrTikl7XgKZ-QUkNnGrQYZG1Njj3-ZLC1ixUrtfqbOUbUmZz4mW63F7cvEsaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82a48bd9a.mp4?token=ObpaK8oTsB2Zy6CM0Jl14QiMq4Y_qP7B_sIP1eXLclRuOR-MgUKXI89JqClPM5zZ4kfd5iP_HCy7vwIJaqa0XIEKdOmTJjC6l_J54o2v5hOgujPX2qP8q78s7gZ8bWI-HKtfZQwEh5XNwhfUA71DwaqlzCV0GEAF7_85Hfk-m7TKcegdVhOcMZcjFLTHbq3AR2ZeqKR7t0Jw05z7IhbCHcNsu8wlUm2_0X6wbSx3pDjqE8IV6DOfePo2DnfUjr3DPfXLIgqRNs1UeClLlZ2d-P2cdrTikl7XgKZ-QUkNnGrQYZG1Njj3-ZLC1ixUrtfqbOUbUmZz4mW63F7cvEsaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: در زمان شهادت شهیدان رجایی و باهنر، من نیز در همان ساختمان حضور داشتم که ترکش‌های انفجار نیز به محل جلسه ما هم رسید و من به واقعه نزدیک بودم
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/458929" target="_blank">📅 23:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e58c2255d.mp4?token=PEmnguKUdlYPhYfOjQthJKfElCfuUa4rjR61UmIrEa0t-RZBPIHBxzihCMOPGQcsrmrR-O5pnXBPNdKf2HJwExAl0JJetU9M4vRoOFAPGU_-anBDYM4YvhSFuuRzLbuqcwCcCMp0-96zz9vItlqTMtm7B0eTMhyBxppLLB_3Qz_AvB3SIJcbwSlvKfMSoQcryawLl3RFNcc-hG8uO4-mfr4Bx2v62ZZ1VvWMDXgO7femVCVrItzR24oSBIdKcVa3qZLBB9Zt4Xr6oAPxh4vRT5LWZbal16616VbDzgtUo0j8jd5b1b7hNW5XqVLWPbItvhjk4wIZkRoPYGlxMxwZyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e58c2255d.mp4?token=PEmnguKUdlYPhYfOjQthJKfElCfuUa4rjR61UmIrEa0t-RZBPIHBxzihCMOPGQcsrmrR-O5pnXBPNdKf2HJwExAl0JJetU9M4vRoOFAPGU_-anBDYM4YvhSFuuRzLbuqcwCcCMp0-96zz9vItlqTMtm7B0eTMhyBxppLLB_3Qz_AvB3SIJcbwSlvKfMSoQcryawLl3RFNcc-hG8uO4-mfr4Bx2v62ZZ1VvWMDXgO7femVCVrItzR24oSBIdKcVa3qZLBB9Zt4Xr6oAPxh4vRT5LWZbal16616VbDzgtUo0j8jd5b1b7hNW5XqVLWPbItvhjk4wIZkRoPYGlxMxwZyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نورافشانی آسمان شهرقدس در شب میلاد نبی اکرم(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/458928" target="_blank">📅 23:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW0ST3JZnzMi9dGj-74skx8AqfCtKqUGhZNY2hBgaZMFlpBBxzGlatutKYT_meQJJU9tf2wUzr9WmlQ9DzgLD0nI15oSbLQ58GeOpuvd0jm1E5oLlphyYfj68pa95EqyO4DbbZUthnBFv0N_VUMwe7B6NVhIb2DAPNiKdU1yLfXu70Oxa03kfnsC1Qa87Sf1wYwIXiMdUAo9blmWI_e3ejZMUiPSFCKOB2XA_ibRtfK43fjH1hUgwcQoJkQ7NrenBazi3y0S_qVyju0Uk5Fx1hgOtDnKJDiNzOxUzXwrdX1Nu6eQo68AZPiEybnQJS0yT9tH1rnOZRpMuunZRdKE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات صهیونیست‌ها به انبارهای دارویی غزه
🔹
در حملهٔ پهپادی امروز اسرائیل به انبار دارویی بیمارستان «شهداء الاقصی» در شهر دیرالبلح واقع در مرکز نوار غزه ۳ فلسطینی مجروح شدند.
🔹
در همین ارتباط، مدیر بیمارستان شهداء الاقصی از جامعه بین‌المللی خواست تا برای توقف حملات اشغالگران به مراکز درمانی در غزه مداخله کند.
🔹
اشغالگران صهیونیست طی روزهای گذشته هم انبارهای دارویی این بیمارستان را هدف قرار داده بودند.
🔹
کمبود دارو به‌ ویژه اقلام مورد نیاز، افراد مبتلا به بیماری‌های مزمن همچنین داروهای کودکان و زنان باردار را تحت تأثیر قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/458927" target="_blank">📅 23:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b633bfd29.mp4?token=N7xVG9QX-9pFm5GldAOGn0xRec9tJW4_PsUE7WmwLPPdxnK_V6qaCRWko4c5g8EmPPUWqQ1tZHlROYg3LcrZMzs1OoThTsEa_-oqnnJ0g34FDvpmHYso2wH4Ra3YHY6AvpykAJqzgTcb8cmYw_wJ-x4Bfxxqs5ALS8lc9Svr4ru6foXTa3s0JD_P5ecNDGJ-ov6NBtVuqw3IFm0xkArxCPwsqWBTXnuEWOnjKNQRPOJ0i--tKLsdOnrX8mJDdrRdqn5_L7ff_ooKoCPfggDyLgJzUb_3x6aPqVZRWLzpFysGlvCAXDklX74ZwqBicurufO3ETD5GmFAOLCMNfdOv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b633bfd29.mp4?token=N7xVG9QX-9pFm5GldAOGn0xRec9tJW4_PsUE7WmwLPPdxnK_V6qaCRWko4c5g8EmPPUWqQ1tZHlROYg3LcrZMzs1OoThTsEa_-oqnnJ0g34FDvpmHYso2wH4Ra3YHY6AvpykAJqzgTcb8cmYw_wJ-x4Bfxxqs5ALS8lc9Svr4ru6foXTa3s0JD_P5ecNDGJ-ov6NBtVuqw3IFm0xkArxCPwsqWBTXnuEWOnjKNQRPOJ0i--tKLsdOnrX8mJDdrRdqn5_L7ff_ooKoCPfggDyLgJzUb_3x6aPqVZRWLzpFysGlvCAXDklX74ZwqBicurufO3ETD5GmFAOLCMNfdOv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت نفت: یک بانک ایرانی حساب شرکت نفت را بست
🔹
با وجود پیگیری‌های انجام‌شده، این حساب تاکنون باز نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/458926" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6pzhJ7ghALiMs1EDBkpB9WhFYDxSZpU8sRMnYwTxpulNlb6vkparZOUKgXjFcf5feLg-aQHafUtQT_QTh-YAmy7Ffq4sO_fCPRcNs5-xxQ6J_q8xf0FkXIp6J05vM98D_zvecIdVyUfx9K3Qpm59zRpkBeaI28zNjo0bhCMQMeCdUci6daUNIMhPB-_TroUdp3RiozUYcooXo1wkk7gj6wh5IE2Cp4C5q-rJBjMLCs59dDTtIQTjI66FpVvkco0asAlfK0cnlGy7q231iEwf9P8Vbw3XbAJI0so9VIiG7zg8AQ_R11mjbseVAiutO20DU0cO8LuNGOj6uioqKk7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فرمانده کل سپاه درپی قهرمانی والیبالیست‌های نوجوان ایران
🔹
سردار وحیدی: نوجوانان قهرمان تیم ملی والیبال؛ سلام و آفرین بر شما که با حماسه آفرینی خود عزم و اراده پولادین یک ملت عزتمند را در عرصه جهانی به نمایش گذاشتید و با غیرت و تلاش خستگی‌ناپذیر در اوج جنگ روانی دشمن بار دیگر "ما می‌توانیم" را تفسیر کردید.
🔹
درود بر شما و همه دست‌اندرکاران متعهد و فداکاری که شما را برای این درخشش امیدبخش پشتیبانی کردند.
🔹
در شب ولادت نورانی پیامبر اعظم(ص) دل ملت را شاد کردید. همیشه موفق و دلشاد باشید.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458925" target="_blank">📅 23:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
مراسم جشن «نسل نبوی» در گرمسار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/458924" target="_blank">📅 23:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxwPY4szMc5_Pedzvkg5zRVSxNezKaqxW0k6B2UKWi79eBA-RxL0_1MPEkBHO6xrgCcRx41tC3Qc--REhe1J5u6pSeCDMWDQkufzW7H2WdTB5_pLA5FDycJsPI4RlLGE5dFUMx4kz1ylvb80IdT9KxY-pPWMK81DLEzVqeR6yxup5i7B0BQ6wz2J23wIQQEpU0A7eOv9nNwYgRUxdiPNgZOe7ltZfwISjPT2zvdh99KEwE_UdE39axrrq0YpRhv3Hoab-o5IDQ6-WBn8CyysyyMDJGKchOhp4rT3jXZksYMBx9cwtWH_483oWBbAPfCY5XV5xQpc3hzB_qGsa139DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X67A7kPhglXc1AW2ysqo6PKdjiawiIQTZT7a28KJtfK0pl4Z7jPOZ1JlNhHCQm67a3ui86vNnhnBpWOxq6ACapljw85LAoa3Wm6Hx9MY2acQD7q15L6E3-i2qsq_seasLHLYa28GrP6QGP01RoGKZyANfrjbdxTLLv4xh-CY_iZ16_NlLbezJM18lSsFGGC1dKQP-PX2ua7YMmbIySaxtI6Evi8PE2AlSDWrxRIqrJ5nsMH4zYWNG8jICPI1qYZEdSVs0_bjy7BdfVlzxffvZKIdlK6xRS4_o_nYJdNPngyL8YvsTZ5NX-hePrXhxyDdHzr3m1hbnethRM11tEcvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6AVV2Xkrzv1R0NFAVQFV6D8tpkhA2m3cRyk5LmJsl7blyBgon3_ytSWbfLIPc0IACsroCViCEgQ08K_MTQI1CcyNJQMJXYCEDks9DvJ4G5vIE1WdExPFTx7TsuS86RTnsqz62VRaXoD8N5SCyfdm-rHNB6WbF9wyt0YXZg984tRbm0zVpL4uDfSgknADG6bA2PTP-g2e0Q2PvlK8C2wra85Zpgl1fmFjCVbYaMUboX8dQItN9LsaNfcaDiaejwlbGRS4VI89p3a06uAIexak8fXMMsyzRyy2NHSoz66mDwnI7rhzE38rjIK7ckoI6yXSIc5eC3uqU1Ar3doKKoaKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گرامیداشت مدافعان آسمان ایران به‌مناسبت روز پدافند هوایی در میدان خانی‌آبادنو تهران  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458921" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
اجتماع و شادی بروجردی‌ها در شب میلاد پیامبر(ص)
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/458920" target="_blank">📅 22:58 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
