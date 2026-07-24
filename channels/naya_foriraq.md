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
<img src="https://cdn4.telesco.pe/file/nrpSN10HLcftzlyOmHlW0YFm-bAsj5Htns0A75yny8FP5OhbCqbNZSrqvorwEMnqnK1ABsOOkBIewo9qdTmfcdvTKEJlQRblYQjfEPI46OlhmAgZuzyP4RwUVAIP-RRucVwmCWcD8Sqn-vNNdEsPFD4tjdek8C0_69446Qo9dB2Nd5KNY2bnGOqVhEumt25eMjLuj2Yv_eZxqwPYYG08s8r4l4GOs2KN8ZWk86rsfYR_23eySVFpfq8rvmYncICNr0EejpG4oRwwJ4L3a_18BoN5pfi1TKomtV_Z2pFh5dYR89vd2ZAqZFvJrQjoOVw2TdPmj0mg8e-TfDQtmfmCVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 23:41:34</div>
<hr>

<div class="tg-post" id="msg-85416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJCRai_134XeMWGUPcP1vdFsR3NeDsWaz0JZfdIbBfIhREO4HEN_uU7q4cxzsLS2Hz69ZEkd1Ao899mobdN-pnPFpIitB2-3t0ApKGdpUl1Lq93-EGFRIXAoas6CCJiQYCfCx2HWdbJmgtGD1DXKOjkCr1ttETDjQ7b47q60RnzMrIuCo378xs4dQAnlftCjTPyRPoXWxHR1oKa7GWT_nlyFla9RC5W3nVBwlHrjrIsKDTc3kBxLre4aLT2sFsclkcTioMvwWytEyHgxz4X8e0vamUNsVRkpX8o887FLt0O9SqPu4RPlFWXT3l_cB_f3lh6DKoAv2VBnnzhmIjYnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2suauiisL_eZ5D-59UKodYC-LanGk4Kslf7t7C-gtoiCEA2SbJZkzLYSPbDRbgWyDqoPzaJSHAD9O3ZwIHARc_JsiAWKkUdmH9nv4Wm5DY2MAKZHaUWV3cozYSd0mzEuDUlTgqLYaTVo-ROHlG4PAsHgvN46LKdFXAo_OPUuUx1gDE9qAJi3vQxIxHPExm0GJNe2b0mXBXWJ6O8-QbGREWxcuJgBmEYEPpiHZOyneami9j_7MuWXY3SYpLp24V9hUTLhcR2TEWqQ8mjoIGHDYVYNnNnUT5JGwPvN4b0emliWDxMofyXkHzhc7Oj4piiphkG95Pzbin10cLzaHFg9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النظام الاجرامي السعودي يستمر بالاعتداء على ميناء الحديدة في اليمن</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/naya_foriraq/85416" target="_blank">📅 23:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32f6837f.mp4?token=J2RGnmV28o3nNBUtVFlazzNU52H_lW87rZF5xi-mWKTQeJt5EdwnWDh3eFZ4M6J2i3f2sQTY68QJHh-BxhUEOYXIpcyBB25oQlIGP59wHygmRXjjYXZpXyF5FBtUqvy81W8VfWEpyn3jcVD2YxPLnMEDp7i3KKQ3fYzvA6fqAu9ytqJ4B7EyLmv7x1rQypb1FF2v7o5RsIwL36Ju0WFNlAeb5dzICLzo3de77qk0ffgd-m1HFaMQuLysToaKd_axdNnz_9L22fMbtYY7GZwJqwzlqy0WrvDPRoWI2PPjX40WIAPtvP4xnO9pPEJqHuh5JJL5gSjxqR-z7pReKdmoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32f6837f.mp4?token=J2RGnmV28o3nNBUtVFlazzNU52H_lW87rZF5xi-mWKTQeJt5EdwnWDh3eFZ4M6J2i3f2sQTY68QJHh-BxhUEOYXIpcyBB25oQlIGP59wHygmRXjjYXZpXyF5FBtUqvy81W8VfWEpyn3jcVD2YxPLnMEDp7i3KKQ3fYzvA6fqAu9ytqJ4B7EyLmv7x1rQypb1FF2v7o5RsIwL36Ju0WFNlAeb5dzICLzo3de77qk0ffgd-m1HFaMQuLysToaKd_axdNnz_9L22fMbtYY7GZwJqwzlqy0WrvDPRoWI2PPjX40WIAPtvP4xnO9pPEJqHuh5JJL5gSjxqR-z7pReKdmoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة من ميناء الحديدة في اليمن وهو يتصاعد منه النيران بعد الاستهداف الارهابي السعودي.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/naya_foriraq/85415" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA-zRm9kzmY1FznvzWlPvxOk4PJIXxbyW8CuDpt716epzpolStStlrHdQzUhT2ahBVEpFbY1CdrjN2Xytxg53T-B0dVmJjRBc3jHW6PJJ7_yvuAZbgjb4tyCuWrsFqchQZXf699iLGLnpGIed7Gw5QwaUzIKQ9kVDjdVHlFsJSpw0K7KSbBl3oQjdrTVr5diwFDqNKIQClIQ12p4YMCGWksF0g-h2-UmEJx3yGFCAPjrtAfmP3vDIVjfVjnKXv-VUPzUxhPj3DBBe7N0_fQtUduIrtjcfEnxAbI_T1aZvTvW0xBXw8rLCr3-UklKxT8b0dSkVH03_vKjLbQOS9nxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز تدعي هجوم على ميناء الحديدة اليمني</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/naya_foriraq/85414" target="_blank">📅 23:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رويترز تدعي هجوم على ميناء الحديدة اليمني</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/85413" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
🔻
حظرت فرنسا استخدام الأطفال دون سن 15 عامًا لوسائل التواصل الاجتماعي، لتصبح بذلك أول دولة في الاتحاد الأوروبي تُقر حظرًا شاملًا على هذه المنصات، في ظل تزايد المخاوف في جميع أنحاء العالم بشأن الآثار الضارة للمحتوى الرقمي على الأطفال.</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/85412" target="_blank">📅 23:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e996641e.mp4?token=M1igGPrTxlOFScUnxJb4oH50xa_4EdWuJVWuhyyx5rMNRFS31SvE1kjkU_9SznLandzHlb_y0amsVPBj2teS_n541gh64xviohnLWemY9PEIWQtHJXBui88H9g4WbH6fgJCcd5nRekpepXaGpOQkrod9gbinHoW8gyC2cSOPbbHbgYqMdDRQkfr9e7FsGlqBLdPg9omkckbNs4mdgAs8XJK16mR2-Z45PLNdwDU-YHiBZl5tu-oAp2UuuuCa3sza_lVZDeaudwFjC8-mgsFP5WfK0H0ehITQ4V7-dbow3fdujsspNmewVPu78rILpc6F4QpbxZrCvbEicpPOpPEfjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e996641e.mp4?token=M1igGPrTxlOFScUnxJb4oH50xa_4EdWuJVWuhyyx5rMNRFS31SvE1kjkU_9SznLandzHlb_y0amsVPBj2teS_n541gh64xviohnLWemY9PEIWQtHJXBui88H9g4WbH6fgJCcd5nRekpepXaGpOQkrod9gbinHoW8gyC2cSOPbbHbgYqMdDRQkfr9e7FsGlqBLdPg9omkckbNs4mdgAs8XJK16mR2-Z45PLNdwDU-YHiBZl5tu-oAp2UuuuCa3sza_lVZDeaudwFjC8-mgsFP5WfK0H0ehITQ4V7-dbow3fdujsspNmewVPu78rILpc6F4QpbxZrCvbEicpPOpPEfjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  إذا لم تنضم المملكة العربية السعودية إلى اتفاقيات أبراهام، فلن أقم بهذا الاتفاق.  كان هذا الأمر مفهومًا دائمًا. كانت المملكة العربية السعودية على علم بذلك.</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/85411" target="_blank">📅 23:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521af5d459.mp4?token=A25p86P6bqAADewm30JBGd_vIXUOJCQuyWgtKBqrzngk_s50xblUoCr02N6EcCoQmhIYmBc6XWITIGe369xIbSsE2ebLTgaq1bWidf3cTr-MXt1Xz216rcw-qmWwRuCkIIXOMrw7D-3VlwNDDn0ZoDM0SWYtviMG9RRY0X9q1YRAWBY9TjNdrKuymlzCOeLVAqsLL6S9YBy1TAIsax01rXi4yyv01vdijaEPLL6IWUARXdHYOL0F7UwhEvqKiXkQhddaMOoIV8pqarn7U9FbSHFDScEr4KLhcX5xnaDt5C9p0iCOj-FfaIgs_5eAKEyN_v0vDeBiT9Gn6TQ_onIMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521af5d459.mp4?token=A25p86P6bqAADewm30JBGd_vIXUOJCQuyWgtKBqrzngk_s50xblUoCr02N6EcCoQmhIYmBc6XWITIGe369xIbSsE2ebLTgaq1bWidf3cTr-MXt1Xz216rcw-qmWwRuCkIIXOMrw7D-3VlwNDDn0ZoDM0SWYtviMG9RRY0X9q1YRAWBY9TjNdrKuymlzCOeLVAqsLL6S9YBy1TAIsax01rXi4yyv01vdijaEPLL6IWUARXdHYOL0F7UwhEvqKiXkQhddaMOoIV8pqarn7U9FbSHFDScEr4KLhcX5xnaDt5C9p0iCOj-FfaIgs_5eAKEyN_v0vDeBiT9Gn6TQ_onIMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/85410" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/85409" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/85408" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD8KTPzRgFhVsOnIOtSVyBrdHb5lYmB1zG6_yPFBfny4tY7ACHe4zvHYMbMdHmspdsTo-pH5WGUiK5c6ndp-qCd4X4-RbTZ2cYT8BVliDP7fPAOFswn4_9j26O3GMeScQqmQ8t2xqANCbE6l8d8UUJbOgKMFI558OsxqxsLHNgGEwMhuhJUyZYVKulg93Vz-b1MgRw5moCa0X4KRFRWniT-t9KMHrllTxpocXXx44dsB91d8pv4lsibRL1VFbs2RsxKsZqC1hAew38ftNfq1kk87e3zds_qUbLXbhXn6DHrE1texz4GHLvXuAtf4YrFGKUINIOj8-OmBTWcuVSJ_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترمب: الذخائر جاهزة للضربة الكبرى ضد إيران</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/85407" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇸🇦
‏
هيئة النقل السعودية:
السفينة المستهدفة في البحر الأحمر تعرضت لإصابات طفيفة في بدنها.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/85406" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامب: يمكننا التفاوض ونحن نجري محادثات مع إيران</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/85405" target="_blank">📅 23:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0368971c8.mp4?token=MC4sDIoxWpHcN0b_RgZJmGAp2DdHfEg6bxRFBuiK2MyAJKJzs9kNFgC6QdhP4IX4OBQ8ACsH51z9MYV6dJirK6aBWZQwIbCcIGc1JTFodY1WprEzWj5JKfFB5ZGbD_q-RMD3eW6Km_YFjceZNdLraKOgcA12cznTXR7QXFIdAupNAyd4yS6eG6V-1zRled7qaSmJ2kC2aghudnyv2xL0PYbIP-8ALbqaMeIumfsed7LhyeBKdBFHNQju3TELd2IUakVCo-vNRktqW0jqA_8Rrx7fsNLJOJx6wWIlxlCYaat3DItqBR1iB0dz0L_UxFAu1F4DUiubU-KlewGMTKrUDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0368971c8.mp4?token=MC4sDIoxWpHcN0b_RgZJmGAp2DdHfEg6bxRFBuiK2MyAJKJzs9kNFgC6QdhP4IX4OBQ8ACsH51z9MYV6dJirK6aBWZQwIbCcIGc1JTFodY1WprEzWj5JKfFB5ZGbD_q-RMD3eW6Km_YFjceZNdLraKOgcA12cznTXR7QXFIdAupNAyd4yS6eG6V-1zRled7qaSmJ2kC2aghudnyv2xL0PYbIP-8ALbqaMeIumfsed7LhyeBKdBFHNQju3TELd2IUakVCo-vNRktqW0jqA_8Rrx7fsNLJOJx6wWIlxlCYaat3DItqBR1iB0dz0L_UxFAu1F4DUiubU-KlewGMTKrUDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/85404" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3a1afad1.mp4?token=YWViuqgeKTZD_7GZC5b96RL5qzOlV-3Y0CbRRUV9UKVjDLdge2_5lUjqbC8J8m3GluW20kq3cHd6EPo9HKjLPSqm5ed9o2BBj2SVv5CWoLBqxG_Ib_sLIu15VQXGXM6O65H0GVks-SftK8Hh7sf6Ea84zEPfnpY2eA69_ScaNL3nwWTHURHAIZmgUBCH4GVD62IO9SjJoRHOE6E7WIz88ZOzzgmqb1BoOKM_flaJU1YT3XdqJkAdPVQZ833bKNoL2ptR8kCk1fRRwqjRJVzMvU17g2nFzNSdVJ2ovBONHKVU4wRuFLUQ2N3FuhRxreGmjqnXQHQEWh2IUU6Qcjd3Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3a1afad1.mp4?token=YWViuqgeKTZD_7GZC5b96RL5qzOlV-3Y0CbRRUV9UKVjDLdge2_5lUjqbC8J8m3GluW20kq3cHd6EPo9HKjLPSqm5ed9o2BBj2SVv5CWoLBqxG_Ib_sLIu15VQXGXM6O65H0GVks-SftK8Hh7sf6Ea84zEPfnpY2eA69_ScaNL3nwWTHURHAIZmgUBCH4GVD62IO9SjJoRHOE6E7WIz88ZOzzgmqb1BoOKM_flaJU1YT3XdqJkAdPVQZ833bKNoL2ptR8kCk1fRRwqjRJVzMvU17g2nFzNSdVJ2ovBONHKVU4wRuFLUQ2N3FuhRxreGmjqnXQHQEWh2IUU6Qcjd3Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85403" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38cc825320.mp4?token=eiZ3LteBDGeVYlpugQ6lf0Pf5Im5GqlIgZI8YDKW2sUZgwwa2qZ3AU3Rk9LAiRADNfG-5GvSFVnLCRMzMXTQ0CFOS8gu8MU0iRj6CXg72dn1EUKq_Gvr3ePGszLWH4ZOQ72zC7OkKphS3qAyRGN-3uxVSr5zDnNGh8e6AtOdjQj8aWyHokuBtglgPayDC520eEfAOFVSDfzTHG1TmtH3wx6qxUuAOZo5k4azeozfRSmURc6qHYpxiEgJcefzRCFFjU8TTEFCR6vLRAqOR3TX7R9U-nH1NNs28PC088lc49k974QRVaVhWwdKeohwD1YvMTiZJ1zmKUtAPcCdiRY0WEpmRK1UW1juwff46exVOkqyg4X36kbUAY6W-xCIYh_iHZkdSDDkEVUo0cA3Ngk3v2mpV7rOwGN4i-vaLIft8VrI9V51V3r3CYOc_f-XcFX9qYDlV--12i3It3LrHWbMcoRrdK996kj4oEADNLtMCKGQTDNr3ESsIjmMyT5eJpnBBrb77hmQu_StvGhpl8DrjxqUHwqY-iawZkvvxUIqYl-LToSLCqHd_7GbkSlZk-P-ro9mXU0iC51JMK63EQ4TZL_r75Q83eyClH5UiX6pZmM9kE0hLpNnOPskKhfPVZ20Wr0cL_xGSpIO1mNDZCxnqNVnAThOhhL-A-5lAxCx4q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38cc825320.mp4?token=eiZ3LteBDGeVYlpugQ6lf0Pf5Im5GqlIgZI8YDKW2sUZgwwa2qZ3AU3Rk9LAiRADNfG-5GvSFVnLCRMzMXTQ0CFOS8gu8MU0iRj6CXg72dn1EUKq_Gvr3ePGszLWH4ZOQ72zC7OkKphS3qAyRGN-3uxVSr5zDnNGh8e6AtOdjQj8aWyHokuBtglgPayDC520eEfAOFVSDfzTHG1TmtH3wx6qxUuAOZo5k4azeozfRSmURc6qHYpxiEgJcefzRCFFjU8TTEFCR6vLRAqOR3TX7R9U-nH1NNs28PC088lc49k974QRVaVhWwdKeohwD1YvMTiZJ1zmKUtAPcCdiRY0WEpmRK1UW1juwff46exVOkqyg4X36kbUAY6W-xCIYh_iHZkdSDDkEVUo0cA3Ngk3v2mpV7rOwGN4i-vaLIft8VrI9V51V3r3CYOc_f-XcFX9qYDlV--12i3It3LrHWbMcoRrdK996kj4oEADNLtMCKGQTDNr3ESsIjmMyT5eJpnBBrb77hmQu_StvGhpl8DrjxqUHwqY-iawZkvvxUIqYl-LToSLCqHd_7GbkSlZk-P-ro9mXU0iC51JMK63EQ4TZL_r75Q83eyClH5UiX6pZmM9kE0hLpNnOPskKhfPVZ20Wr0cL_xGSpIO1mNDZCxnqNVnAThOhhL-A-5lAxCx4q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:
يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.
حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.
إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/85402" target="_blank">📅 23:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
‏
ترمب
: لن نسمح لإيران بأن تكون بلطجي المنطقة</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/85401" target="_blank">📅 23:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
🏴‍☠️
زلينسكي : ‏
نعلم من معلوماتنا الاستخباراتية وشركائنا أن الروس قد جهزوا صواريخ لشن هجوم واسع النطاق جديد على أوكرانيا. قد يقع الهجوم اليوم، ولدينا معلومات أولية تشير إلى أنه قد يحدث خلال الـ 48 ساعة القادمة. لذا، نرجو منكم توخي الحذر والانتباه إلى تنبيهات الغارات الجوية. ونتوقع تفهمًا من شركائنا، فالدفاع الجوي هو أولويتنا القصوى، ويمكن للشركاء تقديم الدعم اللازم لنا.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85400" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
🇺🇸
الخارجية الأميركية:
إيران قد تستهدف المصالح والشركات والمؤسسات الأميركية بالمنطقة</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85399" target="_blank">📅 22:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3fapRW5z4Ds609J6-kzNaXDKaqxz0YFy7R7X-MV1ipncLwJol0v6rITY9ZhSAXqvmvXZhOX3nOUBUJwXge61j1XL5ruHNXIFHgwlTFjCAzb4YyO4PRheeOhk9BIBTvjEzZEP9ajpgLxjINUnnAcpYMLZN5ro8Bz7-CAwGk801clwWmW0_v-4MPorAt2XT7WZ7H8nLEoNLB8UWvg3IdK-RZxi7GsXZrcBar0EUnmMb52p7XzPaICdpR7-rPUz3l8Bo3mS9EchBUoH_6pWRPZljPSw9f_g1FKy4t9uKDYslbe6FEevaiw-_47LnPiGzQezcoDPrk3L6LsINtg6fsD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
نشاط لطيران لوجستي تابع للقوات البريطانية في شمال العراق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85398" target="_blank">📅 22:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be502294d3.mp4?token=R0FBGUMa-xnPbcAaFDO6ypP11UbDgfLKs1YA7qU6PQ8NbwhPs0cKfqCTNQOml2XhBiUSMV6Mw8gpIo-3BPlFSchS_qmYLmx1qXMn9sgC3OaYjxvsVlxflMlKqBaiisnaDc01WTMw-q4lw60x3zqrPLS5zVxfjw9oFpxzEQF9CkV6ZzROWypk-fA2JtqihOLM-fV-wpEPi0BWwKLQG8aiKyIdAcst25XzJ2NU2RJl6vy-QimhByLaj0l7ao6tKJKMMogYWZcjNGqD880KiYwgzQ98nt-XwOYaSbN3fHMFoNAAJXqlNWgvsRTMOZilQckT1_j0N3fPMWg1ft2E189fDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be502294d3.mp4?token=R0FBGUMa-xnPbcAaFDO6ypP11UbDgfLKs1YA7qU6PQ8NbwhPs0cKfqCTNQOml2XhBiUSMV6Mw8gpIo-3BPlFSchS_qmYLmx1qXMn9sgC3OaYjxvsVlxflMlKqBaiisnaDc01WTMw-q4lw60x3zqrPLS5zVxfjw9oFpxzEQF9CkV6ZzROWypk-fA2JtqihOLM-fV-wpEPi0BWwKLQG8aiKyIdAcst25XzJ2NU2RJl6vy-QimhByLaj0l7ao6tKJKMMogYWZcjNGqD880KiYwgzQ98nt-XwOYaSbN3fHMFoNAAJXqlNWgvsRTMOZilQckT1_j0N3fPMWg1ft2E189fDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
مروحيات عسكرية اميركية تحلق باستمرار في اجواء قضاء القائم بمحافظة الانبار غربي العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85397" target="_blank">📅 22:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات تهز شمال الكويت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85396" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85394" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الولايات المتحدة قصفت موقعا قرب معبر الشلامجة الحدودي بين العراق وإيران.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85393" target="_blank">📅 21:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لحظة سقوط الطائرة المسيرة في أحد مقرات حزب المعارضة الإيراني الإرهابي</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85392" target="_blank">📅 20:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoZSCJBN_dTDgimSxaTVODugQ37E5V2HKF5pp53MFuP0lCGxIK2g2cvdWZixzqyLpcWhbv80X1cGq0Zpi0ZwHjNZ6TFnfZKaY8LtHR5G5SS2ilGLt79XvaVBZpRvRPKPTZzriKqu6BqHejrsiVSoFDQQI0cuuWNPI7Apkyc1k3h5vqa-wGB79UXTb-oLGtwNn_-S10EmctZ1dMuDvvheHmlUspSPdL0jUwzfnNodO87LvzTgLQR5ThLM26-g64XjfB6VGF6mfOer0IBLkuDg_c7cNQA1Mby6Bf9sHfHm_DNx6Lvjcsw8xCIu1FU5mw7HnPGs_wqm-gTrvfpvZwf3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: الاتحاد الأوروبي يستهدف الشركات الأميركية الكبرى بشكل مباشر، وسيدفع ثمنا باهظا لسلوكه غير القانوني ضد شركاتنا، وسوف افرض رسوم جمركية كبيرة على الاتحاد الأوروبي قريبا.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85391" target="_blank">📅 20:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdZMR5HDWVFrYJyUWBoQSRCyXYxy4JUKwcZNOzAL9NMZ3fLhhqVOhaAUFwDYDpbuk3bLjADeISaYmrSPyY6KEEXmWd5APf5jWWvbxWkuN-1cIpE-ymNY3_-aEgvsqyRUnRnEpfE3lKCa6pfkx4fhpflK4u70GwtzAxcqr1SBYxAbwnAq20mcs1aAtza4NFlyMngmG64EWOA6tCxjjM1LP3EJpnozPvYNgiE_Ie6NEoKUUCUvG7_P4ErOT1jF7wj8WKDYgr3x98nUwWFOhQL6iM4Qy92Rpp78Oa8qLRpKaszCmXitAAH4rhfIrEhTUn9LkrcqI9iy-LZhYHUOBdZ3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو الاء الولائي:
افتحوا أبواب الحصار عن اليمن يفتح لكم المضيق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85390" target="_blank">📅 20:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHtlVNNIHMSSIGe5gng3L0gQLUFysmsYHZFTSkXpJU62uMAslRV3yK7p8kYbu0XRdMQgzpd0YuFEGhiMirg7d2LATCXrCGlV2W7kpnE_0XPAL0JdsC6k5Z_30_B1QWsGUzACeM40Q7bXJNFYRaEV_dZTUd1Y5SBs52XZEbbfekVzjRVe-01-Akk-Y4yNF5-xiT9jHHjLT6mdJfpHB2v5VJXBVBpHbyYBbKXC9wf5ar82vOuLtii_iPJ1-NkzkqmFhI4qrOJSCofaaCH-Xk9Ejf9zM5D3FzbhKUENx1QEN74leGVaWiSN3VlWF0er8H0mhbZuykUQCCH9t0iGIK0cJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
استهداف مقرات الاحزاب الاثنية الايرانية في محافظة اربيل شمالي العراق بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85389" target="_blank">📅 20:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmtOSqRGdIDRyNDFXBf10u6ejnbu_-hBd_jk815vnp_DfhSBDlVEO3l6JzFzXOairjmadNPvDg0YZ833PO81jAtjK0QMWOaG_IqlOk92cHWnfKfZSZe9FyDhqW3bvxSUWiy68hcD05HAoWlQ83gJscQVfW5cQYi2b3RlsuMMGiXuix-wn91VsCynbZ6TzTZL_gEbMBb3Kh-iWPLBtA_JyhlFogpJ-tfAkzWe0ry9IcR5sByvL-Jo1i-T3YoD3lVHUly_XC4o6reSSuvOPZ-n6HH6j3ClcsRzwu8LmsWPBum3aW46ApHGplDoy5g5ZUbqIZDzUglGjjZ1UWO-He0M4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
استهداف مقرات الاحزاب الاثنية الايرانية في محافظة اربيل شمالي العراق بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85388" target="_blank">📅 20:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82bbdac65a.mp4?token=FHWC3wNdXAmn6nImGE2lhKsNuWq5m8YhkNcHcMyRIjiCKS22PUhAzINAfpZP6VpfOAjFuPbMO3UmkLi_ZfzfIg4jUlR0Uu8vF5tXsFDA9CKK031muyobHzPjvySOxw5q4RCePNQbdLbDVVYE8yjxeCVw2_wRYWoavsW0D_tRHikSFteqY9uCkpSjXaNFiLWIY-2V90iHLxpgnZoA0q2DfQBCRvOGF6-xgQJ0re8cW0jyDNKw3zjl8PTJRNhn_HCOn2kLZIrih2hdHbxk2TfhzMJMtxdjkzWG7AMBWux4YhEyaoXLDRlOc9NQQDxhtBCwgMp7j89aVsuwp3GcEw21CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82bbdac65a.mp4?token=FHWC3wNdXAmn6nImGE2lhKsNuWq5m8YhkNcHcMyRIjiCKS22PUhAzINAfpZP6VpfOAjFuPbMO3UmkLi_ZfzfIg4jUlR0Uu8vF5tXsFDA9CKK031muyobHzPjvySOxw5q4RCePNQbdLbDVVYE8yjxeCVw2_wRYWoavsW0D_tRHikSFteqY9uCkpSjXaNFiLWIY-2V90iHLxpgnZoA0q2DfQBCRvOGF6-xgQJ0re8cW0jyDNKw3zjl8PTJRNhn_HCOn2kLZIrih2hdHbxk2TfhzMJMtxdjkzWG7AMBWux4YhEyaoXLDRlOc9NQQDxhtBCwgMp7j89aVsuwp3GcEw21CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طيران امريكي من طراز شينوك يحلق في اجواء قضاء القائم في محافظة الانبار غربي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85387" target="_blank">📅 20:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇨🇳
جمهورية ‏الصين الشعبية:
سنواصل لعب دور فاعل في استعادة السلام والاستقرار بالشرق الأوسط.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85386" target="_blank">📅 19:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmDqDy_lXcrzwjBgRpa9CRn3XtYH3EE-YwxgYy-elOAXRsfo0Jqs1q7X3tQzXTWSWHTxqMjcJd6nv58f51OlDbaD3OJymizy0106ftqPdim8J1rq7Fs6tpUNY_JmFTW3ZAzvI4rx1E9Gud_QigTxScuTbOKlfVhKABGZVDGxWiydudGWvsyOE97-8F6AqwexFogTT9qMRH2S91ggnXfN_otxXdhdN867RNa08AHC4DpmNOBnYJbIGVb-Oy7lHVo-KShUmtuprtQMMmzRue8aAM-63vUBTjbvKEijnSgnIoOsJGKbgK0QdfLjDenKVS1BvsM20TAI5b497L3taBEkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85385" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDpRE44tVf_Gy4Lz_3IagbzyWqop10ORJH2Crx7pAqpxG0WxUcnetM_rxa5l2m8b1Di_6TEaF1rkdDdWvHRN21Los_5Y7N5YN606RpqEYGVhUaBN_FZycFlANdiWIRLt47131w7CqW5lSRFf-_VfwxUo2-cvXIBHQmJKRb7evNBLcpdUTNiSUc0jHUsJGNtAI0V2pXOXvteWM4ayZRzIn4BJbUv-WjURSh2KVDIXmsRP_cZJbxkoY4iCMhnzxxiHWqCwx7PtpwsKNURC-WKrZIiP_sMZPip3QW3oedeqPnyDhQP_9h_LkW4_s_BB5c7Xsqg78Lzdh4Lrv49wVxQ0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء:
مقابل استشهاد كل مواطن إيراني، سيصل جندي أمريكي إلى مصيره لقد أعددنا لكم تذاكر مجانية ومباشرة إلى الجحيم.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85384" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇰🇼
انفجارات عنيفة في الكويت.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85383" target="_blank">📅 19:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية بالأردن: على رعايانا مراقبة معلومات الحكومة الأردنية بشأن التهديدات واتباع التعليمات.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85382" target="_blank">📅 19:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏إجلاء اكثر من 45 ألف فرنسي من إقليم لاجيروند "وحده" بسبب الحرائق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/85381" target="_blank">📅 19:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية بالأردن: على رعايانا مراقبة معلومات الحكومة الأردنية بشأن التهديدات واتباع التعليمات.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/85380" target="_blank">📅 19:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
السفارة الأمريكية بالأردن:
على رعايانا مراقبة معلومات الحكومة الأردنية بشأن التهديدات واتباع التعليمات.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/85379" target="_blank">📅 19:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDLKSXTOK5NEhJKI-jiEDgwB_SH6kVMQ-diU0qSfwGd7ZYUT2d05akOjSTOkItybw1gJNIPK4YEQ4XkoOrsxjbN3UoPFAarI6gHi_Qguibwf4_3CRHtocohfQkx1BNF0I64Bo2ffGOukAtG3JEPt8cleITDuKREZoo6BeeVnNAEPf0oi5-G86tPDsIp9XBi83cL4faR_NKd6O-hy5ypjOs0uWjtHNYvnr5mnAMRrdA_saNkQNhM8RFD_5iD6JYcjrAvMV49C_9k3VBFNZ2ql3a4MUT7rUaxIYRaVZS7d_q1TyWW5YJ17Ld6JIIa03ssPwxd7zV0qOcOFPrhuN2DFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب
:
السيد الرئيس شي، في اجتماعنا الأخير في بكين، الصين، أخبرني أنه لن يقدم أو يبيع أسلحة إلى الجمهورية الإسلامية الإيرانية بأي حال من الأحوال - وتضمن هذا التصريح الشركات الصينية. نظرًا لعلاقتنا، أثق بكلمته، وعلاوة على ذلك، فإنني أقدم له خدمات كبيرة جدًا أيضًا.
وبالمثل، أخبرني الرئيس بوتين، على الرغم من الحرب المروعة التي تحدث في أوكرانيا (إلا أن العلاقة لا تزال قائمة، كما هي الحال مع الرئيس زيلينسكي)، أنه لن يبيع أسلحة إلى إيران. فهو يفهم أنني لا أبيع أسلحة إلى أوكرانيا، بل إلى دول حلف شمال الأطلسي. إنهم يدفعون السعر الكامل، ولا أعرف كيف يتم توزيع هذه الأسلحة.
لذلك، أعتقد أن دولتين رئيسيتين غالبًا ما يتم الحديث عنهما فيما يتعلق بإيران، لا تشتركان في هذا الأمر. وإذا فعلتا ذلك، فسيكون ذلك سيئًا جدًا لهما - بالتأكيد ليس في مصلحتهما الفضلى.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85378" target="_blank">📅 18:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الامين العام للامم المتحدة ‏غوتيريش:
قلق بالغ إزاء استئناف هجمات الحوثيين على سفن تجارية وتهديد الملاحة بالبحر الأحمر.
وحصار مطار صنعاء ما عليها قلق بالغ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85377" target="_blank">📅 18:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e25c329d.mp4?token=Nhtjy2aF10mIWStBULkkOIPviZ18faBYi8aHP5gtf6uiFPFE2slqw3LJMZ3iaHZB7GjZgXBxUmbreKIlQkJmLGaQyI875iuUyesKLE1wujipD9cyOb8wReLi3GTGVTIPh-44mhM463quE6wCBtQ_i6pVKJmdhQ96I2W7R8T7nFyxCdPnSIvnbcLYHPfdOwO74TXX0zoFg8nagzza1ZcUjKtLndkeeCIxf_pVDg-7PkjHocJJHm8ZQbOqmsJndBnbbUsO0v8go2TXXg0GWzgYUHa82thFJb_Xql4EJeXrroq6BksaR6jSEgiA8s9_mivlaWf597VSlLcEM4_F4hTCijSo6DlmQQlFVbszUzj5C00IU3eOH0CUMbYgZhaOsDbX3S6cs8ISfvc3kZf2Mk8fVA-UrOc4DTMiRwAPzMrUMjNQ9OMMl7Tj7jUIvoI6hEeGkWbmyBQrHg23GUxz_lL7AfSLC5a391_07H26UN_qJv2f2ue_jQYJLJ5cGGZDg45blcKrNGXa2PkPrEe3b9CiCITJtZz38oIY_LiVOelZ_pPPn-Rc6goSaPOI3PwlkQEIFcr7gh3gFtSnxf05cSKeXBxls2vtjJaYQDc30ZbddfMhxmFQbfw6ec4H42ZXw2C3QoyYNGK-01gjpPP4Tfo9UuuKY2YDPlmBYGLpDMe_Qms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e25c329d.mp4?token=Nhtjy2aF10mIWStBULkkOIPviZ18faBYi8aHP5gtf6uiFPFE2slqw3LJMZ3iaHZB7GjZgXBxUmbreKIlQkJmLGaQyI875iuUyesKLE1wujipD9cyOb8wReLi3GTGVTIPh-44mhM463quE6wCBtQ_i6pVKJmdhQ96I2W7R8T7nFyxCdPnSIvnbcLYHPfdOwO74TXX0zoFg8nagzza1ZcUjKtLndkeeCIxf_pVDg-7PkjHocJJHm8ZQbOqmsJndBnbbUsO0v8go2TXXg0GWzgYUHa82thFJb_Xql4EJeXrroq6BksaR6jSEgiA8s9_mivlaWf597VSlLcEM4_F4hTCijSo6DlmQQlFVbszUzj5C00IU3eOH0CUMbYgZhaOsDbX3S6cs8ISfvc3kZf2Mk8fVA-UrOc4DTMiRwAPzMrUMjNQ9OMMl7Tj7jUIvoI6hEeGkWbmyBQrHg23GUxz_lL7AfSLC5a391_07H26UN_qJv2f2ue_jQYJLJ5cGGZDg45blcKrNGXa2PkPrEe3b9CiCITJtZz38oIY_LiVOelZ_pPPn-Rc6goSaPOI3PwlkQEIFcr7gh3gFtSnxf05cSKeXBxls2vtjJaYQDc30ZbddfMhxmFQbfw6ec4H42ZXw2C3QoyYNGK-01gjpPP4Tfo9UuuKY2YDPlmBYGLpDMe_Qms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طيران امريكي من طراز شينوك يحلق في اجواء قضاء القائم في محافظة الانبار غربي العراق.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85376" target="_blank">📅 18:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85375" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85374" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني عباس عراقجي:
كلما اختبرت واشنطن بلادنا تلقت ردا حاسما من جانبنا لكنها لا تزال تواصل النهج نفسه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85373" target="_blank">📅 17:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇮🇱
"رئاسة الوزراء الصهيونية":
بدعوة من ترامب، سيتوجه نتن ياهو يوم الاثنين المقبل إلى واشنطن وسيلتقي ترامب يوم الثلاثاء في البيت الأبيض، وسيشارك في مراسم تشييع السيناتور ليندسي غراهام.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85372" target="_blank">📅 17:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#ترفيهي
🇺🇸
وزارة الحرب الأمريكية تخفض عدد أفراد الجيش الأمريكي الذين تم إدراجهم كقتلى خلال الحرب مع إيران من 18 إلى 14 وفقًا لموقعها الإلكتروني الخاص بسجلات الضحايا
ثلاثة مسؤولين عسكريين لصحيفة نيويورك تايمز: هذا التغيير يعكس قرارًا بإزالة أربعة جنود قُتلوا في نهاية الأسبوع - ثلاثة في الأردن وواحد في شمال العراق - لأن وفاتهم وقعت بعد إعلان الرئيس دونالد ترامب عن وقف إطلاق النار في أبريل.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/85371" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2DPMoOTxa7rWPnUpQ6sfCS62rWnBE00O4lM-ZAIGkmLLQFjYhCAqzpfM5smmBfsY9PIf49slQhOwMV-HyZ2HnDg8Je84ebIIwBDw1mKUM0CBa_1h6MIVP5AOT6S2pOB6XDM2bnTdtTqgVVsKudvaeXwRINNYFn-wrBwoaUjsHa0eV5DUxWkGwVcY6Qb6Cavh3a1gBu4LoW8azE77yUYJsFuQ4dVUGBdj4MNHT7ZTa9vLTuOLlraiBH3DbuauwD5WlyomQgWOsKtG7_ClizmxdlsuS-VhjAWmVCjXqtcAI_2_RnVwc7uxLDLjr6kw-wLo4vQyiny_Fnr5juBiAUSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
جيش العدو ينشر متألما:
هذا ارهابي ملحد وليس شيخا.. مشاهد توثق لحظة الاعتداء في قرية تل صباح اليوم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85370" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حزورة بليرة
زيارة امريكا ؛ البو عيثة ، الرادارات السبعة ، زيارة ايران ، المدائن ، الأتراك الثمانية شارع فلسطين ، عودة عبد الأمير الشمري اربطها وتربح سفرة لجزيرة بوركينا فاسو
حارة يا مسلمين</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/85369" target="_blank">📅 16:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
محمد عبدالسلام - رئيس الوفد الوطني اليمني المفاوض:
لا إغلاق لباب المندب
كما يروج البعض وموقف اليمن المعلن من قبل القوات المسلحة اليمنية يقتصر على حظر بحري يطال الجانب السعودي فقط ردا على حصاره اليمن ورفضه القبول بأي مقاربة منصفة للحل تضمن أمن وسيادة واستقلال الشعب اليمني.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/85367" target="_blank">📅 16:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/85366" target="_blank">📅 15:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85365" target="_blank">📅 15:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85364" target="_blank">📅 15:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoI8hmMWzhFSriYSpRX0ol7dfNUgTlgMJ1q5an3HNVmZvTE9pkn8wZhYYkNpc5NhsCYfdcwuKqcNi1O5IxtBfe1vAJ5tBzqjRkXr4DPP-d6RBj8iiSWLjJbT08KOvB6GrucJ1X2Mi4YHj8tST7SrwhCgEL6Ll7sMn26-FDyao-7lgB22Ji8m9I4megUAh_M-KF-a-noH1kUZvz1k4PPvndZI4w3UFNtATsIfpMmTGB5qjbbnRcgFmxfc6GiVBSSHZ368a9WIzxU_X0Uv9auFnWmCRzYcw-_-YhBjMLa1j3dpe-XzOiPRGKO-MiEU2ksgMOWuMuduk7GCzdURVenVgzI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310f040801.mp4?token=RmwVx81qFt2stioIQ-Xk35JBV28v-DlG0tqryvnwi_1vWLGaF-vU2wmGIV-c7xHKpn7gt8ULuhhDnhmvsPoxmq7EqEhN4VWvLyiwTw6-zc7yOsdO6iYRuUaExePhzJhXAPbwXJB2bXgjLpVxOLCVM7fx_SwZHgwyuTyaMiMjfR7zdDhG7JyzTX98LA0b3hrof3T1ZxgXyG_ySrMA5Sk1S0t1WJ4jXA2BkiMtiKv8akopnYQTYbwiEg5_GJDk0QVKsxvXuFO1CZBAKEdBiU-4E3JlsJTGOFTvgTPssrX8LaR5I9H4dB0NqkaHIuDbWIMLiA1Y4sXOg7GkoN0s0A5BoI8hmMWzhFSriYSpRX0ol7dfNUgTlgMJ1q5an3HNVmZvTE9pkn8wZhYYkNpc5NhsCYfdcwuKqcNi1O5IxtBfe1vAJ5tBzqjRkXr4DPP-d6RBj8iiSWLjJbT08KOvB6GrucJ1X2Mi4YHj8tST7SrwhCgEL6Ll7sMn26-FDyao-7lgB22Ji8m9I4megUAh_M-KF-a-noH1kUZvz1k4PPvndZI4w3UFNtATsIfpMmTGB5qjbbnRcgFmxfc6GiVBSSHZ368a9WIzxU_X0Uv9auFnWmCRzYcw-_-YhBjMLa1j3dpe-XzOiPRGKO-MiEU2ksgMOWuMuduk7GCzdURVenVgzI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الإسلامية:
في الموجة 27 من عملية "النصر 2"، وباسم مبارك "يا أبا صالح المهدي، أدركني"، شنوا هجومًا مدويًا آخر على قاعدة أمريكية في الأزرق بالأردن، مما ألحق أضرارًا جسيمة بعدة طائرات مقاتلة، وقاموا بتدمير معسكر عسكري أمريكي، مما أسفر عن مقتل وجرح عدد من الجنود الأمريكيين.
النظام الأمريكي القاتل للأطفال يكذب بوضوح على شعبه وعلى الآخرين بشأن عدد القتلى، وندعو المراكز البحثية ووسائل الإعلام إلى إجراء تحقيق ميداني في هذا الشأن.
في عملية أخرى مفاجئة، قام مقاتلو الإسلام بتدمير نظام دفاع جوي "باتريوت" ومنطاد تجسس تابع للنظام الأمريكي القاتل للأطفال في أربيل، واستهداف معسكر إرهابيين أمريكيين.
سيواجه النظام الأمريكي المتغطرس وغير القانوني ردود فعل مختلفة إذا استمر في أعماله الشريرة</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85363" target="_blank">📅 15:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇷
تداول ناشطون ايرانيون استهداف الجيش الأمريكي، المطار المدني في جزيرة خارك، ودمر أربع مروحيات من طراز أغوستا ويستلاند التابعة لشركة خدمات مروحيات الخليج الفارسي. وكانت هذه المروحيات تُستخدم في عمليات الإخلاء الطبي البحري، والبحث والإنقاذ، ونقل عمال منصات النفط.
‏ استهداف طائرات الهليكوبتر المدنية والبنية التحتية للطيران المدني التي لا وظيفة عسكرية يشكل انتهاكًا خطيرًا لقانون النزاعات المسلحة ويصنف جريمة حرب.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85362" target="_blank">📅 15:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
بيان لديوان نتن ياهو وكاتس:
أمرنا الجيش بهدم منزل المخرب الذي نفذ إطلاق النار تجاه الإسرائيليين في قرية تل.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85361" target="_blank">📅 15:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي ‏لافروف:
أميركا تزود أوكرانيا بمعلومات استخباراتية لاستخدامها في الحرب</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/85360" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZvpfc2x3Q3FGqo3uTPqUzvnFs8nFLFUi82dAHT70BIvkjUNOgJ3OBBmdSgkkfIcUM_5GbEsPSwrCKLGsx2rMylhU6Hn_vQaFi1EDn9GEFdSiOBHUMknsKo8CxPih0TbaxVs5HFlGPC292B5sbpHd9jb9ZmVxLs0itBlRgHitPCyVPFOngstVuk-AuaGo3CflUpt_X01y24aPwvHFK_HexJXPRLAdlAGz0RSS2Ens_L28p1hm-QNrHb0UeHrFQI55WNY-bAG8JcvESGendinpiadItgUeW_tAu0one_m73uGBBIXYzqCm3Rqjgnkmymz4k6RakMyTxEvOBGjslFc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
بيانات التتبع:
بعد مغادرة ينبع في السعودية، والمرور عبر قناة السويس مع تجنب مضيق باب المندب، حددت ناقلة غاز البترول المسال "جاس كينج" وجهتها مرة أخرى إلى "شيبا" ‏ويعتقد أنهم سيتجهون إلى اليابان عبر طريق البحر الأبيض المتوسط ​​- رأس الرجاء الصالح لتجنب خطر الهجوم من قبل الحوثيين.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/85359" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇧🇭
البحرين:
تعرضنا لهجمات ايرانية ونهيب بالجميع ضرورة توخي الحذر وعدم الاقتراب من أي أجسام غريبة أو مشبوهة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85358" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇱
اعلام العدو:
نقاش أمني متعدد الجبهات يجري الان بقيادة نتن ياهو وبمشاركة القيادة الأمنية، مع التركيز على إيران.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85357" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جهاز مكافحة الإرهاب في الاقليم يزعم:
قوات التحالف أسقطت 5 طائرات مسيرة مفخخة في سماء أربيل بين 9:32 و9:45 صباحاً دون خسائر بشرية، الطائرات المسيّرة أطلقت من غرب محافظة أربيل.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85356" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85355">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
حرس الثورة الإسلامية:
في الموجة 27 من عملية "النصر 2"، وباسم مبارك "يا صاحب المهدي، أدركني"، استهدف المقاتلون ثلاث مستودعات لتخزين الذخائر والمعدات في القاعدة الأمريكية الواقعة في العديري بالكويت، وتم حرق هذه المستودعات وتدميرها.
كما استهدف المقاتلون في الوقت نفسه برج مراقبة الأسطول الخامس الأمريكي في البحرين، وألحقوا به أضرارًا جسيمة.
العملية العقابية مستمرة.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85355" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85354">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7bbd-GznPVJq-Bj2tRX_DiCWIYkt1qkrx4GrFIxc4NAYYtrMBNLIIT76H068cxh95k3KY13lbw7ovT1c3Djnw9B01DpQbsc3kik4MNORm7wRcJQT_ZuNZ27xymiCovHkqMnSOXFfJZYW2uNxCr7BCH3TyUV9tvvJHlu5ibV8pMVFoZ5xp3ApLu8mbWyUTY7CBNfIkQdE3yxrgpcnY7Qo2_707d1AK69lzx4xRqDRlTRnGFVuoMu1FiKRVH4_auZARzzBQJzkQ2lliHAVrBY1hfv8IDF9v5_rY90_ZjFuwsOod_Xt-U3sKCJGi-02Gra4LtBCu9nLApAOrVc9llloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بيان تحذيري عاجل
إلى المواطنين والمقيمين في الإمارات العربية المتحدة، والبحرين، والكويت، وقطر، والأردن، والمملكة العربية السعودية، وسوريا:
حرصًا على سلامتكم، يُرجى الابتعاد فورًا عن القواعد والمنشآت والمقار العسكرية والأمنية، ومواقع انتشار القوات الأمريكية، وعدم الاقتراب من أي منطقة تشهد تحركات عسكرية أو إجراءات أمنية استثنائية.
ابتعدوا فورًا لمسافة 500 متر عن أماكن الإقامة السرية والتمويهية للعسكريين الأمريكيين.
وتشمل هذه الأماكن، الفنادق الأمريكية، والبنوك الأمريكية، والشركات الأمريكية، والأبراج، والممتلكات العائدة إلى عائلة ترامب، والاستثمارات المرتبطة بها.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85354" target="_blank">📅 13:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85353">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNdavMGZJ921obUA5jhYhLeICB-LRNd2ZdE3n7-iPGe9gVpiQy_g81Wu9pvKDkfoMbWoVqMlnKj8s54x0Um1K3zw2C3D2dy9h2dZM8ZH7OwMF9y9aDhcNtuD0TX3IVMQY5hSZL56OIz2-EBsyVvJsG767jNehuww3WlPLOjVeCxnZy7sKGsx5EhCalyp8ZJjKU6itrEmUG_rNj--kZ8567LkPI3eRUFo0cNoifIDe2TOUtqzrCbPoE-8SP3UHAj04N8AiJHUU16gKqU1LQba--trrwFcbjBAPSjEtGW-UuphdIE92Wov0eLPh_lr7WgwdmfQVgPOF3jd7wnmZdXR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المكتب الإعلامي لرئيس الوزراء العراقي: ما ورد في التقرير المنشور بصحيفة نيويورك تايمز بشأن الوساطة العراقية بين الولايات المتحدة وايران عارية عن الصحة ولا تمتّ إلى الواقع بصلة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85353" target="_blank">📅 13:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85352">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
أيها الشعب الكريم في الدول التي توجد بها قواعد أمريكية في المنطقة:
منذ خمسة أشهر، بدأ النظام الأمريكي القاتل حربًا عدوانية ضدنا دون سبب منطقي أو مبرر قانوني، وذلك بعد استشهاد أبرز عالم ديني وسياسي في العالم، واستشهاد 168 طفلاً بريئًا في نفس الوقت.
بعد 40 يومًا من الحرب، حققت إيران انتصارًا، وعلى الرغم من قدرتها على مواصلة الحرب بقوة، إلا أنها، بدافع من التسامح، وافقت على الجلوس مع هؤلاء المجرمين على طاولة المفاوضات وتوقيع اتفاقية إنهاء الحرب.
ومع ذلك، فإن الطبيعة الإجرامية والوحشية للولايات المتحدة جعلتها تعود إلى القتال وتتجاهل التزاماتها منذ الأيام الأولى للاتفاق. وفي 21 يوليو، ألغت الاتفاق رسميًا وأعادت الحرب.
بعد مرور 13 يومًا على استئناف الحرب، ظهرت آثار هزيمة أمريكا مرة أخرى، وأدرك العدو أنه لا يستطيع التغلب على قواتنا المسلحة بالعمليات الحربية. ولكن، بدلًا من التراجع، لجأ إلى ارتكاب جرائم حرب، مستهدفًا الجسور، والمرافئ، والقوارب، والسفن الصغيرة للمواطنين، والمركبات العابرة، والسكك الحديدية، مما أدى إلى استشهاد المدنيين. وفي اليوم الماضي، بلغت الجريمة ذروتها عندما قتلت وجرحت زوار زيارة الأربعين الحسينية على الحدود العراقية، وكشفت عن طبيعتها اليعزيدية.
نظرًا لأن استمرار مثل هذه الجرائم سيؤدي إلى معاقبة المجرمين، فقد هرب العديد من ضباط وجنود الجيش الأمريكي المتجاوز خوفًا من نيران مقاتلي الإسلام، وتركوا قواعدهم، واستخدموا مباني في المدن لتنفيذ جرائمهم. لذلك، نحذر جميع المواطنين في البلدان التي توجد بها قوات أمريكية، من ضرورة الابتعاد فورًا عن محيط يبلغ 500 متر من أماكن إقامة وتمركز القوات الأمريكية السرية، لكي يكونوا في أمان.
يمكن للناس إبلاغنا عن أماكن الانتقال الجديدة للعسكريين الأمريكيين عبر علر تلغرام
@sepahnewsiradmin
أو عبر قسم "اتصل بنا" في الموقع الإعلامي
sepahnews.ir
.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85352" target="_blank">📅 13:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85351">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
المكتب الإعلامي لرئيس الوزراء العراقي:
ما ورد في التقرير المنشور بصحيفة نيويورك تايمز بشأن الوساطة العراقية بين الولايات المتحدة وايران عارية عن الصحة ولا تمتّ إلى الواقع بصلة.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85351" target="_blank">📅 13:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85350">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGcyqen9Yx95U1sAVfjPdiFgWWpa4rwv_pWClKRrqgJv-dZp_nFnJSxVXb_jWUq-0Do9iiBfnu3O1gDTbovwibMj65IX6rj3Vzcplm8u9zj_hG-LCnnRlx46oFPVMQXZu5mcUY4Z9MIr6UXBCTmuPpLqH3LNFLIe1Vu4cn9-eFhyllPfdU3PCGZAEQzHi_h2qk6Bt9U6XqFdtSCekI1YWrqaIJ46OsYj2fBo_7zt-3y2s3dPSMHB4LDd7_kAIwQAJCRxnnbhnSn1Cp3jVEkiGohtqeTyUAx3F9PebtpkqacA0vM5IIK_3Y3TFhVQsZ5DEn_9507VCchhajiKjt3PPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي انفجار في محافظة فارس الايرانية</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85350" target="_blank">📅 13:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85349">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوي انفجارات تهز محيط مطار أربيل الدولي ومناطق غرب المدينة</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85349" target="_blank">📅 12:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85348">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقتل 9 اشخاص وجرح 27 كحصيلة اولية في تفجير انتحاري باقليم خيبر الباكستاني</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/85348" target="_blank">📅 12:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
مدير مطار أربيل:
الرحلات الجوية من وإلى المطار مستمرة.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/85346" target="_blank">📅 12:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇷🇴
طيران مسير مجهول التبعية يخترق أجواء رومانيا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85345" target="_blank">📅 12:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
العثور على عدة صواريخ مجهولة سقطت في صحراء ناحية بصية بمحافظة المثنى جنوب العراق.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85343" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">موقع كبلر للبيانات الملاحية: تراجع عدد السفن التي عبرت مضيق باب المندب إلى 12 خلال الـ24 ساعة الماضية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85342" target="_blank">📅 12:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇦
دوي انفجارات في كييف</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85341" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOmYn9la28AM777I0pZWiU_7S60BAFpINt-GcOnrn6yfTHbw7MsIxdw3BjeSb6AzJVubLDt9swH6QFWPQD9Wj7HyvSC9nS2nln6sbaZQqOx61bXjlJartVbAsfzTGf80K60R0PqIBPjFvL_AhSJWyK-B4AnME2AwCgvBpqc6QbR-bLW1O4p8XMKu4m2r8-vbYSL-2vsojeWl92ayAEuBR3HX68dbHoXWRGV6TYSugP1eKZN41TAHtGgsHIfgPmlrDJ2BcvYLtPQOZ8lDqpc7UGpaogkWoao9wgbYvqZNmGcsWcIG7MIiDSUIn1JNAnrzpsjcoPcqquKgStq0g99RQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: واصل جنود الإسلام في الموجة السابعة والعشرين من عملية "النصر 2"، استكمالًا لعملياتهم السابقة ضد مركز البيانات التابع للشركة الأمريكية "أمازون"، والذي يلعب دورًا رئيسيًا في جمع المعلومات للجيش الأمريكي القاتل للأطفال، وتدمير المبنى المتبقي من هذا المركز.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/85340" target="_blank">📅 11:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85339">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca16a78a7.mp4?token=pG4ZFp0NvTVOZ7crWcysvoBQW13jwUMExd58_xJJNpgGSa84sgonLJb_nDqY5KvJ9V9ZF-cTMeVYiWSiyRI_jqQ1K4FVspSzw_SGLw_78ioWDnSITI0SV8ptp_Qz2I_XlyRzGRbTHCJQRdOxiJYGX6XfNG-XIES-DFryvYWhlLSngQrm9BgPGPt4UVG391Ds05BsN6WVPv6Bm0pxi4R2FJXA_1CUp8Nocns-zAkOE6wHM8lT5o92hhXixvnCLLBY8LO_pn9rQKvI-MBhacaXPOfuByrHDWyh6RJtzvJ0RL6gJgGHZe_F1lL5f2Tgb-HibeyKOLXsUVgBjsXZfyLocbvqsGBi_Vsi2OYK_DpSh9cXC5cndAmvD6zWd2PTGAKjJ2qkaYnG4ZgwTS-VTXtB4JcN5NJGCil6Az3Uw-r2rkeJ30Pdmbej2NIdk1ol54YG12ABN1223mX8fFbTNdC73NhJxjoXfYq7xQlNEVns1m4Ps72wnnr0AIwrHPOmBFZM7PvBvOV7alNXz6KWq7gpb1o8noxFMP3LWmdmBcAXXbPcKQ5fT5Hn0EwFXNJNPq7G7T9BoiSP0gZRMPnXk3xRJg3guzbv-8bPCnUoFv-Qhzpubqj-qLFjB3YB-rPob5S8NVOnux-3SJTstilg0gMDnBdLn8NBWb2fQEHiemxwklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca16a78a7.mp4?token=pG4ZFp0NvTVOZ7crWcysvoBQW13jwUMExd58_xJJNpgGSa84sgonLJb_nDqY5KvJ9V9ZF-cTMeVYiWSiyRI_jqQ1K4FVspSzw_SGLw_78ioWDnSITI0SV8ptp_Qz2I_XlyRzGRbTHCJQRdOxiJYGX6XfNG-XIES-DFryvYWhlLSngQrm9BgPGPt4UVG391Ds05BsN6WVPv6Bm0pxi4R2FJXA_1CUp8Nocns-zAkOE6wHM8lT5o92hhXixvnCLLBY8LO_pn9rQKvI-MBhacaXPOfuByrHDWyh6RJtzvJ0RL6gJgGHZe_F1lL5f2Tgb-HibeyKOLXsUVgBjsXZfyLocbvqsGBi_Vsi2OYK_DpSh9cXC5cndAmvD6zWd2PTGAKjJ2qkaYnG4ZgwTS-VTXtB4JcN5NJGCil6Az3Uw-r2rkeJ30Pdmbej2NIdk1ol54YG12ABN1223mX8fFbTNdC73NhJxjoXfYq7xQlNEVns1m4Ps72wnnr0AIwrHPOmBFZM7PvBvOV7alNXz6KWq7gpb1o8noxFMP3LWmdmBcAXXbPcKQ5fT5Hn0EwFXNJNPq7G7T9BoiSP0gZRMPnXk3xRJg3guzbv-8bPCnUoFv-Qhzpubqj-qLFjB3YB-rPob5S8NVOnux-3SJTstilg0gMDnBdLn8NBWb2fQEHiemxwklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
استهدف المقاتلون المسلمون، قبل ساعات، في الموجة 27 من عملية "النصر 2"، تحت شعار "يا صاحب المهدي، أدركني"، مخزن ذخيرة كبير جدًا في القاعدة الأمريكية "علي السالم" باستخدام طائرات مسيرة متطورة وثقيلة، وقاموا بتدميره بالكامل من خلال سلسلة من الانفجارات.
في الوقت نفسه، تعرضت المباني السكنية في هذه القاعدة للهجوم، حيث تم تدمير 6 مباني كبيرة بالكامل، وتسبب الهجوم في أضرار جسيمة لثلاثة مبان أخرى، وقُتل وجُرح عدد كبير من عناصر العدو.
العدو الأمريكي، الذي تكبد مئات القتلى وأعداد أكبر من الجرحى في الحرب الأخيرة التي استمرت 5 أشهر، وتعتبر إجلاء آلاف الجرحى يوميًا عن طريق الطائرات المروحية إلى المستشفى الأمريكي في ألمانيا دليلًا قاطعًا على هذه الخسائر الكبيرة، يدعي، من خلال الكذب على شعبه، أنه لم يخسر أقل من 20 قتيلًا.
إن مسؤولية وسائل الإعلام الأمريكية هي التحقيق في حقيقة هذه الحرب، والخسائر الكبيرة التي تكبدها الجيش الأمريكي، والأضرار الجسيمة، والأرقام الحقيقية للتكاليف التي يتم إخفاؤها عن الناس، وكشف الأرقام الحقيقية وطرق الرقابة التي يمارسها الحكام الكاذبون.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85339" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw-rFqJsEybQkt2ZqVS-Z4J0x0hfU3xDtHsBOpVGAf-7wPLashNHZ4EjBQpFVFiOgjBVXlzjBtOZXqFJyw_lLr_0LIk-mws8XPhVmQJhkmlsErNjqpAmZw9SfhWkqnpA5-gRJCN_A_sxe4YRn91UoeJ7_WhjUQaqX0K84o6JXLxuJ-Glxp-bB9sKU-iNpUn2bSqcXVGDex5HBi2uI76f9sVnBQcuKPUVuKNUN4dDvCg6W7JawnGOzV4ZJxDZ0C7GbROl6B3eW1G2vh5o9bB-yDxQp4UVqHQmKscaJRqVJBzCuv_ZFwC-0mpF1SO-m6PzGo6wBMb6cqXgk6bslbtJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇮🇱
الاعلان عن مقتل الضابط الصهيوني في عملية إطلاق النار.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/85338" target="_blank">📅 11:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85336" target="_blank">📅 11:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85335" target="_blank">📅 11:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5ed4be62.mp4?token=SLVe9NJKmkDSG8a1aZ8cSU1R9pSShOhswnZy8U2DuglMMd3Lk7594HgRYFBGYppRi0rW5iPJ1DUm79fXQogVkqk7MESGJsQIFJCJo1qKW2Na9HPEFAnSCvVYZCyCV4qfuXGckyKuAbg6tXAX4kZ5vdpQPb2-s7yvCJnICWOki6hFPodIyDUmr8C9oMahkdBI_0jKsGvEDIz7v2bUyvrq_KnhBuKldbz4i44zk0p0jksVb-qH60j5_9R5SlAnrM3RPiRl5QEWTUkQOczlW21952pEagwQLO9IkXNiSUWp6yN_vxswknidZowbcDzZtwA-cUxEeqopi7xCPtNyevz4_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5ed4be62.mp4?token=SLVe9NJKmkDSG8a1aZ8cSU1R9pSShOhswnZy8U2DuglMMd3Lk7594HgRYFBGYppRi0rW5iPJ1DUm79fXQogVkqk7MESGJsQIFJCJo1qKW2Na9HPEFAnSCvVYZCyCV4qfuXGckyKuAbg6tXAX4kZ5vdpQPb2-s7yvCJnICWOki6hFPodIyDUmr8C9oMahkdBI_0jKsGvEDIz7v2bUyvrq_KnhBuKldbz4i44zk0p0jksVb-qH60j5_9R5SlAnrM3RPiRl5QEWTUkQOczlW21952pEagwQLO9IkXNiSUWp6yN_vxswknidZowbcDzZtwA-cUxEeqopi7xCPtNyevz4_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط اخر في إحدى مقرات حزب المعارضة الإيراني على طريق سيبيران - أربيل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85334" target="_blank">📅 11:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21767db47.mp4?token=GkpwmAKl_jtGqqujEhwrZSyYtrw7b_Sc-mhrAPVhSgUD_78LpZEi0C_VJRa2rVPmHKlLj2leQjQoeLN-V76d-FazcM7m7UejZaS33fzAOf6fYZeTyrbctAWOBFujOy4wePyXzg0LJcGvHkmAhd5ikzxemA0viPUl3prazRnqhyAFZF926V-Yj3rF6QuqoxdukiQ0QPPhBTKXoTwUXaktSRU-klo9Qz5rgEuofbKeBiWh1CG0MtkNlsCIfVI2kMtq4LWMX_nS3S2HV-C9ZoFJ44CVvpv6PmJtLwLiWQ9LY8hWlsy9aekslqopTMkRo3qk5CcLIN678kCSMPuu4EauCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21767db47.mp4?token=GkpwmAKl_jtGqqujEhwrZSyYtrw7b_Sc-mhrAPVhSgUD_78LpZEi0C_VJRa2rVPmHKlLj2leQjQoeLN-V76d-FazcM7m7UejZaS33fzAOf6fYZeTyrbctAWOBFujOy4wePyXzg0LJcGvHkmAhd5ikzxemA0viPUl3prazRnqhyAFZF926V-Yj3rF6QuqoxdukiQ0QPPhBTKXoTwUXaktSRU-klo9Qz5rgEuofbKeBiWh1CG0MtkNlsCIfVI2kMtq4LWMX_nS3S2HV-C9ZoFJ44CVvpv6PmJtLwLiWQ9LY8hWlsy9aekslqopTMkRo3qk5CcLIN678kCSMPuu4EauCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات في مخازن القنصلية الأمريكية في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85333" target="_blank">📅 11:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مشاهد خاصة لنايا من داخل مطار أربيل الدولي حيث موقع الاستهدافات</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85332" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JirE_xGt2uK-zLFSbhTdo3t4qBPevWH-WKbbr06uKHxULlJHeZfeCA6V37YjPT_TAXbjYGyMGhNL0-oJMgDluzJ561V7dtJbtrGG7kyz8NIL3_9Cm5CfEMpVX8T2oBlgvnf01ujYr2DzpOkSGGttWzmwxNsL8AZy8z8jpIGOKYKtMBBJUzy6TEMDlLx0SQiqGU91maaTcYrgMaHhIvoB6h8SPtDqOZhhmOdlR7ieQQVMNDvBFuBxIMgdKpec0gETwyZHeI59Ribue7kCs3-oLRxGMIGsJn3QedmqYssbqmNuwvgEWq8BwPuWh-Y_uHT1iq0iUwhxGaTOZFU6jMj7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد خاصة لنايا من داخل مطار أربيل الدولي حيث موقع الاستهدافات</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85331" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85330" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فرانس برس: بدت عدة انفجارات يوم الجمعة بالقرب من مطار أربيل، الذي يستضيف قوات التحالف التي تقودها الولايات المتحدة في إقليم كردستان العراقي المتمتعة بالحكم الذاتي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85329" target="_blank">📅 10:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سقوط مباشر على موقع لحزب المعارضة الإيراني في منطقة ناحية رزكاري "توبزاوا" غرب محافظة أربيل ودوي انفجارات عنيفة في المكان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85328" target="_blank">📅 10:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">القنصلية الأمريكية موقع الاستهداف</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85327" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=oSnJW6u1DDTZSWreBj7Kjkd3rJn4WOXerQK-kMYBg4qVgCrwSfD6IqmWohGQ67kcjfjxcq5tMCtyHpnzmwU0zedTCKov9n9E0TAzJ5_rvKyt2DItTg9bWI5CTnzT0Dma7zYhPiApBmzBTb5RQApoDDsXQOqT921gzxB1zjy0CVS4f03OAZxVke9CZPp1RH_Ikm5dRt1AT2N2AVVMUuVW1Z1DfIunHr5C7rdXGpUN1jip23LENkHLKODgxSfwCRg-mYzMFnbbKL4_30IW1Obm3hJ9HPFPAtHWy7taRKO2Gv-zYlNARF0lx8FJa-dWriLlIt2xomYEWV8iUUwJBuSAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=oSnJW6u1DDTZSWreBj7Kjkd3rJn4WOXerQK-kMYBg4qVgCrwSfD6IqmWohGQ67kcjfjxcq5tMCtyHpnzmwU0zedTCKov9n9E0TAzJ5_rvKyt2DItTg9bWI5CTnzT0Dma7zYhPiApBmzBTb5RQApoDDsXQOqT921gzxB1zjy0CVS4f03OAZxVke9CZPp1RH_Ikm5dRt1AT2N2AVVMUuVW1Z1DfIunHr5C7rdXGpUN1jip23LENkHLKODgxSfwCRg-mYzMFnbbKL4_30IW1Obm3hJ9HPFPAtHWy7taRKO2Gv-zYlNARF0lx8FJa-dWriLlIt2xomYEWV8iUUwJBuSAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القنصلية الأمريكية موقع الاستهداف</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85326" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6818cf22b1.mp4?token=EGYst5_Rm5FBEfvFWk2CiKHuZKkZVVAzgxMLa5R7h9t-DxX8cxQkVBlAjp3iHYp5GcMdRLlGwfvfaG-qNNh7Fa7Np1ix1uQUeuN-S_w_6MkitlwXnXlvB6V0vbgp3OsJPZpU8ilA_iNxbyay6tjGraFi4KuqPXcl8bm4J14D_4uR39a9xRa1z4pYQyJ2SEarN0LiaXlnxt49VDblbWfX9EBdMJicxgl-k02BXWtszyy-o9nexW-15dO4a-JxCgDMWVHbI5JMfgdDehqz8gn-fNNYcUcNDNhMFXXwxqaYHwrqrPJx4f74xF7_qdTu06q57ENw-vpBBE1sm2OmLWVhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6818cf22b1.mp4?token=EGYst5_Rm5FBEfvFWk2CiKHuZKkZVVAzgxMLa5R7h9t-DxX8cxQkVBlAjp3iHYp5GcMdRLlGwfvfaG-qNNh7Fa7Np1ix1uQUeuN-S_w_6MkitlwXnXlvB6V0vbgp3OsJPZpU8ilA_iNxbyay6tjGraFi4KuqPXcl8bm4J14D_4uR39a9xRa1z4pYQyJ2SEarN0LiaXlnxt49VDblbWfX9EBdMJicxgl-k02BXWtszyy-o9nexW-15dO4a-JxCgDMWVHbI5JMfgdDehqz8gn-fNNYcUcNDNhMFXXwxqaYHwrqrPJx4f74xF7_qdTu06q57ENw-vpBBE1sm2OmLWVhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الأمريكية تحاول اعتراض المسيرات الإيرانية في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85325" target="_blank">📅 10:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e49d25fd.mp4?token=WNoDuJQdvfBUbYK-wky4_gFN6bVR5PCox3z8btwKQb5FSan4W7xw6FBZIegdvKJ68L1dABhsz_cXh8AJ7KydKkEXBzJkQnqYdRt4Rmi-NtS1Gl_KTC_7atcfncy2YPykllli6w-qjvJeB35-ccwkhtXQbD6MU5M6bzLMASn4QhlttB2jHLr-Br1cf0q1te7s3Vm1b9-zJFOTJJkH3uL8D4jN_VP17U_AOi0ZjJbWPC_U73qVSi5qCKS_DpmO8BFXGwfZQrdqAPu9bZcCn1IoSc2XLD629ZEkIJJ4qedDRX8ZIbBg0MSKMX1Kpc3FHeYoHvBo-GPrLty6sH8puHN1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e49d25fd.mp4?token=WNoDuJQdvfBUbYK-wky4_gFN6bVR5PCox3z8btwKQb5FSan4W7xw6FBZIegdvKJ68L1dABhsz_cXh8AJ7KydKkEXBzJkQnqYdRt4Rmi-NtS1Gl_KTC_7atcfncy2YPykllli6w-qjvJeB35-ccwkhtXQbD6MU5M6bzLMASn4QhlttB2jHLr-Br1cf0q1te7s3Vm1b9-zJFOTJJkH3uL8D4jN_VP17U_AOi0ZjJbWPC_U73qVSi5qCKS_DpmO8BFXGwfZQrdqAPu9bZcCn1IoSc2XLD629ZEkIJJ4qedDRX8ZIbBg0MSKMX1Kpc3FHeYoHvBo-GPrLty6sH8puHN1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط مباشر على موقع لحزب المعارضة الإيراني في منطقة ناحية رزكاري "توبزاوا" غرب محافظة أربيل ودوي انفجارات عنيفة في المكان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85324" target="_blank">📅 10:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سماء مدينة أربيل تكتظ بالمسيرات الإيرانية التي اتخذت من مقرات حزب المعارضة الإيرانية أهدافاً لها.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85323" target="_blank">📅 10:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7763e1bcd2.mp4?token=odRKM8wUMp_N3riZsOcQiGaTOWMo6xIbQvHZdu263nqisLf1uY3i47r9wR9DWGa_c_KYrD1e7kIoPg-SNozqKoidgGU5o3lQxS-4TWXF3amECIG4cRe8BoZnjuvcbk_1iMJIs_PQ9L_faW7XfY4RYN188tAcMJK8KXdhwiH6aju2hhjj5Vdq_oiJTg8lI9XUpGbr-AocwJz-rAZgRRMsp3R1-q5aQLvbr0B6ZODGFY4TgTZFcY-z15rq16ypdAq03O_pDeAYId5Ap98s34VS9A0qVhmlOY4fFq9lTu5ppgVN-D1wsuUdPEr1PTyiY9ZlHodF-QzXRIM15dyuT1GFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7763e1bcd2.mp4?token=odRKM8wUMp_N3riZsOcQiGaTOWMo6xIbQvHZdu263nqisLf1uY3i47r9wR9DWGa_c_KYrD1e7kIoPg-SNozqKoidgGU5o3lQxS-4TWXF3amECIG4cRe8BoZnjuvcbk_1iMJIs_PQ9L_faW7XfY4RYN188tAcMJK8KXdhwiH6aju2hhjj5Vdq_oiJTg8lI9XUpGbr-AocwJz-rAZgRRMsp3R1-q5aQLvbr0B6ZODGFY4TgTZFcY-z15rq16ypdAq03O_pDeAYId5Ap98s34VS9A0qVhmlOY4fFq9lTu5ppgVN-D1wsuUdPEr1PTyiY9ZlHodF-QzXRIM15dyuT1GFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة انقضاض الطائرة المسيرة على هدفها في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85322" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a91a7bc7d.mp4?token=ThdUJhKd1lg-S_0tdhY8JdE8qaXLVXToFCqBWrfLOStNjAXuaShAFZGCo2QSJVc0oxw_XJY1UYQ2rN8rAWAbtJSA4sMbPlYpfAyseKf4jw6rk1g7TbSW8eglsrSJ5QiiZHKbH2PvyPR4WksWbGUIwqImxZDmEXdEeblWey3SldBlBYX9XdyBA-35n1Ew6M8VrJvbcBnhcIs63y_G4uiNCTdGhZuuhC8kdcfkgjh3Q_uUC1tuKfj5FG0UwMfKsECY-IbiQ6kPiJbF2ZFiC3xNnIGWBMmcj5VtVdkqaIJJe3IZpLnCfQG3oxMHcTuXauhue_oQHRbm7eyQOHT4nNO9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a91a7bc7d.mp4?token=ThdUJhKd1lg-S_0tdhY8JdE8qaXLVXToFCqBWrfLOStNjAXuaShAFZGCo2QSJVc0oxw_XJY1UYQ2rN8rAWAbtJSA4sMbPlYpfAyseKf4jw6rk1g7TbSW8eglsrSJ5QiiZHKbH2PvyPR4WksWbGUIwqImxZDmEXdEeblWey3SldBlBYX9XdyBA-35n1Ew6M8VrJvbcBnhcIs63y_G4uiNCTdGhZuuhC8kdcfkgjh3Q_uUC1tuKfj5FG0UwMfKsECY-IbiQ6kPiJbF2ZFiC3xNnIGWBMmcj5VtVdkqaIJJe3IZpLnCfQG3oxMHcTuXauhue_oQHRbm7eyQOHT4nNO9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موقع الانفجارات داخل مقر حزب المعارضة الإيراني</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85321" target="_blank">📅 10:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8443be5d06.mp4?token=BHGlWd2zwNEXMQ4DdwsfmQTl_k-cUlppaCcxTUro9s6XZPegApb9WtB0tEZqMDKPgnDZiLKE-F5B2QH1kqaR1KdtZD5yEIsd4lGERI03k8mCASFNmrmTbK-cO0QzLTolZSg91RDC_2o1zKjjnN0i_nidnGVjEk-lhegTl_E_M8llm2LNmAoZFnfht7EqSe_UZ0pczLDi_zozhErGpJE31Ei1zQEEjkzI1CoU5RMNzB8bdCdisdj0HSNo3nhukbUQ39gH3cYg_DElCTaADrRS12eCCxMTsaX_k2KX-hzqpx2BG0OcEB7z4S3InltfcJqnz0SLRwXp6IU_WN3r5mcVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8443be5d06.mp4?token=BHGlWd2zwNEXMQ4DdwsfmQTl_k-cUlppaCcxTUro9s6XZPegApb9WtB0tEZqMDKPgnDZiLKE-F5B2QH1kqaR1KdtZD5yEIsd4lGERI03k8mCASFNmrmTbK-cO0QzLTolZSg91RDC_2o1zKjjnN0i_nidnGVjEk-lhegTl_E_M8llm2LNmAoZFnfht7EqSe_UZ0pczLDi_zozhErGpJE31Ei1zQEEjkzI1CoU5RMNzB8bdCdisdj0HSNo3nhukbUQ39gH3cYg_DElCTaADrRS12eCCxMTsaX_k2KX-hzqpx2BG0OcEB7z4S3InltfcJqnz0SLRwXp6IU_WN3r5mcVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من موقع سقوط المسيرات الإيرانية قرب مطار أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85320" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae715a6f35.mp4?token=nMWYrK6ntoK_Hp3P6FnssNwcQ1l9tI9BeGP4G_I4qLJ1E75cuKpbtpyO97h8U2-aOIPKBL2isViPK1Vcd6DZC1A0g4cdWI5jFs8HVNjqYNpuL15u7TXwdfepXFDAPQSQQhsWAU-RDXmWfe6dcfaUPllBZzXbjTbqbltX838PtTKhfN2TfX7qNsjJ2JMzUBNNi8E9lU-fiQL_UOYwNfNnl7Fz2I4QrTdUs4QqGLYKidNOOx5ELB3N97vxgcTFq418beR9tBYjyU7P7wJJ4pmz_PfvJg0VzKmTSQc8StNH1SBhAsvL6Qlxrg8-d9jgCgFDAlkGIFNy4B-dLR6REraStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae715a6f35.mp4?token=nMWYrK6ntoK_Hp3P6FnssNwcQ1l9tI9BeGP4G_I4qLJ1E75cuKpbtpyO97h8U2-aOIPKBL2isViPK1Vcd6DZC1A0g4cdWI5jFs8HVNjqYNpuL15u7TXwdfepXFDAPQSQQhsWAU-RDXmWfe6dcfaUPllBZzXbjTbqbltX838PtTKhfN2TfX7qNsjJ2JMzUBNNi8E9lU-fiQL_UOYwNfNnl7Fz2I4QrTdUs4QqGLYKidNOOx5ELB3N97vxgcTFq418beR9tBYjyU7P7wJJ4pmz_PfvJg0VzKmTSQc8StNH1SBhAsvL6Qlxrg8-d9jgCgFDAlkGIFNy4B-dLR6REraStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لحظة السقوط</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85319" target="_blank">📅 10:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85318">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2fdd71e2.mp4?token=QOBWiWTYtcNgvxwEgapkqHbeLUxGdM7WgJiCJPy6b5yAaOJ9syZDLAVqoRP936SEcFEM3kEtqzzY4WahkqoligtRTYPj8dvCn7v213NMJWCyJzPitwJy2riaeLKYhWzaH6D85jWLE1qlN6wJOGiN_ETF_-Ygd8diYhmSuoNG-wGH8MnFu442tW4yx3peuQJDkO4aBHhrPl7uj6pJRG_OoZIODTq6rNgD0pWKpcDd7nEclqrSIGRuZZMHOOIL_tPfjv1GOf-eR4U0ZGfnmTdWqcn6SFpHN6knTuWcR_i8HdKR5OrlT7XGjMnRzfyKiaqrMSRoOJ4gLclqc3jbExc-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2fdd71e2.mp4?token=QOBWiWTYtcNgvxwEgapkqHbeLUxGdM7WgJiCJPy6b5yAaOJ9syZDLAVqoRP936SEcFEM3kEtqzzY4WahkqoligtRTYPj8dvCn7v213NMJWCyJzPitwJy2riaeLKYhWzaH6D85jWLE1qlN6wJOGiN_ETF_-Ygd8diYhmSuoNG-wGH8MnFu442tW4yx3peuQJDkO4aBHhrPl7uj6pJRG_OoZIODTq6rNgD0pWKpcDd7nEclqrSIGRuZZMHOOIL_tPfjv1GOf-eR4U0ZGfnmTdWqcn6SFpHN6knTuWcR_i8HdKR5OrlT7XGjMnRzfyKiaqrMSRoOJ4gLclqc3jbExc-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار المحاولات الفاشلة للتصدي للطيران المسير</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85318" target="_blank">📅 10:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85317">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dfa85ff76.mp4?token=tREviDV0oa9U2N1rR1eLjnqNK9MwKkit2nM4JW2bvoWDevNnWdIrodHyKrisclKNxnR8ItILofjL3FWsRU2aYZoYSCZbEF7fB5H-hzkbuhOA3o4tUipDyNHPbCiX0UPUYenCYtbqJo0KZGKc-OaupV5FpPfl7tT-wpjkhILQJJOT7a62dcVgnvJmopLEBLQIAmQ7bGnfqFqnMutm7hp8ekxy4D8HrWc0CmvmYWo2wIXxrNqmTt2YNEUhE-KbbVhPCivP911Q1T1hLHjiLIBe6r7aVA_CqqoLl9uyJrqmr70V-kHHgmlrlIES1xJUnHG43lo2u9jHlCTz8wJLY3Mu4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dfa85ff76.mp4?token=tREviDV0oa9U2N1rR1eLjnqNK9MwKkit2nM4JW2bvoWDevNnWdIrodHyKrisclKNxnR8ItILofjL3FWsRU2aYZoYSCZbEF7fB5H-hzkbuhOA3o4tUipDyNHPbCiX0UPUYenCYtbqJo0KZGKc-OaupV5FpPfl7tT-wpjkhILQJJOT7a62dcVgnvJmopLEBLQIAmQ7bGnfqFqnMutm7hp8ekxy4D8HrWc0CmvmYWo2wIXxrNqmTt2YNEUhE-KbbVhPCivP911Q1T1hLHjiLIBe6r7aVA_CqqoLl9uyJrqmr70V-kHHgmlrlIES1xJUnHG43lo2u9jHlCTz8wJLY3Mu4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة سقوط الطائرة المسيرة في أحد مقرات حزب المعارضة الإيراني الإرهابي</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85317" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85316">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e2077859.mp4?token=SkoMH_q2aPf8zRTFBtXoX0R5xGdk4Ow2qesnpv_Z4i5fJ95w068RhEaAUAMgM8fEkhPIsBU8QS7jMxHNhzmmMsH8kRsWEFFGyPyTDOU77r66ATW7IUuUYqYotztfI_E0WwTK20z6P3Js2iGs20TPVGldzHCkeqUlCXf0O_dlgrrR8WuaulQis_U6kO-nUkyFwk82wmvZyzK_K6lSmiDlLjvsUl6qgVXwfqyRSP6c_Vmh2_10B1OcS4MUaM19dEvYJyFlXX6rrDKOtpA9V6pgtUqYpdxixjlKgRHbBiqnfBTh6fwxf8zP5-5mZSgWNp7p0SK5SV5Gbuq0juyGmx9zHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e2077859.mp4?token=SkoMH_q2aPf8zRTFBtXoX0R5xGdk4Ow2qesnpv_Z4i5fJ95w068RhEaAUAMgM8fEkhPIsBU8QS7jMxHNhzmmMsH8kRsWEFFGyPyTDOU77r66ATW7IUuUYqYotztfI_E0WwTK20z6P3Js2iGs20TPVGldzHCkeqUlCXf0O_dlgrrR8WuaulQis_U6kO-nUkyFwk82wmvZyzK_K6lSmiDlLjvsUl6qgVXwfqyRSP6c_Vmh2_10B1OcS4MUaM19dEvYJyFlXX6rrDKOtpA9V6pgtUqYpdxixjlKgRHbBiqnfBTh6fwxf8zP5-5mZSgWNp7p0SK5SV5Gbuq0juyGmx9zHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لإسقاط المسيرات الإيرانية قبل وصولها نحو أهدافها في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85316" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85315">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2984d00b0.mp4?token=bZ202GO5GiuWDbv4Oy1JifbKc_aso910Lkxz6Psd44odJPN4YeYzmqQYZSI3qlwmgXyT8mYUpE8QkFFf4ReF5bbEdUcDjNfxYxM7Nh6k3SOQBKk8CLwB838oyMUlMlK6GuUnMMna2AirdnlPQAvSmGfR9tF2vev3ZP-9tQdXdRbLL_dffEzrOjQVYeXnTXJDMxOmvvTETXpYdr4sWmoLt8FitRE9G35CiCKO1SxQ5FCNqpxozSCZ47r-momLVk9BuLhthUB2LrwGtcODeoImt-emnh40RVzAl1ztzUfKqWLvmcJ5UGcQMtt9zFaDUq5Y_-WhBpGTaYShzPf3bONFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2984d00b0.mp4?token=bZ202GO5GiuWDbv4Oy1JifbKc_aso910Lkxz6Psd44odJPN4YeYzmqQYZSI3qlwmgXyT8mYUpE8QkFFf4ReF5bbEdUcDjNfxYxM7Nh6k3SOQBKk8CLwB838oyMUlMlK6GuUnMMna2AirdnlPQAvSmGfR9tF2vev3ZP-9tQdXdRbLL_dffEzrOjQVYeXnTXJDMxOmvvTETXpYdr4sWmoLt8FitRE9G35CiCKO1SxQ5FCNqpxozSCZ47r-momLVk9BuLhthUB2LrwGtcODeoImt-emnh40RVzAl1ztzUfKqWLvmcJ5UGcQMtt9zFaDUq5Y_-WhBpGTaYShzPf3bONFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرب من الطيران المسير يتجه نحو مقرات حزب المعارضة الإيراني الإرهابي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85315" target="_blank">📅 10:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85314">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087ee61fb.mp4?token=BDMT1uYXw1hATsJYljomK7DGItl8YTp3guhEXvkPZ-ZuK7SX4fH8Bc1hcQThog5mDEXDdRZEPLADLnRg-a8HWpBGbiVMaHwOwZEqBj0f8Z76Pz3VK0LZXLPzRueFJg7OcMe0WbnPFTWHqxq25sqCGsDq1zEj2JQQdgCpV0j3KZmjMbstge9GF5ejz6RD80_Vsh4qTf3VGEA4AL6ucIYZEsUTwxIkO4jKeg57Z6Gy2FIpFB-yAkib5YI5tHhiUnTyVo_-dwmF0R7x0N0nsggBYhUe2lfn4fHfjhx9M1jQQoH78Bt_mtJwAwbrwQqLb5dbHldlZxCtjPvpRDDAVJp8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087ee61fb.mp4?token=BDMT1uYXw1hATsJYljomK7DGItl8YTp3guhEXvkPZ-ZuK7SX4fH8Bc1hcQThog5mDEXDdRZEPLADLnRg-a8HWpBGbiVMaHwOwZEqBj0f8Z76Pz3VK0LZXLPzRueFJg7OcMe0WbnPFTWHqxq25sqCGsDq1zEj2JQQdgCpV0j3KZmjMbstge9GF5ejz6RD80_Vsh4qTf3VGEA4AL6ucIYZEsUTwxIkO4jKeg57Z6Gy2FIpFB-yAkib5YI5tHhiUnTyVo_-dwmF0R7x0N0nsggBYhUe2lfn4fHfjhx9M1jQQoH78Bt_mtJwAwbrwQqLb5dbHldlZxCtjPvpRDDAVJp8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان قرب مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85314" target="_blank">📅 10:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85313">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866d7491f9.mp4?token=nwLG7kUc1aR39mkJqbEOCUggPf9zFx1Fpok6i_-NyV3-gR5p6DqjBsv3zWoqVC-shINUSWVhtuVVePNQA5zAZZwtjU_TgSJtRGzHlsUojiukWq2IKNGVMiYNkACR_tBsfI9N0aIQmoxzM6meK_Dcx29J0E-QhqlNrdAusJhCWPOAgyvzrrStRLS57q20wDMYUX87hOWi0nYSfJS_tP5oeVqyuPOs_lIv13pVILWMq6L2GZ7MY3IyatlD0Uy5TqkTS78sU-cXBdO96sBG_K-rnSIoAghl_vBJZ-r19yiz-mkgX7ca32AsYbTjuxBncsbYXnbXPdD4Ef5lU2zCH0FpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866d7491f9.mp4?token=nwLG7kUc1aR39mkJqbEOCUggPf9zFx1Fpok6i_-NyV3-gR5p6DqjBsv3zWoqVC-shINUSWVhtuVVePNQA5zAZZwtjU_TgSJtRGzHlsUojiukWq2IKNGVMiYNkACR_tBsfI9N0aIQmoxzM6meK_Dcx29J0E-QhqlNrdAusJhCWPOAgyvzrrStRLS57q20wDMYUX87hOWi0nYSfJS_tP5oeVqyuPOs_lIv13pVILWMq6L2GZ7MY3IyatlD0Uy5TqkTS78sU-cXBdO96sBG_K-rnSIoAghl_vBJZ-r19yiz-mkgX7ca32AsYbTjuxBncsbYXnbXPdD4Ef5lU2zCH0FpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجارات قرب مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85313" target="_blank">📅 10:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85312">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات تهز محافظة أربيل مجدداً</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85312" target="_blank">📅 10:11 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
