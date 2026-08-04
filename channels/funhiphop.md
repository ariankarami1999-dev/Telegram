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
<img src="https://cdn4.telesco.pe/file/mxW25Y1ywUnuUX-nnTxn2KvNbbjS2Kd3JVzOQcrD2Aa1TF2knDl44Dsiiz_zmtXuWxJy3OBg8APUflVwGgIQSB5Yq0mwOnnH6bEjF7VPX_JOmHYDIIVqze_9wmVIf2-P3mT9qQoEjrZBzhQ9jMimmGACEBKTXIyBuTk7Y2Zij4lQkdue6J2gN9YEPHudo5LIwSuYNKVWAwM7ruE9jk2TwL9YCCt_nHeqA4WjXV_5ouJzn88slvPFn-CYlzoF2-JUsm2Lidbmdyn0IKxL7kO9w9YH4OFteVRNci7pdSYGYLosnwYKmBBIaspeoNyrm_cFP-A_e98LrN_ZgmuepScGeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 01:15:18</div>
<hr>

<div class="tg-post" id="msg-81802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwUH2wT-vqxeR3qCk2tARqcj0BZk1t9no9zpMC8tZJ_m8PGxhL0kkhNv2tMAM5FEBsAW2H-vrcyynOSXLyK62cltMpo1OT_1y_DnkcU9PJO-uRiBfOEDVz8397Gy9OMVYIt0sls272UzUWj-We9HLLwX0vxsJ09HFrzcRNwtsD6CcJ8rlgFuwCwFGskaeY-YSe6xl-TPoMxNT7Ks1mAoD5atVGq1mUMGJ-Dgkzfhl29fqkuDZlLaJ58H_UEZOhbBdyHciCRSQu982rEEwDtuXwdWLqFt-o11W-GF2TsvN-TAJU5o0LamZE76kNGiPzavf6lk4a9d9yzdsh8oXN_RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد هم اومد پیشم خوش اومدی سلطان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/funhiphop/81802" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from꓄ᥲһᥲ</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/81801" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from`</strong></div>
<div class="tg-text">این ناموس کونیا دریای خزر رو دارن میفروشن به روسیه</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/81800" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuaf0_jgmaK_yGp8uF5pF2itV0ITFA-sE3QmABnwgKR41h7nkzT_HJkkYy5m4v2_8tMKPMYejOpBUSUXmY1B56zDsjQzCoglBIETRF17eP7Ce-mxTKLpTVqo2mxHDXEXClYUw3fJcHLvLQvgd9yFDK8KTbB3tg76SEW5Ju-RnYfRsXLCqTYFsw5cNdZNdpTUHWDMSiyifvhv2DUh9afem32lr3XaccBfC3O64RRrBzlctQNn019zH-tuu3X5RSRBkZxm6CF7TvYkF-SmCRpIvTJKFd2-WGidWvXaMOGL0jg4ZDo3DprAGfz1W5osYtVONCrDrcXTl-OD-Tr1sq7t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میتونم زن مدیریتو راضی نگه دارم، میشه استخدام بشم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/81799" target="_blank">📅 23:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه چنل میزارم جوین شید هر خبر جدیدی میاد میزاره و تحلیل میکنه براتون که چه اتفاقی قراره بیفته و چیکار باید بکنید: https://t.me/+UEUtK77ntq5iN2Q0  جوین شید صدرصد از تحلیلای ادمینای اینجا بهتره</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/81798" target="_blank">📅 23:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81797">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سلام</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/81797" target="_blank">📅 23:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/81796" target="_blank">📅 23:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW6TOzXV8yWaefbAAuvv5nas0h5RIEmpWeCtHjN1iQy6JHfvKBlGG_hXN3ErGJbvsDNnQmSJIysZwTXFYj9Fk0w8vCbs4PCsih3RRWgHkmJX-ct7-IkaB-IHxUxpS7FmcBtt4C3zbIIVClej9md2_1sWzPqsHPX7xEO5fnJAiABuFl5twndAr5VO3Crw-4lcyR62ipbbOWxaaHssHRgnE--yQowOIwvl21whjhl040fYD0DwQ50_NDLjFiBkoZb2F_QEobjTGgT4cr6rQB5ivtAgPrMzw3RbL4B2tVwbmRyeAOHtzZuspSFK1LoCcHxSyaxmSgO6gsRDZntQkOd3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال پیش تو همچنین روزی، خیلیامون واسه اولین بار تو زندگیمون حس واقعی شکست عشقی رو تجربه کردیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/81795" target="_blank">📅 23:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNRoEAPKn0A8iqjwOnOP9Lp8sI1qVV1COw3sL47lFEJVqhuZTQ5KAcAxmXl73JBiZetIJLVIyve3Cra-zsrd2eSpFWUOuPAAV3MIQjmA0e1pVR34P5Sfh-HDmO53zqwH6vIsxTroYhZ89JWfialH8iDklmvNXEVpSs5KoL154Itj2IXvzcXHy9HrWDxdQajrAthgg1eSiahnd1XPIo_29UdIFrCcQ2DwrFqbl1vYqaZSB_Mc8A3xKDz1Q0Jpzk04mZYit7kNjxDG2_VIr2LW9hH7gSw4D2p9qGjGre3v0k4QAMoJ5kjQ9QIpZ6qBfRBXRRDxASo102-4SkUFV1k8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیک
جیلنهال و پارتنرش از هم دیگه جدا شدن
💔
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81794" target="_blank">📅 22:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyBa-xE7clnojLrv4rugjsMWCzkdFpQzDWLG3xRwEpI1vPqXQBUle9co4Y_WN4eQHLU1ttIPLUND2Pw7BTqvcPN7_tJD0W7kjCHlYrODvVpNiKPKeF_LbMOVIgmjP2eBrqpHrI0i6daQvYkKj-8bGfV2tEzEbXSJlNVqxGnKgZ168iVkC_NCTJ70IhvCiZJPsUd8ALDzGE2DObdzdPmm_RVOD9nOhicT-X7bjS5pGDFfx58disczmEwwRSVUXKXPf_69cqmCpKbb-fuN2G4lpAXRnx9p2TpOTHHozhQMQUDTwQATBNbmMxvIktBhmGjCkK8HO47eaolm9NTaH9mO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپر اپلیکیشن بله وارد اپ استور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81793" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMVr8x-n_vrnELsRJPZ-vv432Sqz3_oWgGrMIbGYTCbNmx3gMynH5FiwGAm8IgoRvd2o3oUrAqRbSVYN31gYTEN3lugciJrV_bypVWaexWFlRJKb9y8W9llppWunyIp7PZjdsPMWDtR-hEvIg4dHS0a89CKlyLJa9ygv82zjFmnrqdhippkQkV_I1cxRtY_CnRjmLM4No7eWgVTvnoqP3j2tGEKLCFVvfi7-2kC3LSIcNHA93WrFUighvT7b5ErrUkK3Gq2EpEUk_zJJTEucKQdlHE3E1eg3XCjNQU8U4HqfTC7hw06X-EfjnDMwyrJ3zn3V-vu0jiyU1D2VMaN9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/81792" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارژنگ امیرفضلی:
بالابرید پایین بیاید، جنگ کنید یا نکنید، موشک بزنید یا نزنید، توافق بکنید یا نکنید؛
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81791" target="_blank">📅 21:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=B5Wi5G3z8k1LDydjLdCxRu6RF1a4XY02hzEEcUO5YASPGvIgN5XAe647o83BwWynl1OyHJ1omCPG44DQYqv3Of1cyHlJBRCGOC_zp3mHl-MA0U6I7bGe-tT0kB_X1eQ_ZvglX2OHe54O9n7hmx22NM75hL4hkYINr5CW3OPN6tnSYHOctveglUvcV8fn0eXlR_lpmcM5FZucOL8FvIVDUVr06kYrQrDI_0dOssxGLrIjOG0HNDgZ9pQM8ZXGiPw5mAdHpEYjEC0K1HUj1u4CXCqu9Rkpl0IQRhSNEQwxVuxFOP7CYokPsZ5nE6QlQGMk-fapAcDApGCL2d_-_Ov-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06551d5d7.mp4?token=B5Wi5G3z8k1LDydjLdCxRu6RF1a4XY02hzEEcUO5YASPGvIgN5XAe647o83BwWynl1OyHJ1omCPG44DQYqv3Of1cyHlJBRCGOC_zp3mHl-MA0U6I7bGe-tT0kB_X1eQ_ZvglX2OHe54O9n7hmx22NM75hL4hkYINr5CW3OPN6tnSYHOctveglUvcV8fn0eXlR_lpmcM5FZucOL8FvIVDUVr06kYrQrDI_0dOssxGLrIjOG0HNDgZ9pQM8ZXGiPw5mAdHpEYjEC0K1HUj1u4CXCqu9Rkpl0IQRhSNEQwxVuxFOP7CYokPsZ5nE6QlQGMk-fapAcDApGCL2d_-_Ov-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی: رضا پهلوی مقصره که به مردم گفت برن خیابون کشتار دی ماه کار جاسوسای موساد بوده، کسایی که کشته شدن بخاطر بالا پایین شدن هورموناشون رفته بودن خیابون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81790" target="_blank">📅 20:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره. به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81789" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">طبق کصشرایی که گفتن، از این به بعد کشتی ها و نفتکش ها از آب های تحت حاکمیت ایران از تنگه برای ورود به خلیج فارس رد میشن و برای خروج از طرف عمان رد میشن، و در ازاش آمریکا محاصره دریایی رو به طور کامل بر میداره.
به هیچ کشوری حق گرفتن عوارض از تنگه هرمز داده نمیشه و ایران و عمان باید تنگه رو به عنوان یک آبراه بین المللی بپذیرن و بعد از توافق کامل و پایان شرایط جنگی/عملیاتی بین دو کشور، ایران دیگه حق نظارت بر کشتی هایی که مقصدشون بنادر ایران نیست نداره‌، ولی تا رسیدن به توافق نهایی ایران حق نظارت رو داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81788" target="_blank">📅 20:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEYJf0Mi3uKbPWodAioAtyVkX64_giKfomcM1XkuwOE3pwgxnU1t5Ze7PjqrtZCiF3M944BjHwRVk5omRNde9_zNV90Pm379EGvpL5gBd8yk_0bnTzi_tov1ivq0uJxwSzvGIkyGUUlHgdjrbKa5cnOCYiNYllmTIDGa1pp6dv1QvBZl8RRUEFzssThVs6hqg4xT4yDXI-d_0OR1oAu2YcoNyM76OwWNEoe4xWZmcSctfw1F51zcc2V7aYMnhhM4ohigOOfSXb8AmGKWg9faE_vZOBjLu1KLTpPljFqrOsQahzM9AN1c6jjKklOkmydkFc_wUDATEjI3UWiLZMMjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNY4yTRH0RX3yFqPCa0kbXA_db-x4wCOeka_BjTlA9XjkvJSeMbxyP5ycBKMg8TfYOKHUAHbrtVF9NpR181Eg46_juXAhpxPuCd98sUn-71s3BMAUN6Xp9b0_HQ88kUgTnh6cdiaFLKlcUZJKlPO223oGe_QwHisUxuldlsOaReIy5-2JJtxePQ5n5vXoDWF4VLx53BFqeVC_-_1_reCaj2aqJkvIWpB80BC3_pGgrkK71v4azLdGZdX5G9DPSWK3fcU557VVSRLlPtNLwTCmn8oxv1_MOCSWZO2WwT53zGdiKLWb0PWZBVUSZadI-opiCbIdnNI3TWP97yoXN7DLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81786" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ریدم حاجی اینجا رو زدن فک کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81785" target="_blank">📅 19:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تقریبا همه خبرگذاری های رسمی پالس های مثبت از مذاکرات ایران و  آمریکا میدن، فقط مونده فارس و تسنیم تکذیب کنن تا دیگه مطمئن شیم که توافق قطعی شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81784" target="_blank">📅 18:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnk3gEpA7r5lGf83lqamDo5lwQZ0tgLWOv_b2qk4yulcOH0WqMpaeZMYM5m1lqxKAzQjfxlgJ1eHPfv3j4HlCm7JkPlbD4cviBJRIO8PRz2ydmLbykqZmYqJUPB1n19Kb3_jjAmDvNQJ8x-ubbyBQ4g_M2hJeViqdIvo7koSjvuvVXKs8vEpityXjPB9KNnsvR_7BNyF7Hmda4lpy89-qDapmlsMqjvElLV1zdo2oluirFCvLF-OKjQ0oVqAream8s6KUBn0tc7D0oOF7yzDHXRpsM33hZFhgHPW6AgfvgbDYmA-ch1CTPWwb1sADVhdjRyNOwxP9aVP_izheM5-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون، مخصوصا اونایی که لباس اسپایدرمن میکنن تن خودشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81780" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امروز تولد جاویدنام مسعود ذات پروره؛ اگه زنده بود امروز 40 ساله میشد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81779" target="_blank">📅 17:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEkUdt7_MDc00cl_THb_Bzktlg4hOLMA2XRtsykOS4aOqru7pPb7-FpVSOmXvkzZVFTHTOdCfXFPtYp9yafpPVDunTrTFdCILVadNezx8n4lOdn6Vug_R5bNgpBvnnMTgakNpcEF6jtPR-hT544ExSomwHQQISMr491P4072HzLK7Z906-sKRIreibyt1CU1yWg3oVoAqJGYomb_2aiO6WDWHpTNLoEEuec_QsZ91SiO4UM0r0YBCbSnxSKv_y8hT-cmo74QJXTm-9f82FblYPl2rfg5p8x35qWIEInhC66sJHzQu1QwASpuVeo6KU18zGEw9ta44JhFVe_gnMHCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشیدنی مخصوص طرفدارای ریری که پسرن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81778" target="_blank">📅 17:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=sdO7zdH2omCNeWfF-AwmlbDpjYUwqzDos4kwraFZ7atYvAOCrhkjM8Z0S4GyP69k7odTCF8FU0ggADpM_a0mMxwhiJOuVDHoMwpFeC5f52XlFnH89Vix4JTFWl1DLlN4d58BtpXxNf4OUP6rwIs9VwdEAl33NbIwww0_VVXGeMIL2rkt0iV7yjMNnzCW13VOy1QraLCHGVoVH9OVJ1AWXPnuR6BujcmJWsBiFFmELi9gPL6LHny3J0p3-LkmMEpbOGrYCsH8-bCdelI46Xmhy_fdgyDgpIZwDkGqmOxpAVsd42KNuOK-g9dJedDjPpmsZOXGFjVLOuCFaDY1pJtwKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3ab90449.mp4?token=sdO7zdH2omCNeWfF-AwmlbDpjYUwqzDos4kwraFZ7atYvAOCrhkjM8Z0S4GyP69k7odTCF8FU0ggADpM_a0mMxwhiJOuVDHoMwpFeC5f52XlFnH89Vix4JTFWl1DLlN4d58BtpXxNf4OUP6rwIs9VwdEAl33NbIwww0_VVXGeMIL2rkt0iV7yjMNnzCW13VOy1QraLCHGVoVH9OVJ1AWXPnuR6BujcmJWsBiFFmELi9gPL6LHny3J0p3-LkmMEpbOGrYCsH8-bCdelI46Xmhy_fdgyDgpIZwDkGqmOxpAVsd42KNuOK-g9dJedDjPpmsZOXGFjVLOuCFaDY1pJtwKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیدونم چی میگن ولی اییییییی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81777" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlb1zpFwgv5_Z7Ue1uGF2sdPFu6ISkbczvltT-6gScQpBUqhJKWJMARbM55UR5dEjJTdTgUBPvehEe-dqrTcmrtVgCzcycm2Up8FWMd6etI61s64nL2VNew-Cp1UAh9LdFFi5vdKxcDlnClfmEW9ID2BHtnuWOyOhRNkabdmaohwzNIOs_kphE56VKZ5YsmY6qFzlaowvStN1D33wWl-EcoxKqSGU7ODFE-Ez7Y9_u-4avS5CcD0lV1G6iM99725abFlZxmY6M4eNR7YDbzRe9m-zg2enI4LejoqaE2mdXbjju9dk3jc4vJKhMXTw2aYjdwpLLkXlr6SoqqO4we7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بازگشت نقدی بت فوروارد تا ۱۰ درصد
🎲
🔥
با حداقل ۳ میلیون ریال شارژ حساب کاربری و سپس ثبت حداقل ۳ میلیون ریال پیش‌بینی ناموفق در میزهای کازینوی زنده، ماشین‌های اسلات و یا انفجار در طول هفته، بت‌فوروارد در هر هفته تا سقف ۱۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را به عنوان بونوس نقدی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/WEEK
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81776" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvL5FH5rLGuul8AXyxz3g0jr2lYSSJaxrcww9qZViOhchq5KQJE_kKI0iRcAIbOhuARF4Gt2OcdsoByySNpSoOI9aEKMFbv5U6VyHqeoOAZYNIhJsElZ1bmonhSO8TLBCsaE2YK3ph8j9b9j0e3o7CxGz1eVlx6JOzlFNL6qIoIKQCHD9pMNLK8Zp9wSlTk8f7cuFNh-qUN3R4T-Qoi3ulNj5MljLL3fHrJcuvdRt4gSrgJGw97gZZM1LXFZYQf-X8JWMjul57sWxXeg-v9sJobc0oRsBn65pvXQWocxgfLgAbVgHXuotFdXXlhZQwECy5_aPdGnenPWwpSNURYALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۶  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81774" target="_blank">📅 15:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">باز تتلو از تو زندان داره ترک میده، واقعا دوست دارم ری اکشن اونایی که تو صفن تا با خانواده شون صحبت کنن رو ببینم موقع آهنگ خوندن تتلو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81773" target="_blank">📅 14:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اسلامشهر صدای انفجار
اصفهان هم چن دیقه پیش صدا انفجار اومدم یادم رفت بزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81772" target="_blank">📅 14:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81770">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoaQdLyIrHk-BILDTXVF9SWXewo1lYbqSvIp4xTehVswoxXiBxXSxSBTqpPQnNs2elbV7Z5ezgx7UpOgGcS6YpkMns_mohd5qJcmJasTQJitUCsc09oEm10AqzaV8lKMskmWI6nsmlWfLPrJ1VCobX3NgX38kjvj3GWtd1lPruTh7MV2HPfKTCZJ3IqXxmQyvdPhOm70iHSkBxzV_B60a-qKGv1X07PyhnZjqS0o894fy2heIdjLkepMTrBGZy33VCzKcYV5dG6xEzjBEVqqhlRxG_W1So_2vdQYeKSxn024S5Hs403zFZ-u7xRUHUkFuRY2ZLvy0zBr9yBLOViBzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا صبح قیامت بر ۲ مرداد لعنت!
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81770" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81769" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران
ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81768" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=Zg1cayOo7OYrT-vNMH4OPLNfmqBwFrRWkktS53DdpwZRNT0CHMoGHTEH6VUGiPcjpj0IlCcrVDyT16rmK5SICpRpaPRW-mA4hoB_S0RhaFZFnmDBkghgx4gIgxLXUpr_iXDq059mbiAfoNOfSNHIURAaqqi3gBgv2CVCj9Go_M0-WB8foDeCrwv1TX3FyzJb3J_9RcD4tOpXZo2okGqfvQzlt8jWRhzozSCSr_LX0mt5WTgMdcpRop2xLImq3FrMyJ2N1J2x6DOx01arPwKxp4VmK1Mf8hgPYG-8aLcP--R6O1Q90qFbE2OxP76OzyUT7hLdH2rbNqbDBeWcq4vi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=Zg1cayOo7OYrT-vNMH4OPLNfmqBwFrRWkktS53DdpwZRNT0CHMoGHTEH6VUGiPcjpj0IlCcrVDyT16rmK5SICpRpaPRW-mA4hoB_S0RhaFZFnmDBkghgx4gIgxLXUpr_iXDq059mbiAfoNOfSNHIURAaqqi3gBgv2CVCj9Go_M0-WB8foDeCrwv1TX3FyzJb3J_9RcD4tOpXZo2okGqfvQzlt8jWRhzozSCSr_LX0mt5WTgMdcpRop2xLImq3FrMyJ2N1J2x6DOx01arPwKxp4VmK1Mf8hgPYG-8aLcP--R6O1Q90qFbE2OxP76OzyUT7hLdH2rbNqbDBeWcq4vi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81767" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آدرویت داره میره سمت استعداد واقعیش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81766" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81765">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8a-CuXDr-47bN2susXe0KEx_X4MbjR46OfXJvEvTfzqRF5S-lJvHtdqlxSG81F3gBzG03mTrAvfSoaAZbyeCPc4aipTfQzahhij7F2mBuI7aMK0kYxU8NcHwSLhwgdElywipvVoQm0BCqtTAm2Fsu_mEQvg57zWxZbeoBjsVt74TE_NkhaZ7_FGVlnSV_Y5ccJq_YKqTZJJSEj4U8PV1ZNPZsWxhYAqQ4WJH9iuDedxyYdYxzocIcTCyLh9rxt42xHuH4guKTTFf0XwxNLqY70wcegl5KLdOAJqwvOPpl8IFDRKzWr9b-GmlwAKvBPPD482MfY_txxOde_q5AVDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بازگشت نقدی بت فوروارد تا ۱۰ درصد
🎲
🔥
با حداقل ۳ میلیون ریال شارژ حساب کاربری و سپس ثبت حداقل ۳ میلیون ریال پیش‌بینی ناموفق در میزهای کازینوی زنده، ماشین‌های اسلات و یا انفجار در طول هفته، بت‌فوروارد در هر هفته تا سقف ۱۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را به عنوان بونوس نقدی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/WEEK
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81765" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=EwmeswfXc7vOmE2RlLpRnvwwFpTBlYGNRhCvNWBMvzqaHfuk-ein57pveTqk--DmfMJmhVX19ZU_wWJoXWx1s6zkRKRfMCtdn12d2NWsidv5624zjhZwmzBR_4imB2RgY-ZLCrg4kaB1FKcLaF-9sNpDPZbGqwXxwXVsPpkTsSh-1FvVL9JVglnKadW7KMkNHjRqd1pmg05uKDedrzoqKwDV23iH6SaZJSex9GE9-u9mUBg-hoye1dWmo5hgwshaqV48VV7rKeuhVNiYOM8Rm8Lw6HQqPXbCzU0VOQbBaFklmYyPQGoZ37kwcdhPnsqsUqxd4E22FI9Ci6cLkOVNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=EwmeswfXc7vOmE2RlLpRnvwwFpTBlYGNRhCvNWBMvzqaHfuk-ein57pveTqk--DmfMJmhVX19ZU_wWJoXWx1s6zkRKRfMCtdn12d2NWsidv5624zjhZwmzBR_4imB2RgY-ZLCrg4kaB1FKcLaF-9sNpDPZbGqwXxwXVsPpkTsSh-1FvVL9JVglnKadW7KMkNHjRqd1pmg05uKDedrzoqKwDV23iH6SaZJSex9GE9-u9mUBg-hoye1dWmo5hgwshaqV48VV7rKeuhVNiYOM8Rm8Lw6HQqPXbCzU0VOQbBaFklmYyPQGoZ37kwcdhPnsqsUqxd4E22FI9Ci6cLkOVNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران اینترنشنال: پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81764" target="_blank">📅 10:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2wL7e2e0w6Bvg6jKwnp-Fy1MSY7RpV47G2468SmVwOK_XiKR9KwmKLQ1Wqe2LQN1ldZOHAYeOBw9eT9g6752Vfrbi0DB_O8c5K4ZdFGWM155vc4hcZxNmP4Y4KIekunPsABDPPAn74JkfaTUc2F9jYkUEhTKpC4bvTb1Dgx1zzScfwzOiWeOhjQWJEFecDkVVwBOVVuzPrNZVcCwfdaiketyxdJruhMJssFOd1llaJfpfl3dWurYljpPfOSvzrwk-NpT9fv80cYkq0gpuGc5BmhZitcjNIywSgqtVoU0J0ALRfIyetvoqgZKdVlYOd3tMhHzDHe1BtqGQXvxDq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اصلی اسرائیل است: «ما را دیوانه کردی»
‏ترامپ: «من حمله خواهم کرد. من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81763" target="_blank">📅 10:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDObaUmY5xcyDeKm5oq6bf-yo7J-aZLRU-i3HVfP832L1u1sQa9v2XttVEptIM47T_aGb2CauvxBx4l3q4-jzAfMTa_9YOpXnxfqVMQAzAv5RWbZxC9GzgckiviozDT0wqpIGEpDfVuGlu1SsPPRvkpOP7F2BGkpmQ-pNAjeU2eUl8PJdo8puTWvA132TZYidR4230bJFI5Zmt27eIcRZ23HUDLVBTMOLZCwpwcD1PxEaNBAmFS5_xP7Ar7vrEZkPQS1eJ1HIpqlwAEIYrA8zq8yC9oSUrv6_s_crPepCmb4wdOKfp_rA2-CAH08u31EP5djBdSsxbLFolztM1yrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81762" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=QBmPZ9qqWCawSDOSEIR2yuNE2DioMVjTKyFMR9qemZjoSd53F1CJdl9ZsHIyAw39uJzSU2bHewPBYsesX4ZlBLBBYEBCgV23yN8tyOn0uAB2iySiHEEOJ8qQ6_AiITPF_I9W7Uj4c3t5m2Xh_3cWR02q7RciUG1TFPuBJBLjvMlF4i6PW0F4jnIjL4947mHcdNIx1l6qIdXDvhy8i-UpsV1ax5EnYMWgRclW5aWx5eB1b4ux5oh5TovZJXYC3DFUqRH87i1H_4BTuphnTw5QGZkIGbPY4UgMwZsVQUPSzDKUwWvHSuG8IHX6_dD_HVGIs_xfo44740Fd-mhtxMXhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=QBmPZ9qqWCawSDOSEIR2yuNE2DioMVjTKyFMR9qemZjoSd53F1CJdl9ZsHIyAw39uJzSU2bHewPBYsesX4ZlBLBBYEBCgV23yN8tyOn0uAB2iySiHEEOJ8qQ6_AiITPF_I9W7Uj4c3t5m2Xh_3cWR02q7RciUG1TFPuBJBLjvMlF4i6PW0F4jnIjL4947mHcdNIx1l6qIdXDvhy8i-UpsV1ax5EnYMWgRclW5aWx5eB1b4ux5oh5TovZJXYC3DFUqRH87i1H_4BTuphnTw5QGZkIGbPY4UgMwZsVQUPSzDKUwWvHSuG8IHX6_dD_HVGIs_xfo44740Fd-mhtxMXhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81761" target="_blank">📅 09:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایران اینترنشنال:
پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81760" target="_blank">📅 07:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81759">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81759" target="_blank">📅 07:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81758">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81758" target="_blank">📅 05:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81757">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLnNC55u7phsQPyzf0z17GYb2tzBqQ9R0eUczOjaq4cqkb6w-35SRjJmGz52UD315Z11md294NxzQGlNEzRti2td4DWig4Mu_-NL1TAwUAqHsDDyrUkOTgliOjmBYH-g7rNo3iDnsuajln54kXGhlF4G8rjL4n7olrVHXpTpHlUxCbBfzjulzuUPb5hdeV1ddfnW3TRxCHfKMTXRG0j9SOZIM9yX3_ZG4qytTXGkfws2YArXIZDFb00PlYjyxd12ZKQxJz5Lz46GOJRp3htv2ZvjHlPOmMRPl4VWxOtXQZaMxWGy6bxaP-ZU08Dvy2QdGSRF5gnp7VFSsiaeK2eYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد. #بماند_به_یادگار  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81757" target="_blank">📅 05:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81756">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ مادرتو گاییدم تو که بزن نیستی فقط تایم خوابمونو بهم ریختی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81756" target="_blank">📅 03:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81755">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDqq2V-lEQnz1Y_Jgho4jYE-iBHJNyEqrbHu8iNXoY3UrhZGK0cfQNF_W1KXY43bWoe05d8j6YTIdGG-C-0W9A3hc-UApnALEcIMnQNqN0Uh3o8lMHmT5fJvthGNSZwbc96TY6ufxkvS7A8-nBgXO6l1sXuW_0kAoIA1Zw6PHoMSOxaAvHIDzZS9UWuYmUiTfiECLWI35HcEYXoJwUoi7DlDjtbitj0bGBfgz3Yp18b81HLu4_OT2GOgdqQMM3-nXTFp7zRET_FKdBNdEvyKhMb_b4EILL09SBi5tW76simg3EKPAhzO4Fd9Iw5_lbHpgRTzsmyH2_4oNjrg-J-ceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل کسی که تایم زیادی تو خونس خودش نمیخواد باهات ارتباط برقرار کنه اصلا که تو بخوای دوری کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81755" target="_blank">📅 02:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81754">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">محکم ببند درو، دیگه ماکان بند نیست که بهمون حس ناکافی بودن بده و بگه کار اشتباهیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81754" target="_blank">📅 02:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBARNR6ZWMgfTjsNH4gWQWmTFLFJ-MwVYE8PF-WaWbcXMJ9HcY_EmiGjSJGG5wgyJEtNJOAtP3mrbo-a9XL77LeZDIdb3EZlRTHjZb69_zRZSsDCXBxJx0rjHloRET6rrVKwx6Ozi6HIhGjkzf0bqGPaitFxrBe25mqU80ul2nrojWSdGMD0Tw_KF3C4OHVHoJu_XNUowSm7wnNCMsjBVlN3qbe3vSpJgEhMsYFIFbK4XSfmA2XLA2VxGRl1-fJrP9eB6G3BMXPGkdjQDgJPqhedwk695O_ddMw3LdPHjhdtU-N-akaVo-g8zY2C6kgtqAFnktwANxW5DEC_ZY1-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرا رسیدن اربعین حسینی رو به همه شیعیان دنیا تسلیت عرض میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81753" target="_blank">📅 01:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ستار هاشمی کیرم تو ناموست این چه نتیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81752" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b8952566.mp4?token=tFEBb85PysmvLHhC6GhmPkhe06zzg7dVHitYC67jQAicaqBj0BEWsN0_10vtg3lG0jBus7kO1Z1cAN5oVOoJMFW1QCGY4IOVcxBL41_dup3cfcY53r1IOAxI5o15IcdXFUVoumqzlYtPMUMSaJwIv1qLVOT6BofZ9_v9Evl9UHvDFvOK9tuIbx7i_Y1692Wb42KJqrJPam9bH9CsdZ2Cag-R4JzY3lboLD92b13s0RN3BGCiqB60y9YVHttOvOx01ToBL-phqK7xpy7eqx75Ef8YVxdew850rQGpb52mxF6RYTBJ612GhagdvYsYKVV_556E8fxeBithHN50HV6w7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b8952566.mp4?token=tFEBb85PysmvLHhC6GhmPkhe06zzg7dVHitYC67jQAicaqBj0BEWsN0_10vtg3lG0jBus7kO1Z1cAN5oVOoJMFW1QCGY4IOVcxBL41_dup3cfcY53r1IOAxI5o15IcdXFUVoumqzlYtPMUMSaJwIv1qLVOT6BofZ9_v9Evl9UHvDFvOK9tuIbx7i_Y1692Wb42KJqrJPam9bH9CsdZ2Cag-R4JzY3lboLD92b13s0RN3BGCiqB60y9YVHttOvOx01ToBL-phqK7xpy7eqx75Ef8YVxdew850rQGpb52mxF6RYTBJ612GhagdvYsYKVV_556E8fxeBithHN50HV6w7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آره خلاصه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81751" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=vnvzlMkz0KnOGcdFHh_6m2ZULk9RLutnWMZ8UxjTrXoMFBHnu8bTvv0PyuCS1w2BTkAznXBPXuVosJb-vUo9BfdgGB1FG4cJsnPgnlBIWyiB8ZdqZ29qSP7aFdNClmC6s3oOe-MFyIOJ7gWUF0U_qsAVU-AfTDyCL8OqRCti_ZNqMl3gNmg9kpjvJcd5QOcD_BaNM-fqmNCJvv_KcaJi2vVR3_bwRR2oYxmkr6Q0CunnXHC6ughJwUGAL_4gzvAlFAn-FlDm0nkr1xSfZ6krKZoseRc27YPeUPoLPvJdy2_DRbZF9_CHgow4x3kHOAwfHkNJFFDYQne2PDi8CxK7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=vnvzlMkz0KnOGcdFHh_6m2ZULk9RLutnWMZ8UxjTrXoMFBHnu8bTvv0PyuCS1w2BTkAznXBPXuVosJb-vUo9BfdgGB1FG4cJsnPgnlBIWyiB8ZdqZ29qSP7aFdNClmC6s3oOe-MFyIOJ7gWUF0U_qsAVU-AfTDyCL8OqRCti_ZNqMl3gNmg9kpjvJcd5QOcD_BaNM-fqmNCJvv_KcaJi2vVR3_bwRR2oYxmkr6Q0CunnXHC6ughJwUGAL_4gzvAlFAn-FlDm0nkr1xSfZ6krKZoseRc27YPeUPoLPvJdy2_DRbZF9_CHgow4x3kHOAwfHkNJFFDYQne2PDi8CxK7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81750" target="_blank">📅 23:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
الان میان میبرنم
ترامپ:
چمن مثل انسان‌هاست. آن هم زندگی دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81749" target="_blank">📅 22:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ امروز (
درحالی که دیروز گفته بود فردا با ایران مذاکره مستقیم داریم و تنگه باز می‌شه
): فردا تنگه کاملا باز می‌شه و بعدش هم در مورد هسته‌ای مذاکره می‌کنیم و همه‌چی به خوبی پیش می‌ره وگرنه خواهیم دید چگونه کیر خواهم شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81748" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81747" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81746" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Won6NZnXUwWyUMDRp6yUtVImsShUSH1kQI4Mqchhy3sAKIvmtQwLTb2Jbs0ZcEHJMkQuFANTqThswuZilWzC836FT5ZIvF92W5Oor0YZBxHypzuvVEJ2Fqx2Z9wBL6IAU_rEeFyqS45vEU6LwSf4bfxkg0B3pHN-4YBOLYUmdJKo6kbq3xcxux296uoehcVlWiFm2qdCbQq9vvk2llgizNpr2Ez5gbrT5B5oty-0eytuKjqHusPLWP3GB6XwPsa1KWYJL2NX2S7-Evpc4cgw7ssyEqPBgH0s4zXm3WO84BLeucbYZUJZyqsBw8hFY-ax2znqQquxY2ssfgis7hifZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که جانفدا اسم نوشتید نگاه کنید شاید بکارتون بیاد
مستند تفنگداران دریایی که با همکاری نتفلیکس و ارتش امریکا ساخته شده درمورد تمرینات
و
مانورهای
واقعی هستش.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81745" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqSftCXAF3H3EMAk1m7sAe7NMoiY6zxBpq2Wtj-pcl3zrE3Cg8Nl17jbgZGmjMLS8YJ7q8CHUxxdYLM-fSzNllYDmRJrUZLNvOw81XasxrjIS1N0ehGOVgzd4Vu2wKl6Y8Viynvey7rdQ4bHtor1K9Kz_BmroTSFbJWXDJJmgbsytE0hHBWTyRrszknuuXZTZSbC0JpKbB_nvqRMyQbixTZawuK1x_JmKhlRclSYaSpgDAV4ree1HXqoRiG5T7EbRCdYYLI8C3VrgzC4s4l7KiC58qWhLsVfOf3kyHmi6lczvpqjJueGjysiqHdksVfqNUhkEeRsbj54WM58HuPaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاحالا دقت کرده بودید اگه نقشه ایران رو برعکس کنید میشه صورت ترامپ؟
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81744" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-VxCELbhF2rnOharrenV6jOrdF8YbLxkKjC8yeMZ2YkDOURteirPY8fNuEMJR6Ll79qRpouQ5XNJsXMBRV9ib9IQ8G9zozqZFMgPVXyQJghzpPqgIltm37Q5M_0IFfX5T2ElOGnwp5Fj5JBQyLforvBjZhAakdt7PpSTLD7Eu9x3FzeE8-udsd7dRMTKx8wlzWvlkBYgEdn4LNSFdhXqLXUV2Hl-_VOcuKqZVT194mX97ujK8nWMf5vr3phUZ4UnFsLAn8gEK60tcFBm1nErPEheBdH172L9xpgLZeoa67oNp3YYnwKzqsoBfSQ1o0Oy5v8gXe2hfIt1wJY6gbDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی جدی می‌خواید بگید هنوز هیچکدومتون تاکتیکای بسیار هوشمندانه‌ای مثل «انتشار عکس مونث بی‌حجاب کنار صندوق» و «مجهول ضرب در ۳» رو به این میانجیگرای خوش تکنیک یاد ندادید که به این زحمتا نیوفتن؟
این بود رسم رفاقت و برادری؟
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81743" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnu3EJWBaVoo4ROkis_2_HMZSvEpMzEXYmWxz4ID7FcXXfCtyTO1NG7wfC1ziYy0M5bwxrdLLfupkyExXXdE37hWO0DehefL8pvPChVLk0G3QB97Sw53K0HipGmYc-_5mNfjKt3MP6ra9hGObvQIgS2A7VQ3e0iGa1tvUeFszh2OTGExGFHF7zIkK5T9JVNXSRIkEoJC6QbN56lvYGWpu1YIerUsdBntQwXsvwMJLM0dTWRyf2EaSSR5gvJALsTDw_OHkieBshAycM8C0EYtpqOkL2KHBqruPCRHrdzTW1xKbO5JIAT7baRQqSaaoPeCiGcVjfSv7KJAqnXnQAiF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد.
#بماند_به_یادگار
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81742" target="_blank">📅 20:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به ابر قهرمان های ترک میگن ترکمن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81741" target="_blank">📅 20:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMB4Q1ME-eSVjupFTkJQ2c4EOExd1KRSW2RxNkGriA7FSLMxQlcKK9ukBLoEaxSRNa-7BkyYF8fU5Pq4h375hsdXYIC7UKXLT9UahOimaFmoJ5yOZ7crrgZXsrvCR9IZLXry9TKa04mj4GIRkTFNAH2acbdLO7YO8bSdlvA7yMzMAke2KbCBlQLGL990vCCivbx6-OzxvFbPYCce8tT20qGwZFPgOzu1CG68uWUebQ2QrOHgWGWgrnEZXPv27ZlJQmHhpyC5Lg97J50a7E288mISxj1Dq_tuLsed2l5ACUvf8D4Lk1w9ZE2H83p5YFwNzAKYVLrJZmItgNr-K-ejYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.2  پ‌ن: بهم اعتماد کنید و فصل چهار به بعد ادامه ندید و ولش کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81740" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1mHj8G7rOJInGOxcWML9jMGUztxlfrClshFRjlMu0YT71eDp7f3a0J0qCMHJQZfDVD8B8saBb1nK0bVaN5-Pc6_BK5KwnldxnUIzhFFDVxLYLvpFxlbFzMHLZFs-65VOgIgXCbcA5E6yGXCacld7JYX23FzP5NiTW1uO9JKziz5pYLueSSbdCSh3baWTd3MmRnISFHZ8lotwDl5pJcmHJmhypTClPDElcneIDrdqUnbiAHx6FgA7ykYUETJnPebVINMU1wtH0Qe7QxS9vymnDh-_BsmLzTaFnimyY5s244AdVNsSGypV6BYwSS8lQKsiFYEgNO6rdHnu8DkNrcEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هری؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81738" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNM76l9towgLF-n-Trz0DIqPqbpeotwrnFeDAP-hAHjVAqbMwMLF8amEBKAxVPqWGU_kkY8a0lJ3EsaTyFTADUvptL6NrMbqQGioQevNoyyFnxmHXBqIVtzb1DKHfhQ9Y_OZ0ZZeu02OeryDOAUnfLmeHG3bNlHMCuwKZxu11ltqcqoxvBIpNVf_Md3C_y9DuxabjE_qpjjcUweKQMMiuAxeSfUeqdz5PHmeajKKDDCMPO2fDCyvM0GbS1YzQq9ZntyHQ426B4Ia7ybcm8d8lD_c7aMgwCg7S5WhQOsidg_WThKtcYVBaJoW5JefjqQhsOhtxEFkDERSwpRIgw7ctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای تعصبی رونالدو و مسی و رپفارس شروع کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81737" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحَسَ</strong></div>
<div class="tg-text">نشور سفید نمیشه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81736" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7_qPOxtRY1x9WU2YG5SWNkwt3Lwbf1fdWTP0oIPnSEKD5esRt1qfn82ow09dzJAxoHIzEpqrp8YZHitTSDzDOQAZyoWqZnPFcY0yQPKHmymipU5k-7bC6njfxyZNAEanB4rAld_EXYv4S8AoVycheHjrtPYP2XR8bXl4Y5AinEZNL56BK--fI2OeXgsCBCTusj4edEkQL_UQA14NtYVbnV4sK_EsQ7UCdtdRtxg8e9OlICFMc3bXG0dUdECKT7NY4SXr2gKqFgYe9jY-Zm1AgIwyc8xuZjAUd4AJhhHt5mhJsLgBn5r5pTNcCZFqBrCRU16OHf8amxJYc0ZLIKTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوس دختر وینی داره پتشو میشوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81735" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">-خانوم جورجینا ایا وکیلم شمارو به عقد کریستیانو دربیارم؟
+عروس رفته جام جهانی دامادو بیاره.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81733" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGf_MOgntfRR2wUkzg8wN8mtjiXkIvC5X3xKTYpmGKFrEKIpLv7ai4G4ACNUhwp93VC1BXuyzRGWnBufU4Q9fqfCDoWoDeJSu-K8a-CsBqs8hXtCK-RkFm3NW98X5WA3QB2xiN7fB4FKQ8e1pFzekZkfsJodd_XZ37DYBxlJG5XBSDxFgU2YZTrpsAEEOL2D2lp5o8IWW_UGh8KATTAMX4E5dur10y7hTfibcNJaPBaS7wMWtttAh3aqxQUuUrzQyTHg8Z5oLbeLUtKSuKyB_OJL-cZ4jYLadLvSVizttr0CtNSPhIoU4vvazBQ5I1Hvubq5oeW6zC1-M1zLIYb_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش هنوز انقلاب نشده ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81732" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خفه شید تلخون ترک داده</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81731" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه
پ.ن: خدا از دهنت بشنوه اینا باورشون شده قراره تنگه تبدیل به یه سلاح خطرناک تر از بمب اتم بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81730" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbb9r719G3gacjuM2byC8x9rJfFKVStsYSJ9KTuRwhMZrWWuTmCdOhwC8m8Z16U2mtDMcseXkzRJmYGoswcoqEzjDQx_fBM8EM3fKBaqcoCaN1osE-nMR93pDH-rD_ChmEXzu22NfP7bZ2BZxEDeHFflYO0oWhLBzEVzelVcdW-B3RKzQsuwnqJ9WQUadDhX9n6olD6lJn-v4OHyFC0WQxwPeyZBFU2xM361nxpDB2wj6lkflqMAQIfljMbN2ZkvSXTHZMsXy3yENiZDQgX3uuTYvUwPGP_XP9qAWTDr_0_Xsw0ZlF-XVYmOh5E48fVU5YtzhWih8rWvybKjNiZVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر دردناک بود و جانگداز
امیر و رهام از هم جدا شدن و گروه ماکان بند منحل شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81729" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPUoXRYPGh1go9T3O9DOqLrdf7ZrFe6CGO3cGyHhdNhMTzZ8pqt8-80TsXtz7LOjy5Dw0eJlj34jJI6qzCC1i5lDmJN4RyvAY-HX2_AhosOdV9cNgfMfrezivse56xaRvL36Xj1eMQbSjhg2dcV3-fuoHX9br0Fh0UlI0gvDAWi0bEmer2SrAeE91zL9ia39__6Iqgd-wDrHHMY6x-DAWHrBNytIH-PAyCYpvRExMOZjbDuJaDw4SoubeCRWN66HkI3djGmgacHA97TaonuiIoMAiG1p_Tt71TC1tnv5dhWJyiJp8eiMqr4mb4STxoMphXk1VwhsxVlZf9IqZW62jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترک چندوقت اخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81728" target="_blank">📅 15:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81727" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgG7g8QufPZE9oObpB_Lm90BBFAveHnBHF74QoPJzi-MevTFRhnHoh7fz0cGRPsMXohAM-NBLnR-RgK-00WkMnrOAJLIFChY2sPkn_0cGnoURUgvdiZIlcU7q5LoVbXuBMCEGA9YpzMfufiqwn8QDFBeOCxK2sqNq9Mr3YiQ5SHgwIPIc6jP4se6kWNSS2JpM_NwuuUZ_I_zJDfQjxs5Ue4P_5TaMCfbHnP6uV8aNbg7YvwvCLjTmBvjiyjSHbfQdoAVXV0pobvAubREiaIhfGzLc5sqZ1UPoPg0DGamWZXLmBhe47idcVKhe8rDNWM9iRd5ioVg1GL8VlMbYc0q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81725" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هرچی پیج تو اینستاگرام میبینم به دستور مقام قضایی بسته شده، وقتشه برا پیشگیری علی رو دوباره ادمین کنم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81724" target="_blank">📅 14:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so2gzd-XNVh4tZ6G6X7aj3tUSmJe7OAATIBf390fevPQ9jBmDeVzJTBP_mWOGtOCTesWlXphj85ytW93sssHQuB5768gY1lU5J7Yh6acLt7MhFUksEugi0xh13hrQqgJOtpTkPWJBo-4nKpa8UXozFJUaYSzQ4ewtoFR623bk_3a17hZcrK4qkZme0IKq6TCni8swL9ElV7Q1_YN4xLbC_io_JWhYK0ViuNteBNBoU7JG83BGM1wsWxrk6_DMqS5qmN1vGtjow2KGPQ7utdc_4Ww19zpvW8DpGYRRMeKV0au1K5rGCY_n-FALYnD9JOtQfIq3riabNXLycNjvkNLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا، حافظ ممبر های فان هیپ هاپ باش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81723" target="_blank">📅 14:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با این حجم از هواپیماهای باربری نظامی آمریکا که به خاورمیانه میان و می‌رن دوتا احتمال بیشتر وجود نداره:
یا دکتر عراقچی پخت و پز کرده، توافق خیلی وقته پشت پرده بسته شده و آمریکا داره تجهیزاتشو از منطقه خالی می‌کنه؛
یا اینکه دکتر عراقچی به معنای واقعی کلمه پخت و پز کرده و آمریکا داره اونقدر بمب برا مراسم بعد از مذاکرات انبار می‌کنه که قراره ازمون یه سری یاد و خاطره و چند تا کلیپ فرید کنزو تو آپارات باقی بمونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81722" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFVEdsdu3M6vYlaDMfvA7M_etpafdXu9ZJyhI9UZZnfOJy8cZQaGCRH0Md0Z4rAoq2yf4i6FCpXU5WIXvABsDYDSk521uayiynqft0iTGa2Ob43Q3wgtwnQX89D1vY_ZnSPI5-JNKHAwP1CT99QC-83DIBp8HWkVdxN6qXuIWcrr7CO918UTkmqkJ9QrbMGCptCAOONx_ZrVpAwgepJtvSp6kkQhyFqmkPdZZoR2U2IiFX__xALn6YzvSjpqFILe7iW5UDlaIrIX4G01FqALycFp7LIsRARpLmPVXKKWsLUjRH5vJsf6cSUVkQIpeOtQ2vmgc4YtZuI-btOg1-SK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره واقعا به چه حقارتی افتاده بنده خدا؛
اگه بچه خوبی بود و ایران می‌موند خیلی راحت می‌تونست مجوز یه کنسرت خیلی خفن آنلاین تو لایو اینستاگرامش رو با اسپانسری دوغ آلیس بگیره و برا هزار دلار بره هیئت علی ضیا کاتالوگ فیلیمو رو پر کنه نعره بزنه اییینهههه خووونواااادهههه رپفارسییییی.
جدی آینده خودشو رو نابود کرد این پسر.
💔
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81721" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسایی زورش به مذاکره کننده ها نمیرسه هی میاد فتوا میده که اینترنتو باید قطع کنیم، ولمان کن دیگر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81720" target="_blank">📅 11:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81719">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=PtAZlrvr3C80UVjCQGsWL6zF_Zin_TzF-L6HUH1yIx2K520SmOa4naZTNSAz5IjWyD_-h4rm33NLu_wJxvcWPmL07ZUe1l7dVov4EfYUBAfWZoEsaOfKp6p4D2uM1luesM8IWBGYFKuQ8pD7JJJGeDjiCWXChrBBTG3LXhzulDM6L8bRpBtG92wUf-nV_M5T2o7gbbvCK8d_8-Ik0MHMBh6uYq1WVjNOSJPLLbmC6fbKEw5BM8uWxAY3_NiyyOLaBNKg2wB9_4jNVUWQHZCLTqZuThT7My1BnEcbDMHVAwJQZXxDgZyXce1aY_XPHpWynhLVl44SKj9dyiSmH4Ghlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=PtAZlrvr3C80UVjCQGsWL6zF_Zin_TzF-L6HUH1yIx2K520SmOa4naZTNSAz5IjWyD_-h4rm33NLu_wJxvcWPmL07ZUe1l7dVov4EfYUBAfWZoEsaOfKp6p4D2uM1luesM8IWBGYFKuQ8pD7JJJGeDjiCWXChrBBTG3LXhzulDM6L8bRpBtG92wUf-nV_M5T2o7gbbvCK8d_8-Ik0MHMBh6uYq1WVjNOSJPLLbmC6fbKEw5BM8uWxAY3_NiyyOLaBNKg2wB9_4jNVUWQHZCLTqZuThT7My1BnEcbDMHVAwJQZXxDgZyXce1aY_XPHpWynhLVl44SKj9dyiSmH4Ghlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی فنات دارن اکسپلورمو تسخیر میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81719" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrZVlmHBS0suWhC5fI_WQXsGxNPX5_BBrWimzyLJXyE41BTEcKYalga2KEPlJUyAeq_iVCXV3HMO1svk0xt8BnOEYqy2SlefmeBbFOixafNynrL3Zgykp-RC9y_xC6AE7XIlBwsEBzBHjSc9EiSvIPcBoOk67m28113_7XnhYkibc-GtfuoI4i4dHf0b0qjkb1G3zzIUzwofVe1TJj7VDL_kl8wN_MRywRlMQj_d37SnPaZp_8Mvezg8FVgoTED_5OZGLDflem_k88PRC1vUnwk0lDNJfzGXVp_HGaF1aPZoYkb4qTQ02Rz8JkU9fwpuicLfP73FG0FpfJUJwMLo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگولیییی
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81718" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81717">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=jdQPuA-xT6vgs3l_HObc6wXFg1-fM720u7yAkp68AJv6kETv6tlIsvggBL1iEsWSDS9_K5WB57iY03latECOEUHmdiu6Z-YIT6y_O_bLjOMSKBrP76MJIg93XMqwZAzv3CTRDTs3-RNIK4P0O79HwKzKT8JolGVP9TcXybCY1xa21X6HcBjNqocZHeJeR2J5jIxIo1yIYsU03vNDzHoGsrgpaP08TGD2ZlMysiQeU6QNDg5IY59-ihF94sR9gGQrIhBikxn3yszCYgNy41dyKDd2_cq73USm-hRLig98qX5XeGKiHIYuN0hNy8jynefNhtlqXwSRchlYdQlM7e8Q3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=jdQPuA-xT6vgs3l_HObc6wXFg1-fM720u7yAkp68AJv6kETv6tlIsvggBL1iEsWSDS9_K5WB57iY03latECOEUHmdiu6Z-YIT6y_O_bLjOMSKBrP76MJIg93XMqwZAzv3CTRDTs3-RNIK4P0O79HwKzKT8JolGVP9TcXybCY1xa21X6HcBjNqocZHeJeR2J5jIxIo1yIYsU03vNDzHoGsrgpaP08TGD2ZlMysiQeU6QNDg5IY59-ihF94sR9gGQrIhBikxn3yszCYgNy41dyKDd2_cq73USm-hRLig98qX5XeGKiHIYuN0hNy8jynefNhtlqXwSRchlYdQlM7e8Q3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین علی گرامی، پدر تشریفات ایران گفت اول تعارف، لطفا بگو الان کی بهت تعارف کرده رپر شی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81717" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امید بهزاد و پویا صفوت، از معترضین دی ماه اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81715" target="_blank">📅 10:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ببینید ترامپ چه روانی ایه که لابی سیاسی یهودیا تو آمریکا هم نمیتونه کاریش کنه، رو اوردن به لابی کردن با کشورای عربی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81714" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: حمله‌ای که آمریکا برای ایران در نظر گرفته بود، می‌تونست بزرگ‌ترین حمله از زمان جنگ جهانی دوم باشه، اما متوقف شد. محمد بن‌سلمان ترجیح داده به‌جای حمله، توافق با ایران حاصل بشه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81713" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF_sfMi4kK0k0Hpo_PtHzeH4yYL3va6rwCeglIHQ1R4o4qJD6S2ePh3H15HTTM-yhUiLqUkKw_0d_VvpFtal04QJ_JrgD3wnCOyIH-G0YgNgx8YUYug5HTXEsbcHmim1zCCrbka5xeVx4f-y0vT8sgpcbZsbJpxHqZr7kfQP5suERV7hEnQqzQHWVkvZ4eUvHapDSjyzx4nbYegOTsH8gxariHP5drv4HCumVKwfoToATom30PAmBlxz8p6DJCxWgXtoI0aB-UcJF01N2-PG86pnvXCXdFiBcQA2B_8Ha3uFTRt7QmZWVBCBrGoGy-FgEMqrmKise4QgSfw4nwc6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینم کاخ سفید این پستو زده بیشتر تنو بدنم میلرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81712" target="_blank">📅 09:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8hgpReS3mrrKx3MvWSosrpa8Xkp5caDbKtdc7v0pxrYB8xb5Bn00s-3eX6V9FoeYfIYD4eYYTigotsDjBj_-wAojpEveORv-EFMIE4BprdL64pcccChwdXUeQU0TIAGut_arrqHRdLblrC7MNe8GlrfbCCayxqoxADcJQt-IyFCV9FZCd7Y3uZIk2pndQFxbUbE7eJN5htugMFg1G7JHEabg2A5-2mZdvhD7LCBX7A02HD__vtdgslEPxP5UWvBEgeR6Eoy0XtG1ViCzMRnlHH1BNOBjoItOfpdLxkKDC43Y8Xuy6Ta6LMnX6E0wigUTQazbZ_sAR1dXLhSFR_BIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام نه قطعیم لطفا آهنگ نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81711" target="_blank">📅 08:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فوررررررررری
آکسیوس: منابع نزدیک به کاخ سفید تایید کردند که تا دقایقی دیگر ترامپ دو نقطه را خواهد زد؛ پشم‌های زیربغل و خایه‌ش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81710" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/81709" target="_blank">📅 02:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عباس مگه صبح نگفتی تنگه بازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81708" target="_blank">📅 01:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81707" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx7_fx1FC_s5bq9C_jdJYYmZJEV2doNqjwgeKoobJyRkJc4L_yHIgYv40gCnB5YPnImzoFJOzsqclMy8cUYeLj1rmEf93puM16O8-rxtXaWS_E3JQ0WbpQA47cS5R8PvECGlHiO-x76QCbTU0ue0AcB0Bh4Q8GCcb_de1lf1fGD67nFfBtoaa98Jth6JD9QKxCiFJ1655_pdWOQET1Gn_cyl3b0hQtm31ywIGJr62syva5ASiSXUNrHNcD4ssxdtvFzCFJNdwi_jKYNFtNbkqCicRf8Dkpm-3jUjglAQfcO1qrRtMhondkVRksDHH0afk_Gg0mfIBeb1vpNL6B8n3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی کصکشکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/funhiphop/81706" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9FOP6nrWuDQSX18ue9spaUFGSh3II-DXeP3dOxtn5zTRtdvijCI6Noav7W5uyMtLGTtVOGonAJTlmGm5FuzLXijscBiHw9pI-E3fz-_0ZD_cHrUESo9Ig1dyq6QlzktebFHin5P9wLD_UEGfvsYOTpiJdoKbG47ycnZuL95pZgTPNO4iJe7OSUU-QM5upN7bL538dORyonJTw1_tbgY8UuCOb3ChziST9fwoySjZxNmgKi8RmprMY8Rjy35g4CAMtIAb5hcDt5H3_WvuPLCiL3MAucz4GVe5KhSt5IKbrzkNeuOEBTv8ymLgQ8m-dywgl2ihHbumDhljUOeqha6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید راجب اتفاقای دیروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/81705" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMTqgFpDS8heH8FCb7sP93TlLQpy25_SjRLCnbUvtCbPw_4tB9SBLuGUUU_GVgt1iFWuEVn5rN41LwlWTRNN7dN5rri71LvypvRGvNlYT4ufe72LvUNMjSOFK18atbioeO1VtFXjUHL2eBMpEAySkXTgHzs44ot9k2pg1PW-UKjpFpBAra4J9dzwBeVlHDeLWmbUSYc9N-G1a9S8zTZ_6sds4YpyR-ERAWLwTifVCngXXqshkzsAs00C7xcirdKtRGQSEAine_deORLrzJAFwVzJAh_f3T_48O_1i_sN9XegeBuP0u8Jeo8fyVW0cAj3K0s-Y1X3idxcIa3OEXXZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81704" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حماس خودش خلع سلاح رو قبول کرده امضا کرده، ایران بیانیه داده که نه توطئه در کار است ما نمیزاریم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81703" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klfEi3pJe-bmBPwX8la4uXONr37xVJ7N5zTtEoyozBhmCnha5vHshtDXGK7TCsX-x-GvJsPtEV6sYty63xEhUDdcxdJqTvByx1UMrcyCleKX0-n0oVsrAW4XqPvv50g2df942hukeF5IC2snmSTcbCN9p7V8b7FQo3aKe16RTXlc3ElIynhSiCfvsUBB8vzeEVV7OW_i80KN2EkaacXHsvcQkOa2Ers1vizHnQEKq_lr0PuYmoOhyducSOUfSRiap3Ucc2GzKO3NPVDt9GJ2Ws4W5l_gp6IEJZo8iA01CaQSVAbmag5mh6z8uRVLwvQa11E1kDgZRCjFtd8Sie8LcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی ناموسا ببین کاراتو
نيروي انتظامي تهران بزرگ امروز یه دختر پسره رو توی پارک با گزارشات همسایه دستگیر کردن! حالا میپرسید به چه علت ، چیکار این بدبختا داشتید؟ به این علت که هر روز این دختر پسر میومدن اینجا دختره به پاهاش کیک میمالیده و پسره پاهاشو می‌خورده و فیلم فوت فیتیش ضبط میکردن
همسایه ها هم دیدن و گزارش دادن به ماموران انتظامی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81702" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPJh8ELBhmbdMIfunD2GoQaWMaX5q5v09qSwWjC8jCLWzZ4qEZFZ_CpXuzNQN7N52JN997xEWmaI8dJfpWxLltV5tEc4dq06dicpOuueFrqfzhy9jJ4rKW_PlpkWDrn6J-rZoLPkJFc2aURhsBD1ClPQuvqJW6LhKe45TdwDNvMkYOwCrU_pZE-X86o7aMB9DRJ44_A-2epwg_dhDAavUME8ar88TfDJCtk3x1aSMuOV8pDM_cxNu-haToY45CXPvfI6YAofkVWbLSbuf7cx7aJxhQVjs6D_iXmyULC_F-3dkIkJaJwU1L9NxNadoYuO3Sqj1ITPZFoUlMx5RFINnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- زنان با قاعدگی بارداری زایمان و یائسگی دست و پنجه نرم میکنند  مردان با چه چیزی؟
+ رونالد ارائوخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81701" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل: علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81699" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل:
علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81698" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr12JgwFKezkrW8noGVTRgfZR4cYyRBJ8iKAG_cirQcLLeXpG_sH6wsaH5-ByTgzxRegSU0yhXdnqCHPCaFcwqPam5TR5bt3-Xm_OUIghOY8XHXco_cvIjux8lZTddKa8Oj7AjB_kAPX3G4tPPeXy8peUEYmOxOvhrc4GEXCGWz8oQM7jsaGUGTgTZV049gjRCeI0BaEPp2dgNQMbOtxer5q4_SDPNYpl6b_1SvVydHpN4sSMthCYgVhdpB2LOwNBc7Tw8LKWMZV2N5BMw3Ly3a39b8M-OOhz9Gf6WmiZkCmp9DOeO7Tcb197a7mQetdFpxFmjHQp2xYDcyvA2mQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاس زدناشون
😅
😅
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81697" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81696" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81695" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5iqbVnc-6R0EFdt4upgUwFtTUXWDCPB-Fsma35Ki7Q78qiljjXoYM4BL2TI3YtDy3lWBn1kioohT1JINbCXrq6nOSORwvTS1RYu_tC7Ps6xtOZqznNWeTOjPdYe5e6X2a74-ra4uc-V7jpahXu_Y864nRPl9OjhWQ46gb70sf3a2IIWHX-75N9e3M0PRbmYYgt5G763g0SzTMnmBk04l-UvP-HOo2Xho6utkDP7HSa7xDyubEHYY9dMg-y2w3jAy_BsfIhwHg1MCiv3Stftxq5dNSgoaBMibvrp2HDDarlrEHYTf14cWNqI_fUJJHPy35xXey9R9AVK86LGEYST4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
